---
title: "DDIA — Rebalanceo: shards fijos, división dinámica y rangos proporcionales"
created: 2026-09-29
capitulo: 7
tags:
  - lecturas/ddia
  - arquitectura/sharding
---

# DDIA — Rebalanceo: shards fijos, división dinámica y rangos proporcionales

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|↑ Índice del capítulo 7]]

**Rebalancear** es mover datos y carga entre nodos cuando el clúster cambia: entra un nodo, sale uno, un shard crece demasiado o se calienta. El objetivo es doble: que al terminar la carga vuelva a estar pareja y que por el camino se mueva **la menor cantidad posible de datos**, porque mover datos consume red, disco y CPU mientras el sistema sigue atendiendo peticiones.

## Por qué `hash % N` es mala idea

La primera ocurrencia es asignar cada clave al nodo `hash(clave) % N`, con N nodos. Con 10 nodos, el resto va de 0 a 9 (el último dígito del hash en decimal). Funciona mientras N no cambie. Cuando cambia, casi todas las claves cambian de nodo.

La figura 7-3 lo muestra de 3 a 4 nodos: el hash 3 pasa del nodo 0 al 3, el 6 del nodo 0 al 2, el 9 del nodo 0 al 1, y así sucesivamente.

**Cálculo de cuánto se mueve.** Una clave se queda donde estaba solo si `h % 3 == h % 4`. El patrón se repite cada 12 valores (mínimo común múltiplo de 3 y 4). Revisando 0–11, solo se cumplen 0, 1 y 2. Se quedan 3 de cada 12, el **25 %**; se mueve el **75 %**. Lo ideal sería mover solo lo que le toca al nodo nuevo: 1/4 = 25 %.

De 10 a 11 nodos: se quedan quietas las claves con `h % 110` entre 0 y 9, es decir, 10 de cada 110 ≈ **9,1 %**; se mueve ≈ **90,9 %**, cuando lo necesario sería ≈ 9,1 %. Suponiendo hashes uniformes y los mismos identificadores de nodo, al pasar de N a N + 1 solo se queda 1/(N + 1) de los datos: exactamente la fracción que debería *moverse*. El módulo es fácil de calcular pero produce movimientos innecesarios masivos.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-03-hash-modulo-rebalanceo.png|1000]]

Las cajas agrupan los mismos hashes, del 0 al 23, antes y después de añadir el cuarto nodo. Con tres nodos se calcula hash % 3; con cuatro, hash % 4. La operación cambia el destino de 18 de los 24 valores de este ejemplo, aunque solo se haya añadido una máquina. Los números son hashes, no necesariamente las claves originales.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=9|PDF 9 · impresa 259 · figura 7-3]].

## Número fijo de shards

La solución sencilla y muy usada es crear **muchos más shards que nodos** desde el principio y dar varios a cada nodo. Ejemplo del libro: 10 nodos y 1.000 shards, 100 por nodo. La clave va al shard `hash(clave) % 1.000` y, **aparte**, el sistema guarda una tabla «shard → nodo».

Al añadir un nodo, el sistema le pasa shards enteros de los demás hasta equilibrar. La figura 7-4 parte de 4 nodos con 20 shards (s0–s19, cinco por nodo). Al llegar el nodo 4, cada nodo antiguo le cede uno: s4, s9, s14 y s19. Quedan 4 shards por nodo y se ha movido 4/20 = **20 %**, justo la parte que corresponde al nodo nuevo. Estos porcentajes de datos suponen shards de tamaño parecido. Con 1.000 shards y un nodo 11: cada nodo antiguo cede 9 shards (de 100 a 91) y el nuevo recibe 90, ≈ 9 % de los datos.

Qué cambia y qué no: la asignación **clave → shard** nunca cambia; solo cambia **shard → nodo**. Mover un shard entero es más barato que dividirlo. La transferencia tarda, así que mientras dura, lecturas y escrituras siguen usando la asignación antigua.

Detalles prácticos del libro:

- Conviene un número de shards **divisible por muchos factores**, para repartir bien con distintos tamaños de clúster sin exigir potencias de 2. Por ejemplo (propio), 720 se divide exactamente entre 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16 o 24 nodos; 1.000 no se divide entre 3, 6 ni 12.
- Con **hardware desigual**, das más shards a los nodos potentes.
- Lo usan, según el libro, Citus (capa de sharding sobre PostgreSQL), Riak, Elasticsearch y Couchbase.

