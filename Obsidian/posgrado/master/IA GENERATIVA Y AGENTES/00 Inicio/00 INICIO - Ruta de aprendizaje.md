---
title: "IA generativa y agentes - Ruta de aprendizaje"
tags:
  - maestria/ia-generativa
aliases:
  - IA generativa y agentes
---

# IA generativa y agentes: empieza aquí

Este conjunto cubre las sesiones 00 a 14 de los materiales disponibles. Las notas avanzan desde qué es un modelo hasta transformer, preentrenamiento, alineamiento, inferencia, prompting, evaluación experimental, embeddings y RAG: fragmentación, recuperación, construcción del contexto, evaluación y patrones avanzados; y agentes, uso de herramientas, memoria, control del bucle, ReAct, Reflexion, planificación y diseño del toolset. La sesión 07 añade búsqueda exacta, IVF, HNSW y bases vectoriales antes de RAG.

**Alcance de «agentes»:** la introducción está en [[11 S01 - Del bigrama al LLM y primeros conceptos de agentes]]. La sesión 11 desarrolla PEAS, selección y ejecución de herramientas, memoria, Toolformer, límites y trazas en [[59 S11 - Guía para entender agentes y herramientas]]. La sesión 12 incorpora ReAct, Reflexion, Plan-and-Execute, verificadores, diagnóstico de trazas y contratos de herramientas en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]]. La sesión 13 desarrolla MCP, catálogo, adaptación, descubrimiento y casos de uso en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|Guía de la sesión 13]]. La sesión 14 añade supervisor, handoff, paralelismo, LangGraph, presupuestos, inyección indirecta y observabilidad en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|el índice de S14]]. La evaluación integral de agentes conserva el alcance de las sesiones posteriores.

> [!tip] Cómo estudiar
> Lee primero la situación concreta, sigue el gráfico y después relaciona cada símbolo con el ejemplo. Al final de cada nota responde las preguntas sin abrir las soluciones. Usa [[27 PRÁCTICA - Sesiones 02 a 05]] para comprobar la segunda mitad del recorrido.

## Mapa visual

Abre [[Mapa de IA generativa y agentes.canvas|Mapa de IA generativa y agentes]] para recorrer las conexiones entre fundamentos, embeddings, índices, RAG y agentes. El mapa específico de RAG y sus dos etapas está en [[34 S08 - Guía para entender fragmentación y recuperación]].

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

- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/00 Índice - Prácticas de la semana 3|Prácticas de la semana 3: lunes, martes y miércoles]], con originales, notebooks resueltos y explicaciones del código.
- [[13 PRÁCTICA - Repaso integrado y ejercicios resueltos|Repaso de sesiones 00 y 01]].
- [[17 PRÁCTICA - Modelos generativos Naive Bayes GMM y bigramas|Notebook de Naive Bayes, GMM y bigramas]].
- [[26 S05 - Diseñar una comparación de modelos|Cómo comparar modelos con un experimento controlado]].
- [[27 PRÁCTICA - Sesiones 02 a 05|Ejercicios resueltos de transformer, alineamiento, inferencia y evaluación]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/95 PRÁCTICA - Notebook del lunes resuelto y explicado|Lunes: el bucle de herramientas resuelto y explicado]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/96 PRÁCTICA - Notebook del martes resuelto y explicado|Martes: trazas, límites y Mini-Reflexion resueltos y explicados]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/94 PRÁCTICA - Notebook del miércoles grafos checkpoints y MCP|Notebook del miércoles: grafos, checkpoints y MCP]], con una copia resuelta ejecutable, diagramas y resultados verificados.

## 7. Embeddings y recuperación semántica

1. [[28 S06 - Qué es un embedding y qué significa cercanía|Qué representa un embedding y qué quiere decir cercanía]].
2. [[29 S06 - De tokens a un vector de texto|Token, salida contextual y pooling]].
3. [[30 S06 - Cómo se entrena SBERT y por qué permite buscar|SBERT, aprendizaje entre textos y bi-encoder]].
4. [[31 S06 - Coseno producto punto y normalización|Coseno, producto punto, distancia y normalización con números]].
5. [[32 S06 - Elegir modelo y reconocer límites|Cómo elegir un modelo y detectar límites de recuperación]].
6. [[33 PRÁCTICA - Embeddings y similitud semántica|Ejercicios resueltos de la sesión 06]].

