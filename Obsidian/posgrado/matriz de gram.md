# Matriz de Gram: qué mide y por qué puede causar problemas numéricos

## La idea antes de la fórmula

La matriz de Gram reúne los productos internos entre un conjunto de vectores. Cada casilla responde: **¿cuánto se alinean estos dos vectores, teniendo en cuenta también sus longitudes?**

Para vectores reales, el producto interno usual multiplica componentes correspondientes y suma. Si $u=(1,2)$ y $v=(3,4)$:

$$u^T v=1\cdot3+2\cdot4=11.$$

No es una distancia. Un producto interno grande puede deberse a una dirección parecida, a vectores largos o a ambas cosas. Para comparar dirección mediante coseno, divides por las dos normas, siempre que no sean cero.

## Qué significa $G=A^T A$

Supón que guardas los vectores como **columnas** de $A$. Si hay $n$ vectores, cada uno con $m$ componentes, entonces:

$$A\in\mathbb{R}^{m\times n},\qquad A^T\in\mathbb{R}^{n\times m},\qquad G=A^TA\in\mathbb{R}^{n\times n}.$$

$T$ significa transpuesta: intercambia filas y columnas. La casilla de fila $i$, columna $j$ de $G$ es:

$$G_{ij}=a_i^T a_j.$$

Aquí $a_i$ es la columna $i$ de $A$. Si tus vectores están almacenados como filas, la Gram entre esos vectores es $AA^T$. **Mira dónde están los vectores antes de elegir el orden.** En vectores complejos se usa transpuesta conjugada en lugar de transpuesta simple.

## Ejemplo completo a mano

Tomemos $a_1=(1,0)$ y $a_2=(1,1)$ como columnas:

$$A=\begin{bmatrix}1&1\\0&1\end{bmatrix},\qquad
A^T=\begin{bmatrix}1&0\\1&1\end{bmatrix}.$$

Calcula las cuatro comparaciones:

| Casilla | Operación | Valor |
|---|---|---:|
| $G_{11}$ | $a_1^Ta_1=1\cdot1+0\cdot0$ | 1 |
| $G_{12}$ | $a_1^Ta_2=1\cdot1+0\cdot1$ | 1 |
| $G_{21}$ | $a_2^Ta_1=1\cdot1+1\cdot0$ | 1 |
| $G_{22}$ | $a_2^Ta_2=1\cdot1+1\cdot1$ | 2 |

Por tanto:

$$G=\begin{bmatrix}1&1\\1&2\end{bmatrix}.$$

La diagonal contiene longitudes **al cuadrado**: $\|a_1\|^2=1$ y $\|a_2\|^2=2$. Fuera de la diagonal están las comparaciones entre vectores distintos. Los dos valores simétricos coinciden porque $a_1^Ta_2=a_2^Ta_1$.

Para estos vectores, el coseno es $1/(1\sqrt{2})\approx0{,}707$. El producto interno es 1, pero el coseno no es 1: los vectores no tienen la misma dirección.

## Qué revela sobre los vectores

- Si las columnas son ortogonales, los productos entre columnas distintas son cero y $G$ es diagonal.
- Si además tienen norma 1, son ortonormales y $G=I$.
- Si las columnas son linealmente independientes, $G$ es definida positiva e invertible.
- Si una columna es combinación de las otras, $G$ es singular: no tiene inversa.

La propiedad central se ve con cualquier vector de coeficientes $z$:

$$z^TGz=z^TA^TAz=(Az)^T(Az)=\|Az\|^2\geq0.$$

Por eso toda Gram es **semidefinida positiva**. «Definida positiva» exige que el resultado sea estrictamente positivo para todo $z\neq0$; esto ocurre cuando $Az=0$ solo tiene la solución $z=0$, es decir, cuando las columnas son independientes.

## Corrigiendo el apunte: no basta decir «números pequeños»

El apunte original decía: «es inestable para números muy pequeños». La idea necesita precisión: al formar $A^TA$ puedes empeorar mucho el **condicionamiento**, especialmente si las columnas de $A$ son casi dependientes.

El número de condición mide sensibilidad a perturbaciones relativas. Usando norma 2 y columnas de rango completo:

