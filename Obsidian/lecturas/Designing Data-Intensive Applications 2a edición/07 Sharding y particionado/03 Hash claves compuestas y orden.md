---
title: "DDIA — Hash, claves compuestas y orden"
created: 2026-09-29
capitulo: 7
tags:
  - lecturas/ddia
  - arquitectura/sharding
---

# DDIA — Hash, claves compuestas y orden

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|↑ Índice del capítulo 7]]

El sharding por rangos agrupa claves cercanas, y eso es justo lo que provoca shards calientes cuando las escrituras llegan con claves cercanas. Si **no te importa** que claves parecidas vivan juntas (por ejemplo, identificadores de inquilino en una aplicación multiinquilino), la alternativa habitual es aplicar primero una **función hash** a la clave de partición y decidir el shard a partir del resultado.

## Qué debe hacer una función hash para sharding

Una buena función hash dispersa claves distintas de forma aproximadamente uniforme. No convierte una carga concentrada en una sola clave en carga uniforme: todas las peticiones sobre esa misma clave conservan el mismo hash. Con un hash de 32 bits, cualquier cadena produce un número entre 0 y 2³² − 1 (0 a 4.294.967.295) de aspecto aleatorio. Dos entradas casi idénticas, como `pedido-1000` y `pedido-1001`, suelen dar números sin cercanía predecible. Pueden caer en el mismo shard e incluso tener el mismo hash; una colisión no vuelve iguales las claves originales. Pero la misma entrada produce **siempre** el mismo número: si no, no podrías volver a encontrar el registro.

No hace falta que sea criptográfica. La edición menciona MD5 como ejemplo en MongoDB y Murmur3 en Cassandra y ScyllaDB; aquí se estudia la propiedad requerida, no se verifica la configuración vigente de esos productos. Lo que sí hace falta es **estabilidad entre procesos y máquinas**. El libro advierte que funciones incorporadas en lenguajes, como `Object.hashCode()` de Java o `Object#hash` de Ruby, pueden dar un valor distinto para la misma clave en procesos distintos. Sirven para tablas hash dentro de un proceso, pero si el nodo A y el nodo B calculan valores diferentes para la misma clave, cada uno buscaría el registro en un shard distinto.

## Del hash al shard

Una vez tienes el hash, falta decidir qué shard le toca. La idea ingenua, `hash(clave) % número_de_nodos`, es fácil de calcular pero obliga a mover casi todos los datos cuando cambia el número de nodos; el cálculo completo está en la [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/05 Rebalanceo fijo dinámico y proporcional|nota 05]]. Aquí interesa la otra opción que presenta el libro: **sharding por rango de hash**, que combina la división por rangos con la función hash. Cada shard ya no posee un rango de *claves*, sino un rango de *valores hash*.

### Cálculo con la figura 7-5

La figura usa un hash de 16 bits, con valores de 0 a 65.535 (2¹⁶ − 1). En la realidad suele ser de 32 bits o más. Con cuatro shards del mismo tamaño, cada uno cubre 65.536 / 4 = 16.384 valores:

| Shard | Rango de hash |
|---|---|
| 0 | 0 – 16.383 |
| 1 | 16.384 – 32.767 |
| 2 | 32.768 – 49.151 |
| 3 | 49.152 – 65.535 |

La figura aplica el hash a seis marcas de tiempo consecutivas, del 19 de diciembre de 2024 a las 17:08:10 hasta las 17:08:15. Comprobando cada valor contra la tabla:

| Clave | Hash | Shard |
|---|---|---|
| 17:08:10 | 7.372 | 0 |
| 17:08:11 | 18.805 | 1 |
| 17:08:12 | 50.537 | 3 |
| 17:08:13 | 31.579 | 1 (31.579 < 32.768) |
| 17:08:14 | 62.253 | 3 |
| 17:08:15 | 24.510 | 1 |

Las claves eran consecutivas y, sin embargo, acaban en shards distintos: el hash rompe la cercanía que causaba el shard caliente. Con solo seis claves, el shard 1 recibe tres y el shard 2 ninguna. La uniformidad del hash es **estadística**: se nota con miles o millones de claves, no con un puñado.

Igual que con rangos de claves, un shard por rango de hash se puede **dividir** cuando crece o se calienta. Sigue siendo costoso, pero ocurre cuando hace falta, así que el número de shards se adapta al volumen de datos. El libro atribuye este esquema a YugabyteDB y DynamoDB, y lo presenta como opción en MongoDB; Cassandra y ScyllaDB usan una variante con fronteras aleatorias (figura 7-6, [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/05 Rebalanceo fijo dinámico y proporcional|nota 05]]).

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-05-rangos-de-hash.png|1000]]

