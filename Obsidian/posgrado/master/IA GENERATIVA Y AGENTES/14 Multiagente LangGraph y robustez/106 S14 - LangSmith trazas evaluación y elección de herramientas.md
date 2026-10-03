---
title: "106 S14 - LangSmith trazas evaluación y elección de herramientas"
created: 2026-10-02
fecha: 2026-10-01
capitulo: 14
sesion: "14"
tags:
  - maestria/ia-generativa
  - agentes/robustez
  - estudio
---

# 106 S14 - LangSmith trazas evaluación y elección de herramientas

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|Índice de S14]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Una **traza** representa una ejecución completa. Dentro contiene eventos o spans: clasificación, llamada al modelo, consulta, recuperación y respuesta. Un **dataset de evaluación** guarda preguntas y referencias esperadas. Un **evaluador** calcula criterios sobre las respuestas o sus trayectorias. Tener una traza no demuestra éxito; permite localizar errores y medirlos.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 14/09-traza-y-evaluacion.png]]

La petición registra lo solicitado y sus límites. La caja central conserva la propuesta y lo que efectivamente se ejecutó. El cierre distingue respuesta completa, parcial y rechazo. La evaluación utiliza esos registros para preguntar por corrección y cumplimiento. Las flechas muestran el orden lógico de los eventos; los eventos también necesitan identidad y relación con la tarea.

## Qué registrar

Para una consulta de ventas conviene guardar pregunta, herramienta, argumentos validados, identificador de llamada, resultado, tokens cuando existan, tiempo y motivo de parada. Para una acción protegida también la propuesta presentada y su aprobación o rechazo. Un rechazo es parte de la traza; omitirlo haría parecer que la acción nunca se intentó.

Los prompts, resultados y documentos pueden contener datos personales o internos. En la modalidad cloud del tutorial, activar el rastreo transmite esos registros al servicio. Configurar secretos mediante variables de entorno no anonimiza las trazas. Debes decidir qué contenido registrar y aplicar redacción antes de enviarlo cuando corresponda.

El tutorial muestra `LANGSMITH_TRACING`, `LANGSMITH_API_KEY` y un proyecto opcional. Para un bucle propio propone `@traceable` o envolver el cliente. La [guía de trazas](https://docs.langchain.com/langsmith/observability-quickstart) confirma las vías de instrumentación y configuración. Las notas no activaron rastreo ni crearon una cuenta.

## Tres costos separados

| Componente | Qué significa su costo |
| --- | --- |
| Bibliotecas | Licencia de los paquetes, distinta de ejecutar infraestructura |
| Modelo | Tokens, cómputo o cuota según el proveedor y entorno |
| Observabilidad | Asientos, trazas, retención y demás consumo contratado |

Según el tutorial, los paquetes utilizados tienen licencia MIT. Eso no vuelve gratuitos todos los servicios o servidores. La H200 no cobra tokens al estudiante en el ejemplo; sigue teniendo un costo operativo institucional.

La página oficial consultada el 1 de octubre de 2026 coincide en Developer: 0 USD, un asiento, hasta 5 000 trazas base/mes; Plus: 39 USD por asiento/mes y hasta 10 000 trazas base/mes. La retención base es 14 días y la extendida 180, con cargos adicionales. Hay consumo más allá de lo incluido; estos valores no son una cotización de costo total. [Planes y precios](https://www.langchain.com/pricing).

## Elegir por el problema de la tarea

| Necesidad | Pieza que la cubre | Lo que todavía debes diseñar |
| --- | --- | --- |
| Entender y ajustar un bucle pequeño | Bucle propio | Ejecución, límites y errores visibles |
| Obtener un agente empaquetado | `create_agent` | Contratos, política y evaluación |
| Bifurcar, pausar o recuperar estado | LangGraph | Nodos, rutas y persistencia apropiada |
| Auditar y comparar ejecuciones | LangSmith o trazas locales | Dataset, verificador y registro útil |

La instalación del PDF fija versiones específicas: LangGraph 1.2.12, langchain-openai 1.6.7, langchain-anthropic 1.7.5, LangChain 1.4.3 y LangSmith 0.14.2. Se conservan como la configuración declarada y comprobada por el docente, sin afirmar que sean las más recientes ni instalar ese entorno aquí. Reproducir su demo requiere además datos, servidor y scripts que no se adjuntaron.

El cierre del curso anuncia Taller 3 para sábado 3 de octubre de 2026, con peso de 25 %, baseline de agente único y al menos tres herramientas. Multiagente, estas bibliotecas y sus servicios aparecen como extensiones. Estas consignas explican el curso; no son órdenes de entregar, desplegar o conectarse a un servicio.

Fuente: PDF 11–15 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/tutorial-langgraph.pdf#page=11|tutorial-langgraph.pdf]].

Fuente: PDF 30–31 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-14.pdf#page=30|sesion-14.pdf]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/105 S14 - LangChain modelos herramientas RAG y salidas estructuradas|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/107 S14 - Notebook del jueves laboratorio y repaso resuelto|Siguiente]] →
