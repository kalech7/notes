---
title: "99 Fuentes y cobertura S18"
created: 2026-10-09
fecha: 2026-10-07
capitulo: 18
sesion: 18
tags:
  - maestria/ia-generativa
  - agentes/llmops
  - estudio
  - lecturas/fuentes
---

# 99 Fuentes y cobertura S18

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/00 Índice - S18 Guardrails costo y latencia|Índice de S18]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

## Fuente principal y límites

Fuente: `sesion-18.pdf`, 31 páginas, sesión del 7 de octubre de 2026. Copia de consulta: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S18 Guardrails costo y latencia.pdf|S18 Guardrails costo y latencia.pdf]]. La numeración visible coincide con la página PDF, incluidos los divisores 6, 18, 21 y 27.

Se leyó el texto de las 31 páginas. Las explicaciones y ejemplos no son transcripciones. Las rutas a código del curso son referencias descritas por el PDF: esos archivos no fueron entregados y no se afirma haber ejecutado su repositorio, su banco de 17 casos o su servidor H200.

## Cobertura por página

| Página PDF | Contenido | Nota que lo explica |
| --- | --- | --- |
| 1 | Tema, RA-5 y distribución de tiempos | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/00 Índice - S18 Guardrails costo y latencia|Índice]] |
| 2 | Prompt, inyección, secretos y controles de borde | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/01 S18 - Guardrails y bordes de confianza|01 Guardrails y bordes]] |
| 3 | RAG con entrada, contexto y salida | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/01 S18 - Guardrails y bordes de confianza|01 Guardrails y bordes]] |
| 4 | Bloquear, corregir, pasar; muestreo y θ | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/01 S18 - Guardrails y bordes de confianza|01 Guardrails y bordes]] |
| 5 | Familias de regla, contrato, FP/FN | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/02 S18 - Reglas patrones y normalización|02 Reglas]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/05 S18 - Medir guardrails y equilibrar seguridad y utilidad|05 Medición]] |
| 6 | Divisor: archivo evaluado | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/09 S18 - Laboratorio local de guardrails y versiones|09 Laboratorio]] |
| 7 | validate_input y validate_output | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/01 S18 - Guardrails y bordes de confianza|01 Contrato]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/03 S18 - Datos personales y errores de redacción|03 PII]] |
| 8 | Dos regex con diferencia de tilde | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/02 S18 - Reglas patrones y normalización|02 Normalización]] |
| 9 | Entradas A y B | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/02 S18 - Reglas patrones y normalización|02 Normalización]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/09 S18 - Laboratorio local de guardrails y versiones|09 Experimento 1]] |
| 10 | Tabla de coincidencias y normalización | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/02 S18 - Reglas patrones y normalización|02 Normalización]] |
| 11 | EMAIL_RE, PHONE_RE y redact_pii | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/03 S18 - Datos personales y errores de redacción|03 PII]] |
| 12 | Pregunta: tiendas 101 102 103 | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/03 S18 - Datos personales y errores de redacción|03 PII]] |
| 13 | Redacción equivocada y falta de evento | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/03 S18 - Datos personales y errores de redacción|03 PII]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/09 S18 - Laboratorio local de guardrails y versiones|09 Experimento 2]] |
| 14 | Evasiones, asimetría PII y banco de 17 | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/02 S18 - Reglas patrones y normalización|02 Reglas]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/03 S18 - Datos personales y errores de redacción|03 PII]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/05 S18 - Medir guardrails y equilibrar seguridad y utilidad|05 Medición]] |
| 15 | Pregunta original en camino bloqueado | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/04 S18 - Trazas secretos y retención|04 Trazas]] |
| 16 | Secretos, PII, retención y acceso | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/04 S18 - Trazas secretos y retención|04 Trazas]] |
| 17 | Orden de costos, muestreo, reintentos | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/05 S18 - Medir guardrails y equilibrar seguridad y utilidad|05 Medición]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/06 S18 - Costo de tokens y ahorro calculado|06 Presupuesto]] |
| 18 | Divisor: elección inevitable de reglas | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/05 S18 - Medir guardrails y equilibrar seguridad y utilidad|05 Medición y política]] |
| 19 | Principios implícitos y tres listas distintas | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/02 S18 - Reglas patrones y normalización|02 Reglas]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/05 S18 - Medir guardrails y equilibrar seguridad y utilidad|05 Política]] |
| 20 | Bloquear todo; utilidad y falsos positivos | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/05 S18 - Medir guardrails y equilibrar seguridad y utilidad|05 Medición]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/10 S18 - Repaso activo y ejercicios resueltos|10 Repaso]] |
| 21 | Divisor: costo y latencia | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/06 S18 - Costo de tokens y ahorro calculado|06 Costo]] |
| 22 | Campos de tabla y categorías ausentes | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/06 S18 - Costo de tokens y ahorro calculado|06 Costo]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/07 S18 - Cachés streaming batching y latencia|07 Cachés]] |
| 23 | Corrección del factor 5–25× a 5× | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/06 S18 - Costo de tokens y ahorro calculado|06 Costo]] |
| 24 | Actividad de costo: cuatro cálculos | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/06 S18 - Costo de tokens y ahorro calculado|06 Costo]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/09 S18 - Laboratorio local de guardrails y versiones|09 Experimento 6]] |
| 25 | Prefijo, router y porcentajes | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/06 S18 - Costo de tokens y ahorro calculado|06 Costo]] |
| 26 | Cachés, límite 128, streaming y batching | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/07 S18 - Cachés streaming batching y latencia|07 Cachés y latencia]] |
| 27 | Divisor: prompt como artefacto agregado | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/08 S18 - Prompts versionados evaluación y rollback|08 Versiones]] |
| 28 | Registro, changelog, evaluación, rollback | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/08 S18 - Prompts versionados evaluación y rollback|08 Versiones]] |
| 29 | Puntero ausente, None, máximo de cadenas | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/08 S18 - Prompts versionados evaluación y rollback|08 Versiones]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/09 S18 - Laboratorio local de guardrails y versiones|09 Experimento 5]] |
| 30 | Cuaderno: PII, jailbreak, cadena, registro y H200 | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/09 S18 - Laboratorio local de guardrails y versiones|09 Laboratorio]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/07 S18 - Cachés streaming batching y latencia|07 H200 y límites]] |
| 31 | Taller, medición dual, cierre y ajuste fino | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/05 S18 - Medir guardrails y equilibrar seguridad y utilidad|05 Integración]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/10 S18 - Repaso activo y ejercicios resueltos|10 Repaso y entrega]] |

