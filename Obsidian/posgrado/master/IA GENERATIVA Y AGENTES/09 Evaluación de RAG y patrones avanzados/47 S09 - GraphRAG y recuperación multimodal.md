---
title: "47 S09 - GraphRAG y recuperación multimodal"
sesion: "09"
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-09.pdf]]"
---

# 47 S09 - GraphRAG y recuperación multimodal

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[42 S09 - Guía para evaluar un RAG|Guía de la sesión 09]]

## 1. Cuándo buscar unos pocos fragmentos se queda corto

Fuente base: [[sesion-09.pdf#page=21|PDF, pp. 21–23]]. Para «¿cuántos créditos se requieren?» puedes señalar un pasaje. Para «¿cuáles son los principales problemas de gestión que aparecen en todo el corpus?» necesitas una síntesis distribuida: los temas pueden estar repartidos entre decenas de documentos.

Una búsqueda por similitud puede concentrarse en los textos más parecidos a la pregunta y omitir temas menos frecuentes. Aumentar k ayuda hasta cierto punto, pero crece el costo y no asegura una representación equilibrada de todo el corpus.

En este caso, la referencia puntual documento-frase del taller resulta insuficiente. El PDF dice que las métricas de recuperación no están definidas para esa pregunta global: **se refiere al protocolo que no ha definido un conjunto de fragmentos relevantes**. No significa que ninguna pregunta global pueda evaluarse ni que sea imposible construir otros juicios de referencia. Se necesita otro diseño de evaluación.

## 2. Qué es un grafo en este contexto

Un grafo representa **entidades** como nodos y **relaciones** como aristas. En un corpus universitario, los nodos podrían ser programas, asignaturas y competencias. Una arista «enseña» podría conectar una asignatura con una competencia; una arista «requiere» podría conectar dos asignaturas.

Una **comunidad** es un grupo de nodos que, según el criterio del algoritmo, están especialmente conectados entre sí. No tiene por qué coincidir exactamente con una categoría humana. Extraer relaciones con un LLM tampoco garantiza que todas sean correctas: un error de extracción puede contaminar resúmenes posteriores.

## 3. GraphRAG global, paso a paso

![[32-s09-graphrag.png]]

### Cómo leer el diagrama

La fila superior ocurre durante la preparación. Los documentos se dividen, se extraen entidades y relaciones, se organiza un grafo, se detectan comunidades y se escriben resúmenes de esas comunidades. La fila inferior ocurre cuando llega una pregunta: varios resúmenes generan respuestas parciales y una reducción las integra.

Las flechas muestran transformaciones de información. El paso de arriba a abajo señala que la consulta reutiliza trabajo previo. No representa una búsqueda vectorial que devuelve sin más un documento; describe el patrón de consulta global explicado por la sesión.

**Map** significa aplicar una tarea a varias partes: preguntar a cada resumen qué aporta. **Reduce** significa combinar los resultados en una respuesta final, eliminando repeticiones y conciliando aportes. «Reduce» aquí no significa reducir dimensionalidad de embeddings.

### Preparación

1. Un LLM lee fragmentos y extrae entidades, relaciones y afirmaciones.
2. Se consolidan menciones y se forma el grafo. La implementación descrita en la diapositiva usa coincidencia exacta de nombres; los alias pueden requerir cuidado adicional.
3. Se detectan comunidades con Leiden en una jerarquía. Dentro de un nivel, las comunidades forman una partición; entre niveles hay agrupaciones más gruesas y más finas.
4. Se generan resúmenes de comunidades para reutilizarlos después.

### Consulta

1. Llega una pregunta global.
2. Se obtienen respuestas parciales desde los resúmenes elegidos.
3. Se asignan puntuaciones de utilidad, de 0 a 100 en el procedimiento citado.
4. Se integran los aportes para producir una síntesis global.

Una puntuación de utilidad no es una probabilidad calibrada de que la afirmación sea cierta. Es una señal interna para seleccionar aportes.

## 4. Qué cambia al elegir el nivel de comunidad

Una partición gruesa tiene menos comunidades, más amplias, y resúmenes que condensan mucho contenido. Una partición fina tiene más grupos pequeños y puede conservar mayor detalle. Consultar más resúmenes generalmente implica más trabajo; consultar resúmenes muy generales puede omitir matices.

El PDF cita una reducción de más del 97 % de tokens de consulta para C0 frente a resumir textos fuente y una preferencia del 72 % en exhaustividad frente a RAG vectorial, dentro del estudio referido. También cita 281 minutos de indexación por un millón de tokens. Son resultados de aquel protocolo y configuración, no promesas de costo ni tiempos de tu equipo. La preferencia en exhaustividad no equivale a exactitud factual.

## 5. Cuatro formas de usar grafos

| Patrón | Qué hace | Pregunta ilustrativa |
| --- | --- | --- |
| Global | Combina resúmenes de comunidades | ¿Qué temas se repiten en todo el corpus? |
| Local | Parte de una entidad y explora sus vecinos | ¿Qué asignaturas se relacionan con esta competencia? |
| Grafo como fuente | Consulta hechos o relaciones de un grafo existente | ¿Qué programa exige esta asignatura? |
| Grafo como índice | Usa conexiones para localizar documentos u otras evidencias | ¿Dónde está la tabla vinculada a esta sección? |

No necesitas elegir GraphRAG solo porque tu pregunta mencione varias entidades. Primero determina si la respuesta está en unos pocos pasajes, requiere seguir relaciones o necesita sintetizar el conjunto. Los casos locales pueden tener referencias puntuales evaluables con el golden set; el caso global necesita criterios de cobertura, coherencia, diversidad temática y soporte de la síntesis.

## 6. RAG multimodal: preservar relaciones, no solo archivos

Una tabla no es una bolsa de números: filas, columnas, encabezados y unidades determinan su significado. Una figura puede expresar una tendencia que no está escrita en el párrafo contiguo. Una ecuación necesita sus símbolos y definiciones.

Ejemplo propio: una tabla contiene «65» en la columna de rendimiento de 2025. Si la extracción pierde el encabezado, recuperar «65» no permite saber si son créditos, porcentaje o número de estudiantes. Un sistema multimodal busca conservar la entidad y sus conexiones: tabla, título, celda, unidad y sección.

El patrón avanzado no elimina la necesidad de evaluar. Puede mejorar la interpretación de estructuras y aun así fallar en preguntas que el documento no responde.

## 7. Por qué mirar solo el promedio lleva a elegir mal

![[33-s09-promedio-y-segmentos.png]]

### Cómo leer el gráfico

El eje horizontal contiene dos métodos tal como se comparan en la diapositiva 23. El vertical es exactitud porcentual, de 0 a 100. La barra azul es global; la naranja corresponde al subconjunto de preguntas incontestables. Los números están transcritos del PDF, que los atribuye a DocBench en el trabajo *RAG-Anything*; no se ejecutó ese benchmark aquí.

RAG-Anything tiene mayor exactitud global: 63,4 frente a 61,0. Pero MM-GraphRAG tiene mayor exactitud en incontestables: 60,5 frente a 46,0. La conclusión se invierte al cambiar de segmento. Por eso el método «mejor» depende de qué errores importan y de cómo se compone la evaluación.

La distancia es 2,4 **puntos porcentuales** en global a favor de RAG-Anything y 14,5 puntos en incontestables a favor de MM-GraphRAG. No son mejoras relativas del 2,4 % y del 14,5 %.

El PDF también cita una ablación de reranking de 63,4 a 62,4: un punto en esa evaluación. No permite concluir que todo reranker aporta solo un punto, ni comparar esa magnitud directamente con nDCG de otro conjunto de datos.

> [!abstract] Para recordar
> La arquitectura debe corresponder a la pregunta y la evaluación debe corresponder al tipo de respuesta que esperas.
