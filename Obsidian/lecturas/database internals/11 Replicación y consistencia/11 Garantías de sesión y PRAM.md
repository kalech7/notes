---
title: "Database Internals — Capítulo 11 · Garantías de sesión y PRAM"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Garantías de sesión y PRAM

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

Una **sesión** es una secuencia lógica de operaciones de un cliente. Las garantías de sesión describen qué puede observar ese cliente aun si cambia de réplica. No prometen que todos los clientes vean el mismo estado al mismo tiempo.

El capítulo mantiene el supuesto de operaciones locales secuenciales. Cuando una llamada queda sin respuesta, no se sabe si surtió efecto: una garantía de sesión debe definirse con respecto al historial y al contexto que se conserva.

## Las cuatro garantías

| Garantía | Regla | Ejemplo propio de violación |
|---|---|---|
| Leer propias escrituras, *read-your-writes* | Las lecturas posteriores incorporan mis escrituras previas | Cambio mi avatar y la recarga muestra el antiguo |
| Lecturas monótonas | Una lectura posterior no pierde versiones que ya observé | Veo un pedido enviado y después vuelve a pendiente |
| Escrituras monótonas | Otros ven mis escrituras en el orden en que las produje | Actualizo «borrador» a «publicado» y luego vuelve el borrador tardío |
| Escrituras después de lecturas, *writes-follow-reads* | Mi escritura se ordena tras los cambios que observé antes | Respondo una publicación y mi respuesta llega sin ese antecedente |

En leer propias escrituras, «incorporar» no obliga a devolver exactamente el mismo valor si otro cambio posterior lo reemplazó. Se conserva la relación de versión. En lecturas monótonas, monótono tampoco equivale a número creciente: el saldo puede bajar por una operación nueva sin retroceder en historia.

## Cambiar de réplica

Ejemplo propio: A conoce versiones hasta `v8`, B sólo hasta `v5`. El cliente leyó `v8` en A y ahora llega a B. Para preservar lecturas monótonas, B debe ponerse al día, buscar otra fuente adecuada o no completar esa lectura aún. Devolver `v5` rápido viola la sesión.

Una implementación puede adjuntar al cliente un token de versión o contexto que resume lo observado y exigir que la réplica lo satisfaga. También puede fijar afinidad a una réplica, pero esa estrategia necesita tratar failover y no arregla por sí sola una réplica que pierda su estado. Son mecanismos ilustrativos, no un algoritmo de producto especificado por el capítulo.

## PRAM o FIFO

**PRAM**, *Pipelined RAM*, también llamado consistencia FIFO, conserva el orden de escrituras procedentes de cada proceso. Las de distintos orígenes pueden intercalarse de forma diferente para distintos lectores. Si Ana produce A1→A2 y Bruno produce B1→B2, un lector puede observar A1,A2,B1,B2 y otro B1,A1,B2,A2. Ambos preservan los dos órdenes locales.

El libro relaciona PRAM con combinar lecturas monótonas, escrituras monótonas y leer propias escrituras. La idea relevante para el estudio es conservar la secuencia de cada origen sin exigir el orden total común de consistencia secuencial. Esto no incorpora automáticamente la dependencia «leí algo de otro cliente y luego escribí»; **writes-follow-reads** cubre esa relación adicional.

## Qué cubre causalidad

Conservar contexto causal adecuado puede ofrecer las cuatro garantías de sesión. Pero decir «hay vectores en el almacenamiento» no garantiza esa experiencia si el cliente pierde contexto al cambiar de servidor. Hay que verificar la propiedad a través del camino de acceso completo.

Las garantías se cumplen para cada sesión; no establecen un único calendario entre sesiones independientes. Reiniciar la aplicación y abandonar la identidad/contexto puede iniciar una sesión distinta. La promesa de continuidad necesita definir qué persiste y durante cuánto tiempo.

> [!question]- ¿Leer mis escrituras evita que otro cliente lea datos viejos?
> No. Es una garantía respecto a mi sesión. Otra sesión puede tener una vista atrasada si el sistema no promete algo más fuerte.

**Referencia:** PDF 37–38 · impresas 233–234. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=37|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/10 Relojes vectoriales y conflictos|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/12 Consistencia eventual y convergencia|Siguiente]] →
