---
title: "Database Internals — Capítulo 11 · Consistencia eventual y convergencia"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Consistencia eventual y convergencia

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

Bajo **consistencia eventual**, los cambios pueden propagarse de forma asíncrona y las réplicas pueden divergir temporalmente. Si dejan de producirse actualizaciones para un dato y los cambios necesarios llegan y se reconcilian, las lecturas terminan coincidiendo con el estado resultante.

«Eventual» no fija un número de segundos ni garantiza que toda lectura intermedia sea nueva. Tampoco define por sí sola una regla correcta de reconciliación. El resultado final puede depender de una política de conflictos y no ser simplemente el último cambio según un reloj físico.

## Convergencia necesita condiciones

Ejemplo propio: A acepta una etiqueta roja y B acepta verde durante una partición. Al restaurar la comunicación, pueden fusionar mediante unión o elegir un valor mediante LWW. En ambos casos pueden converger, pero sólo la unión conserva ambas etiquetas. El contrato de convergencia no decide cuál semántica de negocio era deseada.

Si B nunca vuelve a comunicarse o un cambio se pierde de forma irrecuperable, no se cumplen las condiciones que permiten propagar y reconciliar todo. La palabra «eventual» no hace desaparecer esas obligaciones. En una aplicación que actualiza sin pausa, la definición basada en cesar escrituras no exige que exista un instante de igualdad absoluta entre todas las copias.

## Diferente de una cota de atraso

Una promesa «las lecturas tienen como máximo cinco segundos de atraso» es una cota adicional. La consistencia eventual sin esa condición no la proporciona. El capítulo no ofrece una distribución de tiempos de propagación ni métricas reales: no se debe convertir su explicación en un objetivo de latencia supuesto.

| Propiedad | Pregunta que contesta |
|---|---|
| Eventual | ¿Se igualan las réplicas cuando los cambios se entregan y se estabiliza el dato? |
| Leer propias escrituras | ¿Una sesión pierde sus cambios al leer? |
| Lecturas monótonas | ¿Una sesión vuelve a versiones anteriores? |
| Linealizabilidad | ¿Toda la historia respeta un orden atómico y la precedencia real? |

Un sistema puede combinar convergencia eventual y garantías de sesión. Convergencia no implica esas garantías por sí sola. Si un balanceador mueve al cliente de una réplica nueva a otra vieja, puede producir una regresión de lectura aunque todos terminen coincidiendo después.

## Política de resolución

LWW compara etiquetas ordenadas y descarta perdedores. Si se usan relojes físicos desajustados, una escritura realizada después puede tener una etiqueta menor. Usar un desempate determinista permite coincidir en un ganador, pero no devuelve los datos descartados.

Los vectores permiten reconocer cambios concurrentes y pedir reconciliación, pero necesitan una regla para terminar con un estado común. Los CRDTs dan esa regla dentro de tipos restringidos: diseñan la fusión para converger sin una decisión arbitraria del usuario ante cada intercambio.

> [!question]- ¿Una réplica que devuelve 0 y luego 1 ya prueba consistencia eventual?
> No. Ese fragmento de historial muestra una actualización. La garantía trata todas las réplicas y su convergencia bajo las condiciones declaradas, no una observación aislada.

**Referencia:** PDF 38–39 · impresas 234–235. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=38|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/11 Garantías de sesión y PRAM|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/13 N R W quórums y sus límites|Siguiente]] →
