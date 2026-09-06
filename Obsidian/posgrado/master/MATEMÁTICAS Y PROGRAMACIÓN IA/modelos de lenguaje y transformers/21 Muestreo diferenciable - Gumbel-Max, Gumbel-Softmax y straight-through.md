---
title: Muestreo diferenciable - Gumbel-Max, Gumbel-Softmax y straight-through
aliases:
  - Gumbel-Softmax
  - Concrete distribution
  - Straight-through Gumbel-Softmax
tags:
  - master/matematicas-programacion
  - llm
  - muestreo-diferenciable
  - gumbel-softmax
related:
  - "[[01 Del texto a probabilidades - embeddings, logits, softmax y entropía]]"
  - "[[05 Entrenamiento de un LLM - objetivo, parámetros, FLOPs y memoria]]"
  - "[[07 Muestreo, temperatura, top-k, top-p y decodificación especulativa]]"
  - "[[11 Post-entrenamiento - SFT, RLHF, PPO, GRPO y DPO]]"
---

# Muestreo diferenciable: Gumbel-Max, Gumbel-Softmax y straight-through

> [!abstract] Objetivo
> Entender cómo obtener una decisión categórica exacta con **Gumbel-Max**, por qué esa decisión bloquea el gradiente, cómo **Gumbel-Softmax** la reemplaza por una relajación diferenciable y qué compromiso introduce el estimador **straight-through**.

> [!summary] Idea central
> **Gumbel-Max** produce una muestra discreta exacta, pero <code>argmax</code> no ofrece un gradiente útil.<br>
> **Gumbel-Softmax** cambia el vértice discreto por un punto suave del simplex.<br>
> **Straight-through** usa la decisión dura en el forward y una ruta suave sustituta en el backward.

