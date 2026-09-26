---
title: "Capítulo 1 · Introducción · Principios decisiones y ADR"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 1
orden: 5
---

# Principios decisiones y ADR

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 1 · Introducción](00%20%C3%8Dndice.md) → Nota 5 de 6

**Objetivo:** Registrar una decisión y su justificación.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 5. Principios, decisiones y un ADR breve

El libro menciona principios de diseño junto con decisiones que orientan a los equipos; describe las decisiones como reglas y remite su documentación al capítulo 21. Estas páginas no desarrollan un formato de ADR. **Fuente: PDF 5–8, impresas 5–8.**

**Distinción operativa de esta guía:** un principio expresa una orientación general, como «reducir el impacto de los cambios de datos en las interfaces». Una decisión concreta esa orientación bajo un contexto, como «la interfaz consumirá operaciones de Pedidos y no consultará sus tablas». El principio ayuda a interpretar casos nuevos; la decisión establece una restricción verificable. Una preferencia personal no se convierte en ninguna de las dos simplemente porque la anuncie el arquitecto.

> [!example] ADR-001 · Acceso a datos de pedidos — ejemplo inventado
> **Estado:** aceptado para el escenario didáctico.
> **Contexto:** web y caja comparten reglas de pedidos; esperamos cambiar su almacenamiento.
> **Decisión:** ambas interfaces accederán mediante operaciones del módulo Pedidos; quedan prohibidas sus consultas directas a tablas.
> **Alternativas:** acceso directo desde cada interfaz; módulo intermedio compartido.
> **Razón:** concentrar reglas y limitar el impacto de cambios del esquema.
> **Consecuencias:** mantener un contrato explícito y asumir trabajo adicional; centralizarlo también puede concentrar dependencias.
> **Verificación:** revisar dependencias y medir el tiempo de confirmación.
> **Revisión:** reconsiderar si el contrato impide un requisito demostrado o cambia el contexto.

ADR significa *Architecture Decision Record*, registro de decisión arquitectónica. El ejemplo desarrolla la segunda ley: conservar la razón permite revisar la decisión sin adivinar qué intentaba proteger.

![5. Principios, decisiones y un ADR breve ](../Recursos%20visuales/Diagramas/cap01-diagrama-04.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap01-diagrama-04.mmd)

**Interpretación:** una orientación adquiere consecuencias mediante decisiones, implementación y evidencia. **Límite:** no prescribe una metodología del libro ni supone que toda decisión requiera aprobación centralizada; es una síntesis didáctica propia.

---

**Anterior:** [Responsabilidades del arquitecto](04%20Responsabilidades%20del%20arquitecto.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Preguntas y ejercicio resuelto](06%20Preguntas%20y%20ejercicio%20resuelto.md)
