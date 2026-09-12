---
title: "06 Laboratorio razonado y gráficos - M11"
modulo: M11
tags:
  - master/matematicas-programacion
  - m11
---

# 6. Laboratorio: seguir cuatro ejecuciones hasta el ranking

> [!info] Alcance del ejemplo añadido
> Los números de esta nota son **sintéticos**, distintos de los resultados del PDF. El laboratorio ejecutable usa SQLite en memoria y Python estándar para aislar las reglas de cobertura y cardinalidad. No reproduce el proyecto completo de DuckDB/dbt ni vuelve a entrenar un clasificador. No toca tus bases de datos.

## Paso 1. Declarar qué esperamos

Dos configuraciones, A y B, y dos semillas, 11 y 22. Todas corresponden a una única versión y al mismo origen. Debe existir una ejecución por combinación.

| Configuración | Semilla 11 | Semilla 22 |
|---|---|---|
| A | esperada | esperada |
| B | esperada | esperada |

La semilla controla una fuente de aleatoriedad del experimento. Comparar las mismas semillas ayuda a mantener el diseño; dos semillas no bastan para afirmar superioridad general.

## Paso 2. Separar ejecución y medición

| run_id | config_id | seed |
|---|---|---:|
| r1 | A | 11 |
| r2 | A | 22 |
| r3 | B | 11 |
| r4 | B | 22 |

| run_id | accuracy |
|---|---:|
| r1 | 0.60 |
| r2 | 0.80 |
| r3 | 0.70 |
| r4 | 0.90 |

La primera tabla dice **qué se ejecutó**; la segunda **qué se midió**. En el curso, metrics distingue además split y nombre de métrica. Aquí solo existe la métrica objetivo para simplificar.

## Paso 3. Integrar sin cambiar la unidad de fila

Cada ejecución encuentra una medición y una ficha de origen. La población contiene cuatro filas y cuatro run_id distintos. Cada combinación esperada aparece exactamente una vez.

Antes de resumir, comprueba en voz alta: “cada fila todavía representa una ejecución”. Si una corrida aparece dos veces, el JOIN ya alteró la unidad que querías contar.

## Paso 4. Calcular a mano

$$\overline{a}_A=\frac{0.60+0.80}{2}=0.70$$

$$\overline{a}_B=\frac{0.70+0.90}{2}=0.80$$

| Configuración | Media | Semillas | Puesto |
|---|---:|---:|---:|
| B | 0.80 | 2 | 1 |
| A | 0.70 | 2 | 2 |

La diferencia observada es 0.10, es decir, **10 puntos porcentuales** de accuracy. Esta resta describe el ejemplo; no constituye una prueba estadística de superioridad.

![[assets/m11-grafico-ejemplo.svg|1100]]

**Cómo leer el gráfico izquierdo:** las barras representan las medias y los puntos cada semilla. El eje empieza en cero y termina en uno. B queda por encima de A en este conjunto; el gráfico no estima incertidumbre ni demuestra generalización.

**Cómo leer el gráfico derecho:** morado cuenta filas integradas y turquesa ejecuciones distintas presentes en staging. La línea en cuatro recuerda el número esperado. Al duplicar la ficha crecen las filas, pero no los entrenamientos. En el escenario de métrica ausente quedan tres ejecuciones en staging, aunque el registro runs aún tiene cuatro.

## Paso 5. Romper el proceso: quitar una métrica

Eliminamos solo la medición de r2 en la base temporal del laboratorio. La ejecución A/22 sigue existiendo en runs.

| Lugar | Qué se observa |
|---|---|
| diseño | cuatro combinaciones esperadas |
| runs | cuatro ejecuciones |
| metrics | tres mediciones |
| staging con INNER JOIN | tres filas |
| prueba not_null en staging | pasa: las tres métricas presentes no son nulas |
| prueba de cobertura | falla en A/22: encuentra cero coincidencias |

