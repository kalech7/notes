---
title: "DDIA — Detectar concurrencia: causalidad, números de versión y vectores de versión"
created: 2026-09-29
capitulo: 6
tags:
  - lecturas/ddia
  - arquitectura/replicacion
cobertura: "Impresas 237–242"
---

# DDIA — Detectar concurrencia: causalidad, números de versión y vectores de versión

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Índice de Replicación]]

Las notas anteriores daban por hecho que el sistema **sabe** cuándo dos escrituras chocan. Esta nota explica cómo lo averigua. La idea central: **la causalidad trata de qué sabía cada operación, no de qué hora marcaba el reloj**.

## Por qué el orden de llegada no sirve

Adaptando la figura 6-14: los clientes A y B escriben a la vez sobre la clave X en tres nodos. El nodo 1 recibe la escritura de A y nunca la de B por un corte momentáneo; el nodo 2 recibe A y luego B; el nodo 3 recibe B y luego A. Si cada nodo **sobrescribe** con lo último que le llega, el nodo 2 termina con B y los nodos 1 y 3 con A, **para siempre**. Nadie converge.

Los conflictos pueden detectarse al escribir, pero también después, durante el read repair, el hinted handoff o la antientropía. Para converger se usa cualquier mecanismo de resolución ya visto: LWW (Cassandra, ScyllaDB), resolución manual o CRDT (Riak). LWW es fácil, pero una marca de tiempo **no dice si dos valores son concurrentes** o si uno se escribió después de ver el otro. Para resolver conflictos explícitamente hay que detectar la concurrencia.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-14.png|1000]]

A envía X = A y B envía X = B sin haber observado la escritura ajena. El nodo 2 recibe B después de A, pero el nodo 3 recibe A después de B; el nodo 1 no acepta la solicitud de B. Una consulta posterior puede obtener A, B y A de las tres copias. El orden de llegada local no identifica una última escritura común: hace falta detectar la concurrencia y aplicar una política explícita de resolución.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=42|PDF 42 · impresa 238 · figura 6-14]].

## «Sucede antes» y concurrencia

Una operación A **sucede antes** (*happens before*) que B si B **conoce** A, **depende** de A o **se construye sobre** A. En la figura 6-8 del libro, B incrementa una fila que A insertó: B se apoya en A, así que A sucede antes que B y B **depende causalmente** de A. En la figura 6-14, en cambio, ningún cliente sabía del otro: no hay dependencia.

Dos operaciones son **concurrentes** si **ninguna sucede antes que la otra**. Entre dos operaciones A y B solo hay tres posibilidades: A antes que B, B antes que A, o concurrentes. Para dos versiones de la misma clave, si una sucede antes y la nueva representa su sustitución, la posterior puede sobrescribir a la anterior. Si son concurrentes, hace falta una regla para tratarlas; dos escrituras en claves independientes no necesariamente chocan por ser concurrentes.

> [!info] Concurrencia no es simultaneidad
> Dos mensajes enviados desde móviles sin cobertura en un túnel, con una hora de diferencia, son concurrentes si ninguno pudo ver al otro. Dos escrituras separadas por un milisegundo no son concurrentes si la segunda leyó la primera. Saber si dos cosas ocurrieron exactamente a la vez es muy difícil con relojes distribuidos (capítulo 9), y además no importa. El libro lo compara con la relatividad: dos sucesos lejanos no pueden afectarse si la luz no tuvo tiempo de ir de uno a otro. En computación el criterio es aún más amplio: aunque la luz sí hubiera tenido tiempo, una red lenta o cortada puede impedir que una operación sepa de la otra, y entonces son concurrentes.

## El algoritmo con un solo servidor

Para empezar simple, el libro usa **una sola réplica**. Reglas:

1. El servidor guarda **un número de versión por clave**, lo incrementa en cada escritura y lo almacena junto al valor.
2. Al leer, el servidor devuelve **todos los siblings** (valores no sobrescritos) y el **último número de versión**. Hay que leer antes de escribir.
3. Al escribir, el cliente incluye **el número de versión de su lectura previa** (su **contexto**) y **fusiona todos los valores que recibió**. La respuesta a una escritura también trae los siblings, así que se pueden encadenar escrituras.
4. Al recibir una escritura con versión v, el servidor **sobrescribe todos los valores con versión ≤ v** (ya están fusionados en el nuevo) y **conserva los de versión mayor** (son concurrentes con esta escritura).

