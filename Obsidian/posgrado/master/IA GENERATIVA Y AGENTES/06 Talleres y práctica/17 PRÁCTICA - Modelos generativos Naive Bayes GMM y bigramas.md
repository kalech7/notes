---
title: "Modelos generativos — Naive Bayes, GMM y bigramas"
tags:
  - maestria/ia-generativa
  - estudio
  - practica
aliases:
  - Modelos generativos del notebook s1 lun estudiante
---

# Modelos generativos — Naive Bayes, GMM y bigramas

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

Esta nota completa mis apuntes con el dataset y los ejercicios de [[s1-lun-estudiante.ipynb|S1·LUN — El puente generativo]]. Primero clasifico y genero palabras con Naive Bayes, después genero puntos con GMM y finalmente genero texto conservando una palabra de contexto.

Las explicaciones, cálculos y preguntas amplían el notebook. El código se puede ejecutar por bloques, en orden, en un notebook con `numpy`, `scikit-learn` y `matplotlib`.

## Resumen general

| Modelo | Factorización | Idea principal | Cómo genera |
| --- | --- | --- | --- |
| Naive Bayes | $P(X,Y)=P(Y)\prod_i P(x_i\mid Y)$ | Las características se consideran independientes dada la clase | Elegir clase y muestrear palabras según esa clase |
| GMM | $p(x)=\sum_{k=1}^{K}\pi_k\mathcal N(x\mid\mu_k,\Sigma_k)$ | Cada punto puede proceder de uno de varios componentes gaussianos ocultos | Elegir componente y muestrear un punto de su gaussiana |
| Bigramas | $P(x_{1:T})=P(x_1)\prod_{t=2}^{T}P(x_t\mid x_{t-1})$ | El siguiente token depende únicamente del anterior | Muestrear una continuación, actualizar el contexto y repetir |

En Naive Bayes, la primera fórmula expresa el supuesto general. Para el modelo multinomial de conteos veremos la forma concreta más abajo. En GMM, $p(x)$ es una **densidad**, no la probabilidad de un punto exacto. En bigramas hace falta una distribución inicial; si proporciono la primera palabra, genero condicionado a ella.

## 1. Naive Bayes

### ¿Qué aprendí?

Naive Bayes permite clasificar datos utilizando probabilidades. En este ejemplo las clases son `spam` y `ham` —mensajes normales—. Aprende qué palabras son frecuentes en cada clase:

- `gratis`, `premio`, `dinero`: frecuentes en spam.
- `proyecto`, `profesor`, `reunion`: presentes en ham.

Además de clasificar, puedo usar la distribución aprendida para generar palabras. **Clasificar** pregunta qué clase explica un mensaje; **generar** fija una clase y produce un mensaje posible bajo el modelo.

Teoría: [[07 S01 - Naive Bayes con un ejemplo de spam]].

### Dataset y preparación

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

rng = np.random.default_rng(42)

spam = [
    "gana dinero gratis ahora haz clic aqui",
    "oferta exclusiva gratis compra ahora descuento increible",
    "haz clic gana premio dinero facil ahora",
    "descuento increible oferta gratis compra ya",
    "premio gratis haz clic ahora dinero",
]

ham = [
    "la reunion del proyecto es el martes a las diez",
    "adjunto el informe de avance del modelo",
    "podemos revisar el codigo del pipeline manana",
    "el profesor subio las notas del taller al aula virtual",
    "confirmo asistencia a la defensa del proyecto",
]

corpus = spam + ham
etiquetas = ["spam"] * len(spam) + ["ham"] * len(ham)

vec = CountVectorizer()
X = vec.fit_transform(corpus)
nb = MultinomialNB(alpha=1.0)
nb.fit(X, etiquetas)

