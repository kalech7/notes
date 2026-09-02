---
epoch: 1787808902943
mode: agent
backendId: codex
sessionId: "01a041b6-db5a-7da3-83eb-fd2d0d9142b1"
agentLabel: "Formas completa, reducida y compacta no entendi"
usage: '{"usedTokens":43005,"contextWindow":258400,"updatedAt":1787810886280}'
tags:
  - copilot-conversation
---

**user**: Formas completa, reducida y compacta
no entendi
[Timestamp: 2026/08/27 00:35:02]

**ai**: Voy a revisar esa sección exacta de [[00 Formulario razonado - fundamentos, espectro y SVD]] y te la explicaré con un único ejemplo numérico. Usaré la guía de Markdown de Obsidian solo para mantener bien formateadas las fórmulas y los enlaces a la nota.Las tres formas representan exactamente la misma matriz $A$. Solo cambia cuántas columnas “inútiles” se guardan.

Supongamos una matriz $A\in\mathbb{R}^{4\times3}$:

$$
A=
\begin{bmatrix}
3&0&0\\
0&2&0\\
0&0&0\\
0&0&0
\end{bmatrix}.
$$

Aquí:

$$
m=4,\qquad n=3,\qquad q=\min(4,3)=3,\qquad r=\operatorname{rank}(A)=2.
$$

El rango es $2$ porque solo existen dos direcciones activas: las asociadas a los valores singulares $3$ y $2$.

## 1. SVD completa

Conserva bases completas de los espacios de entrada y salida:

$$
A=U\Sigma V^T
$$

con dimensiones

$$
(4\times3)
=
(4\times4)(4\times3)(3\times3).
$$

En este ejemplo:

$$
U=I_4,
\qquad
\Sigma=
\begin{bmatrix}
3&0&0\\
0&2&0\\
0&0&0\\
0&0&0
\end{bmatrix},
\qquad
V^T=I_3.
$$

$U$ contiene cuatro direcciones porque debe ser una base completa de $\mathbb{R}^4$, aunque algunas no participen realmente en producir $A$.

## 2. SVD reducida

Elimina las columnas que solo servían para hacer cuadrada la matriz más grande:

$$
A=U_q\Sigma_qV_q^T
$$

con

$$
(4\times3)
=
(4\times3)(3\times3)(3\times3).
$$

En el ejemplo:

$$
U_q=
\begin{bmatrix}
1&0&0\\
0&1&0\\
0&0&1\\
0&0&0
\end{bmatrix},
\qquad
\Sigma_q=
\begin{bmatrix}
3&0&0\\
0&2&0\\
0&0&0
\end{bmatrix},
\qquad
V_q^T=I_3.
$$

Se eliminó la cuarta columna de $U$, pero todavía se conserva una dirección asociada al valor singular cero.

## 3. SVD compacta

Conserva solamente las direcciones realmente activas, es decir, aquellas cuyos valores singulares son positivos:

$$
A=U_r\Sigma_rV_r^T
$$

con

$$
(4\times3)
=
(4\times2)(2\times2)(2\times3).
$$

En el ejemplo:

$$
U_r=
\begin{bmatrix}
1&0\\
0&1\\
0&0\\
0&0
\end{bmatrix},
\qquad
\Sigma_r=
\begin{bmatrix}
3&0\\
0&2
\end{bmatrix},
\qquad
V_r^T=
\begin{bmatrix}
1&0&0\\
0&1&0
\end{bmatrix}.
$$

La tercera dirección desaparece porque su valor singular era cero. No aportaba nada:

$$
0\,u_3v_3^T=0.
$$

## La idea esencial

| Forma | Qué guarda | En el ejemplo |
| --- | --- | --- |
| Completa | Bases completas de entrada y salida | $4$ columnas en $U$ |
| Reducida | Solo $q=\min(m,n)$ direcciones | $3$ columnas en $U_q$ |
| Compacta | Solo las $r$ direcciones con $\sigma_i>0$ | $2$ columnas en $U_r$ |

Una forma sencilla de recordarlo:

- **Completa:** guarda todos los ejes.
- **Reducida:** elimina los ejes añadidos únicamente para completar una base cuadrada.
- **Compacta:** elimina además las direcciones con valor singular cero.