## Aclaraciones y discrepancias

1. **Tres salidas.** Se presenta como el contrato del ejemplo, no como clasificación universal de todos los controles.
2. **El código se ejecuta siempre.** Solo ocurre si todos los caminos lo llaman correctamente. Las notas explican integración y ramas que podrían eludir la política.
3. **Regex ≈ 0.** Es bajo costo relativo; no costo ni latencia nulos. NER local también consume recursos.
4. **Normalización.** Se demuestra con frases literales para no alterar operadores regex. Quitar marcas también puede cambiar ñ; se explicita la pérdida.
5. **Formato y verdad.** El muestreo restringido favorece estructura válida, pero no garantiza correctitud semántica ni elimina todos los posibles reintentos.
6. **Precios y nombres.** Las tarifas y los identificadores se preservan como datos históricos citados por el PDF. No son verificación actual del proveedor.
7. **Factor 5×.** Se reproduce la corrección: 25 USD/M de salida no equivale a 25× de ahorro. Ambas categorías de las dos filas tienen razón 5.
8. **55,6–60,6 %.** Las dos filas del ejercicio producen 55,56 %. La figura de p. 25 muestra el 60,6 % para gpt-4o-mini; se distingue esa figura del cálculo Opus/Haiku, sin inventar tarifas del tercer modelo.
9. **Caché.** El mecanismo KV dentro de una generación y el servicio de caché entre llamadas se distinguen. La tabla de dos tarifas no permite calcular escritura o lectura.
10. **Streaming.** Se distinguen primer evento, primer token y primer texto visible. No se atribuye ahorro automático.
11. **Rollback.** Historial no es selección activa. Se aporta práctica propia que hace explícito el puntero.
12. **Cuaderno.** La comparación del PDF está rotulada simulada. No se presentan sus métricas como experimento real.
13. **Rúbrica.** Se conservan las referencias 25 %, 3 %, 10 % y 15 % sin inventar denominadores o sumar como rúbrica completa.

