---
tags:
  - algebra-lineal
  - svd
  - valores-singulares
related: "[[00 Índice - Espectro, SVD y rango bajo]]"
---

# Descomposición en valores singulares: SVD

Anterior: [[02 Autovalores, autovectores y espectro]] · Siguiente: [[04 Aproximación de rango bajo y elección de k]]

Formulario general: [[00 Formulario razonado - fundamentos, espectro y SVD|fórmulas explicadas paso a paso]].

## 1. Definición

Toda matriz $A\in\mathbb{R}^{m\times n}$ admite una descomposición

$$
A=U\Sigma V^T,
$$

donde $U$ y $V$ tienen columnas ortonormales y $\Sigma$ contiene valores singulares no negativos, ordenados

$$
\sigma_1\ge\sigma_2\ge\cdots\ge0.
$$

La SVD funciona para matrices cuadradas, rectangulares, singulares y de rango deficiente.

![[assets/infografia-04.jpg|900]]

## 2. Lectura geométrica

![[assets/12-geometria-svd.jpg|900]]

Para calcular $y=Ax$:

1. $z=V^Tx$: expresa la entrada en las direcciones singulares derechas;
2. $w=\Sigma z$: escala cada coordenada sin mezclar ejes;
3. $y=Uw$: reconstruye la salida en las direcciones singulares izquierdas.

La multiplicación se lee **de derecha a izquierda**. Si $V=[v_1,\ldots,v_n]$, entonces

$$
z=V^Tx=
\begin{bmatrix}
v_1^Tx\\
\vdots\\
v_n^Tx
\end{bmatrix}.
$$

Cada $z_i=v_i^Tx$ mide cuánto de $x$ está alineado con $v_i$. Como $\Sigma$ es diagonal,

$$
w_i=\sigma_i z_i:
$$

cada coordenada se estira, comprime o anula **sin mezclarse con las demás**. Finalmente, $U$ combina las direcciones de salida $u_i$:

$$
Ax=Uw=\sum_{i=1}^{r}\sigma_i(v_i^Tx)u_i.
$$

```mermaid
flowchart LR
    X["x en Rⁿ"] -->|"Vᵀ: coordenadas"| Z["z"]
    Z -->|"Σ: escalas σᵢ"| W["w"]
    W -->|"U: reconstrucción"| Y["Ax en Rᵐ"]
```

Si $x$ tiene una componente en $\ker(A)$, la SVD compacta no la conserva porque esa dirección tiene valor singular cero y no contribuye a $Ax$.

## 3. Tres formas y sus dimensiones

Sea $q=\min(m,n)$ y $r=\operatorname{rank}(A)$.

| Forma | $U$ | $\Sigma$ | $V^T$ |
| --- | --- | --- | --- |
| Completa | $m\times m$ | $m\times n$ | $n\times n$ |
| Reducida | $m\times q$ | $q\times q$ | $q\times n$ |
| Compacta | $m\times r$ | $r\times r$ | $r\times n$ |

La forma reducida de NumPy con `full_matrices=False` conserva $q$ direcciones, incluso si algunas tienen valor singular cero. La compacta conserva solo las $r$ direcciones activas.

### Auditoría dimensional de la forma compacta

Para $A=U_r\Sigma_rV_r^T$ y $x\in\mathbb{R}^n$:

| Etapa | Multiplicación | Dimensiones | Resultado |
| --- | --- | --- | --- |
| Coordenadas activas | $z=V_r^Tx$ | $(r\times n)(n\times1)$ | $z\in\mathbb{R}^r$ |
| Escala | $w=\Sigma_rz$ | $(r\times r)(r\times1)$ | $w\in\mathbb{R}^r$ |
| Reconstrucción | $y=U_rw$ | $(m\times r)(r\times1)$ | $y\in\mathbb{R}^m$ |

> [!warning] Señal de error
> Si las dimensiones interiores no coinciden, la fórmula no está bien escrita aunque la idea verbal parezca correcta.

## 4. Puente espectral

Si $v_i$ es una columna de $V$ y $u_i$ una columna de $U$:

$$
Av_i=\sigma_i u_i,
\qquad
A^Tu_i=\sigma_i v_i.
$$

Por tanto,

$$
A^TAv_i=\sigma_i^2v_i,
\qquad
AA^Tu_i=\sigma_i^2u_i.
$$

Los autovalores no nulos de $A^TA$ y $AA^T$ son los mismos y valen $\sigma_i^2$. $v_i$ vive en el espacio de entrada; $u_i$, en el espacio de salida.

### Derivación completa desde $A^TA$

Partimos de un autovector unitario $v_i$ de $A^TA$:

