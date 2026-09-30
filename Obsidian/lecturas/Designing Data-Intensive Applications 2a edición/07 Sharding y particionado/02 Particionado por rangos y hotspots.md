---
title: "DDIA — Particionado por rangos y puntos calientes"
created: 2026-09-29
capitulo: 7
tags:
  - lecturas/ddia
  - arquitectura/sharding
---

# DDIA — Particionado por rangos y puntos calientes

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|↑ Índice del capítulo 7]]

El **sharding por rango de claves** asigna a cada shard un intervalo continuo de claves de partición, desde un mínimo hasta un máximo. Es la misma lógica que una enciclopedia de papel: si buscas «Danubio», miras los lomos y tomas el tomo cuyo rango incluye esa palabra. Saber en qué shard está una clave es inmediato si conoces las fronteras.

## Las fronteras se adaptan a los datos, no al alfabeto

La figura 7-2 muestra doce tomos. El primero va de «A-ak» a «Bayes» y cubre dos letras; el tomo 12 empieza en «Trudeau» y llega hasta «Zywiec», es decir, cubre el final de la T y todas las letras de la U a la Z. Los rangos son desiguales porque las palabras no se reparten por igual entre letras. Si cada tomo tuviera exactamente dos letras, unos serían gruesísimos y otros casi vacíos.

La consecuencia para una base de datos: las fronteras deben elegirse **mirando la distribución real de los datos**. Puede hacerlo un administrador o el propio sistema:

| Cómo se eligen las fronteras | Ejemplos que cita el libro |
|---|---|
| Manualmente | Vitess (capa de sharding sobre MySQL) |
| Automáticamente | Bigtable, HBase, la opción por rangos de MongoDB, CockroachDB, RethinkDB, FoundationDB |
| Ambas | YugabyteDB (división de *tablets* manual y automática) |

Estas atribuciones describen lo que el libro presenta como ejemplos; no son una comparación actual de productos.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 07/07-02-rangos-enciclopedia.png|1000]]

Los doce volúmenes reproducen los límites alfabéticos de la figura del libro. Cada entrada pertenece al volumen cuyo rango contiene su título: no hace falta mirar todos los volúmenes. Los rangos no abarcan la misma cantidad de letras; la distribución de títulos determina dónde conviene colocar sus fronteras.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=6|PDF 6 · impresa 256 · figura 7-2]].

## La gran ventaja: orden y escaneos por rango

En el modelo del capítulo, dentro de cada shard las claves se guardan **ordenadas**, por ejemplo en un B-tree o en SSTables (capítulo 4). Eso permite:

1. **Escaneos por rango** baratos: «todas las claves entre X e Y» se leen de forma contigua.
2. Usar la clave como **índice concatenado**: si la clave tiene varias partes, puedes traer registros relacionados en una sola consulta.

El ejemplo del libro es una red de sensores cuya clave es la marca de tiempo de la medición: pedir «todas las lecturas de marzo» es un solo escaneo.

## El precio: escrituras que se amontonan

Si la clave es una marca de tiempo, cada shard corresponde a un intervalo de tiempo, por ejemplo un mes. Todas las mediciones nuevas tienen marcas de tiempo *actuales*, así que todas las escrituras caen en el shard del mes en curso. Ese shard se sobrecarga mientras los demás esperan sin trabajo. Es el caso de manual de **shard caliente**.

**Ejemplo propio con pedidos.** Supón que la clave de la tabla `pedidos` es `fecha_hora_creación` y hay 12 shards, uno por mes. Con 20.000 pedidos por minuto, el shard de este mes recibe los 20.000; los otros 11 reciben 0. Tener 12 máquinas no multiplica la capacidad de escritura: la multiplica por 1.

La solución que propone el libro es **no poner el tiempo en primer lugar**. Si antepones el identificador del sensor (o, en nuestro caso, de la tienda), la clave queda ordenada primero por tienda y luego por fecha: `(tienda_id, fecha_hora)`. Con muchas tiendas activas a la vez y fronteras de shard que separen sus prefijos, las escrituras pueden repartirse entre muchos rangos. Cambiar el orden de la clave no mueve los datos por sí solo: la asignación de rangos también debe aprovechar esa diversidad.

El coste aparece en la lectura: «todos los pedidos de ayer de todas las tiendas» ya no es un rango contiguo. Hay que hacer **una consulta de rango por tienda**. Con 500 tiendas son 500 escaneos pequeños, que el sistema puede lanzar en paralelo pero que ya no son una sola operación.

Un límite que conviene añadir (elaboración propia): anteponer un prefijo solo reparte si el prefijo tiene **muchos valores con carga parecida**. Si tres tiendas generan el 80 % de los pedidos, sus rangos seguirán calientes.

## Crecimiento del rango: una vista previa

Al crear la base no hay datos ni, por tanto, rangos que dividir. Algunos sistemas (HBase, MongoDB) permiten **pre-dividir** (*pre-splitting*) una base vacía en varios shards, siempre que ya intuyas la distribución de claves. Después, cuando un shard crece o recibe demasiadas escrituras, se divide en dos subrangos; si se borra mucho, se pueden fusionar shards vecinos. El detalle, con sus costes, está en la [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/05 Rebalanceo fijo dinámico y proporcional|nota 05]].

