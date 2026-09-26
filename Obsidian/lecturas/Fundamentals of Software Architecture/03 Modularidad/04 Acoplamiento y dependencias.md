---
title: "Capítulo 3 · Modularidad · Acoplamiento y dependencias"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 3
orden: 4
---

# Acoplamiento y dependencias

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 3 · Modularidad](00%20%C3%8Dndice.md) → Nota 4 de 7

**Objetivo:** Leer dependencias entrantes y salientes.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 4. Acoplamiento: quién depende de quién

El acoplamiento aferente $C_a$ cuenta dependencias **entrantes**: otros elementos dependen del elemento analizado. El eferente $C_e$ cuenta dependencias **salientes**: el elemento analizado depende de otros.

![4. Acoplamiento: quién depende de quién ](../Recursos%20visuales/Diagramas/cap03-diagrama-03.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap03-diagrama-03.mmd)

**Interpretación:** para Pedidos, en este grafo $C_a=3$ y $C_e=2$. La flecha va del dependiente hacia aquello que utiliza. **Límite:** son dependencias entre módulos distintos, no cantidad de llamadas, tráfico, latencia ni una traza temporal.

Hay que fijar la unidad: tipos, paquetes o componentes. También qué relación cuenta: importación, referencia de tipo o uso efectivo. En este ejemplo contamos módulos distintos y excluimos dependencias internas. Mezclar conteos de clases con conteos de paquetes produciría ratios engañosos.

Un $C_a$ elevado señala un alcance potencial de propagación de cambios: modificar un contrato puede afectar muchos consumidores. Un $C_e$ elevado señala muchos proveedores cuyos cambios podrían afectar al módulo. Ninguno demuestra por sí solo mala arquitectura; un contrato central estable puede tener numerosos consumidores deliberadamente.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=8|PDF pp. 8–9; impresas pp. 44–45]].

---

**Anterior:** [LCOM y sus variantes](03%20LCOM%20y%20sus%20variantes.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Abstracción inestabilidad y distancia](05%20Abstracci%C3%B3n%20inestabilidad%20y%20distancia.md)
