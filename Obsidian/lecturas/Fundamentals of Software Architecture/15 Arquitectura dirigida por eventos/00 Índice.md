---
title: "15 · Arquitectura dirigida por eventos"
created: 2026-09-29
capitulo: 15
tags:
  - lecturas/software-architecture
  - arquitectura/event-driven
---

# Arquitectura dirigida por eventos

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Libro]]

**Este capítulo explica cómo organizar un sistema que reacciona a hechos mediante procesadores, canales y eventos derivados.** El trabajo puede avanzar en paralelo, y cada consumidor puede responder sin que el productor conozca todas sus tareas. Ese beneficio exige diseñar contratos, contexto, recuperación, orden y consistencia.

Las 55 páginas del escaneo corresponden a las impresas 227–281. Este recorrido desarrolla las 40 figuras y las dos tablas del capítulo con explicaciones originales, trece gráficos PNG en español, diagramas Mermaid, ejemplos paso a paso y preguntas resueltas. Puedes entenderlo desde estas notas; el PDF queda para contrastar referencias.

## Recorrido de lectura

- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/01 Fundamentos y topología broker|01 Fundamentos y topología broker]] — Qué distingue el modelo de solicitudes y la coreografía por eventos.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/02 Pedido del libro y eventos derivados|02 Pedido del libro y eventos derivados]] — Todas las ramas del pedido, incluyendo notificación, pago, almacén y envío.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/03 Eventos mensajes y extensibilidad|03 Eventos mensajes y extensibilidad]] — Hechos, órdenes, consultas y puntos de extensión futuros.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/04 Asincronía difusión y desacoplamiento|04 Asincronía difusión y desacoplamiento]] — Respuesta percibida, trabajo total, difusión y fronteras de disponibilidad.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/05 Payloads con datos o claves|05 Payloads con datos o claves]] — Elegir datos incluidos o una clave que exige recuperar información.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/06 Contratos acoplamiento y eventos anémicos|06 Contratos acoplamiento y eventos anémicos]] — Versionar contratos, calcular tráfico y reconocer falta de contexto.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/07 Payload y granularidad de eventos|07 Payload y granularidad de eventos]] — Separar resultados útiles y evitar el enjambre de eventos.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/08 Errores asíncronos y Workflow Event|08 Errores asíncronos y Workflow Event]] — Delegar fallos, reparar de forma segura y proteger orden por cuenta.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/09 Evitar la pérdida de eventos|09 Evitar la pérdida de eventos]] — Persistencia, confirmaciones, duplicados, idempotencia y doble escritura.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/10 Request-reply y correlación|10 Request-reply y correlación]] — Relacionar solicitudes y respuestas sin confundir transporte con independencia.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/11 Topología mediadora y selección del mediador|11 Topología mediadora y selección del mediador]] — Cuándo coordinar explícitamente y qué tipo de mediador elegir.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/12 Flujo mediado de un pedido|12 Flujo mediado de un pedido]] — Los cinco pasos del pedido y sus tareas paralelas, resultados y checkpoints.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/13 Datos compartidos y bases por dominio|13 Datos compartidos y bases por dominio]] — Base común, caché y aislamiento por dominio con sus dependencias.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/14 Base por procesador y elección de topología|14 Base por procesador y elección de topología]] — Propiedad de datos por procesador y selección razonada de topología.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/15 Nube riesgos y gobernanza|15 Nube riesgos y gobernanza]] — Operación, no determinismo y reglas que protegen la estructura.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/16 Equipos quanta y características|16 Equipos quanta y características]] — Las cuatro topologías de equipos, quanta y cada valoración de la tabla.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/17 Elegir el modelo y caso de subastas|17 Elegir el modelo y caso de subastas]] — Decidir por escenario y entender el flujo Going, Going, Gone.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/18 Laboratorio y repaso resuelto|18 Laboratorio y repaso resuelto]] — Aplicar las decisiones, calcular acumulación y resolver fallos de entrega.

## Tres distinciones que conviene conservar

Aceptar un evento rápidamente y terminar una operación son momentos distintos. Un canal asíncrono puede transportar una solicitud cuya respuesta es necesaria para continuar, conservando una dependencia temporal. Y un evento puede ser una instantánea correcta del pasado aunque el estado actual haya cambiado: el contrato debe decir cuál de los dos representa.

Las ampliaciones sobre outbox, idempotencia, reserva de existencias, concurrencia en subastas y pruebas se identifican como elaboración propia. Ayudan a completar mecanismos que el capítulo simplifica; no se atribuyen al libro.

## Ruta por sesiones

1. Notas 01–04: dibuja el pedido y explica qué significa cada flecha. Distingue el ID devuelto al cliente del pedido preparado o enviado.
2. Notas 05–07: diseña el contrato de un perfil actualizado y explica qué información se perdería al enviar solo su ID.
3. Notas 08–10: coloca fallos antes y después de cada confirmación. Decide si necesitas recuperar, deduplicar o reconciliar.
4. Notas 11–14: compara broker y mediador; después decide quién puede acceder a qué datos y qué fallos se propagan.
5. Notas 15–18: relaciona organización y operación con garantías medibles. Resuelve el laboratorio antes de desplegar las respuestas.

## Fuente y cobertura

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/12 Arquitectura dirigida por eventos.pdf#page=1|Escaneo intacto · 55 páginas]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/10 Ampliación capítulo 15|Mapa completo de páginas, figuras y precisiones]]

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/00 Índice|← Capítulo 14]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/01 Fundamentos y topología broker|Comenzar →]]
