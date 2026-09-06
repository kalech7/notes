---
title: Lenguajes formales, autómatas y memoria de redes secuenciales
aliases:
  - Autómatas y redes neuronales
  - DFA, PDA y memoria secuencial
tags:
  - master/matematicas-programacion
  - lenguajes-formales
  - automatas
  - rnn
  - transformer
fuente: https://alisawuffles.notion.site/alisa-s-book-of-llms
---

# Lenguajes formales, autómatas y memoria de redes secuenciales

> [!abstract] Objetivo
> Entender qué memoria exige una regla secuencial, cómo un DFA reconoce lenguajes regulares, por qué un PDA puede reconocer estructura anidada y qué significa realmente comparar esas máquinas con RNN y Transformers.

> [!summary] La idea en una frase
> Un autómata convierte cada prefijo en la información mínima necesaria para continuar: un DFA dispone de un número finito de estados; un PDA añade una pila; una red secuencial aprende o implementa alguna representación numérica de esa memoria.

> [!info] Alcance y prerrequisitos
> La recurrencia, las compuertas LSTM, la atención, el KV cache y sus costes ya se explican en [[10 RNN, LSTM, SSM y Transformer - comparación]]. Aquí no se repiten: se usan para responder una pregunta distinta, **qué clase de cálculo secuencial puede representar, aprender y generalizar cada arquitectura**.
>
> Para la activación usada en la construcción consulta [[../redes neuronales desde cero/01 Neurona, MLP, activaciones y formas#Activaciones|ReLU]]. Para separar ajuste del conjunto de entrenamiento y generalización consulta [[../machine learning clasico y generalizacion/03 Generalización, sesgo-varianza y regularización|Generalización, sesgo-varianza y regularización]].

## La clase en cuatro preguntas

| Pregunta | Respuesta breve |
|---|---|
| **¿Qué es?** | Un lenguaje formal es un conjunto de cadenas definido con exactitud; un autómata es un procedimiento que decide si una cadena pertenece a él. |
| **¿Cómo funciona?** | Lee símbolos y actualiza una memoria: un estado finito en el DFA o un estado finito más una pila en el PDA. |
| **¿Para qué sirve?** | Para especificar sintaxis, construir analizadores y aislar qué memoria o algoritmo aprende un modelo secuencial. |
| **¿Por qué importa para LLM?** | Permite separar afirmaciones sobre capacidad teórica, aprendizaje, generalización y limitaciones numéricas que suelen confundirse. |

## 1. De cadenas a lenguajes

Un **alfabeto** $\Sigma$ es un conjunto finito de símbolos. Si

$$
\Sigma=\{0,1\},
$$

entonces $0$, $101$ y $00110$ son cadenas. El conjunto de todas las cadenas finitas, incluida la cadena vacía $\varepsilon$, se denota $\Sigma^*$.

Un **lenguaje formal** es cualquier subconjunto:

$$
L\subseteq\Sigma^*.
$$

Por ejemplo,

$$
L_{\mathrm{par}}
=
\{w\in\{0,1\}^*: w\text{ contiene un número par de unos}\}.
$$

Un **reconocedor** recibe una cadena completa y responde si pertenece a $L$:

$$
\mathbf 1_L(w)=
\begin{cases}
1,&w\in L,\\
0,&w\notin L.
\end{cases}
$$

> [!important] Reconocer no es modelar probabilidades
> Un reconocedor define pertenencia binaria. Un modelo de lenguaje define una distribución, por ejemplo $p(x_t\mid x_{<t})$ o $p(w)$. Se puede convertir una salida probabilística en una decisión mediante un umbral, pero los teoremas sobre reconocedores y los teoremas sobre distribuciones no son intercambiables. [Svete y Cotterell (EMNLP 2023)](https://aclanthology.org/2023.emnlp-main.502/) estudian explícitamente esta diferencia para RNN-LM y autómatas finitos probabilísticos.

### Por qué usar lenguajes artificiales

En una tarea natural, un error puede deberse a vocabulario, conocimiento, ambigüedad, datos o razonamiento. En un lenguaje formal se conoce exactamente la regla. Esto permite:

- controlar la longitud y la profundidad estructural;
- crear positivos y negativos con dificultad conocida;
- demostrar qué memoria es suficiente o necesaria;
- inspeccionar si el estado interno sigue una variable interpretable;
- evaluar longitudes mayores que las vistas durante entrenamiento.

No son una escala general de inteligencia ni prueban por sí solos cómo procesa un modelo el lenguaje natural. Son un **microscopio experimental** para una capacidad concreta.

> [!warning] Todo problema acotado puede parecer regular
> Todo lenguaje finito es regular: basta construir un árbol de prefijos con un estado por prefijo relevante y un estado sumidero. Por ello, acertar todas las cadenas hasta longitud $N$ no demuestra haber aprendido una regla para longitudes arbitrarias; también es compatible con memorizar el dominio acotado.

## 2. DFA: memoria finita y lenguajes regulares

Un **autómata finito determinista** o DFA se define como

$$
\mathcal A=(Q,\Sigma,\delta,q_0,F),
$$

donde:

- $Q=\{q_1,\ldots,q_K\}$ es un conjunto finito de estados;
- $\Sigma$ es el alfabeto;
- $\delta:Q\times\Sigma\to Q$ es la función de transición;
- $q_0\in Q$ es el estado inicial;
- $F\subseteq Q$ contiene los estados de aceptación.

Al leer $w=a_1\cdots a_n$, la máquina ejecuta

$$
q_t=\delta(q_{t-1},a_t),\qquad t=1,\ldots,n,
$$

y acepta si $q_n\in F$. Para la cadena vacía, decide usando directamente $q_0$.

La palabra **determinista** significa que cada par $(q,a)$ tiene un único destino. La máquina no necesita conservar el prefijo completo: conserva solo su **clase de futuro relevante**. Dos prefijos pueden compartir estado cuando toda continuación posible produce la misma decisión desde ambos.

### Ejemplo: paridad

Para reconocer cadenas con un número par de unos bastan dos estados:

- $E$: se han visto una cantidad par de unos;
- $O$: se han visto una cantidad impar.

$E$ es inicial y aceptante.

| Estado actual | leer `0` | leer `1` |
|---|---|---|
| $E$ | $E$ | $O$ |
| $O$ | $O$ | $E$ |

La cadena `1010` produce

$$
E\xrightarrow{1}O
\xrightarrow{0}O
\xrightarrow{1}E
\xrightarrow{0}E,
$$

por lo que se acepta. En cambio, `1011` termina en $O$ y se rechaza.

> [!tip] Qué memoriza el estado
> El DFA no recuerda en qué posiciones aparecieron los unos ni cuántos hubo exactamente. Solo conserva el bit de información que afecta al futuro: par o impar.

Los DFA reconocen exactamente los **lenguajes regulares**. Las expresiones regulares, los autómatas finitos no deterministas y los DFA describen la misma clase, aunque el tamaño de sus representaciones pueda ser muy diferente.

> [!info] Apunte visual existente
> Si quieres repasar la representación gráfica antes de continuar, abre [[maquina de estados finitos.excalidraw|máquina de estados finitos]].

## 3. PDA: estado finito más una pila

Un **autómata con pila** o PDA amplía el control finito con una pila cuyo contenido pertenece a $\Gamma^*$, donde $\Gamma$ es un alfabeto de pila finito. Una transición puede depender de:

- el estado de control;
- el siguiente símbolo de entrada, o $\varepsilon$;
- el símbolo situado en la cima de la pila.

Puede retirar la cima, conservarla o reemplazarla por una cadena de símbolos. En forma no determinista, la transición tiene el tipo

$$
\delta:
Q\times(\Sigma\cup\{\varepsilon\})\times\Gamma
\longrightarrow
\mathcal P(Q\times\Gamma^*).
$$

La pila puede crecer con la entrada, pero solo se accede por su cima: es memoria **LIFO**, no memoria de acceso aleatorio.

> [!important] Determinista frente a no determinista
> Los PDA no deterministas reconocen exactamente los lenguajes libres de contexto. Los PDA deterministas reconocen una subclase propia. La equivalencia habitual entre PDA y gramáticas libres de contexto se refiere al caso no determinista.

### Ejemplo: la misma cantidad de `a` y `b`

Considera

$$
L_{ab}=\{a^n b^n:n\ge 0\}.
$$

Un PDA puede:

1. apilar un símbolo $A$ por cada `a`;
2. al ver la primera `b`, pasar a una fase en la que ya no admite más `a`;
3. desapilar un $A$ por cada `b`;
4. aceptar solo si entrada y pila terminan a la vez.

Para `aabb`, usando $Z$ como marcador de fondo:

| Entrada leída | Acción | Pila después de la acción |
|---|---|---|
| inicio | colocar marcador | $Z$ |
| `a` | push $A$ | $AZ$ |
| `a` | push $A$ | $AAZ$ |
| `b` | pop $A$ | $AZ$ |
| `b` | pop $A$ | $Z$ |

No existe un DFA para $L_{ab}$. Los prefijos

$$
\varepsilon,a,a^2,a^3,\ldots
$$

son distinguibles entre sí: la continuación $b^n$ acepta después de $a^n$, pero no después de $a^m$ cuando $m\ne n$. Un DFA necesitaría infinitos estados para conservar todas esas posibilidades.

### Contador no es lo mismo que pila

Dyck-1, el lenguaje de paréntesis de un solo tipo correctamente balanceados, puede reconocerse manteniendo la profundidad:

- `(` incrementa un contador;
- `)` lo decrementa;
- se rechaza si un prefijo intenta bajar de cero;
- se acepta si el contador termina en cero.

Con varios tipos, la profundidad no basta. Para distinguir `([])` de `([)]` se debe recordar el orden de los tipos abiertos; esa información es una pila.

> [!note] Profundidad acotada
> Si la pila tiene profundidad máxima fija $m$, sus configuraciones posibles son finitas. Puede compilarse a un DFA con, como máximo, una cantidad proporcional a
> $$
> |Q|\sum_{d=0}^{m}|\Gamma|^d
> $$
> configuraciones. El lenguaje acotado se vuelve regular, aunque la representación explote con $m$. [Hewitt et al. (EMNLP 2020)](https://aclanthology.org/2020.emnlp-main.156/) construyen RNN eficientes para una familia de lenguajes jerárquicos con profundidad acotada.

> [!info] Apunte visual existente
> Para la intuición mecánica de push, pop y cima, abre [[Push down machine .excalidraw|Push down machine]].

## 4. De un DFA a una red recurrente

La semejanza conceptual es directa:

| DFA | Red recurrente |
|---|---|
| estado $q_{t-1}$ | estado oculto $h_{t-1}$ |
| símbolo $a_t$ | vector de entrada $x_t$ |
| transición $\delta$ | celda recurrente |
| misma tabla en cada paso | pesos compartidos en el tiempo |
| estado final en $F$ | lectura o clasificador final |

Esto motiva codificar cada estado mediante un vector one-hot

$$
s_t=e_{q_t}\in\{0,1\}^{K}
$$

y cada símbolo mediante

$$
x_t=e_{a_t}\in\{0,1\}^{M},
$$

con $K=|Q|$ y $M=|\Sigma|$.

El problema es implementar una tabla arbitraria

$$
(q_i,\sigma_k)\longmapsto \delta(q_i,\sigma_k)
$$

sin perder la relación entre cada estado y su símbolo.

## 5. Por qué falla la construcción aditiva directa

La fuente propone una actualización de ancho $K$:

$$
s_t=\operatorname{ReLU}(W_hs_{t-1}+W_xx_t+b),
$$

y, para cada transición $\delta(q_i,\sigma_k)=q_j$, asigna

$$
(W_h)_{ji}=1,\qquad
(W_x)_{jk}=1,\qquad
b_j=-1.
$$

La intención es que la unidad $j$ compruebe simultáneamente el estado $q_i$ y el símbolo $\sigma_k$. Sin embargo, cuando varias transiciones llegan a $q_j$, la fila $j$ conserva dos conjuntos separados:

- qué estados aparecen en alguna transición hacia $q_j$;
- qué símbolos aparecen en alguna transición hacia $q_j$.

No conserva **qué estado estaba emparejado con qué símbolo**.

### Cruces falsos en el DFA de paridad

Para llegar a $E$, los pares correctos son

$$
(E,0),\qquad(O,1),
$$

mientras que los pares cruzados

$$
(E,1),\qquad(O,0)
$$

deben llegar a $O$.

Una fila aditiva para el destino $E$ tiene la forma

$$
z_E(q,a)=u_q+v_a+b_E.
$$

Pero siempre se cumple

$$
z_E(E,0)+z_E(O,1)
=
z_E(E,1)+z_E(O,0),
$$

porque ambos lados son

$$
u_E+u_O+v_0+v_1+2b_E.
$$

Si los dos pares correctos tuvieran preactivación positiva, su suma sería positiva. Si ambos cruces tuvieran preactivación no positiva, su suma sería no positiva. La igualdad anterior hace imposibles ambas condiciones simultáneas.

En la receta concreta, la fila de $E$ recibe un $1$ para ambos estados y para ambos símbolos. Por tanto,

$$
z_E(q,a)=1+1-1=1
$$

para los cuatro pares: aparecen exactamente los cruces falsos que se querían evitar.

> [!danger] Alcance de la corrección
> Esto no demuestra que una ReLU-RNN sea incapaz de reconocer paridad. Demuestra que **la construcción propuesta, con una unidad indicadora por estado destino y una suma separable estado+símbolo, no implementa un DFA arbitrario**. Puede funcionar para tablas especiales cuyas entradas hacia cada destino tengan estructura separable, pero no constituye una prueba general.

## 6. Construcción correcta: una gate por par estado–símbolo

La solución general conserva el emparejamiento creando una unidad intermedia por cada elemento de $Q\times\Sigma$.

Para el par $(q_i,\sigma_k)$, define

$$
g_{i,k}^{(t)}
=
2\operatorname{ReLU}
\left(
s_{t-1,i}+x_{t,k}-\frac32
\right).
$$

Como las dos entradas son binarias, la gate implementa un AND:

| $s_{t-1,i}$ | $x_{t,k}$ | preactivación | $g_{i,k}^{(t)}$ |
|---:|---:|---:|---:|
| 0 | 0 | $-3/2$ | 0 |
| 0 | 1 | $-1/2$ | 0 |
| 1 | 0 | $-1/2$ | 0 |
| 1 | 1 | $1/2$ | 1 |

La intuición de una compuerta aprendida sobre los cuatro casos se desarrolla en [[../gradientes autodiferenciacion y optimizacion/07 Mini-batch y SGD como estimador#Caso AND: un lote, cuatro ramas y una sola actualización|Caso AND: un lote, cuatro ramas y una sola actualización]]. Aquí la función lógica es la misma, pero los pesos se fijan constructivamente: no hacen falta pérdida, `backward()` ni optimización para demostrar la expresividad.

Como $s_{t-1}$ y $x_t$ son one-hot, exactamente una de las $KM$ gates vale $1$: la correspondiente al par real $(q_{t-1},a_t)$.

### Proyección al estado siguiente

Define una matriz de enrutamiento

$$
T\in\{0,1\}^{K\times KM}
$$

mediante

$$
T_{j,(i,k)}
=
\mathbf 1[\delta(q_i,\sigma_k)=q_j].
$$

El estado siguiente es

$$
s_t=Tg_t,
$$

o, coordenada por coordenada,

$$
s_{t,j}
=
\sum_{\substack{i,k:\\
\delta(q_i,\sigma_k)=q_j}}
g_{i,k}^{(t)}.
$$

Aunque muchas columnas de $T$ pueden apuntar al mismo destino, solo una gate está activa en cada paso. Por eso $s_t$ vuelve a ser one-hot.

En forma matricial completa:

$$
g_t
=
2\operatorname{ReLU}
\left(
As_{t-1}+Bx_t-\frac32\mathbf 1_{KM}
\right),
$$

$$
s_t=Tg_t,
$$

donde la fila $(i,k)$ de $A\in\{0,1\}^{KM\times K}$ selecciona $s_{t-1,i}$ y la misma fila de $B\in\{0,1\}^{KM\times M}$ selecciona $x_{t,k}$.

### Demostración por inducción

**Caso base.** Se inicializa

$$
s_0=e_{q_0},
$$

que representa correctamente el estado inicial.

**Paso inductivo.** Supón que $s_{t-1}=e_{q_i}$ y que el símbolo actual es $x_t=e_{\sigma_k}$. Entonces:

1. $g_{i,k}^{(t)}=1$ porque sus dos entradas seleccionadas valen $1$;
2. cualquier otra gate recibe al menos un cero y vale $0$;
3. la columna $(i,k)$ de $T$ contiene un único $1$, en la fila correspondiente a $\delta(q_i,\sigma_k)$;
4. en consecuencia,

$$
s_t=e_{\delta(q_i,\sigma_k)}.
$$

Por inducción, la red representa exactamente el estado del DFA después de cada prefijo, para cualquier longitud.

La lectura final puede ser

$$
y(w)=\sum_{q_j\in F}s_{n,j}\in\{0,1\}.
$$

No se necesita una sigmoide para la construcción exacta: $y=1$ significa aceptar y $y=0$ rechazar.

### Coste y arquitectura que realmente se demostraron

La celda anterior posee:

- $K$ coordenadas para el estado del DFA;
- $KM$ gates internas para las parejas;
- una proyección lineal de gates a estados.

Por tanto, es una celda recurrente de dos etapas con ancho interno $KM$, no una capa Elman de ancho $K$.

Si se exige estrictamente una sola transformación afín seguida de ReLU por paso, las gates pueden ser el propio estado recurrente. Sea $r_t[i,k]$ la indicadora de que en el paso $t$ se procesó $\sigma_k$ desde $q_i$. Entonces la entrada recurrente que indica que el estado actual es $q_i$ es

$$
\sum_{\substack{p,\ell:\\
\delta(q_p,\sigma_\ell)=q_i}}
r_{t-1}[p,\ell].
$$

Cada coordenada se actualiza mediante

$$
r_t[i,k]
=
2\operatorname{ReLU}
\left(
\sum_{\substack{p,\ell:\\
\delta(q_p,\sigma_\ell)=q_i}}
r_{t-1}[p,\ell]
+x_{t,k}
-\frac32
\right).
$$

Una coordenada adicional activa solo en $t=0$ suministra $q_0$ al primer paso. El factor exterior $2$ puede incorporarse a los pesos y al sesgo porque ReLU es positivamente homogénea. Esta variante es una ReLU-RNN estándar de ancho $KM+1$.

> [!important] Qué prueba y qué no prueba
> La construcción prueba que existe una ReLU-RNN finita que simula cualquier DFA. No afirma que $KM$ sea el ancho mínimo, que descenso por gradiente encuentre esos pesos ni que una red entrenada adopte estados one-hot.

## 7. Qué memoria puede tener una RNN

Una RNN reutiliza la misma transición en cada posición. Este es un sesgo inductivo apropiado para ejecutar algoritmos de izquierda a derecha, pero la palabra **memoria** necesita supuestos precisos.

### Estado fijo y precisión fija

Si cada una de $d$ coordenadas solo puede tomar uno de $R$ valores de máquina, existen como máximo $R^d$ configuraciones internas. Con actualización determinista, el sistema completo puede verse como un DFA enorme.

La construcción anterior evita acumular cantidades: usa valores $0$, $1/2$, $1$ y $3/2$, todos exactamente representables en aritmética binaria habitual, y devuelve $0/1$ en cada paso. Por ello no necesita precisión creciente para simular memoria regular.

### Contadores

Una unidad ReLU o una celda LSTM puede, bajo pesos adecuados, incrementar o decrementar una magnitud y comportarse como contador. [Weiss, Goldberg y Yahav (ACL 2018)](https://aclanthology.org/P18-2117/) estudian este comportamiento bajo restricciones prácticas de precisión, y [Suzgun et al. (ACL 2019)](https://aclanthology.org/W19-3905/) muestran experimentalmente que LSTM pequeñas pueden aprender conteo dinámico en Dyck-1.

Esto no crea automáticamente una pila general:

- un contador conserva una cantidad;
- varios contadores conservan varias cantidades;
- una pila conserva una secuencia ordenada de símbolos y permite recuperar el último.

En hardware real, además, todo contador termina limitado por rango, redondeo o longitud de contexto. Las afirmaciones de completitud de Turing basadas en números reales de precisión infinita no describen literalmente una implementación float32. Consulta también [[09 Escalado, GPU, precisión y cuantización#Formatos numéricos|formatos numéricos]].

## 8. Relación con Transformers

Un Transformer no comprime necesariamente todo el prefijo en un único vector recurrente. Durante el prefill mantiene una representación por posición y usa atención para combinar información. En generación causal conserva claves y valores anteriores en el KV cache y produce tokens secuencialmente.

| Propiedad | RNN | Transformer causal estándar |
|---|---|---|
| actualización sobre la entrada | un paso recurrente por símbolo | capas paralelas sobre las posiciones conocidas |
| resumen del pasado | estado de dimensión fija | representaciones por posición y KV cache |
| ruta entre posiciones lejanas | atraviesa muchas transiciones | una capa puede conectar posiciones permitidas |
| decode | secuencial | también secuencial entre tokens generados |
| memoria práctica | limitada por estado y precisión | limitada por ventana de contexto, cache y precisión |
| simulación de autómata | encaje natural paso a paso | posible mediante construcciones dependientes de arquitectura y supuestos |

[Bhattamishra, Ahuja y Goyal (EMNLP 2020)](https://aclanthology.org/2020.emnlp-main.576/) construyen Transformers para una subclase de lenguajes con contadores y observan empíricamente diferencias entre Transformers y LSTM incluso en lenguajes regulares.

No existe un único resultado llamado "el poder del Transformer". Cambiar atención, codificación posicional, profundidad, uniformidad, precisión o longitud permitida cambia el modelo matemático:

- [Hao, Angluin y Frank (TACL 2022)](https://aclanthology.org/2022.tacl-1.46/) muestran límites distintos para atención hard única y atención hard promediada;
- [Chiang y Cholak (ACL 2022)](https://aclanthology.org/2022.acl-long.527/) construyen Transformers que superan una limitación previa y reconocen paridad bajo una configuración apropiada;
- permitir pasos intermedios o chain-of-thought proporciona cómputo secuencial adicional y ya no es el mismo problema que clasificar en un forward de profundidad fija.

> [!warning] Evita conclusiones absolutas
> "Los Transformers no pueden reconocer paridad" y "los Transformers pueden reconocer cualquier patrón secuencial" omiten los supuestos que hacen verdadera o falsa cada afirmación. Siempre pregunta: **qué variante, con qué precisión, qué profundidad y para qué longitudes**.

## 9. Cuatro preguntas diferentes

Las discusiones sobre redes y autómatas se vuelven confusas cuando mezclan estos ejes:

| Eje | Pregunta | Evidencia adecuada |
|---|---|---|
| **expresividad** | ¿Existen pesos que implementen la regla para todas las entradas permitidas? | construcción o prueba de imposibilidad |
| **learnability** | ¿Un algoritmo de entrenamiento puede encontrar una solución a partir de datos finitos? | experimentos con semillas, regímenes de datos y optimizadores |
| **generalización** | ¿La solución aprendida funciona fuera de las longitudes o estructuras vistas? | evaluación fuera de distribución, especialmente por longitud y profundidad |
| **precisión finita** | ¿La representación sobrevive a redondeo, rango limitado y perturbaciones? | análisis numérico y pruebas con dtypes o ruido |

La construcción con gates prueba

$$
\exists\theta\ \forall w\in\Sigma^*:
f_\theta(w)=\mathbf 1_L(w)
$$

para todo lenguaje regular $L$. No prueba que, dado un conjunto finito $D$, el entrenamiento produzca esos $\theta$.

En forma compacta:

$$
\text{existencia de pesos}
\not\Rightarrow
\text{aprendizaje}
\not\Rightarrow
\text{generalización por longitud}.
$$

> [!example] Misma exactitud, algoritmos distintos
> Dos modelos pueden obtener 100 % hasta longitud 20. Uno aprendió la paridad y funciona hasta 10 000; otro aprendió correlaciones de posiciones frecuentes y cae al azar desde longitud 30. La exactitud dentro del rango de entrenamiento no distingue ambos mecanismos.

## 10. Cómo diseñar un experimento serio

Para investigar si una red aprende un lenguaje formal:

1. **Define la tarea.** Indica alfabeto, lenguaje, criterio de aceptación y si se clasifica la cadena completa o cada prefijo.
2. **Separa longitudes.** Por ejemplo, entrena con $n\le 40$, valida en el mismo rango y prueba por bandas $41$--$80$, $81$--$160$ y $161$--$320$.
3. **Construye negativos difíciles.** No basta ruido aleatorio; usa cadenas a una edición de una positiva, prefijos casi válidos y violaciones tardías.
4. **Controla la distribución.** Equilibra clases y evita que longitud, último símbolo u otra pista superficial prediga la etiqueta.
5. **Reporta por longitud y profundidad.** Una media global oculta dónde se rompe el algoritmo.
6. **Inspecciona el mecanismo.** Para paridad, intenta decodificar $E/O$ de cada estado; para Dyck-1, compara una coordenada con profundidad; para Dyck-2, comprueba si conserva tipos anidados.
7. **Prueba perturbaciones.** Cambia semilla, dtype, escala de pesos y pequeñas cantidades de ruido.
8. **Compara con el autómata correcto.** El baseline simbólico establece la respuesta exacta y permite localizar el primer prefijo divergente.

[Suzgun, Belinkov y Shieber (SCiL 2019)](https://aclanthology.org/W19-0128/) muestran por qué las conclusiones empíricas sobre lenguajes formales dependen fuertemente del régimen de datos y del protocolo de evaluación.

## 11. Errores frecuentes

- **"Acertó el test, así que aprendió el autómata".** Puede haber explotado una pista del conjunto o memorizado el rango.
- **"Todo lenguaje context-free necesita una pila compleja".** Algunos, como Dyck-1, admiten mecanismos más restringidos; la clase indica lo que existe en general.
- **"Un PDA tiene memoria ilimitada de acceso aleatorio".** Su acceso está restringido a la cima.
- **"Una LSTM que cuenta aprendió una pila".** Contar profundidad no conserva el orden de varios tipos.
- **"Toda RNN de precisión finita es simplemente un DFA".** Hay que especificar si el rango está acotado y si la precisión o el número de bits puede crecer con la longitud.
- **"Turing-complete significa ilimitada en un computador real".** Muchas demostraciones dependen de precisión idealizada o tiempo no acotado.
- **"La receta aditiva de la fuente demuestra ancho $K$".** Pierde el emparejamiento estado–símbolo y crea cruces falsos.
- **"Un resultado para hard attention vale para cualquier Transformer".** El mecanismo de atención y el modelo de precisión son parte del teorema.
- **"Reconocer y asignar probabilidades son el mismo problema".** Un lenguaje no especifica cómo repartir masa entre sus cadenas.
- **"El lenguaje natural es exactamente context-free".** Las gramáticas context-free son modelos útiles de estructura, no una caracterización completa de toda sintaxis, semántica y contexto discursivo.

## 12. Autoevaluación

> [!question]- 1. ¿Qué información conserva el DFA de paridad?
> Solo si la cantidad de unos vista hasta el momento es par o impar. No necesita conocer la cantidad exacta ni las posiciones porque toda continuación futura afecta a ambos prefijos del mismo modo cuando comparten paridad.

> [!question]- 2. ¿Por qué $\{a^n b^n:n\ge0\}$ no es regular?
> Porque los prefijos $a^0,a^1,a^2,\ldots$ son todos distinguibles: para $n\ne m$, la continuación $b^n$ hace que $a^nb^n$ pertenezca al lenguaje, pero $a^mb^n$ no. Un DFA finito no puede asignar un estado diferente a infinitos prefijos distinguibles.

> [!question]- 3. ¿Por qué Dyck-1 no demuestra que una red aprendió una pila general?
> Con un solo tipo de paréntesis basta conservar profundidad, rechazar cuando se vuelve negativa y comprobar cero al final. Eso puede hacerse con un contador. Una pila general se vuelve necesaria cuando también debe recuperarse el orden de tipos anidados, como en Dyck-2.

> [!question]- 4. ¿Qué información pierde $W_hs+W_xx$ en la construcción defectuosa?
> Cada fila registra contribuciones del estado y del símbolo por separado. Si $(q_1,a)$ y $(q_2,b)$ conducen al mismo destino, la suma también puede activar los cruces $(q_1,b)$ y $(q_2,a)$ porque no existe una unidad que represente la pareja.

> [!question]- 5. Comprueba la gate $2\operatorname{ReLU}(s_i+x_k-3/2)$.
> Si ambas entradas valen $1$, la preactivación es $1/2$ y la salida es $1$. Si falta cualquiera de ellas, la preactivación es como máximo $-1/2$ y ReLU devuelve $0$. Por eso actúa como AND sobre entradas binarias.

> [!question]- 6. ¿Por qué solo una gate por pareja queda activa?
> El estado $s_{t-1}$ tiene exactamente una coordenada igual a $1$ y la entrada $x_t$ también. Solo la gate que selecciona simultáneamente esas dos coordenadas recibe dos unos; todas las demás reciben al menos un cero.

> [!question]- 7. ¿Qué demuestra la construcción y qué queda abierto?
> Demuestra expresividad: existen pesos de una red ReLU finita que simulan cualquier DFA en cualquier longitud. No demuestra que el ancho sea mínimo, que SGD encuentre esos pesos, que una solución aprendida sea robusta ni que generalice fuera de las longitudes de entrenamiento.

> [!question]- 8. ¿Cómo distinguirías memorización de generalización algorítmica?
> Reservaría bandas de longitud y profundidad mucho mayores que las vistas, usaría negativos difíciles sin pistas superficiales, reportaría resultados por longitud, buscaría el primer prefijo de divergencia e inspeccionaría si el estado interno sigue la variable del autómata.

> [!question]- 9. ¿Por qué dos artículos pueden atribuir poderes distintos a "los Transformers" sin contradecirse?
> Pueden analizar modelos diferentes: hard o soft attention, promediado o selección única, distintas codificaciones posicionales, profundidad fija o creciente, precisión ideal o finita y uso o no de pasos intermedios. El resultado pertenece al conjunto completo de supuestos.

> [!question]- 10. ¿Por qué un contexto práctico finito cambia la discusión?
> Para una longitud máxima fija solo existen finitas cadenas y el problema puede memorizarse con suficiente capacidad. Las diferencias entre clases de lenguajes son asintóticas; en la práctica interesa además la eficiencia, robustez y extrapolación antes de llegar al límite de contexto.

## 13. Resumen de dominio

- Un lenguaje es un conjunto de cadenas; reconocerlo es decidir pertenencia.
- Un DFA conserva una de finitas situaciones futuras y reconoce exactamente los lenguajes regulares.
- Un PDA añade una pila LIFO; en versión no determinista caracteriza los lenguajes context-free.
- Una profundidad de pila fija puede compilarse a memoria finita.
- Una ReLU-RNN puede simular cualquier DFA, pero la construcción general debe conservar cada pareja estado–símbolo.
- La suma separable propuesta en la fuente crea cruces falsos y no prueba una simulación general de ancho $K$.
- Contador, pila, estado recurrente y KV cache son formas de memoria diferentes.
- Expresividad, learnability, generalización y precisión finita requieren evidencias distintas.
- Todo resultado teórico sobre Transformers debe leerse junto con sus supuestos arquitectónicos y numéricos.

## Referencias primarias en ACL Anthology

- [On the Practical Computational Power of Finite Precision RNNs for Language Recognition](https://aclanthology.org/P18-2117/) — Weiss, Goldberg y Yahav, ACL 2018. Precisión finita y mecanismos de conteo en variantes recurrentes.
- [Sequential Neural Networks as Automata](https://aclanthology.org/W19-3901/) — Merrill, 2019. Marco para estudiar redes secuenciales mediante autómatas y memoria.
- [On Evaluating the Generalization of LSTM Models in Formal Languages](https://aclanthology.org/W19-0128/) — Suzgun, Belinkov y Shieber, SCiL 2019. Efecto del régimen de datos sobre las conclusiones de generalización.
- [LSTM Networks Can Perform Dynamic Counting](https://aclanthology.org/W19-3905/) — Suzgun et al., ACL 2019. Conteo dinámico, Dyck-1 y dificultad de mecanismos de pila.
- [RNNs can generate bounded hierarchical languages with optimal memory](https://aclanthology.org/2020.emnlp-main.156/) — Hewitt et al., EMNLP 2020. Construcción de memoria eficiente para jerarquía con profundidad acotada.
- [On the Ability and Limitations of Transformers to Recognize Formal Languages](https://aclanthology.org/2020.emnlp-main.576/) — Bhattamishra, Ahuja y Goyal, EMNLP 2020. Construcciones y evaluación de Transformers en lenguajes regulares y con contadores.
- [Formal Language Recognition by Hard Attention Transformers: Perspectives from Circuit Complexity](https://aclanthology.org/2022.tacl-1.46/) — Hao, Angluin y Frank, TACL 2022. Diferencias entre variantes formales de hard attention.
- [Overcoming a Theoretical Limitation of Self-Attention](https://aclanthology.org/2022.acl-long.527/) — Chiang y Cholak, ACL 2022. Construcciones para paridad y dependencia de los supuestos del modelo.
- [Recurrent Neural Language Models as Probabilistic Finite-state Automata](https://aclanthology.org/2023.emnlp-main.502/) — Svete y Cotterell, EMNLP 2023. Relación entre RNN-LM y distribuciones finito-estatales.

## Fuente base

- [Alisa’s book of LLMs](https://alisawuffles.notion.site/alisa-s-book-of-llms), sección *Theoretical CS*. La construcción aditiva se analizó y corrigió arriba; la nota no la reproduce como resultado válido.

---

Anterior: [[21 Muestreo diferenciable - Gumbel-Max, Gumbel-Softmax y straight-through]] · Volver al [[00 Índice - Modelos de lenguaje y transformers]]
