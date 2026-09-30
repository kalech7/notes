---
title: "Database Internals — Capítulo 7 · Almacenamiento estructurado como log"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Capítulo 7 · Almacenamiento estructurado como log

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Capítulo 7]]

> [!abstract] Frase para comenzar
> Ya sabemos cómo cambiar un árbol de páginas. En este capítulo aprendemos a conservar archivos escritos, añadir versiones nuevas y recuperar el estado correcto mediante mezcla y compactación.

El **almacenamiento estructurado como log** agrupa escrituras y evita modificar archivos publicados. La pieza central es una LSM: mantiene una memtable en RAM, produce tablas ordenadas en disco y compacta esas tablas para controlar versiones, fuentes de lectura y espacio ocupado. La escritura rápida del primer plano y el trabajo posterior de mantenimiento forman parte del mismo diseño.

> «Los contables no usan gomas de borrar o terminan en la cárcel». — Pat Helland, traducción breve del epígrafe de la impresa 129.

La imagen contable ayuda a iniciar el tema: registrar una corrección preserva lo anterior hasta que el motor pueda reconciliarlo. No implica un historial perpetuo, porque la compactación puede retirar versiones innecesarias.

## Ruta de estudio

| Nota | Pregunta que resuelve |
|---|---|
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/01 Inmutabilidad y la idea de añadir correcciones\|01 Inmutabilidad y la idea de añadir correcciones]] | ¿Cómo cambia un dato sin modificar su archivo? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/02 Dos componentes y múltiples archivos\|02 Dos componentes y múltiples archivos]] | ¿Cómo se organiza una LSM y por qué hay muchas tablas? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/03 Memtables flush y publicación de archivos\|03 Memtables flush y publicación de archivos]] | ¿Cómo se publica un flush sin perder datos? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/04 Actualizaciones borrados y tombstones\|04 Actualizaciones borrados y tombstones]] | ¿Por qué borrar necesita tombstones? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/05 Merge iteration y reconciliación de versiones\|05 Merge iteration y reconciliación de versiones]] | ¿Cómo se mezclan fuentes y resuelven versiones? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/06 Compactación por niveles tamaños y tiempo\|06 Compactación por niveles tamaños y tiempo]] | ¿Qué cambia entre niveles, tamaños y ventanas de tiempo? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/07 Amplificación y la conjetura RUM\|07 Amplificación y la conjetura RUM]] | ¿Cómo se miden los costos y se interpreta RUM? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/08 SSTables índices y búsquedas secundarias\|08 SSTables índices y búsquedas secundarias]] | ¿Cómo localiza datos una SSTable y un índice secundario? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/09 Filtros Bloom y falsos positivos\|09 Filtros Bloom y falsos positivos]] | ¿Qué garantiza un Bloom y qué significa falso positivo? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/10 Skiplists caché y bloques comprimidos\|10 Skiplists caché y bloques comprimidos]] | ¿Cómo se conserva orden en RAM y se direccionan bloques? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/11 Bitcask WiscKey y separación de claves y valores\|11 Bitcask WiscKey y separación de claves y valores]] | ¿Qué cambia al separar claves y valores? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/12 Concurrencia snapshots y truncamiento del WAL\|12 Concurrencia snapshots y truncamiento del WAL]] | ¿Qué coordinación necesitan vistas, snapshots y WAL? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/13 Logs apilados FTL y cooperación con LLAMA\|13 Logs apilados FTL y cooperación con LLAMA]] | ¿Qué trabajo duplican las capas y cómo coopera LLAMA? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/14 Síntesis de la Parte I buffering mutabilidad y orden\|14 Síntesis de la Parte I buffering mutabilidad y orden]] | ¿Cómo conecta la conclusión toda la Parte I? |
| [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/15 Laboratorio y repaso resuelto\|15 Laboratorio y repaso resuelto]] | ¿Cómo comprobar las reglas y resolver cálculos? |

## Alcance de la fuente

Se leyeron visualmente las **36 páginas disponibles**: PDF 1–34 corresponden a impresas 129–162, y PDF 35–36 a impresas 165–166. Estas dos últimas contienen la conclusión de la Parte I y la figura I-1, desarrolladas en la nota 14. Las impresas 163–164 no están en el archivo; **según la aclaración del usuario**, contienen lecturas futuras y una página en blanco, por lo que no hay un hueco temático que impida explicar el capítulo. No se reconstruyó bibliografía ausente.

La nota de [[Obsidian/lecturas/database internals/90 Fuentes y revisión/06 Cobertura y validación del capítulo 7|cobertura y validación]] registra la correspondencia de cada página y las precisiones técnicas. Se distinguen ejemplos históricos del libro de garantías generales: estas notas no evalúan versiones actuales de los motores mencionados.

## Qué conviene recordar del capítulo anterior

En [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Variantes de B-Trees]] aparecieron copy-on-write, buffers, FD-Tree y deltas de Bw-Tree. Este capítulo profundiza en archivos inmutables, reconciliación y mantenimiento, y después conecta esas ideas con sistema de archivos y SSD.

**Referencia:** PDF 1–36 · impresas 129–162, 165–166. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=1|PDF conservado]].


---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Anterior: capítulo 6]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/01 Inmutabilidad y la idea de añadir correcciones|Siguiente]] →
