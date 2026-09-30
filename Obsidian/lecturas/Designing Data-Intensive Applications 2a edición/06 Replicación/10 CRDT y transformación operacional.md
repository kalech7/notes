---
title: "DDIA — Resolución automática: CRDT y transformación operacional"
created: 2026-09-29
capitulo: 6
tags:
  - lecturas/ddia
  - arquitectura/replicacion
cobertura: "Impresas 226–228"
---

# DDIA — Resolución automática: CRDT y transformación operacional

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Índice de Replicación]]

LWW converge perdiendo datos y los siblings conservan todo pero trasladan el trabajo a la aplicación. Para muchas aplicaciones la mejor opción es un **algoritmo que fusione automáticamente las escrituras concurrentes** y preserve, en lo posible, la intención de todas. Esta nota explica qué garantiza eso, cómo se hace para cada tipo de dato y dónde se acaba.

## Convergencia y consistencia eventual fuerte

La resolución automática garantiza **convergencia**: todas las réplicas que han procesado **el mismo conjunto de escrituras** tienen el mismo estado, **sin importar el orden en que les llegaron**. Consistencia eventual más convergencia garantizada se llama **consistencia eventual fuerte** (*strong eventual consistency*). LWW es, técnicamente, un algoritmo de este tipo; los que siguen intentan además no perder actualizaciones.

> [!warning] «Fuerte» no significa linealizable
> Consistencia eventual fuerte promete que réplicas con las mismas escrituras coinciden. **No** promete que leas la escritura más reciente, ni que todas las réplicas vean las escrituras en el mismo momento, ni que se cumplan reglas globales. Si tu móvil aún no recibió los *likes* que llegaron a otro dispositivo, te mostrará un número menor y eso está permitido. La **linealizabilidad**, que el libro trata en el capítulo 10, exige que las operaciones parezcan ocurrir atómicamente en una sola copia respetando el orden temporal real. Una lectura que empieza después de completar una escritura debe verla o ver otra escritura legítimamente posterior.

## Cómo se fusiona cada tipo de dato

**Texto.** Se detectan los caracteres insertados y borrados de una versión a otra; el resultado conserva todas las inserciones y borrados de todos los siblings. Si dos usuarios insertan en la misma posición, se ordenan con una regla determinista para que todos los nodos obtengan lo mismo.

**Colecciones.** Una lista de tareas (ordenada) y un carrito (sin orden) necesitan registrar inserciones **y borrados**. Una lista añade el problema de preservar el orden de los elementos; el ejemplo siguiente desarrolla únicamente un conjunto sin orden. Retomando el carrito de la figura 6-10 (adaptado): cada alta recibe una etiqueta única, y cada baja deja una **lápida** (*tombstone*), un registro de «esta alta concreta se borró».

| Réplica | Altas conocidas | Lápidas | Visible |
|---|---|---|---|
| Inicio | DVD#a1, Libro#a2 | — | {DVD, Libro} |
| Dispositivo 1: quita Libro, añade Jabón | DVD#a1, Libro#a2, Jabón#d1 | a2 | {DVD, Jabón} |
| Dispositivo 2: quita DVD | DVD#a1, Libro#a2 | a1 | {Libro} |
| Fusión: unión de altas y unión de lápidas | a1, a2, d1 | a1, a2 | **{Jabón}** |

Es el resultado que el libro da como correcto. Si alguien vuelve a añadir un Libro de forma concurrente, esa alta tendrá una etiqueta nueva sin lápida y sobrevivirá. El coste (elaboración propia) es que las lápidas se acumulan; retirarlas exige demostrar que ninguna réplica o actualización antigua podrá reintroducir las altas borradas. Saber que las réplicas relevantes ya conocen el borrado forma parte de esa prueba, pero también importan las reglas de reconexión y entrega de mensajes antiguos.

**Contadores.** Para un número que sube y baja, como los *likes*, el algoritmo sabe cuántos incrementos y decrementos hizo cada sibling y los suma sin contarlos dos veces ni perderlos. La forma habitual es guardar **un componente por réplica**; cada réplica solo incrementa el suyo:

