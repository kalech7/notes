---
title: "Database Internals — Capítulo 7 · Amplificación y la conjetura RUM"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Amplificación y la conjetura RUM

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] Para conectar las políticas
> Una escritura barata al entrar puede generar trabajo futuro. Para comparar diseños debemos contar todo el recorrido y definir qué mide cada razón.

## Tres amplificaciones con unidades claras

**Amplificación de escritura**: bytes físicos escritos divididos por bytes lógicos aportados por la carga. Si una carga aporta 100 MB y el motor escribe 100 MB de WAL, 100 MB de primer flush y 400 MB de compactación, la amplificación del motor es `(100+100+400)/100 = 6`. Si medimos solo tablas y excluimos WAL, da 5. Las dos cifras son posibles, pero no comparables sin declarar el alcance.

**Amplificación de lectura**: trabajo o bytes leídos para obtener el resultado lógico. Una consulta puede revisar diez tablas candidatas pero leer datos de solo dos por efecto de filtros. “Diez archivos” y “dos bloques de datos” son métricas diferentes. Para una consulta fallida con cero bytes de respuesta es más útil contar I/O o bytes leídos que dividir entre cero.

**Amplificación de espacio**: espacio total retenido dividido por tamaño de los datos vivos, con una convención declarada. Si hay 100 MB vivos, 50 MB de versiones viejas y 10 MB de índices, la razón es 1,6. Durante una compactación pueden coexistir entradas y salida; el pico temporal será mayor que la ocupación estable.

## Cómo aparece la deuda

Compactar más agresivamente reduce archivos y versiones redundantes, mejorando lecturas y espacio, pero escribe más. Posponer compactación ahorra trabajo presente, aunque conserva la deuda y hace que lectores examinen más fuentes. El rendimiento de ingestión medido antes de que el mantenimiento alcance el ritmo de entrada puede ocultar esta deuda.

Los B-Trees también amplifican escrituras: páginas completas, divisiones y writeback de páginas sucias. Los LSM las amplifican al mover datos entre tablas. Comparar una página B-Tree con un primer flush LSM sin contar compactación o caché no describe el costo total de ninguna de las dos cargas.

## RUM como herramienta de razonamiento

**RUM** significa *Read, Update, Memory*: lectura, actualización y sobrecosto de memoria o espacio en el modelo. La conjetura presenta una tensión: optimizar dos dimensiones tiende a empeorar la tercera. Sirve para identificar qué costo paga un diseño al mejorar otro; no es una cifra universal ni reemplaza un benchmark.

Un filtro Bloom usa memoria adicional para evitar lecturas de archivos ausentes. La compactación usa escrituras para reducir fuentes y espacio. WiscKey compacta claves pequeñas, pero los rangos de valores pueden requerir lecturas dispersas. Estas decisiones vuelven visible el intercambio.

El propio capítulo reconoce límites: latencia, patrones de acceso, complejidad, mantenimiento, hardware, consistencia y replicación quedan fuera o simplificados. Una mejora por mejor implementación puede reducir varios costos a la vez respecto a una base deficiente; eso no convierte el modelo en una prohibición de optimizar.

## Qué preguntar antes de escoger

En vez de “¿LSM o B-Tree es mejor?”, una comparación útil fija tamaño de valores, proporción de actualizaciones, distribución de claves, necesidad de rangos, memoria, política de durabilidad, snapshots y ocupación del dispositivo. Luego mide ingestión sostenida, latencia de consultas y picos de mantenimiento en esa misma carga.

> [!question]- ¿Menos bytes escritos por la LSM implica menos desgaste de flash?
> No necesariamente en la misma proporción. El controlador SSD puede mover páginas durante su propia recolección. Hay que separar bytes del motor, bytes que llegan al dispositivo y escrituras internas de NAND.

**Puente al siguiente tema:** para reducir lecturas hace falta conocer la representación física de cada tabla. El índice permite llegar al bloque; un filtro puede evitar llegar al archivo.

**Referencia:** PDF 16–17 · impresas 144–145. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=16|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/06 Compactación por niveles tamaños y tiempo|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/08 SSTables índices y búsquedas secundarias|Siguiente]] →
