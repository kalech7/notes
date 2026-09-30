---
title: "Database Internals — Capítulo 11 · Replicar para tolerar fallas"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Replicar para tolerar fallas

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

Replicar consiste en conservar varias copias de los mismos datos. La **tolerancia a fallas** es la capacidad de continuar cumpliendo el comportamiento prometido cuando un componente falla. La primera ayuda a la segunda porque permite reemplazar una máquina perdida, pero disponer de copias no especifica por sí solo qué versión deberá devolver una lectura.

El capítulo construye precisamente esa especificación. Un **modelo de consistencia** dice qué observaciones son válidas cuando las copias se actualizan a velocidades diferentes y varios clientes actúan a la vez. Sin ese contrato, «la escritura funcionó» puede significar desde «un servidor la aceptó» hasta «ninguna lectura posterior podrá devolver un estado anterior».

## Redundancia y recuperación

Un **punto único de falla** es un componente cuya pérdida detiene una función necesaria del sistema. En una base con un único primario, las réplicas permiten promover una nueva autoridad cuando el primario falla. La promoción necesita conservar el orden y controlar qué nodo tiene permiso para escribir. Un sistema que consulta varios participantes puede conservar disponibilidad mediante respuestas suficientes, sin promover explícitamente un primario para cada operación.

Ambas organizaciones tienen trabajo adicional: replicar cambios, detectar faltantes y recuperar nodos. Tres copias colocadas en un único centro de datos siguen siendo vulnerables a la pérdida de ese centro. La **georreplicación** distribuye las copias entre ubicaciones para cubrir fallas de mayor alcance y acercar lecturas a los clientes. La distancia también encarece coordinar escrituras que necesitan respuestas de varios sitios.

## Tres momentos diferentes

Conviene separar **escritura**, **actualización de réplica** y **lectura**. El servidor puede confirmar la escritura a Ana antes de que la réplica usada por Bruno reciba el cambio. Esa implementación evita esperar a Bruno, pero debe especificar si Bruno puede obtener el dato anterior. La respuesta depende del contrato y del instante en que se inició la lectura.

Ejemplo propio: A acepta `dirección = Quito`, responde a Ana y B todavía conserva `dirección = Cuenca`. Si Ana recarga su perfil mediante B, puede parecer que su cambio se perdió aunque la propagación siga pendiente. La garantía de leer las propias escrituras controla esa experiencia; la linealizabilidad añade obligaciones frente a todos los clientes.

| Decisión | Beneficio posible | Obligación adicional |
|---|---|---|
| Confirmar antes de propagar a todas las copias | Menor espera | Definir visibilidad y recuperar faltantes |
| Esperar autoridad o participantes suficientes | Orden más fuerte | Poder bloquear cuando faltan respuestas |
| Mantener copias cerca del cliente | Menor recorrido de lectura | Tratar retrasos y conflictos entre sitios |

El libro presenta actualizar copias atómicamente como un problema estrechamente relacionado con consenso. La precisión práctica es que «tener muchas copias» no garantiza una única historia: hace falta un protocolo que decida qué operaciones se aceptan y en qué orden. Los capítulos posteriores estudian protocolos; aquí se define qué resultado deben ofrecer.

> [!question]- ¿Replicar implica que todos los nodos devuelven inmediatamente lo mismo?
> No. La replicación define copias y propagación. La consistencia define las diferencias permitidas y cuándo deben desaparecer. Un sistema puede conservar varias copias y aun servir datos atrasados.

**Referencia:** PDF 19–20 · impresas 215–216. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=19|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/02 CAP PACELC y sus límites|Siguiente]] →
