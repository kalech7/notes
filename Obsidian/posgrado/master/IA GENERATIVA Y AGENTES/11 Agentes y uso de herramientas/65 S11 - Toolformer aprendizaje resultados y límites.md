---
title: "65 S11 - Toolformer aprendizaje resultados y límites"
sesion: "11"
fecha: 2026-09-28
tags:
  - maestria/ia-generativa
  - agentes
  - herramientas
fuente: "[[sesion-11.pdf]]"
---

# 65 S11 - Toolformer aprendizaje resultados y límites

[[59 S11 - Guía para entender agentes y herramientas|Guía de la sesión 11]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[64 S11 - Memoria contexto y costo de repetir el historial]]

Siguiente: [[66 S11 - Límites trazas y laboratorio del bucle]]

## 1. Qué pregunta intenta responder Toolformer

En vez de programar manualmente para cada ejemplo dónde debe ir una llamada, Toolformer explora si un modelo puede generar llamadas candidatas y aprender de aquellas cuyos resultados ayudan a predecir texto.

Es un método de ajuste fino presentado por Schick y colaboradores en 2023. El modelo aprende cuándo introducir una llamada, qué herramienta seleccionar y qué argumentos escribir. El artículo local trabaja con GPT-J de 6,7 mil millones de parámetros y cinco tipos de herramientas: preguntas factuales, búsqueda BM25 en Wikipedia, calculadora, calendario y traducción.

Que una herramienta use otro modelo también cuenta: una herramienta se define por su interfaz y operación externa, no por estar implementada con reglas simples. En ese estudio, la herramienta de calendario devuelve la fecha actual; no es un calendario de reuniones que permita crear eventos.

## 2. El proceso de entrenamiento paso a paso

![[46-s11-toolformer-aprendizaje.png]]

**Cómo leerlo:** la fila superior propone y ejecuta llamadas. La inferior filtra los ejemplos y termina modificando los parámetros. No es el bucle de un asistente resolviendo la tarea de un usuario; es la preparación de datos de entrenamiento y el ajuste posterior.

1. Se parte de texto y de unas pocas demostraciones escritas para cada API.
2. El modelo propone posiciones y llamadas candidatas dentro del texto.
3. Un programa ejecuta las llamadas y obtiene sus respuestas.
4. Se calcula si disponer de la llamada y de su respuesta facilita predecir los tokens siguientes.
5. Se conservan las llamadas útiles y se construye un corpus aumentado.
6. Se ajusta el modelo sobre ese corpus con un objetivo de modelado del lenguaje.

**«Autosupervisado» no significa ausencia total de intervención humana.** Hay herramientas diseñadas por personas y unas pocas demostraciones iniciales. La señal para filtrar millones de candidatos se deriva de la propia pérdida del modelo, sin etiquetar manualmente cada llamada útil.

## 3. Qué se mide al decir que una llamada «ayuda»

La pérdida de predicción penaliza que el modelo asigne baja probabilidad al texto observado. En una ilustración de un solo token, $-\log(0.1)\approx2.30$ y $-\log(0.8)\approx0.22$. Dar más probabilidad al token correcto reduce esa pérdida. El filtro real utiliza varios tokens y pesos, no solo un token.

La sección 2 compara:

- $L^{+}$: pérdida con llamada y resultado.
- $L^{-}$: el mínimo entre la pérdida sin llamada y la pérdida con la llamada pero sin resultado.

Conserva la llamada si:

$$L^{-}-L^{+}\geq\tau_f.$$

$\tau_f$ es el umbral de mejora requerido. Tomar el mínimo obliga a superar el mejor de los dos escenarios de control, evitando atribuir al resultado una mejora que ya aportaba la forma de la pregunta.

**Cuenta didáctica:** sin llamada la pérdida es 2.0; con llamada sin resultado es 1.8; con resultado es 0.9. Entonces $L^-=1.8$ y la mejora es $1.8-0.9=0.9$. Si $\tau_f=0.5$, pasa el filtro. Si otra llamada deja $L^+=1.5$, mejora solo 0.3 y se descarta.

Estos números son inventados para entender la regla. No son mediciones del artículo ni significan que el resultado sea verdadero. Un texto que reduce pérdida según el corpus no equivale automáticamente a una acción conveniente en cualquier tarea del mundo real.

## 4. Entrenamiento e inferencia son fases distintas

Durante entrenamiento se fabrican ejemplos y se actualiza $\theta$. Durante la inferencia posterior, el modelo genera hasta indicar que necesita una respuesta de API; el programa la obtiene, la inserta y continúa la generación.

| Aspecto | Toolformer del artículo | Aplicación de function calling de esta sesión |
| --- | --- | --- |
| Cómo incorpora las herramientas del experimento | Corpus aumentado y ajuste fino | Catálogo y esquemas disponibles en el contexto. |
| ¿Cambia pesos al incorporar ese repertorio? | Sí, en su procedimiento de entrenamiento. | No durante una llamada ordinaria a la aplicación. |
| Quién ejecuta | Un programa externo | Un programa externo. |
| Continuación | Sigue generando tras insertar el resultado | El harness admite nuevas decisiones y llamadas. |

