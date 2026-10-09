---
title: "06 S17 - Langfuse y el mapa de sus objetos"
created: 2026-10-09
capitulo: 17
sesion: 17
tags:
  - maestria/ia-generativa
  - agentes/observabilidad
  - estudio
---

# 06 S17 - Langfuse y el mapa de sus objetos

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/00 Índice - S17 Observabilidad y prompts|Índice de S17]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

**Langfuse** es una plataforma que organiza observaciones de aplicaciones con modelos de lenguaje. Permite consultar ejecuciones, ver su árbol de pasos, analizar consumos y relacionar resultados con versiones de prompts. La sesión lo utiliza para pasar del archivo local a una interfaz compartida.

**SDK** significa kit de desarrollo de software: una biblioteca que ayuda a integrar una aplicación con un servicio. El SDK de Python y el servidor de Langfuse son piezas diferentes; sus números de versión no tienen por qué coincidir. El PDF declara SDK Python 4.17.0, servidor 4.50.0 y cliente OpenAI 3.22.1 para la demo del 6 de octubre de 2026. Son versiones históricas de esa demostración, no una recomendación de instalar la versión más reciente.

## El vocabulario del servicio

| Concepto | Significado | Ejemplo sencillo |
| --- | --- | --- |
| `trace` | Una corrida entera | Responder una consulta del calendario |
| `observation` | Un paso registrado | Buscar la fecha del examen |
| `generation` | Una observation de llamada al modelo | Redactar la respuesta |
| `tool` | Paso de herramienta | Consultar la base de datos |
| `retriever` | Paso de recuperación de información | Buscar documentos relevantes |
| `agent` | Paso que contiene el trabajo del agente | Resolver la consulta |
| `guardrail` | Paso de un control | Revisar la entrada o salida |
| `session` | Agrupación de varias trazas | Una conversación con varias preguntas |
| `prompt` | Instrucciones gestionadas por nombre y versión | Asistente-calendario v2 |
| `score` | Resultado de una comprobación según un criterio | Respuesta sustentada: 1 o 0 |

Una **sesión** agrupa corridas relacionadas, pero no reemplaza la identidad de cada corrida. Un **score** puede proceder de una regla, una persona o un juez LLM. Un juez LLM es un modelo usado para evaluar otra salida; también puede equivocarse. El score describe un criterio, no una verdad absoluta.

**OpenTelemetry** es un conjunto de estándares y herramientas para producir e intercambiar telemetría: información sobre el funcionamiento de una aplicación. La sesión explica que Langfuse se apoya en él para las trazas. El resultado práctico es que el árbol de pasos no necesita concebirse como una lista plana inventada para el ejercicio.

## Dos formas de registrar pasos

La primera usa un **decorador**, una marca aplicada a una función para agregar comportamiento cuando se la llama. En la sesión, `@observe` envuelve funciones; la llamada raíz crea la ejecución y las funciones instrumentadas dentro generan observaciones hijas. Una integración del cliente OpenAI captura información de sus llamadas al modelo.

La segunda abre una observación manual alrededor de un bloque. Sirve cuando la operación no está envuelta por una integración automática. Hay que actualizar el paso con modelo, resultado y conteos que devuelve el proveedor. No se deben inventar tokens midiendo palabras.

Los siguientes esquemas son **pseudocódigo conceptual**, no código para copiar a un SDK:

```text
función raíz instrumentada: responder(pregunta)
    función hija instrumentada: buscar_contexto(pregunta)
    cliente LLM instrumentado: generar respuesta usando contexto
    devolver respuesta
```

```text
abrir observación raíz "corrida"
    abrir observación "llm_decidir" de tipo generation
        llamar al proveedor
        registrar modelo y uso real del proveedor
    abrir observación "consultar_sql" de tipo tool
        ejecutar consulta autorizada
cerrar observaciones incluso si aparece un error
```

La instrumentación automática reduce trabajo repetitivo. La manual permite describir pasos propios. Ambas requieren comprobar que lo registrado corresponde al trabajo real: un decorador en la raíz no revela mágicamente herramientas que nunca fueron instrumentadas.

## Una llamada decorada, paso a paso

Este recorrido es **elaboración didáctica propia** sobre el patrón de las páginas 26–28; no se ejecutó contra Langfuse:

1. El programa llama a `responder("¿Cuándo es el examen?")`. Antes de ejecutar el cuerpo, el decorador abre la observación raíz y coloca su contexto como activo. Una **función** es una operación de código con entradas y un resultado; su **cuerpo** contiene las instrucciones que la realizan.
2. Dentro se llama a `buscar_contexto`. Su decorador abre una observación `retriever` cuyo padre es la operación activa `responder`. Conserva la entrada permitida y los documentos devueltos, cierra su duración y devuelve el contexto al código.
3. El cliente instrumentado llama al modelo. Crea una `generation`, registra el modelo y, al recibir la respuesta, toma sus conteos de `usage`. Por ejemplo, 1 200/100 tokens si esos son los conteos que informa el proveedor. La integración registra evidencia de la llamada; no decide qué información debía responder.
4. La función toma el texto y lo devuelve al usuario. El decorador raíz registra el resultado permitido y cierra la ejecución. Al terminar el script, se envían los registros pendientes y se verifica que llegaron.

