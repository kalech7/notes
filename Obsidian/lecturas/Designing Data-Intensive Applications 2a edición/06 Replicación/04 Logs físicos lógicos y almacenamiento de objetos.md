---
title: "DDIA — Logs físicos lógicos y almacenamiento de objetos"
created: 2026-09-29
capitulo: 6
tags:
  - lecturas/ddia
  - arquitectura/replicacion
---

# Logs físicos lógicos y almacenamiento de objetos

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|← Índice del capítulo 6]]

El seguidor necesita una descripción reproducible de los cambios. Esa descripción puede representar **instrucciones**, **modificaciones físicas** o **cambios lógicos en registros**. Elegirla afecta determinismo, compatibilidad entre versiones y posibilidades de integración.

## Replicar sentencias: repetir el trabajo original

En replicación basada en sentencias, el líder envía operaciones como `INSERT`, `UPDATE` o `DELETE` y cada seguidor las ejecuta. Parece simple y puede ser compacto: una instrucción que cambia mil filas puede ser menor que mil registros de cambio. Pero ejecutar el mismo texto no garantiza el mismo resultado.

```sql
UPDATE pedidos SET codigo = RANDOM() WHERE id = 'P42';
```

Es un ejemplo conceptual: el nombre de la función varía entre motores. Si cada réplica calcula su propio número aleatorio, obtiene valores distintos. Una función de hora puede divergir por el instante de ejecución. Triggers y funciones con efectos externos añaden más problemas: repetir una sentencia podría repetir una notificación o un cobro.

**Determinista** significa que, para el mismo estado y entrada, se obtiene el mismo resultado. Si la operación depende del estado previo, también importa el orden. Primero incrementar un contador y después leerlo no es equivalente a invertir esos pasos.

El líder puede sustituir algunas funciones variables por resultados calculados y enviar un orden común. Es la idea de replicar una máquina de estados: las réplicas ejecutan las mismas entradas deterministas en el mismo orden. El reto es controlar todas las fuentes de variación y efectos, no solo la función aleatoria visible.

## Replicar WAL: repetir cambios físicos

El **WAL**, o write-ahead log, registra cambios antes de modificar de forma definitiva las estructuras que permite recuperar. Ya lo estudiaste con B-trees en el capítulo 4. Si sus registros contienen lo necesario para reconstruir páginas e índices, el líder puede enviarlos y el seguidor reconstruir archivos equivalentes.

Es **replicación física** porque describe detalles del almacenamiento, como cambios en bloques y posiciones. Su ventaja es reutilizar una representación completa de recuperación. Su límite es el acoplamiento al formato físico: un seguidor con una versión incompatible del motor puede no comprender esos registros.

Actualizar software sin interrupción resulta más difícil si no pueden convivir versiones. Las restricciones concretas dependen del sistema y del salto de versión; «físico» no significa que cualquier actualización requiera siempre detener todo, pero sí que el formato interno pasa a ser parte del contrato.

## Replicar cambios de filas: describir el resultado lógico

Un **log lógico** describe operaciones sobre entidades del modelo de datos. Para insertar una fila necesita sus valores; para borrar, identificarla; para actualizar, identificarla y expresar los valores nuevos. Una transacción con varias filas necesita también una frontera que indique cuándo se confirma el conjunto.

```json
{"tabla":"pedidos","op":"update","id":"P42","cambios":{"estado":"pagado"}}
```

Este registro propio representa el significado del cambio, sin decir qué byte de qué página se modifica. Un motor puede almacenar la fila en una organización y el destino en otra. Eso facilita compatibilidad, pero no la regala: ambos deben acordar tipos, esquema, identificadores y semántica, como explica el capítulo 5.

El capítulo menciona el binlog lógico de MySQL y la decodificación del WAL de PostgreSQL. La representación usada para recuperar almacenamiento local y la usada para comunicar filas pueden ser diferentes aunque una se derive de la otra.

## CDC conecta la base con otros sistemas

**Change data capture**, o CDC, captura cambios para alimentar un almacén analítico, un índice de búsqueda o una cache. Un flujo lógico es más fácil de interpretar que modificaciones físicas. Por ejemplo, el cambio de estado de P42 podría actualizar un tablero analítico.

Una ampliación práctica: un consumidor que recibe eventos repetidos necesita procesamiento idempotente o deduplicación; un consumidor que ve solo una parte de una transacción debe saber si ya puede publicar el resultado. El log útil no reemplaza los contratos de evolución y entrega del capítulo 5.

| Representación | Qué reproduce | Ventaja | Riesgo principal |
|---|---|---|---|
| Sentencias | Operación original | Puede ser compacta | No determinismo, orden y efectos secundarios |
| WAL físico | Cambios de almacenamiento | Recuperación y réplica de archivos | Acoplamiento al motor y su versión |
| Log lógico | Filas y valores | Integración y menor dependencia física | Mantener esquema, semántica y fronteras transaccionales |

## Almacenamiento de objetos en la arquitectura

Las páginas 202–203 amplían el tema: un **object store** guarda objetos mediante una API, en vez de ofrecer exactamente las operaciones de un disco o un sistema de archivos POSIX. Puede conservar snapshots y logs, o participar directamente en las consultas de una base diseñada para ello.

El libro presenta almacenamiento por niveles: datos frecuentes en memoria o SSD y datos fríos en objetos; también arquitecturas que persisten allí todos los datos y utilizan discos locales solo como cache. «Sin disco» en ese contexto significa sin estado duradero dependiente del disco del nodo, no ausencia de almacenamiento físico en toda la infraestructura.

Los objetos pueden ofrecer replicación gestionada y escrituras condicionales. **CAS**, compare-and-set, permite publicar un cambio solo si el valor o versión previo coincide. Una base puede construir protocolos de publicación o liderazgo sobre esa operación. La operación primitiva no implementa por sí sola cualquier transacción: la base debe definir cómo coordina y publica sus objetos y metadatos.

Los costos incluyen mayor latencia, llamadas a API y necesidad de agrupar operaciones. Agrupar reduce llamadas, pero añade espera. Reescribir parte de un objeto grande puede requerir producir otro objeto. Montar un bucket con FUSE no demuestra compatibilidad con todas las garantías POSIX de las que depende un motor tradicional. Esta sección describe las arquitecturas del escaneo; no recomienda proveedores ni confirma precios actuales.

> [!question]- ¿Un log lógico siempre permite mezclar cualquier versión de software?
> No. Reduce el acoplamiento al formato físico, pero lectores y escritores todavía necesitan un contrato compatible de datos, esquema y transacciones.

> [!question]- Si guardas el WAL en objetos, ¿las escrituras dejan de necesitar un protocolo de confirmación?
> No. Debes definir cuándo el log está persistido, qué fallos tolera y cuándo respondes al cliente. Cambia el medio, no desaparece la obligación de precisar la garantía.

## Referencias

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=6|PDF 6 · impresa 202]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=7|PDF 7 · impresa 203]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=10|PDF 10 · impresa 206]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=11|PDF 11 · impresa 207]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=12|PDF 12 · impresa 208]]. Explicación basada en el escaneo; pedidos, cifras ilustrativas y ejercicios son elaboración propia.

---

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/03 Snapshots recuperación y failover|← Anterior]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/05 Retraso y lectura de tus propias escrituras|Siguiente →]]
