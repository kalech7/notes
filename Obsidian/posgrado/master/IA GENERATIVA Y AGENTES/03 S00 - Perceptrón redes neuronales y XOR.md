---
title: "03 S00 - Perceptrón redes neuronales y XOR"
tags:
  - maestria/ia-generativa
  - estudio
---

# 03 S00 - Perceptrón redes neuronales y XOR

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-00.pdf#page=13|Sesión 00, páginas 13]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción.

## Una neurona artificial como decisión numérica

El perceptrón combina entradas, calcula un puntaje y aplica un umbral:

$$a=w_1x_1+w_2x_2+b,\qquad y=f(a).$$

En el perceptrón de la sesión, $f(a)=1$ si $a\geq0$ y $f(a)=0$ en otro caso.

- $x_1,x_2$: entradas observadas.
- $w_1,w_2$: pesos; regulan cuánto influye cada entrada.
- $b$: sesgo; desplaza el umbral.
- $a$: puntaje antes de decidir.
- $y$: salida del modelo.

La salida 0 o 1 es una decisión, no una probabilidad calibrada.

## Ejemplo resuelto: la función AND

Queremos salida 1 solo cuando ambas entradas valgan 1. Elige $w_1=w_2=1$ y $b=-1.5$.

| $x_1$ | $x_2$ | $a=x_1+x_2-1.5$ | Salida |
| --- | --- | --- | --- |
| 0 | 0 | -1.5 | 0 |
| 0 | 1 | -0.5 | 0 |
| 1 | 0 | -0.5 | 0 |
| 1 | 1 | 0.5 | 1 |

El sesgo exige que la suma alcance 1.5. Como las entradas son binarias, solo el último caso lo consigue. Hemos elegido los pesos para explicar el mecanismo; un algoritmo de aprendizaje podría buscarlos a partir de ejemplos.

## Qué significa aprender los pesos

Una regla clásica de actualización del perceptrón es:

$$w_i\leftarrow w_i+\eta(y_{\mathrm{real}}-y_{\mathrm{pred}})x_i,$$
$$b\leftarrow b+\eta(y_{\mathrm{real}}-y_{\mathrm{pred}}).$$

$\eta>0$ es la tasa de aprendizaje. Si la predicción es correcta, la diferencia es cero y no hay cambio. Si predice 0 donde debía predecir 1, la actualización aumenta el puntaje para esa entrada. Esta regla es una ampliación didáctica, distinta de la retropropagación usada en redes profundas.

## Por qué XOR no cabe en un solo perceptrón

XOR devuelve 1 cuando las entradas son diferentes y 0 cuando son iguales.

| Entrada | XOR |
| --- | --- |
| (0, 0) | 0 |
| (0, 1) | 1 |
| (1, 0) | 1 |
| (1, 1) | 0 |

Dibuja esos cuatro puntos en un cuadrado: las dos clases ocupan diagonales opuestas. Una única recta no puede dejar todos los ceros de un lado y todos los unos del otro.

La frontera del perceptrón es $w_1x_1+w_2x_2+b=0$, una recta en dos dimensiones. El límite es de representación: repetir el entrenamiento no arregla que la familia del modelo no pueda expresar XOR.

## Cómo ayudan varias capas

Podemos calcular primero dos características:

- $h_1=\operatorname{OR}(x_1,x_2)$: al menos una entrada vale 1.
- $h_2=\operatorname{AND}(x_1,x_2)$: ambas valen 1.

Después una salida con puntaje $h_1-2h_2-0.5$ y el mismo umbral resuelve XOR. Para (0,0) da -0.5; para entradas diferentes da 0.5; para (1,1) da -1.5.

Esto demuestra por construcción por qué una representación intermedia puede hacer resoluble un problema. En redes prácticas esas representaciones normalmente se aprenden.

## Retropropagación y optimización

La **retropropagación** calcula derivadas de la pérdida respecto de los parámetros aplicando la regla de la cadena. Un **optimizador** utiliza esas derivadas para actualizar pesos. Son operaciones relacionadas, pero distintas.

Las redes profundas suelen usar activaciones adecuadas para ese cálculo, como ReLU, y no el escalón duro del perceptrón como mecanismo ordinario de entrenamiento. Además, apilar capas solo lineales equivale a otra transformación lineal; las no linealidades son esenciales para ganar capacidad expresiva.

Un modelo más expresivo no aprende automáticamente mejor: aún necesita datos, un objetivo apropiado y evaluación. Tampoco obtiene causalidad solo por tener más capas: [[04 S00 - Correlación causalidad y límites de las predicciones]].

## Complemento del libro: qué garantiza el aprendizaje del perceptrón

Bishop distingue tres cosas que a menudo se mezclan: que exista una frontera correcta, que el algoritmo la encuentre y que esa frontera generalice.

Para un conjunto finito linealmente separable, el algoritmo clásico del perceptrón converge a una solución separadora en un número finito de actualizaciones. Esa garantía **depende de la separabilidad**. XOR en las entradas originales no cumple la condición.

Además, corregir un ejemplo puede hacer que otro antes correcto quede mal clasificado. Por eso una actualización no tiene por qué reducir el número total de errores inmediatamente. Incluso si hay varias soluciones válidas, el orden de los ejemplos y la inicialización pueden influir en cuál encuentra el algoritmo.

Una última distinción: separar todo el conjunto de entrenamiento no prueba que se clasifiquen bien nuevas observaciones. La garantía del algoritmo se refiere al problema de entrenamiento bajo sus condiciones, no a una inteligencia general.

**Notación del libro:** Bishop codifica clases como −1 y +1 en este apartado. Estas notas usaron 0 y 1. Ambas convenciones sirven, pero no debes copiar una fórmula de actualización sin comprobar con cuál se definió.

**Fuente:** [[bishop-2006-prml.pdf#page=213|Bishop, §4.1.7, pp. impresas 193–194; PDF 213–214]].

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
