---
title: "Database Internals — Capítulo 2 · Fundamentos de B-Trees"
created: 2026-09-26
libro: "Database Internals"
capitulo: 2
tags:
  - lecturas/database-internals
  - indice
  - b-tree
---

# Capítulo 2 · Fundamentos de B-Trees

[[Obsidian/lecturas/database internals/00 Empieza aquí|← Mapa del libro]]

**Pregunta central:** ¿Cómo convierte un B-Tree el costo físico de leer páginas en búsquedas, inserciones y borrados predecibles?

Lee las notas del 01 al 06. Cada una aísla una pieza del mecanismo y termina enlazando la siguiente, para que puedas reconstruir el árbol desde el hardware hasta sus invariantes.

| Nota | Lo que podrás explicar |
|---|---|
| [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/01 Hardware páginas y árboles de búsqueda\|01 · Hardware, páginas y árboles]] | Por qué un árbol binario razonable en RAM resulta ineficiente en disco y cómo la página física conduce al nodo multivía |
| [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/02 Anatomía fanout altura y ocupación\|02 · Anatomía, fanout, altura y ocupación]] | Cómo separadores, punteros, fanout y espacio libre determinan la forma y el costo del árbol |
| [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/03 Búsqueda puntual y rangos\|03 · Búsqueda puntual y rangos]] | Cómo se elige un único hijo por nivel y por qué las hojas enlazadas vuelven eficientes los recorridos ordenados |
| [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/04 Inserción overflow y split\|04 · Inserción, overflow y split]] | Cómo una inserción local puede dividir páginas, cambiar separadores y propagarse hasta crear una raíz nueva |
| [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/05 Borrado redistribución y merge\|05 · Borrado, redistribución y merge]] | Cuándo basta borrar, cuándo conviene prestar entre hermanos y cuándo una fusión puede reducir la altura |
| [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/06 Invariantes costos y razonamiento\|06 · Invariantes, costos y razonamiento]] | Cómo comprobar que el árbol sigue siendo correcto y estimar su costo con páginas, ocupación y carga de trabajo reales |

> [!tip] Regla de estudio
> No memorices `split` y `merge` como recetas aisladas. En cada paso pregunta qué rango representa la página, qué puntero permite alcanzarla y qué invariante debe seguir siendo verdadero.

**Fuente del bloque:** [[Obsidian/lecturas/database internals/Materiales/Database Internals - Parte I (fuente).pdf#page=23|PDF, capítulo 2, pp. 23–41]].

**Anterior:** [[Obsidian/lecturas/database internals/01 Introducción y panorama general/00 Índice|Capítulo 1]] · **Siguiente:** [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/01 Hardware páginas y árboles de búsqueda|Empezar el capítulo]]
