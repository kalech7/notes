---
title: "Tablas, claves y granularidad de los experimentos"
modulo: M10
tags:
  - master/matematicas-programacion
  - m10
---

# Tablas, claves y granularidad de los experimentos

## Primero separa las cosas del mundo

Imagina que pruebas dos configuraciones de una red, cada una con dos semillas. No tienes dos ejecuciones: tienes cuatro. Cada ejecución puede producir accuracy y loss en train y validation. Esas métricas tampoco son cuatro nuevas ejecuciones.

![[assets/m10-04.png|1000]]

### Cómo leer las cuatro cajas

| Tabla | Una fila representa | Identificador típico |
|---|---|---|
| `datasets` | una versión identificable del dataset | `dataset_id` |
| `configs` | una configuración de entrenamiento | `config_id` |
| `runs` | una ejecución con dataset, config y semilla | `run_id` |
| `metrics` | una medida para una ejecución, split y nombre | `(run_id, split, metric_name)` |

**Granularidad** significa qué representa una fila. **Clave** significa cómo la distingues de otras. Están conectadas, pero responden preguntas distintas.

Ejemplo: «una fila por ejecución» es granularidad. `run_id='r01'` es la identidad concreta de una ejecución.

## Clave primaria y clave foránea

Una **clave primaria** identifica una fila de forma única y no nula. Una **clave foránea** referencia la identidad de una fila en otra tabla.

En `runs`, `dataset_id` apunta a `datasets`; `config_id` apunta a `configs`. En `metrics`, `run_id` apunta a `runs`.

![[assets/m10-06.png|1000]]

Una ejecución puede tener varias métricas: relación uno a muchos. Unir ambas tablas sin filtrar la métrica devuelve varias filas por run; es coherente con esa relación.

## Unicidad experimental

En el diseño del módulo, `(dataset_id, config_id, seed)` se declara único: una ejecución por combinación. Eso permite interpretar una fila elegible como una semilla de una configuración.

Si tu sistema admite reintentos, esa restricción puede dejar de representar la realidad. Tendrías que modelar un identificador de intento y definir una política de selección antes de promediar. No se deben mezclar reintentos como si fueran semillas nuevas.

## Por qué no poner todo en una tabla gigante

Si repites la descripción del dataset en cada métrica, una modificación puede dejar versiones contradictorias. Separar entidades conserva una definición del dataset y conecta las observaciones mediante claves.

Antes de consultar, termina esta frase: «cada fila de mi resultado debería ser…». Si quieres comparar configuraciones, probablemente la salida final tenga una fila por dataset y configuración; no una por métrica individual.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- Una ejecución tiene tres métricas, ¿son tres ejecuciones?
> No. Son tres hechos asociados a la misma ejecución; el run_id puede aparecer tres veces en metrics.

> [!question]- ¿Granularidad y clave son lo mismo?
> No. Granularidad dice qué representa una fila; clave dice cómo identificarla sin ambigüedad.

> [!question]- ¿Qué evita UNIQUE(dataset_id, config_id, seed)?
> En este diseño evita dos ejecuciones para la misma combinación experimental. Un sistema con reintentos necesitaría modelarlos y seleccionar explícitamente.

## Fuente y ruta

Material base: [[assets/module_10.pdf#page=1|M10, páginas 1, 2, 3, 4, 5, 6]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M10 Modelo relacional y SQL analítico]].

## Aplicación en Data Engineering freelance

- [[Obsidian/freelance/Data Engineering/SQL/01 Cómo piensa SQL|01 Cómo piensa SQL]] — Aplicación de granularidad a ventas y partidos.
