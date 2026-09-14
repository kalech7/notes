---
title: "07 S01 - Naive Bayes con un ejemplo de spam"
tags:
  - maestria/ia-generativa
  - estudio
---

# 07 S01 - Naive Bayes con un ejemplo de spam

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-01.pdf#page=12|Sesión 01, páginas 12]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción.

## La idea que simplifica el problema

Naive Bayes supone que las características son independientes **condicionadas a la clase**:

$$P(X,Y)=P(Y)\prod_{i=1}^{d}P(x_i\mid Y).$$

Aquí d es el número de características. El supuesto no afirma que todas las palabras sean independientes en general. Afirma que, una vez fijada la clase, el modelo calcula sus contribuciones por separado.

En lenguaje esto rara vez es exacto: «tarjeta» y «crédito» siguen relacionadas aunque ya sepamos que el correo es spam. La simplificación puede ser útil para clasificar, pero pierde estructura.

## Dos variantes que no debes mezclar

**Bernoulli:** cada característica indica presencia o ausencia de una palabra en un documento. Se estiman probabilidades de presencia dentro de los documentos de cada clase y también importa la ausencia.

**Multinomial:** representa conteos de palabras y estima probabilidades de tokens dentro de cada clase. En un correo importa cuántas veces aparece cada palabra. Esta es la variante del siguiente ejemplo.

Contar documentos que contienen una palabra y contar todas las apariciones de esa palabra no es la misma operación.

## Ejemplo de conteo y suavizado

Vocabulario: `oferta`, `premio`, `reunión`. Supón estos conteos de tokens:

| Palabra | Spam | Normal |
| --- | --- | --- |
| oferta | 6 | 1 |
| premio | 3 | 0 |
| reunión | 1 | 9 |
| Total | 10 | 10 |

Sin suavizado, premio tendría probabilidad cero en normales. Eso anularía el producto completo de esa clase cuando aparece la palabra.

Con suavizado de Laplace, $\alpha=1$, sumamos uno a cada conteo y el tamaño del vocabulario al total:

$$P(w\mid c)=\frac{N_{w,c}+\alpha}{N_c+\alpha V}.$$

En este ejemplo V=3 es el tamaño del vocabulario; es una notación local a esta nota.

| Palabra | $P(w\mid S)$ | $P(w\mid N)$ |
| --- | --- | --- |
| oferta | 7/13 | 2/13 |
| premio | 4/13 | 1/13 |
| reunión | 2/13 | 10/13 |

Cada columna suma 1. El suavizado evita tratar un evento no observado como imposible; no demuestra que todas las palabras sean igualmente plausibles.

## Clasificar «oferta premio»

Supón priors iguales: $P(S)=P(N)=0.5$. Para comparar clases calculamos puntajes proporcionales a la posterior:

$$s_S=0.5\frac7{13}\frac4{13}=\frac{14}{169},$$
$$s_N=0.5\frac2{13}\frac1{13}=\frac1{169}.$$

Normalizamos:

$$P(S\mid X)=\frac{s_S}{s_S+s_N}=\frac{14}{15}\approx0.9333.$$

El modelo asigna mayor probabilidad a spam. El coeficiente multinomial común a ambas clases se cancela en esta comparación. Esta probabilidad es la del modelo y depende de sus supuestos; no constituye una certeza del mundo real.

Para correos largos se suman logaritmos en lugar de multiplicar números muy pequeños:

$$\log P(c)+\sum_w n_w\log P(w\mid c).$$

## Usar el modelo para generar

Fija la clase spam y elige una longitud, por ejemplo cinco palabras. En cada posición muestrea usando las probabilidades 7/13, 4/13 y 2/13. Podría salir «oferta premio oferta reunión oferta».

Ese procedimiento refleja frecuencias de la clase, pero no utiliza la palabra anterior. No aprendió orden, concordancia ni significado composicional. Fijar la longitud también es una decisión de este ejemplo: estas probabilidades no modelan por sí mismas la longitud del correo.

## Qué aporta al recorrido del curso

Naive Bayes demuestra que la generación comienza en una distribución y un mecanismo de muestreo; no exige una red enorme. Sus límites permiten comprender por qué luego necesitamos dependencias, estados ocultos y representaciones más flexibles.

## Complemento del libro: por qué tiene sentido sumar uno

El suavizado no tiene que entenderse como un truco arbitrario para evitar ceros. Murphy muestra que, para una variable binaria y un prior uniforme sobre su probabilidad, la predicción bayesiana da:

$$P(\text{éxito siguiente}\mid D)=\frac{\text{éxitos}+1}{\text{ensayos}+2}.$$

El denominador añade dos porque hay dos resultados posibles. Con tres éxitos y ningún fracaso se predice éxito con 4/5, dejando probabilidad para un fracaso aún no observado.

En la tabla multinomial de palabras, sumar uno a cada una de V categorías exige sumar V al denominador. Si aumentas el vocabulario y mantienes los conteos, cada palabra recibe una porción menor: estás repartiendo masa entre más posibilidades. No puedes sumar uno arriba y olvidar ajustar abajo.

**Lo que sí cambia:** cuánto peso das a eventos no vistos. **Lo que permanece como supuesto del modelo:** la independencia condicional y la pérdida del orden. Suavizar una bolsa de palabras no la convierte en un modelo de sintaxis.

**Fuente del razonamiento binario:** [[murphy-2022-pml-introduction.pdf#page=164|Murphy, §4.6.2.9, p. impresa 134; PDF 164]]. La conexión con tu tabla multinomial es una explicación algebraica propia. Más detalle en [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]].

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Qué significa la independencia condicional?
> Que, una vez conocida la clase, el modelo factoriza las probabilidades de las características. No afirma independencia universal entre palabras.

> [!question]- Con 0 apariciones, 10 tokens y vocabulario de 3, ¿cuál es la probabilidad con Laplace?
> (0+1)/(10+3)=1/13. Sin suavizado sería cero.

> [!question]- ¿Qué posterior obtiene spam para «oferta premio» en el ejemplo?
> 14/15, aproximadamente 93.33 %. Se divide su puntaje 14/169 por la suma 15/169.

> [!question]- ¿Por qué el texto generado no suele ser gramatical?
> Porque el modelo del ejemplo sortea palabras independientemente dada la clase. No representa el orden ni dependencias sintácticas.

> [!question]- ¿La clase Y es una variable latente durante el entrenamiento supervisado de este ejemplo?
> No. Las etiquetas se observan al entrenar. Que la clase sea desconocida en un correo nuevo no convierte las etiquetas del conjunto de entrenamiento en latentes.


> [!question]- ¿Qué pasa si sumas uno a cada conteo pero no cambias el denominador?
> Las probabilidades dejan de sumar 1. Hay que añadir al denominador la suma de todos los incrementos.

> [!question]- ¿El suavizado arregla la falta de orden en Naive Bayes?
> No. Evita probabilidades cero o extremas; no añade dependencias secuenciales.
