---
title: "DDIA — Replicación sin líder: reparación y cuórums"
created: 2026-09-29
capitulo: 6
tags:
  - lecturas/ddia
  - arquitectura/replicacion
cobertura: "Impresas 229–233"
---

# DDIA — Replicación sin líder: reparación y cuórums

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Índice de Replicación]]

Con uno o varios líderes, el cliente envía cada escritura a **un** nodo y ese líder decide el orden en que los seguidores la aplican. La replicación **sin líder** (*leaderless*) abandona esa idea: **cualquier réplica acepta escrituras directamente**, y el cliente habla con varias a la vez. Algunos de los primeros sistemas replicados ya eran así; la idea volvió a ponerse de moda cuando Amazon describió su sistema interno **Dynamo** en 2007. Riak, Cassandra y ScyllaDB se inspiraron en él, y por eso a este estilo se le llama **tipo Dynamo**.

> [!warning] Dynamo no es DynamoDB
> Dynamo se describió en un artículo y nunca se ofreció fuera de Amazon. La edición describe **DynamoDB**, el servicio en la nube de nombre parecido, con una arquitectura distinta: replicación con **un único líder por grupo de datos** basada en el algoritmo de consenso Multi-Paxos. Lo que se explica aquí no describe DynamoDB.

## Coordinador no es líder

En algunas implementaciones el propio cliente envía la escritura a varias réplicas. En otras, un **nodo coordinador** lo hace en nombre del cliente. Parecería un líder con otro nombre, pero no: el coordinador **no impone un orden** a las escrituras. Reenvía y cuenta respuestas; cada réplica aplica lo que le llega en el orden en que le llega. Cualquier nodo puede coordinar cualquier petición, y dos coordinadores pueden reenviar escrituras concurrentes sobre la misma clave sin enterarse. Esa ausencia de orden único es lo que obliga, más adelante, a detectar escrituras concurrentes ([[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/13 Causalidad versiones y vectores|nota 13]]).

## Escribir con un nodo caído

Hay tres réplicas y la réplica C se está reiniciando para instalar una actualización. Con un solo líder quizá necesitarías un *failover*. Sin líder **no existe failover**: todas las réplicas son iguales.

Adaptando la figura 6-12 a un ejemplo propio: un usuario cambia su tema de `claro` (versión 6) a `oscuro`. El cliente envía la escritura **en paralelo a las tres réplicas**. A y B la aceptan; C no responde. Si basta con que dos de tres confirmen, tras dos «OK» la escritura se considera exitosa, y el cliente ignora que C se la perdió.

Cuando C vuelve, sigue guardando `claro`. Quien lea solo de C obtendrá un valor **obsoleto** (desactualizado). Por eso **las lecturas también se envían a varias réplicas en paralelo**. Las respuestas pueden diferir: `oscuro` versión 7 desde A y B, `claro` versión 6 desde C. En este ejemplo sin escrituras concurrentes, cada valor lleva un **número de versión** y el cliente se queda con la mayor, aunque solo una réplica la haya devuelto. En el caso general una marca de tiempo permite escoger según LWW; los vectores de versión, en cambio, pueden detectar valores incomparables que deben conservarse como siblings. No siempre existe una única versión mayor.

> [!warning] Qué significa exactamente un «OK» de una réplica
> Confirmar no es lo mismo que haber **aplicado** el cambio en todas partes ni haberlo **forzado a disco** con `fsync`. Según el sistema y su configuración, una réplica puede responder al recibir el dato en memoria, al añadirlo a su *commit log* (que quizá solo llegó a la caché de páginas del sistema operativo) o únicamente después del `fsync`. La documentación de Cassandra distingue modos: `periodic` puede confirmar antes de la sincronización periódica y `batch` espera a que termine el `fsync`. No se presupone aquí cuál es el modo de tu instalación. [Fuente oficial sobre CommitLog](https://cassandra.apache.org/_/blog/Learn-How-CommitLog-Works-in-Apache-Cassandra.html). «w réplicas confirmaron» significa «w réplicas dijeron que cumplieron **lo que su protocolo define como confirmar**». Elaboración propia.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-12.png|1000]]

La escritura de la nueva foto se confirma en las réplicas 1 y 2 aunque la réplica 3 esté desconectada. Después, la lectura de dos copias recibe tanto la versión 7 como la versión 6, detecta cuál quedó atrasada y devuelve la nueva foto. La flecha final transmite la versión 7 a la réplica 3: es reparación en lectura. El dibujo simplifica el número de solicitudes para destacar el quórum y la reparación.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=34|PDF 34 · impresa 230 · figura 6-12]].

## Tres formas de ponerse al día

El sistema debe asegurar que, tarde o temprano, todos los datos lleguen a todas las réplicas. Los almacenes tipo Dynamo combinan tres mecanismos:

| Mecanismo | Cuándo actúa | Qué arregla | Qué se le escapa |
|---|---|---|---|
| **Read repair** (reparación en lectura) | Durante una lectura a varias réplicas | Quien lee ve versión 6 en C y 7 en A y B, y **escribe la 7 de vuelta en C** | Claves que casi nunca se leen |
| **Hinted handoff** (entrega con pistas) | Mientras una réplica está caída | Otra réplica guarda las escrituras destinadas a C como **pistas** (*hints*) y se las entrega cuando vuelve; luego las borra | Si el nodo que guarda pistas también falla, o si la caída dura tanto que las pistas se descartan (comportamiento de implementaciones concretas) |
| **Anti-entropy** (antientropía) | Proceso de fondo periódico | Compara réplicas y copia lo que falta, se lea o no | Actúa con retraso y **sin orden**: no replica un log en secuencia como un líder |

