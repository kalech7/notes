---
title: "42 S09 - Guía para evaluar un RAG"
sesion: "09"
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-09.pdf]]"
---

# 42 S09 - Guía para evaluar un RAG

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

## La pregunta central

**¿Cómo sabemos si un RAG recupera la evidencia necesaria, responde con fundamento y reconoce cuándo no tiene información suficiente?** En la sesión 08 construimos la cadena de recuperación. En esta sesión aprendemos a comprobarla sin confundir una respuesta convincente con un sistema fiable.

Imagina un asistente que consulta un reglamento universitario. Le preguntas por los requisitos de graduación. Puede encontrar un párrafo parecido, encontrar el párrafo correcto pero ignorarlo, o redactar una respuesta muy clara con un requisito inventado. Los tres casos se ven similares si solo observas la fluidez. Para distinguirlos hay que evaluar etapas distintas.

## Mapa de las tres evaluaciones

![[27-s09-tres-evaluaciones.png]]

### Cómo leer el diagrama

Lee de izquierda a derecha. El **índice** devuelve vecinos próximos según una representación numérica; la **recuperación** debe aportar evidencia pertinente; la **generación** debe usarla correctamente. Debajo de cada etapa aparece su referencia de comparación.

El primer bloque pregunta si una búsqueda aproximada reproduce los vecinos de una búsqueda exacta. El segundo pregunta si esos vecinos contienen lo que un humano anotó como necesario. El tercero pregunta si la respuesta está sustentada y atiende la consulta. Las flechas muestran dependencia entre etapas, no una garantía de éxito: un 1,0 en el primer bloque no obliga a obtener 1,0 en el segundo.

**Ejemplo:** el índice devuelve exactamente los cinco textos más similares a «plazo para titularme». Su recall frente al buscador exacto puede ser 1. Si los embeddings acercan la pregunta a textos sobre matrícula, los vecinos exactos también pueden ser inadecuados. La búsqueda aproximada funciona y la selección semántica falla. Si sí llega el reglamento correcto pero el modelo añade un plazo inventado, el problema está después.

## Las palabras que debes manejar

| Palabra | Significado en esta sesión |
| --- | --- |
| Corpus | Conjunto de documentos disponibles para responder. |
| Ranking | Resultados ordenados, desde el que el sistema considera más pertinente. |
| Top-k | Los primeros k resultados; k es una cantidad, no una puntuación. |
| Relevancia | Juicio sobre si una unidad recuperada aporta evidencia para una pregunta. |
| Golden set | Preguntas con referencias, respuestas esperadas y criterios de evaluación revisados. |
| Respondible | Hay evidencia suficiente en el corpus definido para contestar. |
| Negativa | Pregunta sin respuesta en ese corpus; no significa pregunta mal formulada. |
| Abstención | El sistema reconoce que no puede responder con la evidencia disponible. |
| Baseline | Configuración inicial contra la que comparas un cambio. |

## Ruta de estudio

1. [[43 S09 - Hit Rate Recall MRR MAP y nDCG paso a paso|Métricas: calcular y explicar qué mide cada una]].
2. [[44 S09 - Golden sets anotación y caducidad|Golden set: construir una referencia que siga siendo válida]].
3. [[45 S09 - Preguntas negativas y abstención|Abstención: medir tanto el silencio correcto como el innecesario]].
4. [[46 S09 - Evaluar respuestas fidelidad y citas|Generación: revisar afirmaciones y citas]].
5. [[47 S09 - GraphRAG y recuperación multimodal|Patrones avanzados: preguntas globales, grafos y documentos multimodales]].
6. [[48 S09 - Diagnóstico experimentos y Taller 2|Experimentos: usar resultados para elegir cambios]].
7. [[49 S09 - Ejercicios resueltos y repaso|Práctica: comprobar que puedes razonar sin memorizar]].

## La distinción que evita casi todos los errores

Una **métrica** es una regla de cálculo. Una **anotación** indica qué se acepta como relevante. Un **juicio** decide si una afirmación está realmente sustentada. Las métricas de recuperación también se calculan: lo que se anota es su referencia. La frase del PDF «un recall se calcula; el otro se anota» contrasta el origen de la referencia, no dos clases incompatibles de operaciones.

Una fórmula aplicada correctamente puede producir un número inútil si compara identificadores obsoletos, mezcla poblaciones distintas o utiliza anotaciones incompletas. Por eso, antes de preguntar cuánto dio una métrica, pregunta **qué unidad comparó, contra qué referencia y sobre qué preguntas**.

## Fuente y alcance

Fuente principal: [[sesion-09.pdf]], *Evaluación de recuperación, golden sets y patrones avanzados*, 25 páginas, Daniel Andrés Riofrío Almeida, 24 de septiembre de 2026. Las notas cubren las páginas 2–25; las páginas 3, 9, 15 y 19 son separadores.

Los ejemplos universitarios, las cuentas adicionales y los gráficos son elaboraciones didácticas propias. Los resultados de investigaciones se presentan según el PDF y con su contexto histórico; no son mediciones hechas aquí. No se ejecutó el Lab 02 ni se verificó su implementación actual. Las consignas del taller se documentan como contenido académico, no como órdenes para ejecutar comandos o entregar trabajos.

> [!abstract] Para recordar
> Un RAG necesita tres comprobaciones distintas: encontrar vecinos, recuperar evidencia y elaborar una respuesta fundamentada.
