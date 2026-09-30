---
title: "Database Internals — Cobertura y validación del capítulo 5"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/transacciones
  - fuentes
  - revision
---

# Cobertura y validación del capítulo 5

[[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice del capítulo 5]] · [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice|Fuentes del libro]]

## Fuente, alcance y lectura

Fuente aportada: `CamScanner 2026-09-30 14.02.pdf`, 31 páginas escaneadas. Copia conservada sin alterar: [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf]]. El capítulo es el 5, *Transaction Processing and Recovery*, de *Database Internals*, Alex Petrov.

Se renderizaron las 31 páginas. Se leyeron visualmente y con apoyo de OCR; PDF 14–15 se giraron para leerlas y recuperar su texto. **Página impresa = página PDF + 78**. Los contenidos del documento se trataron como fuente de estudio, sin convertir sus sugerencias o bibliografía en instrucciones para ejecutar acciones.

Tres subagentes colaboraron: uno leyó PDF 16–31 y desarrolló concurrencia, otro recreó los gráficos de caché y recuperación, y otro los de concurrencia. La revisión principal integró las explicaciones, contrastó los ejemplos con las imágenes y revisó todos los PNG finales.

PDF 30, impresa 108, incluye el resumen. PDF 31, impresa 109, contiene lecturas adicionales y termina cortando la referencia de FOEDUS. No se inventa su continuación ni se afirma haber leído las obras mencionadas en esa bibliografía. La fuente disponible sí incluye el desarrollo de los temas que explica este capítulo.

| PDF | Impresas | Cobertura en las notas |
|---|---|---|
| 1–2 | 79–80 | Transacciones, ACID y componentes |
| 3–7 | 81–85 | Buffer management, dirty, flush, pinning y prefetching |
| 7–10 | 85–88 | FIFO, LRU, 2Q, LRU-K, CLOCK, LFU y admisión por frecuencia |
| 10–13 | 88–91 | Recovery, WAL, fsync histórico, LSN, checkpoints, logging y shadow paging |
| 13–15 | 91–93 | Steal/force y las tres fases de ARIES |
| 15–19 | 93–97 | Estrategias de concurrencia, serialización, anomalías, niveles y snapshot isolation |
| 20–22 | 98–100 | OCC, MVCC, timestamp ordering, Thomas y 2PL |
| 22–24 | 100–102 | Bloqueos, deadlocks, detección y prevención |
| 25–28 | 103–106 | Latches, lectores/escritores, contención y latch crabbing |
| 29–30 | 107–108 | Upgrades, B-link trees y resumen |
| 31 | 109 | Lecturas adicionales y límite bibliográfico |

## Figuras del libro y recursos producidos

Las figuras se redibujaron como diagramas técnicos en español con Pillow. Identificadores, ejemplos y geometría son didácticos; no son especificaciones de un producto. Los dos scripts se guardan con las imágenes en [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/generar_cache_recuperacion.py|generar_cache_recuperacion.py]] y [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/generar_concurrencia.py|generar_concurrencia.py]].

| Recurso PNG en Capítulo 05 | Relación con la fuente | Explicación |
|---|---|---|
| `01-cache-paginas.png` | Figura 5-1 · PDF 4 · impresa 82 | Árbol, disco, tabla de páginas y frames de RAM |
| `02-clock.png` | Figura 5-2 · PDF 9 · impresa 87 | Anillo con bits y segunda oportunidad; pin añadido por separado |
| `03-tinylfu.png` | Figura 5-3 · PDF 10 · impresa 88 | Ventana, filtro de frecuencia y región principal segmentada |
| `04-wal-y-flush.png` | Elaboración propia · PDF 11–14 · impresas 89–92 | WAL durable, commit y flush diferido |
| `05-aries.png` | Elaboración propia · PDF 14–15 · impresas 92–93 | Análisis, repetir historia, retirar perdedoras y CLR |
| `06-serializacion.png` | Figura 5-4 · PDF 17 · impresa 95 | Tres transacciones y seis órdenes seriales candidatos |
| `07-write-skew.png` | Elaboración propia · PDF 19 · impresa 97 | Dos médicos, snapshots y violación conjunta de una regla |
| `08-deadlock.png` | Figura 5-6 · PDF 23 · impresa 101 | Recursos poseídos y ciclo de espera |
| `09-latches-crabbing.png` | Figura 5-9 · PDF 28 y prosa PDF 27 · impresas 105–106 | Proteger al hijo antes de soltar al padre; seguro e inseguro |
| `10-blink-split.png` | Elaboración propia · PDF 29–30 · impresas 107–108 | High key y enlace derecho durante un half-split |

La **figura 5-5** es la tabla de niveles y anomalías, PDF 19 · impresa 97: sus relaciones se desarrollan en una tabla Markdown en la nota 06. Las **figuras 5-7 y 5-8**, PDF 26 · impresa 104, ilustran lectores/escritores compatibles e incompatibles: la nota 09 expresa las combinaciones en una tabla y explica sus efectos. No se atribuye a esas figuras el dibujo de crabbing ni el de B-link.

