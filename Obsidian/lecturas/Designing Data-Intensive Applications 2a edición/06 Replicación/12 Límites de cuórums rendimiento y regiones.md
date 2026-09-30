---
title: "DDIA — Límites de los cuórums, rendimiento y operación multirregión"
created: 2026-09-29
capitulo: 6
tags:
  - lecturas/ddia
  - arquitectura/replicacion
cobertura: "Impresas 233–237"
---

# DDIA — Límites de los cuórums, rendimiento y operación multirregión

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Índice de Replicación]]

La [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/11 Sin líder reparación y cuórums|nota anterior]] dejó una regla: si **w + r > n**, el grupo de réplicas donde escribiste y el grupo desde el que lees comparten al menos un nodo. Esta nota explica por qué esa intersección **no equivale a consistencia fuerte**, qué ganas y pierdes al relajarla, y por qué, aun así, los sistemas sin líder rinden bien cuando algo va mal.

## Lo que importa es el solapamiento, no la mayoría

Se suele elegir w y r como **mayorías** (más de n / 2) porque así w + r > n y se toleran hasta ⌊n / 2⌋ fallos. Pero un cuórum no tiene que ser mayoría: basta con que **cualquier grupo de lectura y cualquier grupo de escritura se solapen** en al menos un nodo. Existen otras asignaciones de cuórum que aprovechan esa flexibilidad.

También puedes elegir **w + r ≤ n**. Las peticiones siguen yendo a las n réplicas, pero esperas menos respuestas. Consecuencias: lecturas obsoletas más probables (quizá no incluyas el nodo con el valor nuevo), **menor latencia** y **mayor disponibilidad**, porque el sistema solo deja de escribir o leer cuando las réplicas alcanzables bajan de w o de r.

> [!warning] Intersección no es consistencia fuerte universal
> w + r > n es una afirmación sobre **conjuntos de nodos**. No dice nada de escrituras que están en curso, de escrituras que fallaron a medias, de relojes, de nodos restaurados ni de réplicas que cambian de sitio. El libro recomienda tratar w y r como **perillas que ajustan la probabilidad** de leer datos obsoletos, no como garantías absolutas. Las bases tipo Dynamo están pensadas para casos que toleran consistencia eventual.

## Seis situaciones en que la intersección no basta

Todas con n = 3 (réplicas A, B, C), w = 2 y r = 2; los escenarios son propios, las causas son del libro.

1. **Restaurar desde una réplica vieja.** El valor v8 está en A y B. El disco de B muere y se reconstruye copiando C, que tenía v7. Ahora solo A tiene v8: por debajo de w. Una lectura de {B, C} devuelve v7.
2. **Rebalanceo en curso.** La clave se está moviendo de {A, B, C} a {B, C, D} (capítulo 7). Un escritor con la vista antigua escribe en {A, B}; un lector con la vista nueva lee de {C, D}. Los cuórums ya no se solapan.
3. **Lectura concurrente con una escritura.** La escritura de v8 llega a A y aún no a B. El lector 1 consulta {A, C}, ve v8 y v7 y devuelve v8. Justo después, el lector 2 consulta {B, C} y devuelve v7. El segundo lector, que preguntó más tarde, ve el pasado. Esto no es linealizable (capítulo 10).
4. **Escritura fallida a medias.** La escritura de v8 llega a A pero B y C tienen el disco lleno. Solo hubo 1 < w confirmaciones y el cliente recibe **error**. Sin embargo, **A no deshace nada**: no hay *rollback* automático de esa escritura parcial. Una lectura posterior de {A, B} devuelve v8 porque tiene la versión mayor, y el read repair puede copiarla a B. La escritura «fallida» puede terminar pareciendo exitosa; otra lectura de {B, C} devuelve v7. Si el cliente reintenta una operación no idempotente, puede aplicarla dos veces.
5. **LWW con relojes reales.** Cassandra y ScyllaDB deciden con marcas de tiempo de reloj real. Una escritura desde un nodo con el reloj adelantado puede hacer que otra posterior se descarte en silencio ([[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/09 Conflictos LWW siblings y reglas del dominio|nota 09]]).
6. **Escrituras concurrentes.** Dos escrituras sobre la misma clave pueden procesarse en orden distinto en cada réplica: es un conflicto como en multilíder ([[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/13 Causalidad versiones y vectores|nota 13]]).

