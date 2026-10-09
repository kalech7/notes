---
title: "18 FUENTES - Sesiones 17 y 18 integración"
created: 2026-10-09
capitulo: 18
sesion: "17 y 18"
tags:
  - maestria/ia-generativa
  - referencias
  - agentes/llmops
---

# Fuentes y revisión de las sesiones 17 y 18

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/01 Guía - Entender las sesiones 17 y 18|Guía conjunta]]

Se leyeron las 37 páginas de *Observabilidad y versionado de prompts* (sesión 17, 6 de octubre de 2026) y las 31 de *Guardrails, costo y latencia* (sesión 18, 7 de octubre), de Daniel Andrés Riofrío Almeida. La numeración visible coincide con la posición en el PDF, incluidos separadores y portadas. Las copias en `Materiales` conservan los originales sin cambios.

- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S17 Observabilidad y versionado de prompts.pdf|Fuente S17, 37 páginas]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S18 Guardrails costo y latencia.pdf|Fuente S18, 31 páginas]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/99 Fuentes y cobertura S17|Cobertura de todas las páginas S17]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/99 Fuentes y cobertura S18|Cobertura de todas las páginas S18]].

Dos subagentes desarrollaron las sesiones por separado y un tercero revisó los conceptos y las cuentas. La integración añadió la guía conjunta, cuatro imágenes didácticas y la ruta en el índice de la materia. La segunda revisión profundizó los mecanismos y añadió un caso resuelto de principio a fin; sus criterios y mejoras están en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/19 REVISIÓN - Profundidad y comprensión S17 S18|la revisión pedagógica]]. Las órdenes, comandos, credenciales de ejemplo y entregas que aparecen en los documentos se estudiaron como contenido académico. No se ejecutaron las demos ni se conectó al servidor del curso.

## Procedencia y límites

Las definiciones, los ejemplos del docente y sus resultados se citan por página. Las analogías, los registros ficticios, las explicaciones ampliadas, los diagramas y las prácticas locales son elaboraciones didácticas. Las prácticas reproducen mecanismos con datos ficticios; no miden respuestas ni desempeño de un LLM real.

Los PDF hacen referencia a `traces.jsonl`, código de los laboratorios 03/04, cuadernos estudiantiles, políticas del curso y mediciones en una H200. Esos archivos concretos no acompañaron esta solicitud. Las notas explican lo visible en las diapositivas; no afirman haber ejecutado o inspeccionado esos originales. Los p50, media y p95 publicados se atribuyen al material porque faltan las diez duraciones para recalcularlos.

## Precisiones comprobadas

**Trazas y tiempo.** Una duración raíz no es necesariamente la suma de todos los spans. Los spans anidados incluyen tiempo de sus hijos y las operaciones paralelas se solapan. La suma de 45 + 900 + 120 + 1 100 = 2 165 ms corresponde al ejemplo secuencial. Un reloj monotónico mide duración; una fecha UTC registra cuándo comenzó.

**Costo y calidad.** 59 000 tokens de entrada a $1 por millón y 2 914 de salida a $5 por millón suman $0,07357. La entrada aporta el 80,196 % del gasto y el 95,293 % de los tokens. No se reconstruye un costo real sin identificar modelo y tarifas. Un error técnico ausente no prueba que una respuesta sea correcta. Costo y latencia se deben inspeccionar por separado, aunque puedan estar correlacionados.

**Comparación de estrategias.** En el escenario S18 de 30 000 llamadas mensuales, 2 100 tokens de entrada y 300 de salida, las tarifas del PDF producen $540/mes para el modelo grande y $108 para el pequeño. Enviar el 60 % al pequeño produce $280,80: ahorro de $259,20, equivalente al 48 %. Reducir el prefijo de 2 000 a 1 000 tokens da $390/mes con el grande: ahorro del 27,778 %. Estas cuentas base no incluyen reintentos, caché, impuestos o infraestructura, ni demuestran igualdad de calidad. La ampliación de S18 calcula por separado qué pasa si el 10 % de las llamadas dirigidas al pequeño requieren una segunda llamada al grande: el costo sube a $313,20 y el ahorro baja al 42 %.

