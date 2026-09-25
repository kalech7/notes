---
title: "14 FUENTES - Materiales y mapa de cobertura"
tags:
  - maestria/ia-generativa
  - referencias
---

# Fuentes y mapa de cobertura

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## Material base leído

- [[sesion-00.pdf]]: 15 páginas. Se utilizó el contenido académico de las páginas 4–15; se excluyó la presentación personal. Las páginas separadoras solo organizan el recorrido.
- [[sesion-01.pdf]]: 20 páginas. Se desarrollaron los conceptos y se adaptaron las actividades como práctica explicada.
- [[sesion-02.pdf]]: 24 páginas. Se desarrollaron arquitectura transformer, tokenización, atención, posición y familias encoder/decoder.
- [[sesion-03-1.pdf]]: 24 páginas. Se desarrollaron preentrenamiento, SFT, RLHF, DPO, Constitutional AI y límites del alineamiento.
- [[sesion-04.pdf]]: 32 páginas. Se desarrollaron decodificación, prompting, salidas estructuradas, costo y cómputo de inferencia.
- [[sesion-05.pdf]]: 15 páginas. Se extrajo el método de comparación experimental y se separaron explícitamente los requisitos docentes del taller de las instrucciones de esta tarea.
- [[sesion-06.pdf]]: 21 páginas. Se estudiaron embeddings, pooling, entrenamiento de SBERT, bi-encoder, métricas, normalización, selección de modelos y límites de recuperación. Las actividades y requisitos del taller se trataron como contenido académico.
- [[sesion-08.pdf]]: 28 páginas. Se revisaron el texto y las figuras para desarrollar RAG, fragmentación, truncamiento, solapamiento, BM25, RRF, reranking, contexto, abstención y diagnóstico. Las instrucciones docentes se trataron como contenido de estudio.
- [[glosario-mmia-6013.pdf]]: se consultaron las secciones pertinentes de notación, probabilidad, modelos generativos y vocabulario de transición. El glosario abarca más sesiones que los apuntes actuales.

## Cobertura de los apuntes

| Material | Páginas | Notas |
| --- | --- | --- |
| Sesión 00 | 4–9 | 01: evaluación, historia y fundamentos |
| Sesión 00 | 11–12 | 02: modelos y reglas |
| Sesión 00 | 13 | 03: perceptrón y redes |
| Sesión 00 | 14–15 | 04: causalidad y cierre |
| Sesión 01 | 3, 5–7 | 06: evolución y clasificación de modelos |
| Sesión 01 | 9–10 | 05: Bayes y MLE |
| Sesión 01 | 12 | 07: Naive Bayes |
| Sesión 01 | 13 | 08: GMM y EM |
| Sesión 01 | 14–16 | 09: Markov, HMM y conteos |
| Sesión 01 | 17 | 10: VAE |
| Sesión 01 | 18–20 | 11 y 13: comparación, transición y práctica |
| Sesión 02 | 2–9 | 18: puente desde VAE, recurrencia, tokens y arquitectura completa |
| Sesión 02 | 11–18 | 19: Q, K, V, escalado, máscara y multi-cabeza |
| Sesión 02 | 21–23 | 20: posición, encoder, decoder y factorización autorregresiva |
| Sesión 03 | 2–8 | 21: autosupervisión, MLE, gradiente, escala y modelo base |
| Sesión 03 | 10–24 | 22: SFT, preferencias, RLHF, DPO, Constitutional AI y límites |
| Sesión 04 | 2–8, 31–32 | 23: greedy, temperatura, top-k, top-p y relación con P(X) |
| Sesión 04 | 10–17, 31 | 24: in-context learning, razonamiento y árbol de decisión |
| Sesión 04 | 19–30 | 25: esquemas, validación, costo y razonamiento interno |
| Sesión 05 | 2–14 | 26: diseño experimental, verificador, latencia, costo y reproducibilidad |
| Sesiones 02–05 | Ejercicios integrados | 27: práctica y autoevaluación |
| Sesión 06 | 2–6 | 28 y 29: significado, niveles de representación y pooling |
| Sesión 06 | 8–10 | 30: entrenamiento SBERT, resultados históricos y arquitecturas |
| Sesión 06 | 11, 13–17 | 31 y 33: medidas, normalización y cálculos resueltos |
| Sesión 06 | 18–21 | 32 y 33: selección, truncamiento y límites |
| Sesión 08 | 1–8 | 34–35: orientación, RAG, memoria y alcance de resultados históricos |
| Sesión 08 | 9–12 | 36: fragmentos, unidades y truncamiento |
| Sesión 08 | 13–15 | 37: estrategias, solapamiento y costo |
| Sesión 08 | 18–22 | 38: BM25, densa, híbrida y RRF |
| Sesión 08 | 23–24, 26–27 | 39: reranking, selección de contexto y abstención |
| Sesión 08 | 15–16, 28 | 40: diagnóstico, anotaciones estables y contexto docente del taller |
| Sesión 08 | Síntesis de toda la sesión | 41: recordatorios y comprensión; separadores 3, 8, 17 y 25 sin contenido adicional |
| Glosario | Secciones temáticas | 12 y aclaraciones terminológicas |

