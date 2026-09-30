---
title: "Database Internals — Control optimista, multiversión y orden temporal"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/concurrencia
  - arquitectura/transacciones
---

# Control optimista, multiversión y orden temporal

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Capítulo 5]]

Un nivel de aislamiento describe una garantía. Un **mecanismo de control de concurrencia** es la estrategia con la que el motor intenta cumplirla. El libro presenta estrategias optimistas, pesimistas, versiones múltiples, ordenación temporal y bloqueos. Estas categorías responden a preguntas distintas y pueden combinarse.

- **Optimista o pesimista:** ¿se permite avanzar y se comprueba después, o se resuelve el conflicto mientras se ejecuta?
- **Una o varias versiones:** ¿hay un único valor accesible o se conservan estados anteriores para distintos lectores?
- **Bloqueos u orden temporal:** ¿se reserva el acceso mediante locks o se autorizan las operaciones según sus marcas lógicas?

No conviene equiparar MVCC con “optimista”, ni pesimista con “usa locks”. El capítulo muestra precisamente que MVCC admite varios protocolos y que la ordenación temporal puede ser pesimista sin usar locks transaccionales.

Los mecanismos proceden del capítulo; las cronologías numéricas y la descomposición de costes son elaboraciones propias para hacer explícitas sus causas.

## Control optimista: trabajar primero y comprobar antes de publicar

El **control optimista de concurrencia**, u OCC por *optimistic concurrency control*, supone que los conflictos son suficientemente infrecuentes como para compensar una apuesta: dejar que varias transacciones hagan trabajo privado y rechazar al final las que no puedan publicarse de forma segura.

### 1. Fase de lectura y ejecución privada

La transacción lee datos y calcula sus resultados en un **contexto privado**. Sus cambios pendientes todavía no son visibles a las demás. Aunque se llame fase de lectura, también contiene lógica de negocio y la preparación de escrituras.

El motor registra dos conjuntos:

- **Read set `R(T)`:** datos que T leyó y de los que dependen sus decisiones.
- **Write set `W(T)`:** datos que T pretende modificar.

Una transferencia de 30 entre cuentas A y B puede tener `R(T)={A,B}` y `W(T)={A,B}`. Una operación que comprueba el límite L y cambia únicamente A puede tener `R(T)={A,L}` y `W(T)={A}`. La diferencia importa: otra transacción podría cambiar L sin tocar ninguna escritura de T, invalidando la comprobación de T.

En operaciones sobre conjuntos, también importa cómo representar las lecturas de rangos o predicados. Como ampliación didáctica: si una consulta dependía de que “no existe ningún registro con esta condición”, guardar únicamente identificadores de filas que sí aparecieron no representa toda su dependencia.

### 2. Fase de validación

Antes de confirmar, el motor comprueba si los cambios concurrentes invalidaron las lecturas, causan sobrescrituras indebidas o forman dependencias incompatibles con el orden de ejecución que el protocolo pretende imponer.

Ejemplo: T1 lee `stock=10` para vender 8 unidades y calcula `stock=2`. Mientras trabaja, T2 vende 4 y confirma `stock=6`. Si T1 publicara su cálculo viejo, aceptaría vender 12 unidades a partir de 10 y además dejaría un stock incorrecto de 2. La validación debe detectar el cambio pertinente, descartar el contexto privado de T1 y hacer que una ejecución nueva consulte el stock actualizado.

Un **reintento** no consiste en reenviar sin cambios el resultado viejo. Debe repetir las lecturas y decisiones con un estado que pueda validar. Con `stock=6`, la venta de 8 ya no pasa la comprobación.

### 3. Fase de escritura

Si valida correctamente, T publica su write set. La validación y la publicación tienen que coordinarse: no puede abrirse una ventana en la que T valide, otra transacción cambie las entradas pertinentes y T publique un resultado que ya dejó de ser válido.

El capítulo presenta una sección crítica que agrupa validación y escritura: mientras una transacción valida, otra no debe confirmar cambios que rompan esa validación. **OCC conserva coordinación**, aunque concentre una parte del trabajo compartido en una fase relativamente corta.

Esquema didáctico del caso del stock:

| Momento | T1 | T2 | Estado publicado |
|---|---|---|---:|
| 1 | Lee 10, prepara vender 8 | — | 10 |
| 2 | Sigue en contexto privado | Lee 10, prepara vender 4 | 10 |
| 3 | — | Valida y confirma | 6 |
| 4 | Detecta lectura invalidada, aborta | — | 6 |
| 5 | Reintenta y rechaza vender 8 | — | 6 |

**Referencia:** PDF 20–21 · impresas 98–99. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=20|Las fases del control optimista]].

## Validación hacia atrás y hacia delante

La **validación hacia atrás** compara una transacción con transacciones que ya confirmaron y pudieron cambiar datos durante su fase de lectura. La **validación hacia delante** considera conflictos con trabajo concurrente aún en curso según el protocolo. El capítulo introduce ambas orientaciones sin desarrollar aquí un algoritmo completo para cada variante.

