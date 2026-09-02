---
title: Conceptos para recordar antes de comparar modelos
aliases:
  - Prerrequisitos de comparación estadística
tags:
  - posgrado
  - estadistica
  - fundamentos
  - machine-learning
related: "[[00 Índice - Comparación estadística de modelos]]"
---

# Conceptos para recordar antes de comparar modelos

Volver al [[00 Índice - Comparación estadística de modelos|índice]] · Siguiente: [[02 Diseño pareado, diferencias e independencia]]

Esta nota empieza desde los conceptos mínimos. La intención es que las fórmulas posteriores no se conviertan en símbolos memorizados sin significado.

## 1. Modelo, predicción y métrica

Un **modelo** es una regla aprendida que transforma una entrada $x$ en una predicción $\hat y$. Por ejemplo, una imagen puede producir una probabilidad $q=0.8$ de pertenecer a cierta clase.

Una **métrica** transforma el comportamiento del modelo en un número que podamos comparar. La métrica define tres cosas:

1. qué aspecto del comportamiento se evalúa;
2. en qué escala se expresa;
3. qué dirección significa mejorar.

No todas las métricas dicen lo mismo. *Accuracy* pregunta cuántas etiquetas fueron acertadas; *log-loss* evalúa la calidad de las probabilidades y penaliza con fuerza la confianza equivocada. Revisa [[funcion de perdida]] para conectar estas ideas con el entrenamiento.

### La log-loss del caso conductor

Para una etiqueta binaria $y\in\{0,1\}$ y una probabilidad predicha $q\in(0,1)$:

$$
\ell(y,q)=-\left[y\log(q)+(1-y)\log(1-q)\right].
$$

Lectura de cada símbolo:

- $y$ es la respuesta real;
- $q$ es la probabilidad que el modelo asigna a la clase $1$;
- $\ell(y,q)$ es la pérdida para un caso;
- el signo negativo convierte logaritmos negativos en una pérdida positiva;
- una predicción correcta y segura produce una pérdida pequeña.

Si $y=1$, la fórmula se reduce a $-\log(q)$. Predecir $q=0.9$ da aproximadamente $0.105$, mientras que $q=0.6$ da aproximadamente $0.511$. La primera predicción es mejor y por eso su pérdida es menor.

> [!important] Regla de dirección
> En este módulo, **menor log-loss significa mejor desempeño**. La resta se define como $A-B$; por tanto, una diferencia positiva favorece a B.

## 2. Observación, unidad de análisis y fila

Una **observación** es una medición registrada. La **unidad de análisis** es la entidad que aporta esa medición y sobre la cual queremos razonar.

Una fila de una tabla no identifica por sí sola la unidad. Una fila podría representar:

- un caso de prueba;
- una corrida completa de entrenamiento;
- un dataset o tarea;
- un *fold* de validación cruzada.

Los cuatro ejemplos pueden tener diez filas, pero responden preguntas distintas. La unidad determina la fuente de variabilidad y hasta dónde puede generalizarse el resultado. Esto se desarrolla en [[06 Unidad de análisis, dependencia y validación cruzada]].

## 3. Población, muestra y proceso generador

La **población objetivo** es el conjunto o proceso sobre el cual queremos aprender algo. La **muestra** contiene las unidades que realmente observamos.

```mermaid
flowchart LR
    A[Población o proceso objetivo] -->|muestreo| B[Muestra observada]
    B --> C[Mediciones de A y B]
    C --> D[Diferencias d_i]
    D --> E[Estimación de Delta]
    E -.incertidumbre.-> A
```

### Cómo leer el diagrama

- La flecha de población a muestra recuerda que los datos son una realización posible del proceso.
- A y B se miden sobre las unidades observadas.
- Las diferencias $d_i$ conservan la comparación dentro de cada unidad.
- Con la muestra estimamos $\Delta$, pero no observamos directamente el parámetro poblacional.
- La flecha punteada representa la inferencia: volver de la muestra al proceso requiere supuestos y un diseño defendible.

