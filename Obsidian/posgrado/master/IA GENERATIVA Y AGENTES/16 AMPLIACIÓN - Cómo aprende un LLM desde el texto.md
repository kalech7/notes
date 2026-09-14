---
title: "16 AMPLIACIÓN - Cómo aprende un LLM desde el texto"
tags:
  - maestria/ia-generativa
  - estudio
---

# 16 AMPLIACIÓN - Cómo aprende un LLM desde el texto

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Continúa:** [[11 S01 - Del bigrama al LLM y primeros conceptos de agentes]]. Esta nota desarrolla el puente al LLM; no presupone saber programar un transformer.

## 1. Del texto a los identificadores

Un tokenizador convierte texto en unidades y les asigna identificadores de un vocabulario. Para explicar el recorrido, usaremos cuatro unidades: `[yo, estudio, Bayes, hoy]`. Son una tokenización didáctica; un tokenizador real puede dividir las palabras de otra forma.

El identificador no expresa por sí mismo significado: que un token tenga ID 25 y otro 26 no significa que sean más parecidos que 25 y 400. El ID permite localizar una fila de la tabla de representaciones vectoriales.

## 2. De identificadores a vectores

Cada token tiene un vector de entrada aprendido. Piensa en una lista de coordenadas que el entrenamiento ajusta para que resulte útil al modelo. No hay que asignar a mano «la coordenada de verbos» o «la coordenada de objetos».

Al procesar contexto, el modelo produce representaciones que dependen de la secuencia. El mismo token puede contribuir de forma diferente en frases distintas. Es importante separar **pesos aprendidos** de **representaciones calculadas para una entrada**.

*Hands-On Large Language Models* usa esta distinción para conectar las representaciones de tokens con aplicaciones que necesitan contexto. Aquí nos permite entender por qué una red puede ir más allá de una tabla aislada de pares.

## 3. El propio texto aporta los objetivos

Para nuestra secuencia, construimos:

```text
Entrada:   yo        estudio    Bayes
Objetivo:  estudio   Bayes      hoy
```

Cada posición predice el token siguiente. Visto como tareas:

| Contexto permitido | Token observado que debe predecir |
| --- | --- |
| yo | estudio |
| yo estudio | Bayes |
| yo estudio Bayes | hoy |

Esto es **aprendizaje autosupervisado**: la señal de entrenamiento se construye a partir de los propios datos. «Texto sin etiquetas manuales» no significa «entrenar sin objetivo».

## 4. Por qué hay que ocultar el futuro

Durante entrenamiento disponemos de toda la secuencia y podemos organizar cálculos por posiciones. Pero al predecir «estudio» desde «yo», permitir que el modelo mire «estudio» revelaría la respuesta.

La máscara causal impide consultar posiciones posteriores a la posición actual. Permite calcular muchas predicciones durante entrenamiento respetando el límite de información de cada una. Durante generación, los tokens futuros aún no existen y hay que producirlos progresivamente.

Esta máscara no prueba causalidad entre fenómenos del mundo, como se aclara en [[04 S00 - Correlación causalidad y límites de las predicciones]].

## 5. De puntajes a probabilidades

El modelo produce **logits**, puntajes sin normalizar para los tokens del vocabulario. Softmax los convierte en probabilidades no negativas que suman 1. Para calcular la pérdida se toma, en cada posición, la probabilidad asignada al token realmente observado.

Supón que las probabilidades de los tres objetivos son 0.5, 0.25 y 0.8. Su producto es 0.1. La pérdida promedio de log-verosimilitud negativa es:

$$L=-\frac{\ln0.5+\ln0.25+\ln0.8}{3}
=\frac{0.6931+1.3863+0.2231}{3}\approx0.7675.$$

Asignar 0.25 al objetivo penaliza más que asignarle 0.8. El logaritmo convierte el producto en suma y el signo negativo permite minimizar. Con objetivos categóricos observados, esta es la forma habitual de entropía cruzada.

Luego la retropropagación calcula gradientes y el optimizador actualiza los pesos. El texto de entrenamiento no desaparece del razonamiento: define cuáles eran los objetivos de esas actualizaciones.

## 6. Qué significa la perplejidad

Cuando la pérdida usa logaritmos naturales y promedio por token, la perplejidad se calcula como $\exp(L)$. En el ejemplo, aproximadamente 2.154.

Si un modelo asignara probabilidad uniforme a cada uno de cuatro tokens posibles en todos los pasos, su pérdida sería $\ln4$ y su perplejidad 4. Esa comparación ayuda a interpretar el número, pero no implica que el modelo esté literalmente considerando siempre esa cantidad de opciones.

Comparar perplejidades requiere condiciones compatibles, incluido corpus y tokenización. Una perplejidad menor no verifica hechos ni demuestra que una respuesta sea útil para una persona.

## 7. Por qué un modelo base no equivale a un asistente

El preentrenamiento busca aprender patrones de texto. Seguir instrucciones es un comportamiento más específico. Un modelo base podría continuar un documento que empieza con una pregunta sin responderla como tú esperas.

El ajuste para instrucciones utiliza ejemplos de la conducta deseada y modifica parámetros. Proporcionar un ejemplo dentro de un prompt solo condiciona la inferencia ordinaria: no es ese mismo entrenamiento.

El libro *Hands-On* presenta el recorrido general de preentrenamiento y adaptación. Estos pasos explican por qué «conoce patrones de lenguaje», «clasifica», «sigue instrucciones» y «actúa con herramientas» describen capacidades distintas.

**Fuentes consultadas:** [[Hands-On_Large_Language_Models.pdf#page=48|Alammar y Grootendorst, p. impresa 26; PDF 48]] y [[Hands-On_Large_Language_Models.pdf#page=79|pp. 57–59; PDF 79–81]]. [[Build_a_Large_Language_Model_From_Scrat.pdf#page=59|Raschka, §2.6, pp. 37–38; PDF 59–60]], [[Build_a_Large_Language_Model_From_Scrat.pdf#page=97|§3.5.1, p. 75; PDF 97]] y [[Build_a_Large_Language_Model_From_Scrat.pdf#page=159|§5.1, pp. 137–139; PDF 159–161]]. Los ejemplos y cálculos de esta nota son propios.

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
