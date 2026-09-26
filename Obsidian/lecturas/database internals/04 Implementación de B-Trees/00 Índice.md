---
title: "Database Internals — Capítulo 4 · Implementación de B-Trees"
created: 2026-09-26
tags:
  - lecturas/database-internals
  - indice
---

# Capítulo 4 · Implementación de B-Trees

[[Obsidian/lecturas/database internals/00 Empieza aquí|← Inicio del libro]]

**Pregunta central:** ¿Cómo se convierte el algoritmo abstracto del B-Tree en páginas que pueden buscarse, modificarse, recuperarse y mantenerse en disco?

Lee las notas del 01 al 06. Cada una aísla un mecanismo para que puedas estudiarlo sin cargar todo el capítulo a la vez.

| Nota | Lo que podrás explicar |
|---|---|
| [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/01 Headers magic numbers y enlaces laterales\|01 · Headers, magic numbers y enlaces]] | Cómo una página se describe a sí misma y por qué enlazar hermanos acelera recorridos pero amplía el costo de un cambio |
| [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/02 Rightmost pointers high keys y overflow\|02 · Rightmost, high keys y overflow]] | Por qué hay `N + 1` hijos, cómo expresar el último intervalo y cómo guardar payloads grandes |
| [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/03 Búsqueda binaria y breadcrumbs\|03 · Búsqueda y breadcrumbs]] | Cómo buscar sobre offsets y recordar el camino para propagar un split o merge |
| [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/04 Rebalanceo right-only y bulk loading\|04 · Rebalanceo y carga ordenada]] | Cuándo mover entre hermanos, aprovechar claves crecientes o construir el árbol desde abajo |
| [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/05 Compresión vacuum y freelist\|05 · Compresión y mantenimiento]] | Por qué espacio libre total no equivale a espacio utilizable y cómo se recupera de forma segura |
| [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/06 Flujo completo e invariantes\|06 · Flujo completo e invariantes]] | Integrar todos los mecanismos en un insert y auditar la corrección de una implementación |

![[Obsidian/lecturas/database internals/Recursos visuales/04-vacuum-page.svg|1000]]

*Lo que demuestra la imagen:* a la izquierda existen bytes libres, pero ningún tramo contiguo suficiente; a la derecha, vacuum conserva las celdas vivas y reúne el espacio en un intervalo utilizable. La transformación no es cosmética: cambia si una escritura cabe. La nota 05 explica por qué MVCC decide cuándo esa recolección es segura.

**Al terminar:** [[Obsidian/lecturas/database internals/05 Práctica y repaso/00 Índice|Continuar con práctica y repaso]].
