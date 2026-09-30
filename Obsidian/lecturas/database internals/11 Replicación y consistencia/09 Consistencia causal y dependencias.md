---
title: "Database Internals — Capítulo 11 · Consistencia causal y dependencias"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Consistencia causal y dependencias

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

La **consistencia causal** conserva el orden entre operaciones conectadas por causa y efecto. Si Bruno lee la publicación de Ana y después escribe una respuesta, la respuesta depende de la publicación. Los participantes no deben ver la respuesta como si existiera antes de su antecedente.

Las escrituras que no tienen relación causal pueden observarse en distinto orden. Esto evita acordar un orden total único para hechos independientes, aunque obliga a transportar información sobre dependencias.

## Qué crea una dependencia

El orden de operaciones de un cliente, observar un efecto y producir otro, y la transitividad crean relaciones de **happened-before**, «ocurrió antes» en sentido causal. Si A causa B y B causa C, A es también antecedente de C. Una comparación entre relojes físicos de clientes distintos no demuestra por sí sola causalidad.

La figura 11-6 deja dos escrituras independientes: P3 ve 1→2 y P4 ve 2→1. En la figura 11-7 se añade contexto para declarar que escribir 2 depende de escribir 1. En la 11-8 ambos lectores deben respetar 1→2. El cambio importante no es que el mensaje de 1 viaje más rápido: es impedir publicar el dependiente mientras falta el antecedente.

## Llegar primero no significa hacerse visible primero

Ejemplo propio: una réplica recibe `M3(respuesta final, depende de M2)` antes que `M1(publicación original)` y `M2(primera respuesta, depende de M1)`. Puede guardar M3 en un buffer, pero no exponerlo. Cuando llega M2 todavía falta M1; cuando llega M1, reconstruye M1→M2→M3 y puede aplicar los tres.

Ese buffer no crea una dependencia que no haya sido comunicada. El cliente o capa de acceso debe conservar y adjuntar el contexto causal. Cambiar de réplica y perder ese contexto puede hacer que el sistema deje de reconocer una relación que la aplicación necesita.

## COPS y Eiger en el capítulo

El libro presenta **COPS**, *Clusters of Order-Preserving Servers*, como un diseño que rastrea dependencias mediante versiones de claves y una capa de acceso. Presenta **Eiger** como un diseño que establece dependencias entre operaciones, incluyendo relaciones entre nodos y operaciones que afectan varias particiones.

En ambos, las actualizaciones que carecen de antecedentes quedan retenidas antes de hacerse visibles. El capítulo diferencia resolución con orden de claves y funciones de aplicación en COPS, y una regla de última escritura en Eiger. Son ejemplos de la fuente, no una auditoría de versiones actuales de esos proyectos ni una recomendación de producto.

## Causalidad no resuelve el significado del conflicto

Dos clientes pueden modificar el mismo dato partiendo de una versión compartida sin haber visto el cambio del otro. La causalidad identifica dos ramas concurrentes, pero no decide si hay que sumar cantidades, conservar ambas direcciones o elegir una versión. Esa semántica pertenece al tipo de dato y a la aplicación.

Si la dependencia necesaria no llegó, retener una operación puede afectar disponibilidad o latencia. Causal es más débil que un orden total, pero no autoriza entregar un resultado cuyo contexto falta. El ahorro consiste en evitar ordenar los eventos independientes.

> [!question]- ¿Mostrar una respuesta antes que su pregunta viola siempre causalidad?
> Viola el contrato causal si la respuesta depende de la pregunta y se expone sin su antecedente requerido. No basta suponer la relación por cercanía de marcas de tiempo; debe formar parte del contexto reconocido por el sistema.

**Referencia:** PDF 33–35 · impresas 229–231 · figuras 11-6, 11-7 y 11-8. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=33|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/08 Consistencia secuencial y composición|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/10 Relojes vectoriales y conflictos|Siguiente]] →
