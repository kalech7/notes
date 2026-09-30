---
title: "Database Internals — Orden, deduplicación e idempotencia"
created: 2026-09-30
libro: "Database Internals"
capitulo: 8
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Orden, deduplicación e idempotencia

[[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice del capítulo 8]]

El reintento mejora la entrega y puede repetir una acción. Para usarlo con seguridad necesitamos controlar tanto el orden en que se aplican las operaciones como la memoria que permite reconocer una repetida.

> «Dos problemas difíciles: 2. entrega exactamente una vez; 1. orden garantizado; 2. entrega exactamente una vez».
> — Mathias Verraes; versión breve traducida del epígrafe.

El chiste enumera fuera de orden y repite un elemento. Su forma representa precisamente los dos defectos que debe controlar el protocolo.

## Idempotencia y deduplicación resuelven problemas relacionados

Una operación es **idempotente** si repetirla produce el mismo efecto final que aplicarla una vez, dentro de la semántica definida. Establecer `estado = cerrado` puede ser idempotente; incrementar un saldo o cobrar una cantidad no lo es. Aunque el estado principal quede igual, un correo enviado en cada intento sería un efecto adicional: la propiedad debe abarcar el efecto que realmente se promete.

**Deduplicación** significa reconocer una operación ya aplicada y evitar repetir su efecto. Para un cobro se puede asociar un ID al efecto y al resultado. Un nuevo intento con el mismo ID devuelve el resultado guardado. El cliente debe conservar el mismo ID, y el servidor debe detectar si el mismo ID intenta representar un contenido diferente.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 08/ack_perdido.png]]

Los dos recorridos terminan con una confirmación perdida después del efecto. En rojo, el cliente repite sin identificación estable y vuelve a cobrar. En azul, reenvía el mismo ID y el servidor reconoce el registro durable; devuelve el resultado sin un segundo cargo. La imagen es elaboración propia y amplía el escenario de las figuras 8-2 y 8-3.

La condición decisiva es **atomicidad** entre registrar el ID y aplicar el efecto: ambos deben quedar comprometidos juntos o ninguno. Si primero guardo «ID visto» y caigo antes de cobrar, un reintento podría omitir un cobro que nunca ocurrió. Si primero cobro y caigo antes de guardar el ID, podría repetirlo. Cuando el efecto está en un sistema externo, una transacción local por sí sola no cubre ese sistema; hace falta un protocolo o una API externa con la garantía adecuada.

## Ordenar requiere saber dónde falta algo

Para una secuencia por emisor, el receptor puede mantener `n_consecutive`, el mayor número hasta el que tiene todos los mensajes recibidos; `n_processed`, el mayor número hasta el que aplicó mensajes en orden; y un buffer para los que llegaron antes que sus predecesores. Con mensajes 1, 2 y 3 aplicados, si llega 5 se guarda porque falta 4. Al llegar 4 puede entregar 4 y después 5.

Un duplicado de 2 se descarta porque su efecto ya fue aplicado. Recibido y procesado son hitos diferentes: `n_processed` puede ser menor que `n_consecutive` si el consumidor está retrasado. La impresa 186 usa una formulación de descarte basada en `n_consecutive`; aquí se distingue el almacenamiento del duplicado recibido de la garantía de efecto ya aplicado, que requiere `n_processed` o el registro correspondiente.

**FIFO** conserva el orden definido para esa secuencia. No establece un único orden global entre mensajes de varios emisores. La numeración necesita ámbito —emisor y sesión, por ejemplo— y reglas al reiniciar; volver a usar números antiguos puede hacer que se descarte una operación nueva.

## Una vez: especificar la capa

| Semántica | Garantía del efecto o entrega definida | Posible inconveniente |
|---|---|---|
| A lo sumo una vez | Cero o una vez | Puede no ocurrir |
| Al menos una vez | Una o más veces, bajo condiciones de progreso | Puede repetirse |
| Exactamente una vez en un ámbito | Una vez para una operación identificada | Requiere definir duración, fallas y almacenamiento |

La política «no reintentar» del libro es un modo sencillo de buscar a lo sumo una vez, pero no es su definición completa: un sistema puede retransmitir y deduplicar. Ninguna etiqueta reemplaza la descripción de qué ocurre al reiniciar, reconectar o agotar la memoria de deduplicación.

TCP ofrece un flujo de bytes ordenado y fiable dentro de una conexión; retransmitir segmentos no exige entregar esos bytes duplicados a la aplicación. No preserva límites de mensajes de la aplicación ni confirma un commit durable. Si una aplicación se reconecta y reenvía una petición, necesita su propia identificación y semántica. [Especificación de TCP, RFC 9293 §2.2](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2).

No debemos convertir la discusión de «exactamente una vez» en una prohibición universal: se pueden garantizar efectos únicos bajo un contrato y supuestos precisos. Lo que no obtenemos por añadir ACK es certeza sin condiciones sobre todo el sistema y todas sus fallas.

**Referencia:** PDF 17–20 · impresas 184–187. [[Obsidian/lecturas/database internals/Materiales/08 Sistemas distribuidos.pdf#page=17|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/07 Enlaces fair-loss ACK y retransmisión|Anterior]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/09 Dos generales y conocimiento común|Siguiente]] →
