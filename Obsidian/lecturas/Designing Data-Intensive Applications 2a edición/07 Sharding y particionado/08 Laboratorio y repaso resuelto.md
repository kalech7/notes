---
title: "DDIA — Laboratorio y repaso resuelto del capítulo 7"
created: 2026-09-29
capitulo: 7
tags:
  - lecturas/ddia
  - arquitectura/sharding
---

# DDIA — Laboratorio y repaso resuelto del capítulo 7

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|↑ Índice del capítulo 7]]

Los ejercicios usan la plataforma de pedidos de las notas anteriores. Intenta resolver cada uno antes de abrir la respuesta. Los datos numéricos son propios salvo cuando se indica que vienen de una figura del libro.


## Laboratorio ejecutable: comprobar las asignaciones

El script [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/Laboratorios/07 sharding.py|07 sharding.py]] usa únicamente Python estándar. Ejecuta `python3 "07 sharding.py"` desde su carpeta. Es una simulación determinista de asignaciones, sin base de datos, red ni migración real.

Reproduce cinco comprobaciones: claves 0–23 con módulo 3 y 4; los veinte shards de la figura 7-4; los seis hashes de 16 bits de la figura 7-5; los intervalos de la figura 7-6; y las listas locales y globales de coches rojos. La salida comprueba que se mueven 18 de 24 claves con módulo, que basta mover cuatro shards fijos, y que el nodo nuevo de la figura 7-6 recibe 182 de 1.024 unidades del espacio de hash. No son 182 pedidos ni una medición de tráfico.

Los `assert` hacen visibles discrepancias entre el cálculo y la asignación. La última parte demuestra que un shard del índice global puede devolver los IDs 191, 306 y 768 mientras los registros siguen repartidos en dos shards de datos. El laboratorio fue ejecutado y todas las comprobaciones pasaron.


## Bloque A · Cálculos de reparto

> [!question]- A1. Un nodo aguanta 6.000 escrituras/s. El pico es de 45.000 escrituras/s y quieres operar al 75 % como máximo. ¿Cuántos shards de escritura necesitas como mínimo?
> Capacidad útil por nodo: 0,75 × 6.000 = 4.500. Shards: 45.000 / 4.500 = 10. Necesitas al menos 10 shards con líderes en nodos distintos, **suponiendo reparto uniforme**. Si hay sesgo, 10 no bastan: el shard más cargado es el que satura primero.

> [!question]- A2. Con un hash de 16 bits y 8 shards iguales por rango de hash, ¿qué rango cubre el shard 5 y a qué shard va el hash 41.000?
> Cada shard cubre 65.536 / 8 = 8.192 valores. El shard 5 va de 5 × 8.192 = 40.960 a 6 × 8.192 − 1 = 49.151. El hash 41.000 está en ese intervalo: shard 5.

> [!question]- A3. En la figura 7-5 (cuatro shards de 16.384 valores), ¿a qué shard va cada hash: 7.372, 31.579 y 50.537?
> 7.372 < 16.384 → shard 0. 31.579 está entre 16.384 y 32.767 → shard 1. 50.537 ≥ 49.152 → shard 3.

## Bloque B · Rebalanceo

> [!question]- B1. Con `hash % N`, ¿qué fracción de claves se mueve al pasar de 5 a 6 nodos? ¿Cuánto sería lo ideal?
> Una clave se queda si `h % 5 == h % 6`. El patrón se repite cada 30 valores (mcm de 5 y 6) y solo se cumple para 0–4: se quedan 5/30 ≈ 16,7 % y se mueve ≈ 83,3 %. Lo ideal es mover solo la parte del nodo nuevo, 1/6 ≈ 16,7 %. La fórmula mueve exactamente lo contrario de lo que debería.

> [!question]- B2. Tienes 600 shards fijos en 12 nodos y añades 3 nodos. ¿Cuántos shards recibe cada nodo nuevo y qué fracción de datos se mueve?
> Antes: 600 / 12 = 50 por nodo. Después: 600 / 15 = 40 por nodo. Cada nodo antiguo cede 10 shards (12 × 10 = 120) y cada nodo nuevo recibe 40 (3 × 40 = 120). Se mueve 120 / 600 = 20 % de los shards y, si tienen tamaños parecidos, aproximadamente ese porcentaje de datos, justo la fracción que corresponde a los 3 nodos nuevos (3/15).