Límites: en este modelo con un dueño por shard, **no puedes aprovechar más nodos como dueños independientes que shards**. La replicación puede añadir otras máquinas con copias del mismo shard, pero eso no crea nuevas divisiones de escritura. Si te quedas corto, hace falta un **resharding** costoso: dividir cada shard y reescribirlo, con mucho disco extra, y algunos sistemas no lo permiten mientras hay escrituras, lo que implica parada. Además, como cada shard es una fracción fija del total, **su tamaño crece con los datos**: 1.000 shards con 100 GB son 100 MB cada uno; con 50 TB son 50 GB cada uno. Shards enormes encarecen el rebalanceo y la recuperación tras fallos; shards diminutos cuestan demasiado en sobrecarga. Acertar con el tamaño es difícil si el volumen de datos es muy variable.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-04-shards-fijos-rebalanceo.png|1000]]

Los veinte shards mantienen su identidad y las claves asignadas a cada uno. Para repartirlos entre cinco máquinas, los shards s4, s9, s14 y s19 migran al nuevo nodo 4; los otros dieciséis se quedan en sus nodos. Las flechas sólidas representan las cuatro transferencias y las líneas discontinuas muestran las asignaciones que no cambian.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=10|PDF 10 · impresa 260 · figura 7-4]].

## División dinámica por rangos

En el sharding por rangos (de claves o de hashes), el número de shards **se adapta** al volumen. Al crear una base vacía no hay rangos que dividir, así que toda la carga inicial cae en poco espacio. La primera edición lo describía como una base que arranca con una sola partición; la segunda lo formula como que al principio no hay rangos de claves que dividir. Por eso HBase y MongoDB permiten **pre-dividir** una base vacía, si ya conoces la distribución de claves que vas a tener.

Después, un shard que crece se **divide** en dos subrangos contiguos, que pueden ir a nodos distintos; si se borra mucho, shards vecinos pequeños se **fusionan**. Se parece conceptualmente a dividir páginas de un B-tree cuando crecen; aquí se dividen rangos completos que pueden pasar a máquinas distintas. La división se dispara al alcanzar un tamaño configurado (la edición cita 10 GB en HBase como ejemplo del umbral) o, en algunos sistemas, cuando el rendimiento de escritura supera un umbral de forma sostenida: así un shard caliente se divide aunque no guarde muchos datos.

El libro señala la ventaja: con pocos datos basta con pocos shards y la sobrecarga es pequeña; con muchos datos cada shard tiene un tamaño objetivo configurable para disparar divisiones, que puede superarse mientras termina la operación. (El texto impreso empieza esa frase con «Unfortunately», aunque describe una ventaja; parece un desliz editorial.) El inconveniente real: **dividir es caro**, porque reescribe todos los datos del shard en archivos nuevos, como una compactación. Y el shard que necesita dividirse suele ser el que más carga tiene, así que la división puede empujarlo a la sobrecarga.

## Rangos proporcionales a los nodos (Cassandra y ScyllaDB)

Cassandra y ScyllaDB usan una variante del rango de hash: el espacio de hashes se divide en un número de rangos **proporcional al número de nodos**, con **fronteras aleatorias**. La figura 7-6 muestra 3 rangos por nodo sobre un espacio de 0 a 1024; el libro dice que en realidad son 16 por nodo por defecto en Cassandra y 256 en ScyllaDB (cifras de la edición, no verificadas como valores actuales).

**Cálculo con la figura (propio).** Para medir longitudes se usan las fronteras como intervalos contiguos sin contar dos veces sus extremos: de 88 a 128 la longitud es `128 − 88 = 40`. La frontera 1024 cierra un espacio de longitud 1024; no se están contando 1025 enteros incluidos. Antes, con 3 nodos:

| Nodo | Rangos | Tamaño | Fracción |
|---|---|---|---|
| n0 | 88–128, 309–398, 930–1024 | 40 + 89 + 94 = 223 | 21,8 % |
| n1 | 0–88, 511–672, 702–930 | 88 + 161 + 228 = 477 | 46,6 % |
| n2 | 128–309, 398–511, 672–702 | 181 + 113 + 30 = 324 | 31,6 % |

Con solo 3 rangos por nodo, n1 tiene más del doble que n0. Las fronteras aleatorias producen rangos desiguales; tener **muchos** rangos por nodo es lo que hace que esas diferencias se compensen.

