---
title: "Database Internals — De bytes a B-Trees reales"
created: 2026-09-26
autor: "Alex Petrov"
tags:
  - lecturas/database-internals
  - indice
  - bases-de-datos
---

# Database Internals — Ruta de estudio

[[Obsidian/lecturas/00 Índice de lecturas|← Biblioteca de lecturas]]

Esta carpeta desarrolla la **Parte I: Storage Engines** incluida en el PDF disponible: introducción, fundamentos de B-Trees, formatos de archivo e implementación. Cada capítulo está dividido en notas pequeñas; una nota explica un mecanismo o un grupo estrechamente relacionado.

> [!tip] Empieza aquí
> Abre [[Obsidian/lecturas/database internals/00 Guía y fundamentos/01 Antes de empezar bytes páginas y costos|Bytes, páginas y costos]]. Luego sigue el enlace **Siguiente** al final de cada nota. Los índices de capítulo sirven para retomar el estudio sin perder el recorrido.

## Orden de lectura

| Paso | Abre este índice | Para qué sirve |
|---|---|---|
| 0 · Preparación | [[Obsidian/lecturas/database internals/00 Guía y fundamentos/00 Índice\|Guía y fundamentos]] | Aclarar bytes, páginas y offsets; interpretar relaciones gráficas; comparar sistemas y benchmarks con criterios justos |
| 1 · Capítulo 1 | [[Obsidian/lecturas/database internals/01 Introducción y panorama general/00 Índice\|Introducción y panorama general]] | Situar el storage engine dentro del DBMS y relacionar workload con layout |
| 2 · Capítulo 2 | [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/00 Índice\|Fundamentos de B-Trees]] | Entender fanout, búsqueda, splits, redistribución y merges |
| 3 · Capítulo 3 | [[Obsidian/lecturas/database internals/03 Formatos de archivo/00 Índice\|Formatos de archivo]] | Convertir tipos, registros y nodos en bytes y páginas seguras |
| 4 · Capítulo 4 | [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/00 Índice\|Implementación de B-Trees]] | Integrar headers, overflow, breadcrumbs, optimización y mantenimiento |
| 5 · Aplicación | [[Obsidian/lecturas/database internals/05 Práctica y repaso/00 Índice\|Práctica y repaso]] | Resolver un caso completo y comprobar comprensión |
| Consulta | [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice\|Fuentes y revisión]] | Revisar alcance, procedencia de gráficos y material original |

Los números `01`–`04` corresponden a capítulos del PDF. `00`, `05` y `90` son materiales de apoyo. Dentro de cada carpeta, `00 Índice` explica qué aprenderás en cada nota.

## El hilo que une los capítulos

```mermaid
flowchart LR
 A[Workload y arquitectura] -->|necesita acceso eficiente| B[B-Tree abstracto]
 B -->|debe persistirse| C[Bytes y páginas]
 C -->|debe cambiar sin corromperse| D[Implementación real]
 D -->|genera basura y deuda| E[Mantenimiento]
```

**Lo que demuestra el recorrido:** los bloques no son productos alternativos, sino una cadena de decisiones. El workload determina qué trabajo importa; la estructura reduce la búsqueda; el formato la vuelve persistente; los protocolos de modificación conservan invariantes; y el mantenimiento paga el trabajo aplazado.

En cada nota pregunta:

- ¿qué operación costosa se intenta evitar?
- ¿qué metadato permite tomar la decisión?
- ¿qué invariante debe seguir siendo cierta?
- ¿qué nuevo costo introduce la solución?
- ¿qué ocurriría si el proceso falla a la mitad?

## Consultas rápidas

- [[Obsidian/lecturas/database internals/00 Guía y fundamentos/02 Atlas visual explicado|Atlas visual explicado]]: ocho figuras técnicas y cómo interpretarlas.
- [[Obsidian/lecturas/database internals/05 Práctica y repaso/02 Glosario y tarjetas de memoria|Glosario y tarjetas]]: términos y repaso activo.
- [[Obsidian/lecturas/database internals/Mapa de lectura.canvas|Mapa de lectura]]: recorrido visual navegable.
- [[Obsidian/lecturas/database internals/90 Fuentes y revisión/01 Fuentes y cobertura|Fuentes y cobertura]]: páginas del PDF y límites del material.

Las figuras no cumplen una función decorativa. Cada una representa un flujo, layout, transición o costo y está explicada en la nota donde aparece.

> [!success] Señal de comprensión
> Puedes cambiar las claves, tamaños o nombres del ejemplo y seguir prediciendo qué páginas se leen, qué punteros cambian y qué trabajo queda pendiente.
