# Fuentes y mapa de cobertura

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## Material base leído

- [[sesion-00.pdf]]: 15 páginas. Se utilizó el contenido académico de las páginas 4–15; se excluyó la presentación personal. Las páginas separadoras solo organizan el recorrido.
- [[sesion-01.pdf]]: 20 páginas. Se desarrollaron los conceptos y se adaptaron las actividades como práctica explicada.
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

Los apuntes distinguen causalidad general de la restricción de los grafos acíclicos; acotan la comparación entre generativos y discriminativos al resultado estudiado; diferencian el estado oculto del historial observado en HMM; y presentan las dificultades de VAE en texto como limitaciones, no imposibilidad.

No se añadieron precios, rankings de modelos o afirmaciones de mercado que se desactualicen. Los ejemplos son didácticos y los textos son explicaciones propias del material, no reproducciones extensas de libros.

## Figuras originales

Los 10 gráficos y diagramas de `Recursos visuales` se generaron específicamente para los apuntes con Matplotlib. Se conservan en PNG para lectura y SVG para ampliación sin pérdida. El archivo `generar_visuales.py` permite reproducirlos; requiere Python con NumPy, Matplotlib y SciPy. Las nubes GMM son sintéticas, con semilla fija 6013; las curvas Beta y fronteras AND se calculan a partir de las fórmulas explicadas. Los diagramas son esquemas didácticos, no capturas de los libros ni resultados experimentales del curso.
