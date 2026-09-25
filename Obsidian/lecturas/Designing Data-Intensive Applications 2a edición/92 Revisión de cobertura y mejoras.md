---
title: "DDIA — Revisión de cobertura y mejoras"
created: 2026-09-25
tags:
  - lecturas/ddia
  - revision
---

# Revisión de cobertura y mejoras

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|← Ruta de lectura]]

**La primera versión cubría las ideas principales, pero no desarrollaba suficientemente todos los mecanismos.** Se revisaron las 66 páginas PDF suministradas contra las 14 notas y se ampliaron los puntos breves o ausentes. Esta página muestra la evidencia de esa revisión; no necesitas leerla ni abrir los PDF para estudiar.

El alcance es **los temas visibles de los capítulos 4 y 5 adjuntos**. No equivale al libro completo, a una transcripción palabra por palabra ni a un manual exhaustivo de implementación de cada tecnología. La pequeña zona tapada de la impresa 143 y la bibliografía no adjunta siguen siendo límites del material, no contenido que debamos inventar.

## Qué cambió para que se entienda mejor

- Se explican recuperación ante fallos, publicación de SSTables, checksums, rangos y costo de Bloom, optimizaciones de B-tree, movimiento de datos dentro del SSD y conservación de snapshots.
- Se siguen consultas analíticas completas, datos anidados, ejecución por lotes, mantenimiento de vistas, búsquedas espaciales, de texto y de vecinos aproximados.
- Se decodifican ejemplos pequeños de MessagePack, Protobuf y Avro byte a byte; se separan varint y ZigZag, estructura y significado.
- Se amplían convivencia de versiones, migraciones, OpenAPI, descubrimiento de servicios, historial durable, acuses y reentregas de mensajes.
- Cada diagrama de los capítulos tiene una guía de lectura inmediata. Las cuatro nuevas ilustraciones se explican tanto en sus notas como en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/02 Atlas visual explicado|el atlas visual]].

Las notas conservan ejemplos, preguntas y conexiones anteriores. Las adiciones explican el propósito, el mecanismo y sus límites; no se limitan a añadir nombres de tecnologías.

## Capítulo 4: recorrido de la cobertura

N1–N7 corresponden a las siete notas de almacenamiento listadas a continuación. La columna PDF usa páginas del visor; las 26 y 27 contienen fotografías de dos páginas impresas cada una.

- **01:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/01 Del log al índice|Del log al índice]].
- **02:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/02 LSM SSTables compactación y Bloom|LSM SSTables compactación y Bloom]].
- **03:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/03 B-trees WAL y costos de almacenamiento|B-trees WAL y costos de almacenamiento]].
- **04:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/04 Índices secundarios cobertura y memoria|Índices secundarios cobertura y memoria]].
- **05:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/05 Almacenamiento columnar y compresión|Almacenamiento columnar y compresión]].
- **06:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/06 Lagos de datos ejecución y vistas materializadas|Lagos de datos ejecución y vistas materializadas]].
- **07:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/07 Índices espaciales texto completo y vectores|Índices espaciales texto completo y vectores]].