La comparación no implica que los modelos capaces de function calling nunca hayan sido entrenados para ello. Significa que **declarar una herramienta nueva en una aplicación no es, por sí mismo, actualizar los pesos del modelo**.

## 5. Qué muestran los resultados y qué no

![[47-s11-toolformer-resultados.png]]

**Cómo leerlo:** compara las dos barras de cada fila, no filas entre sí. En matemáticas, el comparador es el mismo Toolformer con llamadas desactivadas; en LAMA y QA es GPT-3; en árabe es GPT-J sin ajustar. Cambiar el comparador cambia la pregunta experimental.

### Completar hechos: LAMA, tabla 3

| Subconjunto | Toolformer | GPT-3, 175 B | Diferencia en puntos |
| --- | --- | --- | --- |
| SQuAD | 33.8 | 26.8 | +7.0 |
| Google-RE | 11.5 | 7.0 | +4.5 |
| T-REx | 53.5 | 39.8 | +13.7 |

En ese protocolo se desactiva la búsqueda en Wikipedia para evitar una ventaja por el origen de los enunciados; la herramienta factual sigue disponible. El criterio de acierto permite encontrar la palabra correcta entre las cinco primeras palabras generadas. No es una medida universal de «inteligencia».

### Matemáticas: tabla 4

| Tarea | Toolformer con llamadas | El mismo modelo sin llamadas | Cociente aproximado |
| --- | --- | --- | --- |
| ASDiv | 40.4 | 14.8 | 2.73 |
| SVAMP | 29.4 | 6.3 | 4.67 |
| MAWPS | 44.0 | 15.0 | 2.93 |

Aquí la frase «más del doble» compara herramientas habilitadas frente a deshabilitadas en el modelo ajustado. No significa que todas las tareas mejoren así ni que se haya duplicado su número de parámetros. Para ASDiv, $40.4/14.8\approx2.73$; la diferencia absoluta es 25.6 puntos, una cantidad distinta.

### Pregunta-respuesta: tabla 5

| Conjunto | Toolformer | GPT-3, 175 B |
| --- | --- | --- |
| Web Questions | 26.3 | 29.0 |
| Natural Questions | 17.7 | 22.6 |
| TriviaQA | 48.8 | 65.9 |

En estas tareas se desactiva la herramienta de preguntas factuales, y Toolformer depende principalmente de la búsqueda. La respuesta correcta se busca entre las primeras veinte palabras generadas. Toolformer mejora frente a varios modelos de su tamaño, pero queda debajo de GPT-3 en las tres columnas.

En MLQA con preguntas en árabe y párrafos en inglés, tabla 6, Toolformer alcanza 3.7 frente a 8.2 de GPT-J sin ajustar. Eso no significa que la llamada de traducción por sí sola explique toda la caída: el artículo también discute el efecto del ajuste sobre CCNet y el cambio de distribución. Toolformer sin llamadas obtiene 3.1, por lo que habilitarlas mejora esa variante, aunque no supera al modelo base.

Los números proceden del paper de 2023. No son rankings de modelos vigentes ni resultados de una ejecución propia. Tampoco es justo describir el sistema como «solo 6,7 B»: algunas herramientas dependen de sistemas externos cuya capacidad forma parte del resultado.

## 6. Por qué el curso lo usa como contraejemplo

En la evaluación descrita en §4.2 se permite como máximo una llamada por entrada para evitar repetición indefinida. La sección 7 reconoce que el método presentado no enseña a encadenar herramientas ni a usarlas interactivamente para refinar una búsqueda según su resultado.

Bajo la definición de agente de la sesión, falta ese control iterativo que vuelve a elegir a partir de observaciones. No falta toda elección: sí selecciona herramienta, momento y argumentos. La conclusión adecuada es «no cumple el bucle operativo que estamos estudiando», no «jamás toma decisiones».

La restricción experimental de una llamada no es una ley física de la arquitectura ni impide que otro sistema amplíe el procedimiento. También conviene distinguir datos de entrenamiento, que pueden incorporar varias llamadas en un texto, de la restricción durante esa evaluación.

## 7. Conexión con RAG

Si el modelo puede decidir cuándo invocar una búsqueda, la recuperación se vuelve una acción disponible. El buscador BM25 de Toolformer enlaza con [[38 S08 - Búsqueda léxica densa y fusión RRF]]. Un bucle posterior podría observar resultados insuficientes y reformular; esa capacidad interactiva es precisamente una limitación señalada en el artículo.

**Fuentes:** [[sesion-11.pdf#page=19|pp. 19–22]]; consulta directa de [[schick-2023-toolformer.pdf#page=2|§2–4, pp. PDF 2–7]], tablas 3–6 y [[schick-2023-toolformer.pdf#page=11|§7, p. PDF 11]]. [Ficha del artículo original en arXiv](https://arxiv.org/abs/2302.04761). Las derivaciones numéricas son explicaciones propias.
