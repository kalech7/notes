---
title: "Database Internals — Relojes, consistencia y llamadas remotas"
created: 2026-09-30
libro: "Database Internals"
capitulo: 8
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Relojes, consistencia y llamadas remotas

[[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice del capítulo 8]]

El tiempo que una máquina escribe y el estado que conoce son observaciones locales. Para combinar datos de varios nodos necesitamos conocer qué garantiza cada reloj y qué parte del estado puede estar desactualizada.

> «El tiempo es una ilusión; la hora de comer, aún más».
> — Ford Prefect, personaje de *The Hitchhiker’s Guide to the Galaxy*, de Douglas Adams; traducción breve del epígrafe.

El humor introduce una dificultad concreta: dos participantes pueden discrepar sobre la hora y aun así ejecutar eventos reales. Por eso la marca de calendario sola no prueba un orden entre ellos.

## Hora de calendario y duración

Un **reloj de pared** expresa una hora comparable con fechas del mundo. Puede corregirse y saltar hacia delante o atrás. Un **reloj monotónico** no retrocede durante su ámbito de funcionamiento y sirve para medir intervalos locales; no necesariamente coincide con la hora civil ni tiene el mismo origen en otra máquina.

Ejemplo propio: A envía una actualización a las 12:00:10 de su reloj y B registra su recepción como 12:00:08. Si B está atrasado 5 segundos, el registro no demuestra que recibió antes de enviar. Para estudiar duración local, un plazo de 500 ms debe medirse con una fuente que garantice el comportamiento necesario. Un reloj monotónico no elimina los retrasos de planificación ni las pausas del proceso.

**Desfase** es la diferencia entre lecturas de relojes en un instante; **deriva** describe cómo esa diferencia evoluciona por ritmos distintos. La sincronización reduce o acota incertidumbre según el mecanismo, pero no convierte todos los timestamps en orden causal perfecto. El capítulo menciona Spanner como ejemplo de un diseño que usa un intervalo de incertidumbre junto a un protocolo adicional; aquí no se desarrolla ese capítulo posterior.

## La consistencia también alcanza los metadatos

Replicar valores y aceptar su divergencia temporal exige mecanismos de **resolución de conflictos** para elegir o combinar versiones y, en algunos diseños, **read repair** para reconciliar copias durante una lectura. Esto no garantiza automáticamente que esquema y configuración del clúster estén de acuerdo.

El libro relata bugs históricos de Cassandra relacionados con ese supuesto. Si un nodo codifica una respuesta con el esquema nuevo y otro la interpreta con el antiguo, incluso una respuesta recibida puede entenderse mal. Si cada nodo cree que una clave pertenece a un servidor diferente, puede enviar lecturas o escrituras al destino equivocado. Se registran como ejemplos del libro, sin afirmar que esos fallos estén presentes en una versión actual.

Una lectura por **quórum** consulta una cantidad de réplicas definida por el protocolo. El número de respuestas por sí solo no establece todas las garantías: importan qué versiones se aceptan, quién puede escribir y cómo cambia la membresía. El capítulo presenta el riesgo de asumir metadatos consistentes; no desarrolla todavía un protocolo de quórum completo.

## Una API familiar puede ocultar costos diferentes

Una llamada remota usa transporte y serialización, puede bloquear más tiempo y puede terminar con efecto desconocido. Un iterador remoto también necesita definir paginación, reconciliación y qué sucede si los datos cambian entre páginas. Parecerse a una función o iterador local facilita el uso, pero no debe borrar sus garantías.

Una API de estudio podría devolver `confirmado`, `rechazado` o `resultado_desconocido`, además de un identificador de operación. El tercero es necesario cuando no se puede distinguir «no se ejecutó» de «se ejecutó pero perdí la respuesta». La observabilidad —registros, métricas e identificadores correlacionados— ayuda a reconstruir lo ocurrido; no sustituye el protocolo de seguridad.

La transición siguiente es natural: si el estado y la observación son locales, una misma falla puede verse de manera distinta desde dos participantes.

**Referencia:** PDF 9–11 · impresas 176–178. [[Obsidian/lecturas/database internals/Materiales/08 Sistemas distribuidos.pdf#page=9|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/04 Colas procesamiento y backpressure|Anterior]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/06 Fallas parciales particiones y cascadas|Siguiente]] →
