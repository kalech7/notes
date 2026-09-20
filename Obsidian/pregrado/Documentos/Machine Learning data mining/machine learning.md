**Deep Learning** abarca conceptos de cálculo diferencial. 
**Machine Learning** se fundamenta principalmente en la estadística. 
**Inteligencia artificial** busca hacer todo más inteligente y automatizado, aplicándose en áreas como la robótica.

> [!info] Explicación
> - **Inteligencia Artificial (IA):** Es el campo más amplio que busca crear sistemas capaces de realizar tareas que requieren inteligencia humana (razonamiento, visión, etc.).
> - **Machine Learning (ML):** Es un subcampo de la IA que utiliza algoritmos estadísticos para que las computadoras aprendan de los datos y mejoren con la experiencia sin ser programadas explícitamente.
> - **Deep Learning (DL):** Es una rama del ML basada en redes neuronales artificiales de múltiples capas. Depende fuertemente del cálculo diferencial para ajustar pesos mediante procesos como la retropropagación (backpropagation).

La información (data) es muy importante, ya que funciona como la experiencia a partir de la cual la computadora aprende.
El desempeño (*performance*) mide qué tan correcta y precisa es la predicción del modelo.
La tarea (*task*) es la función específica que el modelo debe realizar.
La experiencia corresponde a los datos históricos usados para entrenar al modelo.

> [!info] Explicación
> Esta definición se alinea con la clásica formulación de Tom Mitchell sobre ML: Un sistema informático aprende de la **Experiencia (E)** con respecto a alguna clase de **Tarea (T)** y medida de rendimiento o **Performance (P)**, si su desempeño en T, medido por P, mejora con la experiencia E.
> *Ejemplo:* En un filtro de spam, la tarea (T) es detectar spam, la experiencia (E) son correos anteriores (datos), y el rendimiento (P) es la precisión de la detección.

Frente a las predicciones basadas en reglas tradicionales, el aprendizaje de máquina consiste en el aprendizaje de una función matemática subyacente que produce un conjunto de resultados. Se divide principalmente en:
1. **Regresión:** Predicción de números continuos o de punto flotante.
2. **Clasificación:** Asignación de una etiqueta discreta o número entero.
3. **Reducción de dimensionalidad:** Simplificación de variables, como en el Análisis de Componentes Principales (PCA).
4. **Proceso de Decisión de Markov (MDP):** Toma de decisiones secuenciales bajo incertidumbre.

> [!info] Explicación
> El ML busca aproximar una función matemática que mapea entradas a salidas. Sus principales aplicaciones son:
> - **Regresión:** Se usa para predecir valores numéricos continuos (ej. predecir el precio de una casa).
> - **Clasificación:** Asigna datos a categorías o clases discretas (ej. identificar si un tumor es benigno o maligno).
> - **Reducción de Dimensionalidad:** Técnicas como PCA (Análisis de Componentes Principales) comprimen la información eliminando variables redundantes, lo que acelera el procesamiento y evita el ruido.
> - **Procesos de Decisión de Markov (MDP):** Base matemática del Aprendizaje por Refuerzo, donde se toman secuencias de decisiones en situaciones de incertidumbre buscando maximizar una recompensa.

## Notas relacionadas
- [[tipos de machine learning]]
- [[Ajuste de modelos]]
- [[modelos de regresion]]
- [[metricas para clasificadores]]
- [[conducta racional]]