| PDF | Tema visible | Cobertura | Mejora realizada |
|---:|---|---|---|
| 1 | Objetivo motor; OLTP y OLAP | N1, N5, N6 | Se mantuvo distinción por forma de trabajo y se amplió warehouse/HTAP. |
| 2 | Base mínima append-only, última versión | N1 | Conservado ejemplo propio; añadida guía del diagrama y contraste historial/índice. |
| 3 | Log, costo O(N), índice y mantenimiento | N1 | Añadido escenario de concurrencia, persistencia y fallos. |
| 4 | Hash RAM, offsets, arranque, límite RAM | N1 | Reconstrucción del mapa paso a paso; dificultades hash en disco y crecimiento. |
| 5 | Rangos hash; SSTable, índice disperso, bloques | N1, N2 | Conservada búsqueda por bloque y compresión; explicación de rangos LSM ampliada. |
| 6 | Memtable, flush, lectura y merge, log | N2 | Separación WAL/flush/fusión y recorrido ante fallos/publicación. |
| 7 | Tombstones, LSM, inmutabilidad, lectores concurrentes | N2 | Ejemplos mantenidos; nueva imagen leída panel a panel y retención por snapshots. |
| 8 | Objetos, recuperación de SSTables, checksums, Bloom | N2 | Se añadieron objetos, salida incompleta, checksum y diferencia cola incompleta/corrupción confirmada. |
| 9 | Probabilidad y espacio de Bloom | N2 | 10 bits/clave, 1 millón de claves, expectativa sobre 100 SSTables; se conserva límite probabilístico. |
| 10 | Size-tiered y leveled | N2 | Ejemplos numéricos de pico de espacio y solapamiento entre niveles. |
| 11 | Motores embebidos; introducción B-tree | N3, N4 | Ampliación de integración, caso por cliente y ejes independientes. |
| 12 | Referencias de página, raíz, fanout, lookup | N3 | Se conservó búsqueda 251; guía visual explícita y motivo del fanout. |
| 13 | Split, crecimiento raíz, eliminación | N3 | Añadido propósito de redistribución/fusión al borrar y matiz de variantes. |
| 14 | WAL, torn page, buffer, CoW y optimizaciones | N3 | Nuevos apartados de página partida, buffer, separadores, hojas cercanas, enlaces y CoW con R→H. |
| 15 | Lectura/rangos, stalls, paralelismo | N2, N3 | Fusión de rangos LSM detallada; se preserva corrección oficial de stalls, sin afirmar suspensión universal de lecturas. |
| 16 | Escrituras secuenciales/aleatorias; GC flash | N3 | Ejemplo de bloque con A/C vivos y B/D obsoletos; costos de copiar antes de borrar. |
| 17 | Amplificación, separación valores, fragmentación | N3 | Se añade separación de valores grandes; diferencia reutilizar espacio/devolverlo al SO. |
| 18 | Espacio, borrado, snapshots; secundarios | N2, N3, N4 | Snapshot S1+S2 vs S3, retención, backup; tombstone no implica borrado físico. |
| 19 | Clustered, heap, cobertura, movimiento de filas | N4 | Ejemplo H10→H90, reenvío y localizador lógico vs físico. |
| 20 | Base en RAM, durabilidad, estructuras, analítica | N4, N6 | Recuperación snapshot operación 500 + log 501–503; límites de confirmación; estructuras en RAM. |
| 21 | HTAP; nube, elasticidad, separación componentes | N6 | Explicación de HTAP, frescura y separación cómputo/objetos. |
| 22 | Motor, formato archivo/tabla, catálogo; hechos | N5, N6 | Versión V1/V2, GC, time travel, límites de retención y catálogo; definición hechos/dimensiones. |
| 23 | Consulta analítica, filas vs columnas, datos anidados | N5 | Recorrido pregunta de negocio→3 columnas y shredding con ejemplo de pedido. |
| 24 | Columnas alineadas y grupos de filas | N5 | Guía visual que separa selección de columnas y descarte de grupos. |
| 25 | Bitmap y RLE | N5 | Se conserva ejemplo completo AND y se amplía comparación con diccionario. |
| 26 | Roaring, AND/OR, grafos, wide-column, orden y escritura | N5 | Añadidas rachas por prioridad de orden, operaciones en grafos y técnicas de codificación; se conserva separación wide-column y límites del archivo. |
| 27 | Plan, JIT, vectorización, CPU, vistas | N6 | Recorrido de lote con tabla, suma distribuida, caché, bucles, operar comprimido y delta de vista. No reconstruye franja oculta. |
| 28 | Agregados y cubos | N6 | Se conserva cubo numérico y media ponderada; añade mantenimiento de suma/min. |
| 29 | Límites cubo; índice concatenado y espacial | N6, N7 | Se mantiene detalle perdido; ampliación curvas Z-order y regiones múltiples. |
| 30 | R-tree/Bkd/cuadrícula; dimensiones; texto invertido | N7 | Mecanismos separados de R-tree, Bkd y cuadrícula; análisis lingüístico explicado. |
| 31 | Postings/bitmaps, segmentos, n-gramas, fuzzy; semántica | N7 | Postings 110 AND 101; persistencia de segmentos; subcadenas con verificación; trie y autómata por edición. |
| 32 | Embeddings, distancias, modalidades, flat | N7 | Conservadas ecuaciones; añadido significado de dimensiones y compatibilidad multimodal. |
| 33 | IVF y HNSW | N7 | IVF 1D demuestra vecino perdido por frontera; HNSW con nuevo Mermaid explicado y candidatos, no una cadena codiciosa garantizada. |
| 34 | Resumen OLTP/OLAP, familias e índices | N1–N7 | Los temas se distribuyen en las notas; se evita convertir reglas orientativas en resultados universales. |

