---
title: "Database Internals — Bloqueos transaccionales y deadlocks"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/concurrencia
  - arquitectura/transacciones
---

# Bloqueos transaccionales y deadlocks

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Capítulo 5]]

Un **lock transaccional** es una reserva de acceso a un dato lógico de la base. El gestor de locks decide si puede concederla inmediatamente o si el solicitante debe esperar. La finalidad es que las transacciones no se interfieran de maneras incompatibles con el aislamiento requerido.

La reserva puede cubrir una clave, una clave que aún no existe o un rango de claves. Esto último importa para consultas con predicados: reservar solamente las filas existentes no impediría que otra transacción insertase una nueva fila dentro de un rango cuya estabilidad es necesaria.

Esta nota sigue los mecanismos del capítulo. Los ejemplos paso a paso, el orden fijo de adquisición y la distinción con 2PL estricto amplían la explicación para evitar interpretaciones demasiado generales.

## Qué protege un lock y qué protege un latch

El capítulo distingue dos capas de protección:

| Pregunta | Lock transaccional | Latch |
|---|---|---|
| ¿Qué protege? | Datos y dependencias lógicas entre transacciones | Bytes, punteros y estructura física |
| Unidad típica del capítulo | Clave o rango de claves | Página del árbol |
| Quién lo gestiona | Gestor de locks del DBMS | Código de acceso a la estructura |
| Duración | Vinculada al protocolo de la transacción | Mientras una operación física necesita protección |
| Esperas circulares | Gestor puede detectar o prevenir deadlocks | El algoritmo debe evitar patrones peligrosos |

Supongamos que una transacción está modificando el saldo de la cuenta 42. Puede necesitar un lock lógico sobre esa cuenta mientras decide y confirma. Para escribir los bytes del registro también puede tomar brevemente un latch sobre la página que lo contiene. Suelta el latch cuando termina esa modificación física, aunque el lock lógico todavía deba conservarse.

Si otra transacción actualiza la cuenta 43 en la misma página, sus datos lógicos pueden ser independientes, pero ambas modificaciones de la página requieren coordinación física. Por eso una base con MVCC o sin locks transaccionales no queda automáticamente libre de latches.

La palabra *lock* también se usa para primitivas de programación que cumplen la función que este capítulo llama *latch*. La distinción se basa en la finalidad y duración, no en el nombre de una clase de código.

**Referencia:** PDF 24–25 · impresas 102–103. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=24|Locks y latches]].

## Two-phase locking: adquirir primero, liberar después

**Two-phase locking**, abreviado **2PL**, divide la gestión de locks de cada transacción en dos fases:

1. **Crecimiento:** puede adquirir locks, pero no liberar ninguno.
2. **Decrecimiento:** puede liberar locks, pero ya no adquirir nuevos.

El límite entre fases lo marca la primera liberación. No significa que todos los locks tengan que adquirirse al principio, antes de cualquier lectura. La transacción puede adquirirlos a medida que encuentra los datos que necesita, siempre que todavía no haya empezado a liberarlos.

Ejemplo de una transferencia A → B:

| Paso | Acción | Fase |
|---:|---|---|
| 1 | Adquiere lock sobre A | Crecimiento |
| 2 | Lee A y calcula su saldo nuevo | Crecimiento |
| 3 | Adquiere lock sobre B | Crecimiento |
| 4 | Escribe los cambios de A y B | Crecimiento |
| 5 | Libera lock sobre A | Comienza decrecimiento |
| 6 | Libera lock sobre B | Decrecimiento |

Después del paso 5 no puede solicitar un nuevo lock sobre C. Si C iba a ser necesario, tuvo que adquirirlo antes de comenzar a liberar.

El punto en el que una transacción obtiene su último lock ayuda a ordenar las transacciones: en el protocolo estándar, 2PL con locks que cubren los conflictos pertinentes produce historias serializables por conflictos. La garantía depende de que se protejan realmente los accesos necesarios, incluidos rangos cuando corresponda. Aplicar la regla a un subconjunto de dependencias no prueba el aislamiento completo de la aplicación.

### 2PL básico, estricto y conservador

El capítulo desarrolla las dos fases y menciona la variante conservadora. Como precisión propia, conviene distinguir tres ideas:

| Variante | Regla adicional | Consecuencia |
|---|---|---|
| 2PL básico | Una vez liberado un lock, no se adquieren otros | Controla el orden de conflictos, pero puede liberar antes del final |
| 2PL estricto | Conserva los locks exclusivos hasta confirmar o abortar | Impide que otros dependan de escrituras provisionales protegidas |
| 2PL conservador | Reserva todos los locks necesarios antes de ejecutar | Evita espera circular si no retiene una parte mientras espera por el resto |

La impresa 102 caracteriza los locks como mantenidos durante la transacción. Esa descripción corresponde a prácticas o variantes que los retienen hasta su final; **no se deduce de las dos reglas del 2PL básico**. Es útil separar serialización de la seguridad de exponer estados no confirmados.

El coste del 2PL conservador es que hay que conocer por adelantado el conjunto de locks. Puede ser difícil cuando una lectura determina qué otras filas se consultarán. Además puede reservar recursos que todavía no utiliza y reducir la concurrencia.

### 2PL y 2PC resuelven problemas diferentes

**2PL** gestiona cuándo se adquieren y liberan locks para controlar concurrencia. **Two-phase commit**, o **2PC**, coordina la decisión de confirmar o abortar una transacción entre participantes, tema de capítulos posteriores. Tener dos fases y siglas parecidas no los convierte en el mismo protocolo.

**Referencia:** PDF 22–23 · impresas 100–101. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=22|2PL y diferencia con 2PC]].

## Cómo aparece un deadlock

Un **deadlock** o interbloqueo es una espera circular: las transacciones implicadas conservan recursos que otra necesita y ninguna puede avanzar hasta que la otra libere los suyos.

La figura 5-6 usa dos transacciones y dos locks:

1. T1 adquiere L1.
2. T2 adquiere L2.
3. T1 solicita L2 y espera a T2.
4. T2 solicita L1 y espera a T1.

Esperar un lock no es siempre un deadlock. Si T2 pudiera terminar y liberar L2 sin necesitar nada de T1, la espera de T1 sería una cola normal. Aquí T2 también necesita un recurso retenido por T1, cerrando el ciclo.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/08-deadlock.png]]

Las flechas rojas de espera van de la transacción detenida hacia la transacción que posee el recurso que necesita. La recreación llama A y B a los recursos L1 y L2 del libro: T1 mantiene A mientras espera B, y T2 mantiene B mientras espera A. Las dos flechas forman un ciclo. El recuadro inferior explica que abortar una transacción libera sus locks y permite que la otra continúe.

2PL no excluye este escenario: ambas transacciones todavía están creciendo, han adquirido un lock y aún no han liberado ninguno. La regla que consigue serialización puede coexistir con esperas circulares.

**Referencia:** PDF 23 · impresa 101 · figura 5-6. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=23|Ejemplo de deadlock]].

## Detectar el ciclo y elegir una víctima

Un **grafo de espera** o *waits-for graph* tiene transacciones como nodos y una arista `T1 → T2` si T1 espera un lock que retiene T2. En el modelo de locks de este capítulo, un ciclo indica un deadlock.

El ciclo puede contener más de dos transacciones: `T1 → T2 → T3 → T1`. No basta con buscar parejas que se esperen mutuamente. Un gestor puede revisar el grafo periódicamente o al actualizar las relaciones de espera.

Detectar es solo la primera parte. Después se aborta alguna transacción implicada para romper el ciclo y se deshacen sus cambios según el sistema de recuperación. El libro menciona como elección habitual la transacción que intentó adquirir el lock más recientemente; no es una regla obligatoria de todos los gestores.

Como ampliación, una política puede tener en cuenta cuánto trabajo se perdería o cuántos locks se liberan. La víctima tiene que poder reintentarse sin suponer que las lecturas anteriores siguen siendo válidas. El aborto es un resultado previsto del protocolo de concurrencia, no necesariamente un fallo del programa.

Un **timeout** aborta una transacción que espera demasiado, suponiendo que podría estar interbloqueada. Es sencillo, pero no demuestra la existencia de un ciclo: también puede abortar una espera larga que habría terminado normalmente. Un umbral demasiado corto desperdicia trabajo; uno muy largo tarda en resolver un deadlock real.