Las tres reconstruyen $A$ sin error. La compacta no es una aproximación.

> [!important] Compacta no significa truncada
> La SVD compacta elimina únicamente valores singulares iguales a cero.  
> La SVD truncada elimina también valores singulares positivos y, por eso, generalmente produce una aproximación $A_k\neq A$.

Además:

- Si $r=q$, la forma reducida y la compacta coinciden.
- Si $A$ es cuadrada, la forma completa y la reducida coinciden.
[Timestamp: 2026/08/27 00:35:02]

**user**: pero que es la truncada y como se calcula que es k
[Timestamp: 2026/08/27 00:40:54]

**ai**: Voy a conectar “truncada” con la compacta que acabamos de ver y revisar en la nota los criterios para escoger $k$. Usaré de nuevo la guía de Markdown de Obsidian para presentar las fórmulas con claridad.La **SVD truncada** es una aproximación: conserva solamente los $k$ componentes singulares más importantes y descarta el resto.

Si la SVD compacta exacta es

$$
A=\sum_{i=1}^{r}\sigma_i u_i v_i^T,
$$

la truncada es

$$
A_k=\sum_{i=1}^{k}\sigma_i u_i v_i^T
=U_k\Sigma_kV_k^T,
\qquad k<r.
$$

Como los valores singulares están ordenados

$$
\sigma_1\ge \sigma_2\ge\cdots\ge\sigma_r>0,
$$

se conservan los primeros $k$, es decir, los más grandes.

## ¿Qué significa $k$?

$k$ es simplemente el **número de patrones o componentes que decides conservar**.

Las dimensiones quedan:

$$
U_k:m\times k,
\qquad
\Sigma_k:k\times k,
\qquad
V_k^T:k\times n.
$$

Por ejemplo, si $A$ es $100\times50$ y eliges $k=3$:

$$
A_{100\times50}
\approx
(U_k)_{100\times3}
(\Sigma_k)_{3\times3}
(V_k^T)_{3\times50}.
$$

En lugar de guardar toda la matriz, guardas sus tres patrones dominantes.

## Ejemplo sencillo

Consideremos:

$$
A=
\begin{bmatrix}
3&0&0\\
0&2&0\\
0&0&0\\
0&0&0
\end{bmatrix}.
$$

Sus valores singulares positivos son:

$$
\sigma_1=3,\qquad \sigma_2=2.
$$

Por tanto, su rango es $r=2$ y su SVD compacta conserva ambos componentes:

$$
A=3u_1v_1^T+2u_2v_2^T.
$$

Si escogemos $k=1$, obtenemos la SVD truncada:

$$
A_1=3u_1v_1^T
=
\begin{bmatrix}
3&0&0\\
0&0&0\\
0&0&0\\
0&0&0
\end{bmatrix}.
$$

Hemos conservado el patrón de importancia $3$ y descartado el patrón de importancia $2$:

$$
A\approx A_1.
$$

No eliminamos una columna original de $A$; eliminamos un **componente singular**.

## ¿Cómo se elige $k$?

No existe un único $k$ automáticamente correcto. Se escoge según cuánto error toleras o cuánta información deseas conservar.

### Método 1: porcentaje de masa conservada

Para cada candidato $k$, calculas:

$$
E_k=
\frac{\sigma_1^2+\cdots+\sigma_k^2}
{\sigma_1^2+\cdots+\sigma_r^2}.
$$

Luego eliges el menor $k$ que alcance tu objetivo:

$$
k=
\min\left\{
j:
\frac{\sum_{i=1}^{j}\sigma_i^2}
{\sum_{i=1}^{r}\sigma_i^2}
\ge \tau
\right\},
$$

donde $\tau$ puede ser, por ejemplo, $0.90$, $0.95$ o $0.99$.

En el ejemplo anterior:

$$
E_1=\frac{3^2}{3^2+2^2}
=\frac9{13}
\approx69.23\%.
$$

Con $k=1$ solo conservamos aproximadamente el $69.23\%$. Si queremos conservar al menos el $95\%$, necesitamos $k=2$:

$$
E_2=\frac{3^2+2^2}{3^2+2^2}=100\%.
$$

### Método 2: fijar un error máximo

El error relativo de Frobenius es:

