---
title: "Capítulo 1 · Introducción · Leyes y compensaciones"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 1
orden: 3
---

# Leyes y compensaciones

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 1 · Introducción](00%20%C3%8Dndice.md) → Nota 3 de 6

**Objetivo:** Explicar el porqué y los costos de una decisión.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 3. Tres leyes y dos corolarios para razonar

Los autores presentan estas leyes como generalizaciones de su experiencia: dos surgieron durante la primera edición y la tercera durante la segunda. Son herramientas de razonamiento profesional, no leyes físicas ni resultados matemáticos demostrados. **Fuente: PDF 6–8, impresas 6–8.**

### Primera ley: toda decisión arquitectónica implica compensaciones

Ganar algo suele exigir pagar algo en otra dimensión. Añadir una caché puede acelerar lecturas, pero obliga a decidir cuándo actualizar o invalidar datos. Separar componentes puede facilitar cambios independientes, pero requiere coordinar sus contratos. La pregunta útil es qué mejora, qué empeora, para quién y bajo qué condiciones.

**Ejemplo propio:** si una consulta tarda 80 ms y una caché tarda 5 ms, con un 90 % de aciertos y suponiendo que cada fallo cuesta 85 ms, el tiempo medio de ese acceso sería `0,90 × 5 + 0,10 × 85 = 13 ms`. Es una mejora frente a 80 ms, pero no describe el tiempo completo de compra ni los peores casos. Si el precio permanece desactualizado, ahorrar milisegundos puede crear reclamaciones. El cálculo no decide por sí solo si conviene almacenar precios en caché.

El **primer corolario** advierte que, si no vemos la compensación, probablemente todavía no la identificamos. No obliga a inventar daños imaginarios: obliga a buscar costos desplazados, como mantenimiento, aprendizaje y recuperación ante fallos.

El **segundo corolario** afirma que no basta con analizar compensaciones una sola vez. Un criterio adoptado para cinco tiendas puede ser inadecuado para quinientas. Un estándar puede reducir decisiones repetidas, pero sigue necesitando condiciones de aplicación. **Fuente de ambos: PDF 7, impresa 7.**

### Segunda ley: el porqué importa más que el cómo

Un diagrama puede mostrar que Pedidos se comunica con Cocina mediante una cola. No explica si se buscaba absorber picos, tolerar interrupciones o desacoplar equipos. Sin esa razón, alguien podría sustituirla por una llamada directa y eliminar justamente la propiedad que motivó su incorporación. **Fuente: PDF 7, impresa 7. Ejemplo: elaboración propia.**

Conservar el porqué significa registrar contexto, alternativas y costos aceptados. Una razón convincente tampoco convierte una implementación defectuosa en correcta.

### Tercera ley: la mayoría de las decisiones admite grados

Los autores señalan que muchas decisiones se sitúan en un espectro entre extremos. «Compartir o duplicar» no exige escoger igual para todo el sistema: podemos compartir un contrato estable y separar reglas que cambian por motivos diferentes. **Fuente: PDF 7, impresa 7. Ejemplo: ampliación propia.**

PedidoClaro podría centralizar la confirmación del pago y permitir que cada local organice su cola de preparación. Esto no demuestra que el punto intermedio siempre sea mejor. Una solución intermedia también puede reunir costos de ambos extremos; necesita justificación.

![Tercera ley: la mayoría de las decisiones admite grados ](../Recursos%20visuales/Diagramas/cap01-diagrama-03.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap01-diagrama-03.mmd)

**Interpretación:** hay posiciones posibles entre extremos, y podemos elegir por responsabilidad. **Límite:** no es una escala cuantificada ni demuestra que el centro sea óptimo; algunas restricciones sí producen decisiones binarias.

---

**Anterior:** [Las cuatro dimensiones](02%20Las%20cuatro%20dimensiones.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Responsabilidades del arquitecto](04%20Responsabilidades%20del%20arquitecto.md)
