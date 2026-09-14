---
title: "15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números"
tags:
  - maestria/ia-generativa
  - estudio
---

# 15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Continúa:** [[05 S01 - Probabilidad y teorema de Bayes paso a paso]]. Este desarrollo explica las ideas necesarias aquí; abrir el libro es opcional.

## 1. Dos incertidumbres distintas

Una moneda puede ser aleatoria aunque conozcas perfectamente su probabilidad de cara. Si esa probabilidad es 0.5, conocerla no te permite predecir con certeza el siguiente lanzamiento.

Además, puedes no conocer esa probabilidad. Representamos el valor desconocido mediante $\theta$. Aprender sobre $\theta$ y predecir el siguiente lanzamiento son problemas relacionados, pero diferentes.

## 2. Una distribución sobre probabilidades

La distribución Beta describe valores entre 0 y 1, así que sirve como modelo de incertidumbre sobre $\theta$. Sus dos parámetros, $\alpha$ y $\beta$, controlan su forma:

$$p(\theta)=\frac{\theta^{\alpha-1}(1-\theta)^{\beta-1}}{B(\alpha,\beta)},\qquad 0<\theta<1.$$

No necesitas calcular $B$ para hacer este ejemplo: es la constante que hace que el área total sea 1. Beta(1,1) es uniforme; Beta(2,2) concentra más densidad hacia el centro. No son distribuciones sobre resultados «cara o cruz», sino sobre los posibles valores de su probabilidad.

## 3. Actualizar significa sumar evidencia

Si el prior es Beta($\alpha,\beta$), observas h caras y c cruces, y supones lanzamientos independientes con el mismo $\theta$, la posterior es:

$$p(\theta\mid D)=\operatorname{Beta}(\alpha+h,\beta+c).$$

¿Por qué? La verosimilitud aporta $\theta^h(1-\theta)^c$. Multiplicarla por el prior suma exponentes. La forma Beta se conserva: por eso este prior se llama **conjugado** para la verosimilitud Bernoulli/binomial.

Con Beta(1,1), siete caras y tres cruces:

$$\operatorname{Beta}(1+7,1+3)=\operatorname{Beta}(8,4).$$

No se eligió todavía un único valor: se obtuvo una distribución.

## 4. MLE, MAP y media posterior

| Operación | Qué hace | Resultado del ejemplo |
| --- | --- | --- |
| MLE | Maximiza la verosimilitud | 7/10 = 0.7 |
| MAP | Maximiza la posterior | (8−1)/(8+4−2) = 0.7 |
| Media posterior | Promedia valores según la posterior | 8/(8+4) ≈ 0.667 |

La fórmula interior de la moda Beta utilizada aquí exige ambos parámetros mayores que 1; en casos de frontera no debes aplicarla mecánicamente. MAP coincide con MLE en este ejemplo porque el prior es uniforme, no porque sean siempre equivalentes.

Con un prior Beta(2,2) y los mismos datos, la posterior sería Beta(9,5), MAP = 8/12 ≈ 0.667 y media = 9/14 ≈ 0.643. Los datos son iguales; cambió la información previa.

## 5. Predecir el siguiente resultado

La predicción bayesiana promedia la probabilidad de cara sobre los valores posibles de $\theta$:

$$P(\text{cara siguiente}\mid D)=\int_0^1\theta p(\theta\mid D)\,d\theta
=\frac{\alpha+h}{\alpha+\beta+h+c}.$$

En el primer ejemplo es 8/12. Con tres caras y cero cruces, usando Beta(1,1), es 4/5. La cruz conserva probabilidad 1/5.

El contraste con MLE es instructivo: el ajuste puntual 3/3=1 no deja espacio para una cruz. La actualización bayesiana refleja que tres observaciones no bastan para justificar esa certeza bajo el prior elegido.

## 6. La incertidumbre cambia con la cantidad de datos

Para una Beta con parámetros posteriores a y b:

$$\operatorname{Var}(\theta\mid D)=\frac{ab}{(a+b)^2(a+b+1)}.$$

Beta(8,4) tiene varianza aproximadamente 0.01709 y desviación estándar 0.1307. Si observas 70 caras y 30 cruces con el mismo prior, obtienes Beta(71,31), con desviación aproximadamente 0.0453. Hay más concentración sobre $\theta$.

**Ese número no es la variabilidad de una cara o cruz**, sino la incertidumbre sobre el parámetro. Tampoco constituye automáticamente un intervalo de credibilidad: un intervalo requiere calcular cuantiles o masa posterior.

## 7. Cómo conecta con Naive Bayes

El suavizado de probabilidades tiene una interpretación como protección frente a estimaciones extremas con pocos datos. En el caso binario, el prior uniforme lleva a sumar uno a cada resultado para la predicción posterior.

Esto explica el propósito del suavizado en [[07 S01 - Naive Bayes con un ejemplo de spam]]: dejar masa a eventos no observados. No agrega relaciones entre palabras ni elimina los supuestos de independencia.

**Fuente consultada directamente:** [[murphy-2022-pml-introduction.pdf#page=160|Murphy, §4.6.2, pp. impresas 130–134; PDF 160–164]]. El archivo tiene nombre «2022», pero sus páginas indican versión en línea del 18 de abril de 2025; las referencias corresponden a esa copia. Explicaciones, conteos y cálculos adaptados para estas notas.

## Preguntas para comprobar que entendiste

Responde primero y haz clic para comprobar.

> [!question]- Con prior Beta(2,3), cuatro caras y una cruz, ¿qué posterior obtienes?
> Beta(6,4): se suman cuatro al primer parámetro y una al segundo.

> [!question]- ¿Qué predicción de cara da Beta(6,4)?
> 6/(6+4)=0.6 para el próximo lanzamiento bajo el modelo Bernoulli.

> [!question]- ¿Más datos eliminan la aleatoriedad del lanzamiento?
> No. Reducen incertidumbre sobre theta bajo los supuestos del modelo, pero una moneda con theta entre 0 y 1 sigue produciendo resultados aleatorios.

> [!question]- ¿Por qué la media de Beta(8,4) no es 0.7?
> Su media es 8/12. El 0.7 es la moda de esa posterior y el MLE de los datos del ejemplo, que son resúmenes distintos.
