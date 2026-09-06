---
title: Laboratorio y autoevaluación - Probabilidad para IA
tags:
  - master/matematicas-programacion
  - probabilidad
  - laboratorio
related:
  - "[[../laboratorios fundamentos ia/probabilidad_desde_cero.py]]"
---

# Laboratorio y autoevaluación: probabilidad para IA

## Objetivo

Conectar conteos, Bayes, simulación, CLT y cross-entropy sin depender de una librería estadística.

Archivo ejecutable: [[../laboratorios fundamentos ia/probabilidad_desde_cero.py]].

## Experimento 1: Bayes mediante conteos

Construye cuatro conteos:

```text
TP: impostor con alarma
FN: impostor sin alarma
FP: legítimo con alarma
TN: legítimo sin alarma
```

Calcula:

$$P(A\mid I)=\frac{TP}{TP+FN},\qquad
P(I\mid A)=\frac{TP}{TP+FP}.$$

Predice cuál será menor cuando los impostores sean raros.

## Experimento 2: media muestral

1. Genera valores Bernoulli.
2. Calcula medias con $n=10$, $100$ y $1000$.
3. Repite cada tamaño muchas veces.
4. Compara la dispersión de las medias.

Esperas que:

$$\operatorname{SD}(\bar X)\approx\sqrt{p(1-p)/n}.$$

## Experimento 3: pérdida logarítmica

Para etiqueta verdadera $y=1$, compara:

```python
p_correctas = [0.99, 0.8, 0.5, 0.2, 0.01]
```

La pérdida debe crecer de manera no lineal al acercarse a cero.

## Experimento 4: estabilidad

Compara `exp(1000)` con softmax estable. La primera operación desborda; restar el máximo conserva las probabilidades.

## Tabla de predicciones antes de ejecutar

| Prueba | Predicción | Evidencia esperada |
|---|---|---|
| más repeticiones | media más estable | menor desviación entre medias |
| evento raro | PPV menor que recall | muchas falsas alarmas en la base grande |
| confianza errónea | pérdida muy grande | $-\log(p)$ diverge al acercarse a 0 |
| restar máximo | misma distribución | diferencia numérica cercana a 0 |

## Preguntas de dominio

1. Diferencia entre resultado, evento y variable aleatoria.
2. Diferencia entre probabilidad y verosimilitud.
3. Diferencia entre media poblacional y media muestral.
4. Diferencia entre desviación estándar y error estándar.
5. Qué afirma y qué no afirma el CLT.
6. Por qué cross-entropy penaliza confianza equivocada.
7. Por qué KL no es simétrica.
8. Por qué softmax necesita estabilidad numérica.

> [!question]- Respuestas condensadas
> 1. Posibilidad completa, conjunto de posibilidades y función numérica sobre resultados. 2. En probabilidad varía el dato; en verosimilitud se comparan parámetros con el dato fijo. 3. Parámetro del proceso frente a estimador calculado. 4. Dispersión de observaciones frente a incertidumbre de una media. 5. Aproxima la distribución de un estimador bajo condiciones; no vuelve normales los datos. 6. Porque usa logaritmo negativo. 7. Cambia qué distribución pondera el promedio. 8. Los exponenciales pueden desbordar aunque el cociente final sea válido.

## Criterio de finalización

- [ ] Puedo construir una tabla $2\times2$ y declarar cada denominador.
- [ ] Puedo derivar BCE desde Bernoulli.
- [ ] Puedo explicar $1/\sqrt n$.
- [ ] Puedo distinguir entropía, cross-entropy y KL.
- [ ] Ejecuté el laboratorio y sus aserciones pasaron.

---

Anterior: [[03 Verosimilitud, entropía, cross-entropy y KL]] · Volver al [[00 Índice y recordatorio - Probabilidad para IA]]

