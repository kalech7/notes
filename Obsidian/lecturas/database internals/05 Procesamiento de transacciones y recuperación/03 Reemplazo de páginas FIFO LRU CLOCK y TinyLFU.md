---
title: "Database Internals — Reemplazo de páginas: FIFO, LRU, CLOCK y TinyLFU"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/cache
---

# Reemplazo de páginas: FIFO, LRU, CLOCK y TinyLFU

[[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|← Índice del capítulo 5]]

Una caché llena debe decidir qué página perder. Como no conoce el futuro, usa señales del pasado. El objetivo es evitar expulsar algo que se pedirá enseguida, sin gastar más coordinación de la que se ahorra en I/O.

La política elige **candidatos**. El estado de la página decide si realmente se pueden desalojar: una página referenciada debe permanecer; una dirty necesita flush seguro. Una excelente predicción no permite reutilizar un frame que otro hilo todavía usa.

## FIFO: importa cuándo entró

**FIFO**, *first in, first out*, conserva una cola de llegada. La página que lleva más tiempo desde su carga sale primero. Volver a acceder a ella no modifica su antigüedad. La política es sencilla, pero puede expulsar la raíz del B-Tree precisamente porque entró antes y luego recibió muchísimas consultas.

## LRU: importa cuándo se usó por última vez

**LRU**, *least recently used*, expulsa la página cuyo último acceso está más lejos en el pasado. Si A vuelve a leerse, pasa a considerarse reciente. La intuición es la **localidad temporal**: algo utilizado hace poco suele volver a necesitarse.

Ejemplo propio con capacidad tres y accesos `A, B, C, A, D`:

| Momento | FIFO: más antigua → más nueva | LRU: menos reciente → más reciente |
|---|---|---|
| Después de A, B, C | A, B, C | A, B, C |
| Después de volver a A | A, B, C | B, C, A |
| Al entrar D | Expulsa A: B, C, D | Expulsa B: C, A, D |

LRU usa mejor esta señal, pero mantener el orden exacto cuesta trabajo por acceso. En un sistema concurrente, muchas lecturas que solo quieren consultar datos también deben modificar la estructura de reemplazo. El tráfico de metadatos y la sincronización pueden limitar su ventaja.

El capítulo menciona **2Q**, que distingue primeras visitas de reutilizaciones, y **LRU-K**, que conserva información de varios accesos. Ambos intentan separar una visita aislada de una recurrencia real, a cambio de más estado.

## CLOCK: segunda oportunidad con poco mantenimiento

CLOCK organiza los frames en un anillo y una posición que actúa como manecilla. En la variante didáctica de un bit, un acceso marca el bit en 1. Cuando la manecilla busca una víctima, un 1 se cambia a 0 y recibe otra oportunidad; un 0 hace candidata a la página. La exploración continúa hasta encontrar una que además pueda desalojarse.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/02-clock.png|1100]]

Los cuadros representan frames, y los bits recuerdan accesos recientes desde la última inspección. La flecha indica la siguiente posición a evaluar. Una marca de pin o referencia activa tiene una función distinta del bit: aunque una página tenga bit 0, no puede retirarse si sigue en uso. Poner el bit en 0 consume una segunda oportunidad; no prueba que la página nunca se volverá a leer.

Si la manecilla llega a A con bit 1, lo apaga y avanza. Si B también tiene 1, hace lo mismo. Si C tiene 0 y no está retenida, C es la candidata. Si C está dirty, aún necesita el flush compatible con WAL. CLOCK aproxima recencia sin reorganizar una lista en cada consulta; existen variantes con contadores en lugar de un único bit.

## LFU y TinyLFU: la frecuencia cambia la decisión

**LFU**, *least frequently used*, se interesa por cuántas veces se utiliza una página. Un historial ilimitado sería costoso y podría privilegiar para siempre páginas que fueron populares hace mucho tiempo. TinyLFU utiliza un resumen aproximado de frecuencias para tomar decisiones de admisión.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/03-tinylfu.png|1100]]

La zona de admisión ofrece una oportunidad inicial a páginas nuevas. El filtro compara la frecuencia estimada de la candidata con la de una víctima de la zona principal: una visita nueva no desplaza automáticamente a una página muy usada. Dentro de esa zona, probation contiene elementos menos protegidos y protected contiene elementos con reutilizaciones suficientes. Las flechas entre ambas representan promociones y degradaciones; la salida indica una expulsión.

La estructura de tres colas expuesta por el capítulo corresponde al esquema **W-TinyLFU**: una ventana de admisión combinada con el filtro TinyLFU y una región principal segmentada. Esta precisión complementaria se cotejó con el [diseño oficial de Caffeine](https://github.com/ben-manes/caffeine/wiki/Design). El filtro de frecuencia y las colas cumplen tareas diferentes: uno decide qué merece conservarse y las otras organizan los elementos residentes. No hace falta preservar una lista completa de todos los accesos para estimar frecuencia.

## Más memoria no arregla cualquier política

La **anomalía de Bélády** muestra que, con ciertas políticas como FIFO, aumentar los frames puede aumentar los fallos de página. No significa que más RAM empeore siempre ni que LRU exacto tenga esta anomalía. Significa que también importa cómo cambia la elección de víctimas al cambiar la capacidad.

El capítulo menciona esta anomalía sin dar la siguiente secuencia. La demostración propia está en el laboratorio: `1,2,3,4,1,2,5,1,2,3,4,5` produce nueve misses con tres frames FIFO y diez con cuatro. Se calcula recorriendo toda la cola; no se deduce de mirar únicamente el estado final.

| Política | Señal principal | Ventaja | Riesgo o costo |
|---|---|---|---|
| FIFO | Orden de carga | Poco mantenimiento | Ignora hits posteriores |
| LRU | Último uso | Aprovecha recencia | Actualizaciones y contención de metadatos |
| CLOCK | Bit o contador y manecilla | Aproximación de costo moderado | Necesita recorrer candidatos |
| TinyLFU con región segmentada | Frecuencia aproximada y reutilización | Resiste mejor admisiones poco útiles | Más componentes y estimación imperfecta |

No hay una ganadora universal. Un gran scan y una carga de pequeñas búsquedas repetidas presentan señales diferentes. También cambian el costo de sincronización, el tamaño de páginas y la proporción dirty. La elección debe juzgarse por el trabajo total evitado y agregado.

> [!question]- ¿Por qué FIFO y LRU eligen víctimas distintas después de A, B, C, A?
> FIFO recuerda que A entró primero. LRU recuerda que A se usó por última vez después de B y C. Las políticas no están midiendo la misma propiedad.

> [!question]- ¿CLOCK tiene que buscar siempre un bit 0 en una sola vuelta?
> No. Puede dar segundas oportunidades, encontrar frames retenidos o coincidir con accesos concurrentes. Si todos están pinned, se necesita liberar referencias; no basta con seguir girando indefinidamente.

**Fuente:** PDF 7–10 · impresas 85–88 · figuras 5-2 y 5-3. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=7|Políticas de reemplazo y admisión]].

---

← [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/02 Caché de páginas y gestión de buffers|Anterior]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/04 WAL checkpoints y registros de recuperación|Siguiente →]]
