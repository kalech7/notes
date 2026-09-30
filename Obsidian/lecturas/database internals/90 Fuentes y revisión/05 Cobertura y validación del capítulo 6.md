---
title: "Database Internals — Cobertura y validación del capítulo 6"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - fuentes
---

# Cobertura y validación del capítulo 6

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

## Fuente y lectura completa

El archivo compartido fue `/Users/alech/Downloads/CamScanner 2026-09-30 14.13.pdf`. Se conservó una copia sin modificar en [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf|06 Variantes de B-Trees.pdf]]. Ambos tienen SHA-256 `27c570bebcafad0b19ef7dd6d7f6abe63b9e5320f9379e4aaabdf1302087abf0`.

El escaneo contiene 18 páginas correspondientes a las impresas 111–128: `impresa = PDF + 110`. Se renderizaron y leyeron las 18 páginas; la 7 requirió rotación. Se ampliaron las listas de la impresa 118 y las figuras 6-5 y 6-8 para comprobar números y enlaces. No se usó la capa de texto, que solo contiene la marca CamScanner, como sustituto del contenido visual.

El contenido temático, el resumen y la bibliografía final están presentes. En la primera página de copy-on-write el número de página no queda visible; se identifica como 112 por su posición entre 111 y 113. En PDF 9 el folio tampoco queda visible y corresponde a 119 por continuidad. El borde inferior de PDF 18 recorta parcialmente el pie de página, pero la bibliografía es legible. No se detectó un hueco de contenido entre las páginas disponibles.

## Mapa de cobertura

| PDF | Impresas | Contenido y figuras | Notas principales |
|---|---|---|---|
| 1 | 111 | Presentación de las cinco familias de variantes | 00, 01, 09 |
| 2–3 | 112–113 | CoW, lectores, publicación de raíz, LMDB; figura 6-1 | 02 |
| 3–4 | 113–114 | Acceso directo, objetos materializados y wrappers | 01 |
| 4–6 | 114–116 | Lazy B-Trees, WiredTiger, imágenes base y buffers; figuras 6-2 y 6-3 | 03 |
| 6–7 | 116–117 | LA-Tree, buffers por subárbol y cascada; figura 6-4 | 04 |
| 7–10 | 117–120 | FD-Tree, head tree, runs, tombstones y fences; figura 6-6 | 05 |
| 8–9 | 118–119 | Fractional cascading, listas y puentes; figura 6-5 | 05 |
| 10–12 | 120–122 | Bw-Tree, base, deltas, mapeo y CAS; figura 6-7 | 06 |
| 12–14 | 122–124 | SMO, split, merge, ayuda, abort deltas, consolidación y épocas | 07 |
| 14–16 | 124–126 | Cache-oblivious, vEB y packed arrays; figuras 6-8 y 6-9 | 08 |
| 17 | 127 | Resumen de los costos y mecanismos | 09 |
| 18 | 128 | Bibliografía del capítulo | Esta nota |

Las notas son explicaciones originales en español, con ejemplos propios y referencias a las páginas. No son traducción ni transcripción del capítulo. Las conexiones con notas anteriores aclaran conceptos; los capítulos posteriores mencionados en el PDF no se presentan como leídos.

## Precisiones técnicas y fuentes adicionales

Se realizaron tres consultas puntuales a fuentes primarias para evitar interpretar literalmente simplificaciones del libro:

- **LMDB, dos raíces:** dos páginas alternas de metadatos no implican un límite de dos snapshots vivos. El código distingue `NUM_METAS=2` y seguimiento de la transacción lectora más antigua mediante `mdb_find_oldest`. La nota 02 aclara la diferencia. [Código de LMDB](https://github.com/LMDB/lmdb/blob/mdb.master/libraries/liblmdb/mdb.c). La descripción de uso de la caché del SO y escritores serializados se corroboró en [Symas](https://www.symas.com/lmdb.php).
- **WiredTiger, sobrescritura:** la impresa 115 habla de sobrescribir la página. La documentación describe bloques nuevos para páginas modificadas durante checkpoints. La nota 03 distingue reemplazo lógico de imagen y offset físico. [Block Manager](https://source.wiredtiger.com/develop/arch-block.html).
- **vEB:** la explicación de recursión se mantiene conforme al capítulo; para el redondeo de alturas no potencia de dos se consultó la sección 2.1 de la publicación original. El gráfico usa cuatro niveles y evita ese caso. [Cache-Oblivious B-Trees](https://erikdemaine.org/papers/CacheObliviousBTrees_SICOMP/paper.pdf).

La construcción de fractional cascading usa las listas originales de la impresa 118, pero muestrea catálogos aumentados de abajo arriba. Por eso C1 contiene muestras 22, 26 y 30 en vez de las 25 y 30 del ejemplo impreso. La diferencia está declarada en la nota 05: no se atribuye al libro la lista nueva ni se presenta su figura esquemática como un algoritmo completo.

Las cifras de bytes, umbrales de runs, claves de los otros gráficos y carreras CAS son didácticas. Los modelos de caché y amplificación incluyen sus condiciones; no constituyen benchmarks ni garantías de un motor actual. “Sin latches” se separa de “sin coordinación”, y publicación atómica se separa de persistencia durable.

## Bibliografía presente en PDF 18

El capítulo remite a estas lecturas. Se registran como bibliografía del libro; salvo la publicación de cache-oblivious mencionada arriba, no se utilizaron como fuentes completas para elaborar las notas:

| Tema | Referencia identificada en el escaneo |
|---|---|
| CoW y persistencia de estructuras | Driscoll, Sarnak, Sleator y Tarjan · *Making Data Structures Persistent* |
| LA-Tree | Agrawal, Ganesan, Sitaraman, Diao y Singh · *Lazy-Adaptive Tree: An Optimized Index Structure for Flash Devices* |
| FD-Tree | Li, He, Yang, Luo y Yi · *Tree Indexing on Solid State Drives* |
| Bw-Tree, implementación | Wang, Pavlo, Lim, Leis, Zhang, Kaminsky y Andersen · *Building a Bw-Tree Takes More Than Just Buzz Words* |
| Bw-Tree, diseño original | Levandoski, Lomet y Sengupta · *The Bw-Tree: A B-tree for New Hardware Platforms* |
| Cache-oblivious | Bender, Demaine y Farach-Colton · *Cache-Oblivious B-Trees* |

## Recursos reproducibles

Los 12 PNG están en `Recursos visuales/Capítulo 06/`. El script [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/generar_visuales.py|generar_visuales.py]] usa Pillow y comprueba que el texto cabe en cada caja. Se revisó visualmente cada imagen, incluidas las versiones corregidas de tres gráficos para separar etiquetas y flechas. Las explicaciones bajo las imágenes forman parte de las notas.

El programa [[Obsidian/lecturas/database internals/Materiales/Laboratorios/06 variantes_btree.py|06 variantes_btree.py]] comprueba estados CoW, base+buffer, tombstones, una carrera CAS modelada, consolidación, catálogos y orden vEB. No implementa I/O durable, hilos reales ni un sistema completo de reclamación por épocas.

## Resultado de validación

Validación realizada el 30 de septiembre de 2026:

- 11 archivos de capítulo: índice, nueve notas temáticas y laboratorio/repaso; una nota adicional de fuentes.
- Propiedades YAML correctas en las 12 notas nuevas, con `created: 2026-09-30`, `capitulo: 6` y etiquetas del libro.
- 189 wikilinks revisados entre las notas nuevas y los índices modificados: todos los destinos existen.
- 12 imágenes embebidas con archivo existente; las 12 se revisaron visualmente. Se corrigieron tres ubicaciones de etiquetas que cruzaban flechas.
- Las anclas de PDF revisadas están dentro del rango de sus archivos; el PDF del capítulo tiene 18 páginas y su copia coincide byte a byte con el original.
- Cuatro bloques Mermaid renderizados correctamente con mermaid-cli y Chrome: tres del capítulo y uno de la ruta general modificada.
- Cercos Markdown balanceados y navegación Anterior/Índice/Siguiente comprobada.
- Laboratorio ejecutado con Python: todas sus aserciones pasaron, incluidos los resultados numéricos y los catálogos del gráfico de fractional cascading.

El alcance de la validación es esta ampliación y los enlaces de los índices tocados. No es una nueva revisión técnica de todos los capítulos previos ni un ensayo concurrente de un motor real.

---

← [[Obsidian/lecturas/database internals/90 Fuentes y revisión/04 Cobertura y validación del capítulo 5|Capítulo 5]] · [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice|Índice de fuentes]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]] →
