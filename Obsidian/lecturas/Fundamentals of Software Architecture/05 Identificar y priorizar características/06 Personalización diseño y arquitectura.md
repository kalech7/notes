---
title: "Capítulo 5 · Identificar y priorizar características · Personalización diseño y arquitectura"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 6
---

# Personalización diseño y arquitectura

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 6 de 9

**Objetivo:** Decidir el alcance de una variación entre locales.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 6. Personalización: ¿diseño o arquitectura?

**Libro — PDF p. 21, impresa 76:** un microkernel puede alojar comportamiento común en un núcleo y variaciones en extensiones. Otra arquitectura puede resolverlas con Template Method: una clase base define un flujo y las subclases redefinen pasos. La misma necesidad puede encontrar soluciones a diferente escala.

**Elaboración propia:** en PedidoClaro, cambiar únicamente un descuento por local puede necesitar datos configurables. Si cada franquicia aporta reglas ejecutables independientes, un modelo de extensiones gana atractivo. Ese beneficio implica definir contratos, compatibilidad y tratamiento de fallos. Template Method puede ser suficiente para unas pocas variantes mantenidas por el mismo equipo, aunque la herencia introduce acoplamiento y puede volver difíciles las combinaciones de reglas.

![6. Personalización: ¿diseño o arquitectura? ](../Recursos%20visuales/Diagramas/cap05-diagrama-04.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap05-diagrama-04.mmd)

**Interpretación:** primero se comprende la variación y después se comparan mecanismos. **Límite:** no es un algoritmo de selección ni una lista exhaustiva; las opciones pueden combinarse.

La fuente pide analizar rendimiento, acoplamiento, otras características y coste. Exige colaborar con desarrollo, responsables técnicos, negocio, gestión y operaciones. Evitar la **torre de marfil** significa contrastar la propuesta con quienes implementarán y operarán sus consecuencias.

---

**Anterior:** [Derivar características candidatas](05%20Derivar%20caracter%C3%ADsticas%20candidatas.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Prioridades y mínimos](07%20Prioridades%20y%20m%C3%ADnimos.md)
