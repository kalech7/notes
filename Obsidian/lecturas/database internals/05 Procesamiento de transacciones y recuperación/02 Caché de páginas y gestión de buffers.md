---
title: "Database Internals — Caché de páginas y gestión de buffers"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/buffer-management
---

# Caché de páginas y gestión de buffers

[[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|← Índice del capítulo 5]]

La RAM es más rápida que el almacenamiento persistente, pero normalmente no contiene toda la base. La **caché de páginas** conserva un conjunto de páginas para evitar repetir lecturas y reunir varias modificaciones antes de escribirlas.

Una **página** es una unidad del archivo; un **frame** es una ranura de RAM donde cabe una página. El identificador de página permite encontrar el frame que la contiene. El orden de los frames no tiene que parecerse al orden del B-Tree ni al de las páginas en el archivo.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/01-cache-paginas.png|1100]]

El árbol representa las relaciones lógicas entre páginas; los frames muestran dónde están sus copias en memoria. Las conexiones indican identidad, no vecindad física. Una hoja puede ocupar un frame cercano a la raíz aunque en el archivo esté muy lejos. Por eso el motor necesita un mapa de identificadores a frames y no puede deducir la ubicación a partir de la forma del árbol.

## Qué ocurre al solicitar una página

1. El motor busca su identificador en el mapa de páginas residentes.
2. Si existe, obtiene una referencia a su frame: es un **cache hit**.
3. Si falta, necesita un frame libre. Si no hay ninguno, escoge una víctima que pueda desalojarse.
4. Si la víctima está modificada, primero debe escribir su contenido respetando el WAL. Si está limpia, puede descartarla sin reescribirla.
5. Lee la página requerida desde almacenamiento, actualiza el mapa y devuelve una referencia.
6. El consumidor libera esa referencia cuando acaba de usar la página.

Una **cache miss** es una solicitud cuya página no está residente. No significa necesariamente un error; significa que hay que pagar el costo de traerla.

## Tres estados que conviene separar

**Limpia** significa que la copia en memoria coincide con la versión persistida. **Dirty** —sucia— significa que fue modificada y todavía hay una diferencia que debe escribirse. **Referenciada o pinned** significa que alguien la usa o que existe una instrucción de retenerla.

| Estado | ¿Se puede descartar su frame inmediatamente? | Trabajo previo |
|---|---|---|
| Limpia, sin referencias ni pin | Sí, si la política la elige | Retirar su entrada del mapa |
| Dirty, sin referencias ni pin | No directamente | Flush de datos con WAL previo durable |
| Referenciada o pinned | No mientras deba permanecer residente | Esperar liberación o quitar la retención |

**Flush** significa escribir cambios hacia almacenamiento; **eviction** significa retirar una página de la caché y reutilizar su frame. Un flush puede dejar la página residente y limpia. Una eviction de una página limpia puede no escribir nada. Confundir estas operaciones impide explicar cuándo hay I/O.

El **pin** protege la residencia. Un **latch** protege una estructura o contenido durante una sección crítica, y un **lock** protege la interacción lógica de transacciones. Mantener una página en RAM no impide por sí mismo que otro hilo modifique sus bytes; estas garantías son complementarias.

## Por qué se retrasan las escrituras

Supón, como ejemplo propio, que una página de 8 KiB recibe diez cambios pequeños. Escribir la página completa después de cada cambio produciría diez escrituras de página. Si todos los cambios se reúnen antes de un único flush, se escribe una vez su estado final. El WAL sigue registrando la información necesaria para recuperarlos; reducir los flushes de páginas no elimina el trabajo del log.

Aplazar escrituras consume RAM y acumula páginas dirty. Si se espera hasta que una solicitud urgente necesite el último frame, esa lectura tendrá que pagar también la escritura de una víctima. Un **background writer** puede anticipar parte de ese trabajo, dejando páginas limpias disponibles. Su beneficio es mover I/O fuera de la ruta crítica; si escribe demasiado pronto, pierde la oportunidad de reunir cambios posteriores.

La política debe equilibrar cuatro necesidades: reducir lecturas, amortizar escrituras, conservar frames disponibles y limitar la memoria. La durabilidad añade una condición obligatoria: ningún resultado confirmado puede depender exclusivamente de RAM.

## Pinning, anticipación y grandes recorridos

La raíz y niveles superiores de un B-Tree participan en muchas búsquedas. Mantenerlos residentes evita repetir lecturas comunes. Si la altura es cuatro niveles y los dos superiores están en caché, una búsqueda necesita como máximo dos lecturas de páginas de datos ausentes; no cuatro. Es una cuenta didáctica de páginas, no una predicción exacta de latencia.

**Prefetching** carga páginas antes de que se soliciten, por ejemplo hojas próximas de un rango. Puede solapar el I/O con trabajo útil, pero una predicción equivocada ocupa RAM y lee datos inútiles. Una exploración enorme de páginas utilizadas una sola vez puede expulsar las páginas calientes. Limitar su espacio o desalojarlas pronto protege el conjunto de trabajo habitual.

## Caché del motor y caché del sistema operativo

El sistema operativo también puede mantener páginas de archivos en memoria. El motor puede preferir controlar directamente qué conserva y cuándo escribe. El capítulo discute I/O directo, recomendaciones de acceso y memoria mapeada como alternativas con distintos grados de control.

Estas son opciones arquitectónicas, no equivalentes de durabilidad. Saltarse una caché del sistema operativo no demuestra que una escritura sobreviva a un corte eléctrico; el protocolo de persistencia sigue siendo necesario. Los detalles exactos dependen del sistema operativo y del dispositivo y quedan fuera del laboratorio conceptual.

> [!question]- Una página ya fue escrita al disco. ¿Tiene que desaparecer de RAM?
> No. El flush puede convertirla en limpia y conservarla para futuros hits. Se retira cuando la política necesita su frame y las referencias permiten desalojarla.

> [!question]- ¿Por qué una página dirty puede contener cambios de una transacción aún activa?
> Porque la ejecución modifica la copia en RAM antes del commit. Si se permite escribirla antes de que la transacción termine, se necesita información durable para deshacerla. Esa decisión se llama steal y se explica en la nota 05.

**Fuente:** PDF 3–7 · impresas 81–85 · figura 5-1 en PDF 4. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=3|Gestión de buffers, flush, pinning y anticipación]].

---

← [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/01 Transacciones ACID y componentes|Anterior]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/03 Reemplazo de páginas FIFO LRU CLOCK y TinyLFU|Siguiente →]]