$$
A^TAv_i=\lambda_i v_i,
\qquad
\lVert v_i\rVert_2=1.
$$

Como $A^TA$ es semidefinida positiva, $\lambda_i\ge0$. Definimos

$$
\sigma_i=\sqrt{\lambda_i}.
$$

Si $\sigma_i>0$, definimos la dirección de salida

$$
u_i=\frac{Av_i}{\sigma_i}.
$$

No estamos suponiendo que $u_i$ sea unitario; lo comprobamos:

$$
\begin{aligned}
\lVert u_i\rVert_2^2
&=\frac{1}{\sigma_i^2}(Av_i)^T(Av_i)\\
&=\frac{1}{\sigma_i^2}v_i^TA^TAv_i\\
&=\frac{1}{\sigma_i^2}v_i^T(\sigma_i^2v_i)\\
&=v_i^Tv_i=1.
\end{aligned}
$$

De la definición se obtiene inmediatamente

$$
Av_i=\sigma_i u_i.
$$

Además,

$$
A^Tu_i
=\frac{1}{\sigma_i}A^TAv_i
=\frac{\sigma_i^2}{\sigma_i}v_i
=\sigma_i v_i.
$$

Al aplicar $A$ otra vez,

$$
AA^Tu_i=A(\sigma_i v_i)=\sigma_i Av_i=\sigma_i^2u_i.
$$

Esto demuestra que $v_i$ y $u_i$ describen la misma escala $\sigma_i$ desde dos espacios diferentes.

> [!note] ¿Qué pasa cuando $\sigma_i=0$?
> No se puede dividir por $\sigma_i$. En ese caso, $Av_i=0$ y $v_i\in\ker(A)$: es una dirección de entrada que la matriz anula. En la SVD completa, las columnas faltantes de $U$ se completan con una base ortonormal; en la compacta, esas direcciones inactivas se omiten.

## 5. Microejemplo rectangular completo

Considera

$$
A=
\begin{bmatrix}
1&0\\
1&0\\
0&1
\end{bmatrix}
\in\mathbb{R}^{3\times2}.
$$

Sus columnas son ortogonales. La primera tiene norma $\sqrt2$ y la segunda norma $1$, por lo que una SVD compacta es

$$
U=
\begin{bmatrix}
\tfrac{1}{\sqrt2}&0\\
\tfrac{1}{\sqrt2}&0\\
0&1
\end{bmatrix},
\qquad
\Sigma=
\begin{bmatrix}
\sqrt2&0\\
0&1
\end{bmatrix},
\qquad
V=I_2.
$$

Comprueba que $U\Sigma=A$. Ahora toma

$$
x=\begin{bmatrix}3\\-2\end{bmatrix}.
$$

El recorrido completo es

$$
z=V^Tx=\begin{bmatrix}3\\-2\end{bmatrix},
$$

$$
w=\Sigma z=\begin{bmatrix}3\sqrt2\\-2\end{bmatrix},
$$

$$
y=Uw=
\begin{bmatrix}3\\3\\-2\end{bmatrix}
=Ax.
$$

Aquí se ve el papel de cada factor: $V^T$ obtiene coordenadas, $\Sigma$ aplica las escalas $\sqrt2$ y $1$, y $U$ expresa la salida en $\mathbb{R}^3$.

## 6. Valores singulares frente a autovalores

Los valores singulares siempre son reales y no negativos. Se derivan de $A^TA$, no de los autovalores de $A$ en general:

$$
\sigma_i(A)=\sqrt{\lambda_i(A^TA)}.
$$

Para la matriz nilpotente $B$ de la nota anterior, $\lambda(B)=(0,0)$, pero $\sigma(B)=(1,0)$.

## 7. Unicidad con matices

La matriz $A$ reconstruida es estable, pero los factores no siempre son literalmente únicos:

- **Ambigüedad de signo:** podemos cambiar simultáneamente $u_i\to-u_i$ y $v_i\to-v_i$ sin cambiar $\sigma_i u_i v_i^T$.
- **Valores repetidos:** si varios $\sigma_i$ son iguales, puede cambiar la base ortonormal elegida dentro de ese subespacio.

Por eso, al comparar dos SVD, no se debe exigir que todos los vectores tengan exactamente el mismo signo.

## 8. Expansión en matrices de rango uno

La SVD también se escribe

$$
A=\sum_{i=1}^r\sigma_i u_i v_i^T.
$$

Cada término exterior $u_iv_i^T$ tiene rango 1. Esta suma ordena los componentes desde la mayor hasta la menor escala y prepara el truncamiento.

## Para recordar

> [!tip] Frase mnemotécnica
> **V encuentra direcciones de entrada; Σ mide su importancia algebraica; U las lleva a la salida.**
