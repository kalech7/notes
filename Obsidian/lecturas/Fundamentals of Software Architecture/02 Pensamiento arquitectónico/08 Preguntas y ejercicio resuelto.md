---
title: "Capítulo 2 · Pensamiento arquitectónico · Preguntas y ejercicio resuelto"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 2
orden: 8
---

# Preguntas y ejercicio resuelto

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 2 · Pensamiento arquitectónico](00%20%C3%8Dndice.md) → Nota 8 de 8

**Objetivo:** Justificar una solución para el historial de pedidos.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Evalúa cada respuesta con cuatro preguntas: ¿qué contexto se asumió?, ¿qué alternativa se comparó?, ¿qué costo apareció? y ¿qué evidencia falta? El objetivo no es repetir «depende», sino completar de qué depende.

## 8. Preguntas para comprobar comprensión

### 1. ¿Elegir un framework de interfaz siempre es diseño?

> [!success]- Solución
> No. Si compromete años de formación, accesibilidad, despliegue e integración, tiene consecuencias arquitectónicas. Deben evaluarse estrategia, esfuerzo de cambio y compensaciones, no clasificar por el nombre de la tecnología.

### 2. ¿Qué gana alguien al reconocer una herramienta que todavía no sabe usar?

> [!success]- Solución
> Amplía las alternativas investigables. Pasa de desconocer su existencia a reconocer una posibilidad y sus preguntas pendientes. Todavía necesita evidencia, práctica o apoyo especializado antes de confiar una decisión a esa herramienta.

### 3. ¿Cómo distinguir prudencia de Frozen Caveman?

> [!success]- Solución
> La prudencia actualiza probabilidad, impacto y medidas según el contexto. El antipatrón convierte un episodio pasado en preocupación dominante sin revisar evidencia. Recordar un fallo es útil; asumir que debe gobernar todos los sistemas exige justificación.

### 4. ¿Hold significa borrar una tecnología y Adopt significa adoptarla siempre?

> [!success]- Solución
> No. Hold desaconseja nuevas adopciones o señala hábitos que evitar; puede coexistir con uso existente. Adopt expresa una valoración favorable dentro de un contexto. Ambos requieren fecha, motivos y revisión.

### 5. ¿Tres consumidores de una única cola garantizan tres copias por pedido?

> [!success]- Solución
> No en el modelo de trabajadores competidores explicado aquí: reparten entregas. Si cocina, notificaciones y analítica necesitan cada pedido, deben tener suscripciones independientes, representadas por colas distintas en nuestro esquema. Los reintentos tampoco sustituyen la difusión.

### 6. ¿Un campo adicional obliga a modificar todos los consumidores?

> [!success]- Solución
> Depende del contrato y de sus reglas de compatibilidad. Un campo opcional ignorado por lectores antiguos puede ser compatible. Renombrar campos, cambiar unidades o introducir obligatoriedad requiere otro análisis. Hay que comprobar comportamiento, no solo sintaxis.

### 7. ¿Programar la pieza más difícil demuestra que el arquitecto ayuda más?

> [!success]- Solución
> Solo si su disponibilidad y la organización del trabajo lo permiten. Monopolizar una dependencia crítica puede retrasar a todos. Delegar, acompañar, experimentar y automatizar puede aportar más al resultado global que concentrar código difícil en una persona.

## 9. Ejercicio aplicado: historial de pedidos

**Escenario inventado:** PedidoClaro ya publica pedidos para cocina, notificaciones y analítica. Se añadirá historial. En campañas llegan 90 eventos por segundo; cada trabajador de historial procesa 40. Historial admite hasta treinta segundos de retraso y no necesita direcciones de entrega. El arquitecto tiene cuatro horas semanales disponibles.

Propón una suscripción, capacidad inicial, restricciones de datos, prueba de compatibilidad y reparto del trabajo. Explica una ventaja y un costo de tu opción; define qué evidencia permitiría cambiarla.

> [!success]- Solución orientativa
> Una cola propia para historial permite consumir independientemente. Dos trabajadores sumarían 80 eventos por segundo, menos que los 90 entrantes; tres ofrecen 120 nominales y un margen de 30. Esto no garantiza treinta segundos de retraso: hay que medir ráfagas, tiempos y recuperación. El mensaje destinado a historial debe excluir direcciones innecesarias; sus permisos deben limitarse a su función. Una prueba comprobaría lectores antiguos frente a un campo opcional nuevo y rechazaría cambios incompatibles de unidades. El equipo implementaría la ruta productiva y el arquitecto haría una POC acotada. La ventaja es independencia; el costo, otra suscripción y operación. Revisaríamos capacidad si la antigüedad de eventos crece o la base limita el rendimiento.

---

**Anterior:** [Programar sin ser cuello de botella](07%20Programar%20sin%20ser%20cuello%20de%20botella.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Módulos y separación física](../03%20Modularidad/01%20M%C3%B3dulos%20y%20separaci%C3%B3n%20f%C3%ADsica.md)
