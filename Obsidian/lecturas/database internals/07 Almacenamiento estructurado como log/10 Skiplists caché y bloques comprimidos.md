---
title: "Database Internals — Capítulo 7 · Skiplists caché y bloques comprimidos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Skiplists caché y bloques comprimidos

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] La conexión entre RAM y disco
> La memtable debe mantener orden mientras cambia. Las tablas publicadas ya no cambian, pero se leen mediante bloques físicos, caché y decodificación.

## Una skiplist añade atajos a una lista

Una **skiplist** conserva una lista ordenada en su nivel base y añade enlaces que saltan varios elementos en niveles superiores. Cada nodo tiene una altura elegida con una distribución aleatoria; hay pocos nodos altos y muchos bajos. Esa jerarquía ofrece búsqueda esperada `O(log n)` bajo sus supuestos probabilísticos, aunque el peor caso puede ser lineal.

Para buscar 7 en el ejemplo de la figura 7-8, el enlace alto desde la cabecera llega a 10. Como 10 se pasa, se desciende y se alcanza 5. Desde 5 se prueba un enlace a 10, se vuelve a descender y se llega a 7. No hace falta recorrer 3, 5 y todo el resto de la lista base.

Insertar 6 exige encontrar sus predecesores en los niveles que ocupará. El nodo nuevo apunta a los antiguos sucesores y esos predecesores pasan a apuntar a 6. Los enlaces de niveles superiores a su altura quedan intactos. Eliminarlo conecta cada predecesor con su sucesor en los niveles correspondientes.

Las skiplists evitan las rotaciones de un árbol balanceado, pero los nodos dispersos y punteros pueden tener peor localidad de caché que una estructura con varias claves por nodo. No hay una ventaja universal solo por tener igual complejidad asintótica.

## La concurrencia requiere publicar nodos completos

Actualizar varios enlaces no es una operación indivisible. El capítulo describe un indicador `fully_linked`: señala cuándo un nodo ya está completamente incorporado. Un esquema concurrente debe definir qué ve un lector mientras la inserción está a medias, coordinar escritores y recuperar memoria sin liberar nodos aún referenciados.

**CAS**, compare-and-swap, actualiza una posición solo si todavía tiene el valor esperado. **Hazard pointers** son referencias publicadas que impiden recuperar un objeto que otro hilo está usando. No basta con decir “se usan punteros”: el protocolo de publicación y reclamación conserva la validez de los accesos. El acceso de arriba hacia abajo ayuda a un orden de operaciones, pero ese recorrido por sí solo no prueba ausencia de deadlocks en cualquier implementación.

## Un registro puede cruzar páginas

Una SSTable puede concatenar registros sin alinearlos a páginas. Si la página física mide 4096 bytes y un registro de 200 bytes empieza en offset 4000, ocupa bytes hasta 4199 y cruza dos páginas. Leerlo frío podría necesitar ambas. Una dirección absoluta identifica el comienzo, mientras tamaño y formato permiten reconstruir su contenido.

La caché guarda bloques o páginas decodificados. Sus bytes son inmutables, aunque los metadatos de la caché y el contador de referencias sí necesitan coordinación. Las referencias activas impiden expulsar memoria usada o retirar un archivo del que una lectura todavía depende.

## Comprimir exige conocer límites nuevos

Tres bloques lógicos de 4096 bytes podrían convertirse en tamaños físicos 1500, 2200 y 1700. Sus offsets físicos son 0, 1500 y 3700. El bloque lógico que empezaba en 8192 corresponde al bloque comprimido que empieza en 3700 y mide 1700.

```mermaid
flowchart LR
 L[Bloque lógico solicitado] --> T[Tabla de offsets y tamaños]
 T --> P[Leer región comprimida]
 P --> U[Descomprimir bloque]
 U --> C[Caché y búsqueda del registro]
```

La tabla de offsets enlaza la identidad lógica con una ubicación física de tamaño variable. Añadir ceros hasta el tamaño original perdería buena parte del ahorro. La capa de indirección conserva direccionamiento sin exigir que cada bloque comprimido ocupe una página completa.

El libro dice que las páginas comprimidas son siempre menores. Eso expresa la intención de usar compresión cuando aporta ahorro; datos poco compresibles pueden crecer por encabezados o por el algoritmo. Un formato real necesita admitir almacenamiento sin comprimir u otra política para ese caso.

> [!question]- ¿Inmutabilidad elimina todos los locks de la caché?
> Evita proteger cambios de contenido dentro del bloque publicado. Insertar entradas de caché, contar referencias, expulsarlas y cambiar vistas sigue siendo trabajo compartido que requiere un protocolo.

**Puente al siguiente tema:** ordenar valores facilita rangos, pero también hace que se reescriban al compactar. Podemos separar el orden de las claves de la ubicación de sus valores.

**Referencia:** PDF 21–24 · impresas 149–152 · figuras 7-8 a 7-10. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=21|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/09 Filtros Bloom y falsos positivos|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/11 Bitcask WiscKey y separación de claves y valores|Siguiente]] →
