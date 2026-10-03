---
title: "14 FUENTES - Materiales y mapa de cobertura"
tags:
  - maestria/ia-generativa
  - referencias
---

# Fuentes y mapa de cobertura

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

Este es un registro acumulativo: cada apartado conserva el alcance de su incorporación. El estado actual se resume en la [[15 REVISIÓN - Calidad cobertura y claridad 2026-09-29|revisión global del 29 de septiembre]]. La lectura posterior del ZIP del Taller 2 está documentada al final.

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

La referencia a 900 palabras del PDF no se convirtió en una medida real de tokens. La figura didáctica usa explícitamente 900 tokens y presupuesto útil de 128. Los resultados de Lewis se atribuyen a la presentación; para esta ampliación no se revisó de nuevo el artículo completo ni se ejecutó el notebook o Lab 02. Los archivos fuente y configuraciones internas que citan las diapositivas no se dan por inspeccionados. La sesión 07 se incorporó en la auditoría del 29 de septiembre; su cobertura se registra al final de esta nota. La sesión 09 se añadió posteriormente, según la cobertura siguiente.

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


## Sesión 10 incorporada

Fuente principal: [[sesion-10.pdf]], *Taller 2 — Sistema RAG sobre base vectorial*, Daniel Andrés Riofrío Almeida, 26 de septiembre de 2026, 16 páginas. Se revisó el texto completo y la representación visual de las 16 páginas; se amplió la página 5 para leer su tabla. El original se conserva en `Materiales`.

| Páginas | Notas | Cobertura |
| --- | --- | --- |
| 2–5 | 50–51 y 57 | Método baseline, componentes, criterios y evidencias. |
| 7–9 | 52 | Ingesta, tokens, truncamiento y límites de heurísticas. |
| 5, 7 y 10 | 53 | Golden set, anclas y disponibilidad en corpus, índice y contexto. |
| 3, 11 y 13 | 54–55 | Hit Rate, MRR, denominadores, abstención y evaluación de respuestas. |
| 13 | 56 | Hipótesis para fragmentación, híbrida, reranking y evaluación con RAGAS. |
| 14–16 | 57 | Credenciales, reproducibilidad, recursos y puente hacia agentes. |
| Síntesis | 58 | Dieciocho ejercicios con soluciones desplegables. |

Las páginas 1, 6 y 12 son portada y separadores. No se ejecutó el laboratorio ni se inspeccionaron los archivos internos que el PDF cita. Las consignas se trataron como contenido académico, no como instrucciones para instalar, desplegar, publicar o entregar.

Las figuras 35–40 son esquemas y cuentas didácticas originales; se guardan en PNG y SVG y se reproducen con `Recursos visuales/generar_visuales_s10.py` (Pillow). `verificar_ejemplos_s10.py` reproduce las cuentas de los ejemplos sin usar modelos ni API. Los resultados no son mediciones del corpus del usuario.

Precisiones: el umbral de 200 caracteres es heurístico; 128 es el límite del caso del PDF y no universal; 900 palabras no se convierten aquí en un conteo medido de tokens; la ilustración de truncamiento usa 900 tokens y 126 útiles; un sufijo omitido no contribuye directamente al embedding, pero su fragmento puede recuperarse por el prefijo; MRR ≤ Hit Rate exige mismo corte y población; el detector mostrado usa inclusión de cadena; una pregunta puede ser respondible en los originales y no tener evidencia indexada. Se conserva la incertidumbre de la página 16 sobre la continuidad de los talleres.

### Documentación técnica complementaria consultada el 27 de septiembre de 2026

