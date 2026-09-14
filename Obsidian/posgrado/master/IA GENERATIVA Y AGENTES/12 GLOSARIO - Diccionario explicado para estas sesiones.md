---
title: "12 GLOSARIO - Diccionario explicado para estas sesiones"
tags:
  - maestria/ia-generativa
  - estudio
---

# 12 GLOSARIO - Diccionario explicado para estas sesiones

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[glosario-mmia-6013.pdf|Glosario del curso, versión suministrada del 13 de septiembre de 2026]], secciones de notación y términos de sesiones 01–04. Selección comentada, no transcripción completa.

## Cómo leer las letras sin perderte

| Símbolo | Significado en estas notas | Ejemplo |
| --- | --- | --- |
| X, x | Variable de datos y valor observado | Un correo |
| Y, y | Variable de clase y etiqueta concreta | Spam |
| D | Conjunto observado | Corpus de entrenamiento |
| $\theta$ | Parámetros de un modelo | Pesos o probabilidades ajustadas |
| z | Variable latente | Componente oculto de una mezcla |
| $\pi_k$ | Peso de un componente | 0.3 de peso en un GMM |
| $\mu$ | Media | Centro de una distribución |
| $\sigma^2$ | Varianza | Dispersión en una dimensión |
| $\Sigma$ | Covarianza | Dispersión y orientación multivariada |
| $x_{<t}$ | Elementos anteriores a t | Prefijo de una secuencia |
| $\sum$ | Sumar posibilidades | Marginalizar componentes |
| $\prod$ | Multiplicar factores | Probabilidad de una secuencia |
| $\mathbb E$ | Promedio bajo una distribución | Término esperado de ELBO |
| $\arg\max$ | Valor que maximiza una función | Parámetro MLE |

Una letra puede cambiar de significado entre contextos. Por ejemplo, K cuenta componentes en GMM y símbolos en el ejemplo de Markov. Lee siempre la definición local. No confundas una covarianza mayúscula $\Sigma$ con el operador de suma $\sum$.

## Probabilidad y aprendizaje

**Prior:** distribución antes de incorporar la evidencia considerada. No significa obligatoriamente una opinión arbitraria; puede expresar información previa o un supuesto explícito.

**Verosimilitud:** evaluación de los datos observados como función de parámetros o hipótesis. No es la posterior.

**Posterior:** distribución después de condicionar en datos. Especifica si se refiere a clase, parámetros o latente.

**Evidencia:** denominador que normaliza en Bayes; suma o integra sobre alternativas.

**MLE:** máxima verosimilitud. Ajusta un valor de parámetros maximizando la verosimilitud.

**Pérdida:** criterio numérico que se minimiza para entrenar. Una pérdida menor no garantiza por sí sola resolver todos los objetivos de uso.

**Parámetro:** cantidad ajustada al entrenar. **Hiperparámetro:** decisión que configura el ajuste, como una tasa de aprendizaje o número de componentes.

**Generalización:** funcionamiento en datos nuevos. **Sobreajuste:** capturar particularidades del entrenamiento que no se trasladan bien a esos datos.

**Muestrear:** extraer un resultado aleatorio siguiendo una distribución. No equivale a elegir siempre el máximo.

## Modelos y estructuras

**Discriminativo:** en clasificación, aprende una posterior de etiquetas o una función de decisión.

**Generativo:** modela una distribución de datos, posiblemente condicionada en información, y permite plantear generación. No significa automáticamente generación de lenguaje coherente.

**Latente:** variable no observada que el modelo utiliza para explicar datos. No es sinónimo de parámetro.

**GMM:** mezcla de gaussianas. Combina componentes y permite inferir responsabilidades.

**Responsabilidad:** probabilidad posterior de que un componente explique una observación.

**EM:** esperanza–maximización. Alterna inferencia del latente y reestimación de parámetros.

