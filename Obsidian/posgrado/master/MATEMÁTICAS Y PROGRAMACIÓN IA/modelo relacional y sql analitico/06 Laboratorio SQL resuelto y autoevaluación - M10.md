---
title: Laboratorio SQL resuelto y autoevaluación - M10
modulo: M10
tags:
  - master/matematicas-programacion
  - m10
---

# Laboratorio SQL resuelto y autoevaluación

## La pregunta que queremos responder

**Dentro del dataset d1, ¿qué configuración tiene mayor accuracy media de validación con las semillas 11 y 22, usando solo ejecuciones completadas?** Los datos siguientes son sintéticos y están diseñados para que puedas detectar un error antes de que se esconda en el ranking.

![[assets/m10-21.png|1000]]

Lee la figura como pruebas distintas: unicidad evita doble peso; ausencia revela métricas que no llegaron; rango comprueba la escala; cobertura exige las semillas del diseño. Un solo control no reemplaza a los demás.

## Predice antes de ejecutar

| Configuración | Semilla 11 | Semilla 22 | Estado relevante |
|---|---:|---:|---|
| A | 0.75 | 0.95 | ambas completadas |
| B | 0.85 | 0.85 | ambas completadas |
| C | 0.92 | falta la métrica | ambos runs completados |
| D | 0.70 | 0.80 | ambas completadas |
| E | 0.99 parcial | sin métrica | runs fallidos |

Hay además una semilla 99, otro dataset, una accuracy de train y una loss de validation. Existen para probar que los filtros excluyan observaciones que no responden a la pregunta.

## Archivos listos para practicar

- [[assets/m10-01-datos.sql|Crear tablas y datos sintéticos]]. Define claves primarias, foráneas y unicidad experimental.
- [[assets/m10-02-ranking.sql|Consulta completa de ranking]].
- [[assets/m10-03-ausencias.sql|Detectar la métrica ausente]].
- [[assets/m10-04-cobertura.sql|Contar cobertura, incluso configuraciones con cero semillas válidas]].
- [[assets/m10-laboratorio.py|Ejecutar y verificar con Python y SQLite en memoria]]. No requiere instalar un motor de base de datos separado.
- [[assets/m10-resultados-verificados.txt|Salida de la ejecución verificada]].

Para repetirlo, ejecuta con Python 3 el archivo `m10-laboratorio.py`. Localiza los SQL junto a él automáticamente. Puedes ejecutar los SQL en SQLite siguiendo el orden datos → ranking → auditorías, usando una base nueva.

## Lee la consulta por bloques

```sql
-- Dialecto SQLite. Población objetivo: dataset d1, semillas 11 y 22.
WITH expected_seeds(seed) AS (VALUES (11), (22)),
eligible_runs AS (
  SELECT d.dataset_id, d.version AS dataset_version,
         c.config_id, r.run_id, r.seed, m.metric_value
  FROM datasets AS d
  JOIN runs AS r ON r.dataset_id = d.dataset_id
  JOIN configs AS c ON c.config_id = r.config_id
  JOIN expected_seeds AS es ON es.seed = r.seed
  JOIN metrics AS m
    ON m.run_id = r.run_id
   AND m.split = 'validation'
   AND m.metric_name = 'accuracy'
  WHERE d.dataset_id = 'd1'
    AND r.status = 'completed'
    AND m.metric_value BETWEEN 0 AND 1
),
config_summary AS (
  SELECT dataset_id, dataset_version, config_id,
         AVG(metric_value) AS mean_accuracy,
         COUNT(DISTINCT seed) AS n_seeds
  FROM eligible_runs
  GROUP BY dataset_id, dataset_version, config_id
  HAVING COUNT(DISTINCT seed) = (SELECT COUNT(*) FROM expected_seeds)
),
ranked_configs AS (
  SELECT *, RANK() OVER (
    PARTITION BY dataset_id ORDER BY mean_accuracy DESC
  ) AS performance_rank
  FROM config_summary
)
SELECT dataset_id, config_id, ROUND(mean_accuracy, 4) AS mean_accuracy,
       n_seeds, performance_rank
FROM ranked_configs
ORDER BY dataset_id, performance_rank, config_id;
```

