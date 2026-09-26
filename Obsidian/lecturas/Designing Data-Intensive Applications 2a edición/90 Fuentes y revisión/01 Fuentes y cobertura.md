---
title: "DDIA — Fuentes opcionales, cobertura y criterios de las notas"
created: 2026-09-25
tags:
  - lecturas/ddia
  - fuentes
---

# DDIA — Fuentes opcionales y cobertura

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/00 Índice|Fuentes y revisión]]

**Las notas están escritas para estudiar sin volver a los PDF.** Esta página conserva trazabilidad: puedes ignorarla durante la primera lectura. Las referencias no son tareas pendientes ni requisitos previos.

## Edición identificada

*Designing Data-Intensive Applications*, segunda edición, Martin Kleppmann y Chris Riccomini, O’Reilly. La [ficha oficial de la editorial](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/) confirma autores y capítulos 4 (*Storage and Retrieval*) y 5 (*Encoding and Evolution*). Las primeras páginas de ambos escaneos coinciden con esos títulos y numeración.

## Material conservado

| Original compartido | Copia dentro de lecturas | Cobertura observada |
|---|---|---|
| CamScanner 2026-09-25 00.08.pdf | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/DDIA 2e - Capítulo 4 - escaneo.pdf\|Referencia del capítulo 4]] | 34 páginas PDF; impresas 115–150 |
| CamScanner 2026-09-25 00.03.pdf | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/DDIA 2e - Capítulo 5 - escaneo.pdf\|Referencia del capítulo 5]] | 32 páginas PDF; impresas 161–192 |

Los originales de Descargas se conservaron. Las copias locales permiten mantener las referencias si se reorganiza esa carpeta.

### Numeración del capítulo 4

| Páginas del PDF | Páginas impresas |
|---|---|
| 1–25 | 115–139; suma 114 al número del PDF |
| 26 | Fotografía doble: 140 y 141 |
| 27 | Fotografía doble: 142 y 143 |
| 28–34 | 144–150; suma 116 al número del PDF |

La fotografía doble de 142–143 tiene una pequeña zona superior de la 143 tapada por un adhesivo. No se presenta texto inventado como una transcripción de esa zona. Las explicaciones de ejecución y vistas se desarrollan a partir del material legible y del contexto de las secciones. No se detectaron saltos de numeración en la secuencia conservada. El capítulo termina con su resumen; no incluye su bibliografía numerada.

### Numeración del capítulo 5

Las páginas PDF 1–32 corresponden a impresas 161–192: suma 160. Incluyen la apertura y el resumen, sin saltos aparentes. Hay distorsiones y algunos pies recortados propios del escaneo. No se adjunta la bibliografía numerada del capítulo.

## Qué se explica

| Bloque | Desarrollo en las notas |
|---|---|
| Organización operacional | Logs, mapas hash, SSTables, memtables, WAL, compactación, tombstones, Bloom, B-trees y amplificaciones |
| Acceso a datos | Índices secundarios, heap, cobertura, organización clustered, memoria y motores embebidos |
| Analítica | Filas y columnas, bitmaps, RLE, capas de lago de datos, compilación, vectorización, vistas materializadas y cubos |
| Búsqueda | Índices espaciales e invertidos, embeddings, medidas, IVF, HNSW y aproximación |
| Representación | Serialización, formatos ligados a lenguajes, JSON/XML/CSV, JSON Schema, formatos binarios, Protobuf y Avro |
| Evolución | Versiones de lectores y escritores, defaults, campos desconocidos, conservación y significado |
| Comunicación | Bases, APIs, REST/RPC, descubrimiento, balanceo, workflows, idempotencia, brokers y actores |

No se presenta como cobertura de capítulos posteriores sobre replicación, sharding, transacciones, consenso, batch o streaming. Cuando un concepto de esos ámbitos sirve para aclarar un límite, se menciona como contexto y no como un capítulo leído.

## Qué es elaboración didáctica

Los pedidos, clientes, café y té, monedas, claves, bitmaps pequeños, cálculos de almacenamiento, matrices de compatibilidad y ejercicios son ejemplos creados para explicar los mecanismos. Las analogías visuales y diagramas también son originales. No son benchmarks ni reconstrucciones de figuras del libro.

La introducción de fundamentos, el caso integrador, las tarjetas, las conexiones y el patrón de ampliar/migrar/retirar son desarrollos pedagógicos. Los escaneos son la base temática; las notas no pretenden ser una traducción literal ni reproducir la totalidad del texto.

## Contrastes con documentación primaria