Cada PNG tiene una explicación en prosa debajo de su embed. No hay series numéricas extraídas del libro; los cálculos y tablas de ejemplos propios se identifican como tales.

## Erratas, precisiones y límites del texto

- **PDF 14 · impresa 92:** la frase de undo menciona transacciones confirmadas. La nota 05 corrige esa errata con la propia descripción de undo de las incompletas en PDF 15.
- **PDF 11 · impresa 89:** la formulación write-ahead debe distinguir modificar RAM de persistir páginas. La nota 04 conserva el orden obligatorio entre persistencia del WAL y persistencia de datos.
- **PDF 12–13 · impresas 90–91:** el texto generaliza una relación entre completar fuzzy checkpoints y hacer flush de sus páginas. La nota 04 distingue el protocolo de ARIES y explica por qué no basta el inicio del checkpoint para descartar log anterior.
- **PDF 13 · impresa 91:** logging físico no exige siempre imágenes de páginas completas; también puede describir cambios de bytes, como reconoce el propio pasaje.
- **PDF 9–10 · impresas 87–88:** se distingue el filtro TinyLFU del esquema W-TinyLFU que combina ventana y colas. La figura conserva el mecanismo del libro y precisa el nombre.
- **PDF 18 · impresa 96:** se separan dependencia de una lectura sucia y sobrescritura directa de un dato no confirmado para precisar dirty write.
- **PDF 20 · impresa 98:** las condiciones de validación OCC no se trasladan como un algoritmo universal; se explica qué conjuntos y fases necesita definir una implementación.
- **PDF 22–24 · impresas 100–102:** se distingue 2PL básico de variantes que retienen bloqueos hasta terminar, evitando presentar toda retención como una propiedad de 2PL básico.
- **PDF 29 · impresa 107:** un split de raíz no exige que todos los hijos del árbol estén llenos. La nota 09 aclara la propagación por una rama.
- El caso `fsync` es un relato histórico de la fuente, sin atribuir el mismo defecto a versiones actuales. Tampoco se equiparan WAL y ARIES en todos los productos.

Cotejos complementarios consultados el 30 de septiembre de 2026: la precisión de WAL y group commit está respaldada por la [documentación oficial de PostgreSQL 17](https://www.postgresql.org/docs/17/wal-intro.html); las precisiones sobre checkpoint, `recLSN` y `pageLSN`, por el [artículo original de ARIES, secciones 4.4, 5.4 y 6.2](https://www.cs.cmu.edu/~15849g/readings/mohan92.pdf); la distinción del filtro TinyLFU y la ventana, por el [diseño oficial de Caffeine](https://github.com/ben-manes/caffeine/wiki/Design). Estos cotejos tienen un alcance puntual, distinto de la lectura completa del escaneo.

## Validación de la entrega

Resultados del 30 de septiembre de 2026:

- 11 notas en el capítulo: índice, nueve temas y laboratorio; frontmatter YAML válido y propiedades requeridas en todas las notas nuevas.
- 21 archivos Markdown de la ampliación y sus índices comprobados; 195 wikilinks y 29 referencias de páginas PDF resuelven sin errores.
- Diez PNG inspeccionados individualmente: texto legible, sin cortes ni solapamientos; las explicaciones se contrastaron con sus contenidos.
- Tres bloques Mermaid de los archivos tocados renderizados con Mermaid CLI y Chrome: el diagrama nuevo de componentes, la ruta general actualizada y el flujo de capítulo 4 conservado.
- PDF original y copia con SHA-256 idéntico; 31 páginas y todos los anclajes dentro del rango.
- Laboratorio ejecutado: FIFO produce 9 y 10 misses con tres y cuatro frames; LRU produce 10 y 8. Los grafos con ciclos se detectan y la espera de una sola dirección no forma ciclo.

Registro estructurado: [[Obsidian/lecturas/database internals/90 Fuentes y revisión/validacion_capitulo_05.json|Resultados de validación]]. La comprobación se limita a esta ampliación y los índices tocados; no declara una nueva revisión de toda la biblioteca.

## Regenerar y comprobar los ejemplos

Los scripts visuales se ejecutan con `uv run --with pillow generar_cache_recuperacion.py` y `uv run --with pillow generar_concurrencia.py` desde su carpeta, o indicando su ruta completa. Las fuentes tipográficas utilizadas están declaradas en los scripts; en otro sistema se debe proporcionar una fuente compatible si esas rutas no existen.

El [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/laboratorio_capitulo_05.py|laboratorio Python]] usa únicamente la biblioteca estándar. Reproduce los conteos FIFO/LRU y calcula ciclos sobre grafos didácticos. No implementa un motor, MVCC, consultas por rangos ni ARIES real.

---

← [[Obsidian/lecturas/database internals/90 Fuentes y revisión/03 Procedencia de recursos visuales|Procedencia de recursos]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice del capítulo]] · [[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro →]]
