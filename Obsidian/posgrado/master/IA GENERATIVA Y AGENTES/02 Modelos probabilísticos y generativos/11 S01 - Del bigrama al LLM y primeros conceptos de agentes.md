---
title: "11 S01 - Del bigrama al LLM y primeros conceptos de agentes"
tags:
  - maestria/ia-generativa
  - estudio
---

# 11 S01 - Del bigrama al LLM y primeros conceptos de agentes

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. Lo que ya sabes del bigrama

En la nota anterior, un bigrama elegía la siguiente palabra mirando solo la última. Podía aprender que después de «yo» aparecía «estudio», pero no representaba una relación larga entre partes de una frase.

Un LLM autorregresivo también genera un elemento después de otro. La diferencia es que usa una red entrenada para calcular la siguiente distribución a partir de un contexto más amplio.

LLM significa **modelo grande de lenguaje**. En esta nota hablaremos del tipo generativo autorregresivo, como los modelos de la familia GPT.

## 2. Mira primero el recorrido completo

![Generación paso a paso en un LLM](<../Recursos visuales/08-llm-ciclo.png>)

El sistema convierte el texto en tokens, los representa con números, procesa el contexto y calcula probabilidades para el siguiente token. Elige uno, lo añade al texto y repite.

La flecha que regresa al principio significa **añadir información al contexto**. No significa volver a entrenar los pesos en cada vuelta.

## 3. Qué es un token

Un token es una unidad del vocabulario del modelo. Puede ser una palabra, una parte de una palabra, un signo u otra unidad definida por el tokenizador.

En los ejercicios dividimos por espacios para simplificar. Un LLM real puede dividir de otra forma. Por eso no debes asumir que diez palabras son diez tokens.

## 4. Por qué usa vectores y contexto

Cada token tiene una representación numérica inicial, llamada **embedding** o representación vectorial. La red utiliza esos vectores para calcular relaciones útiles.

Piensa en «banco» en «me senté en el banco» y «deposité dinero en el banco». Si se usa el mismo token, puede comenzar con el mismo vector. Al procesar las palabras que lo rodean, las representaciones internas pueden volverse diferentes.

No cambió necesariamente la tabla de pesos. Cambió el resultado de procesar una entrada distinta. Esta diferencia entre pesos y activaciones es importante para entender la inferencia.

## 5. Qué cambia respecto del bigrama

| Bigrama del ejercicio | LLM autorregresivo |
| --- | --- |
| Mira un elemento anterior | Utiliza el prefijo disponible dentro de su contexto |
| Cuenta pares | Calcula con una red neuronal |
| Cada fila describe un contexto por separado | Comparte pesos entre muchos contextos |
| No aprende vectores de significado en esa tabla | Aprende representaciones útiles de los datos |

Más datos por sí solos no convierten una tabla de bigramas en un transformer. También cambia la forma de representar y calcular las probabilidades.

La identidad se conserva:

$$P(x_1,\ldots,x_n)=\prod_{t=1}^{n}P(x_t\mid x_{<t}).$$

Es decir: la probabilidad de la secuencia se construye con las probabilidades sucesivas. La red aprende cómo calcular esos factores.

## 6. Entrenar, elegir y responder son operaciones distintas

Al entrenar, el texto observado proporciona los objetivos: qué token venía después de cada prefijo. Se ajustan los pesos para mejorar esas predicciones.

Al generar, los pesos suelen estar fijos. Si tras «estudio» las opciones son Bayes 0.5, IA 0.3 y probabilidad 0.2, elegir siempre la de mayor probabilidad produce «Bayes». Eso se llama **greedy**. Muestrear permite obtener cualquiera de las tres según sus probabilidades.

Predecir texto no equivale a verificar la verdad de cada frase. Tampoco equivale automáticamente a seguir instrucciones. El modelo base puede necesitar entrenamiento adicional para adoptar el comportamiento de un asistente.

En [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] puedes seguir todo el entrenamiento con una frase de cuatro unidades.

## 7. Dónde encajan RAG y los agentes

Imagina tres asistentes para estudiar:

1. Uno responde a partir del modelo de lenguaje.
2. Otro busca el apartado en tus PDF y usa el texto recuperado para responder. Añade **RAG**, recuperación de información seguida de generación con ese contexto.
3. Otro decide qué buscar, usa una calculadora y revisa si los resultados bastan para completar una tarea. Añade un ciclo de acciones y observaciones propio de un **agente**.

Pueden combinarse. RAG no garantiza que toda respuesta esté bien respaldada, y un agente no es necesariamente un modelo más grande: incluye herramientas, reglas de acción, estado y condiciones para detenerse.

Este apartado solo ubica esos conceptos. Las sesiones 00 y 01 todavía no desarrollan un curso completo de agentes.

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-01.pdf#page=18|Sesión 01, páginas 18–20]]
- [[Hands-On_Large_Language_Models.pdf#page=48|Alammar y Grootendorst, p. impresa 26; PDF 48]]
- [[Hands-On_Large_Language_Models.pdf#page=79|pp. 57–59; PDF 79–81]]
- [[Build_a_Large_Language_Model_From_Scrat.pdf#page=59|Raschka, §2.6, pp. 37–38; PDF 59–60]]
- [[Build_a_Large_Language_Model_From_Scrat.pdf#page=159|§5.1, pp. 137–139; PDF 159–161]]

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Qué tres cosas le faltan al bigrama para acercarse a un GPT?
> Contexto más amplio, representaciones aprendidas y una red que comparta parámetros entre contextos. También importan arquitectura y escala de entrenamiento.

> [!question]- ¿Cada token es una palabra?
> No. Depende del vocabulario y del tokenizador; una palabra puede dividirse en varias unidades.

> [!question]- ¿Generar normalmente actualiza los pesos?
> No. Se usan los pesos entrenados para calcular distribuciones; cambian el prefijo y las activaciones.

> [!question]- ¿Una continuación muy probable está necesariamente verificada?
> No. Probabilidad de texto y verdad de una afirmación son conceptos distintos.

> [!question]- ¿Qué diferencia básica hay entre RAG y un agente?
> RAG incorpora recuperación de información al proceso de respuesta. Un agente incorpora un ciclo de decisiones y acciones con herramientas y observaciones. Pueden combinarse.


> [!question]- ¿Por qué una palabra puede tener representaciones diferentes sin reentrenar?
> Porque el contexto cambia las activaciones internas. La tabla de entrada y los demás pesos pueden permanecer fijos.

> [!question]- ¿De dónde salen los objetivos del preentrenamiento autorregresivo?
> Del propio texto: el objetivo de cada posición es el siguiente token observado.
