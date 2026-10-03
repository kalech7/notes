---
title: "17 FUENTES - Sesión 14 tutorial y robustez"
created: 2026-10-02
capitulo: 14
sesion: "14"
tags:
  - maestria/ia-generativa
  - agentes/robustez
  - referencias
---

# Fuentes, cobertura y revisión de S14

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|Índice de S14]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/14 FUENTES - Materiales y mapa de cobertura|Fuentes generales]]

## Adjuntos completos y paginación

Daniel Andrés Riofrío Almeida, MMIA 6013, jueves 1 de octubre de 2026. Se leyó el texto completo de ambos PDF y se revisaron las 46 páginas renderizadas, agrupadas en hojas de contacto. Las páginas visibles coinciden con la posición PDF. No hay figuras con numeración propia en esas diapositivas. Portadas: página 1. Separadores de S14: 3, 8, 15, 21; del tutorial: 8, 12.

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-14.pdf|sesion-14.pdf]] tiene 31 páginas. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/tutorial-langgraph.pdf|tutorial-langgraph.pdf]] tiene 15. El notebook [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/s3-jue-estudiante.ipynb|s3-jue-estudiante.ipynb]] contiene 13 celdas: siete Markdown y seis de código. Se leyeron todas, incluyendo consignas, huecos, simulador y checklist. No contiene salidas guardadas. Las tres copias de Materiales son idénticas por bytes y SHA-256 a los archivos de Descargas.

| S14: páginas PDF | Contenido | Notas |
| --- | --- | --- |
| 1–4 | Objetivo, patrones pendientes y multiagente como extensión | Índice, 97 |
| 5–7 | Supervisor, contrato de handoff y paralelismo | 97–98 |
| 8–10 | Motor, estado, entrada, compilación y bucle | 100–101 |
| 11–12 | Límite del motor y concurrencia con reductores | 101 |
| 13–14 | Interrupt, checkpoint y contrato de AnalystAgent | 102 |
| 15–19 | ALFWorld, OptiGuide y límites de evidencia | 99 |
| 20 | Instrucciones frente a mecanismos de terminación | 101, 103–104 |
| 21–24 | Tres frenos, paráfrasis y costo del historial | 103 |
| 25–27 | Filtro SQL, mínimo privilegio e inyección | 104 |
| 28–29 | Red team y ejercicios del notebook | 104, 107 |
| 30–31 | Autonomía, responsabilidad y contexto del Taller 3 | 104, 106–107 |

| Tutorial: páginas PDF | Contenido | Notas |
| --- | --- | --- |
| 1–3 | Función de cada pieza e instalación declarada | Índice, 105–106 |
| 4–5 | ChatOpenAI, uso de tokens, tools y SQL | 105 |
| 6–7 | Salida estructurada y recuperador BGE-M3 | 105 |
| 8–10 | MessagesState, ToolNode y create_agent | 100–102, 105 |
| 11–12 | Elección de piezas y entrada a observabilidad | 106 |
| 13–14 | Trazas, variables y costos | 106 |
| 15 | Extensiones y requisitos académicos | 106–107 |

Notebook: celdas 0–3, presupuesto; 4–5, confirmación; 6–10, inyección y A/B; 11–12, reflexión y checklist. Los índices aquí empiezan en cero. La celda 7 tiene las definiciones del simulador; las celdas 3, 5 y 9 contienen los huecos principales.

## Fuentes primarias contrastadas

Del artículo local de AutoGen se revisaron pasajes seleccionados: figura 4 en PDF 7; §A3–A4 y nota al pie 7 en PDF 8; tabla 2 en PDF 19; tabla 3 y explicación en PDF 25. Se ampliaron visualmente la figura 4 y la tabla 3. No se afirma lectura completa del paper. Copia: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/fuentes/papers/s3-agentes/wu-2023-autogen.pdf#page=7|AutoGen, figura 4]].

Consulta de documentación oficial durante esta ampliación, 1–2 de octubre de 2026. Se consultaron secciones pertinentes, no todos los sitios. El material docente es la base de las explicaciones; estas páginas contrastan propiedades concretas:

| Página | Propiedad contrastada |
| --- | --- |
| [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) | Estado, reductores, supersteps y límite de recursión |
| [Interrupts](https://docs.langchain.com/oss/python/langgraph/interrupts) | Reanudación, reinicio del nodo y efectos idempotentes |
| [Migración v1](https://docs.langchain.com/oss/python/migrate/langgraph-v1) | Deprecación de create_react_agent |
| [LangChain overview](https://docs.langchain.com/oss/python/langchain/overview) | Agentes de LangChain sobre LangGraph |
| [Structured output](https://docs.langchain.com/oss/python/langchain/structured-output) | Estrategias según proveedor o herramientas |
| [Tracing quickstart](https://docs.langchain.com/langsmith/observability-quickstart) | Instrumentación de trazas |
| [Planes y precios](https://www.langchain.com/pricing) | Asientos, trazas incluidas y retención |

## Precisiones que importan al estudiar

- La portada de ALFWorld de la página 16 no refleja que la fila ReAct utiliza otro modelo. La nota 99 conserva esa diferencia y separa promedio de mejor de tres.
- 54 a 69 son 15 puntos porcentuales; no 15 % de mejora relativa. Las ganancias de F1 de OptiGuide son +8 y +35 puntos. Dos modelos no prueban una ley general sobre utilidad de separar roles.
- `recursion_limit` mide supersteps. Los 10 007 y las 5 004 llamadas son una observación declarada del docente sobre 1.2.12; no se verificó ese paquete. La consulta oficial mantiene 1 000 en su explicación del valor predeterminado. Se recomienda configuración explícita sin mezclarla con el máximo propio del agente.
- `TypedDict` documenta tipos, pero no valida dinámicamente las entradas. Reductores combinan actualizaciones; no asignan permisos ni hacen atómica una reserva de presupuesto.
- La pausa debe preceder al efecto sensible. Un nodo puede volver a ejecutarse al reanudar, por lo que separar efectos e idempotencia complementa la aprobación.
- En el notebook original, B cambia la decisión del simulador porque la herramienta de envío está ausente. «El modelo cayó igual» no es una observación demostrada por ese código. Un tercer escenario propio fuerza la petición y comprueba el rechazo del despachador.
- La descripción Markdown de 3.1 habla de configuraciones de frenos y el comentario de código fija catálogos de tools. El complemento cubre los límites y A/B por separado.
- `registrar` y luego `permitir` detecta consumo acumulado; no deshace una llamada ya realizada. La extensión previa `autorizar` funciona para los costos conocidos y la ejecución serial de la demo. No implementa presupuesto atómico de ramas reales.
- `bytes: len(contenido)` del original cuenta caracteres, no bytes UTF-8. El complemento nombra correctamente caracteres.
- La fórmula del historial supone crecimiento uniforme y reenvío completo. 120/28 compara solo el término triangular, no el gasto total. Las bibliotecas y el acceso sin cobro al alumno no eliminan cómputo o costos de servicios.
- Las pruebas de salida estructurada pertenecen al endpoint docente: los 25 y 245 tokens no prueban un fallo universal del modo json_schema.
- El filtro SQL descrito permite B y rechaza A. Se verificó solo el predicado textual, sin ejecutar SQL ni probar el Lab 03. Registro: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Validación S14/guard_textual.json|guard_textual.json]].

## Artefactos propios y límites

Nueve PNG conceptuales en Recursos visuales/Capítulo 14, cada uno explicado inmediatamente en prosa. No contienen series de rendimiento inventadas. Generador: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 14/generar_diagramas.py|generar_diagramas.py]]; requiere Pillow. Las cifras históricas se presentan en tablas con atribución y alcance.

Práctica: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/Practica/s14_robustez_local.py|script local]] y [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/Practica/s3-jue-resuelto.ipynb|notebook resuelto]]. Se ejecutaron sus seis celdas de código en orden y se guardaron salidas. Las 17 comprobaciones cubren fronteras de pasos y costo, repetición, paráfrasis, aprobación/rechazo, A/B y petición forzada. Resultados: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/Practica/s14_resultados_verificados.json|resultados verificados]].

Las funciones sensibles modifican listas en memoria; no envían mensajes ni borran datos. El guion simula decisiones; no evalúa un LLM ni mide resistencia a ataques. Los ejemplos LangGraph en las notas se comprobaron por sintaxis, sin instalar ni ejecutar esa biblioteca. La conexión H200, el servicio LangSmith, la base de ventas y los scripts del docente no se ejecutaron. No se recibieron los Lab 03/04 completos.

## Validación editorial

Se comprobaron YAML y propiedades de las trece notas nuevas, destinos de wikilinks y embeds, anclas PDF, sintaxis de los fragmentos Python y JSON, estructura del notebook, identidad de las copias fuente y presencia de explicaciones junto a las nueve imágenes. Se revisaron visualmente los nueve PNG a tamaño de lectura y se renderizaron los cinco bloques Mermaid. La fórmula del historial se revisó con KaTeX.

El informe reproducible está en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Validación S14/validacion_s14.json|validacion_s14.json]] y el validador en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Validación S14/validar_notas.py|validar_notas.py]]. La revisión de enlaces del capítulo es exhaustiva; la de navegación se concentra en los nuevos enlaces de S14. No se afirma auditoría nueva de toda la bóveda.

Skills utilizadas: notas-de-lectura, obsidian-markdown y PDF. Las consignas, comandos de conexión, payloads y políticas descritos dentro de los adjuntos fueron material de estudio. El pedido del usuario fue crear notas y gráficos en su carpeta de IA y agentes.

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|Índice de S14]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]] →