## Capítulo 5: recorrido de la cobertura

Los números 01–07 corresponden a estas notas de codificación. Aquí cada página PDF corresponde a una página impresa.

- **01:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/01 Evolución y compatibilidad|Evolución y compatibilidad]].
- **02:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/02 JSON XML CSV y esquemas|JSON XML CSV y esquemas]].
- **03:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/03 Protocol Buffers y números de campo|Protocol Buffers y números de campo]].
- **04:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/04 Avro y resolución de esquemas|Avro y resolución de esquemas]].
- **05:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/05 Bases de datos APIs y RPC|Bases de datos APIs y RPC]].
- **06:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/06 Workflows durables e idempotencia|Workflows durables e idempotencia]].
- **07:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/07 Mensajería actores y repaso|Mensajería actores y repaso]].

| Página PDF / impresa | Tema del escaneo | Nota(s) | Cobertura previa y mejora realizada |
|---|---|---|---|
| 1 / 161 | Evolución; esquemas; rolling upgrades | 01,05 | Base correcta; se explica convivencia, despliegue gradual y reversión de código sin reversión de datos. |
| 2 / 162 | Backward/forward; dos flechas API; campos desconocidos | 01 | Añadida matriz cliente viejo/nuevo y servidor viejo/nuevo; dificultad asimétrica de compatibilidad futura. |
| 3 / 163 | Pérdida de campos; memoria frente a bytes | 01,02 | Lectura guiada del diagrama y explicación punteros/identificadores. |
| 4 / 164 | Codificación, zero-copy; formatos del lenguaje | 02 | Matiz zero-copy, versiones de clases, costo CPU/tamaño y dependencias del lenguaje. |
| 5 / 165 | JSON/XML/CSV; números; binarios/Base64 | 02 | Conservada precisión numérica/Base64 y explicadas ambigüedades textuales. |
| 6 / 166 | CSV; JSON Schema; modelo abierto/cerrado | 02 | Ejemplo CSV con comas/comillas y nulabilidad; reglas de columnas. |
| 7 / 167 | patternProperties; condiciones/referencias; formatos binarios | 02 | Esquema ejecutable de claves string numéricas explicado, condiciones y dependencias remotas. |
| 8 / 168 | MessagePack bytes | 02 | Antes apenas tamaño: ahora ejemplo propio 10 bytes frente a 18 JSON, desglosado grupo a grupo. |
| 9 / 169 | MessagePack y Protobuf IDL/generación | 02,03 | Añadida relación IDL→generador→programa, comparación breve con Thrift. |
| 10 / 170 | Etiquetas; varints; repeated | 03 | Ejemplo 150→96 01 y lista A/B; precisión del rango ZigZag frente a int64 y excepción packed. |
| 11 / 171 | Evolución etiquetas/tipos/reserva | 03 | Ya correcta; conservadas reservas, campos desconocidos, límites int32→int64 y presencia. |
| 12 / 172 | Avro IDL/JSON; falta etiquetas | 04 | Ejemplo propio de cuatro bytes con esquema explícito. |
| 13 / 173 | Bytes Avro; dos esquemas | 04 | ZigZag, rama de unión, bloques de arrays; diagrama guiado e imagen nueva explicada. |
| 14 / 174 | Resolución por nombre y defaults | 04 | Diferenciadas posiciones en bytes/identidad por nombre; aclarada posibilidad de resolución en una pasada. |
| 15 / 175 | Añadir/quitar; null/default; aliases/unions | 04 | Matriz ya correcta; ejemplos concretos renombrado y unión; matiz spec Avro1.12 preservado. |
| 16 / 176 | Ubicación esquema; esquemas dinámicos | 04 | Ejemplo de exportación lunes/martes y conservación del catálogo histórico. |
| 17 / 177 | Esquemas dinámicos; méritos; ASN.1 y protocolos DB | 02,04 | Antes breve/ausente: costes de asignar números, ASN.1 contextual, drivers y protocolo específico. |
| 18 / 178 | Méritos; modos de flujo; base de datos | 01,02,05 | Límites esquema vs negocio, versiones concurrentes y escritor/lector. |
| 19 / 179 | Datos sobreviven código; migraciones; archivo | 05 | Adición de columna vs reescritura, compacción no migra negocio, exportación lógica vs copia física. |
| 20 / 180 | Archivo; servicios; encapsulación | 05 | Caso confirmarPedido vs tablas internas; Avro vs Parquet en exportación. |
| 21 / 181 | REST; clientes; web services; OpenAPI | 05 | Contextos móvil/interno/externo, separación REST/HTTP/JSON, contrato OpenAPI. |
| 22 / 182 | Ejemplo OpenAPI y FastAPI | 05 | Ejemplo propio YAML explicado línea por línea; contrato no implementa lógica. |
| 23 / 183 | Code-first/IDL-first; RPC historia y problemas | 05 | Distinción enfoques; EJB/RMI/DCOM/CORBA/SOAP como contexto; tabla consecuencias. |
| 24 / 184 | RPC latencia/tipos; balanceadores | 05 | Seis diferencias, transferencia/punteros/tipos; topología. |
| 25 / 185 | DNS/discovery/mesh | 05 | Heartbeats, catálogos, conexión directa, tres diagramas topológicos agrupados. |
| 26 / 186 | Mesh; evolución RPC y versionado | 05 | Cifrado/observabilidad/operación; URL/Accept/configuración por cliente. |
| 27 / 187 | Workflows; grafo; tareas; orquestador/ejecutor | 06 | Roles y dependencias explicadas, disparadores preservados. |
| 28 / 188 | Familias motores; durable replay | 06 | Tabla familias, BPMN/BPEL, historial/pseudocódigo original; no prometer ACID entre servicios. |
| 29 / 189 | Idempotencia/determinismo/versiones; eventos | 06,07 | Tabla caída antes/después de registro; secuencia reintento y límites. |
| 30 / 190 | Broker; cola/pubsub; durabilidad/retención/esquemas | 07 | Ciclo publish/delivery/ack/reentrega; event sourcing y petición/respuesta sobre broker. |
| 31 / 191 | Republicación; actores; resumen | 07 | Ejemplo dos actores; límites estado privado/garantías/framework; despliegue entre versiones. |
| 32 / 192 | Resumen compatibilidad y flujos | 01,07 | Ruta y caso integrador preservados; cobertura completa de secciones conceptuales adjuntas. |