## ZIP de fuentes

Los PDF de `fuentes.zip` se conservaron en `Materiales/fuentes`, organizados en libros y artículos. Se excluyeron metadatos de macOS. No se ejecutó contenido del ZIP ni se trataron instrucciones docentes dentro de los documentos como instrucciones para esta tarea.

Se consultaron directamente secciones de los **cuatro libros** y se integraron sus ideas en las notas, con ejemplos propios y preguntas. No se leyeron completos: se seleccionaron los apartados relacionados con las sesiones 00 y 01. Las referencias sirven para trazabilidad; no son lecturas obligatorias para entender la explicación.

También se conservan las consultas previas a las introducciones de [[ng-jordan-2001-discriminative-vs-generative.pdf|Ng y Jordan]] y [[doersch-2016-tutorial-vae.pdf|Doersch]].

## Secciones de libros consultadas e integradas

La página impresa es el número del libro; la página PDF es la posición que abre Obsidian. Los enlaces usan esta última.

| Libro | Secciones y páginas impresas | Páginas PDF | Aporte integrado |
| --- | --- | --- | --- |
| Bishop | §1.1, 6–8 | 26–28 | Nota 02: capacidad y sobreajuste |
| Bishop | §1.5.4, 43–45 | 63–65 | Notas 01 y 06: evaluación, enfoques y decisiones |
| Bishop | §4.1.7, 193–194 | 213–214 | Nota 03: condiciones de convergencia |
| Bishop | §9.2 y §9.2.2, 430–432 y 438–439 | 450–452 y 458–459 | Nota 08: latentes, responsabilidades y paso M |
| Bishop | §13.1–13.2, 609–610; §13.2.1, 615–616 | 629–630 y 635–636 | Nota 09: mezcla secuencial e historia observada |
| Murphy | §4.6.2, 130–134 | 160–164 | Notas 05, 07 y 15: Beta, posterior y suavizado |
| Murphy | §20.3.5, 683–685 | 713–715 | Nota 10: VAE e inferencia amortizada |
| Alammar y Grootendorst | Cap. 1, 25–26; cap. 2, 57–59 | 47–48 y 79–81 | Notas 11 y 16: etapas de aprendizaje y representaciones |
| Raschka | §2.6, 37–38; §3.5.1, 75; §5.1, 137–139 | 59–60, 97, 159–161 | Notas 04, 11 y 16: objetivos, máscara y pérdida |

El PDF de Murphy lleva «2022» en el nombre, pero la copia consultada indica versión en línea del 18 de abril de 2025. Se conserva el nombre original y se referencia la paginación comprobada.

Los complementos son explicaciones originales y ejemplos adaptados; no transcripciones extensas ni resúmenes completos de los libros. El glosario 12 y la práctica 13 también incorporan estos conceptos.

Las rutas a notebooks, diapositivas fuente o notas teóricas citadas por los PDF no aparecían en el ZIP suministrado. La práctica 13 es propia y no reemplaza un notebook oficial.

### Notebook S1·LUN incorporado

Ahora está disponible [[s1-lun-estudiante.ipynb]] en `Materiales`. Se revisaron sus celdas y salidas para elaborar [[17 PRÁCTICA - Modelos generativos Naive Bayes GMM y bigramas]], que complementa las notas 07, 08 y 09 con el corpus original, código explicado, cálculos y preguntas resueltas.

