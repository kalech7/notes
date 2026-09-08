---
title: "Población, NULL y métricas ausentes con LEFT JOIN"
modulo: M10
tags:
  - master/matematicas-programacion
  - m10
---

# Población, NULL y métricas ausentes con LEFT JOIN

## Primero decide quién entra en la comparación

La **población** de la consulta es el conjunto de ejecuciones que admite el criterio. Si comparas entrenamientos completados, empieza por filtrar `runs.status = 'completed'`. Después busca sus métricas.

![[assets/m10-07.png|1000]]

Una ejecución fallida no se vuelve elegible porque tenga alguna métrica parcial. Y una completada puede tener un problema de registro: necesitas poder ver que falta su métrica.

## Dos ausencias diferentes

![[assets/m10-08.png|1000]]

- Un atributo `finished_at` con `NULL` existe como campo de una fila, pero no tiene valor conocido.
- Una métrica ausente significa que no hay fila correspondiente en `metrics`.

`NULL` no significa cero, cadena vacía ni falso. Para comprobarlo se escribe `IS NULL`, no `= NULL`.

## LEFT JOIN conserva la población de la izquierda

```sql
SELECT r.run_id, m.metric_value
FROM runs AS r
LEFT JOIN metrics AS m
  ON m.run_id = r.run_id
 AND m.split = 'validation'
 AND m.metric_name = 'accuracy'
WHERE r.status = 'completed';
```

`r` y `m` son alias, nombres cortos para referirnos a las tablas. `ON` define qué pares se corresponden. `WHERE` decide qué filas del resultado conservamos.

![[assets/m10-09.png|1000]]

### Sigue un ejemplo

Si `r1` tiene validation/accuracy $0.8$ y `r2` no tiene esa métrica, el resultado contiene `r1, 0.8` y `r2, NULL`. Un INNER JOIN eliminaría `r2` y escondería esa ausencia.

Si llevas `m.split = 'validation'` a `WHERE`, la fila sin pareja tiene `m.split = NULL` y no cumple la condición: desaparece. Por eso los filtros de la métrica van en `ON` cuando quieres auditar ausencias.

## Ausencia de fila frente a valor nulo

Para listar runs sin esa métrica, añade `AND m.run_id IS NULL` al `WHERE`. La clave derecha permite distinguir «no hay pareja» de «sí hay fila pero metric_value es NULL», si el esquema permite valores nulos.

Antes del ranking sí puedes seleccionar solo métricas válidas. Pero haz visible y cuenta la población excluida: no conviertas un fallo de registro en una mejora aparente del promedio.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- ¿Por qué un LEFT JOIN muestra una métrica ausente?
> Conserva el run de la izquierda y completa columnas derechas con NULL al no encontrar pareja.

> [!question]- ¿Qué pasa si filtro m.split en WHERE?
> Las filas sin pareja no satisfacen el filtro y desaparecen. Para auditar ausencia, filtra la métrica en ON.

> [!question]- ¿NULL equivale a accuracy=0?
> No. Cero es un valor conocido; NULL representa falta de valor. Inventar cero cambia el significado del dato.

## Fuente y ruta

Material base: [[assets/module_10.pdf#page=7|M10, páginas 7, 8, 9]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M10 Modelo relacional y SQL analítico]].