## Sesgo de carga: cuando el problema es una sola clave

Ninguna forma de repartir claves garantiza que la **carga** quede repartida. Aunque cada shard tenga el mismo número de claves, algunas claves pueden recibir muchas más peticiones o guardar muchos más datos. El ejemplo del libro: una publicación de una celebridad con millones de seguidores provoca una tormenta de lecturas y escrituras sobre la misma clave (el ID de la celebridad o de la publicación).

El libro describe varias respuestas:

- **Aislar la clave caliente.** Si los shards se definen por rangos (de claves o de hashes), puedes crear un shard que contenga solo esa clave e incluso asignarle una máquina dedicada.
- **Compensar en la aplicación («salar» la clave).** Añades un número aleatorio al principio o al final de la clave. Con dos dígitos aleatorios, las escrituras a una clave se reparten entre 100 claves distintas, que pueden ir a shards distintos. En un esquema por rangos, sufijos cercanos podrían seguir juntos: el reparto efectivo exige hash o fronteras que separen las subclaves.
- **Automatización en la nube.** Algunos servicios detectan y alivian shards calientes solos; Amazon lo llama *heat management* o *adaptive capacity*. El libro no entra en su funcionamiento.

### Salar una clave: cálculo y consecuencias

**Ejemplo propio.** En una venta relámpago, el contador de unidades vendidas del producto `PROD-777` recibe 20.000 incrementos por segundo. Un shard aguanta 3.000.

1. Sin salar: 20.000 escrituras/s sobre una clave → un solo shard → saturado (20.000 > 3.000).
2. Con dos dígitos aleatorios: claves `PROD-777#00` … `PROD-777#99`, cada una con 20.000 / 100 = 200 escrituras/s de media.
3. Si esas 100 claves se reparten entre 10 shards, cada shard recibe unas 10 subclaves × 200 = 2.000 escrituras/s, por debajo de 3.000.
4. Para leer el total vendido hay que leer las 100 subclaves y sumarlas.

Este ejemplo reparte el registro de incrementos, no la decisión de aceptar una venta. Si además existe un máximo de stock, comprobar por separado cada subcontador no evita sobreventas; necesitas coordinación o cuotas de venta previamente asignadas. Es una distinción propia que conecta el capítulo con los invariantes del capítulo 6.

Esto revela los límites que remarca el libro:

- **Solo se reparte la escritura.** Cada lectura del total ahora cuesta 100 lecturas, y el volumen de lecturas que llega a cada shard de la clave caliente no baja.
- **Hay que llevar la cuenta** de qué claves están saladas. Salar todas las claves añadiría sobrecoste a la inmensa mayoría, que tienen poca carga; necesitas un registro de claves divididas y un proceso para convertir una clave normal en clave especial.
- **La carga cambia con el tiempo.** Una publicación viral puede estar caliente dos días y luego enfriarse; tu mecanismo tiene que activarse y desactivarse.
- **Caliente para leer no es lo mismo que caliente para escribir.** Salar este contador ayuda con escrituras; una clave caliente en lecturas pide otras estrategias (por ejemplo cachés o más réplicas, elaboración propia).

> [!question]- ¿Por qué `(tienda_id, fecha_hora)` reparte mejor las escrituras que `fecha_hora` sola?
> Porque las escrituras nuevas tienen todas una fecha reciente, pero sus `tienda_id` son muchos y distintos. Al ordenar primero por tienda, las inserciones del mismo instante caen en rangos diferentes. A cambio, una consulta por intervalo de tiempo que abarque todas las tiendas necesita una consulta de rango por tienda.

> [!question]- Salaste una clave con 100 sufijos y las lecturas siguen lentas. ¿Qué ha pasado?
> Salar reparte las escrituras, no las lecturas. Cada lectura del valor completo tiene que consultar las 100 subclaves y combinarlas, así que el trabajo por lectura aumenta. Si la clave es caliente en lecturas, hace falta otra técnica.

> [!question]- ¿Un buen reparto de claves entre shards garantiza que no haya hot spots?
> No. El reparto uniforme de claves no implica reparto uniforme de peticiones. Una sola clave muy popular concentra la carga en su shard aunque todos los shards tengan el mismo número de claves.

## Referencias

PDF 6–8 · impresas 256–258 · figura 7-2 (rangos) y PDF 13–14 · impresas 263–264 (sesgo): [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=6|PDF 6 · impresa 256 (figura 7-2)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=7|PDF 7 · impresa 257 (orden, sensores, pre-splitting)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=13|PDF 13 · impresa 263 (sesgo y celebridades)]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=14|PDF 14 · impresa 264 (salado y heat management)]].

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/01 Shards réplicas y carga|← Shards, réplicas y carga]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/03 Hash claves compuestas y orden|Hash, claves compuestas y orden →]]
