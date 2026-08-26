---
epoch: 1787706327442
mode: agent
backendId: codex
sessionId: "01a03b95-7d2f-7703-aef5-1e90c5ca26ab"
agentLabel: "dame un ejemplo de proyeccion"
usage: '{"usedTokens":30073,"contextWindow":258400,"updatedAt":1787707628779}'
tags:
  - copilot-conversation
---

**user**: dame un ejemplo de proyeccion
[Timestamp: 2026/08/25 20:05:27]

**ai**: Voy a revisar la nota adjunta para darte un ejemplo que encaje con su explicación y notación; usaré la guía de Markdown de Obsidian para conservar bien las fórmulas.Por ejemplo, proyectemos

$$
x=\begin{bmatrix}3\\1\end{bmatrix}
$$

sobre la dirección

$$
u=\begin{bmatrix}1\\1\end{bmatrix}.
$$

Como $u$ no es unitario, usamos:

$$
\operatorname{proj}_u(x)=\frac{u^Tx}{u^Tu}u.
$$

Calculamos:

$$
u^Tx=(1)(3)+(1)(1)=4,
$$

$$
u^Tu=(1)(1)+(1)(1)=2.
$$

Entonces:

$$
\operatorname{proj}_u(x)
=\frac{4}{2}\begin{bmatrix}1\\1\end{bmatrix}
=\begin{bmatrix}2\\2\end{bmatrix}.
$$

Por tanto, la “sombra” de $x$ sobre la recta definida por $u$ es:

$$
\boxed{\operatorname{proj}_u(x)=\begin{bmatrix}2\\2\end{bmatrix}}
$$

El residuo es:

$$
r=x-\operatorname{proj}_u(x)
=\begin{bmatrix}3\\1\end{bmatrix}
-\begin{bmatrix}2\\2\end{bmatrix}
=\begin{bmatrix}1\\-1\end{bmatrix}.
$$

Podemos comprobar que el residuo es perpendicular a $u$:

$$
u^Tr=(1)(1)+(1)(-1)=0.
$$

Así, el vector original queda descompuesto en dos partes:

$$
\underbrace{\begin{bmatrix}3\\1\end{bmatrix}}_{x}
=
\underbrace{\begin{bmatrix}2\\2\end{bmatrix}}_{\text{proyección}}
+
\underbrace{\begin{bmatrix}1\\-1\end{bmatrix}}_{\text{residuo perpendicular}}.
$$
[Timestamp: 2026/08/25 20:05:27]

**user**: esto explicame mejor Una base ordenada $B=(b_1,\ldots,b_n)$ es un conjunto de direcciones que cumple dos propiedades:

1. **genera** el espacio: todo vector se obtiene combinando los $b_i$;
[Timestamp: 2026/08/25 20:11:39]

**ai**: Una base ordenada

$$
B=(b_1,\ldots,b_n)
$$

es una colección de vectores que funciona como un **sistema de coordenadas**.

Decir que la base **genera el espacio** significa que cualquier vector $x$ de ese espacio puede construirse multiplicando cada vector de la base por un número y sumando los resultados:

$$
x=c_1b_1+c_2b_2+\cdots+c_nb_n.
$$

Los números $c_1,\ldots,c_n$ son las **coordenadas de $x$ en la base $B$**.

### Ejemplo en $\mathbb{R}^2$

Consideremos la base usual:

$$
b_1=\begin{bmatrix}1\\0\end{bmatrix},
\qquad
b_2=\begin{bmatrix}0\\1\end{bmatrix}.
$$

Estos vectores representan las direcciones horizontal y vertical. Cualquier vector del plano puede construirse combinándolos. Por ejemplo:

$$
x=\begin{bmatrix}3\\2\end{bmatrix}
=3\begin{bmatrix}1\\0\end{bmatrix}
+2\begin{bmatrix}0\\1\end{bmatrix}.
$$

