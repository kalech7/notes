---
title: "DDIA — Índices secundarios locales y globales"
created: 2026-09-29
capitulo: 7
tags:
  - lecturas/ddia
  - arquitectura/sharding
---

# DDIA — Índices secundarios locales y globales

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|↑ Índice del capítulo 7]]

Todo lo visto hasta ahora supone que el cliente **conoce la clave de partición** del registro que quiere. Con ella calcula el shard y va directo. Pero muchas consultas buscan por otra cosa: «todos los pedidos en estado *pendiente*», «todos los coches rojos», «todos los artículos que contienen la palabra *hogwash*». Un **índice secundario** es una estructura de acceso por un atributo distinto de la clave de reparto. Puede devolver muchos registros con cierto valor, como el color, o identificar uno solo si el atributo es único, como un número de seguimiento.

Los almacenes clave-valor a menudo no tienen índices secundarios, pero son estándar en bases relacionales, comunes en bases documentales y la razón de ser de motores de búsqueda como Solr y Elasticsearch. El problema es que **no encajan de forma natural con los shards**: los registros se reparten por la clave de partición y el índice habla de otro atributo. Hay dos respuestas: índices **locales** e índices **globales**.

## Índices locales (particionados por documento)

Cada shard mantiene **su propio** índice secundario, que solo cubre los registros de ese shard. No sabe nada de los demás. En recuperación de información se llama **índice particionado por documento** (*document-partitioned*).

La figura 7-9 del libro usa un sitio de coches usados particionado por ID de anuncio: IDs 0–499 en el shard 0 y 500–999 en el shard 1. El shard 0 guarda los coches 191 (rojo, Honda), 214 (negro, Dodge) y 306 (rojo, Ford), y su índice local dice `color:red → [191, 306]`. El shard 1 guarda 515 (plateado, Ford), 768 (rojo, Volvo) y 893 (plateado, Audi), y su índice dice `color:red → [768]`. La lista de IDs asociada a un valor se llama **lista de apariciones** (*postings list*), como en el capítulo 4. Quien busca «un coche rojo» tiene que leer de los dos shards.

**Escribir es sencillo:** añadir, cambiar o borrar un registro solo toca el shard que lo contiene, y ese shard actualiza su propio índice en la misma operación local.

**Leer es lo caro:**

- Si ya conoces la clave de partición, consultas solo el shard adecuado.
- Si solo quieres *algunos* resultados sin exigir un orden global (por ejemplo, «muéstrame hasta 20 coches rojos»), puedes empezar por un shard. Si allí no hay suficientes, consultas más. Para los 20 más baratos de toda la base hace falta considerar los candidatos de todos los shards.
- Si quieres **todos** los resultados y no conoces su clave de partición, tienes que enviar la consulta a **todos los shards** y combinar las respuestas. Este patrón se conoce como *scatter/gather* (dispersar y reunir); la segunda edición lo describe sin usar ese nombre, que sí aparecía en la primera.

El libro señala dos consecuencias. Primera, aunque consultes los shards en paralelo, sufres **amplificación de la latencia de cola**: la respuesta llega cuando contesta el shard más lento. Segunda, añadir shards te deja guardar más datos, pero **no aumenta automáticamente el número de consultas por segundo** si cada shard tiene que participar en cada consulta. Dividir reduce los datos que procesa cada uno, pero no reduce cuántas consultas recibe; la ganancia depende de qué costo domine.

**Cálculo de latencia de cola (propio).** Supón que cada shard responde por encima de 200 ms en el 1 % de los casos (su percentil 99 es 200 ms). Una consulta que espera a 20 shards independientes solo es rápida si los 20 son rápidos: 0,99²⁰ ≈ 0,818. Así que ≈ 18,2 % de las consultas tardan más de 200 ms. Con 100 shards: 0,99¹⁰⁰ ≈ 0,366, y ≈ 63,4 % de las consultas son lentas. Lo que era raro en un shard se vuelve habitual en la consulta completa.