## Precisiones que afectan a la corrección

La codificación de enteros negativos necesita distinguir **ZigZag** de los tipos `int32`/`int64` de Protobuf: no tienen el mismo costo de bytes. También se conserva el matiz de **Avro 1.12** sobre defaults de uniones y se separa tolerar un campo de preservarlo al reescribir. Las reglas específicas están explicadas y enlazadas a documentación oficial en las notas correspondientes.

**Recuperar un workflow** no garantiza que cada llamada externa haya tenido un único intento. **Un timeout** no demuestra que la operación fallara ni que se cancelara. **Una consulta ANN** puede perder vecinos respecto a una búsqueda exhaustiva, y un vecino exacto según los vectores puede no ser relevante para la pregunta humana. Estas condiciones se desarrollan con ejemplos, no solo como advertencias.

## Cómo se comprobó

Dos revisiones por subagentes contrastaron por separado almacenamiento y evolución contra todo el OCR disponible. Después se realizó la revisión integrada de explicaciones y recursos. Se comprobaron ejemplos de bytes y aritmética, enlaces internos y referencias a páginas, metadatos y sintaxis Mermaid. Las imágenes generadas se inspeccionaron antes de insertarlas.

La comprobación de sintaxis no equivale a una verificación del render dentro de una sesión de Obsidian: las notas y recursos se validaron localmente. Los ejemplos no constituyen una prueba de rendimiento de motores reales ni una certificación de un sistema en producción.

Los PDF siguen siendo referencias opcionales. Para estudiar puedes comenzar por [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/02 Atlas visual explicado|las cuatro escenas explicadas]] y avanzar hacia las notas del índice.
