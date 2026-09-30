---
title: "Database Internals — Capítulo 7 · Inmutabilidad y la idea de añadir correcciones"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Inmutabilidad y la idea de añadir correcciones

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] Punto de partida
> Ya conocemos árboles que modifican páginas. Ahora cambiamos la pregunta: ¿qué ocurre si conservamos lo escrito y registramos cada corrección por separado?

## La frase que abre el capítulo

> «Los contables no usan gomas de borrar o terminan en la cárcel». — Pat Helland, traducción breve del epígrafe del capítulo.

La frase es una analogía: un registro contable corregido conserva una huella de la modificación. En almacenamiento, **append-only** significa añadir registros al final de un archivo, y **inmutable** significa que un archivo publicado no vuelve a cambiar. Si una clave cambia de valor, se escribe una versión nueva. Si se elimina, se escribe una marca de borrado. El estado lógico actual se calcula a partir de esas versiones.

Esto no convierte automáticamente una base en un historial de auditoría perpetuo. La compactación puede eliminar versiones que ya no sirven. El epígrafe explica cómo se representan las correcciones, no una garantía de conservación ilimitada.

## Un ejemplo que separa estado físico y lógico

Supongamos una cuenta identificada por `cuenta-42`. Un archivo antiguo contiene `saldo=80, versión=10`; después registramos `saldo=95, versión=11`. Físicamente hay dos registros; lógicamente el lector actual recibe 95. **Reconciliar** significa resolver estas versiones según una regla de precedencia y producir la respuesta que corresponde a la consulta.

La versión es un orden definido por el motor. En estos ejemplos usamos números crecientes porque son fáciles de comparar. El libro menciona timestamps; no debemos asumir que cualquier reloj de pared ofrece por sí solo un orden correcto para todas las transacciones.

| Decisión | Modificar en el lugar | Escribir otra versión |
|---|---|---|
| Escritura | Localizar y modificar una página | Añadir registro y posponer integración |
| Lectura | Encontrar la representación vigente | Consultar fuentes y resolver precedencia |
| Mantenimiento | Liberar celdas y desfragmentar | Fusionar archivos y eliminar versiones inútiles |
| Concurrencia | Proteger cambios sobre páginas compartidas | Proteger estructuras mutables y publicación de vistas |

Un **B-Tree** clásico organiza claves en un árbol de páginas. Actualizar pocos bytes puede obligar a escribir una página completa; además hay divisiones, fusiones y espacio reservado para inserciones futuras. Una **LSM Tree**, abreviatura de *Log-Structured Merge Tree*, acumula cambios y produce archivos ordenados mediante escrituras grandes. Cambia escrituras pequeñas y dispersas por trabajo agrupado y mantenimiento posterior.

## Por qué la inmutabilidad ayuda

Dos lectores pueden leer un archivo publicado sin coordinar una modificación dentro de él: nadie lo cambia. El archivo tampoco necesita reservar huecos para inserciones futuras. Esa densidad es una ventaja física, pero varias versiones en distintos archivos siguen ocupando espacio. La compactación paga la deuda de conservarlas.

El capítulo contrapone B-Trees y LSM, aunque no son familias incompatibles: una SSTable de una LSM puede usar un índice interno con forma de B-Tree. También hay B-Trees con copy-on-write. La comparación debe identificar qué componente es mutable, cómo se escribe y dónde se ordena.

> [!question]- ¿Una LSM evita escribir en disco cuando aceptamos una escritura?
> Solo evita buscar y modificar inmediatamente el registro previo. Para confirmar una escritura durable normalmente necesita persistir el WAL u otra representación recuperable. La memtable en RAM puede perderse tras una caída.

**Puente al siguiente tema:** separar registro nuevo y estado actual es la idea general. Para convertirla en un motor necesitamos saber dónde se acumulan los cambios y cómo llegan al disco.

**Referencia:** PDF 1–3 · impresas 129–131. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=1|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/02 Dos componentes y múltiples archivos|Siguiente]] →
