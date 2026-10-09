---
title: "99 Fuentes y cobertura S17"
created: 2026-10-09
capitulo: 17
sesion: 17
tags:
  - maestria/ia-generativa
  - agentes/observabilidad
  - estudio
---

# 99 Fuentes y cobertura S17

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/00 Índice - S17 Observabilidad y prompts|Índice de S17]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

La fuente principal es [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S17 Observabilidad y versionado de prompts.pdf|S17 Observabilidad y versionado de prompts.pdf]], 37 páginas. La numeración visible del pie corresponde a la página PDF. El número grande «17» de las portadillas es el número de sesión, no otra numeración de página.

Se leyó el texto completo de las 37 páginas. La portadilla de la página 4 se renderizó y revisó visualmente para confirmar que no había un gráfico omitido por el extractor. Las otras portadillas son separadores de secciones. No se utilizaron instrucciones dentro del documento como órdenes de ejecución.

## Correspondencia completa

| Página PDF | Contenido de la página | Nota que lo desarrolla |
| --- | --- | --- |
| 1 | Presentación, objetivo y agenda de S17 | Índice y 01 |
| 2 | Fallos con HTTP 200 y regla de evidencia | 01 |
| 3 | Cuatro preguntas y 50 fallos diarios | 01 |
| 4 | Portadilla de traza, span y campos | 02 |
| 5 | Traza completa, spans anidados, medir/auditar | 02 |
| 6 | Ocho requisitos, once campos, relación con taller | 02 |
| 7 | Costo de figura no reconstruible sin modelo/tarifa | 03 |
| 8 | Portadilla de diez corridas y cuarenta spans | 03 y 04 |
| 9 | Media, p50, p95 e historial del taller | 04 |
| 10 | Concentración del gasto y conteos de tokens | 03 |
| 11 | Corrida 4 lenta y 7 cara | 04 |
| 12 | Diagnóstico por spans y caso incorrecto ausente | 03, 04 y 09 |
| 13 | Portadilla de código instrumentado | 05 |
| 14 | TraceStep sin uso del proveedor | 05 |
| 15 | Campos ausentes y acoplamiento de laboratorios | 05 |
| 16 | Guardrail excluido, excepción ausente, correo y API vieja | 05 y 07 |
| 17 | Instrumentar dentro del bucle | 05 |
| 18 | Context manager, pila, except/finally y relanzar | 05 y 09 |
| 19 | Mini-dashboard y diez corridas simuladas | 09 |
| 20 | prompt_version y falta de comparación v2/v3 | 08 |
| 21 | Portadilla Langfuse | 06 |
| 22 | SDK, servidor, OpenTelemetry y requisito académico | 06 y 07 |
| 23 | Trace, observation, generation, session, prompt, score | 06 |
| 24 | Docker, opciones del curso y puertos | 07 |
| 25 | Entorno, claves, endpoints y auth_check | 07 |
| 26 | Raíz, generation, tool e importancia de flush | 06 y 07 |
| 27 | Árbol, tiempos, palabras y tokens de demo | 06 |
| 28 | Decoradores e integración automática | 06 |
| 29 | Instrumentación manual y usage del proveedor | 06 |
| 30 | Versiones, etiqueta, changelog, fallback y rollback | 08 |
| 31 | Máscara recursiva, tupla, sesión y flush | 07 |
| 32 | Traza de Mongolia, v1, consumo y score | 06 y 08 |
| 33 | Demo de promoción, rollback y falla | 07 y 08 |
| 34 | Buenas prácticas y límites de Compose | 07 |
| 35 | JSONL, plataformas, colaboración y requisito taller | 06 y 07 |
| 36 | Comparación sin unidad/condiciones equivalentes | 06 y 10 |
| 37 | Síntesis, evaluación y fecha académica contradictoria | 08, 09 y 10 |

Los números de la última columna corresponden a las notas del [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/00 Índice - S17 Observabilidad y prompts|índice de S17]]. Ninguna página queda fuera del mapa.

## Qué se pudo comprobar

Se recalcularon los 50 fallos diarios, la suma secuencial 2 165 ms, el costo hipotético de 2 800/295 tokens, la participación de la corrida 7, su múltiplo de la mediana, la proporción de entrada en tokens y en gasto y la comparación costo medio/mediano de la corrida 4.

