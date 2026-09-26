---
title: "Capítulo 4 · Características arquitectónicas · Lenguaje común y compromisos"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 4
orden: 6
---

# Lenguaje común y compromisos

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 4 · Características arquitectónicas](00%20%C3%8Dndice.md) → Nota 6 de 7

**Objetivo:** Acordar significados y revisar las compensaciones.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Cada capacidad necesita escenario y medida: «disponible», «rápido» o «recuperado» pueden significar cosas distintas para negocio, desarrollo y operaciones. Sin acuerdo semántico, dos equipos pueden optimizar objetivos incompatibles usando la misma palabra.

## 6. Lenguaje ubicuo, compromisos e iteración

El libro recomienda un **lenguaje ubicuo** compartido dentro de la organización. «Aprendizaje» podría significar facilidad de aprender a usar el producto o adaptación automática del sistema; una palabra compartida no garantiza una idea compartida. **Fuente: PDF pp. 7 y 10–11; impresas 61 y 64–65.**

En PedidoClaro, definir «confirmado» como «persistido y aceptado para preparación» cambia qué medimos respecto de definirlo como «recibido en memoria». Cada objetivo necesita nombre, operación, condiciones, umbral y evidencia. Así, negocio, desarrollo y operaciones pueden discutir la misma promesa.

Los autores proponen la arquitectura **menos mala (*least worst*)**: compromisos aceptables para el contexto. Las características cuestan diseño, implementación y mantenimiento; maximizarlas todas genera complejidad. Se mantienen mínimos necesarios y se decide dónde invertir soporte especial.

![6. Lenguaje ubicuo, compromisos e iteración ](../Recursos%20visuales/Diagramas/cap04-diagrama-04.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap04-diagrama-04.mmd)

Decidir arquitectura implica observar consecuencias y corregir hipótesis. Iterar no vuelve gratuitas las migraciones; las decisiones difíciles de revertir requieren evidencia y márgenes explícitos.

Ejemplo propio: replicar pedidos de forma síncrona puede reducir pérdida de datos, pero añadir latencia y dificultar aceptar escrituras cuando falla una réplica. Hacerlo de forma asíncrona puede reducir la espera a cambio de una ventana de pérdida. La decisión depende de los objetivos, no del atractivo del mecanismo.

El libro usa seguridad y rendimiento para ilustrar interacciones. No toda mejora de seguridad empeora inevitablemente el rendimiento: el efecto debe medirse. También existen beneficios conjuntos; eliminar datos innecesarios de registros puede reducir exposición y almacenamiento. La iteración permite comprobar qué efectos aparecen realmente. **Fuente del enfoque: PDF pp. 10–11; impresas 64–65.**

---

**Anterior:** [Disponibilidad fiabilidad y recuperación](05%20Disponibilidad%20fiabilidad%20y%20recuperaci%C3%B3n.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Preguntas y ejercicio resuelto](07%20Preguntas%20y%20ejercicio%20resuelto.md)
