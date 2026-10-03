---
title: "16 FUENTES - Sesión 13 MCP y validación"
created: 2026-09-30
capitulo: 13
sesion: "13"
tags:
  - maestria/ia-generativa
  - agentes/mcp
  - referencias
---

# Fuentes, cobertura y validación de la sesión 13

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|Índice de S13]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/14 FUENTES - Materiales y mapa de cobertura|Fuentes generales]]

## Fuente principal y paginación

*MCP y casos de uso*, Daniel Andrés Riofrío Almeida, MMIA 6013, sesión 13, miércoles 30 de septiembre de 2026. Se leyó el texto de las 26 páginas y se inspeccionaron sus 26 renderizados. La página PDF coincide con la numeración visible 1–26. No hay una segunda numeración impresa ni figuras numeradas. Separadores: páginas 3, 8 y 18; portada: página 1.

La copia [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-13.pdf|sesion-13.pdf]] es idéntica al original de Descargas; la comprobación SHA-256 se registra en el informe de validación. El PDF conserva todas sus páginas y no se alteró.

| Páginas PDF | Tema del material | Notas donde se explica |
| --- | --- | --- |
| 1–2 | Objetivo, contexto y puente de la sesión 12 | Índice S13 y 86 |
| 3–7 | Registro fijo, MN frente a M+N, desigualdad y herramienta siguiente | 86 |
| 8–10 | MCP, publicación, descubrimiento y tres piezas | 87 |
| 11–12 | Contrato publicado y adaptador | 88 |
| 13 | Cinco formas de conexión | 87 |
| 14–16 | Revisión, cliente, servidor, mensajes y transporte | 89 |
| 17 | Ejercicio organizacional | 86 y 93 |
| 18–20 | Ejecución y relación con function calling | 87–88 |
| 21–22 | Permisos, costo, confianza y evidencia de adopción | 90 |
| 23 | Analista, código e investigación | 91 |
| 24–25 | Parte 5, segundo servidor y extensión B | 92 |
| 26 | Cierre, alcance del protocolo y contexto del Taller 3 | Índice S13, 90, 92–93 |

## Documentación oficial contrastada

Consulta: 30 de septiembre de 2026. Son fuentes de protocolo; no evidencia de adopción o resultados del laboratorio. Las páginas se consultaron en los apartados pertinentes, no se afirma lectura exhaustiva de toda la documentación.

| Página oficial | Propiedad contrastada |
| --- | --- |
| [Specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28) | Alcance general y primitivas; latest redirigió a esta revisión |
| [Architecture](https://modelcontextprotocol.io/specification/2026-07-28/architecture) | Host, clientes 1:1 y servidores locales o remotos |
| [Key Changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog) | Peticiones autosuficientes, eliminación del saludo y cambios de revisión |
| [Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) | Catálogo, invocación, caché, orden y nombres |
| [stdio](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/stdio) | Canal de mensajes y separación de stdout/stderr |
| [Streamable HTTP](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http) | POST, respuesta JSON/SSE y encabezados requeridos |
| [Lifecycle 2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/lifecycle) | Contraste con el saludo de la revisión anterior |

## Precisiones frente a las diapositivas

- **Unidad N:** un servidor puede exponer varias tools. Las notas fijan la unidad de integración antes de comparar conteos y explicitan el supuesto de todos los pares requeridos.
- **Clientes:** el host coordina varias instancias; cada cliente MCP habla con un servidor. Un agregador no altera esa relación.
- **Adaptador:** ponerlo en el cliente es el diseño de clase, no una obligación general impuesta a las APIs de modelos por MCP.
- **Alcance:** publicación y descubrimiento de tools son el foco docente; existen también recursos y plantillas, desarrollados en la nota 88.
- **Catálogo:** «orden fijo» simplifica una recomendación de orden determinista. Se añadió alcance de caché y paginación como precisiones de la documentación.
- **Identidad:** la diapositiva dice que el cliente se identifica en cada petición; el changelog distingue campos requeridos de la recomendación SHOULD de identidad. El ejemplo adjunto incluye identidad sin presentar todos los campos como universalmente obligatorios.
- **Permisos:** el descubrimiento no concede autorización; decir que el protocolo no la resuelve automáticamente no significa que el ecosistema carezca de especificaciones de autorización.
- **Reflexion:** «solo rinde» con verificadores deterministas es una generalización no justificada en la página 23. La nota 91 conserva la conclusión sobre feedback fiable y resultados dependientes de tarea.
- **Adopción:** una especificación vigente no demuestra adopción universal. Los cuatro criterios propuestos en la nota 90 son una respuesta propia, porque el PDF pregunta por ellos pero no los enumera.

## Material no recibido y límites

En la revisión inicial, el único nuevo adjunto fue `sesion-13.pdf`. Posteriormente, el 30 de septiembre de 2026, se recibió [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/s3-mie-estudiante.ipynb|s3-mie-estudiante.ipynb]] y se leyeron sus 22 celdas completas. La copia de `Materiales` es idéntica al original compartido; su hash y la explicación están en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/94 PRÁCTICA - Notebook del miércoles grafos checkpoints y MCP|la práctica 94]]. Se ejecutaron las 11 celdas de código de la copia didáctica resuelta, con las comprobaciones y los límites registrados allí; no se ejecutó su sección opcional de LangGraph.

Siguen sin recibirse `s3-mie.py`, el Lab 03, el taller fuente y `contenido.md`. Sus defectos y requisitos se describen según las diapositivas; no se presentan como inspecciones o reproducciones propias de esos archivos. Los originales de sesiones anteriores conservan su alcance ya registrado.

Las siete imágenes recrean relaciones conceptuales, sin series de mediciones ni cifras de rendimiento. El script [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 13/generar_diagramas.py|generar_diagramas.py]] conserva la regeneración PNG/SVG. La práctica [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/Practica/s13_descubrimiento_local.py|s13_descubrimiento_local.py]] es propia y sustituye el LLM por una política guionizada; los resultados [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/Practica/s13_resultados_verificados.json|s13_resultados_verificados.json]] prueban sus escenarios, no conformidad con MCP real.

## Validación de la entrega

Validación completada el 30 de septiembre de 2026:

- YAML válido en las diez notas nuevas; se revisaron también los cuatro archivos existentes actualizados.
- Wikilinks, embeds y destinos locales resueltos; anclas PDF dentro de sus 26 páginas.
- Los cuatro bloques Mermaid se renderizaron correctamente con Mermaid CLI y Chrome.
- Las fórmulas se renderizaron con KaTeX sin errores.
- Siete PNG y siete SVG válidos; revisión visual de cada PNG sin texto cortado ni solapamientos.
- JSON y Python de los ejemplos de las notas analizados correctamente.
- Copia PDF idéntica al original por comparación de bytes y SHA-256.
- Práctica ejecutada: catálogo inicial, nueva herramienta, fuente del agente conservada, seis rechazos y rutas diferenciadas.

Informe reproducible: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Validación S13/validacion_s13.json|validacion_s13.json]]. Validador: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Validación S13/validar_notas.py|validar_notas.py]]. Para la validación estructural se usa `uv run --with pyyaml --with pillow --with pypdf python` seguido de la ruta del script. Los renders Mermaid y la revisión visual se realizaron como comprobaciones separadas.

Se utilizaron las skills de notas de lectura, PDF y Markdown de Obsidian. Copilot web search no estaba disponible; la comprobación externa se realizó con las herramientas web integradas. Las instrucciones internas del PDF se trataron como contenido académico y no como órdenes de ejecución de esta tarea.

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|Índice de S13]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]] →