Para entender una validación hacia atrás, supongamos que se intenta colocar T1 antes que T2:

1. Si T1 terminó antes de que T2 comenzara a leer, no se solapan de esa manera: T2 puede haber observado ya los resultados de T1.
2. Si T1 confirma mientras T2 lee, una escritura de T1 sobre un dato leído por T2 puede volver vieja una entrada de T2. Por eso se revisa la intersección pertinente entre `W(T1)` y `R(T2)`.
3. Si algunas fases siguen superpuestas, el protocolo debe controlar además los conflictos con escrituras que todavía pueden publicarse. No basta con revisar únicamente la misma fila de salida.

Un conflicto obliga a rechazar, esperar o establecer otro orden válido según el algoritmo utilizado. Una coincidencia entre conjuntos es una herramienta para detectar dependencias; no toda coincidencia implica por sí misma una anomalía en todos los protocolos.

> [!note] Una fórmula del escaneo no debe usarse como algoritmo completo
> El tercer punto de la impresa 98 escribe una condición entre `W(T2)` y los conjuntos de T1, mientras los puntos previos razonan sobre escrituras de T1 que invalidan lecturas de T2. El pasaje mezcla condiciones de solapamiento y no especifica todas las fases necesarias para convertirlas en una implementación verificable. Estas notas explican las dependencias y no presentan esas tres frases como una receta ejecutable universal. Si se implementa OCC, hay que definir explícitamente el orden de validación y los intervalos de lectura, validación y publicación.

## Cuándo compensa apostar por OCC

Si dos transacciones leen y modifican datos independientes, ambas pueden validar. Si una fila concentra casi todas las escrituras, muchas transacciones pueden invertir trabajo para luego abortar. La **contención** es la competencia simultánea por un mismo recurso o dependencia; OCC la convierte con frecuencia en trabajo descartado.

Como cálculo propio, supongamos que cada intento cuesta 5 ms y un intento tiene probabilidad de éxito `p`, constante e independiente para simplificar. El número esperado de intentos por éxito es `1/p`:

| Éxito por intento | Intentos esperados | Trabajo esperado por éxito |
|---:|---:|---:|
| 0,90 | 1,11 | 5,56 ms |
| 0,50 | 2 | 10 ms |
| 0,10 | 10 | 50 ms |

Esto no predice la latencia de un motor real: omite colas, pausas y la dependencia entre reintentos. Sí muestra por qué los abortos pueden anular la ventaja de permitir ejecución libre. Tampoco implica que los locks ganen siempre bajo contención; cambiar el protocolo desplaza el coste hacia esperas, gestión de locks y posibles deadlocks.

**Referencia conceptual:** PDF 21 · impresa 99. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=21|Coste de reintentos y sección crítica]].

## MVCC: conservar versiones para elegir qué valor ve cada transacción

**MVCC**, *multiversion concurrency control*, conserva varias versiones de un registro y asocia su visibilidad a identificadores de transacción o marcas lógicas. Un lector puede continuar usando una versión anterior mientras otro prepara o confirma una versión nueva.

Imaginemos una fila con estas versiones confirmadas:

| Versión | Momento lógico de confirmación | Valor |
|---|---:|---:|
| V1 | 10 | 100 |
| V2 | 20 | 130 |
| V3 | 30 | 160 |

Una transacción con snapshot 15 ve 100; otra con snapshot 25 ve 130. Una transacción que comienza después de 30 ve 160. El “valor actual” para un lector depende de su regla de visibilidad, no solo de cuál versión se escribió más recientemente.

El capítulo distingue **versiones confirmadas** y **versiones sin confirmar**. La versión más reciente confirmada es la actual en el estado publicado, pero no necesariamente la visible para un snapshot antiguo. Las versiones pendientes pueden tener lectores permitidos o prohibidos según el nivel de aislamiento.

El texto plantea como objetivo general limitar el trabajo no confirmado por valor. Es una simplificación de su exposición, no una definición universal que imponga exactamente una sola versión pendiente en cualquier implementación de MVCC.

El beneficio central es desacoplar a lectores y escritores: el escritor no tiene que destruir inmediatamente el valor que un lector anterior necesita. El coste, como ampliación del razonamiento, es mantener metadatos y conservar versiones mientras puedan ser necesarias. Eliminar demasiado pronto una versión rompería la vista de un lector activo; conservarlas todas indefinidamente agotaría espacio.

### MVCC y snapshot isolation responden a preguntas distintas

MVCC explica **cómo representar varios estados disponibles**. Snapshot isolation explica **qué vista usa una transacción y qué conflictos impiden confirmar**. MVCC puede servir para construir snapshot isolation, pero tener versiones no define por sí solo las garantías del nivel de aislamiento.

También puede combinarse con locks, orden temporal y otros controles de conflictos. Y ninguna versión antigua protege por sí misma un cambio físico concurrente de los bytes de una página: esa protección mediante latches se estudia en [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/09 Latches y concurrencia en B-Trees|la nota de concurrencia en B-Trees]].