Una escritura **sin** número de versión es concurrente con todo: no sobrescribe nada y queda como un sibling más. El servidor nunca interpreta los valores; solo compara números.

### Las cinco escrituras de la figura 6-15

Dos clientes añaden productos al mismo carrito, inicialmente vacío. Adaptación del libro con los artículos en español (*milk, eggs, flour, ham, bacon*):

| Paso | Cliente | Contexto enviado | Valor enviado | Versión asignada | Se sobrescribe | Siblings tras la escritura (lo que recibe el cliente) |
|---|---|---|---|---|---|---|
| 1 | C1 | ninguno | [leche] | 1 | nada | v1 [leche] |
| 2 | C2 | ninguno (no sabe de la leche) | [huevos] | 2 | nada | v1 [leche] · v2 [huevos] |
| 3 | C1 | 1 | [leche, harina] | 3 | ≤ 1: [leche] | v2 [huevos] · v3 [leche, harina] |
| 4 | C2 | 2 | [huevos, leche, jamón] | 4 | ≤ 2: [huevos] (la v1 ya no estaba) | v3 [leche, harina] · v4 [huevos, leche, jamón] |
| 5 | C1 | 3 | [leche, harina, huevos, tocino] | 5 | ≤ 3: [leche, harina] | v4 [huevos, leche, jamón] · v5 [leche, harina, huevos, tocino] |

En el paso 4, C2 fusiona lo que recibió en el paso 2, [leche] y [huevos], y añade jamón. En el paso 5, C1 fusiona lo que recibió en el paso 3, [leche, harina] y [huevos], y añade tocino. El contexto de cada cliente es **lo que sabía**, y eso decide qué se borra.

### El grafo de la figura 6-16

Una flecha de X a Y significa «Y conocía o dependía de X»:

| Desde | Hacia | Por qué |
|---|---|---|
| v1 [leche] | v3 | C1 añadió harina a su leche |
| v1 [leche] | v4 | C2 fusionó la leche recibida en el paso 2 |
| v2 [huevos] | v4 | C2 partió de sus huevos |
| v2 [huevos] | v5 | C1 recibió los huevos en el paso 3 |
| v3 [leche, harina] | v5 | C1 añadió tocino |

Son **concurrentes** v1 y v2, v2 y v3, v3 y v4, y v4 y v5. Ningún cliente está nunca del todo al día, porque siempre hay otra operación en curso. Aun así, las versiones viejas acaban sobrescribiéndose y **no se pierde ninguna aportación del carrito en este ejemplo**: el estado final guarda dos siblings que una lectura posterior puede fusionar. Las versiones antiguas se eliminan solo cuando su contenido ya está representado en una posterior; una fusión incorrecta de la aplicación sí podría perder productos.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-15.png|1000]]

Las cinco escrituras llegan en el orden numerado de la línea central, pero cada cliente solo conoce la respuesta de su operación anterior. El contexto 1 del paso 3 permite reemplazar [leche], pero no [huevos], que apareció concurrentemente. El contexto 2 del paso 4 y el contexto 3 del paso 5 dejan también una versión hermana que su cliente aún no había visto. La tabla distingue el nuevo valor enviado de todos los valores que conserva el servidor; al final quedan dos ramas, y una fusión posterior puede reunir sus artículos.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=44|PDF 44 · impresa 240 · figura 6-15]].

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-16.png|1000]]

El grafo conecta una edición con las anteriores que su cliente ya conocía. Añadir harina depende de la leche; añadir jamón depende tanto de los huevos como de la leche; añadir tocino depende de harina y huevos. No existe un camino causal entre harina y jamón, ni entre jamón y tocino: esas parejas son concurrentes. Las dos salidas muestran las versiones hermanas que quedaron al final de la figura anterior.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=46|PDF 46 · impresa 242 · figura 6-16]].

## Vectores de versión: varias réplicas sin líder

Con varias réplicas aceptando escrituras, un solo contador falla: si R1 y R2 están en la versión 3 y cada una acepta una escritura distinta, ambas asignan un 4 y el número ya no identifica una historia. La solución es **un número de versión por réplica y por clave**. Cada réplica incrementa **su propio** componente al procesar una escritura y recuerda los números que ha visto de las demás. El conjunto se llama **vector de versión** (*version vector*). Este es el modelo introductorio del libro: hay que asociar el contexto correcto a cada versión, no confundir todo lo recibido por un servidor con lo que conocía el cliente de una escritura concreta. Las variantes con puntos separan la identidad de una escritura nueva del contexto que trae; una implementación no se obtiene simplemente incrementando un contador global y adjuntándolo a cualquier petición.

