---
title: "40 S08 - Diagnóstico de fallos y decisiones del taller"
sesion: "08"
tags:
  - maestria/ia-generativa
  - rag
  - estudio
fuente: "[[sesion-08.pdf]]"
---

# 40 S08 - Diagnóstico de fallos y decisiones del taller

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[34 S08 - Guía para entender fragmentación y recuperación|Guía de la sesión 08]]

## 1. Por qué no se diagnostica solo mirando la respuesta

Una respuesta incompleta puede tener causas diferentes: una tabla se extrajo mal, una condición quedó separada, el buscador eligió otra sección o el generador ignoró evidencia disponible. El síntoma final no identifica la etapa responsable.

Diagnosticar consiste en seguir la información y encontrar el primer punto donde se pierde o deja de utilizarse correctamente. Esto evita cambiar el prompt para reparar un problema de extracción o aumentar top-k para recuperar una frase que nunca fue indexada.

## 2. Las preguntas en orden

![Ruta para localizar el fallo](<../Recursos visuales/25-s08-diagnostico.png>)

Primero comprueba que la fuente contiene la respuesta. Después revisa el texto extraído, los fragmentos, la entrada real al codificador, los candidatos recuperados y el contexto final. Solo cuando sabes qué vio el generador puedes evaluar si su respuesta utilizó correctamente esa información.

| Etapa | Evidencia que debes mirar | Por qué importa |
| --- | --- | --- |
| Fuente | Página y versión del documento | Puede faltar o estar desactualizada la información |
| Extracción | Texto extraído frente al original | OCR, tablas y columnas pueden alterar el contenido |
| Fragmentación | Regla junto con condiciones y encabezados | Un corte puede destruir relaciones |
| Representación | Conteo de tokens y entrada al codificador | El vector puede ignorar parte del texto |
| Recuperación | Lista inicial con identificadores y puntajes | La evidencia puede existir sin ser seleccionada |
| Selección y contexto | Lista tras reranking y prompt real | Un pasaje recuperado puede eliminarse después |
| Generación | Afirmaciones y citas de la respuesta | Puede haber evidencia suficiente mal utilizada |

Una tabla mal extraída puede conservar todos sus números y perder qué columna corresponde a cada uno. Por eso comprobar únicamente que «hay texto» resulta insuficiente: debe conservarse la relación que hace interpretables los datos.

## 3. Cómo relacionar una intervención con una causa

Si falta contenido en la extracción, corrige la ingesta. Si el contenido existe pero queda incomprensible fuera de su sección, ajusta cortes o metadatos contextuales. Si está bien representado pero no se recupera, examina el método de búsqueda, los filtros y el número de candidatos. Si llega y luego se descarta, examina reordenamiento y selección. Si llega correctamente al prompt y la respuesta lo contradice, estudia generación e instrucciones.

Puede haber varias causas simultáneas. El objetivo no es etiquetar apresuradamente una única caja, sino reunir evidencia suficiente para justificar la intervención. Cambiar varias cosas a la vez puede mejorar el resultado sin permitirte saber cuál produjo la mejora.

### Qué significa tener evidencia suficiente para responder

No basta con hallar palabras de la pregunta. Debes identificar qué afirmaciones requiere una respuesta completa y qué fuente permite sostener cada una. A veces un pasaje contiene todo; otras veces la respuesta depende de varios pasajes o de una condición situada en otra sección.

Si el contexto contiene una regla general pero omite la excepción aplicable, puede ser relevante e insuficiente a la vez. Si contiene dos versiones contradictorias y ninguna información de vigencia, el generador no tiene una base clara para elegir. Estos casos explican por qué conviene definir la evidencia esperada antes de evaluar lo convincente de la redacción.

Una salida parcialmente correcta puede ocultar esa insuficiencia. Para revisarla, separa sus afirmaciones y pregunta por el sustento de cada una. Así puedes reconocer una respuesta que acierta el dato principal pero inventa la condición que determina cómo usarlo.

### Intervenir para distinguir causas, no solo observar correlaciones

Un diagnóstico controlado puede sustituir temporalmente una etapa por evidencia revisada. Por ejemplo, suministrar directamente al generador los pasajes correctos permite comprobar si logra responder cuando la recuperación ya no limita su entrada. Es una prueba de diagnóstico, no un resultado del pipeline completo.

