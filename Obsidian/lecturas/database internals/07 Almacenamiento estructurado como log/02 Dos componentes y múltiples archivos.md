---
title: "Database Internals — Capítulo 7 · Dos componentes y múltiples archivos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Dos componentes y múltiples archivos

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] Para situarnos
> Escribir versiones nuevas resuelve la modificación de archivos inmutables. Ahora necesitamos una estructura que conserve orden y permita encontrarlas.

## Los dos mundos de una LSM

Una **memtable** es una tabla en memoria que recibe modificaciones y atiende consultas. Es mutable, aunque los archivos del disco sean inmutables. Mantiene los registros ordenados, por ejemplo con un árbol o una skiplist, para que luego puedan escribirse secuencialmente en el orden de las claves.

Un **flush** es el paso que materializa registros de la memtable en disco. Una **tabla de disco** es un archivo o conjunto de archivos que contiene registros publicados y un índice para buscarlos. Aquí “tabla” designa la estructura física del motor, no una tabla SQL.

Un **WAL**, *write-ahead log* o registro anticipado de escritura, conserva operaciones recuperables antes de depender de su copia en memoria. El WAL suele seguir el orden de las escrituras; la tabla de disco sigue el orden de las claves. Por eso el WAL y la SSTable son dos representaciones con funciones distintas.

## La propuesta de dos componentes

En la LSM de **dos componentes** hay un componente pequeño en RAM y uno grande en disco. El componente de disco puede representarse como un árbol con páginas densamente ocupadas y de solo lectura. Un flush selecciona parte del árbol en memoria, encuentra el subárbol de disco correspondiente y fusiona ambos en una región nueva. Esa región se conecta al resto del árbol y reemplaza las anteriores.

Las figuras 7-1 y 7-2 muestran precisamente ese antes y después: los subárboles seleccionados se sustituyen por el resultado, mientras el resto del árbol sigue siendo aprovechable. No se sobrescriben a ciegas las páginas inmutables seleccionadas.

Ejemplo propio: disco contiene `10:A, 20:B, 30:C`; RAM contiene `20:B2, 25:D`. La fusión ordenada produce `10:A, 20:B2, 25:D, 30:C`. Se reutilizan los subárboles fuera de ese rango. Si cada pequeño flush integra inmediatamente registros con un componente grande, puede reescribir datos antiguos con mucha frecuencia.

El autor dice que no conocía implementaciones de este diseño al escribir el libro. Es una observación histórica del autor, no un inventario actual de motores.

## La alternativa de múltiples componentes

Una LSM **multicomponente** materializa cada memtable como una tabla nueva sin fusionarla inmediatamente con todo lo previo. Tres flushes dejan tres tablas. Las escrituras de primer plano son simples, pero una consulta puede tener que revisar varias fuentes.

```mermaid
flowchart LR
 M[Memtable ordenada] -->|Flush| A[Tabla A inmutable]
 M -->|Otro flush| B[Tabla B inmutable]
 A --> C[Compactación]
 B --> C
 C --> D[Tabla resultante publicada]
```

Cada flecha de flush produce un archivo distinto. La compactación consume las tablas A y B, combina sus registros y publica una nueva tabla; los archivos de entrada se retiran cuando los lectores dejan de necesitarlos. El dibujo representa un ciclo simplificado, no impone que siempre haya dos entradas y una salida.

La **compactación** es la fusión de tablas para reducir fuentes de lectura, recuperar espacio y reorganizar datos. También puede producir varias tablas particionadas por rangos. La ventaja de posponer la integración se convierte en una obligación: sin mantenimiento, el número de archivos aumenta indefinidamente.

> [!question]- ¿“Dos componentes” significa dos archivos?
> No. El componente de disco puede tener varios segmentos o páginas. La distinción describe la organización lógica: un componente en memoria y uno en disco frente a múltiples tablas de disco fusionadas periódicamente.

**Puente al siguiente tema:** crear otra tabla parece fácil; el punto delicado es mantener visibles todos los datos mientras el archivo todavía se está construyendo.

**Referencia:** PDF 4–7 · impresas 132–135 · figuras 7-1 a 7-3. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=4|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/01 Inmutabilidad y la idea de añadir correcciones|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/03 Memtables flush y publicación de archivos|Siguiente]] →
