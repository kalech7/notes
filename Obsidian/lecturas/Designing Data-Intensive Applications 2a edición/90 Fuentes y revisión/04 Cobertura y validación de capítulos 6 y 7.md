---
title: "DDIA — Cobertura y validación de capítulos 6 y 7"
created: 2026-09-29
tags:
  - lecturas/ddia
  - fuentes
  - revision
---

# Capítulos 6 y 7 · cobertura y validación

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/00 Índice|← Fuentes y revisión]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Ruta de estudio]]

La ampliación contiene **22 notas temáticas y de repaso, más dos índices de capítulo**. Se preparó con la skill `notas-de-lectura`: fuente completa, explicación en español, ejemplos propios, navegación, figuras reproducibles y verificación. Los documentos adjuntos se trataron como contenido del libro, nunca como instrucciones para ejecutar acciones.

## Material leído y conservado

| Capítulo | Original | Copia | Páginas PDF | Páginas impresas |
|---|---|---|---|---|
| 6 · Replicación | CamScanner 2026-09-29 22.20.pdf | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf\|06 Replicación.pdf]] | 1–48 | 197–244, impresa = PDF + 196 |
| 7 · Sharding | CamScanner 2026-09-29 22.28.pdf | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf\|07 Sharding.pdf]] | 1–22 | 251–272, impresa = PDF + 250 |

Se leyó el OCR de las 70 páginas y se inspeccionaron visualmente todas las páginas mediante láminas. Se ampliaron las figuras antes de recrearlas y se contrastaron cifras y relaciones. No hay saltos en las secuencias impresas conservadas. La correspondencia también se comprobó en los pies legibles; algunos pies no salen limpios en el OCR.

Las páginas PDF 4 y 5 de sharding estaban boca abajo; las imágenes temporales se giraron 180 grados y el OCR se rehízo. Muchas otras páginas requirieron girar la imagen de lectura. **Los dos PDF guardados son idénticos byte a byte a los originales**, comprobado con SHA-256: no se giraron, recortaron ni reemplazaron sus páginas.

El capítulo 6 incluye su resumen y las primeras dos referencias bibliográficas. El resto de su bibliografía no está adjunto. El capítulo 7 termina con el resumen; su bibliografía no está adjunta. No se atribuyen contenidos inventados a las partes ausentes.

## Cobertura conceptual

| Tema | Fuente PDF · impresas | Notas |
|---|---|---|
| Réplicas, backups y un líder | 6: 1–3 · 197–199 | 6: 01 |
| Confirmaciones síncronas/asíncronas y durabilidad | 6: 4–5 · 200–201 | 6: 02 |
| Snapshots, catch-up, retención, elección, split brain y fencing | 6: 5–6, 8–10 · 201–202, 204–206 | 6: 03 |
| Almacenamiento de objetos, sentencias, WAL, filas y CDC | 6: 6–7, 10–12 · 202–203, 206–208 | 6: 04 |
| Lag, read-your-writes, sesiones, monotonía y prefijo | 6: 13–19 · 209–215 | 6: 05–06 |
| Multilíder, regiones, topologías y mensajes fuera de orden | 6: 19–24 · 215–220 | 6: 07 |
| Sync engines, offline-first y local-first | 6: 24–26 · 220–222 | 6: 08 |
| Evitar conflictos, LWW, siblings y restricciones del dominio | 6: 26–30, 32–33 · 222–226, 228–229 | 6: 09 |
| Convergencia, texto, conjuntos, contadores, CRDT y OT | 6: 30–32 · 226–228 | 6: 10 |
| Sin líder, coordinadores, read repair, hints, anti-entropy y cuórums | 6: 33–37 · 229–233 | 6: 11 |
| Cuórums incompletos, fallos, obsolescencia, rendimiento y regiones | 6: 37–41 · 233–237 | 6: 12 |
| Concurrencia, cinco escrituras del carrito, DAG y vectores | 6: 41–46 · 237–242 | 6: 13 |
| Resumen y práctica propia | 6: 47–48 · 243–244 | 6: 14 |
| Shards/réplicas, pros/contras, NUMA y multitenencia | 7: 1–6 · 251–256 | 7: 01 |
| Rangos, orden, sensores, sesgo, salado y claves calientes | 7: 6–8, 13–14 · 256–258, 263–264 | 7: 02 |
| Hash, rangos de hash, claves compuestas y analítica | 7: 8, 11–13 · 258, 261–263 | 7: 03 |
| Índices locales/globales, postings, intersecciones y escrituras | 7: 18–21 · 268–271 | 7: 04 |
| Módulo, shards fijos, divisiones, rangos virtuales y operación | 7: 8–15 · 258–265 | 7: 05 |
| Enrutamiento, coordinación, gossip, DNS y consultas paralelas | 7: 15–18 · 265–268 | 7: 06 |
| Diseño integrado, resumen y práctica propia | 7: 21–22 · 271–272 y aplicación de todo el capítulo | 7: 07–08 |