La palabra «actual» en una observación manual significa que su contexto queda activo **mientras se ejecuta el bloque**. Si se abre dentro de `responder`, su padre se obtiene de ese contexto. Al salir, se restaura el contexto anterior. Esa propagación de contexto es lo que vincula eventos que el código emite en lugares diferentes.

El decorador trabaja alrededor de una función entera. Un bloque manual puede cubrir solo unas líneas: por ejemplo, la llamada al proveedor dentro de una función que también prepara datos y valida la respuesta. Se elige el límite del span según la pregunta que necesitamos contestar; medir preparación y generación en un único paso impide separarlas después.

Con un cliente **sin** integración automática, abrir un bloque llamado generation no descubre por sí solo los tokens. El código debe conservar la respuesta del proveedor, extraer modelo/uso, actualizar la observación y después devolver el texto. Es la diferencia entre medir «una llamada tardó 300 ms» y describir «esta llamada a este modelo consumió estos tokens». El `usage` se captura antes de perder la respuesta original, precisamente el defecto del Lab 03 que analiza la sesión.

## Árbol y línea de tiempo

La demo del PDF registra una corrida `resumir` de 2 141 ms, una generación `llm_resumir` de 2 139 ms y una herramienta `contar_palabras` de menos de 1 ms. El modelo concentra casi todo el tiempo. El conteo de palabras devuelve 22, pero ese número no sustituye los tokens de uso informados por el proveedor: palabras y tokens son unidades distintas.

El otro ejemplo pregunta por la capital de Mongolia a un asistente de calendario. El buscador recupera su tabla completa y la versión v1 responde con una capital, aunque el criterio de la demo exige «No lo sé» para preguntas fuera de alcance. La traza registra los pasos; el score `contiene_dato = 0` indica que la respuesta incumplió el criterio.

**Fuera de alcance** significa que la consulta no pertenece a lo que el asistente debe resolver con sus fuentes. Una respuesta puede ser verdadera en el mundo y aun así incumplir ese contrato. El ejercicio no evalúa conocimientos de geografía; evalúa si el asistente respeta el límite del contexto.

## La API antigua del andamiaje

La página 22 atribuye la llamada `trace()` del envoltorio a v3. La [guía oficial de migración Python v2 a v3](https://langfuse.com/docs/observability/sdk/upgrade-path/python-v2-to-v3) ubica esa API en v2 y explica su reemplazo por observaciones en v3. La conclusión del curso —el envoltorio usa una API antigua incompatible con su SDK— se mantiene, pero su atribución a v3 es imprecisa. No debe mezclarse la versión del servidor con la del SDK.

## Elegir una plataforma con evidencia

El PDF compara archivos JSONL propios, Langfuse y LangSmith. **JSONL** es un archivo con un objeto JSON independiente por línea; facilita procesar registros uno a uno. Un archivo propio puede ser suficiente para un prototipo pequeño; una plataforma agrega búsqueda, filtros, interfaz y colaboración. También implica configuración, almacenamiento y operación.

| Necesidad | Archivo propio | Plataforma de observabilidad |
| --- | --- | --- |
| Abrir una corrida específica | Buscar por ID con un script | Abrirla en la interfaz |
| Comparar métricas | Calcular tablas y gráficos | Usar consultas y paneles disponibles |
| Compartir con equipo | Organizar y compartir archivos | Acceso común con permisos |
| Mantener funcionamiento | Código y almacenamiento propios | Servicio contratado o servidor propio |

Los límites gratuitos mencionados en la página 36 son datos históricos del material. Además, «unidades» de una plataforma y «trazas» de otra no son necesariamente la misma unidad facturable. Sin un volumen realista de spans, retención, usuarios, costos de operación y prueba sobre el mismo agente no se puede decidir cuál conviene solo leyendo esos límites.

> [!question]- ¿Puede un score reemplazar a la traza?
> No. Un score puede decir que la respuesta no cumplió un criterio, pero no identifica automáticamente qué paso causó el problema. La traza puede explicar el recorrido, pero tampoco garantiza por sí sola que la respuesta sea correcta. Conviene conservar ambas piezas vinculadas.

Fuente: PDF 20–23, 26–29 y 32–36 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S17 Observabilidad y versionado de prompts.pdf#page=23|Sesión 17, página 23]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/05 S17 - Instrumentar el bucle y conservar los errores|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/07 S17 - Configuración privacidad y exportación de trazas|Siguiente]] →
