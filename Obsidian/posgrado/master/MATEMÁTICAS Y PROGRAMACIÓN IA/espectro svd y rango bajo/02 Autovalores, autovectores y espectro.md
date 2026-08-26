---
tags:
  - algebra-lineal
  - autovalores
  - autovectores
  - espectro
related: "[[00 Índice - Espectro, SVD y rango bajo]]"
---

# Autovalores, autovectores y espectro

Anterior: [[01 Prerrequisitos - producto interno, norma y ortogonalidad]] · Siguiente: [[03 Descomposición en valores singulares - SVD]]

Formulario general: [[00 Formulario razonado - fundamentos, espectro y SVD|fórmulas explicadas paso a paso]].

## 1. Dirección propia

Para una matriz cuadrada $A\in\mathbb{R}^{n\times n}$, un vector no nulo $v$ es autovector si

$$
Av=\lambda v.
$$

$\lambda$ es el autovalor asociado. La transformación puede alargar, acortar, invertir o anular el vector, pero no lo desvía fuera de su recta. El requisito $v\neq0$ es esencial: $A0=\lambda0$ se cumple para cualquier $\lambda$ y no aporta una dirección.

![[assets/infografia-03.jpg|900]]

## 2. Cómo se calculan los autovalores

La definición $Av=\lambda v$ también explica el procedimiento de cálculo. Llevamos todos los términos al mismo lado:

$$
Av-\lambda v=0.
$$

Como $v=Iv$,

$$
(A-\lambda I)v=0.
$$

Buscamos un vector **no nulo**. Si $A-\lambda I$ fuese invertible, al multiplicar por su inversa obtendríamos necesariamente $v=0$. Por tanto, debe ser singular:

$$
\det(A-\lambda I)=0.
$$

Esta es la **ecuación característica**. Para

$$
A=\begin{bmatrix}a&b\\c&d\end{bmatrix},
$$

se obtiene

$$
\det(A-\lambda I)
=\det\begin{bmatrix}a-\lambda&b\\c&d-\lambda\end{bmatrix}
=(a-\lambda)(d-\lambda)-bc.
$$

Las raíces de ese polinomio son los autovalores. Después, para cada raíz $\lambda_i$, se resuelve

$$
(A-\lambda_i I)v=0
$$

para encontrar los autovectores asociados.

## 3. Ejemplo simétrico, paso a paso

Sea

$$
A=\begin{bmatrix}2&1\\1&2\end{bmatrix}.
$$

### Paso 1: ecuación característica

$$
\det(A-\lambda I)
=\det\begin{bmatrix}2-\lambda&1\\1&2-\lambda\end{bmatrix}
=(2-\lambda)^2-1.
$$

Factorizamos:

$$
(2-\lambda)^2-1
=\lambda^2-4\lambda+3
=(\lambda-3)(\lambda-1).
$$

Por tanto,

$$
\lambda_1=3,
\qquad
\lambda_2=1.
$$

### Paso 2: autovector para $\lambda_1=3$

$$
(A-3I)v
=\begin{bmatrix}-1&1\\1&-1\end{bmatrix}
\begin{bmatrix}v_1\\v_2\end{bmatrix}
=0.
$$

La ecuación $-v_1+v_2=0$ implica $v_2=v_1$. Elegimos el representante $(1,1)^T$ y lo normalizamos:

$$
q_1=\frac{1}{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix}.
$$

### Paso 3: autovector para $\lambda_2=1$

$$
(A-I)v
=\begin{bmatrix}1&1\\1&1\end{bmatrix}
\begin{bmatrix}v_1\\v_2\end{bmatrix}
=0.
$$

Ahora $v_1+v_2=0$, así que $v_2=-v_1$. Normalizando $(1,-1)^T$:

$$
q_2=\frac{1}{\sqrt2}\begin{bmatrix}1\\-1\end{bmatrix}.
$$

### Paso 4: comprobar la dirección y construir la diagonalización

