---
title: "Database Internals — Aislamiento, anomalías y serialización"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/transacciones
  - arquitectura/concurrencia
---

# Aislamiento, anomalías y serialización

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Capítulo 5]]

Una base de datos necesita ejecutar muchas transacciones a la vez. Si obligara a que cada operación esperara a que terminase la anterior, desaprovecharía CPU, memoria y tiempos de espera de disco. El problema aparece cuando esas transacciones leen y modifican datos relacionados: una decisión correcta con la información inicial puede dejar de ser correcta cuando otra transacción cambia esa información.

El **aislamiento** define qué cambios puede ver una transacción y cómo se permite que su ejecución se mezcle con las demás. La meta fuerte es que el trabajo concurrente tenga el mismo significado que alguna ejecución de una transacción después de otra. No exige ejecutar físicamente de esa manera.

Esta nota explica los conceptos del capítulo con ejemplos desarrollados para estudiar. El ejemplo de las dos cuentas reproduce las cantidades del libro; los otros ejemplos y el análisis de sus dependencias son elaboración propia.

## Una historia de ejecución es una lista de acciones

Una **historia de ejecución** o *schedule* recoge las acciones que interactúan con la base: leer, escribir, confirmar y abortar. La lógica de aplicación importa por los valores que produce y las decisiones que toma, pero para analizar la concurrencia resumimos esa lógica en las acciones sobre los datos.

Usaremos `R1(x)` para una lectura de `x` por T1, `W1(x=120)` para su escritura y `C1` para su confirmación. El orden de una misma transacción debe conservar su significado: no se puede escribir un resultado calculado antes de haber leído sus entradas.

Supongamos `saldo=100`:

- T1 añade 20 al saldo.
- T2 multiplica el saldo por 2.

Las dos historias seriales dan resultados diferentes, pero ambas respetan la lógica de las transacciones:

| Orden serial | Cálculo | Resultado |
|---|---|---:|
| T1 → T2 | `(100 + 20) × 2` | 240 |
| T2 → T1 | `(100 × 2) + 20` | 220 |

La corrección concurrente no significa escoger siempre 240. Significa que la ejecución corresponda a algún orden serial válido, incluidos los valores que las transacciones observaron y las decisiones que tomaron.

Una ejecución **serial** no intercala acciones de transacciones distintas. Una ejecución **serializable** puede intercalarlas, pero mantiene la equivalencia con una historia serial. Tres transacciones admiten `3! = 6` órdenes seriales candidatos. Las dependencias reales pueden descartar algunos de ellos.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/06-serializacion.png]]

Las barras que se superponen representan transacciones activas al mismo tiempo. A su lado aparecen los seis órdenes posibles de T1, T2 y T3. La figura recrea el planteamiento de la figura 5-4: la concurrencia debe poder justificarse mediante algún orden equivalente. La simple superposición de las barras no demuestra que todos esos órdenes sean compatibles con las lecturas y escrituras concretas.

**Referencia:** PDF 16–17 · impresas 94–95 · figura 5-4. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=16|Fuente del capítulo]].

## Las anomalías de lectura

Una **anomalía** es un patrón de intercalado que permite observaciones o resultados incompatibles con la garantía que buscamos. El capítulo separa tres anomalías clásicas de lectura.

### Lectura sucia: usar un cambio que todavía puede desaparecer

T1 cambia `saldo` de 100 a 900, pero aún no confirma. T2 lee 900. Después, T1 aborta y la base restaura 100.

El problema no es que T2 haya leído un valor antiguo: leyó un valor que nunca llegó a pertenecer al estado confirmado. Si T2 utilizó 900 para conceder un crédito o producir otro resultado, deshacer T1 por sí solo no corrige esa decisión. El aislamiento debe impedir esa dependencia o hacerse cargo de sus consecuencias.

La atomicidad dice que T1 se aplica completa o se deshace. El aislamiento añade que las transacciones vecinas no deberían tomar decisiones con un fragmento provisional de T1 cuando el nivel elegido prohíbe lecturas sucias.

### Lectura no repetible: la misma fila cambia entre consultas

T1 lee `saldo=100`. T2 actualiza esa fila a 150 y confirma. T1 vuelve a leer la misma fila y obtiene 150.

Ambos valores estuvieron confirmados cuando se leyeron; no hay lectura sucia. El problema es que T1 no dispone de una visión estable durante toda su ejecución. Una comprobación inicial puede dejar de representar la información que encontrará más adelante.

La repetibilidad pertenece a la **transacción**, no a la sesión completa. Que una transacción nueva vea un cambio confirmado después de terminar la anterior es comportamiento normal.

### Lectura fantasma: cambia el conjunto que satisface una condición

T1 consulta `pedidos WHERE importe >= 100` y obtiene tres filas. T2 inserta un pedido de 120 y confirma. T1 repite la consulta y obtiene cuatro filas.