Es decir:

$$
x=3b_1+2b_2.
$$

Por eso $b_1$ y $b_2$ generan todo $\mathbb{R}^2$: ajustando los números que los multiplican podemos llegar a cualquier punto del plano.

### Una base diferente

Las direcciones no tienen que coincidir con los ejes. También podemos usar:

$$
b_1=\begin{bmatrix}1\\1\end{bmatrix},
\qquad
b_2=\begin{bmatrix}1\\-1\end{bmatrix}.
$$

Por ejemplo, el mismo vector $x=[3,2]^T$ se puede escribir como:

$$
\begin{bmatrix}3\\2\end{bmatrix}
=
\frac{5}{2}\begin{bmatrix}1\\1\end{bmatrix}
+
\frac{1}{2}\begin{bmatrix}1\\-1\end{bmatrix}.
$$

Porque:

$$
\begin{bmatrix}2.5\\2.5\end{bmatrix}
+
\begin{bmatrix}0.5\\-0.5\end{bmatrix}
=
\begin{bmatrix}3\\2\end{bmatrix}.
$$

Así, **generar el espacio** quiere decir:

> Las direcciones de la base son suficientes para construir cualquier vector del espacio mediante escalamiento y suma.

En $\mathbb{R}^2$, dos vectores que apuntan en direcciones diferentes pueden generar todo el plano. Si ambos apuntan sobre la misma recta, solamente generan esa recta y no forman una base de $\mathbb{R}^2$.
[Timestamp: 2026/08/25 20:11:39]

**user**: como es un vector redundante
[Timestamp: 2026/08/25 20:21:45]

**ai**: Un vector es **redundante** cuando no aporta una dirección nueva: ya puede construirse combinando los otros vectores.

Por ejemplo, en $\mathbb{R}^2$:

$$
b_1=\begin{bmatrix}1\\0\end{bmatrix},
\qquad
b_2=\begin{bmatrix}0\\1\end{bmatrix},
\qquad
b_3=\begin{bmatrix}1\\1\end{bmatrix}.
$$

El tercer vector es redundante porque:

$$
b_3=b_1+b_2.
$$

Con $b_1$ y $b_2$ ya podemos generar todo el plano. Agregar $b_3$ no permite llegar a ningún lugar nuevo.

Visualmente:

- $b_1$ aporta la dirección horizontal.
- $b_2$ aporta la dirección vertical.
- $b_3$ es diagonal, pero se obtiene combinando las dos direcciones anteriores.

Otro ejemplo más sencillo:

$$
v_1=\begin{bmatrix}1\\2\end{bmatrix},
\qquad
v_2=\begin{bmatrix}2\\4\end{bmatrix}.
$$

Aquí $v_2$ es redundante porque:

$$
v_2=2v_1.
$$

Ambos apuntan sobre la misma recta. Aunque tenemos dos vectores, solamente hay **una dirección independiente**.

Por eso, una base no debe contener vectores redundantes. Sus vectores deben ser **linealmente independientes**:

> Ningún vector de la base puede construirse combinando los demás.
[Timestamp: 2026/08/25 20:21:45]

**user**: entonces como se que la base genera un nuevo ?
[Timestamp: 2026/08/25 20:24:14]

**ai**: Una base no “genera algo nuevo” al agregar vectores. Lo que debes comprobar es si cada vector aporta una **dirección nueva** que los anteriores no podían producir.

Supongamos que ya tienes $b_1,\ldots,b_k$ y quieres agregar $v$. Pregunta:

> ¿Puedo escribir $v$ como combinación de los vectores anteriores?

Es decir, intenta resolver:

$$
v=c_1b_1+\cdots+c_kb_k.
$$

- Si existen valores $c_1,\ldots,c_k$, entonces $v$ es **redundante**.
- Si no existen, entonces $v$ aporta una **dirección nueva**.

### Ejemplo de vector redundante

