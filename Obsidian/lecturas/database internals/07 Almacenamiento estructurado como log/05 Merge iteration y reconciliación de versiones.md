---
title: "Database Internals — Capítulo 7 · Merge iteration y reconciliación de versiones"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Merge iteration y reconciliación de versiones

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] La pregunta de esta nota
> ¿Cómo mezclamos varias secuencias ordenadas sin cargarlas completas, y cómo evitamos devolver valores viejos al encontrar la misma clave?

## Dos problemas diferentes

**Merge iteration** produce registros en orden de clave a partir de varios iteradores. Un **iterador** conserva una posición y permite obtener el siguiente registro de una fuente. **Reconciliación** resuelve los registros de una misma clave: elige la versión visible y aplica las marcas de borrado. Ordenar claves no basta para resolver versiones.

Una **cola de prioridad** extrae primero el elemento de menor prioridad; aquí esa prioridad es la clave más pequeña. Un **min-heap** implementa esa cola. Se coloca una cabeza por fuente, se extrae la mínima y se repone desde la misma fuente. Como cada fuente está ordenada, su cabeza es el único candidato necesario para conocer su próximo mínimo.

## Un recorrido completo con duplicados

Ejemplo propio, para una lectura actual:

- A: `(10,rojo,v1), (30,azul,v1)`.
- B: `(10,verde,v2), (20,BORRADO,v3)`.
- C: `(20,naranja,v1), (40,gris,v1)`.

| Paso | Cabezas mínimas relevantes | Decisión |
|---|---|---|
| 1 | 10@1 y 10@2 | Consumir el grupo 10 y emitir verde@2 |
| 2 | 20@3 y 20@1 | Consumir el grupo 20 y no emitir valor |
| 3 | 30@1 | Emitir azul@1 |
| 4 | 40@1 | Emitir gris@1 |

La salida es `10:verde, 30:azul, 40:gris`. La cola conserva candidatos para claves futuras; la reconciliación consume el grupo de la clave actual y decide su resultado. Es fundamental reponer iteradores antes de concluir que ya no quedan versiones de esa clave. Una SSTable que conserva varias versiones puede traerlas consecutivamente dentro de la misma fuente.

La explicación del libro usa el supuesto de una entrada por clave en cada iterador. En sistemas con múltiples versiones dentro de una tabla hay que agrupar todas las entradas de esa clave, no solo las cabezas iniciales de fuentes diferentes.

## Costo y memoria

Sean `K` fuentes y `R` registros consumidos. Guardamos hasta K cabezas: memoria `O(K)`, aparte de buffers de I/O y el grupo de versiones en curso. Cada extracción y reposición cuesta `O(log K)` en un heap binario, de modo que la mezcla cuesta `O(R log K)`. No es necesario ordenar R registros desde cero ni mantener todos en RAM.

Para una consulta de rango, primero posicionamos cada iterador en el comienzo relevante mediante su índice. Después mezclamos hasta el límite final. La consulta puntual puede emplear un procedimiento distinto, revisando candidatos y filtros, pero comparte las reglas de visibilidad.

## Lo que significa “más reciente”

No es necesariamente el archivo que acabamos de crear: una compactación nueva puede contener valores muy antiguos. La precedencia se decide por versión y reglas del motor. Para un snapshot S, primero se consideran versiones visibles para S; se resuelve dentro de ese conjunto. Un tombstone posterior a S no debe borrar el resultado histórico.

> [!question]- ¿Por qué una cola ordenada solo por clave no puede escoger la versión final?
> Las versiones de una clave tienen la misma prioridad de clave. Hace falta agruparlas y comparar su orden de versiones, además de considerar la visibilidad de la consulta. El orden accidental de extracción no es una regla de reconciliación.

**Puente al siguiente tema:** el mismo recorrido ordenado que resuelve una lectura sirve para crear archivos nuevos. Esa reutilización conecta lectura y compactación.

**Referencia:** PDF 9–13 · impresas 137–141 · figura 7-5. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=9|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/04 Actualizaciones borrados y tombstones|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/06 Compactación por niveles tamaños y tiempo|Siguiente]] →
