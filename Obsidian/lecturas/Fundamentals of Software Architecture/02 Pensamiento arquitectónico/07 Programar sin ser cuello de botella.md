---
title: "Capítulo 2 · Pensamiento arquitectónico · Programar sin ser cuello de botella"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 2
orden: 7
---

# Programar sin ser cuello de botella

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 2 · Pensamiento arquitectónico](00%20%C3%8Dndice.md) → Nota 7 de 8

**Objetivo:** Colaborar con el equipo sin concentrar el trabajo.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 7. Seguir programando sin convertirse en cuello de botella

Los autores defienden mantener contacto con el código. El peligro es la **Bottleneck Trap**: asumir piezas críticas cuya entrega depende de una persona que también atiende reuniones y decisiones arquitectónicas. **Fuente: PDF pp. 29–31; impresas pp. 33–35.**

Supongamos que el componente de pagos exige veinte horas de trabajo y el arquitecto dispone de cinco horas semanales para programar. Incluso sin imprevistos, necesita cuatro semanas; los equipos dependientes heredan esa espera. No es un problema de capacidad intelectual, sino de disponibilidad y dependencia.

El libro propone delegar piezas críticas y contribuir a funcionalidad menos urgente, prevista una a tres iteraciones después. Así se conserva experiencia con el entorno real y se distribuye conocimiento. Esto no significa desentenderse de decisiones delicadas: se puede acompañar su diseño sin monopolizar implementación y aprobación.

Las alternativas del libro tienen propósitos distintos:

- **POC frecuentes:** implementar un experimento para comprobar una incertidumbre. Comparar dos cachés exige cargas y criterios equivalentes. Los autores recomiendan código cuidado porque el prototipo puede convertirse en referencia; eso no demuestra que esté listo para producción.
- **Deuda técnica:** reducir obstáculos acumulados. Matiz propio: no toda deuda es postergable; una dependencia vulnerable o una migración obligatoria puede estar en la ruta crítica.
- **Corrección de bugs:** descubrir fallos reales de comprensión y estructura. Conviene elegir trabajos compatibles con la disponibilidad; un incidente urgente no debe depender de huecos en la agenda.
- **Automatización:** eliminar comprobaciones repetitivas y crear verificaciones de arquitectura. Una regla que prohíba dependencias indebidas ofrece retroalimentación repetible, aunque no certifique la calidad completa del sistema.
- **Revisiones de código:** comprender implementación y acompañar al equipo. Exigir la aprobación personal del arquitecto en cada cambio recrearía el mismo cuello de botella.

---

**Anterior:** [Negocio y agilidad](06%20Negocio%20y%20agilidad.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Preguntas y ejercicio resuelto](08%20Preguntas%20y%20ejercicio%20resuelto.md)
