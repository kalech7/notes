---
title: "Capítulo 3 · Modularidad · Módulos y separación física"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 3
orden: 1
---

# Módulos y separación física

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 3 · Modularidad](00%20%C3%8Dndice.md) → Nota 1 de 7

**Objetivo:** Distinguir fronteras lógicas y unidades de despliegue.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 1. Modularidad, granularidad y separación física

El libro usa *módulo* como agrupación lógica de código relacionado: funciones, clases u otros elementos. La **modularidad** trata de esa organización y sus fronteras; la **granularidad**, del tamaño y alcance de las piezas. Son dimensiones relacionadas: separar más unidades cambia las fronteras, pero una partición más fina no necesariamente mejora el diseño.

En PedidoClaro, cálculo de subtotales, descuentos y redondeo podrían pertenecer a `Precios`. Si cada operación se convierte en un servicio remoto, calcular un pedido exige coordinar varias llamadas. Aparecen latencia, versiones de contratos y fallos parciales. Ese coste puede ser razonable si existe una necesidad concreta; no surge una ventaja solo por tener piezas pequeñas.

![1. Modularidad, granularidad y separación física ](../Recursos%20visuales/Diagramas/cap03-diagrama-01.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap03-diagrama-01.mmd)

**Interpretación:** puede haber módulos con contratos definidos dentro de un solo proceso. **Límite:** las flechas expresan dependencias conceptuales; no prueban que el código impida accesos a detalles internos ni describen toda la ejecución.

La separación **lógica** establece responsabilidades, visibilidad y contratos. La separación **física** introduce unidades como bibliotecas, procesos o despliegues. Un monolito puede conservar buenas fronteras lógicas; varios servicios pueden depender continuamente de los detalles de sus vecinos y requerir cambios coordinados. Por eso no conviene equiparar modularidad con distribución.

Un *namespace* distingue nombres: `clientes.Estado` y `pedidos.Estado` pueden coexistir sin representar el mismo concepto. Esto resuelve identificación, pero no demuestra cohesión. Una carpeta `utilidades` puede contener funciones sin relación aunque todos sus nombres sean únicos.

El recorrido histórico del libro conecta programación estructurada, mecanismos de módulos y posterior conservación de paquetes y espacios de nombres en lenguajes orientados a objetos. Sirve para entender por qué conviven funciones, clases y paquetes. Aquí no se reproduce como cronología estricta de versiones de Java: el propósito didáctico es distinguir **organización de nombres, encapsulación y empaquetado físico**. Ninguna de esas propiedades sustituye automáticamente a las otras.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=1|PDF pp. 1–4; impresas pp. 37–40]].

---

**Anterior:** [Preguntas y ejercicio resuelto](../02%20Pensamiento%20arquitect%C3%B3nico/08%20Preguntas%20y%20ejercicio%20resuelto.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Cohesión y responsabilidades](02%20Cohesi%C3%B3n%20y%20responsabilidades.md)
