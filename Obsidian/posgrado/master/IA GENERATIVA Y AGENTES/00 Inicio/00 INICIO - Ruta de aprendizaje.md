---
title: "IA generativa y agentes - Ruta de aprendizaje"
tags:
  - maestria/ia-generativa
aliases:
  - IA generativa y agentes
---

# IA generativa y agentes: empieza aquí

Este conjunto cubre las sesiones 00 a 06 y las sesiones 08 y 09. Las notas avanzan desde qué es un modelo hasta transformer, preentrenamiento, alineamiento, inferencia, prompting, evaluación experimental, embeddings y RAG: fragmentación, recuperación, construcción del contexto, evaluación y patrones avanzados. La sesión 07 no está incorporada en los materiales actuales.

**Alcance de «agentes»:** por ahora hay una introducción en [[11 S01 - Del bigrama al LLM y primeros conceptos de agentes]]. Las sesiones disponibles todavía no desarrollan en profundidad planificación, uso de herramientas ni evaluación de agentes.

> [!tip] Cómo estudiar
> Lee primero la situación concreta, sigue el gráfico y después relaciona cada símbolo con el ejemplo. Al final de cada nota responde las preguntas sin abrir las soluciones. Usa [[27 PRÁCTICA - Sesiones 02 a 05]] para comprobar la segunda mitad del recorrido.

## Mapa visual

Abre [[Mapa de IA generativa y agentes.canvas|Mapa de IA generativa y agentes]] para recorrer las conexiones iniciales entre temas. El mapa específico de RAG y sus dos etapas está en [[34 S08 - Guía para entender fragmentación y recuperación]].

## El hilo conductor en seis preguntas

| Pregunta | Idea que debes poder explicar | Nota de partida |
| --- | --- | --- |
| ¿Qué aprende un modelo entrenable? | Ajusta parámetros con datos para mejorar una tarea; acertar en ejemplos nuevos importa más que memorizar el entrenamiento. | [[02 S00 - Reglas modelos y aprendizaje desde datos]] |
| ¿Cómo representa incertidumbre? | Una distribución asigna probabilidades a posibilidades; Bayes actualiza una creencia al observar datos. | [[05 S01 - Probabilidad y teorema de Bayes paso a paso]] |
| ¿Cómo produce texto un LLM autorregresivo? | Calcula una distribución del siguiente token a partir del prefijo y repite el proceso. | [[11 S01 - Del bigrama al LLM y primeros conceptos de agentes]] |
| ¿De dónde sale esa distribución? | El transformer procesa tokens y contexto; el entrenamiento ajusta sus pesos para predecir los tokens observados. | [[18 S02 - Transformer de extremo a extremo]] y [[21 S03 - Preentrenamiento autosupervisado y MLE]] |
| ¿Qué cambia al pedirle una respuesta? | El prompt aporta contexto y la decodificación selecciona tokens; normalmente los pesos ya están fijos. | [[23 S04 - Greedy temperatura top-k y top-p]] |
| ¿Cómo usa información externa? | Los embeddings ayudan a recuperar textos pertinentes; RAG incorpora esos textos a la respuesta. Un agente puede decidir acciones y revisar sus resultados. | [[28 S06 - Qué es un embedding y qué significa cercanía]] y [[11 S01 - Del bigrama al LLM y primeros conceptos de agentes#7. Dónde encajan RAG y los agentes]] |

Si una fórmula te resulta abstracta, vuelve a la pregunta de su fila: identifica **qué entra, qué se calcula y qué significa el resultado**. Por ejemplo, la atención calcula pesos entre posiciones del texto; esos pesos no son los parámetros que el entrenamiento guarda.

## 1. Fundamentos de IA

1. [[01 S00 - Qué es la IA y cómo evaluar inteligencia|Qué es la IA y cómo comprobar una capacidad]].
2. [[02 S00 - Reglas modelos y aprendizaje desde datos|Qué es un modelo y cómo aprende de ejemplos]].
3. [[03 S00 - Perceptrón redes neuronales y XOR|Cómo una neurona artificial toma una decisión]].
4. [[04 S00 - Correlación causalidad y límites de las predicciones|Por qué predecir no demuestra causalidad]].

## 2. Probabilidad y modelos generativos

1. [[05 S01 - Probabilidad y teorema de Bayes paso a paso|Bayes paso a paso]].
2. [[06 S01 - Modelos discriminativos y generativos|Discriminativo frente a generativo]].
3. [[07 S01 - Naive Bayes con un ejemplo de spam|Naive Bayes]].
4. [[08 S01 - GMM variables latentes y algoritmo EM|GMM y EM]].
5. [[09 S01 - Markov HMM y generación con bigramas|Markov, HMM y bigramas]].
6. [[10 S01 - VAE espacio latente y ELBO|VAE, latente continuo y ELBO]].
7. [[11 S01 - Del bigrama al LLM y primeros conceptos de agentes|Puente hacia LLM y agentes]].

Ampliaciones: [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números|incertidumbre bayesiana]] y [[17 PRÁCTICA - Modelos generativos Naive Bayes GMM y bigramas|práctica con el notebook de modelos generativos]].

## 3. Transformers

1. [[18 S02 - Transformer de extremo a extremo|Pipeline completo del transformer]].
2. [[19 S02 - Atención Q K V paso a paso|Atención Q, K y V con números]].
3. [[20 S02 - Posición familias y decoder-only|Posición, encoder, decoder y decoder-only]].

## 4. Entrenamiento y alineamiento

1. [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto|Ejemplo pequeño: del texto a la pérdida]].
2. [[21 S03 - Preentrenamiento autosupervisado y MLE|Preentrenamiento, MLE, gradientes y perplejidad]].
3. [[22 S03 - SFT RLHF DPO y Constitutional AI|SFT y ajuste por preferencias]].

