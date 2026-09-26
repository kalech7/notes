---
title: "Capítulo 5 · Identificar y priorizar características · De necesidades a decisiones"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 1
---

# De necesidades a decisiones

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 1 de 9

**Objetivo:** Convertir preocupaciones en preguntas verificables.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 1. Identificar significa convertir necesidades en decisiones justificables

Una funcionalidad describe algo que el sistema permite hacer: registrar un pedido. Una característica describe una condición relevante para hacerlo: seguir aceptándolo durante un pico de demanda. Identificar características consiste en descubrir qué condiciones importan tanto que pueden orientar la estructura del sistema. No consiste en reunir palabras terminadas en «-idad».

**Libro — PDF p. 12, impresa 67:** hay al menos tres fuentes: preocupaciones del dominio, requisitos del proyecto y conocimiento implícito del dominio. Deben combinarse. Los requisitos pueden indicar cuántas personas usarán una aplicación; el conocimiento del negocio puede revelar que todas intentarán entrar a la misma hora.

En PedidoClaro, «no perder el almuerzo de las oficinas» expresa una preocupación comercial. Debemos preguntar cuándo se concentra la demanda y qué puede fallar. Aceptar pedidos durante un pico importa, pero recibir más de los que la cocina puede preparar empeora el problema.

![1. Identificar significa convertir necesidades en decisiones justificables ](../Recursos%20visuales/Diagramas/cap05-diagrama-01.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap05-diagrama-01.mmd)

**Interpretación:** las tres fuentes convergen en situaciones concretas antes de justificar decisiones. **Límite:** el diagrama simplifica un proceso iterativo; probar una decisión puede revelar requisitos omitidos y obligar a volver atrás.

---

**Anterior:** [Preguntas y ejercicio resuelto](../04%20Caracter%C3%ADsticas%20arquitect%C3%B3nicas/07%20Preguntas%20y%20ejercicio%20resuelto.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Traducción del negocio y características compuestas](02%20Traducci%C3%B3n%20del%20negocio%20y%20caracter%C3%ADsticas%20compuestas.md)