> [!question]- B3. Con esos 600 shards, el negocio crece hasta necesitar 700 nodos. ¿Qué ocurre?
> No se pueden aprovechar 700 dueños de escritura independientes con solo 600 shards. Sí podrían existir máquinas adicionales como réplicas, pero no crearían nuevas unidades de reparto de escritura. Habría que hacer un resharding, que divide cada shard y lo reescribe, consume mucho disco extra y en algunos sistemas exige detener escrituras.

> [!question]- B4. Con 1.000 shards fijos, los datos pasan de 200 GB a 80 TB. ¿Cómo cambia el tamaño de cada shard y por qué importa?
> De 200 GB / 1.000 = 200 MB a 80.000 GB / 1.000 = 80 GB. Shards de 80 GB hacen caro cada movimiento y cada recuperación tras un fallo. El número fijo acertaba al principio y deja de acertar cuando el volumen varía mucho.

> [!question]- B5. Un sistema divide un shard al llegar a 10 GB, en dos mitades de unos 5 GB. Con 3 TB de datos repartidos por divisiones, ¿entre cuántos shards esperarías?
> En el modelo ideal del ejercicio, suponiendo mitades equilibradas, sin borrados ni shards recién creados diminutos, cada shard mide entre 5 y 10 GB: 3.000 / 10 = 300 como mínimo y 3.000 / 5 = 600 como máximo. El número de shards se adapta al volumen, a diferencia del esquema fijo.

> [!question]- B6. Con la figura 7-6 (espacio 0–1024), ¿qué fracción poseía el nodo 1 antes de añadir el nodo 3, y cuánto recibe el nodo 3?
> Nodo 1: 0–88, 511–672 y 702–930 → 88 + 161 + 228 = 477, un 46,6 %. El nodo 3 recibe 60–88, 276–309 y 551–672 → 28 + 33 + 121 = 182, un 17,8 %. Con solo 3 rangos aleatorios por nodo el reparto es desigual; por eso los sistemas reales usan muchos más rangos por nodo.

## Bloque C · Puntos calientes

> [!question]- C1. Clave `fecha_hora` por rangos mensuales y 12 shards. ¿Qué fracción de las escrituras nuevas recibe el shard del mes actual?
> Prácticamente el 100 %: todas las inserciones llevan fecha actual. Los otros 11 shards solo reciben lecturas de datos antiguos. La solución del libro es anteponer otro campo, por ejemplo `(tienda_id, fecha_hora)`, y repartir sus prefijos entre rangos distintos. El ejemplo supone inserciones con fecha actual; correcciones y cargas históricas pueden escribir en otros meses.

> [!question]- C2. Salas la clave `PROD-9` con 3 dígitos aleatorios. Recibe 90.000 incrementos/s. ¿Cuántas escrituras por subclave, y cuántas lecturas cuesta obtener el total?
> Tres dígitos dan 1.000 subclaves: 90.000 / 1.000 = 90 escrituras/s por subclave de media. Leer el total exige leer las 1.000 subclaves y sumarlas. Más dígitos reparten mejor la escritura pero encarecen cada lectura.

> [!question]- C3. ¿Por qué no salar todas las claves por defecto?
> Porque la inmensa mayoría tienen poca carga y pagarían lecturas multiplicadas sin beneficio. El libro recomienda salar solo las pocas claves calientes y mantener un registro de cuáles están divididas.

## Bloque D · Índices secundarios

> [!question]- D1. Índice local, 50 shards, cada uno con 1 % de probabilidad de responder por encima de 150 ms. ¿Qué fracción de consultas *scatter/gather* supera 150 ms?
> Suponiendo respuestas independientes, la consulta es rápida solo si los 50 responden rápido: 0,99⁵⁰ ≈ 0,605. Supera 150 ms ≈ 39,5 % de las consultas.