1. `expected_seeds` declara el diseño: 11 y 22.
2. `eligible_runs` conecta identidades y filtra dataset, estado y métrica válida. Una fila conserva una semilla de una configuración.
3. `config_summary` calcula la media y admite solo grupos completos.
4. `ranked_configs` añade posición sin mezclar datasets ni romper empates.
5. `ROUND` aparece al presentar: el ranking se calcula antes de redondear.

Un empate se determina por el valor numérico almacenado, no por cómo se imprime. Con números de punto flotante, medias que son iguales en aritmética decimal pueden diferir mínimamente. En datos reales, declara previamente una precisión o tolerancia de comparación si necesitas ese criterio; no lo elijas después para forzar un empate. Este caso usa valores que producen el empate verificado en SQLite.

Las claves impiden múltiples runs por dataset/config/seed y múltiples métricas objetivo por run. El chequeo de rango excluye accuracy fuera de [0,1]; esa exclusión debe ir acompañada de una investigación, no quedar oculta.

## Solución esperada del caso inicial

> [!question]- Mostrar ranking y explicar las exclusiones
> A y B tienen media 0.85, dos semillas y puesto 1. D tiene media 0.75, dos semillas y puesto 3. C queda fuera por faltar la métrica de la semilla 22. E queda fuera porque no tiene runs completados. Las demás filas no pertenecen al dataset, semillas o métrica objetivo.

## Auditar también lo que quedó fuera

La consulta de ausencia devuelve `c22`. La de cobertura devuelve C con 1/2 y E con 0/2. Para detectar cobertura cero parte del diseño configuración × semillas y usa LEFT JOIN: si partiera solamente de `eligible_runs`, E no existiría en esa relación y no podría contarse.

En este laboratorio todas las configs son candidatas para d1 por construcción. En un proyecto real declara una tabla de configuraciones previstas por dataset antes de hacer ese producto.

## Experimentos que verifica el script

- JOIN sin identidad: 132 filas; JOIN por identidad con el mismo filtro de validation: 11. Este conteo incluye distintas métricas de validation, no es aún la población final del ranking.
- Añadir la métrica faltante de C con 0.80 le da media 0.86 y pasa al primer puesto.
- Cambiar esa métrica a 1.2 la vuelve inválida y C deja de cumplir cobertura.
- Insertar una métrica duplicada o referenciar un run inexistente falla por las restricciones.

Estas modificaciones ocurren en memoria para contrastar causas. La tabla inicial de los archivos no se reescribe.

## Preguntas con respuestas desplegables

> [!question]- ¿Por qué C con 0.92 no gana al principio?
> Tiene una sola métrica válida de las dos semillas requeridas. Una media basada en esa cobertura no cumple el diseño.

> [!question]- ¿Por qué los puestos son 1, 1 y 3?
> RANK mantiene el empate entre A y B; ambas ocupan las dos primeras posiciones y el siguiente puesto es 3.

> [!question]- ¿Qué error produciría añadir config_id al orden de la ventana?
> Rompería el empate aunque las medias fueran iguales. config_id sirve para estabilizar la presentación final, no para definir mérito.

> [!question]- ¿Qué prueba añadir el valor 0.80 de C?
> Que la ausencia causaba su exclusión: al completar la cobertura, su media es (0.92+0.80)/2=0.86 y entra al ranking.

> [!question]- ¿Por qué E requiere partir del diseño para contar cobertura?
> No tiene ninguna ejecución elegible. Si consultas únicamente filas elegibles, no aparece; el diseño proporciona la fila que permite mostrar cero.

> [!question]- ¿A y B son universalmente equivalentes porque empatan?
> No. Empatan en esta media, dataset y semillas. La dispersión de sus valores es diferente y no hemos hecho una prueba estadística.

Fuente conceptual: [[assets/module_10.pdf#page=17|M10, páginas 17–23]]. La base y los resultados son un ejemplo didáctico añadido y ejecutado localmente.

Volver a [[00 Índice - M10 Modelo relacional y SQL analítico]].
