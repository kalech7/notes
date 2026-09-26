---
title: "DDIA — Capítulo 4 · Almacenamiento y recuperación"
created: 2026-09-25
tags:
  - lecturas/ddia
  - indice
---

# Capítulo 4 · Almacenamiento y recuperación

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|← Inicio del libro]]

**Pregunta central:** Cómo guardar un dato, encontrarlo y recuperarlo tras un fallo.

Lee las notas del 01 al 07. El número de cada nota ordena el estudio dentro del capítulo. Los enlaces al pie permiten avanzar sin volver a buscar en la carpeta.

| Nota | Lo que podrás explicar |
|---|---|
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/01 Del log al índice\|01 · Del log al índice]] | Por qué guardar al final es fácil y encontrar la última versión puede ser caro |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/02 LSM SSTables compactación y Bloom\|02 · LSM, SSTables y Bloom]] | Cómo memoria, archivos ordenados y compactación colaboran; por qué Bloom dice “quizá” |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/03 B-trees WAL y costos de almacenamiento\|03 · B-trees, WAL y costos]] | Cómo buscar por páginas, dividir hojas y comparar amplificaciones |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/04 Índices secundarios cobertura y memoria\|04 · Índices secundarios y cobertura]] | Por qué localizar una fila no siempre equivale a recuperar toda la respuesta |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/05 Almacenamiento columnar y compresión\|05 · Columnas, bitmaps y compresión]] | Cómo leer menos columnas, combinar condiciones y mantener las filas correctamente alineadas |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/06 Lagos de datos ejecución y vistas materializadas\|06 · Lagos, ejecución y vistas]] | Qué hacen formatos, catálogos, motores, vectorización y resultados precalculados |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/07 Índices espaciales texto completo y vectores\|07 · Espacio, palabras y vectores]] | Cómo funcionan regiones, postings, IVF y HNSW; qué errores introduce la aproximación |

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/01-btree-y-lsm.png|900]]

*Imagen para recordar: navegar por páginas frente a acumular y fusionar segmentos. Es una analogía; las notas desarrollan los mecanismos y sus excepciones.*

## Complemento opcional

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/08 Complemento - Cómo leer el gráfico de proyección|08 · Cómo leer el gráfico de proyección]]: consúltalo al estudiar la nota 05, sobre columnas. Explica el cálculo de bytes y sus límites; no añade una octava etapa obligatoria.


**Al terminar:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/00 Índice|Continuar con el capítulo 5]].
