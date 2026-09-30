---
title: "Database Internals — Cache-oblivious: layout vEB y packed arrays"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - arquitectura/cache
  - arquitectura/memoria
---

# Cache-oblivious: layout vEB y packed arrays

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

Las variantes anteriores cambian cómo representar y publicar modificaciones. Los **cache-oblivious B-Trees** se concentran también en dónde colocar los datos para que una búsqueda aproveche varios niveles de la jerarquía de memoria.

Una **caché** guarda cerca del procesador una parte de los datos de un nivel más lento. Puede haber cachés de CPU, RAM y almacenamiento. Los datos suelen transferirse por bloques: necesitar una palabra puede obligar a traer sus vecinas. Si esas vecinas serán necesarias enseguida, aquella transferencia se aprovecha mejor.

## Cache-aware y cache-oblivious

Un algoritmo **cache-aware** utiliza parámetros del entorno, como el tamaño de bloque B, para diseñar su organización. Un B-Tree que ajusta el nodo a una página concreta es un ejemplo de ese razonamiento.

Un algoritmo **cache-oblivious** no recibe aquellos tamaños para fijar su layout, pero intenta mantener pocas transferencias para distintos tamaños de bloque. “Oblivious” no significa que los datos no se cacheen: significa que el algoritmo no necesita conocer esos parámetros para producir su organización.

El modelo de análisis usa dos niveles, uno rápido de capacidad M y otro lento, con transferencias de B unidades. Una organización con buenos resultados bajo las condiciones del modelo puede aprovechar también parejas de niveles de una jerarquía mayor. No elimina el paging, las políticas de reemplazo ni las constantes de rendimiento de una máquina real.

**Referencia:** PDF 14–15 · impresas 124–125. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=14|Fuente del capítulo]].

## Layout van Emde Boas: dividir por altura

El **layout van Emde Boas**, abreviado **vEB**, es una regla para ordenar físicamente los nodos de un árbol. No es el mismo concepto que un *van Emde Boas tree*, otra estructura de datos para claves enteras.

La regla es dividir el árbol por una altura intermedia, ordenar recursivamente la parte superior y después cada subárbol inferior, y almacenar esas secuencias de forma contigua. La contigüidad se repite en escalas grandes y pequeñas; esa es la propiedad útil para distintos B.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/11-layout-veb.png]]

El árbol superior tiene cuatro niveles y los números identifican nodos, no claves de búsqueda. Las cajas azules forman la parte de dos niveles más cercana a la raíz. Cada color inferior identifica otro subárbol de dos niveles. La fila física coloca juntos `[1,2,3]`, luego `[4,8,9]`, `[5,10,11]`, `[6,12,13]` y `[7,14,15]`. El árbol lógico conserva sus relaciones aunque las posiciones de sus nodos cambien.

El orden por niveles sería `1,2,3,4,5,6,7,8,9,10,11,12,13,14,15`. El vEB del ejemplo es:

`1,2,3,4,8,9,5,10,11,6,12,13,7,14,15`

Con bloques didácticos de cuatro nodos y el primer nodo alineado al inicio de un bloque, la ruta lógica `1→3→7→15` toca posiciones `0,2,12,14` en vEB: bloques 0 y 3. En el orden por niveles toca `0,2,6,14`: bloques 0, 1 y 3. El ejemplo muestra un ahorro posible de una transferencia con caché inicialmente vacía; no demuestra una ventaja en todas las rutas ni todos los bloques.

La figura 6-8 del libro usa 31 nodos y agrupa también subárboles menores dentro de los bloques grandes. Aquí usamos 15 para hacer explícito un corte exacto de dos niveles y evitar esconder la recursión en una imagen demasiado densa.

Como precisión de la fuente primaria, para alturas que no son potencias de dos el algoritmo publicado aplica una regla de redondeo específica; no consiste simplemente en escoger siempre mitades iguales. La propiedad central sigue siendo que cada subárbol recursivo ocupa un intervalo contiguo. [Bender, Demaine y Farach-Colton: Cache-Oblivious B-Trees, sección 2.1](https://erikdemaine.org/papers/CacheObliviousBTrees_SICOMP/paper.pdf).

## El problema de insertar en un layout compacto

Si los datos están todos consecutivos y una nueva clave corresponde al centro, insertar puede obligar a desplazar una gran parte del array. El **packed array**, o array con huecos distribuidos, reserva espacios entre elementos para que muchas inserciones tengan un desplazamiento local.

El array sigue ordenado si se ignoran los huecos. Un hueco no representa una clave especial ni un tombstone: es capacidad libre. Su ubicación se ajusta cuando las regiones se vuelven demasiado densas o demasiado vacías.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/12-packed-array.png]]

La primera fila guarda cuatro claves en ocho posiciones. El 10 de la segunda ocupa un hueco entre 8 y 12. Insertar 11 en la tercera exige mover 12 al hueco vecino. La última redistribuye una ventana mayor para recuperar espacio en una región congestionada. El verde distingue inserciones y el naranja elementos movidos; el punto representa una posición vacía. Todas las filas mantienen las claves en orden.

La **densidad** de un segmento es `elementos / capacidad`. Cuatro elementos en ocho posiciones tienen densidad 50 %. Tras dos inserciones hay seis en ocho, 75 %. Sin embargo, el segmento local `[8,10,11,12]` puede estar al 100 % aunque el array completo tenga espacio libre. Por eso los límites se evalúan en ventanas de distinto tamaño.

Si una región rebasa su umbral, el algoritmo redistribuye una región mayor. Si el conjunto completo se vuelve demasiado denso o disperso, puede reconstruirse para crecer o encogerse. Mantener huecos reduce muchos movimientos locales, pero cuesta espacio y algunas operaciones grandes de mantenimiento.

## El árbol índice tiene que acompañar los movimientos

El capítulo combina un árbol de búsqueda estático con el packed array inferior. **Estático** aquí describe una organización de búsqueda para un conjunto y layout determinados; las modificaciones del conjunto exigen mantener o reconstruir los enlaces correspondientes. Si un elemento cambia de posición en el array, una referencia al offset antiguo debe actualizarse.

Por ejemplo, mover 12 de la posición 4 a la 5 no altera su valor ni su orden relativo. Pero un índice que conserve “12 está en 4” empezaría a dirigir una lectura hacia otra clave. Localidad y coherencia del índice deben conservarse juntas.

El autor señala límites prácticos y su conocimiento de implementaciones en el momento de escribir el libro. No usamos esa observación histórica como inventario de productos de 2026 ni como prueba de que esta técnica siempre gane a un B-Tree ajustado a páginas.

> [!question]- ¿Cache-oblivious elimina la amplificación de espacio?
> No. El packed array mantiene huecos deliberadamente. Su objetivo es equilibrar localidad y costo de actualización bajo el modelo, no ocupar cada byte disponible.

> [!question]- ¿Conocer B es un error en un motor real?
> No. Cache-aware es una estrategia válida. El capítulo contrasta objetivos y modelos; no exige ignorar información útil de una implementación concreta.

**Referencia:** PDF 15–16 · impresas 125–126 · figuras 6-8 y 6-9. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=15|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/07 Bw-Tree split merge consolidación y épocas|Anterior]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/09 Comparar variantes y conectar los mecanismos|Siguiente]] →
