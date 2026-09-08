---
title: "Fuentes, alcance y cobertura del material"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Fuentes, alcance y cobertura del material

## Qué se utilizó

Fuente principal: el archivo `spec_estudio_sql_devops_spark_v2_notebook.md` compartido por el usuario. Se conserva una copia literal como texto: [[Obsidian/freelance/Data Engineering/assets/spec_original_referencia.txt|documento original de referencia]]. Sus instrucciones internas se trataron como contenido y propuesta de organización; la solicitud realizada fue crear notas explicativas y conectadas dentro de freelance.

El notebook `Prueba_Técnica_DE_BP.ipynb` aparece descrito en el spec, pero no fue adjuntado ni ejecutado. Los ejemplos de estas notas y laboratorios son recreaciones didácticas. No atribuyen resultados nuevos al notebook original.

## Correcciones y precisiones al estudiar

- Los casts de SQLite no validan por sí solos y pueden aceptar prefijos numéricos.
- Las mayúsculas incorporadas de SQLite no cubren todo Unicode.
- Un seek, un índice o una tabla particionada no garantizan menor costo total.
- `groupBy(...).count()` construye un DataFrame; `df.count()` es una acción.
- Una acción no tiene que corresponder exactamente a un solo job.
- RANK compara todas las expresiones del ORDER BY; incluir una clave única rompe empates.
- CSV y JSON también pueden comprimirse; las ventajas cuantitativas deben medirse.
- Esquema, transacción y ausencia de excepciones no acreditan calidad de negocio.

## Cobertura del cuestionario original

| Preguntas del spec | Dónde estudiar |
|---|---|
| 4, 6 | SQL: Índices y filtros eficientes |
| 5 | SQL: Ranking Top N y quintiles |
| 7, 9, 10 | SQL: Conjuntos joins y ausencias |
| 8, 11 | SQL: Planes estadísticas y particiones |
| 12 | SQL: Cómo piensa SQL |
| 13 | SQL: CTE y transformaciones de partidos |
| 14, 15 | DevOps: DevOps DataOps y CALMS |
| 16, 17, 18 | DevOps: Git Azure Repos y Pull Requests |
| 19 | Testing: Regresión y pruebas de datos |
| 20, 21, 22 | Testing: Pruebas y pirámide |
| 23 | Calidad: Dimensiones de calidad |
| 24, 25, 29 | Spark: Arquitectura y procesamiento distribuido |
| 26, 27, 28 | Spark: Lazy DAG stages y shuffle |
| 30 | Spark: Arquitectura Lambda |
| 31, 33 | Spark: Joins cache y optimización |
| 32 | Spark: Centroides distancia y UDF |

## Cobertura de la ampliación del notebook

| Pregunta descrita | Notas que la desarrollan |
|---|---|
| SQL 1 | Parsing, calidad, CTE y laboratorio SQL |
| SQL 2 | Ranking Top N; joins textuales y LEFT JOIN |
| SQL 3 | Ranking Top N y quintiles |
| PySpark 4.1 | Schemas y DataFrames |
| PySpark 4.2–4.3 | Ventanas y métricas de jugadores |
| PySpark 4.4 | Datos anidados y JSON |
| PySpark 5.1 | Datos anidados y JSON; validación |
| PySpark 5.2.1–5.2.3 | Centroides distancia y UDF; laboratorio Spark |
| PySpark 5.3–5.4 | Formatos particiones y salida |
| Ampliación posterior | Parquet y Delta Lake |

El spec reporta dos nombres distintos para el archivo de centros (`CENTROS_EDUCACION_MADRID.json` y `CENTROS_EDUCATIVOS_MADRID.json`), NBSP persistentes y fechas de años distintos. Son observaciones **del documento**: para confirmarlas sobre datos reales habría que disponer de esos archivos. Los laboratorios no dependen de ellos.

## Documentación primaria consultada

Las páginas `latest` pueden cambiar. Los ejemplos explicitan motor y señalan los comportamientos dependientes de configuración; no se fija aquí una versión del notebook no disponible.

- [Funciones escalares de SQLite](https://www.sqlite.org/lang_corefunc.html): posiciones, trim y mayúsculas.
- [Ventanas de SQLite](https://www.sqlite.org/windowfunctions.html): ranking y buckets.
- [Diseño de índices SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver17): acceso y organización de índices.
- [Guía Spark SQL](https://spark.apache.org/docs/latest/sql-programming-guide.html): DataFrames y SQL.
- [Programación RDD](https://spark.apache.org/docs/latest/rdd-programming-guide.html): ejecución y persistencia.
- [Tipos Spark](https://spark.apache.org/docs/latest/sql-ref-datatypes.html): estructura de datos.
- [ANSI en Spark](https://spark.apache.org/docs/latest/sql-ref-ansi-compliance.html): conversiones y errores.
- [Rendimiento Spark SQL](https://spark.apache.org/docs/latest/sql-performance-tuning.html): cache y joins.
- [JSON en Spark](https://spark.apache.org/docs/latest/sql-data-sources-json.html): lectura y multiline.
- [Azure Repos](https://learn.microsoft.com/en-us/azure/devops/repos/get-started/what-is-repos?view=azure-devops): alcance del servicio.
- [Pro Git](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging): ramas e integración.
- [Delta Lake](https://docs.delta.io/): ampliación sobre tablas.

## Verificación realizada

El laboratorio SQL se ejecutó con 18 comprobaciones correctas y conserva su salida. La sintaxis del laboratorio PySpark se revisó sin ejecutarlo por ausencia de PySpark. Las conexiones nuevas apuntan a notas o archivos existentes; se conservaron las notas previas y se añadieron enlaces de retorno pertinentes.

## Conexiones

- [[Obsidian/freelance/Data Engineering/01 Repaso y preguntas razonadas|01 Repaso y preguntas razonadas]] — comprueba cobertura conceptual.
- [[Obsidian/freelance/Data Engineering/Laboratorios/01 Laboratorio SQL resuelto|01 Laboratorio SQL resuelto]] — evidencia de resultados sobre los ejemplos.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