Si con ese contexto responde bien, has reunido evidencia de que una limitación anterior importaba. Eso todavía no identifica si falló el corte, la representación, la búsqueda o la selección. Debes recorrer esos pasos para localizar dónde desapareció el pasaje. Si aun con evidencia suficiente responde mal, investiga la interpretación de la tarea, la construcción del prompt o el generador.

Para que la comparación sea interpretable, conserva la misma pregunta, instrucciones y configuración del modelo en lo posible. Si la generación varía entre ejecuciones, una única respuesta no demuestra una regularidad; conviene comprobar si el comportamiento se sostiene. Esta es la conexión con [[26 S05 - Diseñar una comparación de modelos]].

**Una traza** es el registro de lo que ocurrió durante una consulta: versiones y parámetros utilizados, candidatos antes y después de seleccionar, contexto enviado y respuesta obtenida. Su valor consiste en poder explicar el resultado a partir de lo que efectivamente sucedió, no de lo que suponemos que debía ocurrir.

## 4. Qué es un golden set y por qué sus referencias deben ser estables

Un **golden set** es una colección de preguntas con respuestas o evidencias esperadas para evaluar un sistema. «Golden» no significa infalible: las anotaciones también requieren revisión.

Si la evidencia correcta se describe únicamente como `documento-0007`, cambiar la fragmentación puede hacer que ese identificador señale otro texto. Entonces la evaluación puede penalizar un resultado correcto por usar referencias del chunker anterior.

Una anotación más estable conserva el documento, su versión y la evidencia textual o ubicación original. Al cambiar los cortes, se revisa qué nuevos fragmentos contienen esa evidencia. Un fragmento esperado puede convertirse en dos; la tarea y el criterio de suficiencia deben reflejarlo.

La página 15 destaca documento y frase esperada. Eso mejora la estabilidad frente a nuevos cortes, aunque una frase repetida, una extracción distinta o un documento actualizado todavía pueden exigir revisión. Los identificadores son útiles para depurar una ejecución; no deberían ser la única definición duradera de verdad.

### Qué debe mantenerse estable cuando comparas dos configuraciones

La comparación necesita conservar la tarea: preguntas, versión del corpus y criterio de corrección. Los identificadores internos pueden cambiar, pero la definición de qué evidencia satisface la pregunta debe seguir siendo equivalente.

También hay que decidir qué comparación interesa. Mantener el mismo top-k al duplicar el tamaño de los fragmentos puede aumentar mucho el texto que recibe el generador. Podrías estar comparando simultáneamente fragmentación y presupuesto de contexto. Eso no invalida necesariamente el resultado, pero cambia su interpretación.

Si buscas aislar el efecto de un corte, registra y controla los otros factores pertinentes. Si buscas elegir el mejor sistema completo, puedes permitir combinaciones diferentes, pero debes informar junto con la calidad sus costos y condiciones. Justificar una mejora requiere explicar qué se mantuvo igual y qué cambió.

## 5. Cómo leer las indicaciones del taller

La página 28 describe el Taller 2, con entrega indicada para el sábado 26 de septiembre de 2026 y peso del 25 %, y presenta opciones de mejora: otra fragmentación, BM25 con RRF, reranking y una opción de evaluación. Son **datos del documento docente**, no una comprobación del aula virtual ni instrucciones para ejecutar o entregar trabajo desde estas notas.

Lo que interesa comprender es la lógica de la justificación. Defender un tamaño no consiste en decir «usé 512 porque es habitual». Debes explicar su unidad, el límite del codificador, qué relaciones preserva y qué evidencia muestra que funciona en ese corpus. Defender una mejora requiere compararla con el baseline bajo condiciones comparables.

Las métricas Recall@k, MRR y Hit Rate se anuncian para la sesión siguiente. Estas notas no atribuyen a la sesión 08 una evaluación que todavía no desarrolla. Aquí se prepara la base conceptual: qué observar, qué comparar y qué referencia conservar.

> [!abstract] Para recordar
> **Busca el primer punto donde la evidencia deja de estar disponible o se usa mal.** Cambia el componente relacionado con ese punto y vuelve a observar.

> [!question] Comprueba que lo entendiste
> Si cambias los cortes y baja una métrica basada en identificadores antiguos, ¿qué puedes concluir?
>
> Todavía no puedes concluir que empeoró la búsqueda. Primero debes comprobar que las etiquetas siguen representando la misma evidencia.

**Fuente:** [[sesion-08.pdf#page=15|páginas 15–16 y 28]], con conexiones a 9–12 y 23–27. Continúa con [[41 S08 - Recordatorio y preguntas de comprensión]].
