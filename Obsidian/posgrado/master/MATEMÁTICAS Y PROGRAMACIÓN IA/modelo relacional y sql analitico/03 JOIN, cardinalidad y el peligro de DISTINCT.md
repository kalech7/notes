---
title: "JOIN, cardinalidad y el peligro de DISTINCT"
modulo: M10
tags:
  - master/matematicas-programacion
  - m10
---

# JOIN, cardinalidad y el peligro de DISTINCT

## JOIN construye pares que cumplen una condición

No pega tablas de manera automática. Recorre relaciones: si una fila izquierda cumple `ON` con tres filas derechas, genera tres pares de salida.

![[assets/m10-10.png|1000]]

### Ejemplo pequeño

`runs` tiene `r1` y `r2`. `metrics` tiene `(r1, accuracy, 0.8)`, `(r1, loss, 0.4)` y `(r2, accuracy, 0.9)`. Un JOIN por `run_id` produce tres filas. Eso es correcto si pediste todas las métricas.

La **cardinalidad** describe cuántas filas pueden relacionarse. Para obtener una fila por run debes seleccionar una métrica y split únicos y comprobar que las claves garantizan esa unicidad.

## El filtro no reemplaza la relación

```sql
-- Incorrecto: no relaciona cada métrica con su run.
SELECT r.run_id, m.metric_value
FROM runs AS r
JOIN metrics AS m ON m.split = 'validation';

-- Correcto: relación y población de métricas.
SELECT r.run_id, m.metric_value
FROM runs AS r
JOIN metrics AS m
  ON m.run_id = r.run_id
 AND m.split = 'validation'
 AND m.metric_name = 'accuracy';
```

![[assets/m10-11.png|1000]]

En el JOIN incorrecto, cada run se empareja con todas las métricas de validation, incluso las de otras ejecuciones. Si hay cuatro runs y cuatro métricas de validation, puedes terminar con 16 pares.

## Multiplicidad válida frente a error

![[assets/m10-12.png|1000]]

Cuatro runs con tres métricas cada uno producen 12 filas al consultar todas las métricas. No se ha duplicado mal la identidad: la salida ahora representa `run + split + métrica`. El problema aparece si interpretas esas 12 filas como 12 entrenamientos independientes.

## DISTINCT puede esconder el síntoma

`SELECT DISTINCT r.run_id` elimina identificadores repetidos en la salida, pero no corrige la condición de emparejamiento. Si `r1` se relacionó con la métrica de `r2`, quitar filas repetidas no repara esa atribución.

Antes de usar DISTINCT, explica por qué hay varias filas y qué granularidad necesitas. Si el origen debería tener una sola métrica por run/split/nombre, una restricción de unicidad evita duplicados desde el almacenamiento.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- Cuatro runs y tres métricas por run, ¿cuántas filas da JOIN por run_id?
> Doce, si cada run tiene las tres. La fila representa una métrica de una ejecución.

> [!question]- ¿Filtrar validation basta para asignar cada valor al run correcto?
> No. También necesitas m.run_id = r.run_id.

> [!question]- ¿DISTINCT corrige un JOIN mal relacionado?
> No. Solo elimina filas repetidas según las columnas seleccionadas; puede ocultar el problema.

## Fuente y ruta

Material base: [[assets/module_10.pdf#page=10|M10, páginas 10, 11, 12, 13]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M10 Modelo relacional y SQL analítico]].
