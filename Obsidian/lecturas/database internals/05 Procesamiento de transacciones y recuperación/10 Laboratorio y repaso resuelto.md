---
title: "Database Internals — Laboratorio y repaso resuelto"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/recovery
---

# Laboratorio y repaso resuelto

[[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|← Índice del capítulo 5]]

Este laboratorio reúne experimentos propios basados en los mecanismos del capítulo. Las simulaciones son pequeñas para que cada transición sea comprobable. No representan el código de un DBMS, no escriben páginas reales y no simulan errores de hardware.

## 1. Bélády: recorrer FIFO sin saltarse los hits

La caché empieza vacía. Usa la secuencia `1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5`. El frente de cada cola es la página más antigua. **Un hit FIFO no cambia el orden.**

| Paso | Acceso | Cola de 3 frames | Resultado | Cola de 4 frames | Resultado |
|---:|---:|---|---|---|---|
| 1 | 1 | 1 | Miss | 1 | Miss |
| 2 | 2 | 1,2 | Miss | 1,2 | Miss |
| 3 | 3 | 1,2,3 | Miss | 1,2,3 | Miss |
| 4 | 4 | 2,3,4 | Miss | 1,2,3,4 | Miss |
| 5 | 1 | 3,4,1 | Miss | 1,2,3,4 | Hit |
| 6 | 2 | 4,1,2 | Miss | 1,2,3,4 | Hit |
| 7 | 5 | 1,2,5 | Miss | 2,3,4,5 | Miss |
| 8 | 1 | 1,2,5 | Hit | 3,4,5,1 | Miss |
| 9 | 2 | 1,2,5 | Hit | 4,5,1,2 | Miss |
| 10 | 3 | 2,5,3 | Miss | 5,1,2,3 | Miss |
| 11 | 4 | 5,3,4 | Miss | 1,2,3,4 | Miss |
| 12 | 5 | 5,3,4 | Hit | 2,3,4,5 | Miss |

Con tres frames hay nueve misses. Con cuatro hay diez. Las colas no mantienen una inclusión estable entre ambas capacidades; en el paso 7, la cola de cuatro ya perdió 1 y la de tres lo conserva. Ese cambio explica los fallos posteriores.

El mismo script da diez misses LRU con tres frames y ocho con cuatro. No demuestra que LRU gane siempre a FIFO: en este ejemplo concreto, con tres frames FIFO tiene un miss menos. Sí permite distinguir una comparación entre políticas de una comparación entre capacidades de la misma política.

## 2. Clasificar cuatro situaciones antes de ejecutar recuperación

Parte de `X=10`. Para cada caso, decide si hay un efecto que falta o uno que sobra:

| Estado al caer | ¿Hay commit durable? | Qué debe quedar | Trabajo necesario en el modelo |
|---|---|---:|---|
| Disco 10, RAM había pasado a 15, WAL del cambio y commit durables | Sí | 15 | Redo del efecto ausente |
| Disco 15, cambio en WAL durable, transacción seguía activa | No | 10 | Undo del efecto incompleto |
| Disco 15, WAL y commit durables | Sí | 15 | No repetir el efecto ya instalado |
| Disco 10, transacción activa, sin efecto durable en datos | No | 10 | ARIES puede repetir historia registrada y después compensar |

El último caso enseña por qué el estado final no determina por sí solo cuántas fases ejecuta el algoritmo. Redo y undo pueden realizar trabajo cuyo resultado neto devuelve el estado inicial. La existencia de commit durable y el estado de las páginas orientan el protocolo.

> [!question]- ¿Qué pasa si el archivo de datos contiene 15 pero el WAL correspondiente jamás se hizo durable?
> Se violó la regla write-ahead. La recuperación perdió la evidencia que necesita para identificar, repetir o revertir correctamente ese cambio. No se arregla suponiendo que 15 estaba confirmado.

## 3. Recuperar una transferencia parcial

A comienza en 100 y B en 50. T1 transfiere 30. WAL contiene cambios de A y B, y un commit durable. Solo A se escribió: el disco tiene `A=70`, `B=50`.

La información de análisis clasifica T1 como confirmada. Redo conserva el efecto ya instalado en A e instala `B=80`. Undo no revierte T1. El total final vuelve a ser `70+80=150`.

Ahora cambia una sola premisa: no hay commit durable de T1. Bajo el ejemplo ARIES, redo reconstruye la historia y undo retira ambos cambios. El final correcto es `A=100`, `B=50`. La misma pareja de páginas puede requerir una reparación distinta porque el log contiene una decisión distinta.

## 4. Write skew: dibujar dependencias en lugar de buscar una fila pisada

Ana y Bruno están disponibles y debe quedar al menos uno en guardia. Ambas transacciones leen el mismo estado, y cada una cambia solamente su propia fila a «no».

- La decisión de Ana depende de que Bruno siga disponible, pero Bruno modifica ese dato: dependencia T_Ana → T_Bruno.
- La decisión de Bruno depende de que Ana siga disponible, pero Ana modifica ese dato: dependencia T_Bruno → T_Ana.