$$
\operatorname{error}_{\mathrm{rel}}
=
\frac{\lVert A-A_k\rVert_F}{\lVert A\rVert_F}
=
\sqrt{1-E_k}.
$$

Si quieres un error relativo máximo $\varepsilon$, debes escoger el menor $k$ que cumpla:

$$
E_k\ge 1-\varepsilon^2.
$$

Por ejemplo, para permitir como máximo un error del $5\%$:

$$
\varepsilon=0.05
$$

y necesitas:

$$
E_k\ge1-(0.05)^2=0.9975.
$$

Es decir, debes conservar al menos el $99.75\%$ de la masa cuadrática.

> [!warning] Cuidado con los porcentajes
> Conservar el $99\%$ de masa no significa tener un error relativo del $1\%$:
>
> $$
> \sqrt{1-0.99}=0.10.
> $$
>
> El error relativo sería del $10\%$.

## El ejemplo de tu nota

En [[00 Formulario razonado - fundamentos, espectro y SVD]] aparecen aproximadamente:

$$
\sigma=(11.3771,\ 8.0925,\ 0.2492,\ 0.1068).
$$

Con $k=2$ se conservan los dos valores grandes:

$$
E_2=
\frac{11.3771^2+8.0925^2}
{11.3771^2+8.0925^2+0.2492^2+0.1068^2}
\approx99.962\%.
$$

El error relativo queda:

$$
\sqrt{1-0.99962}\approx0.0194=1.94\%.
$$

Por eso $k=2$ es una elección razonable: comprime la matriz a dos componentes y pierde muy poco.

En resumen:

- $k=r$: reconstrucción exacta; no hay truncamiento efectivo.
- $k<r$: hay compresión y aproximación.
- Menor $k$: más compresión, pero más error.
- Mayor $k$: menos error, pero menos compresión.
- Normalmente se elige el **menor $k$ que cumpla el porcentaje conservado o el error máximo requerido**.
[Timestamp: 2026/08/27 00:40:54]

**user**: los valores singulares son las proyeccciones?
[Timestamp: 2026/08/27 00:43:21]

**ai**: No. Los **valores singulares** no son proyecciones; son **factores de escala**.

En

$$
A=U\Sigma V^T,
$$

cada elemento actúa así sobre un vector $x$:

$$
Ax=\sum_{i=1}^{r}\sigma_i(v_i^Tx)u_i.
$$

Aquí hay tres cosas diferentes:

- $v_i^Tx$: es la **coordenada o proyección escalar** de $x$ sobre la dirección $v_i$.
- $\sigma_i$: es el **valor singular**; indica cuánto amplifica o reduce $A$ esa coordenada.
- $u_i$: es la dirección en la que aparece el resultado.

El proceso es:

$$
x
\xrightarrow{\text{proyectar}}
v_i^Tx
\xrightarrow{\text{escalar}}
\sigma_i(v_i^Tx)
\xrightarrow{\text{colocar en salida}}
\sigma_i(v_i^Tx)u_i.
$$

## Ejemplo

Supongamos:

$$
\sigma_1=5
\qquad\text{y}\qquad
v_1^Tx=2.
$$

- La proyección o coordenada de $x$ sobre $v_1$ es $2$.
- El valor singular es $5$.
- Después de aplicar $A$, esa coordenada se convierte en:

$$
\sigma_1(v_1^Tx)=5(2)=10.
$$

La contribución al resultado es:

$$
10u_1.
$$

> [!important] Diferencia clave
> $v_i^Tx$ depende del vector $x$ que introduzcas.  
> $\sigma_i$ pertenece a la matriz $A$ y no cambia al cambiar $x$.

Además, si quieres ser totalmente preciso:

- **Proyección escalar** sobre $v_i$:

$$
v_i^Tx.
$$

- **Proyección vectorial** sobre $v_i$:

$$
(v_i^Tx)v_i.
$$

- **Valor singular**:

$$
\sigma_i,
$$

que mide cuánto estira $A$ la dirección $v_i$:

$$
Av_i=\sigma_i u_i.
$$

La frase para recordarlo es: **$V^T$ proyecta, $\Sigma$ escala y $U$ orienta el resultado**.
[Timestamp: 2026/08/27 00:43:21]

**user**: osea no entendi como se calucla ese valor singular?
[Timestamp: 2026/08/27 00:44:36]

