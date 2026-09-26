---
title: "Capítulo 4 · Características arquitectónicas · Comportamiento y capacidades"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 4
orden: 1
---

# Comportamiento y capacidades

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 4 · Características arquitectónicas](00%20%C3%8Dndice.md) → Nota 1 de 7

**Objetivo:** Distinguir funciones y características arquitectónicas.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 1. Comportamiento y capacidades: dos preguntas distintas

El dominio describe **qué hace** el sistema. En PedidoClaro: seleccionar pan, calcular un precio y registrar un pedido. Una característica arquitectónica expresa una capacidad necesaria para que ese comportamiento resulte útil: responder dentro de cierto tiempo, resistir fallos o permitir cambios sin afectar funciones ajenas. Una compra correctamente calculada que tarda veinte minutos puede resultar comercialmente inútil.

El libro contrapone *behavior*, comportamiento del dominio, y *capabilities*, capacidades del sistema. Prefiere «características arquitectónicas» a «requisitos no funcionales» y «atributos de calidad» para destacar su importancia durante el diseño. Otros equipos pueden usar los términos alternativos con rigor. **Fuente: PDF pp. 1–3; impresas 55–57.**

Para los autores deben concurrir **tres criterios**:

1. **Consideración ajena a la funcionalidad del dominio.** «Calcular descuentos» define comportamiento; «calcularlos con p95 inferior a 300 ms bajo una carga acordada» añade una capacidad.
2. **Influencia estructural.** El requisito obliga a considerar organización, límites, dependencias, distribución o mecanismos de infraestructura. No toda buena práctica local determina la arquitectura.
3. **Importancia para el éxito.** Debe existir una razón concreta para invertir: pérdida de pedidos, riesgo de datos, imposibilidad de evolucionar o interrupción del negocio.

![1. Comportamiento y capacidades: dos preguntas distintas ](../Recursos%20visuales/Diagramas/cap04-diagrama-01.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap04-diagrama-01.mmd)

**Interpretación:** los tres criterios se necesitan conjuntamente. **Límite:** las flechas no representan una secuencia ni un algoritmo automático; determinar la influencia estructural requiere juicio contextual.

Cambiar el color de un botón puede ser local. Garantizar accesibilidad en cientos de pantallas puede exigir componentes compartidos, navegación uniforme y verificaciones continuas: el alcance cambia las consecuencias arquitectónicas.

**Explícitas e implícitas.** Una característica explícita aparece en documentos o instrucciones; una implícita se descubre al comprender el negocio. «No perder pedidos cobrados» puede no estar escrito, pero de allí se derivan necesidades de integridad y recuperación. Inferirlas no autoriza a inventar exigencias ilimitadas: hay que convertir la hipótesis en una condición verificable y validarla con quienes conocen el negocio. **Fuente: PDF pp. 3–4; impresas 57–58.**

### Una precisión sobre seguridad y monolitos

En la página impresa 58, el libro contrasta prácticas de seguridad locales con estructuras especializadas y señala límites al escalado monolítico. **Matiz técnico de esta guía:** un monolito puede escalar horizontalmente mediante varias instancias, siempre que gestione adecuadamente estado, sesiones y recursos compartidos. Separar servicios tampoco garantiza escalabilidad: una base de datos saturada o llamadas encadenadas pueden conservar el cuello de botella.

La seguridad requiere analizar amenazas y controles en cualquier estilo. Un monolito puede necesitar aislamiento o separación de privilegios; contratar un proveedor de pagos no protege automáticamente sesiones, autorizaciones ni datos del resto de PedidoClaro. La pregunta útil es qué estructura necesita el riesgo concreto.

---

**Anterior:** [Preguntas y ejercicio resuelto](../03%20Modularidad/07%20Preguntas%20y%20ejercicio%20resuelto.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Catálogo de características](02%20Cat%C3%A1logo%20de%20caracter%C3%ADsticas.md)
