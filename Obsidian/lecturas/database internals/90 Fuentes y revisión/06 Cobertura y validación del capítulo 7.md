---
title: "Database Internals — Cobertura y validación del capítulo 7"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - fuentes
---

# Cobertura y validación del capítulo 7

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Capítulo 7]]

## Fuente y lectura visual completa

El PDF compartido es `/Users/alech/Downloads/CamScanner 2026-09-30 16.31.pdf`. Se conserva sin modificar en [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf|07 Almacenamiento estructurado como log.pdf]]. SHA-256 de original y copia: `60faf5b4584f6fdbc051fb377f59e2903fbf192ca7b5191496401a224dbf7eae`.

Se renderizaron y leyeron **las 36 páginas disponibles**, incluyendo todas las figuras y la tabla final. La capa de texto contiene únicamente la marca CamScanner y no permite leer el libro. Se empleó PyMuPDF para renderizar a 1,5 veces el tamaño nominal y se inspeccionaron imágenes con orientación corregida. Se intentó OCR como apoyo de extracción, pero la elaboración se fundamentó en la lectura visual de todas las páginas.

El mapa tiene dos tramos: PDF 1–34 → impresas 129–162 (`impresa = PDF + 128`); PDF 35–36 → impresas 165–166 (`impresa = PDF + 130`). Las páginas 2–15 y 32–36 requieren giro de +90° para lectura; las 16–31, −90°; la primera ya está orientada.

**Las impresas 163–164 no están en el archivo. Según aclaración directa del usuario, contienen lecturas futuras y una página en blanco.** Por ello no se considera un hueco temático del desarrollo; no se inventa ni reconstruye la bibliografía que no se recibió. Las impresas 165–166 son la conclusión de la Parte I, no dos páginas adicionales del desarrollo del capítulo 7, y se explican por separado en la nota 14.

## Mapa de cada página disponible

| PDF | Impresa | Giro para leer | Contenido y figuras | Notas principales |
|---|---|---|---|---|
| 1 | 129 | Sin giro | Epígrafe Pat Helland; correcciones e inmutabilidad | 00, 01 |
| 2 | 130 | +90° | Costo de modificar en el lugar; introducción LSM | 01, 02 |
| 3 | 131 | +90° | Archivos inmutables, densidad y mantenimiento | 01, 02 |
| 4 | 132 | +90° | Memtable, WAL y estructura; dos componentes | 02, 03 |
| 5 | 133 | +90° | Dos componentes antes/después de flush; figuras 7-1 y 7-2 | 02 |
| 6 | 134 | +90° | Reglas de flush; múltiples componentes y compactación | 02, 03 |
| 7 | 135 | +90° | Ciclo multicomponente y estados; figura 7-3 | 02, 03 |
| 8 | 136 | +90° | Vista de componentes, WAL y borrado incorrecto; figura 7-4 | 03, 04 |
| 9 | 137 | +90° | Tombstones puntuales/rango; inicio merge-iteration | 04, 05 |
| 10 | 138 | +90° | Cola de prioridad y cabezas de iteradores | 05 |
| 11 | 139 | +90° | Mecánica de merge y ejemplo; figura 7-5 | 05 |
| 12 | 140 | +90° | Complejidad, reconciliación, upsert y precedencia | 04, 05 |
| 13 | 141 | +90° | Mantenimiento, espacio temporal y retención de tombstones | 04, 06 |
| 14 | 142 | +90° | Leveled compaction y rangos; figura 7-6 | 06 |
| 15 | 143 | +90° | Tamaños, inanición y ventanas de tiempo | 06 |
| 16 | 144 | −90° | Amplificaciones y conjetura RUM | 07 |
| 17 | 145 | −90° | Límites de RUM e introducción SSTables | 07, 08 |
| 18 | 146 | −90° | Índice/datos, offsets y SASI | 08 |
| 19 | 147 | −90° | Bloom, estructuras probabilísticas y pertenencia | 09 |
| 20 | 148 | −90° | Colisiones, hashes y falso positivo; figura 7-7 | 09 |
| 21 | 149 | −90° | Negativo Bloom e introducción skiplist | 09, 10 |
| 22 | 150 | −90° | Skiplist, concurrencia y memoria; figura 7-8 | 10 |
| 23 | 151 | −90° | Caché, desalineación y compresión; figura 7-9 | 10 |
| 24 | 152 | −90° | Mapeo de bloques comprimidos; almacenamiento no ordenado; figura 7-10 | 10, 11 |
| 25 | 153 | −90° | Bitcask, keydir y log de datos; figura 7-11 | 11 |
| 26 | 154 | −90° | Costos Bitcask e introducción WiscKey | 11 |
| 27 | 155 | −90° | WiscKey, recolección y vistas; figura 7-12 | 11, 12 |
| 28 | 156 | −90° | Concurrencia de flush y compactación; truncar WAL | 03, 12 |
| 29 | 157 | −90° | Pérdida por truncamiento temprano; log stacking y FTL | 12, 13 |
| 30 | 158 | −90° | Páginas/bloques, GC y wear leveling; figuras 7-13 y 7-14 | 13 |
| 31 | 159 | −90° | Logging de filesystem y segmentos desalineados; figura 7-15 | 13 |
| 32 | 160 | +90° | Flujos desalineados y LLAMA; epígrafe Kuzco; figura 7-16 | 13 |
| 33 | 161 | +90° | Consolidación consciente del método y Open-Channel SSDs | 13 |
| 34 | 162 | +90° | Open-Channel, SDF y resumen del capítulo | 13, 14 |
| 35 | 165 | +90° | Conclusión Parte I: buffering, mutabilidad y orden | 14 |
| 36 | 166 | +90° | Tabla comparativa con notas a pie; figura I-1 | 14 |