Aun así, los índices locales están muy extendidos: el libro cita MongoDB, Riak, Cassandra, Elasticsearch, SolrCloud y VoltDB.

> [!warning] No construyas tu propio índice secundario a la ligera
> Si tu base solo ofrece clave-valor, es tentador mantener en la aplicación un mapa «valor → IDs». El libro advierte que las condiciones de carrera y los fallos parciales (se guarda el registro pero no la entrada del índice, o al revés) desincronizan fácilmente el índice de los datos. Es el problema que motiva las transacciones de varios objetos del capítulo 8.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-09-indices-locales-autos.png|1000]]

Los datos se reparten por ID y cada índice local contiene únicamente los IDs del shard donde reside. color:red devuelve 191 y 306 en el shard 0, y 768 en el shard 1. La consulta por color necesita buscar en ambos y combinar los resultados porque no conoce los IDs de antemano. Las seis filas y las listas de IDs conservan el ejemplo del libro; los colores mantienen sus términos originales en inglés.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=19|PDF 19 · impresa 269 · figura 7-9]].

## Índices globales (particionados por término)

En lugar de un índice por shard, se construye **un índice que cubre todos los datos**. Para mantener la capacidad de escalar no conviene concentrarlo en un solo nodo, que podría convertirse en cuello de botella. En el diseño del capítulo el índice global **también se fragmenta**, pero con una regla distinta a la de los datos: se particiona **por el valor indexado**. Por eso se llama **particionado por término** (*term-partitioned*). En búsqueda de texto un término es una palabra; aquí se generaliza a cualquier valor buscable.

En la figura 7-10, los colores que empiezan de la *a* a la *r* van al shard 0 del índice y los de la *s* a la *z* al shard 1. Así, `color:red → [191, 306, 768]` está entero en el shard 0, aunque el coche 768 viva en el shard 1; `color:silver → [515, 893]` está en el shard 1. El índice de marca se parte entre la *f* y la *h* según las iniciales inglesas de la figura: `make:Audi`, `make:Dodge` y `make:Ford → [306, 515]` en el shard 0; `make:Honda` y `make:Volvo` en el shard 1. Los términos pueden repartirse por rangos, como aquí, o por el hash del término.

**Lecturas de una condición:** «color = rojo» solo necesita leer **un** shard del índice para obtener la lista de IDs. Pero si quieres los registros y no solo los IDs, todavía tienes que ir a los shards donde viven esos registros, que pueden ser todos.

**Varias condiciones:** «rojo **y** Ford» o «estas dos palabras en el mismo texto» usan términos que probablemente estén en shards distintos. Para calcular la intersección hay que juntar las dos listas. Si son cortas, no hay problema; si son largas, enviarlas por la red es lento.

**Ejemplo propio de intersección.** «estado = pendiente» tiene 2.000.000 de IDs y «ciudad = Lima» 500.000, en shards distintos del índice. Con IDs de 8 bytes, mover la lista más corta al shard de la otra supone 500.000 × 8 = 4 MB; mover ambas a un coordinador, 2.500.000 × 8 = 20 MB. Todo eso para una sola consulta, antes de leer ningún pedido.

**Escrituras más complicadas:** un solo registro puede afectar a varios shards del índice, porque cada término del registro puede vivir en uno diferente. Cambiar un pedido de `pendiente` a `enviado` implica escribir el pedido en su shard, **quitar** su ID de la lista de `pendiente` y **añadirlo** a la de `enviado`, que pueden estar en otros dos shards. Mantenerlo sincronizado es más difícil. Una opción es una **transacción distribuida** que actualice atómicamente el registro y sus entradas de índice (capítulo 8).

### El riesgo de actualizar el índice de forma asíncrona

El libro indica que CockroachDB, TiDB y YugabyteDB usan índices globales, y que DynamoDB ofrece locales y globales. En DynamoDB, según el libro, las escrituras se reflejan **de forma asíncrona** en los índices globales, así que una lectura del índice puede devolver datos **desactualizados**, igual que el retraso de replicación del capítulo 6.

