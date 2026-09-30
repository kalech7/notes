---
title: "Database Internals — FD-Tree: runs, fences y fractional cascading"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - arquitectura/fd-tree
  - arquitectura/busqueda
---

# FD-Tree: runs, fences y fractional cascading

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

Un **FD-Tree**, *Flash Disk Tree*, limita las actualizaciones en el sitio a una estructura pequeña y almacena gran parte de los datos en **runs**. Un run es una secuencia ordenada e inmutable de registros. Para cambiar su contenido se construye otra secuencia y se sustituye la versión anterior.

El árbol frontal, llamado **head tree**, es un B-Tree mutable pequeño que acumula cambios. Cuando se llena, su contenido se vuelca y se fusiona con los niveles de runs. La idea es convertir muchas escrituras dispersas en trabajo ordenado sobre lotes mayores.

## Por qué los niveles crecen por un factor

Si la capacidad de referencia es H y cada nivel multiplica el anterior por k, los tamaños objetivo tienen la forma `H, kH, k²H, ...`. Con `H=4` y `k=4`, podemos ilustrar umbrales de 4, 16 y 64 registros. Son tamaños inventados para entender el crecimiento, no parámetros del libro.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/05-fd-tree.png]]

La cabeza naranja acepta los cambios nuevos. Los runs verde, azul y violeta agrupan los registros que descendieron por fusiones. Las flechas verticales representan esa propagación, no punteros del árbol. Los fences mencionados a la derecha son referencias de búsqueda entre niveles. La caja roja recuerda que borrar necesita ocultar versiones que todavía existen físicamente abajo.

Una cabeza llena se combina con L1. Si el run resultante supera el umbral correspondiente, sus datos descienden mediante otra fusión hacia L2. Si L2 existe, se construye un resultado nuevo que incorpora ambos contenidos. La cascada puede continuar.

La expresión **logarithmic runs** no significa que los tamaños crezcan logarítmicamente. Crecen geométricamente por k; el número de niveles necesario para albergar una cantidad creciente de datos tiene relación logarítmica con esa cantidad. La cabeza pequeña conserva trabajo aleatorio, mientras los runs concentran el trabajo grande y ordenado.

## La dificultad que aparece en lectura

Una misma clave puede estar en varios niveles. Un cambio reciente puede reemplazar o borrar una entrada antigua sin modificar su run. El lector debe resolver qué versión sigue vigente; las fusiones deben eliminar o mantener registros de acuerdo con esa regla.

Un **tombstone** es una entrada que representa un borrado. El capítulo usa también el nombre *filter entry* en el contexto de FD-Tree. Si L1 tiene `DELETE(70)` y L3 conserva `70:viejo`, una lectura no puede devolver el valor de L3 porque encontró un borrado más reciente arriba.

Eliminar el tombstone demasiado pronto permitiría que aquel valor antiguo reaparezca. Se puede descartar cuando ya se procesaron las versiones inferiores que debía ocultar. El libro describe su llegada al nivel inferior como ese punto; la regla general es que no quede ninguna versión antigua pertinente que pueda resucitar. Este ejemplo no incorpora snapshots que exigieran conservar historia adicional.

**Referencia:** PDF 7–10 · impresas 117–120 · figura 6-6. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=7|Fuente del capítulo]].

## Fractional cascading: aprovechar la búsqueda del nivel anterior

Si cada run es ordenado, podemos buscar con búsqueda binaria en cada uno. Pero repetir desde cero pierde una oportunidad: al terminar una búsqueda arriba ya sabemos una posición aproximada respecto a las mismas claves abajo.

**Fractional cascading** añade muestras de un nivel inferior al superior y mantiene enlaces a sus posiciones originales. Un **fence** o puente orienta la búsqueda hacia una página o una zona cercana del nivel inferior. Se copian solo ciertas claves como metadatos de navegación; no se copian necesariamente sus registros completos.

El capítulo empieza con estas tres listas:

```text
A1 = [12, 24, 32, 34, 39]
A2 = [22, 25, 28, 30, 35]
A3 = [11, 16, 24, 26, 30]
```

Para mostrar una construcción coherente de abajo arriba, en esta nota muestreamos las posiciones 1, 3, ... usando índices desde cero:

1. `C3=A3`. Tomamos 16 y 26 como muestras y las añadimos a A2.
2. `C2=[16,22,25,26,28,30,35]`. Muestreamos **este catálogo ya aumentado**: 22, 26 y 30.
3. Añadimos esas muestras a A1: `C1=[12,22,24,26,30,32,34,39]`.

**A** designa registros originales; **C** designa catálogos con entradas auxiliares. Las muestras no cambian el conjunto original. En una construcción general se etiquetan origen, duplicados y posiciones para volver al registro pertinente.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/06-fractional-cascading.png]]

Las celdas naranjas son muestras que el catálogo recibió desde abajo. Las flechas unen esas muestras con su posición en el catálogo inferior. La consulta busca el primer elemento mayor o igual que 27: empieza con búsqueda binaria en C1, usa los puentes para acercarse a la posición correcta en C2 y C3 y termina mediante comprobaciones locales. Las cajas de la derecha distinguen los resultados de navegación de los resultados en las listas originales.

## La consulta de 27 paso a paso

La operación **lower bound** localiza el primer elemento `>= clave`. En C1 el lower bound de 27 es 30. Ese 30 es auxiliar: A1 no contiene 30. Para responder en A1, los metadatos de origen conducen a 32.

El puente del 30 lleva a su posición en C2. Allí las entradas anteriores son 28 y 26: 28 cumple `>=27` y 26 ya no. El resultado en A2 es 28. Para continuar a C3 se utiliza una muestra cercana, 26, que apunta al 26 inferior. El siguiente elemento es 30, resultado en A3.

| Lista original | Lower bound de 27 |
|---|---:|
| A1 | 32 |
| A2 | 28 |
| A3 | 30 |

No hemos asumido que 27 exista ni que los tres niveles devuelvan la misma clave. Lo que se reutiliza es una **posición aproximada en un orden compartido**.

> [!note] Diferencia explícita con el ejemplo impreso
> El libro presenta `A1=[12,24,25,30,32,34,39]` como catálogo aumentado. Sus puentes 25 y 30 ilustran la navegación. Para enseñar el muestreo recursivo, aquí usamos C1 con 22, 26 y 30, obtenidos de C2 después de aumentarlo. El ejemplo impreso no muestra todos los metadatos ni explicita una construcción recursiva completa; no debemos tomar solo sus cuatro flechas como un algoritmo general con una cota garantizada de saltos.

En FD-Tree, la adaptación usa las primeras claves de páginas inferiores como fences en niveles superiores. Con eso reduce la búsqueda repetida entre runs. Las referencias deben reconstruirse cuando una fusión cambia las páginas y sus posiciones: una optimización de lectura introduce trabajo de mantenimiento.

> [!question]- ¿Los fences evitan leer todos los niveles?
> Reducen el trabajo para localizar la zona pertinente de cada nivel. No borran la necesidad de resolver registros y tombstones que puedan existir en niveles distintos.

> [!question]- ¿Por qué muestrear en lugar de copiar todas las claves?
> Copiar todo multiplicaría metadatos y mantenimiento. Muestrear busca intervalos pequeños con menos entradas auxiliares; su frecuencia forma parte del algoritmo y de sus garantías.

**Referencia:** PDF 8–10 · impresas 118–120 · figuras 6-5 y 6-6. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=8|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/04 LA-Tree y buffers por subárbol|Anterior]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/06 Bw-Tree cadenas de deltas y CAS|Siguiente]] →
