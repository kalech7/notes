---
title: "53 S10 - Golden set y límites de lo respondible"
sesion: "10"
fecha: 2026-09-27
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-10.pdf]]"
---

# 53 S10 - Golden set y límites de lo respondible

[[50 S10 - Guía para comprender el taller RAG|Guía de la sesión 10]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[52 S10 - Ingesta tokens y tres fallas silenciosas]]

Siguiente: [[54 S10 - Hit Rate y MRR con un experimento completo]]

## 1. El golden set es una referencia revisable

Un **golden set** es un conjunto de preguntas con criterios para juzgar los resultados. No consiste únicamente en una lista de respuestas modelo. Necesita establecer qué evidencia responde a cada pregunta y cuándo corresponde abstenerse.

Si preguntas «¿Hasta cuándo puedo solicitar una equivalencia?», una anotación útil incluye el documento y su versión, página o sección, la cláusula relevante y una respuesta que conserve «diez días hábiles» y «desde el inicio del período».

La respuesta de referencia puede admitir paráfrasis. La evidencia debe permitir comprobarlas. Si solo guardas «diez días», podrías aceptar respuestas que omiten el punto de inicio o alteran el tipo de días.

## 2. Tres niveles de disponibilidad

![[37-s10-corpus-y-contexto.png]]

Empieza por los documentos originales. Solo parte de su contenido puede haber llegado al índice; en cada consulta se recupera una parte todavía menor, que luego se selecciona para el prompt. La reducción del diagrama representa disponibilidad, no porcentajes medidos. Cada paso puede perder justo la evidencia que necesitas.

Conviene distinguir:

- **Corpus original o de referencia:** documentos cuyo contenido pretende cubrir el sistema.
- **Contenido efectivamente indexado:** material que la ingesta y la fragmentación lograron representar.
- **Contexto de una consulta:** evidencia finalmente incluida en el prompt.

Una pregunta puede ser respondible en el primer nivel e irresoluble con el tercero. Eso no convierte mágicamente el documento original en inexistente.

## 3. La sutileza de la página 10

La presentación dice que en `golden_ejemplo.json` las dos preguntas del ejemplo están anotadas como negativas, incluida aquella cuya respuesta está en un PDF rechazado. La inspección de `golden_ejemplo.json` de la entrega confirma esa convención en sus ítems 5 y 6. Describe el corpus indexable del ejemplo; conviene conservar por separado que el ítem 6 sí es respondible en los documentos originales.

Hay dos evaluaciones legítimas, pero **responden preguntas diferentes**:

| Alcance declarado | Etiqueta del caso escaneado | Qué revela |
| --- | --- | --- |
| Sistema completo respecto del corpus original | Respondible; la recuperación falla si la evidencia no llega. | Pérdida de cobertura causada por la ingesta. |
| Capacidad de responder con el contenido disponible en el índice | Negativa respecto de ese contenido. | Si el generador evita inventar ante evidencia ausente. |

Si cambias silenciosamente del primer alcance al segundo, puedes mejorar tus métricas excluyendo precisamente los documentos que el sistema no logró procesar. Debes conservar ambas observaciones: **la abstención puede ser prudente y la pérdida de cobertura puede seguir siendo un defecto**.

Esta es la razón de que ni el score del vecino ni el Hit Rate, aislados del criterio de anotación, separen por sí solos ambos casos de la diapositiva.

## 4. Cómo anotar de forma útil

Para cada pregunta, registra su ID, redacción, tipo, evidencia y criterio de respuesta. La siguiente ficha es pedagógica, no un esquema validado contra el cargador del laboratorio:

```json
{
  "id": "q01",
  "pregunta": "¿Hasta cuándo puedo solicitar una equivalencia?",
  "tipo": "respondible",
  "documento": "reglamento_ficticio_v1.pdf",
  "pagina": 12,
  "evidencia": "diez días hábiles posteriores al inicio del período",
  "respuesta_esperada": "Dentro de los diez días hábiles desde el inicio del período.",
  "criterio": "Debe conservar plazo, tipo de días y punto de inicio."
}
```

El PDF indica que su cargador necesita `id` y `pregunta`, y omite filas con `REEMPLAZAR`. Una plantilla todavía sin completar puede reducir el número de casos realmente evaluados. Por eso se verifica el conteo después de cargar, no solo el número de objetos que parece contener el archivo.

