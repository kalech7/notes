---
title: "Parquet, JSON, CSV y archivos de salida"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Parquet, JSON, CSV y archivos de salida

## El formato determina qué trabajo necesita el lector

CSV guarda texto tabular con un separador. JSON guarda texto con estructura y valores como números, cadenas, booleanos y arrays, pero no trae por sí solo un contrato completo de tipos y dominios. Parquet guarda datos en una organización columnar binaria con esquema y metadatos.

| Aspecto | Parquet | JSON | CSV |
|---|---|---|---|
| Inspección humana directa | Requiere lector | Cómoda para objetos | Cómoda para tablas simples |
| Tipos y esquema | Tipos estructurados almacenados | Tipos JSON; contrato adicional necesario | No conserva tipos fuertes |
| Anidamiento | Lo soporta | Natural para arrays/objetos | Requiere aplanar o codificar |
| Lectura de pocas columnas | Puede evitar columnas no pedidas | Normalmente hay que parsear registros | Normalmente hay que parsear filas |
| Uso típico | Analítica | Intercambio de entidades/eventos | Intercambio tabular simple |

Los tres pueden comprimirse con mecanismos adecuados. El tamaño y velocidad exactos dependen de contenido, codec, lector y consulta: no inventes una ventaja fija. La organización columnar suele favorecer la compresión de valores similares y la lectura selectiva para analítica.

```text
Consulta: sumar importe sin usar descripción

Por filas:    [id, importe, descripción] [id, importe, descripción] ...
Por columnas: [id, id, ...] [importe, importe, ...] [descripción, ...]
                              ↑ columnas necesarias
```

Entre Parquet, JSON y CSV, Parquet suele ser la elección para analítica masiva del tipo descrito en el spec. Si el destinatario exige JSON o CSV, ese contrato también cuenta.

## Una ruta de Spark suele ser un directorio

```python
# Fragmentos: df es un DataFrame y salida es una ruta nueva de laboratorio.
df.write.mode("errorifexists").parquet(salida + "/parquet")
df.write.mode("errorifexists").json(salida + "/json")
(df.write.mode("errorifexists").option("sep", "|")
 .option("header", "true").csv(salida + "/csv"))
```

```text
salida/parquet/
├── part-00000-....parquet
├── part-00001-....parquet
└── _SUCCESS                 (según mecanismo de escritura)
```

No esperes que `.csv('reporte.csv')` cree un único archivo con ese nombre. Las tareas escriben archivos `part-*`. El número final depende de particiones de ejecución, particionamiento de salida y opciones del escritor; no siempre es exactamente igual al número inicial de particiones.

## Repartition, coalesce y particiones de carpetas

`repartition(n)` redistribuye y normalmente hace shuffle. `coalesce(n)` puede reducir particiones sin un shuffle general, pero puede concentrar el trabajo. `coalesce(1)` para un resultado pequeño puede ser aceptable; para millones de filas puede crear un cuello de botella. Ni siquiera una partición única garantiza por sí sola el nombre final de archivo que necesita un tercero.

`write.partitionBy('anio')` crea organización física por valores, normalmente con directorios como `anio=2026`. Es distinta de `Window.partitionBy`, que define una competencia lógica, y de `repartition`, que cambia distribución de ejecución. Una columna de cardinalidad enorme puede producir demasiados directorios y archivos pequeños.

## Ejercicio de comparación honesta

Guarda el mismo DataFrame plano en los tres formatos; lee con esquema explícito cuando haga falta. Compara tamaño, filas, esquema y lectura de una sola columna. Para medir, usa una acción que realmente consuma esa columna y registra cache fría/caliente, compresión y entorno. `count()` puede beneficiarse de metadatos y no medir el costo que querías. CSV requiere decisiones para nulos, comillas, separadores en el texto y saltos de línea; un array de structs necesita otra representación.

> [!tip] Regla para recordar
> Elige el formato por lectura y contrato; una ruta de escritura no promete un archivo único.

## Comprueba que lo entendiste

> [!question]- ¿repartition, Window.partitionBy y write.partitionBy hacen lo mismo?
> No. Cambian distribución de tareas, agrupación lógica de una ventana y organización física de salida, respectivamente.

## Conexiones

- [[Obsidian/freelance/Data Engineering/Spark/06 Datos anidados y JSON|06 Datos anidados y JSON]] — aclara JSON distribuido frente a un array único.
- [[Obsidian/freelance/Data Engineering/Spark/09 Parquet y Delta Lake|09 Parquet y Delta Lake]] — añade semántica de tabla sobre archivos.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