## 5. Inferencia y prompting

1. [[23 S04 - Greedy temperatura top-k y top-p|Decodificación: greedy, temperatura, top-k y top-p]].
2. [[24 S04 - Zero-shot few-shot y razonamiento|Zero-shot, few-shot y razonamiento]].
3. [[25 S04 - Salidas estructuradas costo y razonamiento interno|JSON, esquemas, costo y test-time compute]].

## 6. Talleres y práctica

- [[13 PRÁCTICA - Repaso integrado y ejercicios resueltos|Repaso de sesiones 00 y 01]].
- [[17 PRÁCTICA - Modelos generativos Naive Bayes GMM y bigramas|Notebook de Naive Bayes, GMM y bigramas]].
- [[26 S05 - Diseñar una comparación de modelos|Cómo comparar modelos con un experimento controlado]].
- [[27 PRÁCTICA - Sesiones 02 a 05|Ejercicios resueltos de transformer, alineamiento, inferencia y evaluación]].

## 7. Embeddings y recuperación semántica

1. [[28 S06 - Qué es un embedding y qué significa cercanía|Qué representa un embedding y qué quiere decir cercanía]].
2. [[29 S06 - De tokens a un vector de texto|Token, salida contextual y pooling]].
3. [[30 S06 - Cómo se entrena SBERT y por qué permite buscar|SBERT, aprendizaje entre textos y bi-encoder]].
4. [[31 S06 - Coseno producto punto y normalización|Coseno, producto punto, distancia y normalización con números]].
5. [[32 S06 - Elegir modelo y reconocer límites|Cómo elegir un modelo y detectar límites de recuperación]].
6. [[33 PRÁCTICA - Embeddings y similitud semántica|Ejercicios resueltos de la sesión 06]].

## 8. RAG: fragmentación y recuperación — sesión 08

Empieza por [[34 S08 - Guía para entender fragmentación y recuperación|la guía de la sesión 08]]. Cada nota desarrolla **qué es, cómo funciona, por qué se necesita y cómo se relaciona con el sistema**. Incluye diagramas, gráficos explicados, mecanismos desarrollados paso a paso y recordatorios. La revisión añade conexiones entre etapas y preguntas para anticipar qué ocurre al cambiar el sistema.

1. [[35 S08 - RAG contexto memoria y generación fundamentada|RAG, memoria y evidencia externa]].
2. [[36 S08 - Fragmentos tokens y truncamiento|Fragmentos, límites y truncamiento]].
3. [[37 S08 - Estrategias de fragmentación y solapamiento|Cómo dividir conservando sentido]].
4. [[38 S08 - Búsqueda léxica densa y fusión RRF|BM25, búsqueda densa e híbrida]].
5. [[39 S08 - Reranking contexto y abstención|Reordenamiento, contexto y abstención]].
6. [[40 S08 - Diagnóstico de fallos y decisiones del taller|Cómo localizar un fallo y justificar cambios]].
7. [[41 S08 - Recordatorio y preguntas de comprensión|Recordatorios y preguntas con respuestas desplegables]].

## 9. Evaluación de RAG y patrones avanzados — sesión 09

Empieza por [[42 S09 - Guía para evaluar un RAG|la guía de la sesión 09]]. Incluye métricas con cuentas paso a paso, ocho gráficos y diagramas explicados, anotación del golden set, abstención, fidelidad, GraphRAG y ejercicios resueltos.

1. [[43 S09 - Hit Rate Recall MRR MAP y nDCG paso a paso]]
2. [[44 S09 - Golden sets anotación y caducidad]]
3. [[45 S09 - Preguntas negativas y abstención]]
4. [[46 S09 - Evaluar respuestas fidelidad y citas]]
5. [[47 S09 - GraphRAG y recuperación multimodal]]
6. [[48 S09 - Diagnóstico experimentos y Taller 2]]
7. [[49 S09 - Ejercicios resueltos y repaso]]

## 10. Referencias

- [[12 GLOSARIO - Diccionario explicado para estas sesiones|Glosario explicado]].
- [[14 FUENTES - Materiales y mapa de cobertura|Fuentes y cobertura por sesión]].

## Estructura de carpetas

```text
00 Inicio/
01 Fundamentos de IA/
02 Modelos probabilísticos y generativos/
03 Transformers/
04 Entrenamiento y alineamiento/
05 Inferencia y prompting/
06 Talleres y práctica/
07 Embeddings y recuperación/
08 RAG fragmentación y recuperación/
09 Evaluación de RAG y patrones avanzados/
90 Referencias/
Materiales/
Recursos visuales/
talleres/
```

Los PDF originales se conservan en `Materiales`. Los gráficos propios están en `Recursos visuales` en PNG y SVG. Los requisitos de evaluación encontrados en las sesiones se explican como contenido del curso; no se trataron como instrucciones para modificar estas notas.
