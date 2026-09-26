---
title: "Database Internals — Atlas visual explicado"
created: 2026-09-26
tags:
  - lecturas/database-internals
  - recursos-visuales
  - fundamentos
---

# Atlas visual explicado

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/00 Guía y fundamentos/00 Índice|Guía y fundamentos]]

Los primeros ocho recursos son modelos técnicos vectoriales originales. El noveno es una analogía visual generada para fijar el mecanismo del `split`. Cada recurso aísla una relación que después aparece con más detalle en las notas.

## 1. Una consulta termina en páginas

![[Obsidian/lecturas/database internals/Recursos visuales/01-arquitectura-dbms.svg|1000]]

La ruta azul transforma una solicitud en page IDs y bytes. Las líneas moradas no son pasos posteriores: transacciones y recovery restringen el proceso completo. Sirve para no confundir el storage engine con todo el DBMS.

## 2. Un split repara la ruta del padre

![[Obsidian/lecturas/database internals/Recursos visuales/02-split-btree.svg|1000]]

La clave `35` obliga a dividir. `30` se copia al padre como frontera y permanece en la hoja derecha, siguiendo una convención B+ didáctica. El rango `≥60`, que no cambia, se omite. La enseñanza es que dividir datos también exige actualizar navegación.

## 3. Slotted page: orden lógico, ubicación física

![[Obsidian/lecturas/database internals/Recursos visuales/03-slotted-page.svg|1000]]

Los slots ordenados apuntan a celdas variables que no necesitan estar ordenadas físicamente. Las flechas muestran la indirección. Mover offsets pequeños suele ser más barato que mover payloads.

## 4. Vacuum convierte suma libre en un hueco útil

![[Obsidian/lecturas/database internals/Recursos visuales/04-vacuum-page.svg|1000]]

Antes existen bytes libres, pero están separados. Después forman un tramo contiguo. La regla de visibilidad determina qué puede eliminarse; la freelist hace reutilizables páginas enteras.

## 5. Filas y columnas responden a accesos distintos

![[Obsidian/lecturas/database internals/Recursos visuales/05-filas-columnas.svg|1000]]

La consulta solo necesita `precio`. En layout por filas atraviesa registros completos; en layout por columnas lee el vector necesario. Si la operación necesitara la entidad completa, la comparación podría favorecer filas.

## 6. Fanout reduce saltos entre páginas

![[Obsidian/lecturas/database internals/Recursos visuales/06-fanout-altura.svg|1000]]

La ruta naranja compara cantidad de páginas visitadas, no cantidad total de nodos dibujados. El B-Tree hace más comparaciones dentro de un nodo ancho para reducir altura.

## 7. Endianness es parte del contrato

![[Obsidian/lecturas/database internals/Recursos visuales/07-endianness.svg|1000]]

`0x12345678` contiene los mismos cuatro bytes en ambas columnas, pero cambia su posición. Sin conocer tamaño, signo y endianness, el lector puede reconstruir otro valor.

## 8. Dos problemas de borde

![[Obsidian/lecturas/database internals/Recursos visuales/08-rightmost-highkey-overflow.svg|1000]]

El panel izquierdo explica por qué `N` separadores producen `N+1` intervalos. El derecho muestra cómo overflow preserva páginas fijas al precio de lecturas y bookkeeping adicionales.

## 9. El split como reorganización de un archivo

![[Obsidian/lecturas/database internals/Recursos visuales/09-split-btree-archivo.png|1000]]

El cajón lleno representa la página antes del overflow; los cajones azul y verde son las páginas resultantes, que conservan el orden. `67` queda a la derecha porque supera la frontera `60`. La tarjeta `60` en el estante superior representa el separador publicado en el padre: dividir una página también obliga a reparar la navegación desde arriba. Es una analogía pedagógica; la convención concreta puede copiar la primera clave derecha o publicar otra frontera equivalente.

> [!warning] Límite de las figuras
> Omiten locking, WAL, checksums y variantes de implementación cuando esos detalles no son el objeto del dibujo. En la analogía del archivo tampoco deben tomarse literalmente cajones o tarjetas: representan páginas, entradas, punteros y separadores. La explicación escrita indica qué se simplificó.

---

**Anterior:** [[Obsidian/lecturas/database internals/00 Guía y fundamentos/01 Antes de empezar bytes páginas y costos|Bytes, páginas y costos]] · **Índice:** [[Obsidian/lecturas/database internals/00 Guía y fundamentos/00 Índice|Guía]] · **Siguiente:** [[Obsidian/lecturas/database internals/00 Guía y fundamentos/03 Comparar bases y diseñar benchmarks|Comparar bases y diseñar benchmarks]]