## Vigilar la obsolescencia

Aunque tu aplicación tolere lecturas viejas, necesitas saber si la replicación se está atrasando mucho, para investigar redes o nodos sobrecargados. Con un líder es sencillo: todos aplican las escrituras en el mismo orden, así que **posición del líder − posición del seguidor** en el log mide el retraso. Sin líder **no hay un orden fijo** de aplicación y esa resta no existe. El número de pistas pendientes de entregar sirve como indicio, pero es difícil de interpretar. La consistencia eventual es deliberadamente vaga; para operar el sistema hay que **cuantificar ese «eventualmente»**.

## Rendimiento: por qué sin líder aguanta mejor los fallos

Leer del líder actual evita el retraso de los seguidores para los cambios que ese líder ya aplicó. Una garantía de frescura más fuerte depende del contrato de lectura y de la conservación del historial durante failover. Concentrar allí las consultas tiene costes: el rendimiento de lectura queda limitado por la capacidad del líder; si el líder cae, hay que esperar a que se detecte el fallo y termine el *failover*, y los usuarios notan el aumento de tiempos de respuesta; y cualquier lentitud del líder por sobrecarga o contención de recursos llega directamente a los usuarios.

Sin líder no hay failover y las peticiones ya van a varias réplicas en paralelo, así que **una réplica lenta o caída apenas afecta**: usas las respuestas más rápidas. El libro relaciona ese aprovechamiento de las respuestas rápidas con ***request hedging***: enviar peticiones redundantes para evitar depender de un destino lento. Algunas implementaciones las envían desde el inicio y otras lanzan una copia tras una demora. En una lectura de cuórum debes reunir las r respuestas exigidas y reconciliar sus valores; no basta con devolver la primera. La técnica puede reducir la **latencia de cola** (*tail latency*): los percentiles altos, como el p99, que es lo que sufren los usuarios más desafortunados.

Un cálculo propio, suponiendo que cada réplica tiene independientemente un 1 % de probabilidad de responder lento en una petición:

| Estrategia | La lectura es lenta si… | Probabilidad |
|---|---|---|
| Leer solo del líder | el líder va lento | 1 % |
| n = 3, esperar las 2 más rápidas | al menos 2 de 3 van lentas | 3 · 0,01² · 0,99 + 0,01³ ≈ **0,03 %** |
| n = 3, esperar las 3 | al menos 1 de 3 va lenta | 1 − 0,99³ ≈ **3 %** |

La última fila muestra la otra cara: con n fijo, **cuanto mayor es r o w, más probable es toparte con una réplica lenta**. Por eso en la práctica los cuórums rara vez pasan de 4 de 7 o 5 de 9. En sistemas reales la lentitud suele estar correlacionada (misma zona, misma sobrecarga), y los números serían peores que con independencia.

La resiliencia de fondo viene de que **el sistema no distingue entre caso normal y caso de fallo**. Eso ayuda con las **fallas grises** (*gray failures*): un nodo que no está caído pero funciona degradado y muy lento, de modo que los detectores lo ven «vivo». Un sistema con líder debe decidir si la situación justifica un failover, que a su vez puede empeorar las cosas; sin líder, la pregunta ni se plantea.

Sin líder también hay problemas de rendimiento:

- **La reparación carga al sistema en mal momento.** Aunque no haya failover, las réplicas deben detectar que otra no está para guardarle pistas, y al volver hay que enviárselas. Si estuvo fuera mucho tiempo, el *hinted handoff* genera carga extra justo cuando el sistema ya sufre.
- **Cuórums grandes, más espera**, como muestra la tabla.
- **Particiones de red grandes.** Si el cliente queda separado de muchas réplicas, no se puede formar cuórum.

## Cuórum laxo: escribir fuera de las réplicas habituales