vocab = np.array(vec.get_feature_names_out())
print("Forma de X:", X.shape)
print("Clases:", nb.classes_)
print("Vocabulario:", len(vocab))
print(nb.predict(vec.transform(["gana premio gratis"]))[0])
```

Con este corpus, `X` tiene forma **(10, 44)**: diez mensajes y 44 palabras diferentes. Cada fila representa un mensaje; cada columna, una palabra; cada valor, su número de apariciones. La predicción del mensaje de prueba es `spam`.

`fit_transform` aprende el vocabulario y transforma los mensajes de entrenamiento. Para mensajes nuevos uso `transform`, con las mismas columnas. Ajustar otro vocabulario para predecir rompería esa correspondencia.

> [!note] No todas las palabras del texto llegan a la matriz
> En esta configuración, `CountVectorizer()` convierte a minúsculas y omite tokens de un solo carácter, como `a`. No elimina automáticamente palabras frecuentes como `el` o `del`. Tampoco equipara por defecto `reunion` con `reunión`.

### De los conteos a las probabilidades

Los cinco mensajes spam tienen 33 tokens reconocidos; los cinco ham tienen 39. **Número de mensajes** y **número de tokens** son cantidades distintas.

La probabilidad inicial de cada clase se estima con mensajes:

$$P(\text{spam})=P(\text{ham})=\frac{5}{10}=0.5.$$

La distribución de palabras se estima con apariciones de tokens. Con suavizado de Laplace:

$$P(w\mid y)=\frac{N_{w,y}+\alpha}{N_y+\alpha V},\qquad \alpha=1,\quad V=44.$$

- $N_{w,y}$: apariciones de la palabra $w$ en la clase $y$.
- $N_y$: total de tokens reconocidos de esa clase.
- $V$: tamaño del vocabulario compartido por ambas clases.
- $\alpha$: cantidad añadida a **cada** conteo.

`gratis` aparece cuatro veces en spam y ninguna en ham:

$$P(\text{gratis}\mid\text{spam})=\frac{4+1}{33+44}=\frac{5}{77}\approx0.0649.$$

$$P(\text{gratis}\mid\text{ham})=\frac{0+1}{39+44}=\frac{1}{83}\approx0.0120.$$

El suavizado evita que una palabra del vocabulario tenga probabilidad cero en una clase. No añade automáticamente palabras que estén fuera del vocabulario: el vectorizador ignora esas palabras nuevas.

### Factorización y clasificación

Para una secuencia de $L$ palabras independientes dada la clase, con longitud fijada:

$$P(w_1,\ldots,w_L\mid y,L)=\prod_{j=1}^{L}P(w_j\mid y).$$

Para una bolsa de palabras, $c_v$ es el número de veces que aparece la palabra $v$. La distribución multinomial es:

$$P(c\mid y,L)=\frac{L!}{\prod_{v=1}^{V}c_v!}\prod_{v=1}^{V}P(w_v\mid y)^{c_v},\qquad L=\sum_v c_v.$$

Los conteos no son independientes entre sí cuando su suma está fijada. La intuición del modelo es que cada extracción de palabra es independiente dada la clase. El coeficiente multinomial es igual para todas las clases al evaluar un mismo mensaje, así que se cancela al aplicar Bayes.

Para clasificar basta comparar:

$$\operatorname{score}(y)=\log P(y)+\sum_{v=1}^{V}c_v\log P(w_v\mid y).$$

Sumar logaritmos evita multiplicar muchos números pequeños. La clase con mayor puntaje gana; el puntaje todavía no es una probabilidad posterior normalizada.

En `gana premio gratis`, los conteos spam de esas palabras son 2, 2 y 4. Los conteos ham son cero:

$$s_{\text{spam}}=0.5\frac{3}{77}\frac{3}{77}\frac{5}{77},\qquad s_{\text{ham}}=0.5\left(\frac{1}{83}\right)^3.$$

Normalizando, $P(\text{spam}\mid\text{mensaje})=s_{\text{spam}}/(s_{\text{spam}}+s_{\text{ham}})\approx0.9826$. Es una probabilidad del modelo entrenado con diez mensajes, no una medición de su rendimiento en correos reales.

### Generar mensajes desde la distribución aprendida

```python
def muestrear_mensaje(clase, n_palabras, rng):
    idx_clase = list(nb.classes_).index(clase)
    probs = np.exp(nb.feature_log_prob_[idx_clase])
    palabras = rng.choice(vocab, size=n_palabras, p=probs)
    return " ".join(palabras)