**Consecuencia en pedidos (propia):** un cliente paga, el pedido pasa a `pagado` y la aplicación lo redirige a «Mis pedidos pagados», que consulta el índice global por estado. Si el índice aún no se ha actualizado, el pedido no aparece o sigue listado como pendiente. Y un proceso que lea «pendientes» del índice para cancelarlos por caducidad podría cancelar un pedido ya pagado si no vuelve a comprobar el registro principal antes de actuar. La comprobación y la cancelación deben quedar protegidas como una decisión atómica, por ejemplo «cancela solo si sigue pendiente»: una lectura seguida de una escritura incondicional aún puede correr contra un pago que entra entre ambas.

El libro concluye que los índices globales convienen cuando **las lecturas superan a las escrituras** y las listas de apariciones **no son demasiado largas**.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-10-indice-global-autos.png|1000]]

Los registros siguen distribuidos por ID, pero el índice global se reparte por el término indexado. La lista color:red del shard 0 reúne 191, 306 y 768, aunque 768 vive en el shard 1 de datos. Una consulta al índice obtiene todos esos IDs; recuperar los automóviles completos todavía requiere consultar sus shards de datos. Las flechas discontinuas muestran que los registros 768 y 893 del shard 1 alimentan entradas del índice global del shard 0. Los colores mantienen sus nombres originales en inglés para conservar los rangos a–r y s–z de la figura del libro.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=20|PDF 20 · impresa 270 · figura 7-10]].

## Comparación

| Aspecto | Índice local (por documento) | Índice global (por término) |
|---|---|---|
| Dónde vive | Junto a los datos de cada shard | Fragmentado por el valor indexado |
| Escritura de un registro | Un solo shard | Shard de datos + posiblemente varios del índice |
| Lectura «todos con valor X» | Todos los shards (*scatter/gather*) | Un shard para los IDs; luego los shards de los registros |
| Consistencia índice-datos | Local, más sencilla | Necesita transacción distribuida o acepta retraso |
| Ejemplos que cita el libro | MongoDB, Riak, Cassandra, Elasticsearch, SolrCloud, VoltDB | CockroachDB, TiDB, YugabyteDB; DynamoDB ambos |

> [!question]- ¿Por qué añadir shards no mejora el rendimiento de una consulta por índice local?
> Porque la consulta tiene que ejecutarse en todos los shards. Con más shards cada uno guarda menos datos, pero todos siguen procesando todas las consultas por ese índice, así que aumentar shards no multiplica automáticamente las consultas por segundo. Puede bajar el trabajo de cada escaneo, pero todos siguen recibiendo el mismo número de consultas y la respuesta depende del más lento.

> [!question]- Con índice global, ¿cuántos shards toca «color = rojo» si además quieres los documentos completos?
> Un shard del índice para obtener `[191, 306, 768]` y luego los shards de datos que contienen esos IDs: en la figura, el shard 0 (191 y 306) y el shard 1 (768).

> [!question]- ¿Qué riesgo concreto introduce un índice global asíncrono?
> Que una lectura por el índice devuelva un estado antiguo. Si la aplicación toma decisiones solo con el índice, puede mostrar o procesar registros con valores ya cambiados. Hay que tolerarlo o verificar contra el registro principal.

## Referencias

PDF 18–21 · impresas 268–271 · figuras 7-9 y 7-10: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=18|PDF 18 · impresa 268]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=19|PDF 19 · impresa 269 (figura 7-9 y advertencia)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=20|PDF 20 · impresa 270 (figura 7-10)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=21|PDF 21 · impresa 271 (intersección, escrituras, DynamoDB)]].

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/03 Hash claves compuestas y orden|← Hash, claves compuestas y orden]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/05 Rebalanceo fijo dinámico y proporcional|Rebalanceo fijo, dinámico y proporcional →]]