## 5. Documento relevante y fragmento suficiente

Anotar solo el nombre del documento es sencillo, pero un reglamento de cien páginas contiene muchas secciones irrelevantes para una pregunta. Si recuperas la portada de ese reglamento, un evaluador por documento podría contar un acierto aunque la respuesta no esté allí.

Anotar una frase o pasaje ancla añade precisión. Aun así, un ancla demasiado corta puede ser ambigua y una coincidencia literal puede fallar por OCR, saltos de línea o normalización.

La mejor interpretación combina documento, ubicación, evidencia y una regla clara: **¿se considera relevante cualquier fragmento del documento o solo uno que contiene soporte suficiente?** Las métricas dependen de esta decisión.

Si una pregunta necesita dos evidencias, un Hit Rate de 1 por encontrar solo una no comprueba suficiencia. Conviene revisar cobertura de todas las evidencias y corrección de la respuesta.

## 6. Qué ocurre cuando cambias la fragmentación

Si el golden set apunta únicamente a `chunk_17` y vuelves a dividir documentos, `chunk_17` podría representar otro texto. La comparación deja de medir la misma referencia.

Conserva anclas estables a documento, versión y pasaje, y vuelve a resolver cuáles son los fragmentos relevantes de cada configuración. Esto permite que la línea base y la extensión tengan límites de fragmentación distintos sin que la verdad de referencia cambie a conveniencia.

## 7. Composición y límites de la muestra

El taller pide diez preguntas con **al menos dos negativas**; hay ocho respondibles solo si se eligen exactamente dos negativas. La entrega archivada eligió esa distribución. Incluye variedad de redacción y dificultad: paráfrasis, códigos, condiciones, información en distintos documentos y ausencias reales. Esta diversidad sirve para identificar fallas, pero diez casos no representan automáticamente el universo de uso.

Las negativas deben comprobarse contra el corpus declarado. Una pregunta difícil de buscar no es necesariamente negativa. Y una pregunta global como «¿qué temas se repiten en todos los documentos?» puede ser respondible, aunque un top-5 local no aporte toda la cobertura.

> [!abstract] Para recordar
> La etiqueta define el problema que estás midiendo. Antes de calcular, fija corpus, versión, unidad de relevancia y población de preguntas.

## El golden set real y su criterio de acierto

El archivo entregado contiene diez preguntas: cuatro simples, tres multi-fragmento, dos negativas y una adversarial respondible. Las ocho respondibles forman el denominador de Hit y MRR. `evaluation.py` declara respondible un ítem si `documentos_fuente` no está vacío; cada hit acierta si su documento pertenece a esa lista y su texto normalizado contiene `fragmento_esperado`. El nombre «multi» no obliga al código a exigir todos los documentos.

Se incluyó además `evidencias_esperadas` para los casos multi-fragmento. El evaluador de Hit/MRR no consume ese campo; una comprobación separada mide presencia literal de las anclas. El ejemplo es valioso porque muestra la distancia entre **escribir una anotación rica** y **hacer que la métrica realmente la utilice**. Las cadenas literales pueden fallar ante paráfrasis o frente a un pasaje alternativo válido: una ausencia de ancla exige revisión semántica, además de la cuenta.


**Fuente:** PDF, pp. 3, 5, 7, 10 y 13. La separación explícita entre los tres niveles amplía el problema planteado en la página 10.

### Un error de anotación en el ejemplo del laboratorio

La inspección de los documentos `nimbus_remoto.md` y `nimbus_gastos.md` permite detectar un problema del ítem 4 de `golden_ejemplo.json`: la pregunta pide trámites con aprobación **30 días antes**, pero su respuesta esperada incluye presentar facturas **dentro de los 30 días después** del gasto. Compartir «30 días» no hace iguales ambas condiciones, y el documento de gastos no exige esa aprobación anticipada. La regla de trabajo desde el exterior sí establece aprobación de Recursos Humanos con 30 días de anticipación.

Ese ítem mezcla una regla pertinente con otra cuyo plazo tiene sentido temporal diferente. La solución de evaluación es revisar la pregunta y su referencia, conservando el original para explicar el hallazgo: puede preguntarse solo por la aprobación anticipada, o reformularse para comparar expresamente ambos plazos. Este hallazgo afecta al golden de ejemplo del laboratorio; no se traslada automáticamente al `golden_set.json` personalizado de las diez preguntas sobre las notas.
