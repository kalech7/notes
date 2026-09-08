---
title: "Índice - M10 Modelo relacional y SQL analítico"
modulo: M10
tags:
  - master/matematicas-programacion
  - m10
---

# Índice - M10 Modelo relacional y SQL analítico

Este módulo responde: **¿cómo organizo experimentos y escribo una consulta que compare lo que realmente quiero comparar?** Una tabla ordenada puede estar equivocada aunque SQL no produzca errores.

Una **base relacional** organiza información en tablas conectadas mediante claves. **SQL** expresa consultas sobre esas relaciones. Lo decisivo es saber qué representa una fila antes y después de cada operación.

![[assets/m10-06.png|1000]]

Lee el esquema desde `runs`: cada ejecución referencia un dataset y una configuración; una ejecución puede tener muchas métricas. Esa diferencia de multiplicidad explica por qué un JOIN puede aumentar el número de filas.

## Ruta de estudio

1. [[01 Tablas, claves y granularidad de los experimentos]]
2. [[02 Población, NULL y métricas ausentes con LEFT JOIN]]
3. [[03 JOIN, cardinalidad y el peligro de DISTINCT]]
4. [[04 Comparabilidad, GROUP BY y cobertura de semillas]]
5. [[05 CTE, ranking y auditoría de resultados]]
6. [[06 Laboratorio SQL resuelto y autoevaluación - M10]]

| Notas | Páginas del PDF | Núcleo |
|---|---|---|
| 01 | 1–6 | entidades, claves y granularidad |
| 02 | 7–9 | población, NULL y ausencia |
| 03 | 10–13 | pares del JOIN y duplicaciones |
| 04 | 14–16 | condiciones comparables y cobertura |
| 05 | 17–23 | CTE, ranking y controles |
| 06 | integración | base pequeña y consulta ejecutable |

Los ejemplos pequeños añadidos son sintéticos. El laboratorio usa SQLite y conserva las ideas del módulo; no presenta resultados de experimentos reales.

Fuente: [[assets/module_10.pdf|PDF M10]].

Volver a [[../00 INICIO - Qué es cada cosa y ruta maestra de IA]]. Antes: [[../contenedores y ejecucion reproducible con docker/00 Índice - M09 Docker y ejecución reproducible|M09: ejecutar y registrar]].


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- ¿Que una consulta ejecute demuestra que comparó bien?
> No. Puede mezclar datasets, multiplicar filas, omitir métricas ausentes o promediar configuraciones con distinta cobertura de semillas.
