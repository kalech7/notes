---
title: "Capítulo 7 · Cuatro formas de acoplamiento"
created: 2026-09-28
capitulo: 7
orden: 3
tags:
  - lecturas/software-architecture
  - arquitectura/quanta
---

# Cuatro formas de acoplamiento

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Capítulo 7 · Alcance y quanta]] · Nota 3 de 7

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, segunda edición, capítulo 7. Fuente local: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Las páginas PDF se cuentan desde el archivo suministrado; la impresa aparece en el libro. «Elaboración» y «ampliación didáctica» identifican material propio.

**Objetivo:** distinguir la relación impuesta por el negocio de la relación introducida por el diseño, y el cableado de la interacción en ejecución.

## Cuatro términos que responden preguntas diferentes

**Libro — PDF pp. 4–5, impresas 98–99.** El texto introduce cuatro formas de hablar de acoplamiento. Conviene leerlas como perspectivas complementarias: no son cuatro cajas mutuamente excluyentes en las que toda dependencia deba caer una sola vez.

| Perspectiva | Pregunta | Ejemplo del capítulo o explicación |
|---|---|---|
| **Semántico** | ¿Qué relaciones existen porque el problema del negocio es así? | Pedidos, inventario, catálogo, clientes y ventas están relacionados por el dominio. |
| **De implementación** | ¿Cómo elegimos materializar esas relaciones? | Una base común o varias; un monolito o una solución distribuida. |
| **Estático** | ¿Qué dependencias forman el cableado necesario? | Dos servicios dependen del mismo componente de direcciones o de la misma base. |
| **Dinámico** | ¿Cómo interactúan los participantes mientras realizan el trabajo? | Un servicio llama a otro, espera respuesta o publica un mensaje. |

La regla intuitiva del libro es considerar acopladas dos cosas cuando cambiar una puede romper la otra. Se trata de investigar posibles efectos de propagación, no de decretar que toda relación es perjudicial.

## El acoplamiento semántico no desaparece distribuyendo procesos

Un pedido reserva existencias porque el negocio lo requiere. Separar Pedidos e Inventario en servidores diferentes cambia el modo de interacción, pero no elimina esa relación. Si el negocio añade reservas temporales, ambos modelos podrían necesitar ajustes aunque sus interfaces estén bien diseñadas.

No existe un patrón que impida que cualquier cambio fundamental del dominio afecte a su solución. Un diseño útil hace esos cambios comprensibles y localiza lo localizable; no promete inmunidad a nuevas reglas del problema.

## El de implementación sí incorpora decisiones del equipo

Ante el mismo problema, un equipo puede usar una tabla compartida, una API explícita o mensajes. La elección modifica cómo se propagan los cambios, cómo se despliega y qué garantías pueden ofrecerse. Aquí aparecen compromisos de arquitectura: reducir cierta dependencia puede aumentar la complejidad de coordinación o de consistencia.

**Ejemplo didáctico:** un servicio necesita conocer una dirección. Compartir una biblioteca que fija un modelo de direcciones crea una dependencia distinta de consumir un contrato versionado. Ninguna etiqueta garantiza independencia: lo que importa es qué cambios son compatibles y quién debe coordinarse cuando no lo son.

## Estático no significa simplemente «en compilación»

En el uso del capítulo, el cableado incluye dependencias arquitectónicas como almacenamiento y componentes compartidos. Dos servicios que requieren la misma base relacional pertenecen al mismo quantum en el ejemplo del libro. Tener dos repositorios y dos pipelines no elimina ese punto común.

Una dependencia estática puede tener consecuencias en ejecución: si cambia el esquema o deja de estar disponible el almacenamiento, las funciones que lo necesitan pueden fallar. La palabra «estático» describe la estructura de la relación; no afirma que sus efectos solo se vean antes de ejecutar.

## Dinámico: lo que sucede durante un recorrido

![Dos opciones de acoplamiento dinámico](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-08-acoplamiento-dinamico.png)

*Diagrama didáctico redibujado en PNG; fuente lógica editable: [c07-08-acoplamiento-dinamico.mmd](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-08-acoplamiento-dinamico.mmd).*

**Explicación:** las cajas son participantes en ejecución y las flechas representan mensajes. La rama superior muestra una llamada cuyo resultado se espera; la inferior muestra una alternativa mediada por cola. Son dos opciones de interacción, no una instrucción de ejecutar ambas simultáneamente. La cola permite separar momentos de producción y consumo; no elimina ni la necesidad de pago ni los contratos de mensaje.

**Conclusión y límite:** el acoplamiento dinámico puede unir operacionalmente un recorrido aunque el despliegue de sus participantes sea independiente. Este dibujo propio omite confirmaciones, errores y reintentos; se estudian sus efectos básicos en la nota de sincronía.

## Por qué se tolera más acoplamiento dentro de un límite pequeño

El capítulo acepta un acoplamiento mayor cuando favorece una alta cohesión dentro de un servicio o subsistema. El problema aumenta cuando una modificación aparentemente local rompe partes lejanas que nadie identificó. El ejemplo del libro es renombrar un campo de `State` a `StateCode` y descubrir consumidores inesperados.

La orientación práctica es **mantener más débiles las dependencias al ampliar el alcance**. No significa diseñar cero relaciones: significa comprenderlas, limitar sus efectos y conservar contratos explícitos entre unidades que deben evolucionar separadamente.

## Mini diagnóstico resuelto

«Pedidos y Envíos comparten el concepto de dirección y además leen la misma tabla». La primera relación corresponde al significado del negocio; la tabla común es una decisión de implementación y un punto de acoplamiento estático. Si Pedidos espera la respuesta de Envíos al confirmar una compra, también aparece acoplamiento dinámico. Las cuatro perspectivas ayudan a describir el mismo caso sin confundir sus causas.


---

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/02 Anatomía de un quantum|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/04 Sincronía colas y límites operacionales|Siguiente →]]