**ai**: El valor singular se calcula a partir de los autovalores de $A^TA$:

$$
\boxed{\sigma_i=\sqrt{\lambda_i(A^TA)}}
$$

Es decir:

1. Calculas $A^TA$.
2. Encuentras sus autovalores $\lambda_i$.
3. Sacas la raíz cuadrada de cada autovalor.
4. Ordenas los resultados de mayor a menor.

## Ejemplo paso a paso

Sea

$$
A=
\begin{bmatrix}
1&0\\
1&0\\
0&1
\end{bmatrix}.
$$

Es una matriz $3\times2$.

### 1. Calculamos $A^TA$

Primero:

$$
A^T=
\begin{bmatrix}
1&1&0\\
0&0&1
\end{bmatrix}.
$$

Entonces:

$$
A^TA=
\begin{bmatrix}
1&1&0\\
0&0&1
\end{bmatrix}
\begin{bmatrix}
1&0\\
1&0\\
0&1
\end{bmatrix}
=
\begin{bmatrix}
2&0\\
0&1
\end{bmatrix}.
$$

### 2. Encontramos sus autovalores

Resolvemos:

$$
\det(A^TA-\lambda I)=0.
$$

En este caso:

$$
\det
\begin{bmatrix}
2-\lambda&0\\
0&1-\lambda
\end{bmatrix}
=0.
$$

Por tanto:

$$
(2-\lambda)(1-\lambda)=0.
$$

Los autovalores son:

$$
\lambda_1=2,
\qquad
\lambda_2=1.
$$

### 3. Sacamos las raíces cuadradas

Los valores singulares son:

$$
\sigma_1=\sqrt{\lambda_1}=\sqrt2,
$$

$$
\sigma_2=\sqrt{\lambda_2}=1.
$$

Por tanto:

$$
\boxed{\sigma_1=\sqrt2,\qquad \sigma_2=1}
$$

## ¿Por qué aparece la raíz cuadrada?

El primer vector singular derecho es

$$
v_1=
\begin{bmatrix}
1\\
0
\end{bmatrix}.
$$

Cuando $A$ actúa sobre él:

$$
Av_1=
\begin{bmatrix}
1\\
1\\
0
\end{bmatrix}.
$$

La longitud del resultado es:

$$
\lVert Av_1\rVert
=
\sqrt{1^2+1^2+0^2}
=
\sqrt2.
$$

Ese es precisamente el valor singular:

$$
\sigma_1=\sqrt2.
$$

Para la segunda dirección:

$$
v_2=
\begin{bmatrix}
0\\
1
\end{bmatrix},
\qquad
Av_2=
\begin{bmatrix}
0\\
0\\
1
\end{bmatrix}.
$$

Su longitud es:

$$
\lVert Av_2\rVert=1,
$$

por lo tanto:

$$
\sigma_2=1.
$$

La interpretación es:

$$
Av_i=\sigma_i u_i.
$$

- $v_i$ es una dirección de entrada de longitud $1$.
- $A$ transforma esa dirección.
- $\sigma_i$ indica la longitud obtenida, es decir, cuánto la estiró o comprimió.
- $u_i$ indica hacia dónde quedó apuntando.

Así que el valor singular no es una proyección: es el **factor de estiramiento de una dirección especial**. En este ejemplo, $A$ estira la primera dirección por $\sqrt2$ y mantiene la segunda con escala $1$.
[Timestamp: 2026/08/27 00:44:36]

**user**: esto explica que es la masa conservada y el errrorer realtivo
[Timestamp: 2026/08/27 00:52:29]

**ai**: Sí. Una vez calculados los valores singulares, con ellos puedes calcular la **masa conservada** y el **error relativo** de una SVD truncada.

Sigamos con el ejemplo anterior:

$$
\sigma_1=\sqrt2,
\qquad
\sigma_2=1.
$$

## Masa total

La masa cuadrática total de la matriz es la suma de los valores singulares al cuadrado:

$$
\text{masa total}
=
\sigma_1^2+\sigma_2^2.
$$

Entonces:

$$
\text{masa total}
=
(\sqrt2)^2+1^2
=2+1
=3.
$$

Esto coincide con la norma de Frobenius al cuadrado:

$$
\lVert A\rVert_F^2=\sum_i\sigma_i^2.
$$

## Si truncamos con $k=1$

Conservar $k=1$ significa guardar únicamente el primer valor singular:

$$
\sigma_1=\sqrt2.
$$

La masa conservada es:

$$
E_1=
\frac{\sigma_1^2}
{\sigma_1^2+\sigma_2^2}.
$$

Sustituyendo:

$$
E_1=
\frac{(\sqrt2)^2}
{(\sqrt2)^2+1^2}
=
\frac23
\approx0.6667.
$$

Por tanto, conservamos:

$$
\boxed{66.67\%}
$$

de la masa cuadrática de la matriz.

La masa descartada es:

$$
1-E_1
=
1-\frac23
=
\frac13
\approx33.33\%.
$$

## Error relativo

El error relativo de Frobenius es:

$$
\operatorname{error}_{\mathrm{rel}}
=
\frac{\lVert A-A_k\rVert_F}
{\lVert A\rVert_F}.
$$

También puede calcularse directamente con los valores singulares descartados:

$$
\operatorname{error}_{\mathrm{rel}}
=
\frac{\sqrt{\sum_{i=k+1}^{r}\sigma_i^2}}
{\sqrt{\sum_{i=1}^{r}\sigma_i^2}}.
$$

Como con $k=1$ descartamos $\sigma_2=1$:

$$
\operatorname{error}_{\mathrm{rel}}
=
\frac{\sqrt{1^2}}
{\sqrt{(\sqrt2)^2+1^2}}
=
\frac1{\sqrt3}
\approx0.577.
$$

Por tanto:

$$
\boxed{\operatorname{error}_{\mathrm{rel}}\approx57.7\%}
$$

## ¿Por qué no es $33.33\%$?

Porque el $33.33\%$ es la **masa cuadrática descartada**, mientras que el error relativo se mide en términos de longitud y requiere sacar la raíz cuadrada:

$$
\operatorname{error}_{\mathrm{rel}}
=
\sqrt{1-E_k}.
$$

En nuestro ejemplo:

$$
\sqrt{1-0.6667}
=
\sqrt{0.3333}
\approx0.577.
$$

Por eso:

- Masa conservada: $66.67\%$.
- Masa descartada: $33.33\%$.
- Error relativo: $57.7\%$.

La relación que debes recordar es:

$$
\boxed{
\operatorname{error}_{\mathrm{rel}}^2
=
1-E_k
}
$$

o equivalentemente:

$$
\boxed{
\operatorname{error}_{\mathrm{rel}}
=
\sqrt{1-E_k}
}
$$

Si conservamos ambos valores singulares, es decir, $k=2$:

$$
E_2=100\%,
\qquad
\operatorname{error}_{\mathrm{rel}}=0\%.
$$

En resumen: los $\sigma_i^2$ representan cómo se reparte la masa de la matriz; $k$ decide cuánta conservas y el error relativo mide cuánto se diferencia la aproximación $A_k$ de la matriz original $A$.
[Timestamp: 2026/08/27 00:52:29]

**user**: pero que quiere decir la masa cuadrada de la matriz?
[Timestamp: 2026/08/27 01:06:28]

**ai**: La **masa cuadrática** no es una masa física. Es una manera de medir el “tamaño total” de una matriz.

Se calcula sumando los cuadrados de todas sus entradas:

$$
\boxed{
\text{masa cuadrática de }A
=
\sum_{i,j}a_{ij}^2
=
\lVert A\rVert_F^2
}
$$

## Ejemplo

Consideremos:

$$
A=
\begin{bmatrix}
1&0\\
1&0\\
0&1
\end{bmatrix}.
$$

La masa cuadrática es:

$$
1^2+0^2+1^2+0^2+0^2+1^2=3.
$$

Por tanto:

$$
\boxed{\lVert A\rVert_F^2=3}.
$$

Puedes imaginar que colocamos todas las entradas de la matriz en un solo vector:

$$
(1,0,1,0,0,1).
$$

Su longitud al cuadrado es:

$$
1^2+0^2+1^2+0^2+0^2+1^2=3.
$$

Eso es la masa cuadrática.

## Relación con los valores singulares

La misma cantidad puede calcularse utilizando los valores singulares:

