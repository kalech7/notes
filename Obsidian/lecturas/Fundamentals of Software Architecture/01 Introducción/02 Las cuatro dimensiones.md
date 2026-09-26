---
title: "Capítulo 1 · Introducción · Las cuatro dimensiones"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 1
orden: 2
---

# Las cuatro dimensiones

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 1 · Introducción](00%20%C3%8Dndice.md) → Nota 2 de 6

**Objetivo:** Relacionar características, componentes, estilos y decisiones.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Una arquitectura responde a un contexto y no se agota en su estructura física. Para describirla sin perder el porqué hay que conectar condiciones de éxito, responsabilidades, organización y decisiones.

## 2. Cuatro dimensiones y una estructura que las conecta

Enumerar tecnologías o dibujar cajas no explica por qué el sistema funcionará. Las cuatro dimensiones completan mutuamente esa descripción.

![Las cuatro dimensiones de la arquitectura ilustradas mediante una tienda de sándwiches](../Recursos%20visuales/10-cuatro-dimensiones.png)

El reloj, el escudo y el indicador representan capacidades; pedidos, pagos y cocina representan responsabilidades. Las cajas agrupadas o separadas evocan organizaciones posibles y el registro de decisión conserva el porqué. La tienda central es el contexto del negocio. Es una analogía: un estilo no se reduce a contar contenedores, y los componentes de software no son necesariamente las máquinas físicas dibujadas.

La definición del libro reúne **características arquitectónicas, componentes lógicos, estilo arquitectónico y decisiones de arquitectura**. La estructura aparece como el soporte que conecta esas dimensiones; no basta con presentar cajas y flechas sin explicar qué sostienen. **Fuente: PDF 2–6, impresas 2–6, figuras 1-1 a 1-5.**

### Características: bajo qué condiciones tiene éxito el sistema

El libro menciona disponibilidad, confiabilidad, escalabilidad, seguridad, rendimiento, capacidad de prueba y otras capacidades. Estas expresan criterios de éxito del sistema. «Permitir comprar un sándwich» describe comportamiento; «seguir aceptando compras durante un pico de demanda» introduce una característica que influye en la construcción. **Fuente: PDF 3, impresa 3.**

**Ampliación didáctica:** para decidir conviene transformar adjetivos en escenarios observables. Supongamos que PedidoClaro necesita confirmar el 95 % de los pedidos en menos de dos segundos con veinte solicitudes por segundo. Ahora hay una carga, una operación y un umbral que se pueden comprobar. Decir solamente «rápido» permite que negocio y desarrollo crean estar de acuerdo mientras imaginan objetivos distintos.

**Aclaración propia:** rendimiento describe cómo responde con una carga determinada; escalabilidad plantea cómo cambia su capacidad al crecer la demanda y los recursos.

### Componentes lógicos: organizar el comportamiento

Los componentes lógicos estructuran dominios, entidades y flujos de trabajo. En PedidoClaro podríamos reconocer Catálogo, Pedidos, Cobros y Cocina. Cada nombre debe corresponder a responsabilidades comprensibles: Pedidos conserva el estado de la compra; Cocina organiza su preparación. **Base del libro: PDF 4, impresa 4. Ejemplo: elaboración propia.**

Un componente lógico no implica por sí mismo un servidor, un contenedor ni un despliegue independiente. Podemos separar esas responsabilidades dentro de un único programa. Confundir separación lógica con distribución física incorpora costos de comunicación y operación antes de demostrar que hacen falta.

### Estilo: un punto de partida estructural

Después de analizar características y componentes, el arquitecto dispone de información para escoger un estilo como punto de partida. El libro lo relaciona con encontrar un camino de implementación apropiado para los requisitos. No propone comenzar por el estilo de moda y adaptar después el problema a él. **Fuente: PDF 5, impresa 5.**

**Supuesto para PedidoClaro:** con un equipo pequeño y un volumen moderado, podríamos explorar una aplicación única organizada por módulos y capas. Eso es una hipótesis que debe contrastarse, no una recomendación universal extraída del capítulo. El estilo orienta relaciones y límites, pero no resuelve automáticamente todas las decisiones concretas.

### Decisiones: restricciones justificadas

Las decisiones arquitectónicas establecen reglas de construcción y delimitan lo permitido. El ejemplo del libro restringe el acceso a persistencia a las capas de negocio y servicios, impidiendo el acceso directo desde presentación. **Fuente: PDF 5–6, impresas 5–6; consecuencias en PDF 11, impresa 10.**

En PedidoClaro, permitir que la pantalla consulte tablas directamente puede reducir trabajo inicial, pero vincula la interfaz a su organización. Si la tabla de pedidos cambia, también puede ser necesario cambiar pantallas. Una decisión que imponga una interfaz intermedia busca controlar esa dependencia y acepta el costo de mantener dicha interfaz.

![Decisiones: restricciones justificadas ](../Recursos%20visuales/Diagramas/cap01-diagrama-02.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap01-diagrama-02.mmd)

Describir la arquitectura requiere conectar las cuatro dimensiones con una organización concreta. Las flechas no significan independencia ni un proceso estrictamente lineal: una decisión puede obligar a reconsiderar el estilo o una característica.

![arquitectura contexto](../Recursos%20visuales/01-arquitectura-contexto.png)

*Figura original de la guía: el contexto influye en características y componentes; las decisiones relacionan esos elementos con un estilo. Las flechas indican influencia, no un proceso rígidamente lineal.*

---

**Anterior:** [Arquitectura y contexto](01%20Arquitectura%20y%20contexto.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Leyes y compensaciones](03%20Leyes%20y%20compensaciones.md)