Los valores publicados de p50, media y p95 se explican, pero **no se recalcularon desde las diez duraciones originales**, porque `traces.jsonl` del curso no está adjunto. El ejemplo de cinco duraciones en la nota 04 sí está calculado íntegramente paso a paso.

El laboratorio propio se ejecutó sin API ni LLM. Produjo 10 corridas, 46 spans y costo ficticio de 0,0404 USD. Las comprobaciones verificaron conservación de bloqueo y fallo, excepción propagada, jerarquía, saneamiento de dict/list/tuple y ausencia del correo ficticio original en el archivo exportado. Las duraciones son reales y variables. No se reproduce ni valida el código del docente.

## Discrepancias y precisiones

1. **HTTP 200 y error nulo:** no prueban corrección de la respuesta. La primera pregunta del PDF necesita scores de calidad además del campo técnico de error.
2. **Costo 0,011 USD:** la página 7 no muestra tarifas/modelos suficientes para justificarlo. 0,004275 USD vale únicamente bajo la tarifa de 1/5 USD por millón para todo el consumo.
3. **Suma de tiempos:** válida solo para los cuatro pasos secuenciales sin solapamiento del ejemplo. Sumar padres/hijos o ramas paralelas duplica intervalos o confunde trabajo con tiempo transcurrido.
4. **Independencia:** costo y latencia son dimensiones que deben medirse por separado, pero los ejemplos no prueban independencia estadística.
5. **API trace():** la página 22 la atribuye a v3; la guía oficial Python v2→v3 la identifica como API v2. Se explica API antigua incompatible, diferenciando SDK de servidor.
6. **Prompt por traza o por span:** la simulación pone v3 global; el taller pide versión por span. Las notas explican herencia y varias versiones dentro de la misma corrida.
7. **Máscara de correo:** no es anonimización general. Deben cubrirse rutas bloqueadas, exitosas y de error, y estructuras dict/list/tuple; los mensajes de excepción también pueden filtrar datos.
8. **Fallback y caché:** fallback de prompt no reemplaza el modelo. El cliente puede reutilizar prompts en caché y retrasar observación de cambios de etiqueta; se registra la versión usada.
9. **«Viernes 17»:** el 17 de octubre de 2026 es sábado. No se asumió otra fecha ni se creó una entrega.
10. **Cuotas de servicios:** son citas históricas con unidades distintas; no se presentan como precios vigentes o comparación de costo total.
11. **Caso de calidad ausente:** la diapositiva 12 reconoce que no existe en el cuaderno su tercera traza de respuesta incorrecta. No se inventa un culpable real para las trazas originales.

## Referencias externas verificadas para precisar conceptos

- [Langfuse: migración oficial del SDK Python v2 a v3](https://langfuse.com/docs/observability/sdk/upgrade-path/python-v2-to-v3), para atribuir correctamente `trace()`.
- [Langfuse: caché de prompts](https://langfuse.com/docs/prompt-management/features/caching), para explicar que una etiqueta puede no actualizar instantáneamente todas las instancias.

Consulta de revisión: 9 de octubre de 2026. Los ejemplos de SDK de las notas son pseudocódigo explícito; no se afirma que un fragmento ejecutable sea compatible con un paquete actual.

## Material citado que no fue adjuntado

No están disponibles el repositorio `curso`, el cuaderno `s4-mar.py`, las diez trazas originales, `agent.py`, `instrumented_agent.py`, las tablas semestrales externas, los scripts de demo/exportación ni el enunciado íntegro del Taller 4. El PDF contiene extractos, mediciones y referencias de esos recursos. Las notas atribuyen sus afirmaciones al PDF y distinguen las verificaciones aritméticas propias de la reproducción de la demo.

Las rutas de scripts incluidas en las diapositivas no se convierten en wikilinks locales inexistentes. Reproducir la demo original requeriría esos materiales y el entorno del curso, pero **no hay un pendiente necesario para estudiar estas notas**: la explicación y el laboratorio propio son autocontenidos.

## Validación del conjunto

- Laboratorio propio ejecutado y resultados guardados en `Practica`.
- Texto y citas verificadas frente a las 37 páginas.
- Imágenes solicitadas y embebidas en notas 02 y 08, con explicación inmediatamente debajo.
- YAML y vínculos del lote S17–S18 válidos, sin anclas PDF fuera de rango. Copias originales comprobadas por SHA-256. Los 17 bloques Mermaid del conjunto se renderizaron correctamente y se revisaron sus PNG; las cuatro imágenes didácticas también se inspeccionaron. Resultados en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/18 FUENTES - Sesiones 17 y 18 integración|la revisión general del conjunto]], completada el 9 de octubre de 2026.