Las dependencias requieren simultáneamente ambos órdenes. El ciclo explica por qué no existe un orden serial que acepte las dos salidas con esa comprobación. El resultado no puede justificarse diciendo que las escrituras fueron sobre filas diferentes.

Como ejercicio de diseño, una garantía serializable que controla estas dependencias debe impedir que ambas confirmen esa historia. Otra estrategia propia sería coordinar explícitamente el recurso que representa la guardia, usando un protocolo cuya comprobación se haga sobre información válida después de adquirir su protección. Cambiar solamente el texto de la restricción no resuelve el intercalado.

## 5. Distinguir un grafo de espera de uno de serialización

En el experimento anterior hay un ciclo de **dependencias de datos**. Las transacciones podrían haber terminado sin esperar ninguna a la otra; el problema es que ambas confirmaron una historia inválida.

En un deadlock, T1 posee el bloqueo de A y espera B; T2 posee B y espera A. El ciclo del **grafo de espera** significa que no pueden progresar. Abortar una víctima, deshacer su trabajo y liberar bloqueos permite continuar a la otra.

Un ciclo de dependencias y un ciclo de espera utilizan dibujos parecidos, pero sus flechas tienen significados distintos. El primero analiza equivalencia serial. El segundo analiza bloqueo de progreso. El script usa la misma detección matemática de ciclos sobre grafos distintos; no los considera el mismo fenómeno.

## 6. Predecir una búsqueda durante un split B-link

La ruta antigua del padre cubría `(0,100]`. Una hoja se divide en `(0,40]` y `(40,100]`. El padre todavía apunta a la hoja izquierda para todo el rango original. Las high keys son límites superiores inclusivos en este ejemplo.

Una búsqueda de 75 baja por la ruta antigua. La hoja izquierda tiene high key 40. Como `75 > 40`, la búsqueda sigue el enlace derecho y encuentra 75 en la hoja nueva. Una búsqueda de 40 permanece en la izquierda, porque 40 está incluido en su rango.

> [!question]- ¿Qué pasaría si se publicara la high key 40 antes de que el enlace derecho fuera utilizable?
> Un lector podría detectar que 75 pertenece a la derecha y no tener una ruta válida para alcanzarlo. El protocolo debe publicar de forma coordinada metadatos, enlace y contenido, protegidos por los latches correspondientes. El ejemplo ilustra un estado intermedio válido, no cualquier orden de actualización.

## Ejecutar y modificar los experimentos

El archivo [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/laboratorio_capitulo_05.py|laboratorio_capitulo_05.py]] utiliza solo Python estándar. Desde esta carpeta se ejecuta con:

```bash
python3 laboratorio_capitulo_05.py
```

Produce la traza FIFO, compara FIFO/LRU y detecta ciclos en un ejemplo de conflictos y dos grafos de espera. El análisis de conflictos solo modela lecturas y escrituras de registros exactos; no es un validador de MVCC ni de consultas por rangos.

Predice el resultado antes de cambiar la secuencia. Después compara la cola de víctimas, no solo el conteo. En los grafos, quitar una arista del ciclo deja un orden posible; añadir una dependencia de regreso puede volverlo imposible.

## Repaso resuelto

> [!question]- ¿Dirty significa no confirmado?
> No. Dirty compara memoria y disco. Una página puede contener efectos confirmados todavía no escritos o efectos de transacciones activas, según el protocolo. Commit y dirty pertenecen a dimensiones distintas.

> [!question]- ¿Pinning sustituye un latch?
> No. Pinning impide reutilizar el frame mientras deba permanecer residente. Un latch coordina el acceso físico a su contenido o estructura. Mantener una página en RAM no estabiliza sus bytes frente a otro hilo.

> [!question]- ¿No-force elimina la necesidad de sincronizar el log?
> No. Permite diferir páginas de datos; el WAL necesario y la decisión de commit deben hacerse durables bajo la garantía que explica el capítulo.

> [!question]- ¿MVCC es un nivel de aislamiento?
> No. Es una técnica que mantiene varias versiones. La política de visibilidad y coordinación determina qué nivel ofrece y qué anomalías excluye.

> [!question]- ¿Por qué 2PL básico no es sinónimo de mantener todos los bloqueos hasta commit?
> Porque sus dos fases prohíben adquirir nuevos bloqueos después de empezar a soltarlos. La retención hasta terminar es una condición adicional de variantes estrictas o rigurosas según qué bloqueos se retengan.

> [!question]- ¿Un checkpoint confirma lo que estaba activo?
> No. Registra información de recuperación. La decisión de cada transacción sigue dependiendo de su protocolo de commit o abort.

> [!question]- ¿Por qué los cambios del B-Tree necesitan tanto latches como recuperación?
> Los latches coordinan hilos mientras viven. Recuperación conserva o reconstruye un estado válido después de perder el proceso. Una garantía no reemplaza a la otra.

Los conceptos de estas prácticas proceden del capítulo; secuencias, código y casos adicionales son elaboración propia. Referencias principales: PDF 7–15 · impresas 85–93 para caché y recuperación; PDF 16–30 · impresas 94–108 para concurrencia. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=7|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/09 Latches y concurrencia en B-Trees|Anterior]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Siguiente →]]
