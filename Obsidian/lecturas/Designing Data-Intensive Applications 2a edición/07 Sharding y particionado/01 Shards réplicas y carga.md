---
title: "DDIA — Shards, réplicas y reparto de carga"
created: 2026-09-29
capitulo: 7
tags:
  - lecturas/ddia
  - arquitectura/sharding
---

# DDIA — Shards, réplicas y reparto de carga

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|↑ Índice del capítulo 7]]

Una base de datos distribuida reparte los datos de dos formas que se complementan. La **replicación** (capítulo 6) guarda *la misma* información en varios nodos. El **sharding** divide la información en trozos y guarda *trozos distintos* en nodos distintos. Un **shard** es uno de esos trozos: un subconjunto de registros que se comporta casi como una base de datos pequeña e independiente. La regla habitual es que cada registro (fila, documento, par clave-valor) pertenece a **exactamente un** shard.

La causa de fragmentar es que ya no cabe todo en una máquina: hay demasiados datos o demasiadas escrituras por segundo. La consecuencia es que ahora necesitas una regla para saber en qué shard vive cada registro, y todo lo que antes era «local» (buscar, unir, actualizar varias filas a la vez) puede pasar a ser una operación entre máquinas.

## Dividir y copiar a la vez

Sharding y replicación casi siempre se usan juntos: cada registro está en un solo shard, pero ese shard tiene varias copias para tolerar fallos. La figura 7-1 del libro muestra cuatro nodos y cuatro shards con replicación de líder único. Cada shard tiene un líder y dos seguidores, y cada nodo guarda tres copias de shards distintos: es líder de uno y seguidor de otros dos. Por ejemplo, el nodo 4 es líder del shard 4 y seguidor de los shards 1 y 3. Una escritura dirigida al shard 4 entra por el nodo 4 y desde allí fluye por el canal de replicación de ese shard hacia los nodos 2 y 3.

La idea importante es que **el líder se elige por shard, no por nodo**. Así la carga de escritura también se reparte: ningún nodo recibe todas las escrituras. Como el esquema de sharding es en gran parte independiente del de replicación, el capítulo deja la replicación de lado y habla de cada shard como si tuviera una sola copia.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-01-sharding-y-replicacion.png|1000]]

Cada caja exterior es una máquina; las cajas interiores son las copias de shards que guarda. Un shard tiene un solo líder y dos seguidores, pero una máquina puede ser líder de un shard y seguidora de otros. Las flechas representan la replicación desde el líder hacia las otras copias del mismo shard. La escritura del shard 4 llega a su líder, en el nodo 4.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=2|PDF 2 · impresa 252 · figura 7-1]].

## Un mismo concepto con muchos nombres

| Sistema | Nombre de lo que el libro llama *shard* |
|---|---|
| Kafka | *partition* |
| CockroachDB | *range* |
| HBase, TiDB | *region* |
| Couchbase | *vBucket* |
| Riak | *vnode* |
| Cassandra | *token-range* |
| Bigtable, YugabyteDB, ScyllaDB | *tablet* |

Hay dos trampas de vocabulario. En PostgreSQL, *partitioning* significa dividir una tabla grande en varios archivos **dentro de la misma máquina** (útil, por ejemplo, para borrar una partición entera de golpe), mientras que *sharding* reparte entre máquinas. En muchos otros sistemas las dos palabras son sinónimos. Además, particionar datos no tiene nada que ver con una **partición de red** (*netsplit*), que es un fallo de comunicación entre nodos (capítulo 9). Y un *vnode* de Riak es un shard lógico, no una máquina: cuando leas «nodo» a secas, piensa en un servidor.

El libro recoge dos teorías sobre el origen de *shard*: los fragmentos de cristal del juego *Ultima Online*, cada uno con una copia del mundo, o un acrónimo de un sistema de los años ochenta del que no quedan detalles. Es una curiosidad, no un concepto técnico.

## Cuándo compensa fragmentar

El motivo principal es la **escalabilidad horizontal**: crecer añadiendo máquinas en lugar de comprar una más grande (arquitectura *shared-nothing*). Si cada shard recibe una fracción parecida del trabajo, varias máquinas procesan en paralelo.

Pero el libro insiste en que el sharding es una solución **pesada**. Si una sola máquina aguanta tu volumen de datos y de escrituras, suele ser mejor no fragmentar. Las razones:

- Hay que elegir una **clave de partición**; todos los registros con la misma clave van al mismo shard. Acceder por esa clave permite ir al shard correspondiente; acceder por otra cosa puede obligar a buscar en todos los shards, salvo que exista un índice o una ruta adicional que localice los registros.
- El esquema de sharding **es difícil de cambiar** una vez hay datos.
- Encaja bien con datos clave-valor, pero en datos relacionales complica los índices secundarios y los joins entre shards.
- Si una escritura sobre varios shards debe ser atómica, necesita una **transacción distribuida** (capítulo 8) o un protocolo equivalente que garantice esa atomicidad, que suele ser mucho más lenta que una local y puede convertirse en cuello de botella.

Si los datos caben en un nodo y el problema son las **lecturas** que admiten consultar réplicas, normalmente puedes usar réplicas de lectura, porque cada réplica puede atender consultas. Las escrituras no se reparten así: cada réplica tiene que aplicar todas las escrituras.

