---
title: "83 S07 - Recall del índice latencia y memoria"
created: 2026-09-29
fecha: 2026-09-22
capitulo: 7
sesion: "07"
tags:
  - maestria/ia-generativa
  - recuperacion
  - bases-vectoriales
---

# 83 S07 - Recall del índice latencia y memoria

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/79 S07 - Guía de búsqueda vectorial e índices|Guía de sesión 07]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Elegir un índice implica medir **fidelidad a la búsqueda exacta, tiempo y recursos**. No basta que una consulta devuelva algo plausible. Los tres indicadores responden preguntas distintas y requieren condiciones declaradas.

## 1. Recall del índice

Sea $E_k(q)$ el conjunto de k IDs devueltos por el exacto y $A_k(q)$ los del aproximado, con misma base, filtro y métrica:

$$R_{\text{índice}}(q)=\frac{|E_k(q)\cap A_k(q)|}{k}$$

Si el exacto devuelve A,B,C,D,E y ANN devuelve A,B,C,F,G, la coincidencia es 3/5=0,6. Se promedia después sobre las consultas de evaluación. Cuando hay menos de k puntos elegibles o empates, se declara una convención válida antes de aplicar la fórmula.

La referencia se **calcula** mediante el exacto. En cambio, Recall@k de recuperación compara con evidencia pertinente anotada para la pregunta; su denominador puede ser el número de fragmentos relevantes, no k. Hit Rate pregunta si apareció al menos uno relevante. Sus detalles están en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/09 Evaluación de RAG y patrones avanzados/43 S09 - Hit Rate Recall MRR MAP y nDCG paso a paso|43 S09 - Hit Rate Recall MRR MAP y nDCG paso a paso]].

## 2. Recall alto no localiza por sí solo el defecto de RAG

Un índice con recall 0,98 puede alimentar Hit Rate@5 de 0,55. Antes de subir exploración, se ejecuta el exacto sobre **las mismas consultas, embeddings y filtros** y se evalúa su Hit Rate. Si el exacto sigue cerca de 0,55, la aproximación probablemente no explica la mayor parte del problema.

Si el exacto mejora mucho la recuperación de evidencia crítica, hay una pérdida importante de ANN para esas consultas. El recall promedio puede ocultar fallas concentradas en un segmento; no hay un umbral universal a partir del cual sea imposible mejorar calidad.

Después se revisa extracción del texto, fragmentación, compatibilidad del encoder, medida, filtros, contexto y generación. La intervención cambia una etapa para que el resultado pueda atribuirse a ella.

## 3. p50 y p99 describen una distribución

Ordena las latencias de muchas consultas. p50 es la mediana: aproximadamente la mitad no supera ese tiempo. p99 deja aproximadamente el 99 % por debajo. No es el máximo, una media ni la latencia de todas las consultas. El estimador de percentiles y tamaño de muestra afectan el valor.

Latencia de índice puede excluir embedding de consulta, comunicación y generación. Latencia de extremo a extremo los incluye según el inicio y final declarados. Sumar p99 de componentes no equivale en general al p99 del total: depende de cómo se combinan sus variaciones.

Una muestra de muy pocas consultas no caracteriza bien la cola. Se registran carga, concurrencia, caché y calentamiento además de la medida. Bajar candidatos puede mejorar tiempo sin mejorar la respuesta.

## 4. Memoria de vectores, paso a paso

Un `float32` ocupa cuatro bytes. Solo para N vectores de dimensión d:

$$B_{\text{vectores}}=N\,d\,4$$

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/61-s07-dimension-memoria.png|61-s07-dimension-memoria.png]]

Cada barra muestra el almacenamiento bruto calculado para un millón de vectores. El eje usa gigabytes decimales, con $1\ \mathrm{GB}=10^9$ bytes. La proporción entre 3072 y 384 es ocho: duplicar dimensión duplica esta parte de memoria. El gráfico no incluye estructura ni texto, por lo que no estima la RAM total de un proceso.

| Dimensión | Bytes para un millón | GB decimales |
| --- | ---: | ---: |
| 384 | 1536000000 | 1,536 |
| 1024 | 4096000000 | 4,096 |
| 1536 | 6144000000 | 6,144 |
| 3072 | 12288000000 | 12,288 |

GiB usa $2^{30}$ bytes, de modo que da otro número para el mismo almacenamiento. A los vectores se suman conexiones o listas, IDs, payload, índices adicionales, sobrecarga y memoria de trabajo. La compresión puede reducir representación a cambio de precisión u otros costos.

## 5. El triángulo es una guía de medición

Con un índice fijo, aumentar exploración suele recuperar más vecinos pagando tiempo; aumentar conexiones puede mejorar opciones a costa de memoria. No es una ley que impida toda mejora conjunta: una implementación mejor, otro hardware o una estructura más adecuada puede cambiar varias dimensiones a la vez.

«HNSW usa más memoria que IVF» necesita variantes comparables. La diferencia suele explicarse por el grafo frente a listas simples, pero compresión, precisión, metadatos y parámetros pueden cambiarla. Estas notas no anuncian un ganador universal.

> [!question]- ¿Recall 0,95 quiere decir que el 95 % de las respuestas del chatbot es correcto?
> No. Mide coincidencia de vecinos con el exacto bajo la convención declarada. La evidencia útil y la respuesta requieren evaluaciones distintas.

Fuente: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-07.pdf#page=7|PDF 7, 16–18]]. Cuentas y diagnóstico desarrollados con ejemplos propios. Los tamaños de dimensión se usan como variables matemáticas, sin afirmar disponibilidad actual de modelos comerciales.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/82 S07 - HNSW capas conexiones y exploración|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/84 S07 - Colecciones payload filtros y operación|Siguiente]] →