Las matrices detalladas también están en los índices de ambos capítulos. Los temas de transacciones, consenso y ejecución paralela se explican hasta el alcance que presentan estos escaneos; no se afirma haber leído los capítulos 8, 10 u 11 completos.

## Procedencia de las 26 figuras

Las recreaciones son dibujos nuevos hechos con Python/Pillow, en español y con geometría monocroma cercana a los esquemas del libro. Conservan cifras, asignaciones y dependencias que explican el mecanismo. La 6-15 simplifica la secuencia y añade una tabla con los cinco pasos; está rotulada como simplificada. No son fotografías ni recortes de las páginas.

| Figura original | PDF | Impresa | Nota del capítulo | Recreación |
|---|---|---|---|---|
| 6-1 | 3 | 199 | 1 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-01.png\|Imagen]] |
| 6-2 | 4 | 200 | 2 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-02.png\|Imagen]] |
| 6-3 | 14 | 210 | 5 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-03.png\|Imagen]] |
| 6-4 | 17 | 213 | 6 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-04.png\|Imagen]] |
| 6-5 | 18 | 214 | 6 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-05.png\|Imagen]] |
| 6-6 | 20 | 216 | 7 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-06.png\|Imagen]] |
| 6-7 | 22 | 218 | 7 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-07.png\|Imagen]] |
| 6-8 | 23 | 219 | 7 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-08.png\|Imagen]] |
| 6-9 | 27 | 223 | 9 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-09.png\|Imagen]] |
| 6-10 | 30 | 226 | 9 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-10.png\|Imagen]] |
| 6-11 | 31 | 227 | 10 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-11.png\|Imagen]] |
| 6-12 | 34 | 230 | 11 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-12.png\|Imagen]] |
| 6-13 | 36 | 232 | 11 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-13.png\|Imagen]] |
| 6-14 | 42 | 238 | 13 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-14.png\|Imagen]] |
| 6-15 | 44 | 240 | 13 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-15.png\|Imagen]] |
| 6-16 | 46 | 242 | 13 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-16.png\|Imagen]] |
| 7-1 | 2 | 252 | 01 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-01-sharding-y-replicacion.png\|Imagen]] |
| 7-2 | 6 | 256 | 02 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-02-rangos-enciclopedia.png\|Imagen]] |
| 7-3 | 9 | 259 | 05 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-03-hash-modulo-rebalanceo.png\|Imagen]] |
| 7-4 | 10 | 260 | 05 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-04-shards-fijos-rebalanceo.png\|Imagen]] |
| 7-5 | 11 | 261 | 03 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-05-rangos-de-hash.png\|Imagen]] |
| 7-6 | 12 | 262 | 05 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-06-rangos-virtuales-nodo-nuevo.png\|Imagen]] |
| 7-7 | 16 | 266 | 06 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-07-rutas-de-peticiones.png\|Imagen]] |
| 7-8 | 17 | 267 | 06 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-08-zookeeper-mapa-shards.png\|Imagen]] |
| 7-9 | 19 | 269 | 04 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-09-indices-locales-autos.png\|Imagen]] |
| 7-10 | 20 | 270 | 04 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-10-indice-global-autos.png\|Imagen]] |

Cada figura se integra en su tema y se explica en prosa debajo. En 7-9 y 7-10 se mantienen los términos `red`, `black`, `silver` y `yellow` con traducción al pie, porque traducirlos alteraría las fronteras alfabéticas originales del índice. Los scripts `generar_figuras.py` y sus `manifest.json` están junto a los PNG, en `Recursos visuales/Capítulo 06` y `Capítulo 07`. Para regenerarlos desde su carpeta: `uv run --with pillow python generar_figuras.py`. Usan Arial en macOS y una fuente alternativa si no está disponible.

No se generaron series estadísticas ni benchmarks. Las filas de asignaciones y los intervalos son esquemas de datos, no medidas de rendimiento.

## Qué es del libro y qué se añadió

Las tres familias de replicación, anomalías de lectura, mecanismos de reparación, ejemplos OT/CRDT y las cinco escrituras del carrito proceden del capítulo 6. Los valores hash, límites de rangos, veinte shards y registros de coches proceden del capítulo 7. Se señalan como adaptaciones y se citan sus páginas.