Para comparar dos vectores se mira **componente a componente**, interpretando como cero un componente ausente. a precede a b si cada componente de a es ≤ que el de b y alguno es menor. Si en unos componentes a es mayor y en otros menor, **no son comparables**, y eso significa **concurrencia**.

| a | b | Resultado |
|---|---|---|
| {R1: 1} | {R1: 1, R2: 1} | a antes que b: b sobrescribe |
| {R1: 1, R2: 1} | {R3: 1} | incomparables: concurrentes, siblings |
| {R1: 2, R2: 1, R3: 1} | {R1: 1, R2: 1} | b antes que a |
| {R1: 3, R2: 0} | {R1: 1, R2: 2} | incomparables: concurrentes |

Ejemplo propio con la clave `tema`: X escribe `claro` en R1 → {R1: 1}. Y lee de R1, recibe ese vector y escribe `oscuro` en R2 → {R1: 1, R2: 1}, que domina al anterior y lo sobrescribe. Z escribe `sepia` en R3 sin leer → {R3: 1}, incomparable: quedan dos siblings. W lee ambos (contexto {R1: 1, R2: 1, R3: 1}), elige `oscuro` y escribe en R1 → {R1: 2, R2: 1, R3: 1}, que domina a los dos.

Igual que en la figura 6-15, el vector **viaja al cliente en cada lectura y vuelve en la escritura siguiente**. Riak lo codifica como una cadena llamada **contexto causal** (*causal context*). Por eso es seguro leer de una réplica y escribir en otra: pueden surgir siblings, pero no se pierden datos si se fusionan bien. Existen variantes; la más interesante según el libro es el **vector de versión con puntos** (*dotted version vector*) de Riak 2.0, que funciona de forma muy parecida al ejemplo del carrito.

> [!info] Vector de versión y reloj vectorial no son sinónimos exactos
> A veces se llama **reloj vectorial** (*vector clock*) a un vector de versión, pero no son lo mismo. Un reloj vectorial ordena **eventos de procesos**: se incrementa en cada evento, incluidos envíos y recepciones de mensajes. Un vector de versión describe **versiones de un dato replicado**: solo avanza cuando una réplica acepta una escritura de esa clave, y al sincronizar dos réplicas se toma el máximo por componente sin incrementar. La regla de comparación es la misma, de ahí la confusión. Para comparar estados de réplicas, el libro indica que la estructura correcta es el vector de versión. El detalle de las diferencias es complemento propio.

> [!question]- ¿Qué indica una marca de tiempo que no indica un vector de versión, y viceversa?
> La marca con una regla de desempate da un orden total, pero no dice si dos escrituras se conocían. El vector no da un orden total, pero distingue «una conocía a la otra» de «ninguna conocía a la otra», que es lo necesario para no descartar datos.

> [!question]- En el paso 4, ¿por qué no se borra [leche, harina]?
> Porque tiene versión 3 y C2 envió contexto 2: C2 no la conocía, así que es concurrente con su escritura y se conserva.

> [!question]- {R1: 2, R2: 0, R3: 5} frente a {R1: 2, R2: 1, R3: 4}: ¿qué relación hay?
> Incomparables: R2 es menor en el primero y R3 mayor. Son concurrentes y ambos valores quedan como siblings.

> [!question]- Si el cliente escribe sin enviar versión, ¿qué hace el servidor?
> La trata como concurrente con todo: no sobrescribe nada y añade el valor como un sibling más.

## Referencias

PDF 41–46 · impresas 237–242 · figuras 6-14, 6-15 y 6-16. Enlaces: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=41|PDF 41 · impresa 237]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=42|PDF 42 · impresa 238 · figura 6-14]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=43|PDF 43 · impresa 239]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=44|PDF 44 · impresa 240 · figura 6-15]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=45|PDF 45 · impresa 241]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=46|PDF 46 · impresa 242 · figura 6-16]]. El carrito es adaptación de la figura 6-15 y el grafo de la 6-16; el ejemplo `tema` con R1–R3, la tabla de comparaciones y la diferencia detallada con relojes vectoriales son propios.

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/12 Límites de cuórums rendimiento y regiones|Límites de cuórums, rendimiento y regiones]] · **Índice:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Replicación]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/14 Laboratorio y repaso resuelto|Laboratorio y repaso resuelto]]