> [!question]- Antes de seguir: ¿puedo promediar A con su única medición y comparar?
> El promedio aritmético sería 0.60, pero no cumple el contrato de comparar ambas semillas. El laboratorio bloquea el ranking. La corrección es recuperar la medición original o declarar incompleto el producto, no aceptar una comparación distinta sin explicarlo.

## Paso 6. Romper el proceso: duplicar la ficha

Cada una de las cuatro ejecuciones encuentra dos fichas. Ahora hay ocho filas y cuatro run_id distintos.

$$\overline{a}_A=\frac{0.60+0.60+0.80+0.80}{4}=0.70$$

La media sigue igual. Fallan la clave de metadatos y la cobertura exacta: cada combinación tiene dos coincidencias en vez de una. El laboratorio deja que se vea la multiplicación para enseñar su efecto; un flujo bien protegido rechazaría esa ficha antes de integrarla.

> [!question]- ¿Podemos aceptar porque el resultado numérico no cambió?
> No. La población dejó de tener una fila por ejecución. La invariancia accidental de la media no repara la cardinalidad ni garantiza que otros cálculos sigan correctos.

## Paso 7. Romper el proceso: dejar metrics vacía

Staging queda vacío. La prueba not_null sigue pasando: no hay valores nulos que encontrar. La prueba de cobertura devuelve cuatro fallos, uno por cada combinación ausente. El laboratorio no genera ranking.

| Escenario verificado | Filas staging | run_id distintos | Fallos de cobertura | Ranking aceptado |
|---|---:|---:|---:|---|
| correcto | 4 | 4 | 0 | sí |
| métrica A/22 omitida | 3 | 3 | 1 | no |
| ficha duplicada | 8 | 4 | 4 | no |
| metrics vacía | 0 | 0 | 4 | no |

## Laboratorio ejecutable y resultados

- [[assets/m11-laboratorio.py|Código Python del laboratorio]].
- [[assets/m11-resultados-verificados.json|Resultados obtenidos y comprobados]].

Desde la carpeta `assets`, se ejecuta con:

```bash
python3 m11-laboratorio.py
```

Solo necesita la biblioteca estándar. Crea bases temporales en memoria y muestra JSON. Las aserciones comprueban el ranking correcto, la ausencia específica A/22, la duplicación 8/4, el caso vacío y la igualdad de dos reconstrucciones independientes.

**Simplificaciones:** un solo dataset y versión; una única métrica; todas las ejecuciones originales son elegibles; no se implementan el parser, Polars, Arrow, DuckDB ni dbt. El control Python que bloquea el ranking ilustra la decisión de aceptación; no prueba el comportamiento de `dbt build`. Para este conjunto fijo se comprueba rango y nulos; el contrato completo de la nota 05 añade finitud explícita.

## Predice cambios antes de ejecutar nada

> [!question]- Si B tuviera 0.50 y 0.90, ¿qué puesto tendría?
> Su media sería 0.70, igual a A. Con RANK ordenando solo por media, ambas tendrían puesto 1. El orden exterior por configuración solo estabiliza la presentación.

> [!question]- Si cambio A/22 por A/33, manteniendo dos filas, ¿pasa cobertura?
> No. A/22 sigue faltando y A/33 no pertenece al diseño. El número de filas no sustituye la identidad de las combinaciones.

> [!question]- Si accuracy de r1 pasa a 1.2, ¿qué control corresponde?
> El dominio de accuracy: está fuera de [0,1]. No es un problema de unicidad ni de cobertura.

> [!question]- ¿Qué dato buscarías primero al fallar A/22?
> La ejecución con esa configuración y semilla dentro de la versión correspondiente. Después, su métrica objetivo usando run_id, split y nombre de métrica. Esa ruta distingue ejecución ausente de medición ausente.

Vuelve a [[05 Pruebas, fallos y reconstrucción - M11]] si alguna predicción resulta confusa. Sigue con [[07 Repaso activo, transferencia y respuestas - M11]].
