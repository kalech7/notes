---
title: "09 S01 - Markov HMM y generación con bigramas"
tags:
  - maestria/ia-generativa
  - estudio
---

# 09 S01 - Markov HMM y generación con bigramas

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-01.pdf#page=14|Sesión 01, páginas 14–16]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción.

## La regla del producto es exacta

Para una secuencia de longitud n:

$$P(x_1,\ldots,x_n)=\prod_{t=1}^{n}P(x_t\mid x_{<t}).$$

$x_{<t}$ significa todos los elementos anteriores a la posición t. Para el primero no hay prefijo y el factor es $P(x_1)$.

Esta identidad no supone que el pasado sea corto. La aproximación aparece cuando decidimos cómo representar cada probabilidad condicional.

## Markov de primer orden: usar solo el último elemento

Un modelo de primer orden utiliza:

$$P(x_t\mid x_{<t})\approx P(x_t\mid x_{t-1}).$$

En un modelo de bigramas se cuenta qué palabra sigue a otra. «Bi» se refiere al par anterior-siguiente, no a que el contexto tenga dos palabras.

### Ejemplo contado a mano

Corpus didáctico:

```text
<inicio> yo estudio ia <fin>
<inicio> yo estudio bayes <fin>
<inicio> yo aprendo ia <fin>
```

Después de `yo`, `estudio` aparece dos veces y `aprendo` una:

$$P(\text{estudio}\mid\text{yo})=2/3,\quad
P(\text{aprendo}\mid\text{yo})=1/3.$$

Después de `estudio`, `ia` y `bayes` aparecen una vez cada una: probabilidad 1/2 para cada opción. La probabilidad de la ruta completa `yo estudio bayes`, incluyendo inicio y fin, es $1\times(2/3)\times(1/2)\times1=1/3$.

## Generar paso a paso

Empieza en `<inicio>`. Sortea la siguiente palabra de su fila, añádela a la salida y utiliza esa palabra como nuevo estado. Continúa hasta `<fin>` o un límite de pasos.

La generación necesita una política para contextos sin continuaciones: detenerse, volver a una distribución de respaldo o aplicar suavizado. Un conteo cero no siempre significa que una secuencia sea lingüísticamente imposible; puede indicar falta de ejemplos.

Los marcadores de inicio y fin evitan conectar por accidente la última palabra de una oración con la primera de otra. Son una decisión explícita de este ejemplo.

## Por qué aumentar la memoria sale caro

Con K símbolos y contexto de longitud M hay $K^M$ contextos posibles. Cada fila necesita K probabilidades, pero solo K−1 son libres porque deben sumar 1:

$$\text{parámetros libres}=K^M(K-1).$$

Para K=100: con M=1 son 9 900; con M=2 son 990 000; con M=3 son 99 000 000. Esta cuenta corresponde a una tabla completa de transiciones y no incluye distribuciones iniciales adicionales.

Además del costo de almacenar, muchos contextos tendrán pocos ejemplos o ninguno. El suavizado distribuye probabilidad, pero no equivale a aprender relaciones semánticas entre palabras.

## HMM: el estado que evoluciona está oculto

En un **modelo oculto de Markov (HMM)** tenemos observaciones $x_t$ y estados ocultos $z_t$. Por ejemplo, observamos palabras y postulamos estados que representan alguna estructura no etiquetada.

$$P(z_1,x_1,\ldots,z_n,x_n)=P(z_1)P(x_1\mid z_1)
\prod_{t=2}^{n}P(z_t\mid z_{t-1})P(x_t\mid z_t).$$

La transición conecta estados ocultos; la emisión relaciona un estado con la observación. No son la misma distribución.

### La trampa de «solo recuerda un paso»

La cadena oculta es de primer orden, pero la creencia sobre el estado actual se actualiza usando las observaciones acumuladas. La predicción puede escribirse:

$$P(x_{t+1}\mid x_{1:t})=\sum_{j,k}P(x_{t+1}\mid z_{t+1}=k)
P(z_{t+1}=k\mid z_t=j)P(z_t=j\mid x_{1:t}).$$

La última distribución incorpora la historia observada. Por eso el HMM no es simplemente un bigrama sobre observaciones. Resume el pasado en una distribución de creencias sobre sus estados, aunque esa representación tenga capacidad limitada.

## Camino hacia los modelos neuronales

En lugar de una fila independiente para cada contexto, una red puede compartir parámetros entre contextos. Esa reutilización ayuda a generalizar a combinaciones que no aparecieron exactamente en los datos. Un modelo autorregresivo de lenguaje mantiene la regla del producto, pero cambia la forma de aprender cada factor.

## Complemento del libro: el HMM como una mezcla que evoluciona

Bishop conecta el HMM con las mezclas: en un instante, cada estado oculto propone una distribución de observaciones. La novedad es que el estado siguiente depende del actual, en lugar de elegir independientemente un componente para cada dato.

Ejemplo didáctico: una máquina tiene estado oculto «estable» o «exigido» y observamos su ruido. Después de escucharla, nuestra creencia actual es 0.8 estable y 0.2 exigido. Supón que la probabilidad de seguir estable desde estable es 0.9 y de pasar a estable desde exigido es 0.3.

La predicción del estado siguiente combina los caminos:

$$P(z_{t+1}=\text{estable}\mid x_{1:t})=0.8(0.9)+0.2(0.3)=0.78.$$

Queda 0.22 para exigido. Cuando llega el siguiente sonido, multiplicas esos priors predictivos por las probabilidades de ese sonido en cada estado y normalizas con Bayes. Así alternas **predecir el estado** y **actualizarlo con la observación**.

Esto explica con un cálculo qué significa «resumir la historia»: no guardamos únicamente el último sonido, sino una creencia que ya incorporó observaciones anteriores.

Para evaluar una secuencia completa, enumerar todos los caminos ocultos requeriría $K^n$ posibilidades. El libro explica que se pueden reorganizar las sumas para reutilizar cálculos. Esa es la intuición de la inferencia eficiente en cadenas: evitar volver a calcular los mismos prefijos.

**Fuente:** [[bishop-2006-prml.pdf#page=630|Bishop, §13.2, p. impresa 610; PDF 630]] y [[bishop-2006-prml.pdf#page=635|§13.2.1, pp. 615–616; PDF 635–636]]. Ejemplo de máquina propio.

## Gráficos y diagramas para entender el tema

### Distinguir lo oculto de lo observado

![Distinguir lo oculto de lo observado](<Recursos visuales/06-hmm.png>)

**Cómo leerlo:** Lee horizontalmente la evolución de los estados z y verticalmente la emisión de los datos x. Aunque cada estado dependa del anterior, la creencia sobre el estado actual incorpora el historial observado. Las flechas son dependencias del modelo probabilístico; no debes interpretarlas automáticamente como causas del mundo.

*Figuras originales elaboradas para estos apuntes. Los números y supuestos se explican en el texto; no son imágenes copiadas de los libros.*

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