- [Sentence Transformers: configuración del encoder y límite de secuencia](https://www.sbert.net/docs/package_reference/sentence_transformer/model.html?highlight=hub).
- [Sentence Transformers: recuperación y reranking](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html).
- [Qdrant: consultas híbridas y RRF](https://qdrant.tech/documentation/search/hybrid-queries/).
- [RAGAS: fidelidad](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/).
- [RAGAS: relevancia de respuesta](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/answer_relevance/).

Se emplearon para aclarar conceptos, no para atribuir al laboratorio una API o configuración actual no verificada. Las cuentas RRF declaran posiciones desde 1 y c=60 como ejemplo propio; no se presentan como valores por defecto de Qdrant.


## Sesión 11 incorporada

Fuente principal: [[sesion-11.pdf]], *Qué es un agente y uso de herramientas*, Daniel Andrés Riofrío Almeida, 28 de septiembre de 2026, 26 páginas. Se extrajo todo el texto y se revisaron visualmente las 26 páginas. El PDF se conserva sin modificar en `Materiales`.

| Páginas | Notas | Cobertura |
| --- | --- | --- |
| 2, 4–6 | 59–60 | Transición de RAG fijo a herramienta, definición operativa, chatbot, pipeline y agente. |
| 8–11 | 61 y 64 | PEAS, racionalidad, tipos, observación parcial, harness y estado. |
| 13–15 | 62 | Seis pasos, separación entre emisión y ejecución, correspondencia llamada–resultado. |
| 16–17 | 63 | Catálogo, esquema, descripción y validación. |
| 19–22 | 65 | Toolformer, ajuste fino, filtro por pérdida, resultados y limitaciones. |
| 23–24 | 66 | Límite de pasos, simulación, trazas y depuración. |
| 25–26 | 60 y 66 | Taxonomía de divulgación, cierre y contexto del Taller 3. |
| Síntesis | 67 | 24 ejercicios, caso integrado y glosario. |

Las páginas 1, 3, 7, 12 y 18 son portada o separadores. Los archivos internos que el PDF cita no se consideran inspeccionados. Las consignas se trataron como contenido académico; no se ejecutó el notebook docente ni se configuró un servicio externo.

### Fuentes primarias adicionales consultadas

- [[schick-2023-toolformer.pdf]]: §2–4, páginas PDF 2–7, tablas 3–6, y §7, página PDF 11. Lectura directa de la copia local para verificar el filtro, el protocolo, los resultados y la limitación de una llamada en la evaluación. Se contrastó la identidad del artículo con [arXiv](https://arxiv.org/abs/2302.04761).
- [[Hands-On_Large_Language_Models.pdf]]: cap. 7, pp. impresas 209–210, 212, 217–219 (PDF 231–232, 234, 239–241), sobre memoria, cadenas y agentes; se inspeccionaron además PDF 243 y 245 para contexto, sin usar sus firmas de API como documentación vigente.
- [Referencia oficial de objetos en JSON Schema](https://json-schema.org/understanding-json-schema/reference/object): propiedades, campos requeridos y campos adicionales. Consulta el 28 de septiembre de 2026, hora local.

PEAS y la clasificación de agentes se explican con atribución a la presentación, que cita AIMA. No se afirma haber inspeccionado el capítulo de la edición citada por el docente.

### Precisiones de la ampliación

La definición operativa de agente del curso no se presenta como universal. Una herramienta única puede admitir distintas acciones y decisiones; una corrida sin herramientas no determina toda la arquitectura; un enrutador sin retorno no demuestra un bucle. La función de agente depende de pesos, contexto y código. La clasificación del agente LLM como basado en objetivos caracteriza el ejemplo del curso, no limita todos los sistemas con LLM.

«El modelo no tiene memoria» se precisa como ausencia de recuperación automática de conversaciones previas en una llamada básica; el servicio o aplicación pueden gestionar estado. El reenvío completo es una implementación, no una obligación universal. La correspondencia llamada–resultado no implica ejecución de efectos exactamente una vez. La respuesta final tampoco prueba éxito.

En Toolformer se separa generación del corpus, ajuste e inferencia; autosupervisión no significa cero demostraciones humanas. La restricción de una llamada se atribuye al protocolo evaluado. Los puntajes se conservan con tarea, comparador y condiciones. Las cifras no son resultados actuales ni mediciones propias.

### Figuras y laboratorio

Figuras originales 41–48, en PNG y SVG, generadas con `Recursos visuales/generar_visuales_s11.py` (Pillow). Se inspeccionaron las ocho y se corrigieron el margen del gráfico de contexto y el retorno del diagrama de parada. La figura 47 usa cifras históricas del paper local; las demás son esquemas o cálculos didácticos, sin mediciones de LLM.

El archivo [[s11_laboratorio_bucle.py]] usa únicamente biblioteca estándar de Python y datos ficticios en memoria. [[s11_resultados_verificados.json]] conserva la salida de nueve escenarios: éxito, límite, repetición, herramienta desconocida, mes inválido, ausencia de datos, base cero, ID repetido y mensaje mal formado. Comprueba el emparejamiento de llamadas aceptadas con resultados y las cuentas de crecimiento y contexto. Es un simulador por reglas y no mide autonomía ni calidad de un LLM.


## Sesión 12 y notebooks de la semana 3 incorporados

Revisión del 29 de septiembre de 2026, fecha local de Ecuador. Fuente principal: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-12.pdf|sesion-12.pdf]], *Patrones de agentes y diseño del toolset*, Daniel Andrés Riofrío Almeida, 25 páginas. Se extrajo todo el texto, se renderizaron las 25 páginas y se revisaron sus representaciones visuales. Numeración impresa = página PDF (1–25).

Se leyeron completas las 18 celdas de [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/s3-lun-estudiante.ipynb|s3-lun-estudiante.ipynb]] y las 20 de [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/s3-mar-estudiante.ipynb|s3-mar-estudiante.ipynb]], sin salidas guardadas. Ambos originales se copiaron sin cambios desde Descargas a `Materiales`, como los otros cuadernos fuente. El lunes se integra en la sección 11; el martes complementa la 12. Las correcciones están en notas y práctica aparte.