Las tres filas originales pueden conservar exactamente sus valores. Cambió la pertenencia al conjunto consultado. Por eso proteger solamente las filas que existían al ejecutar la primera consulta puede ser insuficiente: la cuarta fila todavía no existía.

Una eliminación o una actualización que haga entrar o salir una fila del predicado también puede producir este tipo de cambio. El centro del problema es la **condición de búsqueda**, no únicamente un identificador concreto.

**Referencia:** PDF 17–18 · impresas 95–96. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=17|Anomalías de lectura]].

## Las anomalías de escritura

### Actualización perdida: sobrescribir una decisión basada en un valor viejo

Con `contador=10`, T1 y T2 leen 10. Ambas calculan `10+1=11`. T1 escribe 11 y confirma; T2 escribe su propio 11 y confirma.

Hubo dos incrementos aceptados, pero el resultado final es 11. En cualquier ejecución serial de esos incrementos, la segunda transacción leería 11 y produciría 12. La escritura de T2 borró el efecto lógico de T1.

El patrón concreto es **leer → calcular → escribir**, con ambas transacciones usando la misma entrada vieja. Una operación de incremento que el motor ejecuta de forma coordinada puede evitarlo, pero no debemos suponer que una secuencia de aplicación tiene la misma garantía por parecer equivalente.

### Escritura sucia: modificar un estado que otra transacción aún no confirmó

T1 escribe provisionalmente `x=20`; T2 sobrescribe ese mismo dato con `x=30` antes de que T1 termine. Si T1 aborta, una restauración ingenua de su valor anterior podría borrar el trabajo de T2. Las escrituras superpuestas complican qué estado debe conservar la recuperación.

> [!note] Precisión respecto al texto
> En la impresa 96, el libro presenta *dirty write* como una modificación basada en un valor leído sin confirmar. Eso describe una dependencia sucia que desemboca en escritura. Para distinguir los mecanismos, aquí también usamos el caso directo de sobrescribir una escritura no confirmada; no hace falta que T2 haya leído ese valor para que dos escrituras provisionales sobre el mismo dato requieran coordinación.

### Write skew: decisiones coherentes por separado que rompen una regla conjunta

La **desviación de escritura** o *write skew* ocurre cuando dos transacciones leen información relacionada, modifican registros diferentes y la combinación de sus decisiones viola una regla que ambas comprobaron.

El ejemplo del libro permite saldos individuales negativos, pero exige:

`A + B >= 0`

El estado inicial es `A=100` y `B=150`, de modo que el total es 250. T1 quiere retirar 200 de A y T2 retirar 200 de B.

| Comprobación | Estado que calcula la transacción | Total |
|---|---|---:|
| T1, usando el B inicial | `A=100−200=−100`, `B=150` | 50 |
| T2, usando el A inicial | `A=100`, `B=150−200=−50` | 50 |
| Ambas confirmadas | `A=−100`, `B=−50` | −150 |

Cada transacción cree dejar un total de 50. Las dos juntas retiran 400 de un total de 250. No hay una fila en la que una escritura reemplace a la otra: T1 escribe A y T2 escribe B. Se rompió la relación entre ambas filas.

En un orden serial T1 → T2, T2 vería `A=−100` y `B=150`, total 50. Su retirada adicional produciría −150, así que tendría que rechazarla. En T2 → T1 sucede lo mismo al intercambiar los papeles. Por tanto, aceptar ambas retiradas no corresponde a ningún orden serial que ejecute la comprobación correctamente.

El siguiente ejemplo es elaboración propia del mismo patrón. Un hospital exige que al menos una persona permanezca de guardia. Ana y Bruno están disponibles al comienzo. Ana consulta la disponibilidad de Bruno y solicita salir; Bruno consulta la disponibilidad de Ana en el mismo estado inicial y también solicita salir. Cada transacción modifica únicamente la fila de quien sale. Las dos decisiones dejan cero personas de guardia.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/07-write-skew.png]]

Las dos ramas de la figura parten del snapshot con Ana y Bruno disponibles. Cada rama mantiene la condición individualmente porque supone que la otra persona seguirá disponible. La combinación confirma dos filas distintas y reduce las guardias a cero. Es la misma dependencia circular del ejemplo de las cuentas: cada decisión presupone que el dato que cambia la otra transacción seguirá igual.

**Referencia:** PDF 18 · impresa 96. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=18|Anomalías de escritura y ejemplo de las cuentas]].

## Qué garantizan los niveles de aislamiento del capítulo

El libro presenta la clasificación clásica mediante las tres anomalías de lectura. “Permitida” significa que el nivel no la excluye, no que toda ejecución la produzca.

| Nivel | Lectura sucia | Lectura no repetible | Fantasma |
|---|---|---|---|
| Read uncommitted | Permitida | Permitida | Permitida |
| Read committed | Excluida | Permitida | Permitida |
| Repeatable read | Excluida | Excluida | Permitida |
| Serializable | Excluida | Excluida | Excluida |