print(muestrear_mensaje("spam", 15, rng))
print(muestrear_mensaje("ham", 15, rng))
```

1. `nb.classes_` relaciona cada fila con su clase. No debo suponer que spam es la fila cero porque apareció primero en el corpus.
2. `feature_log_prob_` guarda **logaritmos** de las probabilidades de palabras por clase. Aplico `np.exp` para recuperar las probabilidades.
3. `rng.choice(..., p=probs)` sortea palabras usando esos pesos, con reemplazo: una palabra puede aparecer varias veces.
4. La longitud la elijo yo; este ejemplo no aprende cuándo terminar el mensaje.

La función generaliza `muestrar_spam` del notebook y corrige el nombre a «muestrear». Cada llamada consume números del generador aleatorio. Si genero un resultado y después llamo otra vez dentro de `print`, imprimo una muestra diferente. Para repetir exactamente una ejecución necesito la misma semilla **y el mismo orden de llamadas**.

> [!tip] ¿Por qué puede salir «pipeline» en un spam generado?
> El vocabulario incluye las dos clases y el suavizado asigna probabilidad positiva a todas sus palabras. «pipeline» tiene probabilidad $1/77$ en spam, aunque no apareció en esos cinco mensajes. La muestra puede mezclar vocabulario y no será necesariamente gramatical: el modelo no considera el orden.

## 2. GMM: mezcla de gaussianas

### ¿Qué aprendí?

Un GMM representa datos mediante varios componentes gaussianos. En dos dimensiones, cada componente tiene un centro y una dispersión que puede verse como una elipse. El modelo aprende cuánto pesa cada componente y permite generar puntos nuevos.

Teoría y EM paso a paso: [[08 S01 - GMM variables latentes y algoritmo EM]].

$$p(x)=\sum_{k=1}^{K}\pi_k\mathcal N(x\mid\mu_k,\Sigma_k).$$

| Símbolo | Significado |
| --- | --- |
| $K$ | Número de componentes, aquí 3 |
| $\pi_k$ | Peso del componente; todos los pesos suman 1 |
| $\mu_k$ | Media o centro |
| $\Sigma_k$ | Covarianza: dispersión y relación entre coordenadas |
| $z$ | Identidad del componente oculto |

> [!important] Aclaración del título del notebook
> Aunque la sección dice «variables latentes continuas», el componente $z\in\{1,2,3\}$ de este GMM es **discreto**. El punto observado $x\in\mathbb R^2$ es continuo. El espacio latente continuo de un VAE es otro caso.

### Entrenar y generar puntos nuevos

```python
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

X2d, _ = make_blobs(
    n_samples=400, centers=3, cluster_std=1.1, random_state=7
)
gmm = GaussianMixture(n_components=3, random_state=7).fit(X2d)
X_nuevo, componentes = gmm.sample(200)

print("Pesos:", gmm.weights_.round(2))
print("Formas:", X2d.shape, X_nuevo.shape, componentes.shape)

plt.figure(figsize=(7, 5))
plt.scatter(X2d[:, 0], X2d[:, 1], alpha=0.4, label="Entrenamiento sintético")
plt.scatter(X_nuevo[:, 0], X_nuevo[:, 1], alpha=0.5, label="Muestras del GMM")
plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Datos de entrenamiento y puntos generados")
plt.legend()
plt.show()
```

`X2d` tiene forma `(400, 2)` y `X_nuevo`, `(200, 2)`. La segunda salida de `sample` contiene 200 identificadores de componentes. En el notebook se descarta con `_`; aquí la conservo para mostrar qué devuelve.

Los pesos del ejemplo son aproximadamente `[0.34, 0.33, 0.33]`. Los números de componente son identificadores arbitrarios: intercambiar sus etiquetas no cambia la mezcla.

Los puntos de entrenamiento también son sintéticos: los creó `make_blobs`. La leyenda «datos reales» del notebook significa «datos de referencia» en esta comparación; no son mediciones del mundo real. Las etiquetas que devuelve `make_blobs` se descartan: el GMM se ajusta sin conocerlas.

### Qué hace EM dentro del ajuste

- **Paso E:** estima cuánto corresponde cada punto a cada componente, con los parámetros actuales. Estas probabilidades son las responsabilidades.
- **Paso M:** actualiza pesos, medias y covarianzas utilizando esas responsabilidades.
- Repite hasta el criterio de parada. La inicialización influye y no hay garantía de encontrar el mejor máximo global.

Generar invierte el recorrido: sorteo $z\sim\operatorname{Categorica}(\pi)$ y luego $x\sim\mathcal N(\mu_z,\Sigma_z)$. Muestrear no vuelve a entrenar el modelo ni se limita a seleccionar filas del entrenamiento.

Para leer el gráfico, comparo ubicación, dispersión y proporción de las nubes. Que visualmente se parezcan es una comprobación inicial; por sí sola no demuestra que el modelo represente bien cualquier dato nuevo.

## 3. Bigramas: mi primer modelo autorregresivo

### ¿Qué aprendí?

Un modelo autorregresivo construye una secuencia paso a paso. El bigrama cuenta qué palabra sigue a otra y usa únicamente la última palabra para elegir la siguiente. Un par contiene dos tokens, pero su **contexto tiene un token**.

Teoría: [[09 S01 - Markov HMM y generación con bigramas]].

### Corpus y tabla de conteos

```python
from collections import defaultdict, Counter

