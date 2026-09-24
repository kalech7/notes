---
title: "35 S08 - RAG contexto memoria y generación fundamentada"
sesion: "08"
tags:
  - maestria/ia-generativa
  - rag
  - estudio
fuente: "[[sesion-08.pdf]]"
---

# 35 S08 - RAG contexto memoria y generación fundamentada

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[34 S08 - Guía para entender fragmentación y recuperación|Guía de la sesión 08]]

## 1. El contexto: saber redactar no equivale a conocer tus documentos

Un modelo de lenguaje aprende regularidades durante el entrenamiento. Parte de la información de esos datos queda reflejada en sus parámetros, pero eso no lo convierte en una copia consultable de todos los documentos. Puede no haber visto tus archivos privados, puede conservar información desactualizada y puede completar una respuesta plausible sin evidencia suficiente.

El problema no se resuelve únicamente pidiéndole que sea más preciso. Para responder sobre una fuente concreta necesita acceso a esa fuente. **RAG organiza ese acceso:** recupera información externa relevante y la incorpora a la entrada del generador.

## 2. Qué es y qué cambia

RAG significa *Retrieval-Augmented Generation*: generación aumentada con recuperación. En el sistema básico del curso, los pesos del generador permanecen fijos. Cambia el **contexto disponible durante la consulta**.

De forma conceptual:

$$\text{respuesta}=\text{generador}(\text{pregunta},\text{instrucciones},\text{evidencia recuperada}).$$

El modelo sigue generando tokens según lo aprendido, pero ahora puede apoyarse en información explícita. Esa es la razón de llamarla **generación fundamentada**: las afirmaciones deberían estar respaldadas por el contexto que se suministró y poder rastrearse a su origen.

Esto no garantiza fidelidad por sí solo. El modelo puede interpretar mal el texto, omitir una condición o añadir algo que no está sustentado. Una cita hace posible la comprobación; no reemplaza esa comprobación.

### Qué significa que el contexto cambie la generación

El generador no entrega de una sola vez una frase que encuentre guardada. En un LLM autorregresivo, cada paso calcula probabilidades para el siguiente token usando la entrada disponible y los tokens ya producidos. Si llamamos $q$ a la pregunta, $c$ al contexto recuperado, $i$ a las instrucciones y $y_{<t}$ a lo escrito antes del paso $t$, podemos expresar ese cálculo como:

$$P_\theta(y_t\mid q,c,i,y_{<t}).$$

La barra vertical se lee «dado» o «condicionado a». $\theta$ representa los parámetros aprendidos. Mantener $\theta$ fijo no obliga a dar siempre la misma respuesta: al cambiar $c$, cambian las entradas a los cálculos internos y puede cambiar la distribución del siguiente token. Esta es la conexión concreta entre RAG y la inferencia estudiada anteriormente.

La información externa puede influir en la generación porque los tokens de la pregunta y de los pasajes participan en el procesamiento del contexto. La atención permite relacionar posiciones de ese contexto con el token que se está calculando. No crea una obligación de copiar ni una prueba de verdad: el entrenamiento determina cómo se utilizan esas relaciones.

Por eso el modelo puede combinar dos pasajes para redactar una respuesta que no aparece literalmente en ninguno. Esa capacidad es útil si la combinación está justificada; introduce un error si añade una condición que las fuentes no sostienen. Fundamentar no significa repetir palabra por palabra: significa poder justificar el contenido de lo afirmado.

**Utilizar información durante una consulta no equivale a incorporarla permanentemente a los pesos.** En el flujo básico, si una consulta posterior no incluye esa información ni la recupera de nuevo, no debemos suponer que el modelo la «aprendió» por haberla leído antes. Si una aplicación conserva historial o memoria externa, esa persistencia pertenece al diseño de la aplicación.

## 3. Cómo funciona: dos tiempos y dos trabajos

En la **ingesta**, el sistema extrae y limpia documentos, conserva su estructura útil, crea fragmentos, calcula representaciones y guarda índices. También debe conservar el texto y metadatos como documento, sección, página y versión. Un vector por sí solo no sirve para mostrar la evidencia al usuario.

En la **consulta**, la pregunta se transforma en una búsqueda. El recuperador devuelve candidatos, el sistema elige qué textos entrarán al prompt y el generador produce una respuesta. Algunas arquitecturas agregan búsqueda léxica, fusión de listas o reranking; el RAG básico puede funcionar sin todas esas extensiones.

La ingesta se realiza al incorporar o actualizar documentos. La expresión «una vez» de la diapositiva 4 significa que se puede reutilizar el trabajo entre consultas; no significa que el índice deba quedar congelado para siempre.

| Componente | Su trabajo | Lo que no demuestra por sí solo |
| --- | --- | --- |
| Corpus | Proporciona las fuentes disponibles | Que las fuentes estén completas o vigentes |
| Recuperador | Selecciona candidatos relevantes | Que contengan evidencia suficiente |
| Constructor del contexto | Decide qué texto ve el LLM y cómo se identifica | Que el modelo vaya a obedecerlo |
| Generador | Redacta a partir de pregunta y contexto | Que todas sus afirmaciones estén respaldadas |

### El recorrido exacto: el vector ayuda a encontrar; el texto sirve para responder

![De texto a vector y de la búsqueda al texto original](<../Recursos visuales/26-s08-texto-vector-texto.png>)

En el RAG textual básico, **el generador recibe los pasajes recuperados como texto, no la lista de números del buscador**. El sistema obtiene identificadores de candidatos, usa esos identificadores para leer sus textos y construye con ellos el prompt. No intenta invertir matemáticamente un embedding para reconstruir un documento.

