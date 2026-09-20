---
title: "16 AMPLIACIÓN - Cómo aprende un LLM desde el texto"
tags:
  - maestria/ia-generativa
  - estudio
---

# 16 AMPLIACIÓN - Cómo aprende un LLM desde el texto

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. Vamos a entrenar con una frase muy pequeña

Usaremos «yo estudio Bayes hoy» para entender de dónde salen las entradas, los objetivos y la pérdida de un modelo de lenguaje.

Para facilitar la explicación trataremos cada palabra como una unidad. Es una tokenización didáctica: un tokenizador real podría dividir de otra forma. Esta nota amplía [[11 S01 - Del bigrama al LLM y primeros conceptos de agentes]].

## 2. El modelo necesita números para calcular

El tokenizador transforma el texto en tokens y los asocia con identificadores, llamados IDs. Un ID solo identifica una unidad. Tener ID 26 no significa ser más parecido al 25 que al 400.

Después se busca un vector para cada ID en una tabla aprendida. Ese vector es el **embedding de entrada**: una lista de números que se ajusta durante entrenamiento.

La red procesa esos vectores junto con información de posición y contexto. Sus representaciones internas pueden cambiar entre frases aunque los pesos sigan fijos. No necesitas asignar a mano una coordenada que signifique «verbo» u «objeto».

## 3. Los objetivos ya están en el propio texto

Construimos estas dos filas:

```text
Entrada:   yo        estudio    Bayes
Objetivo:  estudio   Bayes      hoy
```

La fila de objetivos está desplazada una posición. Cada posición intenta predecir qué viene después:

| Lo que puede usar | Lo que debe predecir |
| --- | --- |
| yo | estudio |
| yo estudio | Bayes |
| yo estudio Bayes | hoy |

No necesitamos una persona que escriba manualmente la respuesta correcta para cada caso. Sale del texto. Por eso se llama **aprendizaje autosupervisado**: los datos proporcionan la señal con la que se entrena.

## 4. Por qué ocultamos las palabras futuras

Durante entrenamiento tenemos la frase completa, pero permitir que «yo» consulte «estudio» para predecir «estudio» revelaría la respuesta.

La **máscara causal** impide que una posición lea posiciones posteriores. Así podemos calcular muchas predicciones durante entrenamiento sin que cada una use información que no debería tener.

Durante generación el futuro todavía no existe. El modelo elige un token, lo añade y calcula el siguiente.

![Ciclo de generación de un modelo de lenguaje](<../Recursos visuales/08-llm-ciclo.png>)

Lee la flecha de retorno como «añadir un token al contexto». No es una actualización de pesos. Tampoco la palabra causal significa aquí que el modelo haya descubierto causas del mundo: se refiere a la restricción de lectura del texto.

## 5. Cómo se convierte una predicción en una pérdida

El modelo produce un puntaje para cada token del vocabulario. Esos puntajes se llaman **logits**. Softmax los transforma en probabilidades que suman 1.

Para evaluar la predicción buscamos la probabilidad que asignó al token correcto de cada posición. Supón estos resultados:

| Objetivo observado | Probabilidad asignada | Penalización: −ln(probabilidad) |
| --- | --- | --- |
| estudio | 0.5 | 0.6931 |
| Bayes | 0.25 | 1.3863 |
| hoy | 0.8 | 0.2231 |

Asignar poca probabilidad al token observado produce una penalización mayor. La predicción de Bayes recibe más penalización que la de hoy.

Promediamos las tres:

$$L=\frac{0.6931+1.3863+0.2231}{3}\approx0.7675.$$

Esta pérdida es la **log-probabilidad negativa promedio**. Con objetivos categóricos observados corresponde a la forma habitual de **entropía cruzada**.

## 6. Cómo se aprende a partir de ese número

La pérdida indica cuánto penaliza el criterio a las predicciones. La retropropagación calcula derivadas: cómo influirían pequeños cambios de los parámetros en esa pérdida. El optimizador utiliza esa información para actualizar los pesos.

Se repite con muchos ejemplos. El objetivo es mejorar predicciones también en textos nuevos, por lo que se evalúa fuera de los datos usados para ajustar.

La relación con máxima verosimilitud es directa: asignar más probabilidad al texto observado equivale a reducir su log-probabilidad negativa. El logaritmo convierte productos de probabilidades en sumas más manejables.

## 7. Qué significa la perplejidad

Cuando L usa logaritmo natural y promedio por token, la perplejidad es $\exp(L)$. Para 0.7675, aproximadamente 2.154.

Un ejemplo más fácil: si el modelo diera probabilidad 1/4 al objetivo en cada paso, su pérdida sería $\ln4$ y su perplejidad 4. Esto ayuda a interpretar el número, pero no significa que siempre considere literalmente cuatro opciones.

Para comparar perplejidades necesitas condiciones compatibles, como corpus y tokenización. Un valor menor no comprueba que las afirmaciones sean verdaderas ni que una respuesta sea útil.

## 8. Por qué aprender lenguaje no equivale a seguir instrucciones

El preentrenamiento enseña patrones de continuación de texto. Un modelo base podría continuar una pregunta con más preguntas en vez de responder como un asistente.

El ajuste para instrucciones utiliza ejemplos del comportamiento deseado y modifica parámetros. Dar ejemplos dentro de un prompt, en cambio, aporta contexto para responder sin actualizar normalmente los pesos.

La idea que debes poder explicar es esta: **el texto proporciona objetivos; el modelo calcula probabilidades; la pérdida orienta el ajuste de pesos**. Generar después consiste en utilizar lo aprendido para elegir tokens sucesivos.

Continúa con [[21 S03 - Preentrenamiento autosupervisado y MLE]] para conectar este ejemplo con el ciclo completo de entrenamiento, y con [[22 S03 - SFT RLHF DPO y Constitutional AI]] para entender por qué predecir texto no basta para seguir instrucciones.

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[Hands-On_Large_Language_Models.pdf#page=48|Alammar y Grootendorst, p. impresa 26; PDF 48]]
- [[Hands-On_Large_Language_Models.pdf#page=79|pp. 57–59; PDF 79–81]]
- [[Build_a_Large_Language_Model_From_Scrat.pdf#page=59|Raschka, §2.6, pp. 37–38; PDF 59–60]]
- [[Build_a_Large_Language_Model_From_Scrat.pdf#page=97|§3.5.1, p. 75; PDF 97]]
- [[Build_a_Large_Language_Model_From_Scrat.pdf#page=159|§5.1, pp. 137–139; PDF 159–161]]

## Preguntas para comprobar que entendiste

Responde primero y haz clic para comprobar.

> [!question]- ¿Un ID mayor significa que el token tiene más significado?
> No. Es un identificador del vocabulario, no una escala semántica.

> [!question]- Para «yo estudio Bayes hoy», ¿qué objetivos acompañan a «yo estudio Bayes»?
> «estudio Bayes hoy»: los objetivos están desplazados una posición.

> [!question]- ¿Por qué no se permite mirar el token siguiente al entrenar su predicción?
> Porque revelaría el objetivo y permitiría resolver una tarea distinta de predecir con el contexto disponible.

> [!question]- ¿Qué token observado penaliza más: uno con probabilidad 0.25 o uno con 0.8?
> El de 0.25: su log-probabilidad negativa es aproximadamente 1.3863, frente a 0.2231.

> [!question]- Si la pérdida por token es ln(4), ¿cuál es la perplejidad?
> 4, porque exp(ln(4))=4. Eso no es una puntuación de veracidad.
