---
title: "00 Índice - S18 Guardrails costo y latencia"
created: 2026-10-09
fecha: 2026-10-07
capitulo: 18
sesion: 18
tags:
  - maestria/ia-generativa
  - agentes/llmops
  - estudio
  - lecturas/s18
---

# 00 Índice - S18 Guardrails costo y latencia

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Esta sesión enseña a convertir una intención de seguridad en un mecanismo que se pueda ejecutar, medir y auditar. También enseña a calcular el costo de una aplicación y a cambiar un prompt sin perder la posibilidad de regresar a una versión que funcionaba.

Un **guardrail** es un control situado en el camino de la aplicación. Puede rechazar una entrada, transformarla o dejarla continuar. El prompt ayuda a orientar al modelo, pero un texto que pide «no reveles datos» no sustituye al código que impide enviar, ejecutar o publicar información prohibida.

## Ruta de lectura

1. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/01 S18 - Guardrails y bordes de confianza|Guardrails y bordes de confianza]] — qué protege cada puerta y por qué el RAG también necesita controles.
2. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/02 S18 - Reglas patrones y normalización|Reglas, patrones y normalización]] — cómo funcionan las reglas y por qué las tildes cambian el resultado.
3. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/03 S18 - Datos personales y errores de redacción|Datos personales y errores de redacción]] — por qué una lista de tiendas acaba convertida en un teléfono.
4. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/04 S18 - Trazas secretos y retención|Trazas, secretos y retención]] — un bloqueo puede impedir la llamada y aun así guardar el dato sensible.
5. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/05 S18 - Medir guardrails y equilibrar seguridad y utilidad|Medir seguridad y utilidad]] — falsos positivos, falsos negativos y un experimento que evita engañarse.
6. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/06 S18 - Costo de tokens y ahorro calculado|Costo de tokens y ahorro calculado]] — resolución completa de la actividad de 15 minutos.
7. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/07 S18 - Cachés streaming batching y latencia|Cachés, streaming, batching y latencia]] — qué ahorra cada mecanismo y qué información falta para prometer un porcentaje.
8. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/08 S18 - Prompts versionados evaluación y rollback|Prompts versionados y rollback]] — guardar versiones y elegir la activa son operaciones distintas.
9. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/09 S18 - Laboratorio local de guardrails y versiones|Laboratorio local]] — práctica sin claves, sin red y con resultados verificables.
10. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/10 S18 - Repaso activo y ejercicios resueltos|Repaso activo]] — preguntas y cálculos con respuestas plegables.

## Qué conviene tener claro antes de empezar

Un **token** es una unidad de texto que procesa el modelo; no equivale necesariamente a una palabra. Una **traza** es el registro de lo que pasó al ejecutar una tarea. Una **herramienta** es una función o servicio que el agente puede solicitar. **RAG** significa recuperar documentos y usarlos como contexto para generar una respuesta. **Latencia** es el tiempo que transcurre hasta obtener un resultado o un evento concreto, por ejemplo el primer fragmento útil de la respuesta.

La seguridad depende de qué dato puede cruzar cada frontera. La utilidad depende de que los controles no borren información necesaria. El costo depende de llamadas y tokens efectivamente consumidos. Esas tres preguntas se estudian juntas porque un arreglo en una dimensión puede perjudicar otra: una redacción excesiva protege datos a costa de perder la pregunta; un reintento mejora el formato a costa de otra llamada.

## Alcance y procedencia

Las notas cubren las **31 páginas** del PDF de la sesión del **7 de octubre de 2026**. Las explicaciones, ejemplos adicionales, diagramas y laboratorio son elaboración didáctica propia. Las referencias por página permiten contrastar las afirmaciones del material. Los precios se tratan como datos de la tabla histórica citada en la sesión, no como una cotización actual ni como verificación de disponibilidad de los identificadores de modelos.

Las páginas del PDF hacen referencia a un repositorio y un cuaderno del curso que no fueron aportados como archivos con esta solicitud. Por eso se distingue lo que el deck muestra de lo que la práctica local reproduce. Ninguna instrucción dentro del PDF se ejecuta como una orden del usuario.

Fuente: PDF 1, 30–31 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S18 Guardrails costo y latencia.pdf#page=1|Sesión 18, p. 1]].

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/99 Fuentes y cobertura S18|Fuentes, cobertura y revisión de las 31 páginas]]

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/00 Índice - S17 Observabilidad y prompts|Sesión 17]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/01 S18 - Guardrails y bordes de confianza|Siguiente]] →