texto = """
el modelo aprende de los datos y el modelo genera texto nuevo
los datos entrenan el modelo y el modelo predice el siguiente token
el siguiente token depende del contexto y el contexto define la probabilidad
la probabilidad de cada token depende de los tokens anteriores
el transformer procesa todos los tokens anteriores sin cuello de botella
"""

tokens = texto.split()
conteos = defaultdict(Counter)
for w1, w2 in zip(tokens, tokens[1:]):
    conteos[w1][w2] += 1

print(len(tokens), "tokens;", len(set(tokens)), "únicos")
print(conteos["el"])
```

Hay **57 tokens, 29 diferentes y 56 pares consecutivos**. `tokens[1:]` desplaza la lista una posición: `zip` empareja el primer token con el segundo, el segundo con el tercero, etc.

Después de `el` aparece `modelo` cuatro veces, `siguiente` dos, `contexto` una y `transformer` una. La distribución se obtiene normalizando la fila:

$$P(v\mid u)=\frac{C(u,v)}{\sum_{v'}C(u,v')}.$$

| Continuación de `el` | Conteo | Probabilidad |
| --- | --- | --- |
| `modelo` | 4 | $4/8=0.5$ |
| `siguiente` | 2 | $2/8=0.25$ |
| `contexto` | 1 | $1/8=0.125$ |
| `transformer` | 1 | $1/8=0.125$ |

El denominador cuenta las **transiciones que salen de ese contexto**. Si un token aparece al final del corpus, esa aparición no aporta una continuación.

### Generar texto

```python
def generar_texto(inicio, n_pasos=20, rng=None):
    if rng is None:
        rng = np.random.default_rng()
    actual = inicio
    resultado = [actual]
    for _ in range(n_pasos):
        fila = conteos.get(actual)
        if not fila:
            break
        siguientes = list(fila.keys())
        frecuencias = np.array(list(fila.values()), dtype=float)
        probs = frecuencias / frecuencias.sum()
        actual = rng.choice(siguientes, p=probs)
        resultado.append(actual)
    return " ".join(resultado)

print(generar_texto("el", n_pasos=20, rng=np.random.default_rng(42)))
```

Con 20 pasos se producen **hasta 21 tokens**: la palabra inicial y 20 continuaciones. Si llego a `botella`, que solo aparece al final, no hay continuación y la función termina. Una palabra inicial desconocida también hace que termine inmediatamente.

Uso `conteos.get(actual)` para consultar sin crear una fila vacía. A diferencia del Naive Bayes anterior, este código **no aplica suavizado**: una transición no observada no se puede generar.

### La probabilidad de una secuencia

La regla de la cadena permite escribir exactamente:

$$P(x_{1:T})=P(x_1)\prod_{t=2}^{T}P(x_t\mid x_1,\ldots,x_{t-1}).$$

El modelo de bigramas hace la aproximación de Markov de primer orden:

$$P(x_t\mid x_1,\ldots,x_{t-1})\approx P(x_t\mid x_{t-1}).$$

En este código fijo `el` como inicio. La probabilidad de que las tres siguientes palabras sean `modelo genera texto` es:

$$P(\text{modelo genera texto}\mid\text{el})
=\frac{4}{8}\times\frac{1}{4}\times1=\frac18.$$

Es la probabilidad de esas tres continuaciones, no la de terminar allí: el código no tiene un símbolo de fin aprendido.

### Detalle del notebook: los saltos de línea no separan oraciones

`texto.split()` trata los saltos de línea como espacios. Por eso aprende también el par `nuevo → los` entre la primera y segunda línea. Si considero cada línea una oración independiente, conviene contar cada una por separado y añadir inicio y fin:

```python
conteos_oraciones = defaultdict(Counter)
for linea in texto.strip().splitlines():
    secuencia = ["<inicio>"] + linea.split() + ["<fin>"]
    for anterior, siguiente in zip(secuencia, secuencia[1:]):
        conteos_oraciones[anterior][siguiente] += 1
