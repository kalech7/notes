---
title: "Database Internals — WAL, checkpoints y registros de recuperación"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/wal
---

# WAL, checkpoints y registros de recuperación

[[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|← Índice del capítulo 5]]

Cuando una transacción modifica una página en RAM, ese estado puede desaparecer con un fallo. El **write-ahead log**, WAL, es un registro persistente que permite reconstruir cambios sin tener que escribir de inmediato cada página de datos.

El WAL agrega registros al final: es **append-only**. Esto favorece escrituras secuenciales y permite reunir varios registros en un buffer. El buffer del log sigue siendo RAM; registrar algo allí todavía no demuestra durabilidad.

## Dos órdenes obligatorios

Cada registro lleva un **LSN**, *log sequence number*: una posición o identificador que crece dentro del log. Los números usados aquí son ejemplos didácticos, no offsets de un formato real.

1. **Antes de hacer durable una página modificada, debe estar durable el WAL que describe esos cambios.** Si una página contiene cambios hasta LSN 120, el log persistido debe cubrirlos antes de su flush.
2. **Antes de reconocer un commit con durabilidad, debe estar durable el log hasta su registro de commit.** No basta con persistir los registros de cambios si falta la evidencia de que la transacción terminó.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/04-wal-y-flush.png|1100]]

Las dos trayectorias separan el log de las páginas de datos. La barrera de persistencia del WAL precede a las escrituras de páginas que dependen de esos registros. El commit durable permite confirmar aunque los archivos de datos todavía estén atrasados; un flush posterior los pone al día. Las flechas expresan dependencias necesarias, no una obligación de escribir todas las páginas inmediatamente después de confirmar.