**Referencia:** PDF 23 · impresa 101. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=23|Timeouts y detección mediante grafo de espera]].

## Prevenir ciclos con prioridades

El capítulo presenta dos políticas basadas en la antigüedad de las transacciones. Una marca menor representa una transacción más antigua y con mayor prioridad. Supongamos que **O** es antigua y **J** es joven.

| Situación | Wait-die | Wound-wait |
|---|---|---|
| O pide un lock retenido por J | O espera | Se aborta J para permitir avanzar a O |
| J pide un lock retenido por O | Se aborta J | J espera |

### Wait-die: la antigua puede esperar a la joven

Con O de marca 10 y J de marca 20, O puede esperar por un lock de J. Si J solicita después uno retenido por O, J se aborta. No se permite que las esperas formen la dirección contraria.

Todas las aristas permitidas van de menor a mayor marca. Un ciclo requeriría volver a una marca menor, cosa que la política prohíbe. Ese orden estricto explica por qué evita la espera circular.

### Wound-wait: la antigua puede hacer abortar a la joven

Con las mismas marcas, si O necesita un lock de J, se aborta J. Si J necesita un lock de O, J espera. Las aristas de espera permitidas van de mayor a menor marca, así que tampoco pueden cerrar un ciclo.

“Wound” describe que la transacción antigua provoca el aborto de la joven. El nombre no dice que la transacción solicitante se aborte siempre: importa quién es antigua y quién posee el lock.

Estas políticas previenen ciclos restringiendo qué esperas son posibles. La detección, en cambio, permite inicialmente las esperas y resuelve los ciclos cuando aparecen. La elección afecta cuántas transacciones esperan y cuántas se abortan antes de hacer más trabajo.

Como ampliación, la antigüedad y el tratamiento de reintentos deben diseñarse para evitar que una transacción pierda siempre la prioridad y no progrese. No conviene copiar aquí la regla de “nuevo timestamp al reiniciar” de timestamp ordering: aquella regla resuelve otro tipo de conflicto y el capítulo no detalla la política de prioridad de todos los reintentos con locks.

**Referencia:** PDF 24 · impresa 102. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=24|Wait-die y wound-wait]].

## Evitar un ciclo con un orden fijo de adquisición

Otra herramienta conceptual, elaborada aquí, es adquirir recursos siempre en el mismo orden. Si todas las transferencias reservan primero la cuenta de identificador menor y después la mayor, dos transferencias entre las cuentas 10 y 20 no pueden conservar cada una una mitad opuesta de esos dos locks.

Una transacción adquiere 10 y después 20. La otra espera por 10 **antes de adquirir 20**. Cuando la primera termina, la segunda sigue. La espera no se convierte en el ciclo de la figura 5-6.

El razonamiento depende de respetar el orden en todos los caminos relevantes. Un tercer recurso, una consulta que descubre nuevas claves o una conversión de modos puede introducir otras dependencias si el diseño no lo contempla. El ejemplo explica el principio; no sustituye el gestor de deadlocks de una base completa.

> [!question]- ¿2PL garantiza que no haya deadlocks?
> No. Dos transacciones pueden adquirir locks diferentes durante crecimiento y esperar mutuamente por los que les faltan. La serialización y la ausencia de interbloqueo son propiedades distintas.

> [!question]- En wait-die, T10 solicita un lock de T20. ¿Quién se aborta?
> Nadie por esa solicitud: T10 es antigua y puede esperar. Si T20 pidiese un lock retenido por T10, se abortaría T20.

> [!question]- En wound-wait, T10 solicita un lock de T20. ¿Quién se aborta?
> T20, la poseedora joven. T10 la hace abortar para poder obtener el recurso.

> [!question]- ¿Por qué un lock de rango puede proteger algo que no existe todavía?
> Porque protege la condición o el espacio lógico donde aparecería una nueva clave. Evita que otra transacción cambie el conjunto sobre el que se tomó una decisión, cuando el protocolo necesita esa estabilidad.

---

← [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/07 Control optimista multiversión y orden temporal|Control optimista y multiversión]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/09 Latches y concurrencia en B-Trees|Latches y concurrencia en B-Trees]] →