Tenemos:

$$
b_1=\begin{bmatrix}1\\0\end{bmatrix}
$$

y queremos agregar:

$$
v=\begin{bmatrix}3\\0\end{bmatrix}.
$$

Como

$$
v=3b_1,
$$

$v$ no aporta una dirección nueva. Ambos están sobre la misma recta.

### Ejemplo de dirección nueva

Ahora queremos agregar:

$$
b_2=\begin{bmatrix}0\\1\end{bmatrix}.
$$

No existe ningún número $c$ que cumpla:

$$
\begin{bmatrix}0\\1\end{bmatrix}
=
c\begin{bmatrix}1\\0\end{bmatrix}.
$$

Por eso $b_2$ aporta una dirección nueva. Con ambos vectores podemos construir cualquier vector de $\mathbb{R}^2$:

$$
\begin{bmatrix}x\\y\end{bmatrix}
=
x\begin{bmatrix}1\\0\end{bmatrix}
+
y\begin{bmatrix}0\\1\end{bmatrix}.
$$

Por tanto,

$$
B=\left(
\begin{bmatrix}1\\0\end{bmatrix},
\begin{bmatrix}0\\1\end{bmatrix}
\right)
$$

es una base de $\mathbb{R}^2$.

### Regla visual en $\mathbb{R}^2$

Con dos vectores:

- Si están sobre la misma recta, uno es redundante y no generan todo el plano.
- Si apuntan en direcciones diferentes, generan todo el plano y forman una base.

Por ejemplo:

$$
b_1=\begin{bmatrix}1\\2\end{bmatrix},
\qquad
b_2=\begin{bmatrix}2\\4\end{bmatrix}
$$

no forman una base porque $b_2=2b_1$.

En cambio,

$$
b_1=\begin{bmatrix}1\\2\end{bmatrix},
\qquad
b_2=\begin{bmatrix}2\\1\end{bmatrix}
$$

sí forman una base porque ninguno es múltiplo del otro.

En resumen:

> Un vector aporta una dirección nueva cuando no se puede obtener combinando los vectores anteriores. Cuando tienes suficientes direcciones nuevas para cubrir todo el espacio, tienes una base.
[Timestamp: 2026/08/25 20:24:14]

**user**: entonces que es span no entendi
[Timestamp: 2026/08/25 20:26:18]

**ai**: El **span** de unos vectores es simplemente el conjunto de **todos los vectores que puedes construir combinándolos**.

En español también se llama **espacio generado**.

### Ejemplo con un vector

Tomemos:

$$
v=\begin{bmatrix}1\\2\end{bmatrix}.
$$

Podemos multiplicarlo por cualquier número:

$$
2v=\begin{bmatrix}2\\4\end{bmatrix},
\qquad
-v=\begin{bmatrix}-1\\-2\end{bmatrix},
\qquad
0v=\begin{bmatrix}0\\0\end{bmatrix}.
$$

Por tanto:

$$
\operatorname{span}(v)
=
\left\{
c\begin{bmatrix}1\\2\end{bmatrix}:c\in\mathbb{R}
\right\}.
$$

Este span es una **recta** que pasa por el origen. Solo podemos avanzar o retroceder en la dirección de $v$.

### Ejemplo con dos vectores

Ahora tomemos:

$$
v_1=\begin{bmatrix}1\\0\end{bmatrix},
\qquad
v_2=\begin{bmatrix}0\\1\end{bmatrix}.
$$

Su span contiene todos los vectores de la forma:

$$
c_1v_1+c_2v_2.
$$

Es decir:

$$
c_1\begin{bmatrix}1\\0\end{bmatrix}
+
c_2\begin{bmatrix}0\\1\end{bmatrix}
=
\begin{bmatrix}c_1\\c_2\end{bmatrix}.
$$

Como $c_1$ y $c_2$ pueden ser cualquier número, podemos construir cualquier vector del plano:

$$
\operatorname{span}(v_1,v_2)=\mathbb{R}^2.
$$

### ¿Qué pasa si uno es redundante?

Consideremos:

$$
v_1=\begin{bmatrix}1\\2\end{bmatrix},
\qquad
v_2=\begin{bmatrix}2\\4\end{bmatrix}.
$$

Como $v_2=2v_1$, los dos apuntan sobre la misma recta. Sus combinaciones son:

$$
c_1v_1+c_2v_2
=
c_1v_1+2c_2v_1
=
(c_1+2c_2)v_1.
$$

Por mucho que cambiemos $c_1$ y $c_2$, seguimos moviéndonos sobre la misma recta:

$$
\operatorname{span}(v_1,v_2)
=
\operatorname{span}(v_1).
$$

Por eso $v_2$ es redundante: agregarlo no agranda el span.

En pocas palabras:

> **Span = todos los lugares a los que puedes llegar combinando los vectores disponibles.**

- Un vector no nulo suele generar una recta.
- Dos direcciones independientes en $\mathbb{R}^2$ generan el plano.
- Tres direcciones independientes en $\mathbb{R}^3$ generan todo el espacio.
- Un vector redundante no cambia el span.
[Timestamp: 2026/08/25 20:26:18]

**user**: y la base que es
[Timestamp: 2026/08/25 20:26:52]

**ai**: Una **base** es un conjunto de vectores que cumple dos condiciones:

- Su **span cubre todo el espacio**.
- No contiene vectores redundantes.

En palabras sencillas:

> Una base es el conjunto mínimo de direcciones necesarias para construir cualquier vector del espacio.

### Ejemplo en $\mathbb{R}^2$

Consideremos:

$$
b_1=\begin{bmatrix}1\\0\end{bmatrix},
\qquad
b_2=\begin{bmatrix}0\\1\end{bmatrix}.
$$

Estos dos vectores forman una base porque cualquier vector del plano puede escribirse como:

$$
\begin{bmatrix}x\\y\end{bmatrix}
=
x\begin{bmatrix}1\\0\end{bmatrix}
+
y\begin{bmatrix}0\\1\end{bmatrix}.
$$

Por ejemplo:

$$
\begin{bmatrix}3\\2\end{bmatrix}
=
3b_1+2b_2.
$$

Además, ninguno de los dos vectores puede construirse usando solamente el otro. No son redundantes.

### Un conjunto que no es base

Consideremos:

$$
v_1=\begin{bmatrix}1\\0\end{bmatrix},
\qquad
v_2=\begin{bmatrix}2\\0\end{bmatrix}.
$$

Como

$$
v_2=2v_1,
$$

ambos apuntan en la misma dirección. Su span es solamente el eje horizontal, no todo $\mathbb{R}^2$:

$$
\operatorname{span}(v_1,v_2)
=
\left\{
\begin{bmatrix}x\\0\end{bmatrix}:x\in\mathbb{R}
\right\}.
$$

Por eso no forman una base de $\mathbb{R}^2$.

### ¿Qué relación hay entre span y base?

El **span** es el espacio que puedes construir.

La **base** son las direcciones mínimas e independientes que necesitas para construirlo.

Por ejemplo:

$$
v_1=\begin{bmatrix}1\\0\end{bmatrix},
\quad
v_2=\begin{bmatrix}0\\1\end{bmatrix},
\quad
v_3=\begin{bmatrix}1\\1\end{bmatrix}.
$$

Los tres generan $\mathbb{R}^2$, pero no son una base porque:

$$
v_3=v_1+v_2.
$$

$v_3$ es redundante. Si lo eliminamos, queda la base:

$$
B=(v_1,v_2).
$$

La idea esencial es:

$$
\boxed{\text{Base}=\text{genera todo el espacio}+\text{sin redundancia}}
$$
[Timestamp: 2026/08/25 20:26:52]