El laboratorio 15 vuelve a usar los mecanismos de todo el capítulo. No se atribuyen al libro sus datos de claves, snapshots, bytes o resultados de cálculos propios, salvo el ejemplo Bloom de 16 posiciones, verificado en la figura 7-7.

## Precisiones técnicas que se incorporaron

- **Mutabilidad:** archivos o nodos físicos inmutables pueden representar estado lógico que cambia; una memtable normalmente es mutable. No se equipara inmutabilidad con falta de coordinación.
- **WAL:** la memtable es volátil, pero sus cambios pueden ser recuperables por un WAL durable antes del flush. Publicar una vista y persistir bytes son obligaciones distintas. Retirar un segmento compartido exige que no queden otras dependencias.
- **Tombstones:** se conservan mientras puedan ocultar versiones antiguas en otras fuentes. Snapshots y replicación añaden condiciones; la referencia histórica del libro a gracia temporal no se presenta como prueba suficiente de propagación.
- **Mezcla de versiones:** la exposición del libro asume una entrada por clave en cada iterador. Se amplió la explicación para SSTables que guardan varias versiones por clave dentro de la misma fuente. Un archivo nuevo no vuelve recientes sus registros antiguos.
- **Niveles:** se separó capacidad objetivo total de un nivel y tamaño de cada SSTable. No se presenta crecimiento exponencial de cada archivo como condición universal.
- **RUM:** se presenta como modelo de intercambios y se explican sus límites. Las amplificaciones tienen denominadores y alcance declarados.
- **Índice hash y rangos:** orden físico no basta para ubicar el primer registro mayor o igual que un límite ausente. Hace falta un mecanismo para encontrar ese comienzo.
- **Bloom:** más hashes con memoria fija no mejoran indefinidamente precisión. La aproximación matemática propia y el laboratorio muestran el aumento de falsos positivos cuando se supera un número adecuado. Un filtro positivo tampoco demuestra que una clave siga viva, y filtros puntuales no sustituyen metadatos de tombstones de rango.
- **Compresión:** el texto dice que las páginas comprimidas son siempre menores; se precisa que ese es el resultado buscado. Datos poco compresibles pueden crecer, por lo que el formato necesita admitir una alternativa. El ejemplo de offsets es elaboración propia.
- **Skiplist:** orden de recorrido y publicación de punteros no prueban por sí solos ausencia de deadlocks. Se explican protocolos y reclamación de memoria sin atribuir una garantía a cualquier implementación.
- **Figura I-1:** “ordenado” se distingue de soporte de consultas por rango; las notas a pie de WiscKey y Bw-Tree están explícitas. La etiqueta buffering del cuadro no niega buffers de flush de LLAMA.
- **Ejemplos históricos:** SASI, Bitcask, WiscKey, Open-Channel, LightNVM y otros sistemas se explican conforme al libro; no se afirma su soporte o prevalencia actual. No se realizaron búsquedas web ni se presentaron recomendaciones de herramientas actuales.