> [!info] Alcance: enlazar en vez de repetir
> Los logits, softmax y entropía cruzada ya están en [[01 Del texto a probabilidades - embeddings, logits, softmax y entropía#Softmax|Softmax y CE]].<br>
> La temperatura, top-k y top-p de generación están en [[07 Muestreo, temperatura, top-k, top-p y decodificación especulativa#Temperatura|Muestreo en inferencia]].<br>
> Teacher forcing se desarrolla en [[05 Entrenamiento de un LLM - objetivo, parámetros, FLOPs y memoria#Datos y objetivo|Entrenamiento de un LLM]].<br>
> REINFORCE y los baselines están en [[11 Post-entrenamiento - SFT, RLHF, PPO, GRPO y DPO#REINFORCE o policy gradient|Policy gradient]].

## Qué problema queremos resolver

Supongamos que una red produce $K$ logits:

$$
\theta=(\theta_1,\ldots,\theta_K)\in\mathbb R^K
$$

y define probabilidades categóricas:

$$
\pi_i=\frac{e^{\theta_i}}{\sum_{j=1}^{K}e^{\theta_j}}.
$$

Queremos elegir una categoría:

$$
k\sim\operatorname{Categorical}(\pi),
\qquad
z=e_k,
$$

donde $e_k$ es un vector one-hot.

Esto es fácil en el forward. El problema aparece si $z$ controla una operación posterior y queremos que su pérdida actualice los logits $\theta$ mediante backpropagation.

Para un ruido fijo, una selección discreta es localmente constante: pequeños cambios en $\theta$ normalmente no cambian la categoría ganadora. Su derivada es cero casi en todas partes y la función salta en las fronteras donde cambia el ganador.

> [!important] La distribución sí cambia, aunque <code>argmax</code> no tenga un gradiente útil
> Cambiar $\theta$ mueve las fronteras entre categorías y modifica sus probabilidades. El problema no es que el objetivo probabilístico sea independiente de $\theta$, sino que la derivada ordinaria de una realización discreta no captura ese cambio.

## Qué es una variable Gumbel

Una variable Gumbel estándar tiene función de distribución acumulada:

$$
F_G(g)=\exp\left(-e^{-g}\right).
$$

Puede generarse por transformación inversa. Si

$$
U\sim\operatorname{Uniforme}(0,1),
$$

entonces:

$$
G=-\log(-\log U)\sim\operatorname{Gumbel}(0,1).
$$

Para una variable categórica se genera un $G_i$ **independiente por categoría y por elemento del lote**.

## Gumbel-Max: una muestra categórica exacta

El truco Gumbel-Max define:

$$
k=\arg\max_i(\theta_i+G_i),
\qquad
G_i\overset{\mathrm{iid}}{\sim}\operatorname{Gumbel}(0,1).
$$

Entonces:

$$
P(k=i)=\frac{e^{\theta_i}}{\sum_j e^{\theta_j}}=\pi_i.
$$

No es una aproximación: el índice ganador es una muestra exacta de la distribución categórica inducida por los logits.

Si se parte de probabilidades, se usa:

$$
k=\arg\max_i(\log\pi_i+G_i).
$$

No se debe usar $\pi_i+G_i$.

## Derivación mediante una carrera exponencial

La equivalencia se entiende imaginando relojes que compiten.

### 1. Cada categoría tiene un reloj

Sea:

$$
T_i\sim\operatorname{Exp}(\lambda_i),
\qquad \lambda_i>0,
$$

con relojes independientes. Gana la categoría cuyo reloj suena primero:

$$
I=\arg\min_i T_i.
$$

La densidad del reloj $i$ es:

$$
f_i(t)=\lambda_i e^{-\lambda_i t},
$$

y la probabilidad de que cada otro reloj siga sin sonar en $t$ es:

$$
P(T_j>t)=e^{-\lambda_jt}.
$$

Por tanto:

$$
\begin{aligned}
P(I=i)
&=\int_0^\infty
f_i(t)\prod_{j\ne i}P(T_j>t)\,dt\\
&=\int_0^\infty
\lambda_i e^{-\lambda_it}
\prod_{j\ne i}e^{-\lambda_jt}\,dt\\
&=\int_0^\infty
\lambda_i e^{-t\sum_j\lambda_j}\,dt\\
&=\frac{\lambda_i}{\sum_j\lambda_j}.
\end{aligned}
$$

El reloj con mayor tasa tiene más probabilidad de llegar primero, pero no gana siempre.

### 2. Transformar los tiempos exponenciales

Si $U_i\sim\operatorname{Uniforme}(0,1)$, entonces:

$$
X_i=-\log U_i\sim\operatorname{Exp}(1).
$$

Un reloj de tasa $\lambda_i$ puede escribirse como:

$$
T_i=\frac{X_i}{\lambda_i}
=\frac{-\log U_i}{\lambda_i}.
$$

Aplicamos $-\log$, una función estrictamente decreciente:

$$
\begin{aligned}
-\log T_i
&=-\log\left(\frac{-\log U_i}{\lambda_i}\right)\\
&=\log\lambda_i-\log(-\log U_i)\\
&=\log\lambda_i+G_i.
\end{aligned}
$$

Como $-\log$ invierte el orden:

$$
\arg\min_i T_i
=
\arg\max_i(-\log T_i)
=
\arg\max_i(\log\lambda_i+G_i).
$$

### 3. Recuperar softmax

Elegimos tasas no normalizadas:

$$
\lambda_i=e^{\theta_i}.
$$

La carrera exponencial da:

$$
P(I=i)
=
\frac{e^{\theta_i}}{\sum_j e^{\theta_j}}
=\operatorname{softmax}(\theta)_i.
$$

Así queda derivado Gumbel-Max:

$$
\boxed{
k=\arg\max_i(\theta_i+G_i)
\sim\operatorname{Categorical}(\operatorname{softmax}\theta)
}
$$

> [!tip] Por qué no hace falta calcular el normalizador
> Usar $\theta_i$ o $\log\pi_i=\theta_i-\log\sum_j e^{\theta_j}$ produce el mismo <code>argmax</code>, porque el segundo término es una constante común a todas las categorías.

## Ejemplo numérico completo

Partimos de:

$$
\pi=(0.2,0.3,0.5),
\qquad
\theta=\log\pi.
$$

Tomemos una realización uniforme:

$$
U=(0.5,0.9,0.2).
$$

| $i$ | $\pi_i$ | $\theta_i=\log\pi_i$ | $G_i=-\log(-\log U_i)$ | $\theta_i+G_i$ | $T_i=-\log U_i/\pi_i$ |
|---:|---:|---:|---:|---:|---:|
| 1 | $0.2$ | $-1.609$ | $0.367$ | $-1.243$ | $3.466$ |
| 2 | $0.3$ | $-1.204$ | $2.250$ | **$1.046$** | **$0.351$** |
| 3 | $0.5$ | $-0.693$ | $-0.476$ | $-1.169$ | $3.219$ |

La categoría 2:

- maximiza $\theta_i+G_i$;
- minimiza $T_i$;
- es la muestra obtenida en esta realización.

La categoría 3 era la más probable, pero una muestra categórica no tiene que elegir siempre el modo. Al repetir el experimento muchas veces, las frecuencias se aproximan a $(0.2,0.3,0.5)$.

## Por qué Gumbel-Max todavía no es diferenciable

El resultado duro es:

$$
z_{\mathrm{hard}}
=
\operatorname{one\_hot}
\left(
\arg\max_i(\theta_i+G_i)
\right).
$$

Para un $G$ fijo, pequeños cambios de $\theta$ dejan normalmente intacto el índice ganador. Por eso <code>argmax</code> rompe la ruta de gradiente.

Gumbel-Max resuelve **cómo muestrear exactamente**, pero no **cómo propagar un gradiente pathwise a través de la muestra**.

## Gumbel-Softmax: relajar la decisión

Se reemplaza el <code>argmax</code> por softmax:

$$
y_i^{(\tau)}
=
\frac{
\exp((\theta_i+G_i)/\tau)
}{
\sum_j\exp((\theta_j+G_j)/\tau)
},
\qquad \tau>0.
$$

El vector resultante satisface:

$$
y_i^{(\tau)}>0,
\qquad
\sum_i y_i^{(\tau)}=1.
$$

No es one-hot: es un punto continuo dentro del simplex. Condicionado al ruido $G$, sí es diferenciable respecto de los logits:

$$
\frac{\partial y_i}{\partial\theta_j}
=
\frac1{\tau}y_i(\mathbf 1[i=j]-y_j).
$$

Esto permite aplicar la regla de la cadena a una pérdida diferenciable que recibe $y^{(\tau)}$.

## Qué hace la temperatura de relajación

| Régimen | Resultado en el forward | Comportamiento del gradiente |
|---|---|---|
| $\tau$ grande | distribución suave, cercana a $(1/K,\ldots,1/K)$ | suele ser más estable, pero se aleja de una decisión discreta |
| $\tau$ intermedia | conserva preferencias sin ser casi one-hot | compromiso práctico |
| $\tau$ pequeña | se acerca al vértice ganador | muchos gradientes se saturan; cerca de empates pueden aparecer picos |
| $\tau\to0^+$ | converge a la muestra one-hot de Gumbel-Max | el límite deja de ser una relajación suave |
| $\tau=0$ | división inválida | no debe usarse |

En el ejemplo anterior:

| $\tau$ | $y^{(\tau)}$ |
|---:|---|
| $2.0$ | $(0.193,\ 0.607,\ 0.200)$ |
| $1.0$ | $(0.084,\ 0.826,\ 0.090)$ |
| $0.5$ | $(0.010,\ 0.978,\ 0.012)$ |

Al reducir $\tau$, la misma realización se aproxima al one-hot $(0,1,0)$.

> [!warning] Temperatura baja no garantiza un mejor estimador
> Lejos de un empate, softmax se satura y el gradiente puede quedar casi en cero. Cerca de un empate, el factor $1/\tau$ puede producir gradientes grandes. Por eso bajar $\tau$ puede aumentar la inestabilidad o la varianza de Monte Carlo, aunque el forward parezca más discreto.

### Dos temperaturas que no deben confundirse

La temperatura de generación de [[07 Muestreo, temperatura, top-k, top-p y decodificación especulativa#Temperatura|decodificación]] cambia la distribución objetivo:

$$
\pi^{(T)}=\operatorname{softmax}(\theta/T).
$$

Una muestra exacta de esa distribución es:

$$
k=\arg\max_i(\theta_i/T+G_i).
$$

La temperatura de relajación $\tau$ suaviza una realización:

$$
y=\operatorname{softmax}
\left(
\frac{\theta/T+G}{\tau}
\right).
$$

Si solo se calcula:

$$
\operatorname{softmax}
\left(
\frac{\theta+G}{\tau}
\right),
$$

el <code>argmax</code> duro no cambia al variar $\tau$, porque dividir todos los puntajes por el mismo número positivo conserva su orden.

## Sesgo y varianza: qué objetivo se está derivando

Definamos el objetivo discreto real:

$$
J_{\mathrm{hard}}(\theta)
=
\mathbb E_{z\sim\operatorname{Cat}(\pi_\theta)}
[L(z)].
$$

Con Gumbel-Softmax se optimiza un objetivo relajado:

$$
J_\tau(\theta)
=
\mathbb E_G[\widetilde L(y^{(\tau)})].
$$

El gradiente pathwise:

$$
\nabla_\theta J_\tau
=
\mathbb E_G
\left[
\frac{\partial\widetilde L}{\partial y}
\frac{\partial y^{(\tau)}}{\partial\theta}
\right]
$$

es, bajo las condiciones usuales, un estimador de Monte Carlo insesgado para el **objetivo relajado** $J_\tau$.

Sin embargo, para $\tau>0$:

$$
J_\tau\ne J_{\mathrm{hard}}
$$

en general. Por eso el mismo gradiente es sesgado si lo interpretamos como estimador de $\nabla J_{\mathrm{hard}}$.

> [!important] La frase precisa
> Gumbel-Softmax suele dar un gradiente pathwise de menor varianza, pero es un gradiente del problema relajado. “Menor varianza” no significa “gradiente exacto del problema discreto”.

Reducir $\tau$ suele disminuir la diferencia visual entre $y^{(\tau)}$ y un one-hot, pero no garantiza una mejora monótona de la optimización. Conviene validar el sistema con decisiones duras y tratar el annealing como un hiperparámetro experimental.

## Straight-through Gumbel-Softmax

A veces el forward necesita una decisión realmente dura: elegir una ruta, un código, una operación o un embedding. El estimador straight-through combina dos objetos:

> [!note] Straight-through es una familia de estimadores
> El **identity STE** sustituye localmente la derivada de una operación dura por la identidad. **ST Gumbel-Softmax**, en cambio, usa durante el backward el Jacobiano de $y_{\mathrm{soft}}$. Comparten la idea de un backward sustituto, pero no son exactamente el mismo estimador.

$$
y_{\mathrm{soft}}
=
\operatorname{softmax}
\left(
\frac{\theta+G}{\tau}
\right),
$$

$$
y_{\mathrm{hard}}
=
\operatorname{one\_hot}
\left(
\arg\max_i y_{\mathrm{soft},i}
\right).
$$

Se construye:

$$
\boxed{
y_{\mathrm{ST}}
=
y_{\mathrm{hard}}
-
\operatorname{stopgrad}(y_{\mathrm{soft}})
+
y_{\mathrm{soft}}
}
$$

### Qué ocurre en el forward

<code>stopgrad(y_soft)</code> tiene los mismos valores numéricos que $y_{\mathrm{soft}}$:

$$
y_{\mathrm{ST}}
=
y_{\mathrm{hard}}-y_{\mathrm{soft}}+y_{\mathrm{soft}}
=
y_{\mathrm{hard}}.
$$

El consumidor recibe un one-hot verdadero.

### Qué ocurre en el backward

<code>stopgrad</code> —<code>detach()</code> en PyTorch— tiene derivada cero. La ruta dura tampoco aporta un gradiente útil. Por tanto:

$$
\frac{\partial y_{\mathrm{ST}}}{\partial\theta}
=
\frac{\partial y_{\mathrm{soft}}}{\partial\theta}.
$$

El backward actúa como si se hubiese usado la relajación suave.

> [!warning] Straight-through es un estimador sesgado
> El forward evalúa la pérdida en $y_{\mathrm{hard}}$, pero el backward usa el Jacobiano de $y_{\mathrm{soft}}$. Esa derivada no es el gradiente verdadero del grafo discreto y, en general, tampoco coincide con el gradiente de la pérdida puramente suave.

En forma compacta, el gradiente utilizado es:

$$
\nabla_\theta^{\mathrm{ST}}L
=
\left.
\frac{\partial L}{\partial y}
\right|_{y=y_{\mathrm{hard}}}
\frac{\partial y_{\mathrm{soft}}}{\partial\theta}.
$$

Es una decisión pragmática: conservar semántica dura hacia adelante y aceptar una derivada sustituta hacia atrás.

## Implementación manual en PyTorch

~~~python
import torch


def sample_gumbel_like(work_logits):
    eps = torch.finfo(work_logits.dtype).eps
    u = torch.rand_like(work_logits).clamp(eps, 1.0 - eps)
    return -torch.log(-torch.log(u))


def gumbel_softmax(logits, tau=1.0, hard=False):
    if tau <= 0:
        raise ValueError("tau debe ser mayor que cero")
    if not logits.is_floating_point():
        raise TypeError("logits debe tener dtype de punto flotante")

    input_dtype = logits.dtype

    # log(-log(U)) y softmax son sensibles en baja precisión.
    # Si la red usa FP16/BF16, esta parte se calcula en FP32.
    if input_dtype in (torch.float16, torch.bfloat16):
        work_logits = logits.float()
    else:
        work_logits = logits

    g = sample_gumbel_like(work_logits)
    y_soft = torch.softmax((work_logits + g) / tau, dim=-1)

    if hard:
        winner = y_soft.argmax(dim=-1, keepdim=True)
        y_hard = torch.zeros_like(y_soft).scatter_(-1, winner, 1.0)

        # Forward: y_hard. Backward: gradiente de y_soft.
        result = y_hard - y_soft.detach() + y_soft
    else:
        result = y_soft

    # Facilita combinar el resultado con capas en el dtype del modelo.
    # El backward de softmax sigue habiéndose construido en FP32.
    return result.to(input_dtype)
~~~

> [!important] Por qué se usa FP32 internamente
> En FP16/BF16, números uniformes muy cercanos a cero y las dos operaciones logarítmicas pueden perder precisión; softmax también es sensible a rangos grandes de logits. Convertir temporalmente los logits a FP32 hace que el ruido Gumbel y softmax se calculen con mayor estabilidad. El cast final permite continuar con capas de baja precisión y sigue siendo una operación diferenciable.

> [!important] Usar el mismo ruido en ambas ramas
> $y_{\mathrm{hard}}$ debe obtenerse de la misma realización que produjo $y_{\mathrm{soft}}$. Volver a muestrear Gumbel para la rama dura crearía un forward y un backward referidos a decisiones diferentes.

Si se quiere que el gradiente alcance al selector de un embedding, puede usarse:

~~~python
selected_embedding = y_st @ embedding_matrix
~~~

El forward elige exactamente una fila porque $y_{\mathrm{ST}}$ es one-hot en valores. En cambio, convertir el ganador en un entero y hacer solo:

~~~python
selected_embedding = embedding_matrix[token_id]
~~~

elimina la ruta diferenciable desde el resultado hasta los logits del selector.

## Contraste con REINFORCE

Para el objetivo discreto:

$$
J(\theta)=
\mathbb E_{z\sim p_\theta}[L(z)],
$$

el estimador score-function o REINFORCE usa:

$$
\nabla_\theta J
=
\mathbb E
\left[
(L(z)-b)\nabla_\theta\log p_\theta(z)
\right],
$$

donde un baseline $b$ independiente de la acción muestreada puede reducir varianza sin introducir sesgo.

Para una categórica:

$$
\frac{\partial\log\pi_z}{\partial\theta_i}
=
\mathbf 1[z=i]-\pi_i.
$$

REINFORCE no necesita derivar $L$ respecto de la decisión. Puede usarse aunque la pérdida provenga de una métrica, un simulador o una recompensa no diferenciable. Su desventaja habitual es la alta varianza y un problema más difícil de asignación de crédito.

| Método | Forward | Gradiente respecto del objetivo discreto | Requiere downstream diferenciable | Compromiso |
|---|---|---|---|---|
| marginalización exacta | evalúa todas las categorías | exacto | sí, si hay parámetros posteriores | coste proporcional a $K$ |
| Gumbel-Max solo | muestra hard exacta | ninguno a través de <code>argmax</code> | — | sirve para muestrear, no para backprop pathwise |
| REINFORCE | muestra hard exacta | insesgado en Monte Carlo | no | varianza alta |
| Gumbel-Softmax | mezcla soft | sesgado para el objetivo hard; pathwise para $J_\tau$ | sí | menor varianza típica, forward relajado |
| ST Gumbel-Softmax | hard | sesgado, gradiente sustituto | sí | forward correcto, backward aproximado |

> [!tip] Antes de estimar, intenta marginalizar
> Si $K$ es pequeño y pueden calcularse todas las ramas, evaluar
>
> $$
> J=\sum_i\pi_iL(e_i)
> $$
>
> suele ser preferible a introducir ruido. Elimina el error de Monte Carlo y evita el sesgo de la relajación.

## Por qué la CE teacher-forced no necesita muestrear

En entrenamiento teacher-forced el token objetivo $t$ viene del dataset. La pérdida por posición es:

$$
L_{\mathrm{CE}}
=
-\log\pi_t
=
-\theta_t+\log\sum_j e^{\theta_j}.
$$

Su gradiente respecto de cada logit es:

$$
\frac{\partial L_{\mathrm{CE}}}{\partial\theta_i}
=
\pi_i-\mathbf 1[i=t].
$$

Todo es diferenciable. El target es discreto, pero es un **dato constante**, no una decisión producida por los parámetros.

Con $\pi=(0.2,0.3,0.5)$ y target $t=3$:

$$
L_{\mathrm{CE}}=-\log0.5\approx0.693,
$$

$$
\nabla_\theta L_{\mathrm{CE}}
=
(0.2,\ 0.3,\ -0.5).
$$

No hace falta Gumbel, <code>argmax</code> ni muestreo multinomial.

> [!important] Entrenamiento e inferencia responden preguntas distintas
> En teacher forcing preguntamos: “¿qué probabilidad asignó el modelo al token correcto?”.<br>
> En inferencia preguntamos: “¿qué token emitiremos?”.<br>
> Solo la segunda pregunta necesita una regla de selección, y durante inferencia normalmente no se requiere backpropagation.

El problema de muestreo diferenciable sí aparece cuando una elección del modelo se reutiliza dentro del mismo grafo de entrenamiento, por ejemplo:

- una variable latente categórica sin etiqueta;
- un router o compuerta que elige una rama;
- selección de código en una representación discreta;
- búsqueda diferenciable de operaciones;
- un token generado que condiciona cálculos posteriores;
- una recompensa de secuencia que depende de muestras del modelo.

Para recompensas de secuencia en LLM, REINFORCE o métodos de policy gradient preservan la semántica discreta. Una mezcla suave de embeddings puede ser útil como aproximación, pero no representa necesariamente una secuencia lingüística válida.

## Cómo elegir el método

| Situación | Primera opción |
|---|---|
| hay un target conocido y se usa CE | no muestrear |
| hay pocas categorías y pueden evaluarse todas | marginalizar exactamente |
| downstream admite mezclas continuas | Gumbel-Softmax |
| forward debe ser hard y se acepta sesgo | ST Gumbel-Softmax |
| la recompensa o el entorno no es diferenciable | REINFORCE o policy gradient |
| solo se genera en inferencia | muestreo categórico ordinario |

## Protocolo práctico

1. Escribir primero el objetivo discreto que realmente interesa.
2. Comprobar si se puede marginalizar.
3. Decidir si una mezcla soft tiene significado para el downstream.
4. Separar temperatura de generación $T$ y relajación $\tau$.
5. Medir métricas hard, aunque el entrenamiento sea soft.
6. Vigilar entropía, norma de gradiente y frecuencia de categorías.
7. Comparar varias semillas: todos estos estimadores contienen ruido Monte Carlo.
8. Aplicar annealing solo si mejora la validación, no por costumbre.

## Errores frecuentes

- sumar ruido Gumbel a probabilidades en vez de a logits o log-probabilidades;
- reutilizar el mismo escalar Gumbel para todas las categorías: ese ruido común se cancela en el <code>argmax</code>;
- olvidar independencia entre categorías o ejemplos del lote;
- creer que Gumbel-Max vuelve diferenciable a <code>argmax</code>;
- usar $\tau=0$;
- confundir temperatura de generación con temperatura de relajación;
- afirmar que bajar $\tau$ siempre reduce el sesgo y la varianza;
- describir Gumbel-Softmax como una muestra categórica exacta cuando $\tau>0$;
- describir straight-through como un gradiente insesgado;
- aplicar <code>detach()</code> a toda la expresión y cortar también la rama suave;
- volver a muestrear ruido entre $y_{\mathrm{soft}}$ y $y_{\mathrm{hard}}$;
- convertir demasiado pronto la selección en un índice entero;
- calcular ruido Gumbel y softmax directamente en FP16/BF16 sin considerar su estabilidad;
- usar muestreo durante CE teacher-forced aunque el target ya sea conocido;
- validar únicamente con mezclas soft y desplegar después decisiones hard sin medir la brecha.

## Autoevaluación

> [!question]- 1. ¿Por qué el primer reloj de una carrera exponencial elige la categoría $i$ con probabilidad $\lambda_i/\sum_j\lambda_j$?
> La densidad de que el reloj $i$ suene en $t$ es $\lambda_i e^{-\lambda_it}$ y la probabilidad de que todos los demás sigan activos es $\prod_{j\ne i}e^{-\lambda_jt}$. Al integrar su producto:
>
> $$
> \int_0^\infty\lambda_i e^{-t\sum_j\lambda_j}dt
> =
> \frac{\lambda_i}{\sum_j\lambda_j}.
> $$

> [!question]- 2. ¿Cómo se convierte una carrera exponencial en Gumbel-Max?
> Se escribe $T_i=-\log U_i/\lambda_i$ y se aplica $-\log$:
>
> $$
> -\log T_i
> =
> \log\lambda_i-\log(-\log U_i)
> =
> \log\lambda_i+G_i.
> $$
>
> Como $-\log$ es decreciente, minimizar $T_i$ equivale a maximizar $\log\lambda_i+G_i$.

> [!question]- 3. En el ejemplo numérico, ¿por qué gana la categoría 2 si la categoría 3 tenía mayor probabilidad?
> Porque una muestra no es el modo. El ruido de esa realización dio a la categoría 2 el mayor puntaje perturbado. Al repetir muchas veces, la categoría 3 ganará con frecuencia aproximada $0.5$, no con frecuencia $1$.

> [!question]- 4. ¿Cambiar $\tau$ en $\operatorname{softmax}((\theta+G)/\tau)$ cambia la categoría hard?
> No, mientras $\tau>0$. Dividir todos los puntajes por el mismo número positivo no cambia su orden. $\tau$ cambia la suavidad de $y$, no el <code>argmax</code> de esa realización.

> [!question]- 5. ¿Por qué Gumbel-Softmax es sesgado respecto del objetivo discreto?
> Porque calcula el gradiente de
>
> $$
> J_\tau=\mathbb E[\widetilde L(y^{(\tau)})],
> $$
>
> mientras el objetivo original es
>
> $$
> J_{\mathrm{hard}}=\mathbb E[L(z)].
> $$
>
> Para temperatura finita, las entradas soft y hard no son en general equivalentes.

> [!question]- 6. ¿Qué hace exactamente <code>y_hard - y_soft.detach() + y_soft</code>?
> En valores, los dos términos soft se cancelan y el forward recibe <code>y_hard</code>. En derivadas, <code>detach()</code> aporta cero y queda el gradiente de <code>y_soft</code>.

> [!question]- 7. ¿Cuál es la diferencia esencial entre straight-through y REINFORCE?
> Straight-through usa un gradiente sustituto diferenciando una relajación; suele tener menor varianza, pero es sesgado y necesita un downstream diferenciable. REINFORCE usa $(L-b)\nabla\log p$; puede manejar recompensas no diferenciables y es insesgado para el objetivo discreto, pero normalmente tiene mayor varianza.

> [!question]- 8. ¿Por qué una etiqueta one-hot no obliga a usar straight-through en CE?
> Porque la etiqueta es un dato fijo. La pérdida deriva las probabilidades producidas por el modelo respecto de sus logits; no necesita derivar la etiqueta ni una selección <code>argmax</code>.

> [!question]- 9. Si existen ocho categorías y es barato ejecutar las ocho ramas, ¿qué conviene probar antes de Gumbel-Softmax?
> Marginalización exacta: calcular la contribución de cada categoría y ponderarla por su probabilidad. Elimina el ruido Monte Carlo y evita el sesgo de la relajación.

> [!question]- 10. ¿Por qué una temperatura muy pequeña puede producir gradientes problemáticos?
> La derivada contiene $1/\tau$, pero softmax suele estar saturado. La mayoría de muestras puede aportar gradientes casi nulos, mientras que realizaciones cercanas a un empate generan contribuciones grandes. El resultado puede ser esporádico e inestable.

> [!question]- 11. ¿Por qué conviene calcular el ruido y softmax en FP32 cuando los logits están en FP16/BF16?
> Porque $-\log(-\log U)$ amplifica problemas cerca de los extremos del intervalo y softmax es sensible al rango de los logits. FP32 reduce redondeos, ceros accidentales y saturación numérica; el resultado puede volver después al dtype del modelo sin cortar autograd.

## Referencias primarias y fuente de la clase

- Fuente guía del módulo: [Alisa’s book of LLMs](https://alisawuffles.notion.site/alisa-s-book-of-llms).
- Emil J. Gumbel (1954), [*Statistical Theory of Extreme Values and Some Practical Applications*](https://nvlpubs.nist.gov/nistpubs/Legacy/AMS/nbsams33.pdf).
- Chris J. Maddison (2016), [*A Poisson process model for Monte Carlo*](https://arxiv.org/abs/1602.05986). Fuente para carreras exponenciales y su relación con procesos Gumbel.
- Chris J. Maddison, Andriy Mnih y Yee Whye Teh (2016/2017), [*The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables*](https://arxiv.org/abs/1611.00712).
- Eric Jang, Shixiang Gu y Ben Poole (2016/2017), [*Categorical Reparameterization with Gumbel-Softmax*](https://arxiv.org/abs/1611.01144).
- Yoshua Bengio, Nicholas Léonard y Aaron Courville (2013), [*Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation*](https://arxiv.org/abs/1308.3432). Fuente primaria del estimador straight-through.
- Ronald J. Williams (1992), [*Simple Statistical Gradient-Following Algorithms for Connectionist Reinforcement Learning*](https://doi.org/10.1007/BF00992696). Fuente primaria de REINFORCE.

---

Anterior: [[20 Laboratorio aplicado - elegir prompting, RAG o fine-tuning]] · Siguiente: [[22 Lenguajes formales, autómatas y memoria de redes secuenciales]] · Volver al [[00 Índice - Modelos de lenguaje y transformers|índice]]