Para ese último caso, algunas bases permiten que **cualquier réplica alcanzable acepte la escritura aunque no sea una de las n habituales de esa clave**. Riak y Dynamo lo llaman **cuórum laxo** (*sloppy quorum*). El libro también menciona `ANY` de Cassandra y ScyllaDB por permitir confirmar escrituras mediante pistas cuando sus destinos normales no responden; eso no implica que sus protocolos sean idénticos ni que `ANY` sea un cuórum configurable de dos nodos. Ejemplo propio del caso laxo con Dynamo/Riak: la clave vive en {A, B, C}, un corte de red te deja ver solo D y E; con w = 2 escribes en D y E, que guardan pistas para devolver el dato a su sitio. Si otro cliente lee de {A, B} con r = 2, **no hay intersección posible**: D y E no están entre las réplicas consultadas. No hay garantía de leer lo escrito hasta que las pistas se entreguen; aun así, según la aplicación, puede ser mejor que un error.

## Tres enfoques frente a la red

La replicación **multilíder** resiste aún mejor las interrupciones de red, porque leer y escribir solo requiere hablar con un líder, que puede estar junto al cliente; a cambio, las lecturas pueden estar **arbitrariamente** atrasadas. Los cuórums son un compromiso: buena tolerancia a fallos y **alta probabilidad** de leer datos al día.

## Varias regiones sin líder

En Cassandra y ScyllaDB, un cliente que escribe en varias regiones elige un **nodo coordinador en su región local**. El coordinador reenvía la escritura a **todas las réplicas de su región** y a **una réplica de cada región remota**, que la reenvía a las demás de la suya. Así la petición cruza cada enlace entre regiones una sola vez.

El nivel de consistencia decide cuántas respuestas esperar: un cuórum sobre todas las réplicas de todas las regiones, un cuórum separado **en cada** región, o un cuórum **solo en la región local**. El cuórum local evita esperar a regiones lejanas, pero es más probable que devuelva datos viejos. Ejemplo propio: tres réplicas en Europa y tres en EE. UU.; escribes con cuórum local en Europa (2 de 3 europeas) y alguien lee con cuórum local en EE. UU. (2 de 3 estadounidenses). **Los dos grupos no comparten ningún nodo**, así que la lectura americana puede no ver la escritura europea aunque cada operación cumpliera su cuórum. Riak, en cambio, mantiene toda la comunicación cliente-base de datos dentro de una región (su n cuenta réplicas de una región) y replica entre clústeres de forma asíncrona en segundo plano, al estilo multilíder.

> [!question]- Con n = 3, w = 2, r = 2, un cliente recibe error al escribir. ¿Puede otro lector ver ese valor?
> Sí, en el escenario con versiones 7 y 8, el valor 8 puede quedar en una réplica aunque no se alcanzaran w confirmaciones. Si una lectura incluye esa réplica y usa la selección por versión mayor del ejemplo, puede devolverlo; el read repair también puede propagarlo. Con escrituras concurrentes, la resolución puede ser más compleja que escoger el número mayor.

> [!question]- ¿Por qué un cuórum laxo rompe la garantía de w + r > n?
> Porque la escritura se guardó en nodos que no pertenecen a las n réplicas habituales. La cuenta de intersección solo vale dentro de esas n.

> [!question]- ¿Por qué no subir r a 7 de 9 «para ir más seguro»?
> Porque cada respuesta extra que esperas aumenta la probabilidad de depender de una réplica lenta o caída, lo que empeora la latencia de cola y la disponibilidad de lectura.

> [!question]- ¿Qué distingue una falla gris de una caída, y por qué la tolera mejor un sistema sin líder?
> En una falla gris el nodo responde, pero muy lento. Con líder hay que decidir si hacer failover. Sin líder simplemente usas las respuestas más rápidas de las otras réplicas.

## Referencias

PDF 37–41 · impresas 233–237 · figura 6-13 como antecedente. Enlaces: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=37|PDF 37 · impresa 233]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=38|PDF 38 · impresa 234]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=39|PDF 39 · impresa 235]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=40|PDF 40 · impresa 236]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=41|PDF 41 · impresa 237]]. Los seis escenarios con A, B, C, la tabla de probabilidades, el cuórum laxo con D y E y el ejemplo Europa/EE. UU. son elaboración propia sobre las causas que enumera el libro.

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/11 Sin líder reparación y cuórums|Sin líder, reparación y cuórums]] · **Índice:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Replicación]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/13 Causalidad versiones y vectores|Causalidad, versiones y vectores]]