Estas precisiones son explicación técnica y modelos propios a partir del contenido recibido. No se leyeron íntegramente los artículos que aparecen citados en los márgenes del capítulo y no se afirma haber verificado la bibliografía ausente.

## Frases de contexto y atribuciones

Todas las notas comienzan con un callout que sitúa el problema y terminan con un puente conceptual al tema siguiente. La apertura contiene una traducción breve atribuida a **Pat Helland** de su epígrafe, que se explica como analogía contable sin prometer auditoría perpetua.

El epígrafe largo de **Kuzco**, de *The Emperor’s New Groove*, aparece en la impresa 160. Se identifica aquí como parte de la fuente: presenta con humor el nombre LLAMA y no aporta una condición técnica; la nota 13 conserva un fragmento breve traducido y atribuido, explica la broma y conecta el acrónimo con el ejemplo técnico.

## Recursos reproducibles

Hay tres PNG originales en `Recursos visuales/Capítulo 07/`, explicados inmediatamente bajo sus embeds: ciclo de flush, borrado incorrecto frente a tombstone, y separación de claves/valores. Se generaron con [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 07/generar_visuales.py|generar_visuales.py]] y Pillow. Las tres imágenes se revisaron visualmente: texto completo, ausencia de solapes y etiquetas legibles. El script comprueba ancho y alto de textos dentro de cajas.

El programa [[Obsidian/lecturas/database internals/Materiales/Laboratorios/07 lsm_modelo.py|07 lsm_modelo.py]] implementa un modelo lógico de fuentes, heap, versiones, snapshots y compactación conservadora. Reproduce el ejemplo de posiciones Bloom y calcula costos. Usa solo biblioteca estándar de Python; no implementa I/O, WAL durable, transacciones, réplicas, hilos ni tombstones de rango.

## Validación realizada el 30 de septiembre de 2026

- 16 notas del capítulo: índice, 14 temáticas —incluida síntesis de la Parte I— y laboratorio/repaso; esta nota de fuentes añade un archivo de soporte.
- Las 36 páginas renderizadas se revisaron visualmente, con los giros indicados en el mapa.
- Tres PNG generados y revisados visualmente, también por el agente integrador.
- Cuatro bloques Mermaid renderizados correctamente con mermaid-cli por el agente integrador: notas 02, 03, 10 y 13.
- Laboratorio ejecutado correctamente por el autor y el integrador: consulta actual, snapshots, múltiples versiones en una fuente, retención parcial, resurrección incorrecta detectada, purga completa, falso positivo y negativo Bloom, tamaño temporal y amplificación. `p7 = 0,81937 %`; `p20 = 5,45701 %`; pico del ejemplo `520 MB`; amplificación `6` incluyendo WAL.
- Un subagente revisor leyó las 16 notas completas y no encontró otros errores técnicos. Detectó un escape de fórmula y separadores de alias en tabla, ambos corregidos; se cambió “borradores” por “gomas de borrar” para aclarar el epígrafe.
- Los controles conjuntos de YAML, destinos de enlaces, anclas de PDF, cercos, tablas, caracteres de control y navegación terminaron sin incidencias pendientes; el resultado está registrado más abajo y en las fuentes generales.

El alcance es la explicación de las páginas recibidas y los recursos nuevos. Un laboratorio lógico no certifica un motor de producción ni los detalles concurrentes o durables de los sistemas históricos mencionados.

## Resultado de la validación conjunta

Validación final realizada el 30 de septiembre de 2026, sin incidencias pendientes: 31 YAML nuevos, destinos de enlaces y páginas PDF válidos, navegación continua, cuatro PNG revisados y nueve Mermaid renderizados entre ambos capítulos y la ruta general. Ambos laboratorios pasaron todas sus aserciones y ambas copias PDF coinciden con los originales. El alcance y el informe están en [[Obsidian/lecturas/database internals/90 Fuentes y revisión/01 Fuentes y cobertura#Revisión conjunta de la ampliación del 30 de septiembre|Revisión conjunta de la ampliación]].

---

← [[Obsidian/lecturas/database internals/90 Fuentes y revisión/05 Cobertura y validación del capítulo 6|Capítulo 6]] · [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice|Índice de fuentes]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Capítulo 7]] →
