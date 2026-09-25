---
title: "48 S09 - Diagnóstico experimentos y Taller 2"
sesion: "09"
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-09.pdf]]"
---

# 48 S09 - Diagnóstico experimentos y Taller 2

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[42 S09 - Guía para evaluar un RAG|Guía de la sesión 09]]

## 1. Una métrica baja es una pista, no un diagnóstico completo

Fuente base: [[sesion-09.pdf#page=24|PDF, pp. 24–25]], conectada con [[40 S08 - Diagnóstico de fallos y decisiones del taller]]. La sesión propone elegir una extensión por un modo de fallo observado. Eso requiere mirar los casos, no solo el promedio.

| Observación | Hipótesis inicial | Comprobación útil |
| --- | --- | --- |
| Recall del índice alto, Hit Rate bajo | Vecinos correctos según el vector, pero evidencia mal representada o seleccionada | Comparar recuperación exacta y revisar textos relevantes ausentes. |
| Hit Rate alto, MRR bajo | La evidencia entra, pero tarde | Revisar orden y probar reranking. |
| Fallos concentrados en códigos y siglas | La coincidencia literal importa mucho | Comparar búsqueda léxica e híbrida. |
| Fallos generalizados | Problemas de ingesta, corte, truncamiento o representación | Rastrear una frase fuente hasta su fragmento e índice. |
| Recuperación alta, respuestas inventadas | Fallos al construir contexto o generar | Inspeccionar contexto final, afirmaciones y citas. |
| Métricas idénticas | Muestra pequeña, medida poco sensible o sistemas equivalentes en esos casos | Revisar cambios por pregunta y ampliar evaluación. |

Son hipótesis, no reglas causales infalibles. Hit Rate bajo no prueba automáticamente que el chunking sea el culpable. También puede haber anotaciones incorrectas, un corpus insuficiente o preguntas ambiguas.

## 2. Reranking: el conjunto y el corte no son lo mismo

Supón que recuperas 20 candidatos y luego entregas solo 5 al generador. Un reranker reordena esos 20; no puede inventar un candidato que no estaba.

Si el relevante estaba en el puesto 12 y pasa al 2:

- Hit@20 permanece en 1: ya estaba dentro del conjunto de candidatos.
- Hit@5 cambia de 0 a 1: ahora entra en el corte final.
- RR@5 cambia de 0 a 1/2.

Por eso la afirmación de la sesión «el reranking no sube el Hit Rate del conjunto de candidatos» debe leerse con precisión. Puede aumentar Hit Rate y Recall del top-k final cuando k es menor que el número de candidatos. Incluso en el mismo conjunto, un reranker mal ajustado puede empeorar el orden; la mejora debe medirse.

La relación general, para la misma población, corte y definición de acierto, es:

$$0\leq MRR@k\leq HitRate@k\leq1$$

Cada RR es cero si no hay acierto y como máximo uno si lo hay. Por eso un MRR mayor que Hit Rate indica definiciones incompatibles o un error de cálculo.

## 3. Con ocho preguntas, un caso pesa mucho

![[34-s09-resolucion-hit-rate.png]]

### Cómo leer el gráfico

El eje horizontal cuenta preguntas con acierto; el vertical muestra Hit Rate. Son las nueve posibilidades con ocho respondibles, desde cero hasta ocho aciertos. Cada escalón tiene altura 1/8 = 0,125, es decir, 12,5 puntos porcentuales.

Pasar de 0,75 a 0,875 significa acertar una pregunta adicional en este conjunto. No demuestra una mejora de 12,5 puntos en cualquier población futura. Si una pregunta cambia de etiqueta o una anotación está mal, también puede alterar mucho el resultado.

Los puntos se calculan exactamente como aciertos/8. No son observaciones experimentales ni intervalos de confianza. La figura muestra **resolución de la métrica**, que no es lo mismo que incertidumbre estadística.

## 4. Comparación reproducible

Como ampliación práctica, utiliza esta secuencia:

1. Fija corpus, golden set, unidad de relevancia y reglas de respondibilidad.
2. Guarda la configuración inicial: extracción, chunking, modelo, búsqueda, candidatos, corte y generación.
3. Ejecuta la referencia y conserva resultados por pregunta, rankings y respuesta final.
4. Cambia un componente para poder atribuir diferencias de forma razonable.
5. Evalúa ambas configuraciones con los mismos cortes y referencias válidas.
6. Revisa casos ganados y perdidos, no solo promedios; reporta latencia y costo cuando sean pertinentes.

Si cambias fragmentación, revalida las anclas. Si cambias corpus, revisa si las negativas siguen sin respuesta. Si evalúas una generación estocástica, registra parámetros y considera repeticiones antes de atribuir un cambio pequeño al sistema.

**No ajustes el golden set silenciosamente después de ver qué configuración gana.** Una corrección legítima se versiona y se aplica a todos los resultados comparados.

## 5. Qué conviene conservar por pregunta

Una tabla propia de evaluación puede registrar: ID de pregunta, tipo, respondibilidad, versión de la referencia, k, ranking, primer acierto, evidencia cubierta, respuesta, abstención y juicio de soporte. Conservar numeradores y denominadores permite reconstruir promedios.

Ejemplo de reporte: «6/8 respondibles con acierto, Hit Rate@5 = 0,75; 2/2 negativas con abstención correcta; 1/8 respondibles con abstención indebida». Expresa mucho más que «el RAG obtuvo 75 %».

Segmenta al menos por tipos de pregunta. Un promedio global puede ocultar mejoras en preguntas simples y deterioro en multi-chunk. El gráfico de [[47 S09 - GraphRAG y recuperación multimodal]] muestra un intercambio parecido en los resultados históricos del PDF.

## 6. Lo que dice el PDF sobre el Taller 2

> [!info] Contexto docente, no ejecución
> Esta sección registra las consignas de la presentación. No implica que el taller se haya resuelto, que Docker esté preparado ni que se haya entregado un archivo.

La p. 25 sitúa el Taller 2 el sábado 26 de septiembre y le asigna 25 %. Pide un RAG sobre base vectorial, un golden set de diez preguntas anotado por documento y frase, evaluación con k = 3 y k = 5, y entrega del `resultados.csv` crudo. También pide elegir la extensión por el fallo medido.

El PDF indica probar Docker con Qdrant antes del taller y aclara que el RAG multimodal se expone pero no se evalúa allí. La Parte 4 incluye explicar el problema del 0,70 con los resultados propios y plantear una pregunta global sobre el corpus, relacionándola con GraphRAG.

Para estudiar esa Parte 4, debes poder explicar **por qué el denominador cambia el significado del número** y **por qué una síntesis global necesita otra referencia de evaluación**. El contenido de estas notas prepara esas ideas; no sustituye revisar el enunciado oficial ni el código del laboratorio.

> [!abstract] Para recordar
> Primero valida qué mide el número; después úsalo para decidir qué componente cambiar.