| Fuente / páginas o celdas | Notas | Cobertura |
| --- | --- | --- |
| Lunes, celdas 0–17 | 68 | Dataset, funciones, esquemas, adaptación, historial, errores, ejercicios y taxonomía |
| PDF 1–2 | 69 | Objetivo, vínculo con sesión 11 y vocabulario de la traza |
| PDF 4–8 | 70 | Definición ReAct, contexto, resultados y límites de comparadores |
| PDF 9–10; martes 3–8 | 71–72 | Tres trazas, equivalencia, errores del detector y protecciones |
| PDF 12–14 | 73 | Actor, evaluación, reflexión, memorias y composición con ReAct |
| PDF 15–16; martes 11–15 | 74, 77 | Ablación, calidad del verificador, errores reproducidos y mini-Reflexion |
| PDF 18–19; martes 17–19 | 75 | Plan y ejecución, replanning y clasificación por niveles |
| PDF 21–24 | 76 | Contrato, seis defectos descritos del Lab 03, esquema SQL y límites |
| PDF 25; martes 16 | 69, 77 | Contexto del Taller 3 y reflexión sobre un baseline |
| Síntesis de los tres adjuntos | 78 | 24 preguntas desplegables y un caso de ventas resuelto |

PDF 3, 11, 17 y 20 son separadores; 1 es portada. Las actividades, comandos, porcentajes y requisitos de los documentos se trataron como contenido académico, no como instrucciones para desplegar, entregar, conectarse a servicios ni modificar el laboratorio del curso.

### Fuentes primarias contrastadas y precisiones

- ReAct, copia local [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/fuentes/papers/s3-agentes/yao-2023-react.pdf|yao-2023-react.pdf]]: §2, PDF 3–4; tablas 1–2, PDF 5–6; tabla 3, PDF 8. Se comprobaron números, régimen, denominadores y direcciones de conmutación. Identidad contrastada con [arXiv](https://arxiv.org/abs/2210.03629).
- Reflexion, copia local [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/fuentes/papers/s3-agentes/shinn-2023-reflexion.pdf|shinn-2023-reflexion.pdf]]: §3–4, PDF 3–8; limitaciones, PDF 9. Algoritmo 1 en PDF 4 inspeccionado visualmente: la condición impresa usa `or`, incompatible con la intención de terminar por éxito o máximo; la explicación y la práctica utilizan continuación acotada con `and` o un `for`. Identidad contrastada con [arXiv](https://arxiv.org/abs/2303.11366). La copia local lleva lenguaje de preprint; sus cifras se atribuyen a esa copia, sin fingir que corresponden a todas las versiones posteriores.
- [JSON Schema, referencia oficial de objetos](https://json-schema.org/understanding-json-schema/reference/object): `properties`, `required` y política de campos adicionales. Consulta del 29 de septiembre, hora local.

La consulta de los artículos fue seleccionada, no una lectura completa de sus apéndices. Plan-and-Execute se enseña como mecanismo del curso sin atribuir una mejora cuantificada a una fuente primaria no recibida. Los defectos del Lab 03 se explican según las diapositivas: sus archivos no se inspeccionaron.

Precisiones: un pensamiento actualiza contexto sin comprobarse a sí mismo; las observaciones pueden ser erróneas; no toda implementación ReAct exige un Thought por acción; 0 % de alucinaciones en una categoría de fallas no implica ausencia universal; 35,1 y 64,6 proceden de combinaciones con direcciones distintas; mejor corrida y promedio ALFWorld difieren; pass@1 del procedimiento con reintentos no equivale a una generación bruta; la tasa de aceptación engañosa del verificador condiciona sobre tests aprobados; no se convierte «20 %» en puntos porcentuales; límites requieren timeouts si las operaciones pueden bloquearse; un parámetro público puede coexistir con un máximo interno efectivo; los nombres Self-Critique y Self-Reflection no prueban identidad universal.

### Revisión de notebooks y laboratorio complementario

Se reprodujo la incompatibilidad entre `tool_result_meta` del simulador del lunes y el par de mensajes de su consigna. Se identificó el requisito de `curso/actividades`, los ejercicios vacíos, el uso prematuro de `traza`, la selección limitada por palabras y el manejo de solo `tool_calls[0]`. No se ejecutó la fábrica de conexiones ni se leyó `.env`.

Se reprodujeron cuatro defectos del verificador del martes: `[]` y `null` lanzan `AttributeError`, categoría lista lanza `TypeError`, y booleano `true` pasa como entero. El complemento rechaza esos casos de manera controlada; no inventa un rango para urgencia ni verifica la clasificación semántica de un ticket. No detecta claves duplicadas de JSON.

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/Practica/s12_laboratorio_local.py|s12_laboratorio_local.py]] usa biblioteca estándar y extrae mediante AST solo datos y definiciones seleccionadas. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/Practica/s12_resultados_verificados.json|s12_resultados_verificados.json]] conserva resultados: totales y promedios originales, emparejamiento llamada–resultado, cuatro corridas adaptadas, repetición original, detector sobre tres trazas, verificador corregido, reintentos exitosos/agotados y cortes por pasos/costo. El generador de mini-Reflexion recibe y utiliza críticas mediante reglas; no demuestra aprendizaje de LLM.

