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

## 1. Dirección propia

Para una matriz cuadrada $A\in\mathbb{R}^{n\times n}$, un vector no nulo $v$ es autovector si

$$
Av=\lambda v.
$$

$\lambda$ es el autovalor asociado. La transformación puede alargar, acortar, invertir o anular el vector, pero no lo desvía fuera de su recta. El requisito $v\neq0$ es esencial: $A0=\lambda0$ se cumple para cualquier $\lambda$ y no aporta una dirección.

## 2. Ejemplo simétrico

Sea

$$
A=\begin{bmatrix}2&1\\1&2\end{bmatrix}.
$$

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

## 3. Por qué la simetría es especial

El teorema espectral garantiza que una matriz real simétrica:

- tiene autovalores reales;
- admite una base ortonormal de autovectores;
- es diagonalizable mediante una matriz ortogonal.

Fuera del caso simétrico, estas propiedades pueden fallar: pueden aparecer autovalores complejos, no existir suficientes autovectores o no ser posible elegirlos ortogonales.

## 4. Contraejemplo nilpotente

Sea

$$
B=\begin{bmatrix}0&1\\0&0\end{bmatrix}.
$$

Como $B^2=0$, sus dos autovalores son cero. Sin embargo, $B$ no es la matriz cero: transforma $(0,1)$ en $(1,0)$. Este ejemplo será importante porque sus valores singulares son $(1,0)$, no $(0,0)$.

> [!warning] Autovalores ≠ valores singulares
> Coinciden bajo condiciones especiales, pero no son conceptos intercambiables para una matriz general.

## 5. Por qué una matriz rectangular no tiene autovalores propios

Si $X\in\mathbb{R}^{m\times n}$ con $m\neq n$, entonces

$$
Xv\in\mathbb{R}^m,qquad \lambda v\in\mathbb{R}^n.
$$

La ecuación $Xv=\lambda v$ no está bien tipada: sus lados viven en espacios diferentes. En cambio,

$$
X^TX\in\mathbb{R}^{n\times n},\qquad XX^T\in\mathbb{R}^{m\times m}
$$

sí son cuadradas. Sus autovectores organizan, respectivamente, el espacio de entrada y el de salida.

## 6. Espectro

El espectro es el conjunto de autovalores, contando multiplicidades cuando corresponde. Describe escalas propias de una transformación cuadrada, pero no debe confundirse con toda la información de la matriz.

## Preguntas rápidas

1. ¿Por qué el autovector debe ser no nulo?
2. Verifica a mano los dos autovectores de $A$.
3. ¿Qué garantiza el teorema espectral para matrices simétricas?
4. ¿Por qué $B$ separa con claridad autovalores y valores singulares?
5. ¿Qué falla dimensionalmente al hablar de autovalores de una matriz $5\times4$?

