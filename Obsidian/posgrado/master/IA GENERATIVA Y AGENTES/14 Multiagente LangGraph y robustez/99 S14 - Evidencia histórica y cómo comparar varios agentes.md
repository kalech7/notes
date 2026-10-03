---
title: "99 S14 - Evidencia histórica y cómo comparar varios agentes"
created: 2026-10-02
fecha: 2026-10-01
capitulo: 14
sesion: "14"
tags:
  - maestria/ia-generativa
  - agentes/robustez
  - estudio
---

# 99 S14 - Evidencia histórica y cómo comparar varios agentes

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|Índice de S14]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Los materiales utilizan AutoGen, Wu et al. (2023), para discutir cuándo varios agentes aportan algo. **Una ablación** elimina o cambia una pieza manteniendo lo demás comparable; permite investigar qué contribución tiene esa pieza. Comparar sistemas que también usan modelos distintos introduce un factor de confusión.

## ALFWorld: diagnóstico de bucles

ALFWorld contiene tareas interactivas en ambientes domésticos simulados. La tabla 3 del artículo informa resultados sobre 134 tareas no vistas, con tres intentos. La sesión presenta estas cifras:

| Sistema | Éxito promedio (%) | Mejor de 3 (%) |
| --- | ---: | ---: |
| ReAct | 54 | 66 |
| ALFChat, 2 agentes | 54 | 63 |
| ALFChat, 3 agentes | 69 | 77 |

Promedio y mejor de tres responden preguntas diferentes. El mejor de tres beneficia a quien puede repetir y seleccionar; no describe lo que obtienes necesariamente en una sola ejecución.

Los dos agentes son asistente y ejecutor. El tercero aporta conocimiento de sentido común cuando aparecen errores repetitivos: encontrar un objeto no equivale a haberlo recogido. La mejora de 54 a 69 es **15 puntos porcentuales**; relativa al 54 inicial es aproximadamente 27,8 %. El cambio observado apunta a un mecanismo concreto para salir de bucles.

La página 16 de la sesión agrupa las filas bajo GPT-3.5-turbo, pero la nota al pie 7 del artículo aclara que ReAct usa text-davinci-003. Por tanto, comparar ReAct con ALFChat no aísla únicamente el número de agentes. La comparación entre las variantes de ALFChat está mejor controlada respecto del modelo base.

## OptiGuide: escribir y revisar código

OptiGuide combina un coordinador, un escritor y un revisor de seguridad. La ablación compara el diseño separado con uno en que un agente escribe y revisa. El dataset tiene 100 tareas: mitad seguras y mitad inseguras.

| Modelo de 2023 | F1 con un agente | F1 con varios | Diferencia |
| --- | ---: | ---: | ---: |
| GPT-4 | 88 | 96 | +8 puntos |
| GPT-3.5-turbo | 48 | 83 | +35 puntos |

F1 combina precisión y recall al identificar código inseguro; no es porcentaje de programas correctos ni garantía de seguridad. La ganancia de 35 puntos es 4,375 veces la de 8. Eso describe estos dos experimentos; no establece que toda mejora del modelo reduzca siempre la utilidad de dividir roles.

## Una arquitectura también puede perder

En 120 problemas MATH de nivel 5, la figura 4a informa 26,67 % para debate multiagente y 30,0 % para GPT-4 solo. La diferencia es −3,33 puntos. Otros resultados cualitativos son dos problemas con tres intentos cada uno; no deben presentarse como un benchmark grande.

La sesión sostiene que conviene empezar con un agente funcional y agregar estructura por un problema observado. Para tu propia evaluación: conserva preguntas y verificador, compara mismo modelo, registra éxito, gasto, latencia y errores, y revisa si la mejora persiste en tareas que no usaste para ajustar el diseño. Un agente único con mejor herramienta también es una alternativa experimental relevante.

> [!question]- ¿Los 15 puntos prueban que tres agentes siempre superan a uno?
> No. Están ligados al entorno, modelos, intentos y mecanismo de ese estudio. La hipótesis útil es «un componente que corrige este bucle puede ayudar», y necesita evaluación en otra tarea.

Fuente: PDF 16–20 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-14.pdf#page=16|sesion-14.pdf]].

Contraste seleccionado del artículo local: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/fuentes/papers/s3-agentes/wu-2023-autogen.pdf#page=7|AutoGen · figura 4, PDF 7]], PDF 8 §A3–A4 y nota 7, PDF 19 tabla 2 y PDF 25 tabla 3. No se atribuye lectura completa del artículo.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/98 S14 - Contratos de traspaso y paralelismo|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/100 S14 - Estado nodos y aristas en LangGraph|Siguiente]] →