### Figuras y comprobación editorial

Ocho figuras originales 49–56, PNG y SVG, reproducibles con `Recursos visuales/generar_visuales_s12.py` (Pillow). Se inspeccionaron visualmente las ocho: sin texto cortado ni solapamientos. Las barras históricas usan ReAct tabla 1 y Reflexion tabla 3; las otras seis son esquemas propios. Cada figura tiene explicación en prosa en la nota correspondiente. La ampliación inicial entregó diagramas como imágenes reproducibles; la auditoría global añadió un flujo Mermaid en la nota 70.

Comprobación completada: YAML válido en las 11 notas nuevas; enlaces y anclas revisados en esas notas y los seis archivos de navegación/fuentes modificados; cinco fragmentos Python con sintaxis válida; ocho figuras revisadas; SVG válidos; las tres copias fuente coinciden byte a byte con los adjuntos. La práctica local terminó con sus comprobaciones correctas. El registro está en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/Practica/s12_revision_editorial.json|s12_revision_editorial.json]]. Ese registro corresponde a la ampliación inicial y sus enlaces. La auditoría posterior cubre todas las notas de este curso; no toda la bóveda ni la ejecución del Lab 03.


## Sesión 07 recuperada y revisión global — 29 de septiembre de 2026

[[sesion-07.pdf]], *Bases de datos vectoriales*, 22 de septiembre de 2026: 24 páginas leídas completas y revisadas visualmente, numeración PDF = visible. Se recuperó de Descargas y se copió sin modificaciones a `Materiales`. El notebook `s2-mar` citado no se encontró en los materiales disponibles.

| Páginas | Notas | Cobertura |
| --- | --- | --- |
| 1–5 | 79–80 | Problema, búsqueda exacta, N/d/k y límites de alta dimensión |
| 7–10, 14 | 81 | IVF, fronteras, nlist/nprobe y comparaciones |
| 11–14 | 82 | HNSW, capas, construcción y consulta |
| 16–19 | 83 | Recall, latencia, memoria y separación de evaluaciones |
| 21–24 | 84 | Colección, punto, payload, filtros, operación y contexto del taller |
| Síntesis | 85 | Quince ejercicios con soluciones razonadas |

Los seis gráficos 57–62 son propios y están explicados en las notas. Las cifras del ejemplo de recall 0,98 y Hit Rate 0,55 proceden de la presentación, no de una corrida local. Las memorias float32 y las comparaciones IVF se calcularon explícitamente. Las precisiones sobre IVFFlat frente a IVF-PQ, HNSW y persistencia se contrastaron con fuentes primarias enlazadas en las notas; no se usaron versiones actuales para inventar resultados de las demos docentes.

