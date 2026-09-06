---
title: Árboles, Random Forest y boosting
tags:
  - master/matematicas-programacion
  - machine-learning
  - arboles
  - ensembles
---

# Árboles, Random Forest y boosting

## Árbol de decisión

Un árbol divide el espacio mediante preguntas:

```text
velocidad_media <= 420?
├─ sí: pausas <= 5?
│  ├─ sí: legítimo
│  └─ no: sospechoso
└─ no: curvatura > 0.8?
   ├─ sí: sospechoso
   └─ no: legítimo
```

Cada hoja contiene una predicción basada en ejemplos que llegaron allí.

## Impureza

Para clasificación, Gini:

$$G=1-\sum_{k=1}^Kp_k^2.$$

Una hoja pura tiene $G=0$. Una división busca gran reducción ponderada de impureza:

$$\Delta G=G_{padre}-\frac{n_L}{n}G_L-\frac{n_R}{n}G_R.$$

## Por qué sobreajustan

Un árbol profundo puede crear hojas con muy pocos casos. Controles:

- `max_depth`;
- `min_samples_leaf`;
- `min_samples_split`;
- poda;
- validación agrupada.

## Random Forest

Combina árboles entrenados con:

1. muestras bootstrap;
2. subconjuntos aleatorios de características;
3. promedio o voto.

Promediar modelos poco correlacionados reduce varianza.

Si cada árbol tiene varianza $\sigma^2$ y correlación media $\rho$, la varianza del promedio de $M$ árboles se aproxima a:

$$\rho\sigma^2+\frac{1-\rho}{M}\sigma^2.$$

Muchos árboles reducen la parte no correlacionada, pero no eliminan errores compartidos.

## Boosting

Boosting construye modelos secuencialmente. Cada etapa intenta corregir residuos o gradientes del conjunto anterior:

$$F_m(x)=F_{m-1}(x)+\eta h_m(x).$$

| Método | Entrenamiento | Efecto principal |
|---|---|---|
| bagging / Random Forest | paralelo | reduce varianza |
| boosting | secuencial | reduce sesgo y ajusta errores difíciles |

## Importancia de características

La importancia por impureza puede favorecer variables continuas o con muchos puntos de corte. La importancia por permutación pregunta cuánto empeora la métrica al romper una variable, pero también se complica con variables correlacionadas.

> [!warning] Importancia no es causalidad
> Un predictor puede ser útil porque actúa como proxy. El árbol no demuestra que modificar esa variable cause un cambio en el resultado.

## Probabilidades de árboles

La fracción de clases en hojas produce números entre 0 y 1, pero pueden estar mal calibrados. Un modelo puede ordenar bien riesgos y aun asignar probabilidades demasiado extremas.

## Autoevaluación

1. ¿Qué mide Gini?
2. ¿Por qué un Random Forest reduce varianza?
3. ¿Qué diferencia estructural hay entre bagging y boosting?
4. ¿Por qué importancia no implica causalidad?

---

Anterior: [[03 Generalización, sesgo-varianza y regularización]] · Siguiente: [[05 Métricas, umbrales, calibración y validación]]

