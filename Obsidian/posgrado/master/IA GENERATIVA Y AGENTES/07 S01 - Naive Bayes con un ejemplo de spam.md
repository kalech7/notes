---
title: "07 S01 - Naive Bayes con un ejemplo de spam"
tags:
  - maestria/ia-generativa
  - estudio
---

# 07 S01 - Naive Bayes con un ejemplo de spam

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. La idea: aprender qué palabras aparecen en cada clase

Vamos a crear un clasificador pequeño. En lugar de interpretar el correo como una persona, contará palabras y aprenderá cuáles aparecen más en spam y en mensajes normales.

Usaremos solo tres palabras para poder hacer todas las cuentas: **oferta, premio y reunión**. Los conteos son inventados para aprender el procedimiento.

| Palabra | Apariciones en spam | Apariciones en normales |
| --- | --- | --- |
| oferta | 6 | 1 |
| premio | 3 | 0 |
| reunión | 1 | 9 |
| Total | 10 | 10 |

## 2. El supuesto que simplifica el cálculo

Naive Bayes calcula la contribución de cada característica por separado una vez fijada la clase. Este supuesto se llama **independencia condicional**.

Para entenderlo, imagina que ya decidiste evaluar la clase spam. El modelo multiplica la contribución de «oferta» por la de «premio» sin representar que ambas palabras podrían estar relacionadas dentro de la misma frase.

La simplificación suele ser falsa en sentido literal, pero puede ser útil. Permite estimar menos relaciones a partir de los datos.

$$P(X,Y)=P(Y)\prod_i P(x_i\mid Y).$$

La fórmula dice: probabilidad de la clase multiplicada por las probabilidades de sus características. El símbolo $\prod$ significa multiplicar los términos.

## 3. Por qué necesitamos suavizado

En los correos normales no apareció «premio». Si le asignamos probabilidad cero, cualquier mensaje con esa palabra obtiene producto cero para esa clase. Estaríamos tratando algo no observado como imposible.

El **suavizado de Laplace** añade uno a cada conteo. Como tenemos tres palabras, añadimos tres al total:

| Palabra | Probabilidad en spam | Probabilidad en normales |
| --- | --- | --- |
| oferta | (6+1)/(10+3) = 7/13 | 2/13 |
| premio | 4/13 | 1/13 |
| reunión | 2/13 | 10/13 |

Cada columna suma 1. Si sumaras uno arriba pero dejaras 10 abajo, ya no tendrías probabilidades que sumen 1.

Para cualquier vocabulario de tamaño V, la regla es $(\text{conteo}+1)/(\text{total}+V)$. El tamaño del vocabulario importa porque repartes masa entre todas las opciones.

## 4. Clasifiquemos «oferta premio» paso a paso

Supongamos que antes de leer el mensaje spam y normal tienen la misma probabilidad: 0.5 cada uno.

**Puntaje de spam:** $0.5\times7/13\times4/13=14/169$.

**Puntaje de normal:** $0.5\times2/13\times1/13=1/169$.

Estos dos puntajes todavía no suman 1. Sumamos ambos: $15/169$. Luego dividimos el puntaje de spam entre ese total:

$$P(\text{spam}\mid\text{mensaje})=\frac{14/169}{15/169}=\frac{14}{15}\approx93.33\%.$$

Este resultado pertenece al modelo y sus supuestos; no es una garantía absoluta. En el modelo de conteos, un factor combinatorio común a ambas clases se cancela al comparar estos puntajes.

## 5. Cómo generar un mensaje con el mismo modelo

Fija la clase spam y una longitud, por ejemplo cinco palabras. Sortea cada palabra usando las probabilidades 7/13, 4/13 y 2/13. Podría salir «oferta premio oferta reunión oferta».

Se parece al spam en frecuencias, pero no necesariamente en gramática. El modelo no utiliza el orden de las palabras. Suavizar tampoco añade esa capacidad: solo modifica las probabilidades estimadas.

La clase se conoce en los ejemplos de entrenamiento; no es una variable latente allí. Al generar podemos elegirla o sortearla.

## 6. Dos variantes que debes distinguir

El ejemplo anterior usa **Naive Bayes multinomial**: cuenta apariciones de palabras. Si «oferta» aparece tres veces, sus tres apariciones cuentan.

**Naive Bayes Bernoulli** utiliza presencia o ausencia: pregunta si la palabra apareció en el documento. En ese caso también debe considerarse su ausencia. No mezcles conteos de palabras con conteos de documentos al calcular las probabilidades.

Para textos largos, los programas suelen sumar logaritmos en lugar de multiplicar muchos números pequeños. Es otra forma de calcular el mismo criterio y evita problemas numéricos.

## 7. Una conexión con Bayes

Murphy muestra que, en un problema binario con prior uniforme, la predicción bayesiana suma uno a cada resultado. Esto ayuda a entender por qué el suavizado deja una posibilidad para lo que todavía no vimos.

En [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]] se desarrolla esa idea con una moneda. Aquí lo esencial es distinguir **falta de ejemplos** de **imposibilidad**.

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-01.pdf#page=12|Sesión 01, páginas 12]]
- [[murphy-2022-pml-introduction.pdf#page=164|Murphy, §4.6.2.9, p. impresa 134; PDF 164]]

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
