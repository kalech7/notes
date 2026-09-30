---
title: "Database Internals — Capítulo 11 · Réplicas testigo y reparación"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Réplicas testigo y reparación

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

Una réplica **completa** conserva el dato. Una réplica **testigo**, *witness*, conserva normalmente un registro o metadatos que indican que una escritura ocurrió. El capítulo propone usarlas para reducir el costo de almacenar todas las copias completas mientras siguen participando en quórums.

Un registro de ocurrencia no contiene necesariamente el valor. Conocer que existe `v9` no permite reconstruir su contenido si ninguna copia accesible lo conserva. La idea requiere un protocolo que mantenga datos suficientes y permita que un testigo almacene temporalmente el contenido cuando hace falta.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 11/07 Réplicas testigo.png]]

La primera fila presenta dos copias y un testigo. En la segunda, 2c no responde y 3w retiene el dato nuevo para que la escritura no dependa de una sola copia. En la última, 2c ya fue actualizado y el testigo puede conservar sólo el registro otra vez. El esquema reformula el ejemplo [1c,2c,3w] de la impresa 237.

## Los tres grupos de lectura

Supongamos que el nuevo dato está en 1c y temporalmente en 3w; 2c se recuperó con una versión vieja. La mayoría es dos:

| Participantes accesibles | Fuente del nuevo valor | Acción necesaria |
|---|---|---|
| {1c,2c} | 1c | Actualizar 2c según reparación |
| {1c,3w} | 1c y/o dato temporal de 3w | Conservar la versión nueva |
| {2c,3w} | Dato temporal de 3w | Traer 2c al día antes de descartar ese dato |

Si en el último grupo 3w sólo tuviera metadatos y el valor existiera únicamente en 1c, inaccesible, no se podría servir el valor nuevo. Ese contraejemplo explica por qué el payload temporal forma parte de la garantía y por qué «tener votos» no siempre significa «tener datos».

## Condiciones de la propuesta

El libro expresa la comparación de disponibilidad con n copias y m testigos bajo dos reglas: lecturas/escrituras usan mayorías y cada quórum contiene al menos una copia. También necesita conservar las actualizaciones en copias o testigos durante fallas y reparar al recuperarse.

Ejemplo propio de configuración: con tres copias y dos testigos, cualquier mayoría de tres incluye al menos una copia porque sólo hay dos testigos. Con una copia y cuatro testigos, una mayoría de tres puede formarse sin ninguna copia; la segunda regla no se obtiene automáticamente. Restringir quórums a incluir esa única copia hace que su caída impida progresar, de modo que no se puede afirmar disponibilidad idéntica a cinco copias completas sin condiciones adicionales.

## Reparar antes de liberar datos

La transición de testigo con dato a testigo con metadatos debe ocurrir después de asegurar que el dato queda protegido según los invariantes del protocolo. Borrar contenido sólo porque «el nodo volvió» puede perder la última versión: primero hay que llevarlo al día y confirmar la protección requerida.

Los testigos también consumen almacenamiento y tráfico. La propuesta reduce copias de contenido en operación normal; no vuelve gratuito el sistema y necesita espacio temporal cuando hay fallas. El capítulo cita diseños de Spanner y Cassandra como ejemplos de ideas relacionadas; no demuestra que todos los productos con «witness» utilicen exactamente este protocolo.

> [!question]- ¿Puede un testigo responder una lectura del valor usando sólo su voto?
> No. Su registro puede demostrar la existencia o versión de un cambio, pero para devolver el contenido necesita que éste esté accesible en una copia o almacenado temporalmente por el protocolo.

**Referencia:** PDF 40–41 · impresas 236–237. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=40|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/13 N R W quórums y sus límites|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/15 CRDTs contadores registros y conjuntos|Siguiente]] →