**Ejemplo propio con pedidos.** Un nodo aguanta unas 8.000 escrituras por segundo. En campaña se esperan 30.000 escrituras por segundo. Añadir réplicas no ayuda: cada una tendría que aplicar las 30.000. Hace falta dividir las escrituras: 30.000 / 8.000 = 3,75, así que al menos 4 shards si la carga se reparte perfectamente. Si quieres que cada nodo trabaje al 70 % como máximo, la capacidad útil es 0,7 × 8.000 = 5.600 y necesitas 30.000 / 5.600 ≈ 5,4, es decir, 6 shards con capacidad independiente, por ejemplo líderes en seis nodos distintos. El número de shards por sí solo no crea esa capacidad: si alojas todos sus líderes en la misma máquina, comparten su límite. Estos cálculos también suponen que el trabajo de seguidores y replicación ya está incluido en la capacidad medida. En cambio, con 30.000 lecturas y 2.000 escrituras por segundo, un líder y varias réplicas de lectura resuelven el problema sin fragmentar.

## Sharding dentro de una sola máquina

Algunos sistemas fragmentan incluso en un único servidor: ejecutan un proceso de un solo hilo por núcleo para aprovechar el paralelismo de la CPU o la arquitectura **NUMA** (*nonuniform memory access*, en la que cada CPU accede más rápido a ciertos bancos de memoria). El libro cita a Redis, VoltDB y FoundationDB como sistemas que usan un proceso por núcleo y reparten la carga entre núcleos mediante sharding.

## Sharding por inquilino

En productos SaaS **multiinquilino**, cada inquilino (*tenant*) es un cliente con un conjunto de datos separado del resto. Puedes dar un shard a cada inquilino o agrupar varios inquilinos pequeños en un shard mayor; esos shards pueden ser bases físicamente separadas. Ventajas que describe el libro:

- **Aislamiento de recursos:** una operación costosa de un inquilino afecta menos a los demás si están en otros shards.
- **Aislamiento de permisos:** un fallo en el control de acceso tiene menos probabilidad de exponer datos de otro inquilino.
- **Arquitectura por celdas:** no solo los datos, también los servicios se agrupan en celdas autocontenidas; un fallo queda limitado a su celda.
- **Copia y restauración por inquilino:** puedes restaurar a un cliente que borró datos por error sin tocar a los demás.
- **Cumplimiento normativo:** exportar o borrar los datos personales que exigen normas como GDPR o CCPA se vuelve una operación sobre un shard.
- **Residencia de datos:** una base consciente de regiones puede colocar el shard de un inquilino en una jurisdicción concreta.
- **Migraciones graduales de esquema:** se aplican inquilino por inquilino y los fallos se detectan antes de afectar a todos.

Los límites: si un inquilino no cabe en una máquina, vuelves a necesitar sharding dentro de ese inquilino; si hay miles de inquilinos diminutos, un shard por cada uno cuesta demasiado y agruparlos obliga después a moverlos cuando crecen; y cualquier función que cruce inquilinos (informes globales, joins) se vuelve más difícil.

## El objetivo: carga pareja

Idealmente, 10 nodos guardan 10 veces más datos y atienden 10 veces más lecturas y escrituras que uno. Si el reparto es injusto hablamos de **sesgo** (*skew*); en el extremo, toda la carga cae en un shard y 9 de 10 nodos están ociosos. Un shard con carga desproporcionada es un **shard caliente** o *hot spot*; una clave concreta con carga enorme (una celebridad en una red social) es una **clave caliente** (*hot key*).

Para repartir hace falta un algoritmo que reciba la clave de partición y devuelva el shard. En un almacén clave-valor suele ser la clave o su primera parte; en un modelo relacional puede ser cualquier columna, no necesariamente la clave primaria. Ese algoritmo debe permitir **rebalancear** para aliviar los puntos calientes, tema de las notas 02 y 05.

> [!question]- ¿Por qué añadir réplicas no resuelve un exceso de escrituras?
> Porque cada réplica recibe y aplica todas las escrituras de su líder. Las réplicas multiplican la capacidad de lectura, no la de escritura; para repartir escrituras hay que dividir los datos en shards con líderes distintos.

> [!question]- ¿Un registro puede estar en varios nodos si pertenece a un solo shard?
> Sí. Pertenece a un solo shard, pero ese shard está replicado. En la figura 7-1 cada shard tiene tres copias en tres nodos distintos.

> [!question]- Una empresa con 40 GB de pedidos y 500 escrituras por segundo quiere fragmentar «por si acaso». ¿Qué le dirías?
> Que primero debe medir si una máquina maneja esos datos, consultas y latencias con margen: 40 GB y 500 escrituras/s no justifican por sí solos fragmentar. Fragmentar ahora añadiría la elección de clave de partición, consultas entre shards y transacciones distribuidas sin un beneficio real. Es mejor medir y reservar el sharding para cuando el volumen o las escrituras lo exijan.

## Referencias

PDF 1–6 · impresas 251–256 · figura 7-1: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=1|PDF 1 · impresa 251]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=2|PDF 2 · impresa 252 (figura 7-1 y terminología)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=3|PDF 3 · impresa 253 (pros y contras)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=4|PDF 4 · impresa 254 (una máquina y multiinquilino)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=5|PDF 5 · impresa 255 (retos multiinquilino y sesgo)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=6|PDF 6 · impresa 256 (hot spot y hot key)]]. Las páginas PDF 4 y 5 están escaneadas boca abajo.

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|Índice del capítulo]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/02 Particionado por rangos y hotspots|Particionado por rangos y hotspots →]]
