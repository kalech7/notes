---
title: "57 S10 - Reproducibilidad entregables y reflexión"
sesion: "10"
fecha: 2026-09-27
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-10.pdf]]"
---

# 57 S10 - Reproducibilidad entregables y reflexión

[[50 S10 - Guía para comprender el taller RAG|Guía de la sesión 10]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[56 S10 - Elegir una extensión y comprobar su efecto]]

Siguiente: [[58 S10 - Ejercicios resueltos y repaso activo]]

## 1. Reproducibilidad: poder reconstruir qué se midió

Una tabla final no permite revisar por qué falló una pregunta. La reproducibilidad requiere conectar configuración, datos, ejecución y resultados. Otra persona debería poder entender qué se evaluó y repetirlo en condiciones suficientemente similares.

En un sistema con generación remota, repetir no siempre significa obtener exactamente el mismo texto. Se documentan modelo, parámetros, fecha y variabilidad. El objetivo es conservar una trazabilidad honesta, no prometer identidad perfecta cuando no está garantizada.

## 2. Evidencia mínima por etapa

| Evidencia | Qué permite revisar |
| --- | --- |
| Inventario y versiones del corpus | Qué universo de información se pretendía cubrir. |
| Registro de ingesta y rechazos | Qué información llegó realmente al sistema. |
| Configuración de fragmentación y encoder | Qué texto pudo representarse en los vectores. |
| Golden set versionado | Qué se consideró relevante y respondible. |
| Ranking por pregunta | Dónde apareció la primera evidencia y qué compitió con ella. |
| Prompt y respuesta registrados con cuidado | Qué vio el generador y qué afirmó. |
| Métricas por caso y agregadas | Cómo se obtuvo cada promedio. |
| Versiones, costo y latencia | Qué condiciones y recursos produjo la ejecución. |

Un CSV crudo conserva filas por consulta. La tabla resumen se calcula a partir de esas filas. Así puedes detectar que una mejora promedio proviene de una sola pregunta o que el evaluador omitió casos.

## 3. Por qué conservar dos colecciones

La página 2 advierte que el `index()` de ese laboratorio borra la colección antes de crearla. Si reutilizas su nombre para la extensión, puedes destruir la línea base que querías comparar. La recomendación de dos nombres busca mantener ambas configuraciones consultables.

Esto describe la implementación del curso, no una obligación universal de las bases vectoriales. Conceptualmente, conviene conservar una instantánea identificable de cada condición. No basta con recordar «antes usaba otros chunks».

## 4. Entorno, versiones y modos de ejecución

El PDF distingue un modo embebido en memoria para pruebas iniciales y un servidor Qdrant en contenedor para el baseline del taller. El modo en memoria simplifica el arranque y no implica persistencia entre procesos. El servidor separa el servicio de la aplicación; su persistencia debe configurarse según cómo se despliegue.

También menciona cambios de API entre `search` y `query_points`. Esto ilustra por qué el código, las dependencias y las instrucciones deben concordar. Declarar solo versiones mínimas no congela un entorno de forma exacta: versiones resueltas o un archivo de bloqueo permiten mayor precisión.

Estas notas explican el material; no ejecutan sus comandos de instalación ni su contenedor.

## 5. Costo y latencia también son resultados

**Latencia** es el tiempo observado. Conviene separar ingesta e indexación, que suelen ocurrir antes de consultar, de recuperación, reranking y generación, que afectan la espera del usuario. Una primera ejecución puede incluir carga de modelos y ser más lenta que las siguientes.

**Costo** depende de los recursos consumidos: llamadas, tokens y, según el entorno, cómputo. Una estimación sencilla para un servicio con precios por token sería:

$$C=\sum_j(T_{entrada,j}p_{entrada,j}+T_{salida,j}p_{salida,j})$$

Las unidades deben coincidir: si el precio está expresado por millón de tokens, se divide la cantidad de tokens entre un millón. No se incluyen precios actuales ni costos supuestamente medidos aquí.

Un reranker puede mejorar el orden y elevar la latencia. Una nueva fragmentación puede reducir truncamiento y aumentar almacenamiento. Una comparación útil informa calidad y recursos, junto con sus condiciones de medición.

## 6. Credenciales y corpus como parte de la trazabilidad

El PDF describe variables de entorno: los nombres y valores vacíos pueden documentarse en `.env.example`; los secretos reales se mantienen fuera de los archivos versionados y de los resultados compartidos. Añadir `.env` a `.gitignore` no elimina un secreto ya comprometido en el historial.

La frase de la diapositiva «el código nunca ve la clave» debe leerse como **no escribirla literalmente en el código fuente**. El proceso que hace la llamada sí accede al secreto en ejecución. Si una clave se publica, retirarla del archivo no basta; la presentación indica revocarla o rotarla.

También hay que conocer qué corpus se publica: el acceso a documentos para experimentar no implica permiso para hacerlos públicos. Estos puntos se incluyen porque forman parte del contenido de la sesión, no porque se haya detectado una fuga en tus archivos.

## 7. Qué pide el taller según esta presentación