**Markov de orden M:** representa el siguiente elemento usando los M anteriores como contexto.

**HMM:** modelo oculto de Markov. Distingue estados ocultos de observaciones emitidas.

**VAE:** autocodificador variacional. Aprende un modelo generativo latente con un codificador aproximado.

**ELBO:** cota inferior de la log-evidencia que se maximiza en inferencia variacional.

**KL:** divergencia entre distribuciones. No es simétrica.

## Lenguaje y sistemas: vocabulario de transición

**Representación vectorial o embedding:** vector numérico que representa una unidad como un token o texto. La utilidad de sus relaciones depende del entrenamiento.

**Atención:** mecanismo que calcula combinaciones ponderadas de información del contexto. No es una intención consciente.

**Ventana de contexto:** cantidad de tokens que un sistema puede considerar en una entrada o proceso definido. No es el número de parámetros ni la dimensión de los vectores.

**Prompt:** entrada que proporciona instrucciones, contexto o ejemplos al modelo.

**Aprendizaje en contexto:** usar ejemplos en el prompt sin actualizar pesos. Se distingue de **ajuste fino**, que sí entrena parámetros.

**RAG:** recuperación de información seguida de generación con ese contexto.

**Agente:** sistema que combina un modelo con decisiones, herramientas y observaciones para realizar una tarea.

## Tres distinciones para repasar siempre

Probabilidad no es certeza. Representar una relación no identifica necesariamente una causa. Cambiar el contexto de entrada no equivale a entrenar los pesos.

## Términos de los libros incorporados a las notas

| Término | Explicación | Dónde verlo aplicado |
| --- | --- | --- |
| Capacidad | Conjunto de funciones que un modelo puede representar | [[02 S00 - Reglas modelos y aprendizaje desde datos]] |
| Costo esperado | Promedio del costo de una acción según las probabilidades de cada resultado | [[06 S01 - Modelos discriminativos y generativos]] |
| Prior conjugado | Prior cuya familia se conserva al actualizar con una verosimilitud determinada | [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]] |
| MAP | Valor que maximiza la posterior | [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]] |
| Posterior predictiva | Distribución de resultados nuevos promediando incertidumbre sobre parámetros | [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]] |
| Inferencia amortizada | Red entrenada para aproximar la posterior de distintos datos | [[10 S01 - VAE espacio latente y ELBO]] |
| Representación contextual | Vector calculado en función del contexto de una entrada | [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] |
| Autosupervisión | Objetivos de aprendizaje construidos desde los propios datos | [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] |
| Logits | Puntajes antes de normalizarlos como probabilidades | [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] |
| Entropía cruzada | Pérdida que, con objetivos categóricos, penaliza la baja probabilidad del objetivo observado | [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] |
| Perplejidad | Exponencial de la pérdida promedio por token con logaritmos naturales | [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] |

Esta ampliación reúne términos de Bishop, Murphy, Alammar y Grootendorst, y Raschka; las notas enlazadas indican las páginas consultadas. La definición resumida sirve para recordar; el ejemplo de cada nota explica el mecanismo.

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Qué diferencia hay entre z y theta?
> z es una variable latente inferida o muestreada para los datos; theta representa parámetros aprendidos del modelo.

> [!question]- ¿Muestrear es tomar siempre la opción más probable?
> No. El muestreo elige según una distribución; tomar siempre el máximo es una estrategia diferente.

> [!question]- ¿Ventana de contexto y dimensión de embeddings son lo mismo?
> No. Una mide cantidad de tokens de contexto; la otra cantidad de coordenadas de los vectores.

> [!question]- ¿Dar tres ejemplos en el prompt es ajuste fino?
> No si no se actualizan los pesos. Es uso de ejemplos en contexto.


> [!question]- ¿MAP es lo mismo que posterior predictiva?
> No. MAP elige un valor del parámetro; la posterior predictiva describe resultados nuevos integrando sobre su incertidumbre.