**Read committed** permite que dos consultas dentro de una transacción observen distintos estados confirmados. **Repeatable read** añade estabilidad para las filas leídas en esta clasificación. **Serializable** pide una ejecución equivalente a alguna historia serial.

La tabla de la figura 5-5 no es un catálogo de todas las anomalías posibles. En particular, que una estrategia mantenga lecturas estables no basta para concluir que evita *write skew*. La garantía completa de serialización se refiere a las dependencias de la ejecución, incluidas las comprobaciones sobre conjuntos de filas.

Como criterio de estudio, conviene separar tres preguntas: qué estado puede leer una transacción, qué escrituras concurrentes pueden confirmar y qué invariantes debe proteger la aplicación. Los nombres de niveles sirven para orientar esas preguntas; el capítulo no analiza las variantes de productos concretos.

**Referencia:** PDF 18–19 · impresas 96–97 · figura 5-5. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=19|Tabla de niveles de aislamiento]].

## Snapshot isolation proporciona una vista estable, pero admite write skew

Un **snapshot** es una vista de los datos correspondiente a un momento lógico. En *snapshot isolation*, tal como lo describe el libro, una transacción ve los cambios confirmados antes de su inicio y usa esa misma vista durante su ejecución. Las escrituras que otras transacciones confirmen después no alteran su snapshot.

Para confirmar, además se comprueba que los datos que la transacción modificó no hayan sido modificados por una transacción concurrente desde su snapshot. Si dos transacciones concurrentes intentan modificar el mismo dato, no se permite que ambas confirmen sus versiones basadas en aquel estado inicial.

Eso evita la actualización perdida del contador: ambas transacciones quieren escribir la misma fila, por lo que una debe abortar y volver a calcular. En cambio, el ejemplo de las cuentas modifica filas diferentes. La comprobación de conflictos de escritura puede aprobar ambas retiradas aunque la regla `A+B>=0` quede rota.

**Vista estable + ausencia de conflictos escritura/escritura no implica serialización.** Para obtener serialización hay que controlar también dependencias entre lo que una transacción leyó y lo que otra escribió. En las cuentas, T1 decidió con el B viejo mientras T2 lo cambiaba; T2 decidió con el A viejo mientras T1 lo cambiaba.

**Referencia:** PDF 19 · impresa 97. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=19|Snapshot isolation y write skew]].

## Cómo conectarlo con ACID

La **consistencia** se expresa mediante reglas: por ejemplo, el total de ambas cuentas debe ser no negativo. El motor puede comprobar ciertas restricciones declaradas, pero una regla de negocio no se cumple por el mero hecho de utilizar transacciones. Las acciones de la aplicación y el aislamiento deben permitir que esa comprobación sea válida bajo concurrencia.

La **atomicidad** evita dejar media transacción aplicada. La **durabilidad** evita perder sus efectos después de confirmar. Ninguna de ellas convierte las dos retiradas concurrentes en una ejecución correcta: ambas podrían aplicarse completas, persistir perfectamente y aun así violar la regla conjunta. Aquí hace falta aislamiento suficiente.

Como ampliación conceptual de las notas, la **serialización** tampoco fija por sí sola un orden de tiempo real entre todas las operaciones. El capítulo la diferencia de la **linealizabilidad**, tratada más adelante en el libro. Para este capítulo basta retener que serializar significa encontrar una historia serial equivalente; no significa que todos los usuarios deban compartir un reloj físico ni que las transacciones se ejecuten sin superposición.

> [!question]- Si un resultado concurrente coincide numéricamente con un resultado serial, ¿ya está demostrado el aislamiento?
> No. También importan las lecturas observadas y las decisiones que tomaron las transacciones. Una coincidencia accidental del valor final no demuestra equivalencia de la historia.

> [!question]- ¿Por qué proteger las filas leídas no siempre impide fantasmas?
> Porque otra transacción puede crear una nueva fila que satisface la condición. La protección debe cubrir el predicado o el rango pertinente, o una estrategia que controle esa dependencia.

> [!question]- ¿Qué distingue actualización perdida y write skew?
> La actualización perdida suele implicar dos escrituras basadas en un estado viejo sobre el mismo dato. En write skew las escrituras pueden ser sobre datos diferentes, pero sus decisiones dependen de una regla conjunta.

> [!question]- En las cuentas, ¿cuál es el saldo mínimo que necesita comprobar la segunda retirada en un orden serial?
> Tras una retirada, el total queda en 50. La segunda quiere restar 200, lo que dejaría −150. Tiene que rechazar esa retirada; comprobar únicamente su saldo individual no representa la regla del ejemplo.

---

← [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/05 Políticas steal force y recuperación ARIES|Steal, force y recuperación ARIES]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/07 Control optimista multiversión y orden temporal|Control optimista y multiversión]] →