## Complementos primarios

- [Python re](https://docs.python.org/3/library/re.html): clases, operadores y búsqueda.
- [Python unicodedata](https://docs.python.org/3/library/unicodedata.html): normalización Unicode y categorías.
- [Anthropic prompt caching](https://platform.claude.com/docs/en/build-with-claude/prompt-caching): prefijo exacto, mínimos, TTL y categorías de uso.

Consultadas y contrastadas el 9 de octubre de 2026. No se añaden tarifas actuales ni código de API.

## Revisión pedagógica del 9 de octubre de 2026

Se releyeron las 12 notas y la fuente buscando si una persona principiante podía reconstruir cada mecanismo. Se conservaron las partes ya completas y se ampliaron huecos concretos:

- Nota 01: caso de documentos con permiso, evidencia insuficiente y cita válida que no respalda una afirmación.
- Nota 02: transformación Unicode por etapas, diferencia entre NFD y eliminar marcas, y operadores regex frente a texto literal.
- Notas 03–04: ejemplo de campos estructurados y recorrido de ramas que conserva privacidad también al bloquear o fallar.
- Nota 05: etiquetas según política, proporciones del banco y efecto en precisión, y reintento con información permitida.
- Nota 06: escalamiento del pequeño al grande y presupuesto con autorización, reserva y conciliación.
- Nota 07: punto de equilibrio de caché con tarifas inventadas y comparación de caché de prefijo, caché semántica y streaming para la misma familia de preguntas.
- Nota 08: qué afecta el rollback a ejecuciones pendientes y respuestas de caché.
- Notas 09–10: práctica de presupuesto y cinco preguntas de transferencia adicionales.

Las ampliaciones se identifican como elaboración propia y no se atribuyen al PDF las tarifas inventadas, la implementación de presupuesto ni resultados del simulador. La práctica ampliada mantiene el banco anterior y añade comprobaciones de presupuesto, representación Unicode, costo con escalamiento y equilibrio de caché. El presupuesto se integra antes de cada llamada del simulador: se comprueba cero llamadas al rechazar la primera reserva y una sola llamada al rechazar un reintento sin saldo. La ejecución ampliada terminó con todas las aserciones completadas. Los bloques Mermaid y las imágenes de esta sesión conservaron su contenido; los ejemplos nuevos complementan sus explicaciones.

## Validación y pendientes

La práctica local se ejecutó satisfactoriamente con Python y biblioteca estándar el 9 de octubre de 2026. Sus aserciones verifican coincidencias, redacción, matriz, conteo de llamadas, trazas mínimas, versiones y cuentas. El archivo `Practica/s18_resultados_verificados.json` conserva los resultados. El alcance es esta implementación didáctica propia.

La revisión final del lote S17–S18 terminó sin errores de YAML, vínculos o páginas PDF. Sus 17 bloques Mermaid se renderizaron correctamente y se inspeccionaron los PNG; las cuatro imágenes didácticas fueron revisadas visualmente. Las dos imágenes de S18 están en `Recursos visuales/S18/` y sus notas explican el significado debajo del embed. Evidencia en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/18 FUENTES - Sesiones 17 y 18 integración|la revisión general del conjunto]], completada el 9 de octubre de 2026.

Pendientes externos al alcance de los PDFs: archivos originales del curso, banco de 17 casos, mediciones H200/VPN, precios actuales y rúbrica completa. No son necesarios para entender las explicaciones y no se inventan resultados para cubrirlos.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/10 S18 - Repaso activo y ejercicios resueltos|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/00 Índice - S18 Guardrails costo y latencia|Índice]] →
