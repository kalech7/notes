---
title: "Database Internals — Capítulo 7 · Actualizaciones borrados y tombstones"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Actualizaciones borrados y tombstones

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] Para dar contexto
> Si una clave aparece en varias fuentes, quitarla de la memtable solo elimina una copia. Para que una eliminación sobreviva, debe competir con las versiones anteriores.

## Una actualización no necesita buscar el valor antiguo

Una escritura `cliente-8: dirección=B` puede añadirse aunque el disco todavía contenga `dirección=A`. En el camino físico se registra una nueva versión. El libro llama a esta operación **upsert**: insertar si no existe o actualizar si existe.

Esto describe el comportamiento de almacenamiento. Una API SQL puede exigir comprobar unicidad, una condición previa o un conflicto transaccional, y entonces sí realizar lecturas. Evitar buscar el registro para sobrescribirlo no elimina las comprobaciones que exige la semántica de la operación.

## Por qué no sirve quitarlo de RAM

| Fuente | Antes de borrar incorrectamente | Después de quitar la entrada de RAM |
|---|---|---|
| Archivo antiguo | `k=azul, versión=1` | `k=azul, versión=1` |
| Memtable | `k=verde, versión=2` | Sin registro para k |
| Lectura actual | Verde | Azul reaparece |

La eliminación incorrecta devuelve visibilidad a la copia antigua. Un **tombstone** es un registro que afirma “esta clave está borrada” y tiene una versión. Con `k=BORRADO, versión=3`, la reconciliación encuentra la información más reciente y devuelve ausencia.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 07/02 borrado_y_resurreccion.png]]

La columna izquierda quita la versión verde y deja que azul vuelva a ser el único candidato. La derecha conserva una marca con versión 3 que domina las anteriores. El resultado lógico es ausencia aunque existan físicamente los dos valores viejos.

## Borrar un rango

Un **range tombstone** describe un intervalo de claves en vez de una sola. El libro usa límites inclusivo y exclusivo; `[k2, k4)` contiene k2 y k3, pero excluye k4. Durante la lectura se compara tanto la pertenencia al intervalo como la precedencia temporal.

Ejemplo propio: una marca de versión 10 borra `[20,40)`. Los valores 20@8 y 35@9 quedan ocultos; 40@8 está fuera. Si luego insertamos 35@11, esa versión nueva puede volver a ser visible. Una implementación necesita resolver rangos superpuestos y dividir o conservar sus límites al cambiar las fronteras de las tablas.

## Eliminar físicamente la marca exige una prueba

La compactación de A y B no conoce necesariamente los archivos que dejó afuera. Si el tombstone está en A y un valor viejo está en C, descartarlo al compactar solo A+B resucitaría el valor de C. La marca se retira cuando se demuestra que no quedan versiones anteriores relevantes en otras fuentes.

Además, si el motor conserva **snapshots**, vistas históricas de lectura, algunas versiones antiguas siguen siendo necesarias. Una lectura con snapshot 2 del ejemplo anterior recibe verde, mientras la actual recibe ausencia. La compactación debe respetar esa necesidad antes de descartar versiones. En motores distribuidos, una réplica atrasada añade otra condición: su información antigua no debe volver a introducir el valor eliminado.

El capítulo explica las consideraciones locales y menciona plazos de gracia en Cassandra. Un plazo por sí solo no demuestra que todas las réplicas hayan recibido la eliminación; esas políticas dependen de reparación y garantías del motor.

> [!question]- ¿Una clave ausente en una SSTable está borrada?
> No. El archivo puede no contenerla nunca, o puede conservarse en otra tabla. Un tombstone es una afirmación explícita de eliminación; la ausencia de entrada no lo sustituye.

**Puente al siguiente tema:** tenemos versiones y marcas. Falta el procedimiento que recorre varias fuentes ordenadas y decide qué devolver.

**Referencia:** PDF 8–9, 12–13 · impresas 136–137, 140–141. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=8|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/03 Memtables flush y publicación de archivos|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/05 Merge iteration y reconciliación de versiones|Siguiente]] →
