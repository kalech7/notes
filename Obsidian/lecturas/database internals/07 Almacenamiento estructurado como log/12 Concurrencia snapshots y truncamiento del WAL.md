---
title: "Database Internals — Capítulo 7 · Concurrencia snapshots y truncamiento del WAL"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Concurrencia snapshots y truncamiento del WAL

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] El hilo conductor
> Un archivo inmutable protege su contenido. Para que toda la lectura sea correcta, el motor también tiene que decidir qué conjunto de archivos y qué versiones verá cada operación.

## Vista de tablas y snapshot no significan lo mismo

Una **vista de tablas** es el conjunto de memtables y archivos consultables. Un **snapshot lógico** define hasta qué versión pueden verse los cambios. Una lectura puede necesitar ambos: un conjunto físico estable y un límite temporal de visibilidad. Mantener archivos vivos no determina por sí solo qué versión debe devolver.

Ejemplo propio: el snapshot S=12 se abre antes de una actualización versión 13. Después ocurre una compactación y cambian los archivos físicos. La lectura S sigue recibiendo el estado de versión 12 si esa es la garantía del motor, aunque use archivos nuevos. Por eso el mantenimiento debe conservar las versiones necesarias o sostener una vista antigua hasta que termine el lector.

## Tres puntos de sincronización del flush

1. **Cambio de memtable:** las nuevas escrituras van a la nueva. Se espera o coordina con escritores ya admitidos que dependan de la anterior.
2. **Finalización:** se publica una vista que reemplaza la congelada por la SSTable completamente lista. Ninguna lectura nueva atraviesa un hueco entre ambas.
3. **Truncamiento del WAL:** se retiran únicamente segmentos cuya información ya es recuperable desde almacenamiento durable y no tiene otras dependencias pendientes.

El libro presenta barreras de orden de operaciones en Cassandra como ejemplo: quien consume el estado para el flush conoce qué escritores anteriores todavía deben terminar. Es un ejemplo del protocolo del capítulo, no una afirmación de API o configuración actual.

## Tres fallos y sus consecuencias

| Error | Consecuencia |
|---|---|
| Escribir en la memtable antigua después de recorrerla | El archivo puede omitir esa operación |
| Quitar la memtable antes de publicar su archivo | Lectura incompleta durante el intervalo |
| Truncar WAL antes de lograr una tabla durable recuperable | Una caída puede perder los datos |

Publicar un puntero atómicamente no fuerza bytes al disco. Completar una escritura de archivo tampoco demuestra que sus metadatos de publicación sean recuperables. El protocolo durable incluye ambos y ordena los pasos según las garantías de la plataforma.

## Compactación y lectores en curso

La compactación crea salidas nuevas mientras las entradas siguen consultables. Luego cambia la vista y marca entradas retiradas. Sus archivos o buffers se eliminan cuando las referencias activas dejan de necesitarlos. Esto separa **retiro lógico** de **liberación física**.

Si un lector abrió A antes de la publicación y sigue avanzando su iterador, no se le debe quitar A bajo los pies. Contadores de referencias, versiones de vistas u otro esquema de reclamación permiten concluir sin que consultas nuevas sigan eligiendo la entrada retirada.

Una lectura debe trabajar con una vista coherente. Mezclar partes arbitrarias de la vista anterior y posterior puede omitir información o duplicar fuentes de modo que el algoritmo ya no tenga sus invariantes. La inmutabilidad reduce coordinación dentro del archivo, pero la coordinación entre generaciones sigue siendo esencial.

> [!question]- ¿Un WAL durable vuelve durable la memtable?
> Los bytes de RAM siguen siendo volátiles. Lo que es durable es la información necesaria para reconstruirlos mediante replay. Cuando el texto del capítulo dice que los contenidos aún no son durables hasta el flush, se refiere a su materialización como tabla, no a negar la protección de un WAL correctamente persistido.

**Puente al siguiente tema:** el motor no es la última capa de almacenamiento. El sistema de archivos y el SSD también pueden registrar versiones y recolectarlas.

**Referencia:** PDF 27–29 · impresas 155–157. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=27|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/11 Bitcask WiscKey y separación de claves y valores|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/13 Logs apilados FTL y cooperación con LLAMA|Siguiente]] →
