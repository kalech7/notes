---
title: "Schemas, DataFrames y vistas temporales en PySpark"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Schemas, DataFrames y vistas temporales en PySpark

## Lee la transformación fila por fila

En el ejemplo de esta nota, la entrada conserva edad como texto. Tras la conversión esperas:

| id | edad_texto original | edad numérica | edad_conversion_invalida |
|---|---|---:|---|
| 1 | `25` | 25 | false |
| 2 | `abc` | NULL | true |
| 3 | NULL | NULL | false |

La última fila no es una conversión fallida: no había texto para convertir. El booleano se obtiene preguntando **«¿había un original y aun así no obtuve número?»**.

`StructType` describe el conjunto de campos; cada `StructField` describe uno. En `StructField("id", StringType(), False)`, las tres piezas son nombre, tipo y permiso de nulos. Eso no impone que los IDs sean únicos: esa regla requiere otro control.

`F.col("edad")` representa una referencia a la columna dentro de una expresión. `withColumn` describe un DataFrame con una columna añadida o reemplazada; no es un bucle que traiga cada edad a Python. Lee el código como operaciones sobre tablas.

## Qué representa un DataFrame

Un DataFrame es una colección distribuida organizada en columnas con un schema. El schema define nombres, tipos y nulabilidad; describe estructura, no toda la validez del negocio. `nullable=True` permite nulos en ese campo; no significa que un país desconocido o un número negativo sean aceptables.

```python
from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import StructType, StructField, StringType

spark = SparkSession.builder.master("local[2]").appName("EstudioDE").getOrCreate()
schema = StructType([
    StructField("id", StringType(), False),
    StructField("edad_texto", StringType(), True),
    StructField("salario_texto", StringType(), True),
])
datos = [("1", "25", "1200.5"), ("2", "abc", "900"), ("3", None, "1500")]
raw = spark.createDataFrame(datos, schema)
# try_cast: comprobar soporte en la versión del entorno.
tipado = raw.select(
    "*",
    F.expr("try_cast(edad_texto AS INT)").alias("edad"),
    F.expr("try_cast(salario_texto AS DOUBLE)").alias("salario"),
)
revisado = tipado.withColumn(
    "edad_conversion_invalida",
    F.col("edad_texto").isNotNull() & F.col("edad").isNull(),
)
revisado.show()
```

La fila 2 tiene una conversión inválida; la fila 3 tiene ausencia de origen. Separarlas sirve para no culpar al parser de un campo que nunca llegó. Un `cast` común puede fallar bajo ANSI, por eso aquí se solicita conversión tolerante explícita. Aun así, `-5` podría convertirse bien a entero y ser una edad inválida: añade una regla de dominio.

## Tipar antes de calcular

El orden textual puede situar `"100"` antes de `"20"`; el orden numérico dice lo contrario. Una operación aritmética sobre strings puede depender de conversiones implícitas. Elige tipos antes de rankear y conserva el original. Para dinero real, un tipo decimal con precisión/escala definidas suele representar mejor el contrato que DOUBLE; aquí salario solo ilustra una conversión.

## SQL y DataFrame API

```python
revisado.createOrReplaceTempView("personas_estudio")
por_sql = spark.sql("SELECT id, edad FROM personas_estudio WHERE edad >= 18")
por_api = revisado.filter(F.col("edad") >= 18).select("id", "edad")
```

Las dos formas expresan el mismo cálculo con el mismo motor. La vista temporal local pertenece a la sesión y no crea una tabla permanente ni un archivo; reemplazar su nombre tampoco materializa una copia. No supongas que una vista temporal seguirá disponible al abrir otra sesión. El esquema explícito facilita detectar desviaciones frente a inferirlo de una muestra, pero sigue siendo necesario validar valores.

## Errores comunes y práctica

No confundas nombres de columnas con variables Python. `F.col('edad')` construye una expresión de columna; no contiene una lista de edades. Los DataFrames se transforman produciendo otros DataFrames, no editando una fila local en un bucle.

Añade edades vacías, negativas y fuera de rango; crea una columna `motivo`. Cuenta aceptadas y rechazadas y verifica que no desaparezcan filas silenciosamente. El laboratorio posterior muestra ejemplos ejecutables como secuencia completa.

> [!tip] Regla para recordar
> El schema dice qué tipo esperas; la validación dice si el valor sirve.

## Comprueba que lo entendiste

> [!question]- ¿createOrReplaceTempView guarda el DataFrame como un archivo?
> No. Registra una vista temporal para consultar mediante SQL dentro de la sesión.

## Conexiones

- [[Obsidian/freelance/Data Engineering/Calidad/02 Validación Unicode y contratos|02 Validación Unicode y contratos]] — separa estructura, conversión y significado.
- [[Obsidian/freelance/Data Engineering/Spark/05 Ventanas y métricas de jugadores|05 Ventanas y métricas de jugadores]] — usa columnas tipadas para obtener rankings.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].

## Lectura relacionada: DDIA

- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/03 Conexiones con mis otras notas#4. Schemas y JSON: leer hoy no demuestra compatibilidad mañana|DDIA: evolución de schemas]] — Extiende estructura y validación hacia lectores y escritores de distintas versiones, campos ausentes y cambios de significado.