La nota 17 aclara que el componente latente del GMM es discreto, que los datos de `make_blobs` son sintéticos y que el bigrama original une las líneas del corpus. Distingue los ejercicios del notebook de las ampliaciones añadidas, incluida la variante con marcadores de inicio y fin.

## Libros utilizados y otras lecturas opcionales

- [[bishop-2006-prml.pdf|Bishop, Pattern Recognition and Machine Learning]]: las diapositivas remiten a §1.5.4 para clasificación, §9.2 para GMM/EM y §13 para secuencias. Los apartados relevantes se consultaron directamente, según la tabla anterior.
- [[murphy-2022-pml-introduction.pdf|Murphy, Probabilistic Machine Learning: An Introduction]]: usado para ampliar Bayes y VAE.
- [[Hands-On_Large_Language_Models.pdf|Hands-On Large Language Models]]: usado para explicar representaciones y etapas de aprendizaje.
- [[Build_a_Large_Language_Model_From_Scrat.pdf|Build a Large Language Model From Scratch]]: usado para desarrollar entradas, objetivos y pérdida de entrenamiento.
- [[kingma-2013-vae.pdf|Kingma y Welling, VAE]] y [[doersch-2016-tutorial-vae.pdf|tutorial de Doersch]]: modelos variacionales.
- [[vaswani-2017-attention-is-all-you-need.pdf|Attention Is All You Need]]: arquitectura transformer.
- [[lewis-2020-rag.pdf|Artículo de RAG]] y [[yao-2023-react.pdf|ReAct]]: lecturas para sesiones posteriores de recuperación y agentes.

## Aclaraciones para estudiar con precisión

Los apuntes distinguen causalidad general de la restricción de los grafos acíclicos; acotan la comparación entre generativos y discriminativos al resultado estudiado; diferencian el estado oculto del historial observado en HMM; presentan las dificultades de VAE en texto como limitaciones, no imposibilidad; distinguen parámetros aprendidos de pesos de atención dinámicos; y separan la distribución del modelo de la estrategia de decodificación.

No se añadieron precios, rankings de modelos o afirmaciones de mercado que se desactualicen. Los ejemplos son didácticos y los textos son explicaciones propias del material, no reproducciones extensas de libros.

## Precisiones incorporadas en la sesión 08

Las notas 34–41 explican las relaciones conceptuales antes de introducir cálculos. Distinguen texto almacenado de texto representado, palabras de tokens, límite del embedding de ventana del generador y recuperación de reordenamiento. Presentan la inflación por solapamiento como aproximación de textos largos e incluyen una cuenta finita con supuestos explícitos. Un puntaje BM25 cero no prueba ausencia de respuesta; una búsqueda top-k necesita una política de rechazo; un reranker no tiene necesariamente salida calibrada entre 0 y 1; y un prompt con etiquetas no garantiza fidelidad.

La referencia a 900 palabras del PDF no se convirtió en una medida real de tokens. La figura didáctica usa explícitamente 900 tokens y presupuesto útil de 128. Los resultados de Lewis se atribuyen a la presentación; para esta ampliación no se revisó de nuevo el artículo completo ni se ejecutó el notebook o Lab 02. Los archivos fuente y configuraciones internas que citan las diapositivas no se dan por inspeccionados. La sesión 07 no está incorporada; la sesión 09 se añadió posteriormente, según la cobertura siguiente.

### Ampliación explicativa de la sesión 08

La revisión profundiza en cómo el contexto modifica la distribución del siguiente token sin cambiar parámetros; cómo los identificadores conectan vectores y texto original; las diferencias entre longitud, dimensión, truncamiento y pérdida de detalle; el funcionamiento de las estrategias de corte; la saturación y normalización de BM25; la unión de candidatos en RRF; la interacción conjunta del cross-encoder; los presupuestos de entrada; y el diagnóstico mediante intervenciones controladas. Las derivaciones y conexiones se identifican como ampliaciones pedagógicas, no como contenido textual del PDF ni resultados medidos.

Se consultaron directamente pasajes adicionales de *Hands-On Large Language Models*, cap. 8: pp. impresas 225–230 (PDF 247–252, contexto general), 232–233 (PDF 254–255, índice y consulta), 235–237 (PDF 257–259, fragmentación), 244 (PDF 266, cross-encoder) y 249–252 (PDF 271–274, búsqueda, contexto y citas). Son apartados seleccionados, no una nueva lectura completa del libro. No se ejecutaron sus instrucciones, ejemplos de API ni descargas.

