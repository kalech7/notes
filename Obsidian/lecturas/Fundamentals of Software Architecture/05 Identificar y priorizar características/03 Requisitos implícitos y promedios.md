---
title: "Capítulo 5 · Identificar y priorizar características · Requisitos implícitos y promedios"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 3
---

# Requisitos implícitos y promedios

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 3 de 9

**Objetivo:** Descubrir lo que una cifra agregada oculta.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 3. Conocimiento implícito: cuestionar el promedio

**Libro — PDF p. 14, impresa 69:** una universidad tiene 1.000 estudiantes y diez horas de matrícula. El ejemplo contrapone repartirlos uniformemente y recibirlos durante los últimos diez minutos. El objetivo es mostrar cómo el conocimiento del dominio modifica el diseño aunque no aparezca escrito.

**Cálculo propio sobre esas cifras:** diez horas son 600 minutos. El promedio uniforme es 1.000/600 = **1,67 estudiantes por minuto**. Concentrarlos en diez minutos produce **100 por minuto**, sesenta veces más. Diseñar con el promedio ocultaría el pico.

Estudiantes por minuto no equivale a solicitudes por segundo ni a sesiones concurrentes. Si suponemos veinte solicitudes por estudiante, el segundo escenario produce unas 33,3 solicitudes por segundo en promedio durante el pico. La simultaneidad dependerá de la duración de las sesiones; las solicitudes pueden agruparse todavía más alrededor de una apertura de cupos. Estas cifras adicionales son supuestos, no mediciones.

La observación del libro sobre procrastinación sirve para plantear una hipótesis. En un proyecto real conviene comprobar horarios, campañas, historial y comportamiento. En PedidoClaro, el almuerzo sugiere picos, pero una promoción o pedidos programados pueden cambiar su forma. Conocimiento implícito no significa permiso para presentar intuiciones como datos.

---

**Anterior:** [Traducción del negocio y características compuestas](02%20Traducci%C3%B3n%20del%20negocio%20y%20caracter%C3%ADsticas%20compuestas.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Kata Silicon Sandwiches](04%20Kata%20Silicon%20Sandwiches.md)