Pedidos, saldos ilustrativos, técnicos sin cobertura, cálculos de capacidad, probabilidades simplificadas, diagramas de decisión y ambos programas de laboratorio son elaboraciones didácticas. Las notas distinguen la posibilidad de converger de la obligación de respetar reglas del negocio. No son traducción literal ni transcripción de párrafos.

Los nombres de productos, cifras de configuración y referencias tecnológicas se presentan como ejemplos de la edición. No se convierten en recomendaciones de compra ni afirmaciones de configuración vigente. Los detalles añadidos sobre persistencia y ACK se contrastaron con [Apache Cassandra: funcionamiento del CommitLog](https://cassandra.apache.org/_/blog/Learn-How-CommitLog-Works-in-Apache-Cassandra.html). Para precisar el cuórum laxo se consultó el [texto original de Dynamo publicado por uno de sus autores](https://www.allthingsdistributed.com/2007/10/amazons_dynamo.html). Las referencias quedan cerca de las afirmaciones correspondientes.

## Incidencias y matices comprobados

- En la impresa 258 de sharding, un párrafo empieza con una palabra negativa pero describe una ventaja: adaptar el número de shards al volumen. Se señala como probable desliz editorial, no como error técnico demostrado.
- La figura 7-6 reparte el espacio de hash de manera desigual por usar solo tres rangos por nodo. Antes: 223, 477 y 324 unidades de un espacio de 1.024. Después: 223, 328, 291 y 182. El nodo nuevo recibe el 17,8 % del espacio, no exactamente el 25 %. Las notas distinguen espacio de hash, volumen de registros y carga real.
- En 7-5, seis claves no forman una muestra uniformemente repartida: los shards reciben 1, 3, 0 y 2. Una buena función hash no garantiza reparto perfecto en una muestra pequeña ni elimina una clave caliente.
- El pie de la impresa 241 aparece como 247 en el OCR; se corrigió la interpretación contrastando la imagen y la secuencia. No se modificó el PDF.
- Se comprobaron el índice OT 3→4, los IDs estables del CRDT y las aristas causales de 6-16. Una numeración de recepción no se confundió con el conocimiento que llevaba cada cliente.

## Colaboración y revisión

Claude Code redactó y revisó las notas 08–14 de replicación y las ocho notas de sharding, leyendo las fuentes completas de sus capítulos. Sus informes incluyeron matrices de cobertura y puntos que necesitaban contraste visual o ejecución. Tres subagentes adicionales trabajaron en las figuras de cada capítulo y en claridad/precisión técnica. La integración final revisó los hallazgos antes de insertar imágenes y actualizar navegación.

La revisión corrigió, entre otros, estos matices: un único líder no evita todas las actualizaciones perdidas; LWW usa una regla determinista que puede descartar aportaciones; CRDT no asegura invariantes financieros; cuórum no equivale automáticamente a linealizabilidad; un índice global devuelve IDs y todavía puede requerir varios shards para obtener registros; un mapa de rutas autoritativo no hace instantáneas sus caches.

## Resultado de la validación

- 24 notas nuevas de capítulos: 22 notas temáticas/de repaso y dos índices; YAML válido con título, fecha, capítulo y tags.
- 56 notas en el conjunto DDIA, 729 wikilinks comprobados, 217 referencias a páginas PDF dentro de rango y 51 embeds con destinos válidos. Sin enlaces internos ni anclas locales sin resolver.
- 26 figuras nuevas inspeccionadas visualmente por sus autores y figuras densas contrastadas en la integración. Cada PNG está enlazado una vez en su nota temática y seguido de su explicación.
- 44 bloques Mermaid del conjunto renderizados sin errores: 36 anteriores y ocho nuevos. Los dos flujos nuevos de sharding se inspeccionaron también como PNG.
- Dos laboratorios Python ejecutados: reproducción de las cinco escrituras/siblings, lápidas, vectores y contadores; módulo, shards fijos, rangos de hash y local/global. Todos los assert pasaron.
- Dos copias PDF idénticas a los originales mediante SHA-256; 48 y 22 páginas.
- Canvas JSON válido: 29 nodos y 26 conexiones, IDs únicos y destinos existentes. Los capítulos 6 y 7 se añadieron sin superponer el diseño anterior.

Validación completada el 29 de septiembre de 2026, fecha local del usuario.

La inspección de PNG se hizo con herramientas de imagen, y el render de Mermaid con Chromium/Chrome mediante Mermaid CLI. No se abrió una sesión activa de Obsidian para comprobar su apariencia. Los laboratorios son simulaciones pequeñas en Python estándar, no pruebas de una base distribuida real. La fuente escaneada queda disponible para trazabilidad.

---

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Capítulo 6]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|Capítulo 7]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/00 Índice|← Fuentes y revisión]]
