---
title: "Database Internals — Capítulo 11 · RIFL reintentos y efectos únicos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# RIFL reintentos y efectos únicos

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

**RIFL**, *Reusable Infrastructure for Linearizability*, es la infraestructura que el capítulo utiliza para explicar cómo dar semántica linealizable a llamadas remotas bajo reintentos. El problema central es distinguir repetir el transporte de repetir el efecto lógico.

Ejemplo del libro reformulado: C1 escribe V1, el servidor aplica el cambio y la respuesta se pierde. C2 escribe V2. Si C1 reintenta y el servidor aplica V1 otra vez, el nuevo transporte resucita un cambio antiguo sobre V2. La escritura lógica de C1 ocurrió una vez; no debe adquirir un segundo lugar en la historia porque se perdió la confirmación.

## Identidad y objeto de finalización

Cada llamada se identifica con `(identidad de cliente, secuencia local creciente)`. El número de secuencia distingue operaciones de un cliente y la identidad evita colisiones entre clientes. Una repetición con la misma identidad corresponde a la misma operación.

El servidor conserva un **objeto de finalización** que registra que la operación terminó y cuál fue su resultado. Si llega un duplicado, devuelve ese resultado en vez de volver a modificar los datos. Esta memoria debe ser durable y debe crearse **atómicamente junto con la mutación**.

| Caída en un diseño defectuoso | Estado que queda | Riesgo del reintento |
|---|---|---|
| Dato guardado, deduplicación no guardada | Cambio sin recuerdo del efecto | Ejecutar dos veces |
| Deduplicación guardada, dato no guardado | Recuerdo sin cambio | Responder éxito inexistente |
| Ambos guardados atómicamente | Cambio y resultado coherentes | Devolver resultado original |

El objeto de finalización no es una copia de toda la historia de la base. Está asociado a un identificador y vive mientras la operación pueda volver a intentarse. Su resultado puede ser diferente del valor actual del registro: C1 recibe su resultado original aunque C2 haya producido una versión posterior.

## Leases y recolección

Una **lease** es un permiso con duración limitada. RIFL asigna identidades mediante un servicio y exige renovaciones. La lease ayuda a decidir hasta cuándo un cliente puede reintentar con esa identidad, de forma que los objetos de finalización no se conserven para siempre.

Un cliente que vuelve con lease expirada no puede ejecutar operaciones antiguas como si su identidad continuara vigente. El sistema rechaza ese uso y requiere una nueva lease. De lo contrario, recolectar resultados permitiría que un duplicado viejo se tratara como operación nueva.

La recolección ocurre cuando el cliente garantiza que no reintentará o cuando las reglas de la lease impiden que lo haga válidamente. «Detectar una caída» no significa adivinar con certeza por un timeout: la seguridad depende de que el protocolo invalide reintentos de esa identidad.

## Alcance de la garantía

RIFL evita ejecutar más de una vez la misma operación identificada y permite publicar su efecto de manera atómica con la información de finalización. La linealizabilidad completa todavía requiere que el almacén subyacente y sus respuestas respeten el orden necesario. Deduplicación durable por sí sola no convierte una réplica eventual en un registro linealizable.

Tampoco garantiza que una llamada llegue a terminar bajo una partición permanente. Separa una garantía de seguridad —no duplicar el efecto— de las condiciones que permiten progresar. Reiniciar un cliente y generar un identificador nuevo para el mismo intento de negocio puede crear una nueva operación; una política de idempotencia de negocio debe conservar su identidad si quiere reconocerla.

> [!question]- ¿Devolver el resultado original equivale a volver a leer el valor actual?
> No. El resultado original responde qué pasó con esa operación. Una lectura actual podría mostrar una modificación posterior de otro cliente.

**Referencia:** PDF 31 · impresa 227. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=31|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/06 Linealizabilidad puntos de efecto y costo|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/08 Consistencia secuencial y composición|Siguiente]] →
