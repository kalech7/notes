---
title: "Database Internals — Fuentes y cobertura"
created: 2026-09-26
tags:
  - lecturas/database-internals
  - fuentes
---

# Fuentes y cobertura

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice|Fuentes y revisión]]

## Material disponible

El escaneo contiene 74 páginas de la Parte I, *Storage Engines*, de *Database Internals* de Alex Petrov. Empieza con la introducción de la parte y cubre cuatro capítulos:

| PDF | Capítulo | Carpeta de notas |
|---:|---|---|
| 1–6 | Introducción de la Parte I | [[Obsidian/lecturas/database internals/00 Guía y fundamentos/00 Índice|Guía y fundamentos]] |
| 7–22 | 1 · Introduction and Overview | [[Obsidian/lecturas/database internals/01 Introducción y panorama general/00 Índice|Capítulo 1]] |
| 23–41 | 2 · B-Tree Basics | [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/00 Índice|Capítulo 2]] |
| 42–57 | 3 · File Formats | [[Obsidian/lecturas/database internals/03 Formatos de archivo/00 Índice|Capítulo 3]] |
| 58–74 | 4 · Implementing B-Trees | [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/00 Índice|Capítulo 4]] |

**Fuente local:** [[Obsidian/lecturas/database internals/Materiales/Database Internals - Parte I (fuente).pdf]].

## Método de elaboración

El PDF es un escaneo. Se aplicó OCR para recuperar texto y se revisaron visualmente páginas con figuras o texto girado. Las notas no reproducen el libro: reorganizan conceptos, añaden ejemplos propios, diagramas y preguntas.

Las páginas enlazadas en cada nota indican el tramo principal, no una atribución exclusiva. Algunos conceptos se conectan con capítulos anteriores para evitar explicaciones aisladas.

## Límites

- El archivo termina al finalizar el capítulo 4; no se inventaron capítulos posteriores.
- No se afirma que una variante descrita sea universal para todos los motores.
- Los tamaños, claves y layouts de ejemplos son didácticos salvo que se indique lo contrario.
- Mermaid y SVG explican relaciones; no sustituyen el formato exacto de PostgreSQL, SQLite, InnoDB u otro motor.
- La concurrencia y recovery se mencionan cuando afectan el razonamiento, pero sus capítulos completos no están en el escaneo.

> [!important] Alcance de una fuente secundaria
> Estas notas sirven para comprender y repasar. Para implementar un formato compatible con un motor concreto se necesita su especificación y código de la versión exacta.

---

**Índice:** [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice|Fuentes]] · **Siguiente:** [[Obsidian/lecturas/database internals/90 Fuentes y revisión/02 Revisión de estructura y calidad|Revisión de calidad]]
