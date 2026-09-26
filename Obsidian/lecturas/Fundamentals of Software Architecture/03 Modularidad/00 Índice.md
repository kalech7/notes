---
title: "03 · Modularidad — 2.ª edición"
created: 2026-09-25
tags:
  - lecturas/software-architecture
---

# Capítulo 3 · Modularidad

[← Inicio del libro](../00%20Empieza%20aqu%C3%AD.md)

Este capítulo está dividido en **7 notas**. Lee en orden y usa **Anterior / Siguiente** al final de cada una. La última reúne las preguntas y el ejercicio resuelto.

## Orden de lectura

| Nota | Lo que podrás explicar |
|---|---|
| [01 · Módulos y separación física](01%20M%C3%B3dulos%20y%20separaci%C3%B3n%20f%C3%ADsica.md) | Distinguir fronteras lógicas y unidades de despliegue. |
| [02 · Cohesión y responsabilidades](02%20Cohesi%C3%B3n%20y%20responsabilidades.md) | Explicar qué debería permanecer junto. |
| [03 · LCOM y sus variantes](03%20LCOM%20y%20sus%20variantes.md) | Calcular LCOM y reconocer qué no mide. |
| [04 · Acoplamiento y dependencias](04%20Acoplamiento%20y%20dependencias.md) | Leer dependencias entrantes y salientes. |
| [05 · Abstracción inestabilidad y distancia](05%20Abstracci%C3%B3n%20inestabilidad%20y%20distancia.md) | Calcular A, I y D e interpretar sus límites. |
| [06 · Connascencia y refactorización](06%20Connascencia%20y%20refactorizaci%C3%B3n.md) | Identificar las nueve formas de connascencia. |
| [07 · Preguntas y ejercicio resuelto](07%20Preguntas%20y%20ejercicio%20resuelto.md) | Proponer límites para la cancelación de pedidos. |

## Fuente y forma de estudiar este capítulo

Esta guía desarrolla el capítulo 3 de *Fundamentals of Software Architecture*, segunda edición, de Mark Richards y Neal Ford. Se basa exclusivamente en las **páginas 1–18 del PDF de modularidad, correspondientes a las páginas impresas 37–54**. Las referencias siguientes distinguen ambas numeraciones. No presuponen acceso a otros capítulos.

**Contenido del libro:** modularidad, granularidad, cohesión, acoplamiento, métricas estructurales y connascencia. **Elaboración propia:** explicaciones, cálculos, diagramas, aclaraciones de ambigüedades y ejercicios. **Supuesto transversal:** PedidoClaro es una tienda de sándwiches completamente inventada para esta guía; no es la kata *Silicon Sandwiches* del libro. Sus clientes compran productos, reciben pedidos y pagan importes calculados por el sistema.

La pregunta central es: **¿qué conocimiento y qué cambios deben permanecer dentro de una frontera?** Una frontera útil permite modificar una regla sin perseguir sus detalles por toda la aplicación. Dibujar carpetas o servicios no garantiza esa propiedad.

![modularidad](../Recursos%20visuales/03-modularidad.png)

## 9. Alcance y cautelas de la fuente

El cierre del capítulo conecta módulos con componentes como unidades de construcción arquitectónica, pero no desarrolla aquí un procedimiento completo para derivarlos del dominio: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=18|PDF p. 18; impresa p. 54]].

Se revisaron las 18 páginas del escaneo, usando reconocimiento de texto y revisión visual; la ecuación LCOM96b se verificó en una ampliación de la página impresa 43. Se han señalado las ambigüedades relevantes: conteo de pares de LCOM, variantes de normalización, unidades del ejemplo de abstracción, interpretación de inestabilidad y nombres de las reglas de connascencia. Los diagramas y cálculos de esta nota son elaboraciones didácticas propias, no figuras reproducidas del libro.

---

[← Capítulo anterior](../02%20Pensamiento%20arquitect%C3%B3nico/00%20%C3%8Dndice.md) · [Comenzar este capítulo](01%20M%C3%B3dulos%20y%20separaci%C3%B3n%20f%C3%ADsica.md) · [Capítulo siguiente →](../04%20Caracter%C3%ADsticas%20arquitect%C3%B3nicas/00%20%C3%8Dndice.md)