**Referencia:** PDF 21 · impresa 99. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=21|Control de concurrencia multiversión]].

## Orden temporal: autorizar operaciones según un orden lógico

Una estrategia **pesimista** resuelve conflictos mientras las operaciones se ejecutan. Puede bloquear o abortar antes de que la transacción complete todo su trabajo. El libro presenta **timestamp ordering**, u ordenación por marcas temporales, como ejemplo que no necesita locks transaccionales.

Cada transacción obtiene una marca `TS(T)`. No hace falta interpretarla como una hora del calendario: basta que represente el orden lógico relevante. Para un dato `x`, se mantienen:

- `RTS(x)`: la marca máxima de una transacción que ya lo leyó.
- `WTS(x)`: la marca máxima de una transacción que ya lo escribió.

La idea es permitir acciones compatibles con ese orden y rechazar las que necesitarían aparecer retrospectivamente antes de una acción que ya ocurrió.

### Leer una escritura demasiado nueva

Si `TS(T)=10` y `WTS(x)=20`, T intenta leer un dato cuya versión actual proviene de una transacción que debería ir después de ella en el orden elegido. En el esquema de una versión descrito por el libro, se aborta T.

Esto contrasta con una estrategia multiversión: si existe una versión visible anterior, un protocolo MVCC puede tener otra forma de resolver la lectura. Aquí estamos explicando la regla del esquema temporal presentado, no toda lectura posible en cualquier motor.

### Escribir después de una lectura que debería ir después

Si `TS(T)=10` y `RTS(x)=20`, una transacción más nueva ya leyó x. Dejar que T coloque ahora una escritura que debería preceder a esa lectura rompería el orden: la transacción 20 no habría leído el estado que le correspondía. La operación provoca aborto según este esquema.

### Regla de escritura de Thomas: omitir una escritura obsoleta

Si una escritura supera la comprobación anterior, pero `TS(T)<WTS(x)`, ya existe una escritura que va después en el orden lógico. La **regla de Thomas** permite ignorar la escritura atrasada en lugar de reemplazar el valor nuevo con uno viejo.

Por ejemplo, `RTS(x)=5`, `WTS(x)=20` y T con marca 10 intenta escribir 90. No viola la condición de lectura (`10>=5`), pero su escritura quedó superada por la de marca 20. Se omite la operación; no se publica 90 encima del valor más nuevo.

La secuencia de comprobaciones importa. Si `RTS(x)=25`, la misma T10 debe abortar por la lectura incompatible; no puede invocar Thomas para saltarse primero esa comprobación.

Al aceptar lecturas y escrituras, se actualizan sus máximos pertinentes. Una transacción abortada por su marca obtiene una nueva marca al reiniciar en el esquema del texto; repetir exactamente la marca que ya quedó detrás puede repetir el mismo rechazo. Esta política pertenece a timestamp ordering y no debe confundirse con las prioridades usadas para prevenir deadlocks mediante locks.

**Referencia:** PDF 21–22 · impresas 99–100. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=22|Orden temporal y regla de Thomas]].

## Un mapa para comparar las estrategias

| Estrategia | Dónde resuelve el problema principal | Coste característico |
|---|---|---|
| OCC | Validación antes de publicar trabajo privado | Trabajo descartado y reintentos |
| MVCC | Selección y conservación de versiones visibles | Versiones y metadatos adicionales |
| Timestamp ordering | Autorización de cada operación según su marca | Abortos por orden incompatible |
| Locks transaccionales | Reservas de acceso a claves o rangos | Esperas, contención y deadlocks |

La comparación no declara un ganador: el protocolo tiene que proteger las dependencias exigidas por el aislamiento y funcionar con el patrón de acceso de la carga. Dos aplicaciones con el mismo volumen total pueden comportarse muy diferente si una distribuye sus operaciones y la otra concentra todo en una fila.

> [!question]- ¿Por qué una transacción OCC no puede validar y luego publicar sin coordinación?
> Porque otra transacción puede cambiar entre ambas fases los datos que hicieron válida la comprobación. La publicación debe corresponder al estado validado.

> [!question]- Si MVCC permite leer versiones antiguas, ¿siempre evita write skew?
> No. Dos transacciones pueden ver un snapshot coherente y modificar filas distintas de manera que violen una regla conjunta. Se necesita control adicional de dependencias para garantizar serialización.

> [!question]- ¿Qué pasa con una lectura de T15 si `WTS(x)=22` en el esquema temporal de una versión?
> T15 se aborta: la versión actual pertenece a una escritura que debería ejecutarse después de T15 en el orden elegido.

> [!question]- ¿Qué pasa con una escritura T15 si `RTS(x)=12` y `WTS(x)=22` bajo Thomas?
> Supera la comprobación de lecturas porque `15>=12`, pero su escritura está superada por la de marca 22. Se ignora esa escritura obsoleta.

---

← [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/06 Aislamiento anomalías y serialización|Aislamiento y anomalías]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/08 Bloqueos transaccionales y deadlocks|Bloqueos transaccionales y deadlocks]] →