> [!question]- D2. Índice global por término, particionado por rangos: estados de la *a* a la *m* en el shard A y de la *n* a la *z* en el shard B. Un pedido pasa de `pagado` a `enviado`. ¿Qué shards del índice se escriben?
> Hay que quitar el ID de la lista `pagado` (empieza por *p*, shard B) y añadirlo a `enviado` (empieza por *e*, shard A). Dos shards del índice más el shard del pedido: tres escrituras en lugares distintos, que necesitan transacción distribuida o aceptar un índice temporalmente desfasado.

> [!question]- D3. Consulta «estado = pendiente Y ciudad = Cusco» con índice global. Pendiente tiene 3 millones de IDs y Cusco 40.000, en shards distintos. ¿Qué lista conviene mover y cuánto pesa con IDs de 8 bytes?
> La corta: 40.000 × 8 = 320.000 bytes ≈ 0,32 MB, enviada al shard que tiene la lista de pendientes para intersecar allí. Mover la larga costaría 24 MB. Cuando ambas listas son largas, la intersección por red se vuelve lenta, que es el límite que señala el libro.

## Bloque E · Enrutamiento y operación

> [!question]- E1. Enfoque «cualquier nodo reenvía» con 8 nodos y elección aleatoria. ¿Qué fracción de peticiones necesita un salto extra?
> La petición llega al dueño con probabilidad 1/8; en los otros 7/8 = 87,5 % de los casos hace falta reenviar (considerando una sola réplica por shard; con réplicas que también pueden atender, la fracción baja).

> [!question]- E2. Tras mover un shard, un cliente con tabla antigua escribe en el nodo viejo. ¿Qué comportamiento es seguro?
> Que el nodo viejo rechace (o reenvíe) porque ya no es dueño, y que el cliente refresque la asignación desde el servicio de coordinación antes de reintentar. Lo peligroso es que dos nodos acepten escrituras para el mismo shard a la vez.

> [!question]- E3. Un nodo va lento por un pico y el sistema, que rebalancea solo, lo declara caído. Describe la secuencia de riesgo.
> Los demás nodos reciben su carga y además el tráfico de copia de datos; se ralentizan, se les declara caídos a su vez y el problema se propaga: un fallo en cascada. Por eso el libro valora tener un humano en el ciclo.

## Bloque F · Verdadero o falso

> [!question]- F1. «Hashing consistente significa que todas las réplicas ven los mismos datos.»
> Falso. Significa que, al cambiar el número de shards, se mueve el mínimo de claves y cada shard recibe aproximadamente las mismas. No tiene relación con la consistencia de réplicas ni con ACID.

> [!question]- F2. «En PostgreSQL, *partitioning* y *sharding* son lo mismo.»
> Falso. En PostgreSQL, particionar divide una tabla en varios archivos dentro de la misma máquina; fragmentar reparte entre máquinas.

> [!question]- F3. «Un índice global permite leer los registros completos de `color = rojo` consultando un solo shard.»
> Falso. Un solo shard del índice da la lista de IDs, pero los registros viven en sus shards de datos, que pueden ser todos.

> [!question]- F4. «Riak usa gossip y por eso nunca tiene cerebro dividido.»
> Falso. El gossip ofrece consistencia más débil que el consenso y admite cerebro dividido; Riak lo tolera por ser una base sin líder con garantías débiles.

## Autoevaluación final

Deberías poder explicar sin mirar: por qué `hash % N` mueve casi todo; cuándo un rango ordenado es preferible a un hash; cómo una clave compuesta recupera consultas por rango; qué cuesta cada tipo de índice secundario en escritura y lectura; qué problemas resuelve un servicio de coordinación; y por qué las escrituras entre shards quedan pendientes para el capítulo 8.

## Referencias

Cálculos basados en las figuras 7-3 (PDF 9 · impresa 259), 7-4 (PDF 10 · impresa 260), 7-5 (PDF 11 · impresa 261), 7-6 (PDF 12 · impresa 262), 7-9 y 7-10 (PDF 19–20 · impresas 269–270): [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=9|PDF 9 · impresa 259]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=11|PDF 11 · impresa 261]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=12|PDF 12 · impresa 262]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=20|PDF 20 · impresa 270]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=22|PDF 22 · impresa 272]].

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/07 Diseño integrado y decisiones|← Diseño integrado y decisiones]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|Índice del capítulo 7 →]]
