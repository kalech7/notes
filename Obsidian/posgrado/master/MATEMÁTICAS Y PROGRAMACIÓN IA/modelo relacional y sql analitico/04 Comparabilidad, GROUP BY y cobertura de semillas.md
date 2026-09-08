---
title: "Comparabilidad, GROUP BY y cobertura de semillas"
modulo: M10
tags:
  - master/matematicas-programacion
  - m10
---

# Comparabilidad, GROUP BY y cobertura de semillas

## Un promedio solo compara bien si sus observaciones son comparables

Antes de calcular la media, fija dataset/versión, estado de ejecución, split, nombre de métrica y semillas esperadas. Una accuracy de train y una de validation responden preguntas distintas.

![[assets/m10-14.png|1000]]

Lee los bloques como puertas: misma versión, ejecución elegible, mismo split, misma métrica y conjunto de semillas acordado. Solo después tiene sentido resumir.

## GROUP BY cambia la granularidad

Si antes tienes una fila por `(dataset, config, seed)`, al agrupar por `(dataset, config)` obtienes una fila por configuración dentro de ese dataset.

```sql
SELECT dataset_id, config_id,
       AVG(metric_value) AS mean_accuracy,
       COUNT(DISTINCT seed) AS n_seeds
FROM eligible_runs
GROUP BY dataset_id, config_id;
```

`eligible_runs` representa aquí una relación previamente filtrada, no una tabla que aparezca mágicamente. En la nota siguiente se construye mediante una CTE.

Ejemplo: A tiene $0.80$ y $0.90$ con semillas 11 y 22. Su media es $(0.80+0.90)/2=0.85$. B tiene solo $0.92$ con semilla 11. Ordenar $0.92>0.85$ ignora que falta la segunda observación de B.

## HAVING comprueba grupos

![[assets/m10-16.png|1000]]

`WHERE` filtra filas antes del agrupamiento. `HAVING` filtra grupos después de calcular agregados.

```sql
HAVING COUNT(DISTINCT seed) =
       (SELECT COUNT(*) FROM expected_seeds)
```

Esta condición comprueba cobertura **si antes restringiste las semillas al conjunto esperado**, y si ese conjunto no contiene duplicados. Esperar `{11,22}` y observar `{11,99}` da dos semillas, pero no las semillas correctas. El JOIN con `expected_seeds` evita ese error.

## El conteo tampoco reemplaza la unicidad

Si una semilla aparece dos veces, `COUNT(DISTINCT seed)` puede ser correcto y `AVG` seguir sesgado por el duplicado. Necesitas una fila por unidad experimental y una métrica objetivo por run.

Además, `AVG` ignora valores NULL. Por eso una métrica con valor desconocido debe investigarse o excluirse antes de verificar cobertura; contar su semilla como completa daría una falsa garantía.

## Qué permite concluir

Una media mayor es un resultado descriptivo bajo ese protocolo. No prueba significancia estadística ni superioridad universal. Conserva dispersión y resultados por semilla para análisis posteriores; el módulo se centra en que la comparación SQL tenga una población coherente.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- ¿Por qué B con 0.92 y una sola semilla no gana automáticamente?
> Falta cobertura del diseño. Su media no usa el mismo conjunto de semillas que A.

> [!question]- ¿Dos semillas observadas siempre cumplen un diseño de dos semillas?
> No. Deben ser las semillas esperadas. Primero se restringe la población a ese conjunto y luego se cuenta.

> [!question]- ¿COUNT(DISTINCT seed) impide que una fila duplicada sesgue AVG?
> No. El conteo puede seguir igual y el promedio dar doble peso a una semilla. También se audita unicidad.

## Fuente y ruta

Material base: [[assets/module_10.pdf#page=14|M10, páginas 14, 15, 16]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M10 Modelo relacional y SQL analítico]].
