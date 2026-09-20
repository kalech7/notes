---
title: "09 S01 - Markov HMM y generación con bigramas"
tags:
  - maestria/ia-generativa
  - estudio
---

# 09 S01 - Markov HMM y generación con bigramas

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

Práctica del notebook: [[17 PRÁCTICA - Modelos generativos Naive Bayes GMM y bigramas#3. Bigramas: mi primer modelo autorregresivo|Construir la tabla de conteos y generar texto paso a paso]].

## 1. Generar una frase eligiendo una palabra cada vez

Imagina que quieres completar «yo…». Un modelo sencillo podría mirar qué palabras siguieron a «yo» en sus ejemplos y sortear una de ellas.

Después utiliza la última palabra elegida para decidir la siguiente. Así genera paso a paso. Vamos a construir ese modelo antes de estudiar estados ocultos.

## 2. Un bigrama se aprende contando pares

Nuestro pequeño conjunto de frases es:

```text
<inicio> yo estudio ia <fin>
<inicio> yo estudio bayes <fin>
<inicio> yo aprendo ia <fin>
```

Después de «yo» aparece «estudio» dos veces y «aprendo» una. Por tanto:

$$P(\text{estudio}\mid\text{yo})=2/3,\qquad P(\text{aprendo}\mid\text{yo})=1/3.$$

Después de «estudio», «ia» y «bayes» aparecen una vez cada una. Cada opción recibe probabilidad 1/2.

Se llama **bigrama** porque cuenta pares de elementos: anterior y siguiente. El contexto utilizado para la predicción es de una palabra, no dos.

## 3. Cómo generar con esa tabla

Empieza en `<inicio>`, que en estos ejemplos lleva a «yo». Desde «yo», sortea «estudio» o «aprendo» con sus probabilidades. Si sale «estudio», sortea «ia» o «bayes». Continúa hasta `<fin>`.

La probabilidad de la ruta «yo estudio bayes» es $1\times2/3\times1/2\times1=1/3$. Multiplicamos porque la secuencia requiere que se produzcan todas esas elecciones.

Si aparece un contexto sin continuaciones, el programa necesita una regla: detenerse, usar otra distribución como respaldo o aplicar suavizado. Los marcadores de inicio y fin evitan unir accidentalmente dos oraciones distintas.

## 4. Qué significa la hipótesis de Markov

La probabilidad de una secuencia puede escribirse exactamente como:

$$P(x_1,\ldots,x_n)=\prod_{t=1}^{n}P(x_t\mid x_{<t}).$$

Se lee: multiplica la probabilidad de cada elemento teniendo en cuenta todo lo que apareció antes. $x_{<t}$ es el prefijo y $\prod$ indica un producto.

El bigrama hace una simplificación: usa solo el elemento anterior. Esto se llama **Markov de primer orden**. La regla del producto es exacta; restringir el pasado es una decisión del modelo.

## 5. Por qué no basta con crear una tabla cada vez más grande

Si hay K símbolos y guardas M símbolos de contexto, existen $K^M$ contextos posibles. Para cada contexto necesitas una distribución sobre K continuaciones. Como las probabilidades suman 1, hay K−1 valores libres por fila.

La tabla completa necesita $K^M(K-1)$ parámetros libres, sin contar la distribución inicial. Con K=10 y M=2 son $100\times9=900$. Al aumentar M, crece muy rápido y faltan ejemplos para muchos contextos.

Una red neuronal puede compartir parámetros entre contextos en lugar de aprender cada fila de forma aislada. Esa idea ayudará a entender los LLM.

## 6. Un HMM cambia qué cosa sigue la cadena

Ahora imagina una máquina cuyo estado no puedes ver: puede estar «estable» o «exigida». Lo que sí observas es el ruido que emite.

El **modelo oculto de Markov (HMM)** distingue el estado oculto z y el dato observado x. El estado de un momento influye en el siguiente, y cada estado determina una distribución de observaciones posibles.

![Estados y observaciones de un HMM](<../Recursos visuales/06-hmm.png>)

Sigue las flechas horizontales para ver cambios de estado. Sigue las verticales para ver cómo un estado se relaciona con una observación. El modelo puede verse como una mezcla cuyo componente cambia siguiendo una cadena.

## 7. Cómo usa el historial, con números

Después de escuchar los ruidos anteriores, crees que la máquina está estable con probabilidad 0.8 y exigida con 0.2.

Supón que, si está estable, sigue estable con probabilidad 0.9. Si está exigida, pasa a estable con probabilidad 0.3. Para predecir el siguiente estado estable, suma ambos caminos:

$$0.8\times0.9+0.2\times0.3=0.72+0.06=0.78.$$

Cuando llega un ruido nuevo, multiplicas la predicción de cada estado por la probabilidad de ese ruido bajo ese estado y normalizas. Es otra actualización de Bayes.

Así, el modelo conserva información del pasado en **la distribución de creencias sobre el estado actual**. Decir que el estado oculto depende del anterior no significa que solo se use la última observación.

## 8. La fórmula completa, después de entender el recorrido

$$P(z_1,x_1,\ldots,z_n,x_n)=P(z_1)P(x_1\mid z_1)\prod_{t=2}^{n}P(z_t\mid z_{t-1})P(x_t\mid z_t).$$

Hay tres piezas: estado inicial, transiciones entre estados y emisiones de observaciones. Para calcular la probabilidad de los datos sin conocer los estados se suman los caminos ocultos posibles. Los algoritmos de cadenas reutilizan cálculos para evitar enumerar cada camino por separado.

La lección principal es distinguir **el estado que suponemos** de **la observación que recibimos**.

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-01.pdf#page=14|Sesión 01, páginas 14–16]]
- [[bishop-2006-prml.pdf#page=630|Bishop, §13.2, p. impresa 610; PDF 630]]
- [[bishop-2006-prml.pdf#page=635|§13.2.1, pp. 615–616; PDF 635–636]]

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿La regla del producto exige una hipótesis de Markov?
> No. Es una identidad general. Markov aparece al restringir de qué parte del pasado depende cada factor.

> [!question]- En el corpus, ¿cuánto vale P(aprendo dado yo)?
> 1/3, porque hay tres continuaciones de «yo» y una es «aprendo».

> [!question]- Con K=10 y M=2, ¿cuántos parámetros libres tiene la tabla de transiciones?
> 10²×(10−1)=900. No se cuentan aquí distribuciones iniciales adicionales.

> [!question]- ¿Un HMM de primer orden solo usa la última observación?
> No. La condición de primer orden se aplica a los estados ocultos. La creencia sobre el estado actual puede incorporar todas las observaciones previas.

> [!question]- ¿Qué ocurre si no hay continuaciones para una palabra?
> Hace falta una decisión explícita: terminar, usar respaldo o suavizado. El algoritmo no debe asumir que siempre existe una fila válida.


> [!question]- ¿De dónde sale 0.78 en la predicción del HMM?
> De sumar los dos caminos al estado estable: 0.8×0.9 desde estable y 0.2×0.3 desde exigido.

> [!question]- ¿Qué haces cuando llega una nueva observación?
> Multiplicas la predicción de cada estado por la verosimilitud de la observación en ese estado y normalizas.