Las seis marcas de tiempo son consecutivas, pero los hashes originales del libro se dispersan por el espacio de 16 bits: de 0 a 65.535. Cada flecha termina en el shard dueño del intervalo que contiene su hash. El shard 2 no recibe ninguna de estas seis claves: una distribución útil a gran escala no exige que cada muestra pequeña use todos los shards.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=11|PDF 11 · impresa 261 · figura 7-5]].

## Lo que se pierde: el orden

El hash **destruye el orden** de las claves de partición. Una consulta «pedidos entre el 1 y el 7 de marzo» sobre la clave de partición ya no es un rango contiguo: esas claves están esparcidas por todos los shards, así que hay que preguntar a todos.

## Claves compuestas: lo mejor de ambos

El libro señala una salida: si la clave tiene **dos o más columnas** y la clave de partición es **solo la primera**, puedes hacer consultas de rango eficientes sobre la segunda y siguientes columnas, siempre que todos los registros consultados compartan la misma clave de partición. La primera parte decide el shard (vía hash); el resto decide el **orden dentro** del shard.

**Ejemplo propio con pedidos.** Clave `(cliente_id, fecha_pedido, pedido_id)`, con `cliente_id` como clave de partición:

- «Pedidos del cliente 42 en marzo»: hash de 42 → un único shard → escaneo desde `(42, 2026-03-01)` incluido hasta `(42, 2026-04-01)` excluido. Así se incluye todo el último día de marzo, aunque `fecha_pedido` contenga hora. Rápido y ordenado.
- «Últimos 10 pedidos del cliente 42»: mismo shard, leer el final del rango.
- «Todos los pedidos de marzo, de cualquier cliente»: la fecha no es clave de partición; hay que consultar todos los shards.

Este patrón es el que popularizó el modelo de Cassandra, donde la clave primaria se compone de una clave de partición y de columnas de agrupamiento (*clustering columns*) que ordenan las filas dentro de la partición. El texto de la segunda edición describe el patrón de forma general sin atarlo a Cassandra en este punto; el nombre de las columnas de agrupamiento es elaboración propia.

Un límite importante: una clave compuesta **no arregla una clave caliente**. Si el cliente 42 es un mayorista que genera la mitad de los pedidos, todos sus pedidos siguen yendo al mismo shard, porque el hash de 42 siempre es el mismo.

## El mismo patrón en almacenes de datos

El recuadro del libro sobre almacenes de datos muestra la idea con otros nombres. En BigQuery, la clave de partición decide en qué partición vive un registro y las *cluster columns* deciden cómo se ordena dentro. Snowflake asigna registros a *micro-partitions* automáticamente pero permite definir *cluster keys*. Delta Lake admite particiones manuales y automáticas y claves de agrupamiento. Agrupar bien mejora los escaneos por rango y, además, la compresión y el filtrado, porque datos parecidos quedan juntos.

## Comparación rápida

| Esquema | Reparte escrituras de claves cercanas | Rango sobre la clave de partición | Rango dentro de una partición |
|---|---|---|---|
| Rango de claves | Puede concentrar escrituras recientes en un rango | Sí, eficiente | Sí |
| Rango de hash | Dispersa claves distintas; una clave caliente permanece junta | No: hay que consultar todos los shards | Solo con clave compuesta y orden local apropiado |
| Hash + clave compuesta | Depende de la diversidad y carga de la primera columna | No | Sí, sobre las columnas siguientes con el mismo prefijo |

> [!question]- ¿Por qué no puedes usar el `hashCode()` de un objeto Java como función de sharding?
> Porque para la misma clave puede producir valores distintos en procesos distintos. Si dos nodos o dos clientes calculan hashes diferentes, cada uno enviaría la petición a un shard diferente y no encontrarían el registro. Hace falta una función estable, aunque no sea criptográfica.

> [!question]- Con clave `(cliente_id, fecha)` y hash sobre `cliente_id`, ¿cuántos shards consulta «pedidos del cliente 7 entre dos fechas»?
> Uno solo. Todos los pedidos del cliente 7 tienen la misma clave de partición, así que están en el mismo shard, ordenados por fecha. La consulta es un escaneo de rango local.

> [!question]- En la figura 7-5, el shard 2 no recibe ninguna de las seis claves. ¿Es un fallo del hash?
> No. Seis claves son muy pocas para observar uniformidad. El hash reparte bien en promedio; con miles de claves cada shard recibiría una cuarta parte aproximada.

## Referencias

PDF 8 · impresa 258 (funciones hash), PDF 11–12 · impresas 261–262 (rango de hash, figura 7-5, claves compuestas, recuadro de almacenes): [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=8|PDF 8 · impresa 258]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=11|PDF 11 · impresa 261 (figura 7-5)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=12|PDF 12 · impresa 262 (almacenes de datos)]]. Resumen de la idea en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=22|PDF 22 · impresa 272]].

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/02 Particionado por rangos y hotspots|← Particionado por rangos y hotspots]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/04 Índices secundarios locales y globales|Índices secundarios locales y globales →]]