**El 60,6 % de la página 25.** La figura de S18 lo atribuye a un tercer modelo, `gpt-4o-mini`; el pie menciona otra fila de la tabla de precios. Para los dos modelos del ejercicio, el prefijo representa el 55,556 % del costo. El rango de la figura compara modelos diferentes; las tarifas del tercero no están completas en estos adjuntos. No se trasladó el 60,6 % a Opus o Haiku.

**APIs y versiones.** La diapositiva S17 p. 22 atribuye la llamada antigua `trace()` a v3. La [guía oficial de migración Python v2 a v3 de Langfuse](https://langfuse.com/docs/observability/sdk/upgrade-path/python-v2-to-v3) sitúa esa llamada en v2. Las notas describen el problema como una API antigua incompatible y distinguen versión de SDK de versión de servidor. Las versiones impresas se conservan como contexto de la demo, no como una recomendación de instalación vigente.

**Versionado y caché.** Una versión identifica el prompt; una etiqueta selecciona la versión activa. La [documentación de caché de prompts de Langfuse](https://langfuse.com/docs/prompt-management/features/caching) explica la caché del cliente y el fallback de obtención de prompts. Son distintos de una caché de respuesta del modelo. Mover `production` puede requerir esperar o invalidar la caché del cliente. Un fallback de prompt no sustituye al proveedor LLM cuando este falla.

**Normalización y patrones.** Las [operaciones de expresiones regulares de Python](https://docs.python.org/3/library/re.html) interpretan operadores y clases de caracteres; la [normalización Unicode](https://docs.python.org/3/library/unicodedata.html) permite descomponer caracteres. Eliminar acentos requiere una operación adicional, y aplicar transformaciones a una expresión regular arbitraria puede alterar su significado. Los controles por patrones siguen siendo heurísticos: deben medir falsos positivos y falsos negativos.

**Caché de prefijo.** La [documentación primaria de Anthropic](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) distingue tokens de entrada nueva, escritura y lectura de caché. El mecanismo tiene requisitos de coincidencia, longitud y duración. No se inventó un descuento universal ni se convirtió una reducción de cómputo en un ahorro de factura sin medir. Consulta de fuentes externas: 9 de octubre de 2026.

**Fecha de entrega del material.** S17 dice «viernes 17 de octubre»; el 17 de octubre de 2026 cae sábado, como dice S18. Las notas registran la discrepancia. Esta revisión no confirma la fecha vigente de una entrega del curso.

## Imágenes y diagramas

Las cuatro imágenes se generaron con Pillow mediante [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/S17/generar_imagenes.py|el script reproducible]]. Se revisó cada PNG y se ajustó el texto a sus cajas para evitar recortes. Las imágenes explican una traza secuencial, versiones y etiqueta activa, bordes de control y el ejercicio de costo con medidas de latencia. Sus cifras proceden del PDF o están rotuladas como ejemplos propios.

Los bloques Mermaid se conservan dentro de las notas, con una explicación en prosa inmediatamente debajo. La validación extrae cada bloque y lo renderiza con Mermaid CLI y Chrome para detectar errores de sintaxis.

## Validación final

La comprobación posterior a la revisión en profundidad terminó sin errores: 28 notas con YAML válido, vínculos e imágenes resueltos y anclas PDF dentro de sus 37 y 31 páginas. Las copias coinciden con los originales mediante SHA-256. El conjunto contiene 71 preguntas con respuesta plegable y cuatro imágenes propias inspeccionadas visualmente.

Los 17 bloques Mermaid se renderizaron correctamente con Mermaid CLI 12.0.0 y Chrome, con código de salida 0. Se inspeccionaron las representaciones PNG. Las prácticas S17 y S18 ejecutaron sus comprobaciones locales; una revisión independiente contrastó conceptos, cuentas y resultados de los scripts.

El script [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Validación S17 S18/validar_notas.py|validar_notas.py]] conserva las comprobaciones estructurales en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Validación S17 S18/resultado.json|resultado.json]]. La evidencia de renderizado está en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Validación S17 S18/renderizado.json|renderizado.json]] y los PNG de la misma carpeta. Para regenerarlos, desde esa carpeta se utiliza `npx --yes --package @mermaid-js/mermaid-cli mmdc -i diagramas.md -o diagramas-renderizados.md -e png -p puppeteer.json -j 2`.

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/01 Guía - Entender las sesiones 17 y 18|Anterior: guía conjunta]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Siguiente: inicio]] →
