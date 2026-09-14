---
title: "15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números"
tags:
  - maestria/ia-generativa
  - estudio
---

# 15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. Saber una probabilidad y estar seguro de ella son cosas distintas

Observas siete caras en diez lanzamientos. Una estimación sencilla dice que la probabilidad de cara es 0.7. Pero diez lanzamientos son pocos: otro grupo de diez podría dar una proporción diferente.

Ahora imagina setenta caras en cien lanzamientos. La proporción también es 0.7, pero tienes más información. Queremos una forma de expresar esa diferencia de incertidumbre.

Esta nota continúa [[05 S01 - Probabilidad y teorema de Bayes paso a paso|Bayes]]. No necesitas dominar la distribución Beta antes de leerla: la construiremos a partir del ejemplo.

## 2. Qué número desconocemos

Llamamos $\theta$ a la probabilidad real de cara bajo nuestro modelo de moneda. Puede estar entre 0 y 1.

Hay dos incertidumbres: no sabemos exactamente cuánto vale $\theta$ y, aunque lo supiéramos, un lanzamiento seguiría siendo aleatorio si ese valor está entre 0 y 1. Recoger datos ayuda con la primera; no elimina la segunda.

Para representar lo que creemos sobre $\theta$, usamos una distribución sobre sus valores posibles. Una opción es **Beta**.

## 3. Qué significa Beta sin calcular todavía su fórmula

Beta tiene dos números, $\alpha$ y $\beta$, que controlan su forma. Beta(1,1) es uniforme: da la misma densidad a los valores de $\theta$ entre 0 y 1. Beta(2,2) concentra más densidad alrededor del centro.

Estas curvas no describen directamente «cara o cruz». Describen cuánto peso asignamos a posibles valores de la **probabilidad de cara**.

Para el cálculo siguiente solo necesitas esta regla: si partes de Beta($\alpha,\beta$), sumas las caras a $\alpha$ y las cruces a $\beta$.

## 4. Actualiza la distribución paso a paso

Partimos de Beta(1,1) y vemos siete caras y tres cruces:

$$\text{posterior}=\operatorname{Beta}(1+7,1+3)=\operatorname{Beta}(8,4).$$

La distribución inicial es el **prior** y la actualizada es la **posterior**. Usamos lanzamientos independientes que comparten la misma probabilidad de cara.

¿Por qué se pueden sumar los conteos? La verosimilitud contiene $\theta^7(1-\theta)^3$. Al multiplicarla por un prior Beta, se suman los exponentes y obtenemos otra Beta. Cuando la familia de distribuciones se conserva así, se llama **conjugación**.

## 5. Tres formas de resumir los datos

| Nombre | Pregunta que responde | Resultado aquí |
| --- | --- | --- |
| MLE | ¿Qué valor hace más probables los datos observados? | 7/10 = 0.7 |
| MAP | ¿Dónde está el punto más alto de la posterior? | (8−1)/(8+4−2) = 0.7 |
| Media posterior | ¿Cuál es el promedio según la posterior? | 8/12 ≈ 0.667 |

El pico y el promedio no tienen por qué coincidir. MLE y MAP coinciden aquí porque el prior es uniforme. Con prior Beta(2,2), los mismos datos dan Beta(9,5): MAP es 8/12 y la media 9/14.

La fórmula de la moda Beta utilizada aquí requiere ambos parámetros mayores que 1. Si están en la frontera, no debe aplicarse de forma automática.

## 6. Qué predices para el siguiente lanzamiento

Para un lanzamiento nuevo, la predicción bayesiana promedia los posibles valores de $\theta$ según la posterior. En este modelo equivale a la media:

$$P(\text{cara siguiente}\mid D)=\frac{\alpha+\text{caras}}{\alpha+\beta+\text{caras}+\text{cruces}}.$$

Con Beta(1,1), siete caras y tres cruces, da 8/12.

Observa un caso más extremo: tres caras y ninguna cruz. MLE da 3/3=1, por lo que el ajuste puntual no deja probabilidad para una cruz. La predicción bayesiana con Beta(1,1) da cara 4/5 y cruz 1/5. No haber observado una cruz no basta para declararla imposible.

Esta es la conexión con el suavizado de [[07 S01 - Naive Bayes con un ejemplo de spam|Naive Bayes]].

## 7. Mira cómo cambia la curva con más datos

![Incertidumbre sobre la probabilidad de cara](<Recursos visuales/09-bayes-incertidumbre.png>)

La línea gris es el prior uniforme. La azul incorpora 7 caras y 3 cruces. La naranja incorpora 70 y 30. La proporción observada es la misma, pero la curva naranja queda más concentrada.

El eje horizontal contiene valores posibles de $\theta$. El vertical es densidad: puede superar 1. La probabilidad de un intervalo corresponde al área bajo la curva en ese intervalo, y el área total de cada curva es 1.

## 8. Si necesitas expresar la concentración con una fórmula

Para una posterior Beta(a,b), su varianza es:

$$\operatorname{Var}(\theta\mid D)=\frac{ab}{(a+b)^2(a+b+1)}.$$

Su desviación estándar es la raíz cuadrada de esa cantidad. Para Beta(8,4) es aproximadamente 0.1307; para Beta(71,31), aproximadamente 0.0453. El número menor indica una distribución más concentrada sobre el parámetro.

No es la variabilidad de «cara o cruz» ni un intervalo de credibilidad por sí solo. Es una medida de la incertidumbre sobre $\theta$.

La expresión completa de la densidad Beta es proporcional a $\theta^{\alpha-1}(1-\theta)^{\beta-1}$. Una constante normaliza el área. No necesitas calcularla para aplicar las actualizaciones de esta nota.

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[murphy-2022-pml-introduction.pdf#page=160|Murphy, §4.6.2, pp. impresas 130–134; PDF 160–164]]

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
