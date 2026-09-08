---
title: "CTE, ranking y auditoría de resultados"
modulo: M10
tags:
  - master/matematicas-programacion
  - m10
---

# CTE, ranking y auditoría de resultados

## Divide la consulta en preguntas pequeñas

Una **CTE** es una expresión de tabla con nombre, definida dentro de `WITH`. Hace legible una etapa lógica de la consulta; no implica que se guarde una tabla permanente.

![[assets/m10-17.png|1000]]

| CTE | Pregunta | Una fila representa |
|---|---|---|
| `expected_seeds` | ¿qué semillas pide el diseño? | una semilla |
| `eligible_runs` | ¿qué ejecuciones y métricas son comparables? | dataset + configuración + semilla |
| `config_summary` | ¿qué promedio tiene cada grupo completo? | dataset + configuración |
| `ranked_configs` | ¿qué posición ocupa dentro del dataset? | la misma configuración con una posición añadida |

## Relaciona y filtra antes de resumir

![[assets/m10-18.png|1000]]

Las claves unen datasets/configs/runs/metrics. Los filtros exigen estado completed, split validation y métrica accuracy. El JOIN de semillas restringe al diseño. En esta etapa aún no se promedia: `run_id` conserva trazabilidad.

Usa `dataset_id` como identidad al agrupar. Agrupar solo por una etiqueta textual `version` requiere que esa etiqueta sea única; dos datasets distintos podrían llamarse «v1».

## El ranking compara dentro de una partición

```sql
RANK() OVER (
    PARTITION BY dataset_id
    ORDER BY mean_accuracy DESC
) AS rank_in_dataset
```

`PARTITION BY` separa las competencias por dataset. `ORDER BY ... DESC` pone mayor accuracy primero. Para una métrica donde menor es mejor, como loss, el sentido sería ascendente.

![[assets/m10-20.png|1000]]

Si las medias son $0.90,0.90,0.85$, `RANK` asigna $1,1,3$. `DENSE_RANK` asignaría $1,1,2$. `ROW_NUMBER` asigna números distintos incluso si hay empate.

Para conservar empates de desempeño, no metas `config_id` en el ORDER BY de la ventana. Puedes añadirlo al orden final de presentación para mostrar filas de manera estable sin romper el empate.

## Auditar antes de afirmar

Comprueba claves únicas, métricas ausentes, accuracy dentro de $[0,1]$ bajo esa escala y cobertura completa. Una consulta que devuelve cero errores no acredita estos puntos.

Conserva también los excluidos. Si una configuración desaparece del ranking, la persona que lo lee debe poder saber si faltó una semilla o falló una ejecución.

La conclusión debe enlazar pregunta, población, relación, reducción, comparación y límite. El laboratorio siguiente incluye una consulta completa y datos sintéticos para comprobarlo.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- ¿Una CTE crea una tabla permanente?
> No. Es una relación nombrada dentro de esa sentencia SQL.

> [!question]- ¿Qué devuelve RANK para 0.9, 0.9 y 0.8?
> 1, 1 y 3: los empates comparten puesto y el siguiente rango deja un salto.

> [!question]- ¿Por qué config_id no va en el orden de la ventana?
> Porque diferenciaría filas con la misma media y rompería el empate de desempeño. Puede ir en el ORDER BY final para presentación.

## Fuente y ruta

Material base: [[assets/module_10.pdf#page=17|M10, páginas 17, 18, 19, 20, 21, 22, 23]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M10 Modelo relacional y SQL analítico]].

## Aplicación en Data Engineering freelance

- [[Obsidian/freelance/Data Engineering/SQL/06 Ranking Top N y quintiles|06 Ranking Top N y quintiles]] — Ranking, Top N y quintiles con ejemplos de estudio freelance.