Se consultaron fuentes oficiales para precisar detalles que dependen del formato o implementación. Los enlaces junto a las explicaciones permiten localizar la afirmación correspondiente.

| Fuente | Para qué se usó |
|---|---|
| [PostgreSQL: índices multicolumna](https://www.postgresql.org/docs/current/indexes-multicolumn.html) | Importancia de columnas iniciales y excepciones mediante skip scan |
| [RocksDB: write stalls](https://github.com/facebook/rocksdb/wiki/Write-Stalls) | Atraso en flush/compactación y freno de escrituras |
| [Apache Parquet: formato](https://parquet.apache.org/docs/file-format/) | Grupos de filas y bloques de columnas |
| [pgvector: índices](https://github.com/pgvector/pgvector#indexing) | Búsqueda exacta y aproximada, IVFFlat y HNSW |
| [RFC 8259: números JSON](https://www.rfc-editor.org/rfc/rfc8259#section-6) | Precisión numérica e interoperabilidad |
| [JSON Schema: objetos](https://json-schema.org/understanding-json-schema/reference/object) | Campos declarados, requeridos y adicionales |
| [Protobuf: guía proto3](https://protobuf.dev/programming-guides/proto3/) | Números, evolución, presencia y campos desconocidos |
| [Protobuf: buenas prácticas](https://protobuf.dev/best-practices/dos-donts/) | Identidades y cambios de esquema |
| [Avro 1.12: especificación](https://avro.apache.org/docs/1.12.0/specification/) | Resolución entre escritor/lector, defaults y uniones |
| [Temporal: arquitectura](https://github.com/temporalio/temporal/blob/main/docs/architecture/README.md) | Historial, replay y límites frente a efectos externos |

Consulta realizada durante la preparación, 25 de septiembre de 2026. Las reglas específicas se contextualizan; una actualización futura del producto puede modificar detalles operativos.

La revisión ampliada añadió contrastes con la [codificación de Protobuf](https://protobuf.dev/programming-guides/encoding/), la [especificación de MessagePack](https://github.com/msgpack/msgpack/blob/master/spec.md), [OpenAPI 3.0.3](https://spec.openapis.org/oas/v3.0.3.html), la [codificación anidada de Parquet](https://parquet.apache.org/docs/file-format/nestedencoding/) y el [mantenimiento de espacio en PostgreSQL](https://www.postgresql.org/docs/18/routine-vacuuming.html#VACUUM-FOR-SPACE-RECOVERY). Las notas de búsqueda incluyen referencias específicas para curvas espaciales y mecanismos de Lucene. Los cambios de cobertura se documentan en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/02 Revisión de cobertura y mejoras|la matriz de revisión]].

Tres matices reciben atención especial: la especificación Avro 1.12 sobre defaults de uniones no se simplifica como una regla universal de orden; RocksDB documenta frenos de escrituras sin justificar la afirmación de que toda lectura se suspenda; ejecución durable no convierte todos los efectos externos en operaciones realizadas una sola vez.

## Cómo se preparó el conjunto

Se extrajo OCR de ambos escaneos, se inspeccionaron páginas relevantes y se repartió el desarrollo entre subagentes de almacenamiento, evolución y conexiones. Después se revisaron conjuntamente las notas para mantener terminología y ejemplos consistentes. El contenido de los documentos se trató como material de estudio, no como instrucciones para actuar.

Las referencias enlazan páginas del PDF usando la numeración del visor, y sus etiquetas indican también la numeración impresa cuando corresponde. El OCR temporal no se añadió a la biblioteca: la versión para estudiar son estas explicaciones.

## Comprobación del conjunto

En la auditoría del 26 de septiembre de 2026 se validaron los metadatos YAML de las 30 notas y los destinos de 384 wikilinks en Markdown, incluidos 80 enlaces a páginas concretas de las referencias y 22 embeds. Se contabilizaron 36 diagramas Mermaid; los dos diagramas del mapa maestro se renderizaron e inspeccionaron. El Canvas contiene 27 nodos y 25 conexiones, con identificadores únicos y destinos válidos. Las copias PDF se conservaron. Se inspeccionaron las seis ilustraciones generadas y el gráfico numérico.

No se encontraron archivos de backup, copias temporales ni duplicados inequívocos dentro de esta carpeta; por ello no se eliminó ningún archivo. Los PDF de **Materiales** permanecen intactos.

La comprobación de Markdown y diagramas se hizo con analizadores locales; no se verificó la apariencia dentro de una sesión activa de Obsidian. Los ejemplos SQL describen mecanismos y no constituyen un laboratorio ejecutado contra un servidor.

---

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/00 Índice|← Índice de este bloque]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]]
