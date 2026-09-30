---
title: "Revisión de calidad, cobertura y claridad de IA generativa y agentes"
created: 2026-09-29
fecha: 2026-09-29
tags:
  - maestria/ia-generativa
  - revision
  - estudio
---

# Revisión de tus notas de IA generativa y agentes

[[00 INICIO - Ruta de aprendizaje|Ruta de estudio]] · [[14 FUENTES - Materiales y mapa de cobertura|Fuentes y páginas]]

**Después de las correcciones, las notas tienen una cobertura sólida de las sesiones 00–12 disponibles y explicaciones suficientes para estudiar sus conceptos principales.** La revisión encontró errores puntuales, explicaciones que necesitaban más pasos y una sesión entera que faltaba. Se corrigieron directamente en las notas: se mejoraron 64 existentes y se conservaron las demás cuando cumplían su propósito. «Completo» aquí significa cobertura de los materiales recibidos; no de todo el campo de IA, de libros enteros ni de cuadernos ausentes.

La revisión abarca la carpeta **IA GENERATIVA Y AGENTES**. Se leyeron sus 79 notas originales, incluidos índice, glosario y fuentes; se añadieron siete notas de sesión 07. Quedan **86 notas de estudio y navegación**, más este informe. No se cuentan archivos de dependencias `.venv` como apuntes ni se extiende el dictamen a otras asignaturas de la bóveda.

## Cómo se revisó

Tres subagentes revisaron bloques distintos: fundamentos (25 notas), embeddings/RAG (31) y agentes (20). La revisión común cubrió navegación y referencias (3), integró las correcciones y comprobó estructura y recursos. Se contrastó el texto completo de **13 PDF docentes, 295 páginas**, y las **57 celdas** de los tres notebooks disponibles. Las representaciones visuales se revisaron donde correspondía: en fundamentos se inspeccionaron 24 diapositivas clave por imagen, sin afirmar que las 130 se vieran individualmente.

Se separó lo que dice la fuente, lo que las notas añaden para enseñar y lo que demuestra una prueba local. Las actividades y comandos de los PDF se trataron como contenido del curso, siguiendo tu solicitud; no como instrucciones para realizar entregas o desplegar servicios.

## Qué cambió y por qué importa

| Bloque | Hallazgo y mejora | Cómo te ayuda |
| --- | --- | --- |
| Fundamentos y causalidad | XOR ahora tiene una demostración algebraica y pesos concretos; observar e intervenir tiene un ejemplo numérico. | Puedes comprobar el mecanismo y explicar por qué una correlación no identifica un efecto causal. |
| Probabilidad y generación | EM incluye covarianzas y condiciones de no descenso; HMM termina la actualización con la observación; VAE distingue las dos KL y su relación con ELBO. | Evita memorizar etiquetas sin saber qué se calcula, qué se optimiza y con qué límites. |
| Transformer | Se corrigió atención a un token futuro en un ejemplo causal, el supuesto de diagonal máxima de XXᵀ y la explicación de multi-head. Se añadieron formas de tensores y normalización. | Puedes seguir el recorrido entrada → atención → logits sin confundir ancho, contexto, parámetros y pesos dinámicos. |
| Entrenamiento y prompting | DPO tiene pérdida completa y cuenta; se amplían las etapas de Constitutional AI, la coerción de tipos, la calibración y el diseño experimental del taller. | Puedes distinguir objetivos y verificar una salida con criterios claros. |
| Índices vectoriales | Faltaba S07. Se añadieron IVF, HNSW, memoria, percentiles, filtros y operación con seis figuras y quince ejercicios. | Conecta embeddings con RAG y distingue rapidez del índice de calidad de evidencia. |
| RAG y evaluación | Se precisó compatibilidad de espacios, evidencia alternativa frente a conjunta, nDCG y denominadores. Se integró el análisis del Taller 2 archivado. | Puedes interpretar una métrica sin concluir más de lo que mide. |
| Agentes | Se completaron datos y esquemas del lunes; se ampliaron acciones, benchmarks y comparadores ReAct, reinicios Reflexion y contratos efectivos. | Puedes seguir una traza y separar propuesta del modelo, ejecución, observación y verificación. |
| Fuentes y gráficos | Se registró la contradicción del PDF 12 sobre validación del Lab 03; se corrigieron el punto de abstención, un umbral Toolformer y una etiqueta superpuesta. | La explicación reconoce conflictos de la fuente y los gráficos coinciden con las cuentas. |
| Navegación | Se repararon 25 rutas del Canvas y se amplió hasta sesión 12; índice y glosario incluyen S07–10. | Puedes recorrer todos los bloques sin saltarte el puente vectorial. |

Los detalles de cada cambio se conservan en los registros de [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Revision 2026-09-29/fundamentos.json|fundamentos]], [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Revision 2026-09-29/rag.json|RAG]] y [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Revision 2026-09-29/agentes.json|agentes]].