Para $u_1=(1,1)$:

$$
Au_1=(3,3)=3u_1.
$$

Para $u_2=(1,-1)$:

$$
Au_2=(1,-1)=u_2.
$$

Los autovalores son $3$ y $1$. Tras normalizar, $q_1=u_1/\sqrt2$ y $q_2=u_2/\sqrt2$ forman una base ortonormal.

![[assets/06-matriz-simetrica.jpg|850]]

La descomposición espectral es

$$
A=Q\Lambda Q^T,
$$

donde $Q$ contiene los autovectores ortonormales y $\Lambda$ los autovalores. El proceso puede leerse como: $Q^T$ cambia a coordenadas propias, $\Lambda$ escala cada eje y $Q$ vuelve a las coordenadas originales.

En este ejemplo,

$$
Q=\frac{1}{\sqrt2}
\begin{bmatrix}
1&1\\
1&-1
\end{bmatrix},
\qquad
\Lambda=\begin{bmatrix}3&0\\0&1\end{bmatrix}.
$$

> [!tip] Qué significa diagonalizar
> En la base usual, $A$ mezcla las coordenadas. En la base formada por $q_1$ y $q_2$, la misma transformación solo multiplica una coordenada por $3$ y la otra por $1$.

## 4. Por qué la simetría es especial

El teorema espectral garantiza que una matriz real simétrica:

- tiene autovalores reales;
- admite una base ortonormal de autovectores;
- es diagonalizable mediante una matriz ortogonal.

Fuera del caso simétrico, estas propiedades pueden fallar: pueden aparecer autovalores complejos, no existir suficientes autovectores o no ser posible elegirlos ortogonales.

## 5. Contraejemplo nilpotente

Sea

$$
B=\begin{bmatrix}0&1\\0&0\end{bmatrix}.
$$

Como $B^2=0$, sus dos autovalores son cero. Sin embargo, $B$ no es la matriz cero: transforma $(0,1)$ en $(1,0)$. Este ejemplo será importante porque sus valores singulares son $(1,0)$, no $(0,0)$.

> [!warning] Autovalores ≠ valores singulares
> Coinciden bajo condiciones especiales, pero no son conceptos intercambiables para una matriz general.

## 6. Por qué una matriz rectangular no tiene autovalores propios

Si $X\in\mathbb{R}^{m\times n}$ con $m\neq n$, entonces

$$
Xv\in\mathbb{R}^m,
\qquad
\lambda v\in\mathbb{R}^n.
$$

La ecuación $Xv=\lambda v$ no está bien tipada: sus lados viven en espacios diferentes. En cambio,

| Expresión | Dimensión | Espacio |
| --- | ---: | --- |
| $v$ | $n\times1$ | entrada $\mathbb{R}^n$ |
| $Xv$ | $m\times1$ | salida $\mathbb{R}^m$ |
| $\lambda v$ | $n\times1$ | entrada $\mathbb{R}^n$ |

Si $m\neq n$, $Xv$ y $\lambda v$ ni siquiera tienen el mismo número de componentes. El problema no es que «falte un algoritmo», sino que la igualdad compara objetos de tipos distintos.

$$
X^TX\in\mathbb{R}^{n\times n},\qquad XX^T\in\mathbb{R}^{m\times m}
$$

sí son cuadradas. Sus autovectores organizan, respectivamente, el espacio de entrada y el de salida.

## 7. Espectro

El espectro es el conjunto de autovalores, contando multiplicidades cuando corresponde. Describe escalas propias de una transformación cuadrada, pero no debe confundirse con toda la información de la matriz.

## Preguntas rápidas

1. ¿Por qué el autovector debe ser no nulo?
2. Verifica a mano los dos autovectores de $A$.
3. ¿Qué garantiza el teorema espectral para matrices simétricas?
4. ¿Por qué $B$ separa con claridad autovalores y valores singulares?
5. ¿Qué falla dimensionalmente al hablar de autovalores de una matriz $5\times4$?
