---
title: "55 S10 - Abstención fidelidad y errores del evaluador"
sesion: "10"
fecha: 2026-09-27
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-10.pdf]]"
---

# 55 S10 - Abstención fidelidad y errores del evaluador

[[50 S10 - Guía para comprender el taller RAG|Guía de la sesión 10]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[54 S10 - Hit Rate y MRR con un experimento completo]]

Siguiente: [[56 S10 - Elegir una extensión y comprobar su efecto]]

## 1. Abstenerse es una decisión del sistema

Abstenerse significa declarar que no se dispone de evidencia suficiente para responder. Puede evitar una respuesta inventada, pero también puede negar una respuesta que sí era posible. Por eso «se abstuvo mucho» no basta para evaluar calidad.

Compara dos preguntas del corpus ficticio: una solicita el plazo de equivalencias, cuya evidencia está disponible; otra pide una política de mascotas que no aparece en los documentos. Abstenerse en la segunda es adecuado. En la primera, revela un problema que necesita diagnóstico.

## 2. La matriz de cuatro situaciones

![[39-s10-matriz-abstencion.png]]

**Cómo leerla:** las filas representan lo que la referencia permite responder; las columnas, la decisión observada. Los dos colores favorables corresponden a responder cuando hay evidencia y abstenerse cuando falta. Aun así, «responder» no significa «responder correctamente»: la celda correspondiente requiere una evaluación adicional del contenido.

El taller pide dos tasas con denominadores distintos:

$$A_{correcta}=\frac{\text{negativas con abstención}}{\text{total de negativas}}$$

$$A_{indebida}=\frac{\text{respondibles con abstención}}{\text{total de respondibles}}$$

La primera debería ser alta; la segunda, baja. Si no hay casos de alguna población, su tasa no está definida: se reporta como no aplicable, no se inventa un cero.

## 3. Un ejemplo completo

Tenemos ocho respondibles y dos negativas. El sistema se abstiene ante una negativa y ante dos respondibles:

$$A_{correcta}=1/2=0{,}50$$

$$A_{indebida}=2/8=0{,}25$$

Hubo tres abstenciones entre diez preguntas, es decir, 30 % de abstención global. Ese 30 % mezcla decisiones correctas e indebidas y no sustituye las dos tasas.

Un sistema que siempre se abstiene consigue 100 % de abstención correcta sobre negativas, pero también 100 % de abstención indebida sobre respondibles. Celebrar solo la primera tasa premiaría un asistente inútil.

**Matiz:** si la respuesta existía en el corpus original pero se perdió antes del prompt, abstenerse puede ser la decisión prudente del generador. La tasa indebida señala el fallo del sistema completo respecto de su referencia; no demuestra automáticamente un defecto del generador.

## 4. El evaluador también puede fallar

El PDF explica que había tres redacciones distintas del marcador de abstención. Una comparación literal puede tratar como diferentes dos frases equivalentes por una tilde o un punto y reportar una tasa cero aunque el sistema sí se abstenga.

La versión mostrada comparte la frase «El corpus no contiene información suficiente.» y normaliza minúsculas, tildes, puntuación y espacios antes de buscarla en la respuesta.

El detalle técnico importa: el fragmento de código de la diapositiva usa **inclusión de cadena** (`in`), no igualdad de toda la respuesta. Eso admite texto adicional, pero también puede producir falsos positivos si el modelo cita la frase y luego da una respuesta sin fundamento.

Tampoco reconoce necesariamente paráfrasis como «No puedo determinarlo con estos documentos». La normalización soluciona variaciones de escritura; no es comprensión semántica de la decisión.

Una ampliación posible es producir un campo estructurado de estado y revisar su coherencia con la respuesta. Sigue haciendo falta validar el evaluador con ejemplos claros de abstención, respuesta y casos ambiguos.

## 5. Por qué el coseno no es un detector universal de ausencia

Un umbral puede ayudar si lo calibras con casos representativos del mismo sistema. Pero su comportamiento cambia con el modelo, el corpus, las preguntas, los filtros y la métrica. Un vecino relativamente cercano puede ser inadecuado; una evidencia útil con redacción distinta puede obtener un valor menor.

Además, un umbral no distingue entre ausencia en los documentos y pérdida durante la ingesta. Para diagnosticar eso necesitas trazabilidad. La cifra no contiene la historia del documento.

## 6. Evaluar la respuesta: fidelidad, pertinencia y corrección

Supón que el contexto dice: «Diez días hábiles desde el inicio del período». El sistema responde: «Tienes diez días hábiles desde el inicio del período y debes pagar una tasa de veinte dólares».

La respuesta contiene una afirmación respaldada y otra que el contexto no respalda. Una revisión didáctica por afirmaciones daría una de dos sustentadas. La [métrica de fidelidad de RAGAS](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/) sigue esa idea de comparar las afirmaciones con el contexto recuperado. El resultado real depende de cómo el evaluador las descomponga y juzgue.

Distingue tres preguntas:

| Criterio | Pregunta | Contraejemplo |
| --- | --- | --- |
| Fidelidad | ¿El contexto respalda lo afirmado? | Se añade una tasa que no aparece. |
| Pertinencia | ¿Se atiende lo que preguntó el usuario? | Se repite información verdadera de matrícula cuando se preguntó por equivalencias. |
| Corrección y completitud | ¿La respuesta satisface la referencia y conserva condiciones? | Se omite desde cuándo empieza a correr el plazo. |

La [relevancia de respuesta en RAGAS](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/answer_relevance/) evalúa alineación con la pregunta; no debe interpretarse como una prueba suficiente de verdad. Una respuesta puede estar bien enfocada y ser falsa. También puede ser fiel a un documento desactualizado y no describir la regla vigente.

## 7. Citas y afirmaciones

Una cita permite rastrear el origen, pero su sola presencia no demuestra soporte. Para revisar una respuesta, separa afirmaciones y comprueba que la fuente citada respalde cada una. Una referencia al documento correcto puede apuntar a una sección que no contiene la evidencia.

> [!question] Comprueba tu comprensión
> Si Hit Rate@5 = 1 y MRR@5 = 1, ¿puede la respuesta ser incorrecta?
>
> Sí. La primera evidencia relevante llega siempre en primer lugar, pero el generador aún puede omitir condiciones, combinar reglas incompatibles o inventar detalles.

**Fuente:** PDF, pp. 10–11 y 13. El ejemplo, la matriz y las limitaciones del detector son desarrollos didácticos basados en la operación mostrada.