## Revisión pedagógica en profundidad — 9 de octubre de 2026

Se releyeron las doce notas y las 37 páginas de la fuente. La cobertura inicial era completa y las cuentas estaban explicadas; la revisión buscó comprobar si un principiante podía reconstruir los mecanismos, además de reconocer los nombres. No se agregaron páginas por extensión: las ampliaciones responden a huecos concretos de ejemplo y causalidad.

| Nota | Explicación inicialmente insuficiente para practicar | Profundización añadida |
| --- | --- | --- |
| 01 | Reconocer fallos no mostraba cómo distinguir dos causas de una cifra falsa | Caso de ventas: argumentos erróneos frente a transformación errónea, evidencia y siguiente prueba; definiciones de LLM, API, token, prompt y herramienta |
| 02 | Un span aislado no enseñaba a reconstruir la jerarquía ni separar intervalos | Cinco registros completos, padre/hermanos, árbol, 1 000 ms inclusivos, 950 ms hijos y 50 ms exclusivos |
| 03 | Costo de una llamada no mostraba una corrida con tarifas distintas o reintentos | Dos modelos con tarifas hipotéticas, costo por llamada, total correcto de 0,0048 USD; reintento de 0,0079 USD; diferencia entre cero y uso desconocido |
| 04 | Percentiles no indicaban qué optimización modifica la espera final | Paso reducido de 400 a 250 ms, camino crítico paralelo, comparación de ahorros y matiz de p95 interpolado en cinco observaciones |
| 05 | Finally y pila estaban definidos sin un recorrido completo de excepción | Entrada/yield/salida, tabla de pila, registro del hijo y padre, propagación y prevención del doble conteo de incidentes |
| 06 | Decorador y observación manual eran mapas conceptuales sin secuencia detallada | Llamada raíz, retriever, generation, usage y cierre en cuatro pasos; contexto activo y cuándo se deben actualizar tokens manualmente |
| 07 | Sanitización recursiva se entendía por definición pero faltaba una transformación completa | Tupla/dict/list con correo ficticio antes y después; memoria → envío → almacenamiento → exportación, y qué verifica cada etapa |
| 08 | Golden set no mostraba las respuestas comparadas ni una decisión con criterios previos | Plantillas v1/v2 y compilación; cuatro respuestas hipotéticas, scores, límites operativos propios, regresión por caso y conservación del historial |
| 09 | Resultados del laboratorio no terminaban de explicar el diagnóstico desde spans | Atribución del 94,88 % a decidir en caso 7; caso 4 sin redacción posterior, costos sin duplicar padre y alcance de datos simulados |
| 10 | Autoevaluación inicial centrada en definiciones | Tres ejercicios adicionales de intervalos, reintentos y regresiones ocultas por el score agregado |

Los nuevos ejemplos se identifican como propios, hipotéticos o derivados del laboratorio local según corresponda. No se presentan resultados inventados como mediciones de Langfuse o del curso. Los números del PDF se conservan con sus referencias originales; las tarifas mezcladas, los límites de promoción y los tiempos del nuevo árbol pertenecen exclusivamente a la práctica didáctica.

Las ampliaciones no modifican el código del laboratorio ni sus archivos de resultados, y no cambian los bloques Mermaid ya renderizados. Se conserva la evidencia de ejecución previa; releer y explicar los registros no equivale a ejecutar una demo externa. El índice se ajustó para señalar los mecanismos nuevos y los enlaces locales del capítulo se volvieron a comprobar.

Comprobación local tras la profundización: 12 notas, 78 wikilinks resueltos, 10 anclas PDF dentro de las 37 páginas y bloques de código con delimitadores equilibrados. Los siete bloques Mermaid de S17 no cambiaron. Las propiedades YAML se conservaron; la validación con parser y los renders pertenecen a la comprobación integrada mencionada arriba.