> [!example] En el caso del módulo
> Si la unidad es un caso de prueba y los modelos ya están entrenados, la población objetivo podría ser «casos futuros comparables atendidos por estos mismos modelos fijos». No incluye automáticamente nuevas semillas, nuevos entrenamientos ni otros dominios.

## 4. Variable, parámetro, estimando y estimación

Una **variable aleatoria** representa un valor que podría cambiar si repitiéramos el proceso de muestreo. En este módulo:

$$
D=\operatorname{loss}_A-\operatorname{loss}_B
$$

es la diferencia para una unidad extraída de la población objetivo.

El **estimando** es la cantidad poblacional que decidimos conocer:

$$
\Delta=\mathbb E[D]
=\mathbb E[\operatorname{loss}_A-\operatorname{loss}_B].
$$

- $\mathbb E$ significa valor esperado o promedio de largo plazo en el proceso objetivo.
- $\Delta$ es fijo pero desconocido dentro del enfoque frecuentista.
- Declarar $\Delta$ obliga a especificar métrica, resta, unidad y población.

La **estimación** usa la muestra:

$$
\widehat\Delta=\bar d=\frac{1}{n}\sum_{i=1}^n d_i.
$$

El sombrero en $\widehat\Delta$ indica «estimado». En el caso del módulo, $\widehat\Delta=0.019$.

| Objeto | ¿Se observa? | ¿Puede cambiar con otra muestra? |
| --- | :---: | :---: |
| $\Delta$ | No | No; es el parámetro del proceso fijado |
| $d_i$ | Sí | Sí |
| $\widehat\Delta=\bar d$ | Sí, se calcula | Sí |

## 5. Media, desviación estándar y error estándar

### Media

La media muestral resume el centro de las diferencias:

$$
\bar d=\frac{1}{n}\sum_{i=1}^{n}d_i.
$$

### Desviación estándar muestral

La desviación estándar describe cuánto difieren los casos entre sí:

$$
s_d=\sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(d_i-\bar d)^2}.
$$

Se divide entre $n-1$ porque la media ya fue estimada con la misma muestra; queda un grado de libertad menos.

### Error estándar de la media

El error estándar describe la precisión con la que la media muestral estima el promedio poblacional:

$$
\operatorname{SE}(\bar d)=\frac{s_d}{\sqrt n}.
$$

| Cantidad | Pregunta | En el ejemplo |
| --- | --- | ---: |
| $s_d$ | ¿Cuánto varían las diferencias entre casos? | $0.0260128$ |
| $\operatorname{SE}(\bar d)$ | ¿Con qué precisión estimamos la media? | $0.0082260$ |

> [!warning] No intercambiar
> El error estándar no es la dispersión de los casos. Es la dispersión esperada de la **media** si pudiéramos repetir muestras comparables bajo el modelo.

Al aumentar $n$, el denominador $\sqrt n$ crece y el error estándar suele disminuir. Pero duplicar filas dependientes no equivale a duplicar información independiente.

## 6. Emparejamiento e independencia

Hay **emparejamiento** cuando A y B se miden sobre la misma identidad: el mismo paciente, imagen, documento, dataset o corrida, según la pregunta.

La diferencia

$$
d_i=A_i-B_i
$$

elimina la variación compartida dentro del par y concentra la comparación en lo que cambia entre A y B.

Sin embargo:

$$
\text{pareado}\not\Rightarrow\text{independiente entre unidades}.
$$

Los pares pueden compartir hospital, usuario, equipo, periodo, dataset o entrenamiento. La prueba trabaja sobre $d_1,\ldots,d_n$ y necesita que su estructura de dependencia sea compatible con el método elegido.

## 7. Hipótesis, estadístico y distribución de referencia

Una **hipótesis nula** declara un modelo de referencia. Para la prueba $t$ del módulo:

$$
H_{0,t}:\Delta=0,
\qquad
H_{1,t}:\Delta\ne0.
$$

El **estadístico de prueba** resume cuán lejos está el resultado de la referencia nula en una escala de incertidumbre:

$$
T=\frac{\bar d-0}{\operatorname{SE}(\bar d)}.
$$

La **distribución de referencia** describe los valores que podría tomar $T$ si la nulidad y los supuestos fueran adecuados. No describe «la probabilidad de que la nulidad sea verdadera».

## 8. $p$-value

En una prueba bilateral:

$$
p=P\!\left(|T|\ge |T_{\text{obs}}|\mid H_0,\text{ diseño y supuestos}\right).
$$

El $p$-value responde:

> Si la referencia nula fuera el modelo adecuado, ¿qué proporción de resultados sería al menos tan extrema como el observado?

No responde:

- la probabilidad de que $H_0$ sea verdadera;
- la probabilidad de que B sea mejor;
- la probabilidad de repetir el mismo signo;
- la magnitud o importancia práctica del efecto.

## 9. Intervalo de confianza

Un intervalo de confianza del $95\%$ construido con la prueba $t$ es

$$
\bar d\pm t_{0.975,n-1}\operatorname{SE}(\bar d).
$$

El intervalo combina efecto y precisión. En el ejemplo:

$$
IC_{95\%}=[0.00039155,\ 0.03760845].
$$

Lectura frecuentista: son valores de $\Delta$ compatibles con los datos bajo el procedimiento y sus supuestos. No significa que exista $95\%$ de probabilidad posterior de que el parámetro fijo esté dentro.

## 10. Significancia estadística, relevancia práctica y equivalencia

Son tres preguntas distintas:

| Pregunta | Herramienta típica |
| --- | --- |
| ¿El resultado es extremo bajo una nulidad? | Contraste y $p$-value |
| ¿Qué magnitudes son compatibles y con qué precisión? | Estimación e intervalo |
| ¿La diferencia importa en el problema real? | Umbral sustantivo, costos y contexto |

Además, $p>0.05$ no demuestra igualdad. Para defender equivalencia se necesita un margen de equivalencia fijado por razones sustantivas y una prueba diseñada para esa pregunta.

## Glosario mínimo de símbolos

| Símbolo | Lectura |
| --- | --- |
| $i$ | Índice de la unidad |
| $n$ | Número de unidades observadas |
| $d_i$ | Diferencia de A menos B en la unidad $i$ |
| $D$ | Diferencia aleatoria en la población objetivo |
| $\Delta$ | Media poblacional de la diferencia; estimando |
| $\widehat\Delta=\bar d$ | Estimación muestral de $\Delta$ |
| $s_d$ | Desviación estándar de las diferencias |
| $\operatorname{SE}(\bar d)$ | Error estándar de la media |
| $T$ | Estadístico de la prueba $t$ |
| $H_0,H_1$ | Hipótesis nula y alternativa |
| $p$ | Extremidad bajo una referencia nula |
| $IC_{95\%}$ | Intervalo obtenido por un procedimiento con cobertura nominal del $95\%$ |

## Comprobación rápida

Antes de continuar, intenta responder:

1. ¿Por qué una fila no define por sí sola la unidad?
2. ¿Qué diferencia hay entre $\Delta$ y $\widehat\Delta$?
3. ¿Por qué $s_d$ y $\operatorname{SE}(\bar d)$ no son intercambiables?
4. ¿Qué probabilidad calcula realmente un $p$-value?
5. ¿Por qué «pareado» no implica «independiente entre unidades»?

> [!success]- Respuestas breves
> 1. Porque la procedencia decide si representa un caso, corrida, dataset o *fold*.
> 2. $\Delta$ es el promedio poblacional desconocido; $\widehat\Delta$ es el promedio calculado en la muestra.
> 3. El primero mide heterogeneidad entre unidades; el segundo, precisión de la media.
> 4. La proporción de resultados al menos tan extremos bajo $H_0$, el diseño y los supuestos.
> 5. Porque unidades diferentes pueden compartir fuentes de información y por ello sus diferencias pueden depender entre sí.

Anterior: [[00 Índice - Comparación estadística de modelos]] · Siguiente: [[02 Diseño pareado, diferencias e independencia]]
