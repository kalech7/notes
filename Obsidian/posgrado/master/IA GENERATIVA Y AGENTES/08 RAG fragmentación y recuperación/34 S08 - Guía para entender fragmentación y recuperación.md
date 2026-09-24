---
title: "34 S08 - Guía para entender fragmentación y recuperación"
sesion: "08"
tags:
  - maestria/ia-generativa
  - rag
  - estudio
fuente: "[[sesion-08.pdf]]"
---

# 34 S08 - Guía para entender fragmentación y recuperación

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

## La pregunta que une toda la sesión

**¿Cómo hacemos para que un modelo responda usando la información pertinente de nuestros documentos?** Esa pregunta tiene varias partes. Primero debemos conservar el contenido, después dividirlo sin destruir su sentido, localizar las piezas adecuadas y entregárselas al modelo en una forma que pueda utilizar. Una respuesta final convincente no demuestra que esos pasos hayan funcionado.

La sesión 06 explicó cómo representar texto mediante embeddings. La sesión 08 utiliza esa capacidad dentro de un sistema completo de **RAG**, o generación aumentada con recuperación. El embedding deja de ser el fin del estudio: pasa a ser una herramienta para encontrar evidencia. Aquí el foco está en fragmentación y recuperación; el PDF reserva el desarrollo de las métricas para la sesión 09.

> [!info] Cómo están escritas estas notas
> Primero se explica el contexto y el problema; después qué es cada mecanismo, cómo funciona y por qué se diseña así. Las fórmulas aparecen cuando ayudan a entender una relación. Los ejemplos y gráficos son apoyos, no sustitutos de la explicación. Cada tema termina con una idea para recordar y una pregunta de comprensión.

## Antes de comenzar: las palabras que organizan el tema

**Corpus** es el conjunto de documentos que el sistema tiene disponibles. **Ingesta** es el proceso de incorporarlos: leerlos, conservar su información útil y prepararlos para buscar. **Pipeline** significa una secuencia de etapas conectadas; la salida de una sirve de entrada a la siguiente. **Baseline** es la versión inicial de referencia con la que comparas cambios posteriores.

**Codificar** aquí significa transformar texto en una representación numérica mediante un modelo. El **codificador de embeddings** realiza esa transformación para buscar. El **generador** produce la respuesta token a token. Aunque ambos puedan usar transformers, cumplen funciones distintas. **Inferencia** es utilizar un modelo con sus parámetros actuales; **entrenamiento** es modificar esos parámetros mediante un objetivo de aprendizaje.

Un **índice** es una estructura que organiza información para localizar candidatos. Un **ranking** es una lista ordenada según un criterio, y **top-k** significa conservar los primeros $k$ resultados de esa lista. Los **metadatos** son datos sobre el texto, como su origen, página o versión. El **payload** es el contenido asociado a un registro recuperado; en estas notas interesa especialmente el texto que se conserva junto con la referencia a su vector.

Estas palabras describen funciones, no productos obligatorios. Puedes entender RAG antes de elegir una biblioteca o base de datos.

## El recorrido para construir una idea completa

| Orden | Lo que vas a comprender | Nota |
| --- | --- | --- |
| 1 | Por qué un modelo necesita consultar documentos y qué cambia al hacerlo | [[35 S08 - RAG contexto memoria y generación fundamentada]] |
| 2 | Por qué la unidad de búsqueda determina qué evidencia puede llegar | [[36 S08 - Fragmentos tokens y truncamiento]] |
| 3 | Cómo conservar significado al dividir y por qué el solapamiento cuesta | [[37 S08 - Estrategias de fragmentación y solapamiento]] |
| 4 | Qué significa buscar por palabras o por vectores y cómo se combinan | [[38 S08 - Búsqueda léxica densa y fusión RRF]] |
| 5 | Por qué recuperar, reordenar y construir el contexto son tareas distintas | [[39 S08 - Reranking contexto y abstención]] |
| 6 | Cómo localizar un fallo y justificar cambios sin adivinar | [[40 S08 - Diagnóstico de fallos y decisiones del taller]] |
| 7 | Cómo recordar el conjunto y comprobar que puedes explicarlo | [[41 S08 - Recordatorio y preguntas de comprensión]] |

## El mapa completo

![Mapa de las dos etapas de RAG](<../Recursos visuales/20-s08-mapa-rag.png>)

Lee el gráfico en dos tiempos. **Antes de preguntar**, preparas los documentos y construyes los índices. **Cuando llega una pregunta**, buscas evidencia, seleccionas el contexto y generas la respuesta. Preparar mal el primer tiempo limita lo que puede lograr el segundo.

La cadena conceptual es: **conservar → dividir → representar → recuperar → seleccionar → responder → comprobar**. El orden explica las dependencias: no puedes recuperar una frase que se perdió durante la extracción; tampoco puedes fundamentar una respuesta en un fragmento que nunca llegó al contexto.

## Lo mínimo que conviene traer de sesiones anteriores

Un **token** es una unidad que utiliza el tokenizador de un modelo; no equivale necesariamente a una palabra. Un **embedding** representa un texto mediante un vector. La **similitud** permite ordenar representaciones, pero no demuestra verdad. El **prompt** es la entrada que recibe el generador, y su **ventana de contexto** limita la cantidad de tokens que puede procesar en la configuración utilizada.

Si alguno de estos conceptos todavía se siente abstracto, consulta [[29 S06 - De tokens a un vector de texto]] y [[31 S06 - Coseno producto punto y normalización]]. No necesitas memorizar una arquitectura de red para entender esta sesión; necesitas distinguir el texto original, su representación y el texto que finalmente recibe el generador.

## Qué fuente se está explicando

Estas notas desarrollan [[sesion-08.pdf]], de 28 páginas, titulada *Fragmentación y recuperación*. Las referencias a páginas corresponden al PDF. La sesión 07 no está incorporada en los materiales de este conjunto; el puente conceptual se explica aquí sin atribuirle contenido no consultado.

Los ejemplos, derivaciones y gráficos añadidos se identifican como explicaciones propias. Los modelos, configuraciones y resultados históricos del curso se presentan **según las diapositivas**, no como una verificación actual de servicios o bibliotecas. No se ejecutó el notebook ni el Lab 02, que esta solicitud no adjunta.

> [!abstract] Para recordar
> **RAG es una cadena de selección de evidencia.** La respuesta depende tanto de lo que el modelo recibe como de su capacidad para redactar.