## 7B. Bases de datos vectoriales — sesión 07

Empieza por [[79 S07 - Guía de búsqueda vectorial e índices]]. Este bloque completa el puente entre embeddings y RAG: cómo organizar vectores, qué se pierde al aproximar y cómo medir el intercambio entre calidad, tiempo y memoria. Incluye seis gráficos explicados y quince ejercicios resueltos.

1. [[80 S07 - Búsqueda exacta aproximación y costo]]
2. [[81 S07 - IVF celdas centroides y nprobe]]
3. [[82 S07 - HNSW capas conexiones y exploración]]
4. [[83 S07 - Recall del índice latencia y memoria]]
5. [[84 S07 - Colecciones payload filtros y operación]]
6. [[85 S07 - Ejercicios resueltos de búsqueda vectorial]]

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

## 10. Taller RAG medible — sesión 10

Empieza por [[50 S10 - Guía para comprender el taller RAG|la guía de la sesión 10]]. Nueve notas conectan el funcionamiento del sistema con el diagnóstico de fallas, seis figuras explicadas, un experimento numérico completo y dieciocho ejercicios resueltos.

1. [[51 S10 - Del documento a una respuesta con evidencia]]
2. [[52 S10 - Ingesta tokens y tres fallas silenciosas]]
3. [[53 S10 - Golden set y límites de lo respondible]]
4. [[54 S10 - Hit Rate y MRR con un experimento completo]]
5. [[55 S10 - Abstención fidelidad y errores del evaluador]]
6. [[56 S10 - Elegir una extensión y comprobar su efecto]]
7. [[57 S10 - Reproducibilidad entregables y reflexión]]
8. [[58 S10 - Ejercicios resueltos y repaso activo]]

## 11. Agentes y uso de herramientas — sesión 11

Empieza por [[59 S11 - Guía para entender agentes y herramientas|la guía de la sesión 11]]. Nueve notas teóricas desarrollan el mecanismo con un ejemplo continuo de ventas, ocho figuras explicadas, 24 ejercicios resueltos y un simulador local con nueve escenarios verificados. El complemento del notebook del lunes añade los datos originales y una novena figura.

1. [[60 S11 - Chatbot pipeline RAG y agente quién decide]]
2. [[61 S11 - PEAS racionalidad y observación parcial]]
3. [[62 S11 - Function calling y bucle del agente paso a paso]]
4. [[63 S11 - Diseñar herramientas esquemas y validación]]
5. [[64 S11 - Memoria contexto y costo de repetir el historial]]
6. [[65 S11 - Toolformer aprendizaje resultados y límites]]
7. [[66 S11 - Límites trazas y laboratorio del bucle]]
8. [[67 S11 - Ejercicios resueltos y repaso activo]]

## 12. Patrones de agentes y diseño del toolset — sesión 12

Empieza por [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]]. Diez notas de la sesión 12 y una práctica explicativa del lunes desarrollan tres patrones, fallas de trazas, presupuestos, verificadores y contratos de herramientas. Incluyen ocho figuras explicadas, 24 preguntas resueltas, un caso integrado y una práctica local determinista verificada.

El lunes está en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/11 Agentes y uso de herramientas/68 S11 - Notebook del lunes explicado y revisado|Notebook del lunes explicado y revisado]]; sus originales y los del martes están en `Materiales`. Las correcciones didácticas se conservan en una práctica complementaria.

- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/70 S12 - ReAct pensamiento acción observación y evidencia|70 S12 - ReAct pensamiento acción observación y evidencia]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/71 S12 - Autopsia de trazas y detector de repetición|71 S12 - Autopsia de trazas y detector de repetición]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/72 S12 - Pasos presupuestos timeouts y condiciones de parada|72 S12 - Pasos presupuestos timeouts y condiciones de parada]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/73 S12 - Reflexion entre intentos memoria y aprendizaje|73 S12 - Reflexion entre intentos memoria y aprendizaje]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/74 S12 - Verificadores fiables y errores del notebook|74 S12 - Verificadores fiables y errores del notebook]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/75 S12 - Plan-and-Execute y elección de patrones|75 S12 - Plan-and-Execute y elección de patrones]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/76 S12 - Toolsets validación errores y límites efectivos|76 S12 - Toolsets validación errores y límites efectivos]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/77 S12 - Laboratorio local y soluciones del martes|77 S12 - Laboratorio local y soluciones del martes]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/78 S12 - Ejercicios resueltos y repaso activo|78 S12 - Ejercicios resueltos y repaso activo]]

## 13. MCP descubrimiento y casos de uso — sesión 13

Empieza por [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|el índice de la sesión 13]]. Nueve notas explican cuándo conviene MCP, host/cliente/servidor, catálogos, adaptadores, versiones, permisos y tres tipos de agentes. Incluyen siete figuras reproducibles, cuatro diagramas Mermaid, veinte preguntas resueltas y un simulador local verificado. Se contrastó la revisión 2026-07-28 con documentación oficial.

- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/86 S13 - Cuándo conviene MCP y la cuenta de integraciones|86 S13 - Cuándo conviene MCP y la cuenta de integraciones]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/87 S13 - Host cliente servidor y descubrimiento|87 S13 - Host cliente servidor y descubrimiento]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/88 S13 - Catálogo adaptador y function calling|88 S13 - Catálogo adaptador y function calling]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/89 S13 - Mensajes transportes y versiones de MCP|89 S13 - Mensajes transportes y versiones de MCP]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/90 S13 - Confianza permisos costo y límites|90 S13 - Confianza permisos costo y límites]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/91 S13 - Agentes analistas de código y de investigación|91 S13 - Agentes analistas de código y de investigación]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/92 S13 - Laboratorio local de descubrimiento y extensión B|92 S13 - Laboratorio local de descubrimiento y extensión B]]
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/93 S13 - Ejercicios resueltos y repaso activo|93 S13 - Ejercicios resueltos y repaso activo]]

## 14. Multiagente, LangGraph y robustez — sesión 14

Empieza por [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|el índice de S14]]. Once notas temáticas y su índice explican topologías, evidencia histórica, estado y reductores, pausas, presupuestos, permisos e inyección indirecta, y LangChain/LangGraph/LangSmith. Incluyen nueve gráficos con explicación, cinco diagramas Mermaid, 18 preguntas resueltas y un notebook local con 17 comprobaciones.

El cierre práctico está en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/107 S14 - Notebook del jueves laboratorio y repaso resuelto|notebook del jueves y repaso]]. La revisión de fuentes distingue resultados docentes, cifras de 2023 y la simulación propia: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/17 FUENTES - Sesión 14 tutorial y robustez|fuentes y validación de S14]].

## Revisión de calidad y límites

La [[15 REVISIÓN - Calidad cobertura y claridad 2026-09-29|revisión de todas las notas del curso]] registra las correcciones, las comprobaciones y los materiales no disponibles. La incorporación posterior de MCP está en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/16 FUENTES - Sesión 13 MCP y validación|revisión de S13]]. La incorporación de robustez y coordinación está en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/17 FUENTES - Sesión 14 tutorial y robustez|la revisión de S14]]. La cobertura se refiere a estas quince sesiones; los libros completos, los laboratorios no recibidos y las sesiones posteriores tienen un alcance diferente.

## 15. Referencias

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
07B Bases de datos vectoriales/
08 RAG fragmentación y recuperación/
09 Evaluación de RAG y patrones avanzados/
10 Taller RAG medible/
11 Agentes y uso de herramientas/
12 Patrones de agentes y diseño del toolset/
13 MCP descubrimiento y casos de uso/
14 Multiagente LangGraph y robustez/
90 Referencias/
Materiales/
Recursos visuales/
talleres/
```

Los PDF originales se conservan en `Materiales`. Los gráficos propios están en `Recursos visuales` en PNG y SVG. Los requisitos de evaluación encontrados en las sesiones se explican como contenido del curso; no se trataron como instrucciones para modificar estas notas.
