---
title: "03 S00 - Perceptrón redes neuronales y XOR"
tags:
  - maestria/ia-generativa
  - estudio
---

# 03 S00 - Perceptrón redes neuronales y XOR

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. Una decisión hecha con números

Un perceptrón recibe números, los combina y devuelve una decisión. Vamos a usar entradas que solo pueden valer 0 o 1. Queremos que la salida sea 1 únicamente cuando **las dos entradas valgan 1**. Esta regla se llama AND.

No imagines todavía una red enorme. Solo necesitamos dos entradas, una suma y un umbral.

![Cómo calcula un perceptrón](<../Recursos visuales/01-perceptron.png>)

Lee de izquierda a derecha: las entradas llegan a la suma; el resultado pasa por una condición; la condición produce 0 o 1.

## 2. Qué hace cada parte de la fórmula

$$a=w_1x_1+w_2x_2+b.$$

Las entradas son $x_1$ y $x_2$. Cada una se multiplica por un **peso**, $w_1$ o $w_2$, que regula su influencia. Después se añade $b$, llamado **sesgo**. El resultado $a$ es un puntaje.

La regla de salida es: si $a\geq0$, devuelve 1; si es negativo, devuelve 0. El puntaje no es una probabilidad, y la salida tampoco dice cuánta confianza tiene el modelo.

## 3. Hagamos el cálculo de AND

Elige pesos 1 y 1, y sesgo −1.5. Ahora la fórmula es $a=x_1+x_2-1.5$.

| Entradas | Cálculo | Puntaje | Salida |
| --- | --- | --- | --- |
| 0 y 0 | 0 + 0 − 1.5 | −1.5 | 0 |
| 0 y 1 | 0 + 1 − 1.5 | −0.5 | 0 |
| 1 y 0 | 1 + 0 − 1.5 | −0.5 | 0 |
| 1 y 1 | 1 + 1 − 1.5 | 0.5 | 1 |

El sesgo hace que una sola entrada activa no alcance el umbral. En este ejemplo elegimos los valores a mano para ver cómo funciona. Al entrenar, un algoritmo busca valores apropiados a partir de ejemplos.

## 4. Por qué XOR es más difícil

XOR devuelve 1 cuando las entradas son **diferentes**. Devuelve 0 para (0,0) y (1,1), y 1 para (0,1) y (1,0).

![Comparación de AND y XOR](<../Recursos visuales/02-and-xor.png>)

En AND, una recta puede separar los puntos de salida 0 de los de salida 1. En XOR, las clases están en diagonales opuestas. Ninguna recta deja los dos ceros de un lado y los dos unos del otro.

Un perceptrón con estas entradas solo puede crear una frontera recta. Por eso entrenarlo durante más tiempo no resuelve XOR: el problema está en lo que puede representar.

## 5. Cómo ayudan las capas intermedias

Podemos calcular primero dos resultados: $h_1$ indica si al menos una entrada vale 1 (OR), y $h_2$ indica si ambas valen 1 (AND). Después calculamos $h_1-2h_2-0.5$ y aplicamos el umbral.

Para entradas distintas, $h_1=1$ y $h_2=0$: el puntaje da 0.5 y la salida 1. Para ambas iguales a 1, da −1.5 y la salida 0. Para ambas iguales a 0, da −0.5 y la salida 0. Así resolvimos XOR creando una representación intermedia.

Las redes profundas aprenden representaciones de este tipo, generalmente mucho más complejas. Apilar únicamente transformaciones lineales no basta: su composición sigue siendo lineal. Se necesitan funciones no lineales para ganar esa capacidad.

## 6. Qué significa ajustar los pesos

Una regla clásica del perceptrón modifica los pesos cuando se equivoca:

$$w_i\leftarrow w_i+\eta(y_{\mathrm{real}}-y_{\mathrm{pred}})x_i.$$

$\eta$ controla el tamaño del cambio. Si acierta, la diferencia entre resultado real y predicho es cero. El sesgo se actualiza de forma parecida, sin multiplicar por $x_i$.

Corregir un ejemplo puede empeorar otro. La convergencia del algoritmo clásico requiere que los datos sean separables por una frontera lineal en la representación utilizada. Incluso entonces, separar el entrenamiento no garantiza acertar en casos nuevos.

En redes profundas se distingue **retropropagación**, que calcula cómo influye cada parámetro en la pérdida mediante derivadas, y **optimizador**, que utiliza esa información para actualizarlo. El escalón del perceptrón no es la activación habitual para entrenar esas redes con gradientes.

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-00.pdf#page=13|Sesión 00, páginas 13]]
- [[bishop-2006-prml.pdf#page=213|Bishop, §4.1.7, pp. impresas 193–194; PDF 213–214]]

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- Con pesos 2 y 1, sesgo -2.5 y entrada (1,0), ¿qué devuelve el perceptrón?
> El puntaje es 2×1+1×0−2.5=−0.5. Como es negativo, devuelve 0.

> [!question]- ¿Por qué el sesgo es útil?
> Desplaza la frontera de decisión. Permite que el umbral no dependa exclusivamente de una suma que pasa por el origen.

> [!question]- ¿Entrenar más tiempo permite que un perceptrón lineal aprenda XOR?
> No. XOR no es linealmente separable en sus entradas originales. Hace falta cambiar la representación o la arquitectura.

> [!question]- ¿Retropropagación y optimizador son lo mismo?
> No. La retropropagación calcula gradientes; el optimizador utiliza esos gradientes para modificar parámetros.

> [!question]- ¿Por qué no basta con apilar capas lineales?
> Su composición sigue siendo una transformación lineal. Las activaciones no lineales permiten representar fronteras más complejas.


> [!question]- ¿Cada actualización del perceptrón reduce necesariamente todos los errores?
> No. Puede corregir un ejemplo y empeorar otros. La convergencia se garantiza bajo separabilidad, no porque cada paso mejore el total.

> [!question]- ¿Qué condición necesita su garantía de convergencia?
> Que el conjunto de entrenamiento sea linealmente separable en la representación utilizada.
