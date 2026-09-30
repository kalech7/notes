---
title: "Database Internals — El costo de modificar un B-Tree y representar sus nodos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - arquitectura/formatos
  - arquitectura/costos
---

# El costo de modificar un B-Tree y representar sus nodos

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

Un **B-Tree** organiza claves ordenadas mediante nodos internos que eligen un rango y hojas que guardan los registros. Para almacenar el árbol en disco, normalmente se codifica cada nodo en una **página**: una unidad de datos que el motor lee, guarda en memoria y escribe. La ventaja de una página grande es que transporta muchas claves con una sola operación de entrada/salida, o **I/O**. La dificultad es que una escritura muy pequeña puede obligar a mover esa página completa.

## El tamaño de la escritura lógica no es el tamaño del trabajo físico

Supongamos una página de `4096 bytes` y un valor de `16 bytes`. Si cada modificación obliga a escribir la página una vez, modificar esos 16 bytes produce 4096 bytes de salida. La **amplificación de escritura** es la relación entre bytes escritos físicamente y bytes cambiados por la aplicación:

`4096 / 16 = 256`

Esto significa 256 bytes de escritura física por cada byte lógico en ese modelo. Es un cálculo didáctico, no una cifra del libro ni una medición de un motor: no incluye log, metadatos, compresión, caché ni el trabajo interno del SSD.

Ahora llegan 20 cambios de 16 bytes a la misma página:

| Política ilustrativa | Bytes físicos de página | Bytes lógicos | Amplificación |
|---|---:|---:|---:|
| Escribir la página después de cada cambio | `20 × 4096 = 81920` | `20 × 16 = 320` | `256` |
| Acumular los 20 y escribir una página al final | `4096` | `320` | `12,8` |

El ahorro es de 20 veces en escrituras de página bajo estas condiciones. No hemos cambiado la información final: hemos cambiado **cuándo se materializa**. Materializar significa construir una representación completa a partir del estado inicial y sus modificaciones. Si los cambios pertenecen a 20 páginas diferentes, este ahorro concreto ya no se obtiene de la misma manera.

Tampoco es inevitable escribir una página por cada `UPDATE`: la caché ya puede agrupar cambios en un B-Tree convencional. Las variantes del capítulo hacen más explícita esa separación y modifican también el formato, la propagación o la coordinación.

## Tres costos diferentes

La **amplificación de espacio** aparece cuando el almacenamiento total supera el tamaño de los datos útiles. Las páginas pueden reservar huecos para futuras inserciones; copy-on-write puede mantener versiones antiguas; los runs pueden contener registros reemplazados. Son causas distintas de espacio adicional.

La **amplificación de lectura** aparece cuando responder una consulta exige leer datos adicionales: por ejemplo, una base más varias actualizaciones, o la misma clave en distintos niveles. Reducir escrituras a menudo desplaza trabajo hacia las lecturas o hacia mantenimiento posterior.

La **concurrencia** añade otro problema: muchos hilos pueden tocar la misma estructura. Un **latch** es una protección breve de una estructura interna durante una operación. Evitar latches sobre una página exige otra manera de publicar cambios sin que alguien observe una estructura incompleta. Eso no determina por sí solo el nivel de aislamiento de una transacción.

En HDD, las escrituras dispersas pagan movimiento del cabezal; en SSD no hay esa mecánica, pero escribir más sigue teniendo costo y puede provocar trabajo de reclamación interna. El capítulo usa estas diferencias para justificar alternativas. No deduce que todo B-Tree sea lento en SSD.

**Referencia:** PDF 1–1 · impresas 111. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=1|Fuente del capítulo]].
**Referencia:** PDF 7–7 · impresas 117. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=7|Fuente del capítulo]].
**Referencia:** PDF 10–10 · impresas 120. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=10|Fuente del capítulo]].

## Antes de cambiar el disco, hay que representar el nodo en memoria

El programa no opera mágicamente sobre un archivo: accede a sus bytes en memoria o los convierte en otra estructura. El capítulo distingue tres enfoques.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/02-representaciones.png]]

La columna izquierda interpreta directamente el buffer de bytes. La central mantiene un objeto del lenguaje y una imagen binaria distinta; una reconciliación vuelve a convertir sus cambios en bytes. La derecha interpone un wrapper: una interfaz con métodos que modifica el buffer subyacente. La diferencia explica por qué “tener un objeto nodo” no permite concluir si sus cambios ya llegaron a la página física.

| Enfoque | Qué ocurre al insertar | Ventaja | Trabajo que añade |
|---|---|---|---|
| Acceso directo | Se transforman los bytes del buffer | Menos representaciones duplicadas | Respetar offsets, alineación, formato y sincronización |
| Objeto materializado | Se cambia una estructura propia del lenguaje | Mayor libertad para organizar cambios | Guardar objeto e imagen, serializar y mantener coherencia |
| Wrapper | El método aplica el cambio al buffer | Encapsular detalles físicos | Mantener correctamente la relación entre interfaz y bytes |

La segunda columna abre la puerta al buffering: el objeto puede conservar una inserción pendiente aunque la imagen del disco todavía no la tenga. Para ser correcto, el motor debe definir cuándo ese cambio es visible, cómo una lectura lo combina y cómo sobrevive a un fallo.

> [!question]- ¿Una página modificada en RAM ya es durable?
> No. **Durable** significa que el efecto confirmado sobrevive según el protocolo de persistencia del sistema. La representación en RAM, la visibilidad de la transacción y el almacenamiento estable son tres asuntos distintos.

> [!question]- ¿Por qué no basta con hacer páginas diminutas para evitar amplificación?
> Puede reducir bytes por reescritura, pero también reduce el número de claves o hijos por nodo. Eso puede aumentar la altura, los accesos y los metadatos. Hay que evaluar el costo completo.

**Referencia:** PDF 3–4 · impresas 113–114. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=3|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Anterior]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/02 Copy-on-write y snapshots en LMDB|Siguiente]] →