```

Esta variante cambia los conteos. Para generar con ella debo usar `conteos_oraciones`, comenzar en `<inicio>` y detenerme al muestrear `<fin>`, manteniendo un límite de pasos. No debo mezclar sus resultados con la tabla original.

## 4. ¿Qué le falta al bigrama para ser un GPT?

La respuesta del notebook —más contexto, mejores relaciones y más texto— se puede precisar así:

1. **Contexto más amplio:** el bigrama olvida todo salvo la última palabra. Un GPT condiciona en un prefijo de múltiples tokens dentro de su ventana de contexto.
2. **Representaciones aprendidas:** este ejercicio usa palabras separadas por espacios y conteos. Un GPT emplea un tokenizador y vectores aprendidos para representar sus tokens.
3. **Una red neuronal con atención causal:** permite combinar información de posiciones anteriores y compartir parámetros entre distintos contextos. Una tabla de bigramas aprende una fila separada por palabra.
4. **Entrenamiento por optimización a gran escala:** el ejercicio normaliza conteos; un GPT ajusta parámetros para predecir el siguiente token en muchos ejemplos.

Ambos generan autorregresivamente, pero compartir esa receta no los convierte en el mismo modelo. Añadir más texto al bigrama mejora sus estimaciones sin ampliar su contexto de un token.

La frase del corpus «sin cuello de botella» forma parte del texto de ejemplo. No debe interpretarse como ausencia de límites de cómputo, memoria o contexto en un transformer.

Para continuar: [[11 S01 - Del bigrama al LLM y primeros conceptos de agentes]] y [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]]. Estos ejercicios construyen modelos generativos; todavía no implementan el ciclo de un agente que usa herramientas y actúa sobre sus resultados.

## 5. Preguntas para comprobar que entendí

> [!question]- ¿Por qué Naive Bayes es generativo si lo uso para clasificar?
> Porque modela la distribución de los datos condicionada a la clase y el prior de clase. Puedo usar Bayes para clasificar o muestrear datos de esa distribución para generar.

> [!question]- ¿Por qué las clases tienen prior 0.5 si tienen diferentes totales de tokens?
> Hay cinco mensajes por clase. El prior usa el número de mensajes; la distribución de palabras usa los tokens de cada clase.

> [!question]- ¿Qué ocurre con una palabra totalmente desconocida para el vectorizador?
> Se ignora. Si todo el mensaje queda fuera del vocabulario, su vector es cero y la decisión depende de los priors. Laplace suaviza las palabras del vocabulario existente.

> [!question]- ¿Puedo usar directamente feature_log_prob_ como p en rng.choice?
> No. Contiene logaritmos; debo exponenciar para obtener probabilidades no negativas que sumen 1.

> [!question]- ¿Qué es discreto y qué es continuo en este GMM?
> La identidad del componente z es discreta; las coordenadas del punto x son continuas.

> [!question]- ¿Un bigrama puede formar una frase que no apareció completa en el corpus?
> Sí. Puede combinar transiciones observadas en una ruta nueva. Eso no garantiza coherencia global.

> [!question]- ¿Generar 20 pasos equivale a generar exactamente 20 palabras?
> No. Se empieza con una palabra y se añaden hasta 20 más. Puede detenerse antes si no hay continuación.

> [!question]- ¿Las frases generadas y el ejemplo de clasificación demuestran generalización?
> No. Para evaluar clasificación necesito mensajes etiquetados independientes del entrenamiento. Las muestras permiten observar el comportamiento generativo, pero no sustituyen una evaluación.

## Fuente y alcance

- [[s1-lun-estudiante.ipynb]]: corpus, configuración y ejercicios de Naive Bayes, GMM y bigramas. Se revisaron las celdas y sus salidas guardadas.
- Esta nota conserva los datos del notebook; amplía la interpretación, explicita fórmulas, generaliza la función de muestreo y añade una variante con límites de oración.
- Las notas 07, 08 y 09 desarrollan los fundamentos. Los cálculos de esta práctica corresponden al corpus del notebook, no al ejemplo simplificado de tres palabras de la nota 07.
