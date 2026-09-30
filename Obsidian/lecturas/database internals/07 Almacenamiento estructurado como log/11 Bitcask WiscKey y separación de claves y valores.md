---
title: "Database Internals — Capítulo 7 · Bitcask WiscKey y separación de claves y valores"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Bitcask WiscKey y separación de claves y valores

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] Una nueva decisión física
> Hasta aquí compactamos registros ordenados con claves y valores juntos. Ahora veremos qué se gana al escribir valores en orden de llegada y mantener otra estructura para encontrarlos.

## Bitcask: log de datos e índice completo en RAM

**Bitcask** es el diseño no ordenado que describe el capítulo: los registros se añaden directamente a archivos de log, sin memtable que los ordene. Su **keydir** es un mapa en memoria que asocia cada clave con la ubicación de su registro vigente: archivo, offset y demás información para recuperarlo.

Ejemplo propio: el log contiene `k1:A@0`, `k2:B@80`, `k1:C@160`. El keydir guarda `k1→160` y `k2→80`. Buscar k1 consulta el mapa y lee C; no mezcla A y C durante cada consulta. El registro A sigue ocupando espacio hasta la limpieza, pero ya no está referenciado como versión vigente.

La compactación o recolección recorre logs, conserva registros vivos y actualiza sus ubicaciones. El propio log de datos es la representación persistente; no necesita duplicar esos mismos valores en un WAL separado, aunque sigue necesitando una política de sincronización para durabilidad y tratamiento de escrituras incompletas.

Su límite central es que todas las claves y metadatos del keydir deben caber en RAM. Al arrancar se reconstruye el mapa desde archivos y metadatos auxiliares de la implementación. El mapa hash y los logs no ofrecen un recorrido eficiente ordenado por clave. Enumerar claves y ordenarlas externamente sería otro costo, no una consulta de rango propia de la organización descrita.

## WiscKey: claves ordenadas, valores en un log

**WiscKey** conserva una LSM ordenada de claves. En vez de guardar el valor grande dentro de cada SSTable, guarda una referencia a un **vLog**, log de valores. Así la compactación habitual mueve claves y referencias pequeñas, mientras la recolección del vLog se realiza por separado.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 07/03 claves_y_valores.png]]

En la parte superior, una tabla ordenada contiene claves junto a sus valores, que vuelven a copiarse al compactar. En la inferior, el índice ordenado solo contiene claves y offsets; los valores se añaden al log en otro orden. Mantener el orden de claves permite consultas por rango, pero recuperar esos valores exige seguir referencias a posiciones posiblemente dispersas.

Ejemplo propio: clave de 16 bytes, referencia de 16 y valor de 1000. Mover un millón de entradas completas supone unos 1016 MB antes de encabezados. Mover claves+referencias supone unos 32 MB. Este cálculo compara carga útil de una pasada de compactación; no incluye WAL, filtros, recolección del vLog ni amplificación del dispositivo.

## El rango conserva orden lógico y pierde localidad física

Una consulta de claves 100–200 recorre el índice en orden. Sus valores pueden estar en diez segmentos distintos porque se escribieron en diferentes momentos. WiscKey aprovecha prefetch y paralelismo de SSD para ocultar parte de la latencia, pero no elimina los bloques que necesita leer. El beneficio depende del tamaño de valores y de la carga.

El vLog no sabe por sí solo cuáles registros siguen vivos. La recolección consulta el índice de claves para comprobar si cada ubicación candidata sigue siendo la vigente. Si mueve un valor, debe actualizar su referencia sin pisar una escritura nueva concurrente. Head y tail delimitan regiones que se recorren y recuperan; no equivalen a una SSTable ordenada que resuelve todas sus versiones en una sola mezcla.

> [!question]- ¿Separar valores elimina toda amplificación de escritura?
> Reduce las reescrituras de valores durante compactación del índice. Los valores vivos todavía pueden moverse al recuperar el vLog y hay metadatos, referencias y durabilidad que mantener.

**Puente al siguiente tema:** seguir referencias es seguro solo si el índice y los archivos permanecen coherentes mientras cambian. Eso nos devuelve al protocolo de concurrencia y publicación.

**Referencia:** PDF 24–27 · impresas 152–155 · figuras 7-11 y 7-12. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=24|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/10 Skiplists caché y bloques comprimidos|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/12 Concurrencia snapshots y truncamiento del WAL|Siguiente]] →