$$\kappa_2(A)=\frac{\sigma_{\max}(A)}{\sigma_{\min}(A)},\qquad
\kappa_2(A^TA)=\kappa_2(A)^2.$$

Las $\sigma$ son los valores singulares de $A$: describen cuánto estira o comprime la matriz en distintas direcciones. Los autovalores de $A^TA$ son sus cuadrados. Si una dirección ya se comprime muchísimo, al elevar al cuadrado su valor se vuelve todavía más pequeño respecto al mayor.

Si $\kappa_2(A)=10^4$, la Gram tiene condición $10^8$. Eso aumenta la sensibilidad al redondeo; no significa que cada cálculo vaya a perder exactamente ocho decimales.

**Contraejemplo útil:** $A=10^{-8}I$ tiene números pequeños, pero $\kappa_2(A)=1$ y $A^TA=10^{-16}I$ también tiene condición 1. La escala absoluta y el mal condicionamiento son conceptos distintos. Escalas extremas sí pueden producir problemas de representación, como desbordamiento o subdesbordamiento.

## Ejemplo de información que se pierde al formar Gram

Sea:

$$A=\begin{bmatrix}1&1\\0&\varepsilon\end{bmatrix},\qquad
A^TA=\begin{bmatrix}1&1\\1&1+\varepsilon^2\end{bmatrix}.$$

Las columnas $(1,0)$ y $(1,\varepsilon)$ son casi iguales cuando $\varepsilon$ es pequeño. En aritmética exacta, si $\varepsilon\neq0$ son independientes y:

$$\det(A^TA)=1(1+\varepsilon^2)-1=\varepsilon^2>0.$$

Con $\varepsilon=10^{-8}$, $\varepsilon^2=10^{-16}$. En el cálculo habitual con float64, sumar $1+10^{-16}$ redondea a 1. La Gram calculada puede quedar:

$$\widehat{G}=\begin{bmatrix}1&1\\1&1\end{bmatrix},$$

que parece singular. La pequeña diferencia que distinguía las columnas se perdió al sumar cantidades de escalas muy distintas. No desapareció porque todo número pequeño sea imposible de almacenar: $10^{-16}$ puede representarse aproximadamente; el problema es conservar su efecto **al sumarlo a 1**.

## Para qué aparece en mínimos cuadrados

Quieres encontrar $x$ para que $Ax$ se acerque lo más posible a $b$:

$$\min_x\|Ax-b\|_2^2.$$

La condición de primer orden conduce a las ecuaciones normales:

$$A^TAx=A^Tb.$$

Aquí aparece Gram. Matemáticamente, con columnas independientes, la solución es única. Numéricamente, formar $A^TA$ puede amplificar los problemas anteriores.

Para resolver mínimos cuadrados, una factorización QR o SVD evita formar explícitamente la Gram. QR usa $A=QR$ con columnas ortonormales en $Q$ y transforma el problema en uno triangular; SVD permite además estudiar direcciones casi dependientes. No eliminan la sensibilidad inherente de un problema mal condicionado, pero evitan empeorarla al construir las ecuaciones normales.

La expresión $(A^TA)^{-1}A^Tb$ sirve para una derivación bajo sus supuestos; no es una invitación a calcular una inversa explícita para resolver el problema.

## Comprueba que lo entendiste

> [!question]- Si $A$ tiene tamaño $5\times3$ y los vectores son columnas, ¿cuánto mide su Gram?
> $3\times3$: compara tres vectores entre sí. Cada producto interno usa sus cinco componentes.

> [!question]- ¿Una Gram siempre es invertible?
> No. Si los vectores son dependientes, es singular. Siempre es semidefinida positiva, pero solo es definida positiva cuando las columnas son independientes.

> [!question]- ¿Por qué $10^{-8}I$ no demuestra mal condicionamiento?
> Porque todas sus direcciones se escalan por igual: el cociente entre el mayor y el menor valor singular es 1.

> [!question]- ¿Qué empeora al pasar de $A$ a $A^TA$?
> Para rango completo, el número de condición en norma 2 se eleva al cuadrado. Además, formar los productos y sumarlos introduce redondeo.
