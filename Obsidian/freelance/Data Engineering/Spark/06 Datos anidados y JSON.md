---
title: "Arrays, structs y JSON sin saturar el Driver"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Arrays, structs y JSON sin saturar el Driver

## De filas a una entidad con hijos

En una tabla plana, cada fila puede representar un jugador de un país. Para una API o exportación, puede resultar más cómodo tener una fila por país con un array de jugadores. Un **struct** reúne campos de una entidad; un **array** reúne varios elementos de un mismo tipo. Un array de structs permite tener varios jugadores, cada uno con nombre y ranking.

```text
EC | Ana  | 2                 EC | jugadores:
EC | Luis | 1       →              [{ranking: 1, nombre: Luis},
                                   {ranking: 2, nombre: Ana}]
```

## Construcción y orden explícito

```python
# Ejemplo después de crear una SparkSession.
from pyspark.sql import functions as F
filas = spark.createDataFrame(
 [("EC", "Ana", 2), ("EC", "Luis", 1)],
 "pais string, nombre string, ranking int"
)
anidado = filas.groupBy("pais").agg(
 F.sort_array(F.collect_list(
   F.struct(F.col("ranking"), F.col("nombre"))
 )).alias("jugadores")
)
anidado.show(truncate=False)
anidado.createOrReplaceTempView("paises_anidados")
spark.sql("""
 SELECT pais, TRANSFORM(jugadores, j -> j.nombre) AS nombres
 FROM paises_anidados
""").show(truncate=False)
```

`collect_list` agrega valores en un array por grupo y conserva duplicados. Su orden puede cambiar tras un shuffle. Por eso ordenamos el array **después** de agrupar. En el ejemplo los structs empiezan por ranking: su orden natural compara primero ese campo y luego nombre. Si existen empates completos o necesitas otra prioridad, incluye las claves apropiadas o expresa un comparador.

En Spark SQL, `NAMED_STRUCT('ranking', ranking, 'nombre', nombre)` construye el mismo tipo de estructura. `TRANSFORM` aplica una expresión a cada elemento del array, sin escribir un bucle Python por fila. `LPAD('1', 2, '0')` produce `01` para presentación; no conviertas IDs arbitrarios a ancho fijo si pueden truncarse o perder identidad.

## Dos collect muy diferentes

| Operación | Dónde queda el resultado | Riesgo |
|---|---|---|
| collect_list en una agregación | Array dentro del resultado distribuido | Un grupo enorme puede agotar memoria de una tarea |
| DataFrame.collect | Lista de filas en el Driver | Todo el resultado debe caber en su memoria |
| DataFrame.toJSON | Representación JSON distribuida por fila | Aún no equivale a un único archivo JSON |
| df.write.json | Salida escrita por tareas | Produce archivos de salida distribuidos |

`toJSON().collect()` trae todas las cadenas al Driver. Es razonable para un resultado explícitamente pequeño; no escala por el hecho de haber usado Spark antes. Si necesitas un array JSON único de pocas filas, puedes ensamblarlo localmente, pero deja claro ese contrato de tamaño. Para grandes volúmenes escribe distribuido y acuerda el formato con quien consume los datos.

## JSON por línea frente a multiline

```text
JSON por línea:                 Un documento multiline:
{"pais":"EC"}                  [
{"pais":"PE"}                    {"pais":"EC"},
                                   {"pais":"PE"}
                                 ]
```

Spark lee normalmente un registro JSON por línea. Usa `.option('multiLine', 'true')` cuando cada archivo contiene un documento que ocupa varias líneas, como un array formateado. No es un botón para arreglar JSON inválido. El formato físico afecta cómo se puede dividir y paralelizar la lectura; comprueba errores y esquema al leer. Referencia: [JSON en Spark](https://spark.apache.org/docs/latest/sql-data-sources-json.html).

## Ejercicio

Convierte cliente/producto/precio a un array de productos por cliente. Define si dos compras idénticas deben conservarse: `collect_list` no deduplica, y reemplazarlo por un conjunto puede borrar compras reales.

> [!tip] Regla para recordar
> Anidar cambia la forma; collect cambia dónde viven los datos.

## Comprueba que lo entendiste

> [!question]- ¿collect_list y collect tienen el mismo efecto sobre el Driver?
> No. collect_list agrega un array por grupo dentro del cálculo distribuido; collect trae el resultado completo al Driver. Ambos pueden tener problemas de memoria, en lugares distintos.

## Conexiones

- [[Obsidian/freelance/Data Engineering/Spark/05 Ventanas y métricas de jugadores|05 Ventanas y métricas de jugadores]] — produce las filas que se agrupan por país.
- [[Obsidian/freelance/Data Engineering/Spark/08 Formatos particiones y salida|08 Formatos particiones y salida]] — explica el contrato físico de salida.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