## ¿Están bien explicadas?

La estructura parte de problemas concretos, define símbolos y desarrolla pasos con ejemplos. Las ampliaciones añadidas se concentran en puntos que impedían explicar **por qué** ocurre algo: un vecino puede quedar fuera de la celda examinada; un token futuro no está disponible en un decoder causal; recuperar una sola evidencia no asegura responder una pregunta que requiere varias; aprobar un esquema no demuestra exactitud semántica.

Las figuras tienen una explicación cercana en prosa que relaciona cajas, ejes, flechas y números con el concepto. Los diagramas conceptuales se identifican como tales; las cifras históricas conservan fuente y protocolo. Los ejemplos propios no se presentan como rendimiento medido de un modelo real.

Esto es una evaluación editorial y técnica, no una medición de tu comprensión. Para comprobar la segunda, usa las preguntas desplegables y explica una solución con tus palabras antes de abrirla. Si puedes hacer la cuenta y justificar su interpretación, la nota está cumpliendo su propósito.

## Qué muestran realmente los resultados del Taller 2

Los resultados archivados pueden analizarse sin volver a ejecutar el sistema. Baseline Hit Rate 0,875 significa que 7 de 8 preguntas respondibles recuperaron al menos un ID anotado; no demuestra cobertura completa de todas sus evidencias. MRR 0,5625 informa la posición del primer relevante. La extensión híbrida empeora Hit@3 a 0,75, mantiene Hit@5 y mejora MRR@5 a 0,59375. No hay generación comparable en ese archivo de extensión.

Por eso la conclusión útil es un intercambio entre cortes y posiciones, no una mejora general de todo el RAG. La [[54 S10 - Hit Rate y MRR con un experimento completo|nota 54]] distingue el baseline real del experimento didáctico; la [[56 S10 - Elegir una extensión y comprobar su efecto|nota 56]] interpreta la extensión híbrida. Los resultados son de la versión archivada; las notas actuales ampliadas requerirían una ingesta y evaluación nuevas para medir su efecto.

## Comprobación técnica

El registro [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Revision 2026-09-29/validacion.json|validacion.json]] conserva el resultado final: YAML, enlaces y anclas locales, imágenes, fuentes copiadas y Canvas. Los 23 bloques Mermaid se renderizaron sin errores; los 62 PNG y 62 SVG son válidos y las 62 figuras se revisaron visualmente entre los cuatro revisores. Las copias de los dos notebooks s3 y los PDF07/12 coinciden byte a byte con Descargas.

Se recalcularon los ejemplos añadidos y las métricas de CSV. Pasaron las dos prácticas locales de agentes y el verificador didáctico de S10. Esas prácticas usan reglas y datos locales: verifican cuentas y contratos concretos, sin certificar rendimiento de LLM, servicios ni toda posible entrada.

## Qué permanece fuera de esta revisión

| Material o afirmación | Estado |
| --- | --- |
| Notebook `s2-mar` de S07 | No localizado; no se inventa `embed_demo` ni se certifican sus celdas. |
| Notebooks `s1-mar`, `s1-mie` y `s1-jue` citados por diapositivas | No están entre las fuentes disponibles; las actividades se explican desde las diapositivas. |
| Lab 03 mencionado en S12 | Archivos no recibidos; sus defectos y la contradicción de la tabla se atribuyen al PDF. |
| Libros, papers y apéndices completos | Se contrastaron pasajes pertinentes, con páginas en registros; no se certifica lectura íntegra de todos. |
| Sesiones13–14, MCP y coordinación multiagente | Son continuidad anunciada, sin fuentes de esas sesiones disponibles para cubrirlas aquí. |
| Ejecución externa del Taller 2, modelos o APIs | Inspección estática y recálculo de resultados archivados; no nueva corrida externa. |
| Cumplimiento de rúbrica o calificación de tus entregas | No se certifica: el objetivo fue revisar apuntes y explicación conceptual. |

## Por dónde seguir estudiando

1. En [[19 S02 - Atención Q K V paso a paso]], sigue las formas de Q/K/V y explica qué cambia al aplicar la máscara causal.
2. En [[81 S07 - IVF celdas centroides y nprobe]], reconstruye el ejemplo de la frontera y diferencia `nprobe` de k.
3. En [[43 S09 - Hit Rate Recall MRR MAP y nDCG paso a paso]], calcula una métrica pequeña y escribe su denominador.
4. En [[68 S11 - Notebook del lunes explicado y revisado]], sigue una llamada desde sus argumentos hasta el resultado que vuelve al modelo.
5. En [[74 S12 - Verificadores fiables y errores del notebook]], explica por qué aprobar formato no prueba que la respuesta sea correcta.

Estas cinco comprobaciones recorren los puntos donde más fácilmente se confunden conceptos. La ruta completa permanece en [[00 INICIO - Ruta de aprendizaje]].
