---
title: "50 S10 - Guía para comprender el taller RAG"
sesion: "10"
fecha: 2026-09-27
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-10.pdf]]"
---

# 50 S10 - Guía para comprender el taller RAG

[[50 S10 - Guía para comprender el taller RAG|Guía de la sesión 10]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Siguiente: [[51 S10 - Del documento a una respuesta con evidencia]]

## La idea que organiza toda la sesión

Un sistema RAG puede ejecutar todos sus pasos sin lanzar errores y, aun así, ser incapaz de responder bien. Puede perder documentos durante la lectura, ignorar parte de un fragmento al crear su vector, recuperar textos del tema equivocado o inventar una conclusión después de recibir evidencia correcta.

La sesión 10 convierte esa observación en un método: **construir una versión inicial, medir sus fallas, elegir un cambio que responda a ellas y volver a medir**. Su valor está en poder explicar qué ocurrió y con qué evidencia lo sabemos.

RAG significa *Retrieval-Augmented Generation*: generación apoyada por recuperación de información. Un buscador selecciona material externo; un modelo generador recibe ese material junto con la pregunta. Recuperar añade evidencia al contexto, pero no garantiza que el modelo la interprete bien.

## Un caso que seguiremos en las notas

Imagina un asistente de una universidad ficticia. Su corpus contiene reglamentos y guías. Un documento dice: «La solicitud de equivalencia debe presentarse dentro de los diez días hábiles posteriores al inicio del período». Otro habla de diez días para pagar matrícula. Un instructivo escaneado contiene información sobre seguros, pero su lector de PDF no obtiene texto.

Preguntamos: **«¿Hasta cuándo puedo solicitar una equivalencia?»**. El sistema necesita identificar el procedimiento correcto, recuperar la cláusula completa, mantener la distinción entre días hábiles y calendario, y citar el origen. Un resultado parecido sobre matrícula no basta. Tampoco basta decir «diez días» si se omite desde cuándo se cuentan.

Todos los documentos, preguntas, valores y resultados de este caso son **didácticos e inventados**. No son resultados de ejecutar el laboratorio.

## Mapa para orientarte

![[35-s10-cadena-evidencia.png]]

**Cómo leerlo:** la fila superior prepara los documentos antes de las consultas. La inferior usa el índice para responder. Cada flecha necesita conservar información útil: del archivo al texto, del texto al fragmento, del fragmento al vector y de la evidencia a la respuesta. Las cajas inferiores indican qué observar para descubrir dónde se rompe la cadena.

La base vectorial conserva vectores y puede guardar texto y metadatos asociados. El generador utiliza texto recuperado; no lee directamente las coordenadas del embedding como si fueran un documento.

## Ruta de estudio

| Nota | Pregunta que aprenderás a resolver |
| --- | --- |
| [[51 S10 - Del documento a una respuesta con evidencia]] | ¿Qué hace cada etapa y por qué una puede funcionar mientras otra falla? |
| [[52 S10 - Ingesta tokens y tres fallas silenciosas]] | ¿Cómo se pierde información sin que el programa se detenga? |
| [[53 S10 - Golden set y límites de lo respondible]] | ¿Quién decide qué respuesta y qué evidencia son correctas? |
| [[54 S10 - Hit Rate y MRR con un experimento completo]] | ¿Cómo calculo y leo las métricas, sin confundirlas con exactitud? |
| [[55 S10 - Abstención fidelidad y errores del evaluador]] | ¿Cuándo conviene no responder y cómo se mide? |
| [[56 S10 - Elegir una extensión y comprobar su efecto]] | ¿Cuándo probar fragmentación, híbrida, reranking o RAGAS? |
| [[57 S10 - Reproducibilidad entregables y reflexión]] | ¿Qué evidencia hace que una comparación pueda revisarse? |
| [[58 S10 - Ejercicios resueltos y repaso activo]] | ¿Puedo diagnosticar ejemplos nuevos sin repetir definiciones? |

Si embeddings, tokens y coseno todavía te resultan confusos, repasa [[28 S06 - Qué es un embedding y qué significa cercanía]], [[31 S06 - Coseno producto punto y normalización]] y [[36 S08 - Fragmentos tokens y truncamiento]]. Para otras métricas, consulta [[43 S09 - Hit Rate Recall MRR MAP y nDCG paso a paso]].

## Tres distinciones que debes conservar

**Ejecutar y funcionar correctamente.** «La consulta devolvió cinco resultados» describe ejecución. «Los resultados incluyen la evidencia necesaria» describe recuperación útil. «La respuesta interpreta y cita correctamente esa evidencia» describe calidad de la respuesta.

**Métrica y diagnóstico.** Un Hit Rate bajo detecta que faltan aciertos; no revela por sí solo si la causa es una mala extracción, un filtro incorrecto, fragmentación, embeddings o anotación. Para diagnosticar hay que inspeccionar casos.

**Resultado y generalización.** Mejorar en una pregunta de ocho cambia mucho el promedio. Eso demuestra un cambio en esa muestra; todavía no demuestra que el sistema funcione mejor para todos sus usuarios.

> [!abstract] Qué deberías poder explicar al terminar
> «Mi sistema falló aquí; esta evidencia lo muestra; propuse este cambio por este mecanismo; al compararlo bajo las mismas condiciones pasó esto; quedan estas limitaciones».

## Fuente y alcance

Fuente principal: [[sesion-10.pdf]], *Taller 2 — Sistema RAG sobre base vectorial*, Daniel Andrés Riofrío Almeida, 16 páginas, sesión del 26 de septiembre de 2026. La portada y los separadores están en las páginas 1, 6 y 12. Las notas desarrollan el contenido de las restantes páginas y añaden ejemplos, derivaciones y seis figuras propias.

Las referencias del PDF a archivos del curso, al laboratorio y a sus revisiones se presentan como afirmaciones de la presentación: no se inspeccionó ese código para estas notas. Las reglas del taller y sus fechas se explican como contenido académico histórico; no constituyen instrucciones para ejecutar Docker, usar credenciales, publicar un corpus o entregar trabajos.