El escaneo dice en PDF 11, impresa 89, que el log debe llegar a disco antes de modificar los contenidos de las páginas. La regla precisa distingue **modificación en RAM** de **persistencia de la página**: se puede modificar el buffer y reunir registros en memoria, siempre que se respete el orden al hacerlos durables. Esta precisión coincide con la [documentación oficial de WAL de PostgreSQL](https://www.postgresql.org/docs/17/wal-intro.html).

## Una transferencia vista desde el log

| LSN | Registro didáctico | Qué evidencia aporta |
|---:|---|---|
| 100 | T1 inicia | Identidad de la unidad de trabajo |
| 110 | A: 100 → 70 | Cambio que debe poder repetirse o revertirse |
| 120 | B: 50 → 80 | Segundo cambio de la misma transacción |
| 130 | T1 commit | Decisión de conservar la transferencia |

Si 130 es durable y ninguna página de datos fue escrita, la transferencia sigue siendo recuperable. Si solo 110 y 120 son durables y el proceso cae antes de confirmar, no se debe tratar a T1 como confirmada. Con ARIES se puede repetir la historia y luego deshacerla. Otras arquitecturas usan protocolos distintos; «tener WAL» no significa «implementar exactamente ARIES».

Persistir un tramo del log puede cubrir commits de varias transacciones. Se conoce como **group commit**: una sincronización sirve a varios registros incluidos en el tramo. Su beneficio es amortizar la persistencia; no permite confirmar un registro que quedó fuera del tramo durable. Esta ampliación se apoya en la [misma documentación de PostgreSQL](https://www.postgresql.org/docs/17/wal-intro.html).

## ¿Qué pasa si el cliente no recibió la respuesta?

Hay tres momentos distintos: emitir el commit, hacerlo durable y recibir la respuesta. El servidor puede haber hecho durable el commit y caer, o perder la conexión, antes de que el cliente reciba `OK`. Entonces **el resultado es incierto para el cliente**, aunque el motor pueda determinarlo al recuperarse.

Repetir a ciegas la transferencia podría ejecutarla dos veces. Como ampliación didáctica, una aplicación puede usar un identificador de operación y consultar o registrar ese identificador para distinguir un reintento de una operación nueva. La falta de respuesta no demuestra que hubo abort.

## Qué guarda un registro: imágenes, bytes u operaciones

Una **before-image** describe el estado anterior y una **after-image** el posterior. Si X cambia de 8 a 11, repetir su after-image lo lleva a 11; usar la before-image lo devuelve a 8. El log también puede describir una operación, por ejemplo «insertar la clave K».

| Forma de logging | Información principal | Dificultad que debe resolver |
|---|---|---|
| Física | Imagen de página o cambio de bytes identificados | Aplicarlo a la página y versión adecuadas |
| Lógica | Operación sobre registros o claves | Encontrar su objeto aunque cambie la estructura física |
| Combinada | Información física y semántica según el propósito | Coordinar redo rápido y undo correcto |

La frase del libro que asocia logging físico con imágenes de páginas completas es una simplificación: la misma sección admite cambios por bytes. **Físico no significa siempre página completa.** Una entrada lógica tampoco puede ejecutarse sin control sobre cualquier estado: repetir «sumar 3» dos veces daría 14 en lugar de 11. El protocolo debe saber si el efecto ya está instalado.

**Shadow paging** es la alternativa que menciona el libro: se escribe una página nueva sin publicar y después se cambia la referencia que hace visible el nuevo estado. La referencia y las páginas nuevas necesitan un protocolo seguro de persistencia; la expresión «cambiar un puntero» no convierte automáticamente todo el proceso en durable.

## Checkpoints: reducir el trabajo pendiente

Un **checkpoint** registra información que permite acotar la recuperación. No es un commit masivo ni convierte en confirmadas las transacciones activas. También ayuda a identificar cuánto log debe conservarse para las páginas que aún necesitan reconstrucción.

En un modelo **sincrónico**, se sincronizan páginas dirty y se establece una frontera conocida, a costa de concentrar I/O o detener trabajo según el diseño. Un **fuzzy checkpoint** permite que continúen las transacciones mientras se registra el estado de recuperación: qué páginas podrían estar pendientes y qué transacciones siguen activas.

> [!important] Precisión sobre ARIES
> PDF 12–13, impresas 90–91, presenta el fuzzy checkpoint como incompleto hasta escribir sus páginas. En ARIES, el checkpoint puede completarse sin forzar ninguna página dirty: registra las tablas de transacciones y páginas pendientes. Estas páginas conservan necesidades de redo, incluso anteriores al inicio del checkpoint. Un checkpoint no es, por sí solo, una frontera para borrar todo el WAL anterior. Cotejo: [artículo original de ARIES, sección 5.4](https://www.cs.cmu.edu/~15849g/readings/mohan92.pdf).

El peligro práctico es eliminar una entrada todavía necesaria. Por ejemplo propio, un checkpoint inicia en LSN 500, pero una página que no fue escrita conserva pendiente un cambio de LSN 420. Guardar solo el log desde 500 perdería la información para reconstruir ese cambio. La nota 05 conecta el registro de páginas pendientes con el análisis de recuperación.

Incluso después de persistir una página, otro trabajo puede necesitar registros antiguos, por ejemplo deshacer una transacción larga aún activa. La regla segura es conservar el log necesario para **todas** las responsabilidades vigentes; no borrarlo porque una sola página ya se escribió.

## La persistencia depende de una cadena de garantías

El recuadro de PDF 11–12, impresas 89–90, describe un problema histórico entre PostgreSQL y la notificación de errores de `fsync` del sistema operativo. Su enseñanza es que una llamada aparentemente exitosa o un bit dirty borrado no basta si las capas inferiores perdieron o notificaron mal una escritura.

Aquí se conserva como **caso histórico del libro**, sin afirmar que las versiones actuales mantengan el mismo fallo. Recuperación debe contrastar el protocolo del motor con el comportamiento de archivos, sistema operativo y dispositivo; guardar las instrucciones correctas no sirve si se cree durable algo que nunca llegó al soporte.

> [!question]- ¿Un commit durable obliga a que todas sus páginas estén actualizadas en disco?
> No bajo no-force. Obliga a que exista información durable suficiente, incluido el registro de commit, para conservar su resultado después del fallo. Las páginas pueden ponerse al día mediante redo.

> [!question]- ¿Por qué no basta con conservar el log después del inicio del último checkpoint?
> Puede haber páginas con cambios anteriores aún sin persistir, o transacciones activas que necesitan undo anterior. El checkpoint registra lo pendiente; no elimina esas dependencias.

**Fuente:** PDF 10–13 · impresas 88–91. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=10|WAL, LSN, checkpoints, shadow paging y tipos de log]].

---

← [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/03 Reemplazo de páginas FIFO LRU CLOCK y TinyLFU|Anterior]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/05 Políticas steal force y recuperación ARIES|Siguiente →]]
