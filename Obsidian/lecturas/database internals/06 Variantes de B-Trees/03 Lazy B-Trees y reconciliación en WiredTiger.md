---
title: "Database Internals — Lazy B-Trees y reconciliación en WiredTiger"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - arquitectura/buffers
  - arquitectura/concurrencia
---

# Lazy B-Trees y reconciliación en WiredTiger

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

El libro llama **lazy B-Trees** a los diseños que guardan cambios en estructuras auxiliares y los propagan después. La propia nota al pie de la impresa 114 aclara que es un nombre elegido para este capítulo, no una denominación universal de una única estructura.

**Lazy** significa que parte del trabajo físico se aplaza. Si el usuario inserta una clave, el motor puede guardar esa operación en un buffer y hacerla visible sin reconstruir inmediatamente la imagen completa de la hoja. El ahorro surge al aplicar juntas varias operaciones que habrían modificado la misma página.

## La página base deja de ser toda la verdad

El caso de **WiredTiger** separa la imagen de disco y la representación en memoria. Una página inicialmente limpia puede disponer de un índice construido a partir de la imagen base. Una página modificada añade actualizaciones que todavía no están materializadas en esa imagen.

Tomemos una base con `10:A`, `20:B`, `30:C`. Llegan estas operaciones, ya visibles para el lector de nuestro ejemplo:

| Orden | Operación | Efecto lógico |
|---:|---|---|
| 1 | `PUT(20,B2)` | 20 pasa a valer B2 |
| 2 | `DELETE(30)` | 30 deja de existir |
| 3 | `PUT(40,D)` | Se añade 40 |

Una lectura puntual de 20 debe devolver B2 aunque la base siga teniendo B. Una consulta de rango debe producir `10:A, 20:B2, 40:D`: hay que intercalar la clave nueva y suprimir la borrada. No basta con unir listas y devolver todas sus entradas.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/03-wiredtiger.png]]

La página limpia de la izquierda coincide con su imagen base. La modificada de la derecha conserva esa base y añade una estructura de cambios. La caja violeta muestra el resultado combinado; en ella ya no aparece 30. La reconciliación inferior transforma el estado aplicable en una nueva representación persistible. La imagen condensa las figuras 6-2 y 6-3 y omite versiones transaccionales para concentrarse en el buffering.

## Qué hace una lectura

Una lectura necesita localizar la clave o el rango en la página y también consultar las actualizaciones pertinentes. Si una clave tiene varios cambios, debe escoger el que corresponda a la visibilidad de la transacción, no siempre el más reciente en términos físicos. En este ejemplo declaramos que las tres operaciones son visibles; una implementación con MVCC tiene información adicional para resolverlo.

Un borrado pendiente tiene una función concreta: impedir que el valor de la base vuelva a aparecer. Si el algoritmo encuentra `DELETE(30)` y después continúa con el `30:C` antiguo como si nada, está reconstruyendo un estado incorrecto.

El capítulo describe skiplists para los buffers: una **skiplist** es una lista ordenada con enlaces a distintas distancias que permiten saltar elementos durante la búsqueda. Se usa aquí como estructura ligera y adecuada para acceso concurrente. No significa que todas las páginas y versiones de WiredTiger usen la misma estructura para cada clase de actualización.

## Qué hace la reconciliación

La **reconciliación** combina la representación en memoria con la base y produce una imagen de disco. Cuando esta imagen supera el tamaño permitido, puede dividirse en varias páginas. Al agrupar modificaciones, disminuye la frecuencia con la que el camino de escritura paga la construcción física y parte de los cambios estructurales.

El trabajo no desaparece: leer requiere consultar lo pendiente y el motor debe reconciliar antes de que los buffers crezcan sin límite. Bajo presión de memoria, parte del trabajo aplazado puede repercutir en la latencia de las operaciones.

> [!note] “Sobrescribir la página” es una simplificación del capítulo
> La impresa 115 describe persistir el resultado sobrescribiendo la página original. La documentación oficial del block manager indica que una página modificada en un checkpoint se escribe en **un bloque nuevo**, manteniendo bloques necesarios para otros checkpoints. Lo correcto para esta explicación es decir “reemplazar la imagen vigente”; no presuponer el mismo offset físico. [WiredTiger: Block Manager](https://source.wiredtiger.com/develop/arch-block.html).

## Aplazar el flush no decide la durabilidad

**Flush** significa volcar una representación hacia almacenamiento. Tener operaciones en un buffer volátil no prueba que sean durables. El motor necesita un protocolo adicional que preserve lo confirmado si falla antes de reconciliar, mediante log u otro mecanismo según el diseño.

Del mismo modo, “en segundo plano” no significa “gratis para el usuario”. Las tareas de fondo consumen CPU, memoria y ancho de banda; si generan más trabajo del que pueden evacuar, aparece presión sobre las operaciones nuevas.

> [!question]- ¿Se puede devolver directamente la imagen base de una página modificada para acelerar una lectura?
> Solo si la semántica de esa lectura permite aquel estado. Para la lectura visible del ejemplo sería incorrecto: devolvería B en lugar de B2 y aún incluiría 30.

> [!question]- ¿Qué diferencia hay entre página limpia y página inexistente en memoria?
> Limpia significa que su estado no tiene cambios pendientes respecto a la imagen correspondiente. Puede seguir cargada en memoria. La presencia en caché y la condición limpia/modificada son propiedades distintas.

**Referencia:** PDF 4–6 · impresas 114–116 · figuras 6-2 y 6-3. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=4|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/02 Copy-on-write y snapshots en LMDB|Anterior]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/04 LA-Tree y buffers por subárbol|Siguiente]] →
