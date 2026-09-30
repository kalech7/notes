---
title: "Database Internals — Bw-Tree: cadenas de deltas y CAS"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - arquitectura/bw-tree
  - arquitectura/concurrencia
---

# Bw-Tree: cadenas de deltas y CAS

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

El **Bw-Tree**, llamado *Buzzword-Tree* en el capítulo, conserva la organización lógica de un B-Tree y cambia la unidad que representa un nodo. En lugar de una página que se transforma cada vez, combina una **base** con una cadena de **deltas**. Un delta es una pequeña descripción de un cambio: insertar, reemplazar o borrar una clave.

La base y los deltas publicados son inmutables. Una actualización añade una pieza y publica una cabeza de cadena nueva. Un almacenamiento **append-only** escribe piezas nuevas sin sobrescribir las anteriores; luego un mantenimiento agrupa o elimina piezas obsoletas.

## El mismo nodo ya no vive en una única página física

Supongamos una base `A=10, B=20`. Se publican `PUT(A,12)`, `DELETE(B)` y `PUT(C,7)`. El delta más reciente queda al comienzo:

`PUT(C,7) → DELETE(B) → PUT(A,12) → base`

El estado lógico es `A=12, C=7`. B no existe, aunque todavía esté en los bytes de la base. El motor puede reconstruir desde la base aplicando los deltas en orden cronológico, o recorrer desde lo reciente usando reglas que impidan que una versión antigua reemplace a una nueva. Lo esencial es que el orden físico de la cadena no autoriza a aplicar los cambios al revés sin más.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/07-bw-cadenas.png]]

La caja violeta del padre contiene el identificador N7. La tabla verde traduce N7 a la cabeza física H3; las flechas de la cadena enlazan las piezas naranjas y la base azul. El resultado de la izquierda ya incorpora todos los cambios. Esta separación entre ID y dirección evita modificar al padre cada vez que aparece un delta nuevo.

Un **ID lógico** conserva la identidad del nodo aunque cambie dónde están sus piezas. Una **dirección física** señala una ubicación concreta. La **tabla de mapeo** en memoria permite pasar de la primera a la segunda. En la figura 6-7, las líneas virtuales representan relaciones resueltas mediante esta tabla; las líneas físicas unen piezas de una cadena.

## Qué ahorra y qué desplaza

Un cambio pequeño no necesita reescribir inmediatamente la base entera. Las piezas pueden tener tamaños distintos y almacenarse juntas sin reservar huecos dentro de cada página fija para todas las actualizaciones futuras.

La lectura paga el costo desplazado: atraviesa deltas y resuelve el estado visible. Además, siguen existiendo espacio para piezas antiguas, metadatos y trabajo de consolidación. “No reservar huecos en cada base” no equivale a “cero amplificación de espacio”.

**Referencia:** PDF 10–11 · impresas 120–121 · figura 6-7. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=10|Fuente del capítulo]].

## Publicar un delta sin que otro escritor pierda su cambio

La operación **compare-and-swap**, o **CAS**, recibe una ubicación, un valor esperado y un valor nuevo. Atómicamente compara el valor actual con el esperado; solo si coinciden instala el nuevo.

```text
CAS(tabla[N7], esperado=H, nuevo=D1)
```

Si la tabla aún apunta a H, se publica D1. Si otro escritor ya publicó D2, el valor dejó de ser H y CAS falla. Un CAS fallido no confirma aquel delta como cabeza vigente.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/08-cas.png]]

Los dos escritores comienzan leyendo H. T1 publica D1 primero; la casilla roja muestra por qué T2 no puede publicar D2 usando la misma expectativa. T2 relee D1 y prepara una publicación compatible con el estado actualizado. El resultado D2' → D1 → H conserva ambos cambios. En operaciones con comprobaciones dependientes del estado, reintentar también exige reevaluar esas comprobaciones.

Sin esa comparación, T2 podría guardar D2 → H después de T1, dejando D1 fuera de la cadena visible. T1 habría “ganado” una escritura que luego se perdió por una sustitución de puntero. CAS convierte esa carrera en éxito más reintento.

## Qué significa lock-free aquí

El capítulo describe acceso sin latches de exclusión sobre esas páginas y publicación mediante primitivas atómicas. Un algoritmo **lock-free** garantiza progreso del conjunto bajo sus condiciones: no garantiza que cada hilo termine en un número fijo de pasos. Un hilo puede perder repetidamente el CAS y reintentar.

Un algoritmo **wait-free** ofrece una garantía individual más fuerte. No debemos inferirla de que exista CAS. Tampoco debemos inferir durabilidad: el cambio atómico de una entrada en memoria y la conservación tras un fallo requieren mecanismos diferentes.

El Bw-Tree necesita un almacenamiento y un protocolo de recuperación que preserven piezas y referencias recuperables. El capítulo reserva detalles del almacenamiento log-structured para otra sección del libro que este PDF no contiene. Estas notas explican el árbol lógico sin inventar esa implementación completa.

> [!question]- ¿Por qué un ID lógico estable es necesario además de CAS?
> CAS publica la cabeza actual. El ID estable evita que todos los padres y otros enlaces tengan que almacenar y reemplazar su dirección física cada vez que cambia esa cabeza.

> [!question]- ¿Podemos aplicar primero PUT(A,12) y después la base A=10 al reconstruir?
> No si eso restaura A=10. Se debe preservar la precedencia del cambio nuevo sobre la base antigua; el algoritmo de recorrido tiene que expresarlo.

**Referencia:** PDF 11–12 · impresas 121–122. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=11|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/05 FD-Tree runs fences y fractional cascading|Anterior]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/07 Bw-Tree split merge consolidación y épocas|Siguiente]] →