La [[15 REVISIÓN - Calidad cobertura y claridad 2026-09-29|auditoría global de calidad, cobertura y claridad]] reúne la revisión de tres subagentes y la revisión editorial común. Los registros de bloques anteriores describen el momento en que se incorporaron; el informe global indica el estado actual y evita atribuir ejecución a archivos solo leídos.


### Auditoría de fundamentos y archivos reales del Taller 2

Se releyeron las 25 notas de fundamentos, las 130 páginas de sesiones 00–05 y las 19 celdas del notebook `s1-lun`. Se inspeccionaron también 24 diapositivas clave por imagen, los 15 gráficos de esas notas y el gráfico guardado del notebook. Los papers y libros se contrastaron por pasajes, detallados en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Revision 2026-09-29/fundamentos.json|registro de fundamentos]]. FlashAttention, RoFormer y el modo estricto de Pydantic se contrastaron con sus fuentes primarias enlazadas en notas 19, 20 y 25. No se afirma lectura completa de los libros ni inspección de notebooks no recibidos.

Para RAG se releyeron las 31 notas y las 90 páginas de sesiones 06, 08, 09 y 10. En esta auditoría sí se inspeccionó estáticamente [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/talleres/taller 2/Entrega_Taller_02.zip|Entrega_Taller_02.zip]], snapshot del 27 de septiembre: scripts de ingesta, pipeline y evaluación; ambos golden sets; CSV de resultados; evidencias de métricas, cobertura, casos difíciles y configuración; documentos Nimbus; e informe de 22 páginas leído completo por texto, con nueve páginas inspeccionadas además visualmente. No se ejecutó el servicio ni se reprodujeron llamadas del laboratorio. Esto amplía el alcance de las revisiones iniciales descritas arriba, en las que esos archivos aún no habían sido inspeccionados.

La entrega archivada declara 22 notas de las sesiones 06–09, 109 fragmentos, BGE-M3, Qdrant/Podman y Gemma 3:4b/Ollama. Los CSV permiten recalcular baseline Hit Rate=7/8=0,875 y MRR=0,5625 para k=3 y k=5. En la extensión híbrida, Hit@3 cae a 0,75; Hit@5 conserva 0,875 y MRR@5 sube a 0,59375. El archivo de extensión no contiene generación comparable, así que no prueba una mejora de las respuestas. Las cuentas y sus denominadores están en [[54 S10 - Hit Rate y MRR con un experimento completo]] y [[56 S10 - Elegir una extensión y comprobar su efecto]].

El evaluador usa «alguno de los IDs anotados», que no comprueba haber recuperado todas las evidencias necesarias. Su prompt archivado no obliga explícitamente a citar. El ejemplo de anotación mezcla dos plazos distintos: aprobación previa y presentación posterior de facturas. Estas limitaciones se explican en las notas correspondientes. Los resultados pertenecen al snapshot archivado: editar apuntes y reingerir cambia el corpus y exige una corrida nueva para atribuir resultados al estado actual.


## Sesión 13 incorporada el 30 de septiembre de 2026

Se incorporó [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-13.pdf|sesion-13.pdf]], 26 páginas, con revisión del texto y de todas sus figuras. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|S13: MCP y casos de uso]] añade el índice y las notas 86–93, siete figuras reproducibles, cuatro diagramas Mermaid, veinte preguntas resueltas y un simulador educativo ejecutado. La paginación visible coincide con las páginas PDF.

El mapa completo de páginas, las precisiones sobre revisión 2026-07-28, los límites de material y el resultado de la validación están en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/16 FUENTES - Sesión 13 MCP y validación|fuentes y validación de S13]]. Esta incorporación amplía la cobertura posterior a la revisión histórica del 29 de septiembre; no cambia el alcance de esa revisión previa.


## Sesión 14 y tutorial incorporados el 2 de octubre de 2026

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|S14: multiagente, LangGraph y robustez]] incorpora las 31 páginas de sesión 14, las 15 del tutorial y las 13 celdas del jueves. Añade once notas temáticas, índice, nueve PNG explicados, cinco diagramas Mermaid y un notebook resuelto local. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/17 FUENTES - Sesión 14 tutorial y robustez|Fuentes y validación de S14]] contiene el mapa completo, precisiones, límites y registros de comprobación. Se conservaron los tres originales y se actualizaron los índices del curso y de prácticas.
