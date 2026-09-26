---
title: "Capítulo 5 · Identificar y priorizar características · Kata Silicon Sandwiches"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 4
---

# Kata Silicon Sandwiches

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 4 de 9

**Objetivo:** Leer el problema y explicitar restricciones y supuestos.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Identificar características requiere separar hechos, supuestos e inferencias del dominio. Una kata crea un contexto acotado para practicar esa separación y comparar razonamientos, no para adivinar una solución oficial.

## 4. Practicar con katas: problema, restricciones y discusión

**Libro — PDF pp. 15–16, impresas 70–71:** una kata arquitectónica es un ejercicio acotado para practicar decisiones sin esperar años entre proyectos. Ted Neward desarrolló este formato de práctica; los autores lo adaptaron. Sus secciones son **descripción**, **usuarios**, **requisitos** y **contexto adicional**.

Pequeños equipos trabajan durante un tiempo fijado, producen análisis de características y diagramas, presentan resultados y comparan propuestas; el formato descrito incluye una votación. Un arquitecto experimentado puede revisar compensaciones omitidas y alternativas. La limitación temporal hace que se evalúe el razonamiento, no una implementación completa.

**Propuesta propia:** dedicar quince minutos a preguntas, veinte a características, veinte a alternativas y diez a revisión. Registrar supuestos permite descubrir si las propuestas difieren porque imaginaron cargas o presupuestos distintos.

### Silicon Sandwiches: enunciado completo de la fuente

**Libro — PDF p. 16, impresa 71; paráfrasis del enunciado:** una cadena nacional de sándwiches quiere incorporar pedidos por internet al servicio telefónico existente. Espera miles de usuarios y, posiblemente, millones en el futuro.

Sus requisitos son:

1. Permitir realizar pedidos y elegir recogida o entrega cuando el local ofrezca reparto.
2. Dar a quienes recogen una hora y direcciones al local, integrándose con varios servicios externos de mapas que incluyan información del tráfico.
3. Despachar al repartidor con el pedido para la entrega al cliente.
4. Permitir acceso desde dispositivos móviles.
5. Ofrecer promociones y especiales diarios nacionales.
6. Ofrecer promociones y especiales diarios locales.
7. Aceptar pagos en línea, en el local o al entregar.

El contexto adicional aporta tres condiciones: los locales son franquicias con propietarios diferentes; la matriz planea expandirse al extranjero próximamente; y busca contratar personal de bajo coste para maximizar beneficios.

Este enunciado pertenece a **Silicon Sandwiches**; PedidoClaro no añade requisitos retroactivamente a la kata.

---

**Anterior:** [Requisitos implícitos y promedios](03%20Requisitos%20impl%C3%ADcitos%20y%20promedios.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Derivar características candidatas](05%20Derivar%20caracter%C3%ADsticas%20candidatas.md)