Al añadir n3 con fronteras 60, 276 y 551, recibe 60–88 y 551–672 de n1, y 276–309 de n2: 28 + 33 + 121 = 182 (17,8 %). Después, n1 queda con 328 (32,0 %), n2 con 291 (28,4 %) y n0 sin cambios con 223 (21,8 %). La suma verifica que no faltan ni se duplican rangos: `223 + 328 + 291 + 182 = 1024`. Se reasignó solo el 17,8 % del espacio de hash y todo hacia el nodo nuevo. Con claves uniformemente dispersas, corresponde aproximadamente a esa fracción de datos; no garantiza la misma fracción de peticiones. El libro lo resume como una parte **aproximadamente** justa; con 3 rangos la aproximación es gruesa (17,8 % frente al 25 % ideal).

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-06-rangos-virtuales-nodo-nuevo.png|1000]]

Las barras reproducen los límites de hash y los propietarios de la figura original; n0 significa nodo 0 y así sucesivamente. El nodo 3 se incorpora tomando dos subrangos del nodo 1 y uno del nodo 2. Los rangos tienen tamaños distintos y cada máquina almacena varios rangos separados. Las cifras indican fronteras, no dos copias de la misma clave en rangos vecinos.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=12|PDF 12 · impresa 262 · figura 7-6]].

## Hashing consistente

Un algoritmo de **hashing consistente** asigna claves a un número dado de shards cumpliendo dos propiedades: cada shard recibe aproximadamente las mismas claves, y cuando cambia el número de shards **se mueven las menos claves posibles**. «Consistente» aquí no tiene nada que ver con la consistencia entre réplicas ni con la C de ACID: significa que una clave tiende a quedarse donde estaba.

El esquema de Cassandra y ScyllaDB se parece a la definición original. Otras variantes son el **hashing de mayor peso aleatorio** (*rendezvous hashing*) y el **jump consistent hash**. En ellas, el nodo nuevo no recibe subrangos de unos pocos shards, sino **claves sueltas** tomadas de todos los nodos. Cuál conviene depende de la aplicación.

Precaución de vocabulario: «vnode» es el nombre de un shard en Riak y, en el mundo Cassandra, «nodos virtuales» designa los múltiples rangos por nodo (esto último es elaboración propia). En ningún caso es una máquina.

## ¿Automático o manual?

Algunos sistemas deciden solos cuándo dividir y mover; otros esperan a un administrador; Couchbase y Riak, según el libro, proponen una asignación y un humano la confirma. La automatización ahorra trabajo y permite autoescalar (DynamoDB se promociona como capaz de añadir o quitar shards en minutos). Pero rebalancear es caro: redirigir peticiones y mover muchos datos puede saturar la red y los nodos, y si el sistema está cerca de su máximo de escrituras, la división puede no alcanzar al ritmo de llegada.

El peligro mayor es combinarla con la **detección automática de fallos**: un nodo sobrecargado responde lento, los demás lo creen muerto, mueven su carga, se sobrecargan ellos y también parecen caídos. Es un **fallo en cascada**. Por eso puede convenir un humano en el ciclo; y el rebalanceo manual permite prepararse antes de picos conocidos, como el Cyber Monday o la venta de entradas de un Mundial.

> [!question]- Con `hash % N`, ¿qué fracción de datos se mueve al pasar de 4 a 5 nodos?
> Se quedan las claves con `h % 20` entre 0 y 3: 4 de 20 = 20 %. Se mueve el 80 %, cuando bastaría con mover el 20 %.

> [!question]- ¿Por qué con shards fijos no cambia la asignación de claves a shards al añadir nodos?
> Porque la fórmula usa el número de shards (fijo), no el de nodos. Solo cambia la tabla que dice en qué nodo vive cada shard, y se mueven shards enteros.

> [!question]- ¿Por qué un rebalanceo automático puede empeorar una sobrecarga?
> Porque confunde lentitud con caída, mueve datos de un nodo sobrecargado a otros y añade tráfico de red y trabajo de copia; los demás nodos pueden sobrecargarse y ser declarados caídos también.

## Referencias

PDF 7–15 · impresas 257–265 · figuras 7-3, 7-4 y 7-6: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=7|PDF 7 · impresa 257 (pre-splitting)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=8|PDF 8 · impresa 258 (división y módulo)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=9|PDF 9 · impresa 259 (figura 7-3)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=10|PDF 10 · impresa 260 (figura 7-4)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=11|PDF 11 · impresa 261]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=12|PDF 12 · impresa 262 (figura 7-6)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=13|PDF 13 · impresa 263 (hashing consistente)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=14|PDF 14 · impresa 264]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=15|PDF 15 · impresa 265 (automático frente a manual)]].

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/04 Índices secundarios locales y globales|← Índices secundarios locales y globales]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/06 Enrutamiento y ejecución de consultas|Enrutamiento y ejecución de consultas →]]
