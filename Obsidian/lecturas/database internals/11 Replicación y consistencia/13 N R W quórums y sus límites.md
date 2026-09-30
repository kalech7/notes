---
title: "Database Internals — Capítulo 11 · N R W quórums y sus límites"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# N R W quórums y sus límites

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

La **consistencia ajustable** configura cuántas réplicas intervienen en lecturas y confirmaciones. **N** es el número de réplicas del dato; **W**, cuántas deben reconocer una escritura para confirmarla; **R**, cuántas respuestas se requieren para una lectura. Son cantidades por operación y conjunto de réplicas, no necesariamente el número total de máquinas del clúster.

## Derivar la intersección

Si la escritura tiene un conjunto de W réplicas y la lectura consulta R de las mismas N, `R+W>N` obliga a que se solapen. Dos conjuntos disjuntos necesitarían R+W elementos diferentes y sólo hay N. Al menos `R+W−N` participantes están en ambos.

Con N=3,W=2,R=2, una escritura en {A,B} se cruza con cada lectura posible: {A,B}, {A,C} o {B,C}. En el escenario sencillo de una escritura completada, versiones comparables y datos conservados, al menos una respuesta incluye esa versión. La lectura todavía debe identificar y elegir o reconciliar correctamente el dato reciente.

| N | W | R | Intersección mínima | Fallas soportables para confirmar escritura / lectura |
|---:|---:|---:|---:|---|
| 3 | 1 | 3 | 1 | 2 / 0 |
| 3 | 3 | 1 | 1 | 0 / 2 |
| 3 | 2 | 2 | 1 | 1 / 1 |
| 5 | 3 | 3 | 1 | 2 / 2 |
| 3 | 1 | 1 | 0 | 2 / 2, sin intersección garantizada |

La tabla es un cálculo propio que supone nodos accesibles, mismo conjunto estable y sin obstáculos adicionales de protocolo. «Soportar» indica que quedan suficientes respuestas, no que cualquier historia concurrente sea linealizable.

## Mayoría y disponibilidad

Un **quórum mayoritario** tiene `floor(N/2)+1` participantes. Con `N=2f+1`, una mayoría necesita `f+1`, así que quedan suficientes nodos si fallan a lo sumo f. Con cinco réplicas, f=2 y hacen falta tres. Si sólo quedan dos, no se completa una operación que exige mayoría.

R y W no tienen por qué ser iguales. W=1,R=N facilita confirmar escrituras pero exige a todos para leer; W=N,R=1 desplaza la espera a la escritura. Subir los umbrales suele aumentar requisitos de disponibilidad y coordinación, pero la latencia exacta depende de los nodos contactados, almacenamiento y política del coordinador.

El capítulo recomienda enviar una escritura a N participantes aunque sólo se espere W confirmaciones. Si el coordinador es réplica, su aplicación local puede contar dentro de W: espera W−1 confirmaciones remotas, no reduce el umbral total. Una lectura puede lanzar solicitudes extra para que una respuesta lenta no determine por sí sola el tiempo; sólo cuentan respuestas válidas del conjunto requerido.

## Una escritura incompleta rompe monotonicidad

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 11/06 Quórum y escritura incompleta.png]]

A tiene versión 1 y B,C conservan versión 0 porque la escritura sólo alcanzó A. La lectura {A,B} puede seleccionar 1 y la siguiente {B,C} seleccionar 0. Ambas reúnen dos respuestas. La intersección de los dos grupos es B, pero B nunca recibió 1: el dato sólo pertenece a una escritura que no completó W. Es el problema explicado en la caja de la impresa 236.

Reparar sin bloquear después de devolver 1 no impide que la segunda lectura se adelante a la reparación. Una **reparación de lectura bloqueante** propaga la versión elegida a suficientes participantes antes de responder, de manera que lecturas posteriores tengan la intersección necesaria. El capítulo la menciona y remite su desarrollo al capítulo 12, ausente de este PDF.

## Lo que la fórmula no garantiza

> [!warning] Intersección no equivale a linealizabilidad
> `R+W>N` es una propiedad de conjuntos. Para convertirla en garantías de lectura se necesitan supuestos sobre versiones, persistencia, escrituras concurrentes y pendientes, selección de resultados, reparación y membresía. Quórums con réplicas sustitutas fuera del mismo conjunto tampoco heredan automáticamente la intersección. La regla simple del libro es útil para el caso básico, pero no prueba por sí sola un registro linealizable.

Con varias escrituras concurrentes, leer un nodo «que participó» no demuestra que la versión elegida respete el orden real de la historia. Y si todos guardan etiquetas físicas mal ordenadas, una política LWW puede elegir una versión cuya escritura no fue la última en tiempo real. El protocolo completo debe cerrar esas diferencias.

> [!question]- ¿N=4,W=2,R=2 garantiza solapamiento?
> No. {A,B} y {C,D} son conjuntos disjuntos. Hace falta R+W>4, no sólo R+W=4.

**Referencia:** PDF 39–40 · impresas 235–236. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=39|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/12 Consistencia eventual y convergencia|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/14 Réplicas testigo y reparación|Siguiente]] →
