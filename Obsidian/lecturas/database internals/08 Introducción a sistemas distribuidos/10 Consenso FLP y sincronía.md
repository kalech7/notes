---
title: "Database Internals — Consenso, FLP y sincronía"
created: 2026-09-30
libro: "Database Internals"
capitulo: 8
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Consenso, FLP y sincronía

[[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice del capítulo 8]]

Después de distinguir entrega y conocimiento, podemos definir el acuerdo que sí pedimos a un algoritmo. La pregunta no es si alguna ejecución feliz decide, sino qué decisiones y qué progreso garantiza en todas las ejecuciones permitidas por sus supuestos.

## Las propiedades del consenso

El capítulo introduce procesos con propuestas iniciales que deben alcanzar una decisión compatible. **Acuerdo** impide que procesos correctos decidan valores distintos. **Validez** restringe qué se puede decidir; en la formulación introductoria del libro debe ser un valor propuesto, en lugar de inventarse uno. **Terminación** exige que los procesos correctos decidan eventualmente bajo las condiciones del modelo. Algunas formulaciones refuerzan el acuerdo a todos los procesos que deciden; esa variante se denomina uniforme.

La unanimidad se refiere a la compatibilidad de decisiones, no a recibir una respuesta de cada proceso antes de avanzar. Un proceso caído no puede tener la obligación práctica de contestar o terminar. Estas precisiones evitan leer literalmente las frases de la impresa 189 sobre «todos los procesos».

**Seguridad** significa que no ocurre un resultado prohibido; aquí protege acuerdo y validez. **Vivacidad** significa que ocurre progreso; aquí incluye terminación. Un algoritmo puede conservar decisiones seguras y detener el avance mientras no se cumplen las condiciones necesarias.

## Qué demuestra FLP

FLP, de Fischer, Lynch y Paterson, muestra que en un modelo totalmente asíncrono, determinista y con posibilidad de una sola caída, no puede garantizarse terminación del consenso en toda ejecución admisible. El límite incluye comunicación fiable: no depende de exigir pérdida de mensajes. Existe una ejecución que evita la decisión; no significa que todas las ejecuciones fracasen. [Artículo original, 1985](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf).

La impresa 189 y su continuación presentan el resultado como falta de consenso «en tiempo acotado». Esa frase puede inducir una lectura demasiado débil. El problema no es únicamente desconocer un límite de segundos: bajo esos supuestos no se garantiza ni siquiera terminación eventual para todas las ejecuciones. Se puede decidir en muchas ejecuciones útiles, pero eso no cumple la garantía universal que el resultado excluye.

Una intuición es que el proceso lento y el proceso muerto son indistinguibles para quien espera. Si esperamos siempre al ausente, podríamos no terminar ante una caída. Si descartamos respuestas sin una condición suficiente, podemos tomar decisiones incompatibles. Esta intuición no sustituye la demostración formal ni establece que un timeout por sí solo rompa seguridad.

## Sincronía delimita la interpretación del silencio

Un sistema **asíncrono** no proporciona cotas conocidas adecuadas sobre tiempos de mensaje y avance de procesos. **Síncrono** incorpora cotas de entrega y procesamiento que permiten razonar por plazos. No significa ejecutar todo a la vez ni tener todos los relojes de pared idénticos.

La **sincronía parcial** permite cotas desconocidas o cotas que empiezan a cumplirse después de un instante desconocido. Es más preciso que decir simplemente «normalmente la red va bien». Permite diseñar protocolos que preserven seguridad durante retrasos y obtengan progreso cuando aparece un período suficientemente estable. [Dwork, Lynch y Stockmeyer, 1988](https://groups.csail.mit.edu/tds/papers/Lynch/jacm88.pdf).

| Modelo | Qué podemos asumir | Qué indica un plazo vencido |
|---|---|---|
| Asíncrono | Sin cota temporal disponible para decidir | Sospecha, no prueba de caída |
| Síncrono | Cotas especificadas y válidas | Incumplimiento de una cota bajo las hipótesis |
| Parcialmente síncrono | Cotas desconocidas o válidas eventualmente | Puede haber sospechas falsas antes de estabilizar |

El libro menciona detectores de fallas y elecciones de líder como aplicaciones de tiempo. Si dos nodos se consideran líderes, un protocolo correcto necesita reglas de autoridad —por ejemplo, épocas y aceptación de comandos— para impedir decisiones incompatibles. No basta con confiar en que quien va atrasado «aceptará» luego al otro. Este capítulo no presenta una implementación de Raft; la mención sirve para mostrar por qué los supuestos temporales y la seguridad deben distinguirse.

La consecuencia de FLP no es abandonar el consenso: es declarar las condiciones que permiten progresar, como sincronía parcial, detectores con propiedades adicionales o modelos con aleatoriedad. Cualquier garantía concreta debe venir acompañada de su modelo de fallas.

**Referencia:** PDF 22–24 · impresas 189–191. [[Obsidian/lecturas/database internals/Materiales/08 Sistemas distribuidos.pdf#page=22|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/09 Dos generales y conocimiento común|Anterior]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/11 Modelos de fallas y tolerancia|Siguiente]] →
