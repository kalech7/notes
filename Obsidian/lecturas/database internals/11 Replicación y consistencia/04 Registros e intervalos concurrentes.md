---
title: "Database Internals — Capítulo 11 · Registros e intervalos concurrentes"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Registros e intervalos concurrentes

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

Un **registro** es una unidad de almacenamiento accesible mediante `read(x)` y `write(x,v)`. Esta abstracción oculta máquinas y mensajes para estudiar qué valores puede devolver una lectura. Una base se puede imaginar como varios registros, pero una operación sobre un registro no representa automáticamente una transacción sobre varias claves.

Cada operación tiene **invocación**, cuando el cliente la inicia, y **respuesta**, cuando termina para ese cliente. Si la respuesta de A ocurre antes de la invocación de B, A precede a B en tiempo real. Si sus intervalos se solapan, son concurrentes, incluso si una operación queda enteramente dentro del intervalo de la otra.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 11/02 Intervalos y concurrencia.png]]

Las líneas azules y naranjas representan intervalos de P1 y P2. Sólo la primera pareja tiene una respuesta anterior a la siguiente invocación. El segundo caso se solapa parcialmente y el tercero contiene una operación completa dentro de otra; ambos son concurrentes. Es una recreación explicativa de la figura 11-1.

## Safe, regular y atomic

En el caso básico de un registro con un escritor, una lectura que **no se solapa** con ninguna escritura devuelve el último valor escrito. La diferencia aparece cuando se solapa con una escritura.

| Tipo | Lectura concurrente a una escritura | Consecuencia |
|---|---|---|
| Seguro, *safe* | Puede devolver cualquier valor del dominio | No basta conocer el valor anterior y el nuevo |
| Regular | Devuelve el último valor anterior o uno de las escrituras solapadas | Descarta valores ajenos a esos cambios |
| Atómico, *atomic* | Debe encajar en una historia linealizable | Impide volver a una versión anterior sin una escritura que lo justifique |

Ejemplo propio: el dominio es `{0,1,2,3}`, el valor anterior es 1 y se escribe 2. Una lectura concurrente de un registro seguro podría devolver 3. Una regular sólo devuelve 1 o 2. Para distinguir regular de atómico hace falta estudiar varias lecturas: durante una escritura larga, dos lecturas sucesivas pueden devolver 2 y después 1 bajo regularidad. Si sólo existe ese cambio 1→2, esa inversión no admite una única historia atómica.

El caso multiescritor exige definir con cuidado qué escrituras preceden o se solapan y sus condiciones de orden. Las definiciones introductorias del libro no son un algoritmo multiescritor completo. Aquí se utiliza primero el caso sencillo para entender el cambio de garantía.

## Respuesta perdida y operación pendiente

El libro trata como fallida una operación cuyo cliente cae antes de completar. Desde fuera, conviene añadir una precisión: falta de respuesta **no demuestra ausencia de efecto**. El servidor pudo guardar el cambio antes de que se perdiera la confirmación. Esa operación queda pendiente o de resultado desconocido en la historia observada.

Esto es distinto de ver medio registro actualizado. Un contrato puede impedir efectos parciales y aun permitir que una escritura de resultado desconocido haya surtido efecto por completo. Esa distinción reaparece en los reintentos y en los quórums.

> [!question]- ¿Una operación concurrente debe ejecutarse realmente al mismo tiempo en ambas CPU?
> No. Aquí concurrencia es solapamiento entre invocación y respuesta. Una operación podría esperar en una cola y seguir siendo concurrente con otra.

**Referencia:** PDF 23–24 · impresas 219–220 · figura 11-1. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=23|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/03 Disponibilidad parcial harvest y yield|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/05 Modelos como contratos de visibilidad|Siguiente]] →