| Paso | Estado | Total |
|---|---|---|
| R1 recibe 3 likes | {R1: 3, R2: 0} | 3 |
| R2 recibe 2 likes, concurrentemente | {R1: 0, R2: 2} | 2 |
| Fusión: **máximo por componente** | {R1: 3, R2: 2} | **5** |

Compara con las alternativas ingenuas. El **máximo de los totales** daría max(3, 2) = 3 y perdería dos likes. La **suma de los totales** daría 5 la primera vez, pero si R1 vuelve a enviar su estado ya fusionado (total 5) y R2 lo suma a sus 2, obtiene 7: cuenta dos veces. El máximo por componente, en cambio, da el mismo resultado aunque fusiones repetidamente o en cualquier orden. Para restar se usan dos vectores, uno de incrementos y otro de decrementos: si R2 registra un *unlike*, el valor es (3 + 2) − 1 = 4.

**Mapas clave-valor.** Actualizaciones a claves distintas no interfieren. Para la misma clave se aplica a su valor alguno de los algoritmos anteriores.

## Dos familias: OT y CRDT

Las dos familias más usadas son la **transformación operacional** (OT) y los **tipos de datos replicados libres de conflictos** (CRDT). Filosofías y rendimiento distintos; ambas pueden fusionar texto, listas, contadores y mapas. La figura 6-11 compara cómo fusionan el mismo caso: dos réplicas empiezan con `ice`; una antepone `n` (queda `nice`) y la otra añade `!` (queda `ice!`). Ambas deben terminar en `nice!`.

**OT: posiciones que se corrigen.** Cada operación registra un **índice**. La réplica A hace `insert(0, "n")` y la réplica B hace `insert(3, "!")` (en `ice` las posiciones son 0, 1 y 2, así que 3 es el final). Al intercambiarlas:

- B recibe `insert(0, "n")` y la aplica tal cual: `nice!`.
- A recibe `insert(3, "!")`. Aplicada sin más sobre `nice` daría `nic!e`, incorrecto. Hay que **transformarla** teniendo en cuenta la operación concurrente ya aplicada: como `n` se insertó en una posición anterior, el índice sube a 4 → `insert(4, "!")` → `nice!`.

La función de transformación, `T(operación recibida, operación ya aplicada)`, es el corazón de OT: su regla aquí es «si otra inserción concurrente ocurrió antes de mi posición, desplázate una». Escribir funciones de transformación correctas para todos los pares de operaciones es delicado; los sistemas OT prácticos suelen apoyarse en un servidor central que fija el orden de las operaciones (complemento propio).

**CRDT: identificadores estables en vez de posiciones.** La mayoría de CRDT de texto dan a cada carácter un **ID único e inmutable**, por ejemplo contador más réplica: `i` = 1A, `c` = 2A, `e` = 3A. Las operaciones se expresan respecto a IDs, no a índices:

- A: `insert(nil, 4A, "n")` → inserta `n` con ID 4A al principio (`nil` = «no hay carácter anterior»).
- B: `insert(3A, 4B, "!")` → inserta `!` con ID 4B justo después del carácter 3A.

Cuando A recibe la operación de B busca el carácter 3A, esté donde esté ahora; el `n` añadido delante no cambia nada. **No hace falta transformar el índice como en OT.** El protocolo aún necesita reconocer duplicados y disponer de los antecedentes que exige su algoritmo. Si dos inserciones concurrentes apuntan al mismo sitio, por ejemplo `?` con ID 4C y `!` con ID 4B ambos después de 3A, se ordenan por sus IDs con una regla fija (digamos, el ID mayor primero: `ice?!`). Todas las réplicas aplican la misma regla y convergen.

Los borrados vuelven a necesitar lápidas: si alguien borra `c` (2A) mientras otro inserta `x` después de 2A, la `c` se marca como borrada pero su ID se conserva para que la inserción siga encontrando su ancla. El resultado fusionado es `ixe`.