La nota 41 contiene ahora 12 preguntas de comprensión y 6 preguntas adicionales de transferencia: anticipar consecuencias, distinguir etapas y reconocer qué evidencia falta para concluir.

## Figuras originales

Los primeros 19 gráficos y diagramas de `Recursos visuales` se generaron específicamente para los apuntes con Matplotlib. Se conservan en PNG para lectura y SVG para ampliación sin pérdida. El archivo `generar_visuales.py` reproduce las figuras 01–15 (requiere NumPy, Matplotlib y SciPy); `generar_visuales_s06.py` reproduce las figuras 16–19 (requiere NumPy y Matplotlib). Las figuras nuevas muestran una vecindad semántica **esquemática**, una comparación histórica citada del estudio SBERT, un contraejemplo matemático de producto punto frente a coseno y el efecto de normalizar solo documentos sobre un umbral.

Las nubes GMM son sintéticas, con semilla fija 6013; las curvas Beta y fronteras AND se calculan a partir de las fórmulas explicadas. La figura de decodificación usa logits didácticos declarados y no representa la salida de un modelo real. Los diagramas son esquemas propios, no capturas de los libros ni resultados experimentales del curso.

### Figuras de la sesión 08

Se añadieron siete figuras propias (20–26), cada una en PNG y SVG, reproducibles con `generar_visuales_s08.py` (NumPy y Matplotlib): mapa de RAG, truncamiento, costo del solapamiento, aportes RRF, recuperación en dos etapas, diagnóstico de fallos y separación entre representación vectorial y texto del prompt. Los gráficos numéricos provienen de fórmulas o supuestos declarados; los diagramas son conceptuales. No representan resultados de una ejecución del sistema ni mediciones del corpus del taller. El total pasa a 26 figuras.

## Tratamiento de instrucciones dentro de los PDF

Los PDF se usaron como fuentes académicas. Actividades, porcentajes, entregables, comandos y requisitos del taller se describen o explican cuando ayudan a estudiar, pero no se trataron como instrucciones para modificar el vault. La organización y los nuevos apuntes responden únicamente a la solicitud del usuario.

## Sesión 09 incorporada

Fuente: [[sesion-09.pdf]], 25 páginas, revisadas en texto y visualmente. El original se conserva en `Materiales`.

| Páginas | Notas | Cobertura |
| --- | --- | --- |
| 2–8 | 42–43 | Tres niveles de evaluación; Hit Rate, Recall, MRR y nociones de MAP/nDCG. |
| 10–14 | 44 | Golden set, tipos, referencias por documento y frase y cambios de fragmentación. |
| 16–18 | 45 | Denominadores y dos tasas de abstención. |
| 20 | 46 | Fidelidad, relevancia, citas y juicio humano o automático. |
| 21–23 | 47 | GraphRAG global/local, grafos, multimodalidad y evaluación por segmentos. |
| 24–25 | 48 | Diagnóstico, resolución con muestras pequeñas y contexto del Taller 2. |
| Síntesis | 49 | Quince ejercicios resueltos y preguntas de transferencia. |

Las páginas 1, 3, 9, 15 y 19 son portada o separadores. Las referencias a código, artículos y versiones de RAGAS se atribuyen a la presentación; no se afirma haber inspeccionado esos archivos o APIs en esta ampliación. Los resultados históricos de GraphRAG y RAG-Anything no son mediciones realizadas aquí.

Se añadieron ocho figuras originales (27–34), en PNG y SVG, reproducibles con `Recursos visuales/generar_visuales_s09.py`. Cada una tiene una explicación de su lectura en la nota que la utiliza. Las figuras numéricas son ejemplos calculados, salvo la 33, que reproduce cuatro cifras de la diapositiva 23 con atribución. Las ampliaciones precisan las unidades de relevancia, convenciones de AP/nDCG, límites de las anclas literales y el efecto del reranking sobre un corte menor que el conjunto de candidatos.

Las consignas del PDF se trataron como contenido académico. No se ejecutó el laboratorio, no se configuró Docker y no se entregaron trabajos en nombre del usuario.