Esta separación explica por qué se guardan tanto representación como contenido. El embedding permite comparar; la asociación entre identificador y texto permite recuperar la fuente legible; los metadatos permiten saber de dónde vino. Si esa asociación se rompe, podrías encontrar un vector pertinente y mostrar el texto equivocado.

También explica el papel del programa que coordina el flujo. El LLM no abre espontáneamente la base vectorial: en un pipeline fijo, el programa hace la búsqueda y le pasa los resultados. En un agente, el modelo puede proponer utilizar una herramienta, pero una aplicación sigue siendo responsable de ejecutarla y devolver la información.

## 4. Por qué separar memoria paramétrica y memoria externa

La **memoria paramétrica** es la información incorporada en los pesos durante el aprendizaje. La **memoria no paramétrica**, en este contexto, es la colección externa que se consulta. El nombre no significa «sin estructura»; significa que el contenido consultado no está almacenado únicamente en los parámetros del generador.

La distinción importa para las actualizaciones. Si cambia una política, podemos actualizar su documento y su índice sin tener que volver a entrenar el generador. También importa para la trazabilidad: podemos enseñar el pasaje consultado, mientras que no existe una correspondencia sencilla entre una afirmación y un peso concreto del modelo.

## 5. El RAG del artículo y el RAG del curso

Las páginas 5–6 distinguen dos sistemas. Según la presentación, Lewis y colaboradores combinaron un recuperador DPR con un generador BART y entrenaron el codificador de preguntas y el generador; el codificador de documentos y el índice permanecieron fijos. El pasaje recuperado se modelaba como una variable latente.

**DPR** significa *Dense Passage Retrieval*, recuperación densa de pasajes. Utiliza representaciones de preguntas y pasajes entrenadas para poder compararlas. **BART** es el generador de esa arquitectura: su codificador procesa la entrada y su decodificador produce texto. Según la presentación, se preentrenó para reconstruir texto alterado con ruido. Los nombres identifican las piezas del estudio histórico; no son componentes obligatorios de todos los RAG.

«Latente» significa aquí que el pasaje que explica mejor una respuesta no tiene por qué estar señalado de antemano como una única etiqueta observada; el modelo combina posibilidades de recuperación. La consecuencia conceptual es que el sistema puede aprender de la utilidad de los pasajes para producir respuestas, en vez de depender únicamente de una selección documental fijada de antemano.

En el taller, se utilizan modelos ya entrenados para recuperar texto y colocarlo en el prompt. Por eso **«RAG no entrena al modelo» describe ese flujo concreto, no todas las arquitecturas llamadas RAG**.

## 6. Qué mejora y qué no resuelve

RAG puede dar acceso a información privada o reciente y facilitar la auditoría. Sin embargo, quedan dos problemas diferentes: recuperar la evidencia correcta y utilizarla correctamente. Si falla cualquiera de los dos, la respuesta puede ser incorrecta.

La página 7 presenta una evaluación histórica de 452 pares de pistas: RAG fue preferido por factualidad en el 42,7 % y BART en el 7,1 %; en el 17,7 % ninguna salida fue considerada buena. Estos son resultados de esa comparación, con categorías adicionales, **no porcentajes universales de exactitud ni una reducción de alucinación aplicable a cualquier RAG**.

### Tres criterios que conviene evaluar por separado

**Relevancia** pregunta si un pasaje sirve para la consulta. **Fidelidad al contexto** pregunta si la respuesta está sustentada por los pasajes suministrados. **Corrección** pregunta si la afirmación es correcta respecto de la fuente o realidad de referencia para la tarea.

Una respuesta puede ser fiel a un documento desactualizado y equivocarse sobre la política vigente. También puede acertar por conocimiento previo sin estar respaldada por el contexto que debía usar. En el primer caso falla la selección o vigencia de la fuente; en el segundo, acertar no demuestra que el mecanismo de fundamentación haya funcionado.

Esta distinción es la razón de revisar tanto los documentos recuperados como la respuesta. Un único juicio de «suena bien» mezcla problemas que requieren correcciones distintas.

## 7. Cuándo tiene sentido

Si la fuente es pequeña y cabe con margen en el contexto, suministrarla directamente puede evitar una etapa de búsqueda innecesaria. Si tienes muchos documentos y solo algunos importan para cada pregunta, recuperar ayuda a controlar el volumen y la pertinencia del contexto.

El ajuste fino cambia parámetros y puede enseñar comportamientos, formatos o capacidades. RAG cambia la evidencia disponible en cada consulta. Pueden combinarse; no son sustitutos perfectos. Asimismo, un RAG de pasos fijos no es automáticamente un agente. Un agente puede utilizar recuperación como una herramienta dentro de un proceso de decisiones.

> [!abstract] Para recordar
> **RAG cambia lo que el modelo puede consultar en ese momento.** No convierte la búsqueda en una garantía de verdad.

> [!question] Comprueba que lo entendiste
> Si actualizas un documento y reconstruyes su índice, ¿por qué puede cambiar la respuesta sin modificar los pesos?
>
> Porque cambió la evidencia que entra al prompt. La capacidad generativa es la misma, pero trabaja con información disponible diferente.

**Ampliación conceptual:** conexión con [[21 S03 - Preentrenamiento autosupervisado y MLE]] y [[19 S02 - Atención Q K V paso a paso]]. Se consultó también [[Hands-On_Large_Language_Models.pdf#page=272|cap. 8, pp. impresas 250–252 (PDF 272–274)]] para el paso de búsqueda a generación.

**Fuente:** [[sesion-08.pdf#page=4|páginas 4–7]]. Continúa con [[36 S08 - Fragmentos tokens y truncamiento]].
