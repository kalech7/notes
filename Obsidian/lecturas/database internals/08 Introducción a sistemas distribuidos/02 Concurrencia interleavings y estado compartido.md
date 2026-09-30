---
title: "Database Internals — Concurrencia, interleavings y estado compartido"
created: 2026-09-30
libro: "Database Internals"
capitulo: 8
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Concurrencia, interleavings y estado compartido

[[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice del capítulo 8]]

Antes de añadir una red, dos actividades que acceden al mismo dato ya pueden producir varias historias. Entender esta carrera local permite ver por qué varios nodos necesitan reglas explícitas de orden y visibilidad.

## Una operación tiene pasos internos

El capítulo usa `x = 1`, una suma de 2 y una multiplicación por 2. En ejecución secuencial, primero sumar y después multiplicar produce `(1 + 2) × 2 = 6`. En cambio, con dos ejecutores sin coordinación cada operación puede separar **lectura**, cálculo local y **escritura**. El sumador puede leer 1, calcular 3 y escribirlo después de que el multiplicador haya escrito 2.

Un **interleaving** es una mezcla de pasos de los ejecutores que conserva el orden interno de cada uno. El ejemplo abstracto supone lecturas y escrituras individuales indivisibles y un único valor compartido. No es una promesa sobre un lenguaje con carreras de datos: sus reglas de memoria pueden impedir interpretar código real de esta manera.

| Historia | Pasos de lectura y escritura | Valor final |
|---|---|---:|
| Ambos leen 1, escribe al final el multiplicador | `R+1, R×1, W+3, W×2` | 2 |
| Ambos leen 1, escribe al final el sumador | `R+1, R×1, W×2, W+3` | 3 |
| Termina la multiplicación y luego empieza la suma | `R×1, W×2, R+2, W+4` | 4 |
| Termina la suma y luego empieza la multiplicación | `R+1, W+3, R×3, W×6` | 6 |

La figura 8-1 muestra estos cuatro resultados. Hay seis órdenes válidos de cuatro pasos; algunos repiten el resultado porque cambiar el orden de las dos primeras lecturas no cambia qué valor se escribe. La nota al pie del libro omite un orden equivalente por brevedad. En 2 y 3 se **pierde una actualización**: la última escritura usa una lectura antigua y tapa el efecto de la otra operación. En 4 y 6 ambas operaciones tienen efecto, pero su orden cambia el resultado.

## Concurrencia y paralelismo

**Concurrencia** significa que varias actividades están en progreso en intervalos superpuestos. **Paralelismo** significa que ejecutan pasos simultáneamente. El libro recoge la analogía de Joe Armstrong: varias colas frente a una máquina de café ayudan a pensar en concurrencia; varias máquinas permiten trabajo en paralelo. Esa analogía es una ayuda, no una definición de planificación: un programa concurrente puede además usar varios procesadores.

Un solo núcleo puede alternar pasos y exhibir la carrera anterior; por tanto, el fallo no exige dos CPU trabajando a la vez. La coordinación debe proteger la operación completa si se necesita una transformación atómica, no solo cada lectura o escritura por separado.

## Estado compartido y modelos de consistencia

Un **modelo de consistencia** especifica qué órdenes y observaciones de operaciones están permitidos. Reduce las historias que el sistema puede mostrar. Por ejemplo, si la suma y multiplicación completas se ordenan como operaciones indivisibles, los resultados compatibles con ese modelo son 4 o 6; 2 y 3 quedan excluidos. Eso no decide cuál de los dos órdenes se elegirá.

En una máquina los ejecutores pueden acceder a memoria compartida. En un sistema distribuido cada proceso conoce su estado local y recibe mensajes. Añadir una base central no elimina esa frontera: quien envía una actualización todavía necesita saber si llegó, si se ejecutó y qué ven los demás.

Al introducir una segunda copia de la base para tolerar fallos aparece otro problema: mantener las copias de acuerdo. **Redundancia** significa tener recursos adicionales para soportar la pérdida de alguno, pero no define por sí misma el protocolo de replicación ni la consistencia que perciben los clientes.

> [!question]- ¿Un mutex que protege solo la lectura y otro que protege solo la escritura evita la pérdida de actualización?
> No. Entre las dos secciones otro ejecutor puede modificar `x`. Para este modelo hay que proteger la transformación completa o utilizar un mecanismo equivalente que valide la versión y reintente cuando cambió.

**Referencia:** PDF 4–7 · impresas 171–174 · figura 8-1. [[Obsidian/lecturas/database internals/Materiales/08 Sistemas distribuidos.pdf#page=4|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/01 Parte II del motor local al sistema distribuido|Anterior]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/03 La red y sus supuestos peligrosos|Siguiente]] →
