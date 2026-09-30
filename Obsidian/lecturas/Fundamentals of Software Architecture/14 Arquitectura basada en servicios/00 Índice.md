---
title: "14 · Arquitectura basada en servicios"
created: 2026-09-29
capitulo: 14
tags:
  - lecturas/software-architecture
  - arquitectura/service-based
  - indice
---

# Arquitectura basada en servicios

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Libro]]

**Este capítulo explica cómo distribuir la aplicación en servicios de dominio amplios, con entregas separadas y una topología de datos flexible.** La pregunta principal es dónde conviene conservar juntas funciones y transacciones, y dónde la independencia de entrega o escala justifica una nueva frontera.

El recorrido integra las diez figuras del capítulo y los ejemplos de compra y Going Green. Incluye ocho imágenes originales en español, diagramas, un laboratorio resuelto y matices técnicos que evitan confundir este estilo con microservicios o convertir sus recomendaciones en leyes.

## Recorrido de lectura

- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/01 Topología y servicios de dominio|01 Topología y servicios de dominio]] — Identificar servicios, instancias, dominios y dependencia común.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/02 Interior fachadas y granularidad|02 Interior fachadas y granularidad]] — Separar la fachada, los módulos internos y el despliegue.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/03 Transacciones ACID y compensaciones|03 Transacciones ACID y compensaciones]] — Entender atomicidad local, compensación y pago remoto incierto.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/04 Interfaces gateway y fronteras|04 Interfaces gateway y fronteras]] — Comparar tres UI y decidir qué debe hacer un gateway.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/05 Topologías de datos y dependencias|05 Topologías de datos y dependencias]] — Elegir datos comunes, agrupados o privados sin ocultar dependencias.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/06 Esquemas bibliotecas y cambios|06 Esquemas bibliotecas y cambios]] — Limitar el radio de cambio con contratos y bibliotecas por dominio.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/07 Operación nube riesgos y gobierno|07 Operación nube riesgos y gobierno]] — Relacionar escala, nube, pools, comunicación y gobierno.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/08 Equipos y características|08 Equipos y características]] — Alinear equipos y comprender cada valoración de la tabla.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/09 Going Green y quanta|09 Going Green y quanta]] — Recorrer el caso completo, sus dos zonas y el matiz de los quanta.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/10 Migración y elección del estilo|10 Migración y elección del estilo]] — Decidir extracciones selectivas con evidencia.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/11 Laboratorio y repaso|11 Laboratorio y repaso]] — Resolver requisitos de ReCompra y comprobar recuperación y capacidad.

## Ideas que conectan las notas

Un servicio puede publicarse por separado y seguir compartiendo base, biblioteca o disponibilidad con otros. La modularidad, el despliegue y el aislamiento operacional son propiedades distintas. Un rollback local solo cubre operaciones participantes de su transacción; un pago remoto introduce otra frontera. La base compartida simplifica algunas consultas, pero sus cambios requieren límites y compatibilidad.

En Going Green, siete servicios se agrupan en dos quanta según el libro; el acceso interno hacia datos públicos exige revisar la independencia operacional en una implementación concreta. En la tabla, tolerancia a fallos tiene tres estrellas aunque una parte de la prosa diga cuatro: la contradicción está documentada, no ocultada.

## Fuente y cobertura

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/11 Arquitectura basada en servicios.pdf#page=1|PDF completo · 18 páginas · impresas 209–226]].

[[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/09 Ampliación capítulo 14|Correspondencia de páginas, figuras, ejemplos, matices y verificación]].

Las notas son explicaciones originales en español. Los ejemplos propios y el laboratorio se identifican dentro del contenido; el PDF conserva intacta la fuente para contrastar.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Libro]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/01 Topología y servicios de dominio|Comenzar →]]

## Comparación transversal

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/07 Comparación visual de módulos filtros plugins y servicios|Módulos, filtros, plugins y servicios]]: dos imágenes, ejemplos y ejercicios que distinguen responsabilidades, despliegues, datos y fallos.