| | OT | CRDT |
|---|---|---|
| Cómo localiza una edición | Índice numérico | ID estable del elemento vecino |
| Qué hace con concurrencia | Transforma operaciones respecto a las concurrentes | Conserva anclas estables y aplica reglas de orden y borrado del algoritmo |
| Metadatos extra | Pocos en el documento | ID por elemento y lápidas |
| Dónde aparece según el libro | Google Docs; ShareDB (JSON) | Redis Enterprise, Riak, Azure Cosmos DB; Automerge y Yjs (JSON) |

Hay variantes de ambas ideas, se extienden de caracteres a elementos de listas y mapas, y existen algoritmos que combinan ventajas de las dos.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-11.png|1000]]

Los dos rombos muestran las mismas ediciones: una persona añade n al inicio de ice y otra añade ! al final. En OT, insertar n desplaza las posiciones, por lo que la inserción de ! debe transformarse de índice 3 a índice 4. En el CRDT ilustrado, cada carácter tiene una identidad estable: ! se inserta después de 3A y no hay que cambiar esa referencia cuando aparece n. Ambos mecanismos hacen que las dos ramas converjan en nice!, aunque internamente representan y combinan las operaciones de maneras diferentes.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=31|PDF 31 · impresa 227 · figura 6-11]].

## Converger no es cumplir las reglas del negocio

Una cuenta tiene 100 € modelados como contador CRDT. En la réplica A alguien retira 80 €: localmente ve 100, la regla «saldo ≥ 0» se cumple. En la réplica B, de forma concurrente, otra retirada de 80 € ve también 100. Al fusionar, ambas réplicas convergen perfectamente a **100 − 160 = −60 €**. El CRDT hizo exactamente su trabajo: no perdió ninguna operación. La regla se rompió porque **ninguna réplica podía saber lo que aprobaba la otra**. Lo mismo pasa con la lista de máximo cinco elementos del libro: la fusión solo puede respetarla descartando algo.

Para reglas así necesitas coordinar y proteger la decisión antes de confirmar, por ejemplo mediante transacciones o una operación atómica en una autoridad para las retiradas. Tener un único líder sin control de concurrencia tampoco impide que dos lecturas antiguas autoricen retiros incompatibles. Una alternativa propia de diseño es repartir de antemano el margen: cada réplica puede gastar como máximo 50 € sin consultar. El libro concluye que, pese a estos límites, la resolución automática basta para muchas aplicaciones útiles y es casi inevitable en apps colaborativas offline-first o local-first.

> [!question]- ¿Por qué fusionar contadores con el máximo de los totales es incorrecto?
> Porque cada total mezcla trabajo de varias réplicas. Con {R1: 3} y {R2: 2}, el máximo de totales da 3 y pierde los 2 de R2. El máximo **por componente** conserva lo que hizo cada réplica y da 5.

> [!question]- En OT, ¿qué pasaría si A aplicara `insert(3, "!")` sin transformar sobre `nice`?
> Obtendría `nic!e`, porque el índice 3 se calculó sobre `ice` y la `n` desplazó todo una posición. La transformación lo corrige a 4.

> [!question]- ¿Por qué un CRDT de texto necesita lápidas al borrar?
> Porque otras operaciones concurrentes pueden referirse al carácter borrado como ancla («inserta después de 2A»). Si el ID desapareciera, esas inserciones no sabrían dónde ir.

> [!question]- Un sistema tiene consistencia eventual fuerte. ¿Puedo usarlo para vender la última entrada de un concierto?
> No sin coordinación adicional. Garantiza que las réplicas convergen, no que solo una venta se apruebe: dos réplicas pueden vender la misma entrada y converger a un estado con dos ventas.

## Referencias

PDF 30–32 · impresas 226–228 · figura 6-11. Enlaces: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=30|PDF 30 · impresa 226]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=31|PDF 31 · impresa 227 · figura 6-11]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=32|PDF 32 · impresa 228]]. El ejemplo `ice` → `nice!` es del libro; el carrito es adaptación de la figura 6-10; las tablas de lápidas y contadores, el caso `ice?!`, `ixe` y la cuenta bancaria son propios.

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/09 Conflictos LWW siblings y reglas del dominio|Conflictos, LWW, siblings y reglas del dominio]] · **Índice:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Replicación]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/11 Sin líder reparación y cuórums|Sin líder, reparación y cuórums]]