$$
\boxed{
\lVert A\rVert_F^2
=
\sigma_1^2+\sigma_2^2+\cdots+\sigma_r^2
}
$$

En nuestro ejemplo:

$$
\sigma_1=\sqrt2,
\qquad
\sigma_2=1.
$$

Entonces:

$$
\sigma_1^2+\sigma_2^2
=
(\sqrt2)^2+1^2
=
2+1
=
3.
$$

Obtenemos la misma masa cuadrática.

Esto permite interpretar cómo se reparte el tamaño de la matriz:

- Primer componente singular: aporta $\sigma_1^2=2$.
- Segundo componente singular: aporta $\sigma_2^2=1$.
- Masa total: $2+1=3$.

Por eso el primer componente conserva:

$$
\frac{\sigma_1^2}{\sigma_1^2+\sigma_2^2}
=
\frac23
=
66.67\%.
$$

## ¿Por qué se utilizan cuadrados?

Los cuadrados se usan porque:

- Evitan que valores positivos y negativos se cancelen.
- Permiten medir el tamaño total de todas las entradas.
- Hacen que la masa se pueda repartir exactamente entre los componentes singulares.
- Coinciden con la noción geométrica de longitud al cuadrado.

Por ejemplo, si sumáramos directamente las entradas de

$$
\begin{bmatrix}
1&-1
\end{bmatrix},
$$

obtendríamos cero:

$$
1+(-1)=0,
$$

aunque claramente la matriz no es nula.

Con cuadrados:

$$
1^2+(-1)^2=2.
$$

Así sí se refleja su tamaño.

> [!important] Interpretación
> Conservar el $90\%$ de masa cuadrática significa que $A_k$ conserva el $90\%$ de la suma de cuadrados de la matriz, repartida entre sus componentes singulares.
>
> No significa necesariamente conservar el $90\%$ de su significado, de sus filas o de sus columnas.

En datos centrados para PCA, esta cantidad se relaciona con la variación de los datos. En una matriz general, es más preciso llamarla **masa cuadrática**, **energía** o **magnitud total al cuadrado**.
[Timestamp: 2026/08/27 01:06:28]

**user**: entonces el error relativo de frobenius que quiere decir
[Timestamp: 2026/08/27 01:07:53]

**ai**: El **error relativo de Frobenius** indica qué tan diferente es la aproximación truncada $A_k$ de la matriz original $A$, comparando el error con el tamaño total de $A$.

$$
\boxed{
\operatorname{error}_{\mathrm{rel}}
=
\frac{\lVert A-A_k\rVert_F}{\lVert A\rVert_F}
}
$$

Se interpreta como un porcentaje:

- $0\%$: la aproximación es exacta.
- $5\%$: el error tiene una magnitud equivalente al $5\%$ del tamaño de $A$.
- $50\%$: la aproximación perdió una parte importante de la matriz.

Como

$$
\lVert A\rVert_F^2=\sum_i\sigma_i^2,
$$

también puede calcularse así:

$$
\operatorname{error}_{\mathrm{rel}}
=
\sqrt{
\frac{\sum_{i=k+1}^{r}\sigma_i^2}
{\sum_{i=1}^{r}\sigma_i^2}
}.
$$

Es decir:

1. Arriba sumas los cuadrados de los valores singulares que descartaste.
2. Abajo sumas los cuadrados de todos los valores singulares.
3. Divides.
4. Sacas la raíz cuadrada.

Por ejemplo, si conservas el $99\%$ de la masa cuadrática:

$$
E_k=0.99,
$$

entonces:

$$
\operatorname{error}_{\mathrm{rel}}
=
\sqrt{1-0.99}
=
\sqrt{0.01}
=
0.10.
$$

Por tanto, el error relativo es del:

$$
\boxed{10\%}
$$

La diferencia importante es:

- **Masa conservada:** cuánto del tamaño cuadrático de $A$ mantienes.
- **Error relativo de Frobenius:** cuánto difiere $A_k$ de $A$ en términos de longitud.

Por eso no son simplemente complementarios: hay que aplicar una raíz cuadrada.

En palabras sencillas: **mide el porcentaje de tamaño total de la matriz que tu aproximación no logra reproducir**.
[Timestamp: 2026/08/27 01:07:53]