Los tres se complementan. Read repair es barato y oportunista, pero depende del patrón de lecturas. Hinted handoff cubre claves nunca leídas mientras dure la caída. Anti-entropy es la red de seguridad para todo lo demás. En la práctica suele ser el coordinador, no la aplicación, quien hace el read repair, y la antientropía suele comparar resúmenes con árboles de Merkle para no transferir todo; ambos detalles son complemento propio.

## Cuórums: contar votos

¿Por qué bastaba con dos confirmaciones de tres? Para una escritura completada que se conserva en **al menos dos de tres** réplicas habituales, como mucho una no la tiene. Si lees de **al menos dos** de esas tres, una tiene que contenerla. Este argumento supone que las copias no perdieron el valor, que el grupo de réplicas no cambió y que no hay escrituras concurrentes que compliquen la selección; la nota siguiente levanta esos supuestos.

En general hay **n** réplicas por valor; una escritura necesita **w** confirmaciones para considerarse exitosa y una lectura consulta al menos **r** réplicas. Mientras **w + r > n**, el conjunto de réplicas escritas y el de réplicas leídas **se solapan**. El argumento es de conteo: dos grupos de tamaños w y r dentro de n nodos comparten al menos w + r − n nodos. Con n = 3, w = 2, r = 2: 2 + 2 − 3 = 1 nodo en común como mínimo. Las lecturas y escrituras que respetan estos valores se llaman **de cuórum**; r y w son el número mínimo de votos para que la operación valga.

Normalmente la petición **se envía a las n réplicas en paralelo**; w y r solo dicen **a cuántas respuestas esperas**. Si responden menos de w o r, la operación devuelve error. Al sistema no le importa por qué faltó la respuesta: nodo caído, disco lleno, red cortada o cualquier otra causa.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-13.png|1000]]

Los tres nodos que confirman la escritura forman W y los tres que responden a la lectura forman R. Aunque se elijan los grupos con el menor solapamiento posible, ambos incluyen a la réplica 3: 3 + 3 − 5 = 1. Las flechas grises y las cruces indican solicitudes que no contribuyen al quórum. Esta intersección asegura acceso a una copia de una escritura confirmada bajo los supuestos habituales, pero por sí sola no resuelve escrituras concurrentes ni garantiza linealizabilidad.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=36|PDF 36 · impresa 232 · figura 6-13]].

## Elegir n, w y r

Son configurables. Lo habitual es un n impar (3 o 5) con w = r = (n + 1) / 2, es decir, **mayorías**. Una escritura tolera n − w réplicas no disponibles; una lectura, n − r.

| n | w | r | ¿w + r > n? | Réplicas caídas que toleran escrituras / lecturas | Para qué |
|---|---|---|---|---|---|
| 3 | 2 | 2 | Sí (4 > 3) | 1 / 1 | Equilibrio típico (figura 6-12) |
| 5 | 3 | 3 | Sí (6 > 5) | 2 / 2 | Más tolerancia (figura 6-13) |
| 3 | 3 | 1 | Sí (4 > 3) | 0 / 2 | Muchas lecturas: rápidas, pero **un solo nodo caído bloquea todas las escrituras** |
| 3 | 1 | 1 | No (2 ≤ 3) | 2 / 2 | Baja latencia y alta disponibilidad, lecturas obsoletas probables |

El clúster puede tener muchos más de n nodos: cada valor se guarda en **n** de ellos, lo que permite repartir un conjunto de datos mayor que un nodo (particionado, capítulo 7).

La promesa de w + r > n es **la intersección de dos conjuntos de nodos**, no «toda lectura ve siempre la última escritura». Esa diferencia, y los casos en que incluso la intersección falla, son el tema de [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/12 Límites de cuórums rendimiento y regiones|la nota siguiente]].

> [!question]- Con n = 5, w = 2 y r = 3, ¿está garantizado leer la última escritura?
> No: 2 + 3 = 5, que no es mayor que 5. Puedes escribir en {A, B} y leer de {C, D, E} sin ningún nodo en común.

> [!question]- ¿Qué mecanismo repara una clave que nadie lee y cuya réplica estuvo caída?
> Read repair no, porque depende de lecturas. Hinted handoff la repara si las pistas se guardaron y entregaron; si no, la antientropía de fondo acaba copiándola.

> [!question]- Si Cassandra usa un coordinador por petición, ¿por qué no es un sistema con líder?
> Porque el coordinador solo reenvía y cuenta respuestas; no fija un orden de escrituras ni es único. Cualquier nodo puede coordinar y dos escrituras concurrentes pueden llegar en órdenes distintos a cada réplica.

> [!question]- Configuras n = 3, w = 3, r = 1. ¿Qué pasa si una réplica se apaga para mantenimiento?
> Las lecturas siguen (necesitan una respuesta), pero **todas las escrituras fallan**, porque exigen las tres confirmaciones.

## Referencias

PDF 33–37 · impresas 229–233 · figuras 6-12 y 6-13. Enlaces: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=33|PDF 33 · impresa 229]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=34|PDF 34 · impresa 230 · figura 6-12]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=35|PDF 35 · impresa 231]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=36|PDF 36 · impresa 232 · figura 6-13]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=37|PDF 37 · impresa 233]]. El ejemplo del tema claro/oscuro adapta la figura 6-12 (foto de perfil, versiones 6 y 7); la tabla de mecanismos, el recuadro sobre confirmación y `fsync`, y las filas 3/3/1 y 3/1/1 son elaboración propia.

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/10 CRDT y transformación operacional|CRDT y transformación operacional]] · **Índice:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Replicación]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/12 Límites de cuórums rendimiento y regiones|Límites de cuórums, rendimiento y regiones]]