| Componente | Peso | Sentido pedagógico |
| --- | ---: | --- |
| Parte 0: tres fallas reproducidas | 10 % | Aprender a observar pérdidas silenciosas. |
| Parte 1: baseline funcional | 35 % | Definir una cadena de procesamiento verificable. |
| Golden set | 10 % | Construir la referencia. |
| Métricas | 10 % | Cuantificar recuperación y abstención. |
| Tres peores casos | 10 % | Explicar fallas con evidencia. |
| Una extensión | 10 % | Probar una intervención motivada. |
| Reflexión | 5 % | Interpretar límites y significado de los números. |
| Reproducibilidad | 10 % | Permitir revisión y repetición. |
| **Total** | **100 %** | |

El 65 % mencionado en el PDF es $35+10+10+10$: baseline y las tres partes de su evaluación. No incluye la Parte 0. El taller representa, según su portada, 25 % de la nota final del curso.

La presentación describe un corpus propio de cinco documentos y cincuenta páginas, idioma declarado y capa de texto, en formatos PDF, TXT o Markdown. No aclara aquí todos los detalles de equivalencia de «páginas» para TXT/Markdown; para una entrega real habría que consultar el enunciado completo.

La lista visual de la página 5 incluye salidas de la Parte 0, capa de texto y rechazos, tamaño y solapamiento respecto del límite, identificación y fecha de verificación del embedding, tres consultas top-5, una respuesta con su generador, diez preguntas con dos negativas, Hit Rate/MRR a 3 y 5, dos tasas de abstención, peores casos y resultados crudos. Añade README, versiones, uso declarado de IA, costo, latencia y ausencia de claves.

Las fechas y horarios corresponden al **26 de septiembre de 2026**: repositorio al cierre de 11:50 e informe hasta 23:59. Son datos históricos de la sesión, no una nueva entrega creada por estas notas.

## 8. Qué son «los tres peores casos»

Para cada caso, registra pregunta, evidencia esperada, ranking, contexto enviado, respuesta, criterio incumplido y una hipótesis. Evita explicar todo como «el modelo alucinó».

**Caso A:** el reglamento no se extrajo: revisa ingesta. **Caso B:** se recuperó un trámite de código similar: revisa búsqueda léxica/híbrida. **Caso C:** llegó el párrafo correcto, pero se omitió «hábiles»: revisa generación. La intervención se elige después de reunir esta evidencia.

## 9. Reflexión: pregunta global y puente hacia agentes

Una pregunta como «¿qué excepciones aparecen recurrentemente en todos los reglamentos?» requiere cobertura de muchos documentos. Un top-5 local puede ser insuficiente aunque cada resultado sea pertinente. La solución podría necesitar descomponer la consulta, recuperar por documento y sintetizar con trazabilidad; la sesión 09 amplía estas ideas en [[47 S09 - GraphRAG y recuperación multimodal]].

El RAG fijo de estas notas sigue pasos predeterminados. Un agente incorpora decisiones sobre acciones o herramientas según el estado de la tarea. Usar un LLM, una base de datos o una API no basta por sí solo para demostrar esa capacidad de decisión.

La página 16 señala una tensión entre la continuidad de talleres en el sílabo y el cambio de datos del Taller 3. La presenta como pendiente de confirmación. Lo que podemos extraer con seguridad es el método: conservar referencias, registrar resultados y evaluar. No asumimos que el siguiente taller exija el mismo corpus.

## Qué conserva y qué no demuestra el archivo entregado

La entrega histórica registra 22 notas, 109 fragmentos, manifest de hashes, configuración y salidas. Su arquitectura usa BGE-M3 en una RTX 3050 Ti, vectores normalizados, Qdrant persistente mediante Podman y Gemma 3 4B local por Ollama. Podman sustituyó Docker Desktop tras un problema de su máquina virtual; el requisito sustantivo del caso era conservar la base y su API local, no el nombre del gestor de contenedores.

Las notas se amplían en esta auditoría del 29 de septiembre. Por eso los hashes, identificadores de fragmentos y métricas del snapshot del 27 **no describen automáticamente el corpus actual**. Para reproducir aquel experimento se usa el corpus preservado dentro del ZIP y su manifest; para medir estas notas revisadas hace falta una nueva versión y volver a anotar o reasociar evidencias. No sobrescribas los resultados anteriores como si se hubieran obtenido sobre la versión nueva.

Un CSV agregado puede conservar acierto y posición sin conservar respuesta completa o prompt efectivo. Para revisar fidelidad hacen falta esos artefactos adicionales. El contraste archivado no permite confirmar que Gemma local corresponda al identificador `open_weight_pequeno` del catálogo oficial del curso: el nombre y `verified_at` de esa fila permanecen sin verificar. Esto no borra las mediciones identificadas como `gemma3:4b`, pero tampoco permite atribuirles una identidad de catálogo no documentada. La revisión actual fue estática, no comprobó el estado actual de una GPU, un contenedor, un servicio o una clave.


**Fuente:** PDF, pp. 1–5, 7 y 14–16. Las precisiones sobre persistencia, versiones y costos son ampliaciones conceptuales.
