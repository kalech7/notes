---
title: "Database Internals — Comparar variantes y conectar los mecanismos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - arquitectura/costos
  - arquitectura/diseno
---

# Comparar variantes y conectar los mecanismos

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

Todas las variantes parten del mismo trabajo lógico: mantener claves ordenadas y permitir búsquedas y modificaciones. Lo que cambia es **qué representación se modifica ahora, qué estado consulta el lector y qué mantenimiento queda pendiente**. Esa terna explica más que memorizar nombres de estructuras.

## La comparación física

| Variante | Qué guarda una escritura nueva | Qué necesita una lectura | Mantenimiento pendiente | Costo que intenta mejorar |
|---|---|---|---|---|
| CoW | Copias privadas de las páginas afectadas y sus ancestros | Una raíz de snapshot y sus páginas | Reutilizar páginas que ninguna vista necesita | Integridad y lectura concurrente de páginas |
| Lazy por página | Actualizaciones asociadas a la página | Base más cambios visibles | Reconciliar y gestionar memoria | Reescrituras repetidas de la misma página |
| LA-Tree | Operaciones en buffers de subárboles | Base y buffers pertinentes de la ruta | Propagar lotes y resolver cambios estructurales | Trabajo repetido en grupos de páginas |
| FD-Tree | Entradas en el head tree | Cabeza, runs y fences, con resolución de versiones | Fusionar runs y eliminar tombstones seguros | Muchas escrituras aleatorias pequeñas |
| Bw-Tree | Un delta nuevo y publicación de la cabeza | Mapeo de ID a cadena y reconstrucción | Consolidar, completar SMO y reclamar piezas | Reescritura de bases y exclusión por latches |
| Cache-oblivious | Cambios en estructura con localidad recursiva y huecos | Índice y array con posiciones vigentes | Redistribuir ventanas y mantener referencias | Transferencias en distintos niveles de memoria |

La tabla presenta los mecanismos del capítulo, no una clasificación de productos actuales. Los nombres de motores sirven como ejemplos del texto; cada implementación añade protocolos que esta comparación no detalla.

## Cinco términos que no conviene confundir

**Reconciliación** construye una representación física a partir de una base y cambios en memoria. **Consolidación** acorta la representación de un nodo lógico reuniendo base y deltas. **Fusión de runs** combina secuencias ordenadas de niveles. **Merge estructural** une nodos y modifica relaciones del árbol. **Reclamación** libera recursos cuando ya no pueden ser usados.

Podrían ocurrir juntos en una implementación, pero responden a condiciones diferentes. Una consolidación puede mantener el mismo rango y número de hijos; un merge modifica el árbol. Publicar una base nueva puede completar una consolidación y aún dejar pendiente la reclamación de su cadena vieja.

## Inmutabilidad aparece en lugares distintos

En CoW, la página de una versión publicada permanece estable; la nueva versión usa páginas copiadas. En FD-Tree, los runs son inmutables, pero la cabeza es mutable. En Bw-Tree, base y deltas publicados permanecen estables, pero la tabla de mapeo cambia.

Por tanto, “este sistema usa inmutabilidad” no permite deducir si lee con una raíz de snapshot, busca varios niveles o sigue una cadena. Hay que identificar la unidad inmutable y el punto mutable que publica el cambio.

## La misma operación: cambiar 70 de A a B

| Diseño | Camino simplificado de la modificación |
|---|---|
| CoW | Copiar hoja → cambiar 70 → copiar ancestros → publicar raíz |
| Lazy por página | Añadir actualización 70:B → resolverla en lectura → reconciliar después |
| LA-Tree | Registrar 70:B arriba → propagar por su rango → materializar por lote |
| FD-Tree | Registrar 70:B en cabeza → fusionar hacia runs → reemplazar versión vieja al resolver |
| Bw-Tree | Crear PUT(70,B) → enlazar a cabeza vigente → publicar mediante CAS |

Los cinco caminos pueden representar el mismo resultado lógico. Los bytes, las lecturas auxiliares y los puntos de coordinación son distintos. La latencia inmediata no mide todo el trabajo: una respuesta rápida puede dejar fusiones o consolidaciones pendientes.

## Preguntas útiles para evaluar un diseño

1. ¿Los cambios se concentran en pocas páginas o se dispersan? El buffering por página gana más oportunidad de agrupar cuando existe repetición.
2. ¿Predominan lecturas puntuales o rangos? Ambos necesitan resolver versiones, pero un rango combina muchas claves y puede pagar más por estructuras auxiliares.
3. ¿Cuánto duran los lectores? Los lectores largos pueden retener páginas CoW o piezas retiradas en un esquema por épocas.
4. ¿Qué ocurre cuando el mantenimiento no alcanza a las escrituras? Debe haber límites, presión de memoria o mecanismos de regulación; acumular deuda no es una solución permanente.
5. ¿Cómo se recupera la publicación tras un fallo? La atomicidad en memoria no sustituye la persistencia.
6. ¿La carga modifica claves existentes o añade nuevos rangos? Cambia la oportunidad de amortizar, la frecuencia de splits y el comportamiento del layout.

Estas preguntas son elaboración didáctica, no recomendaciones de compra ni resultados de un benchmark. El capítulo explica mecanismos, pero no aporta una medición común que permita ordenar universalmente todas las variantes.

## Conexión con lo estudiado antes

Los [[Obsidian/lecturas/database internals/03 Formatos de archivo/04 Slotted pages e indirección|slots]] y la tabla de mapeo del Bw-Tree comparten la idea de **indirección**: un identificador evita que todo usuario dependa de una dirección que cambia. Operan en escalas diferentes: una página y un nodo lógico distribuido en piezas.

Los [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/02 Rightmost pointers high keys y overflow|límites de rango y high keys]] ayudan a entender por qué un split delta puede redirigir una búsqueda cuando el padre aún no refleja la división. La invariante útil sigue siendo que cada clave tenga un camino correcto y que los separadores describan rangos coherentes.

La [[Obsidian/lecturas/database internals/01 Introducción y panorama general/02 Memoria disco y durabilidad|durabilidad]] permanece transversal: un buffer, una raíz o una tabla de mapeo no bastan por estar en RAM. El siguiente capítulo del libro desarrolla LSM-Trees; este escaneo solo los menciona como conexión y no contiene ese capítulo.

> [!question]- ¿Cuál es la variante “mejor” si solo sabemos que el hardware usa SSD?
> No alcanza para decidir. Faltan tamaños, distribución de claves, lecturas, duración de snapshots, concurrencia, recursos y política de durabilidad. El SSD cambia costos; no determina todo el workload.

> [!question]- ¿Qué tienen en común las optimizaciones del capítulo?
> Separan el trabajo lógico del cambio físico inmediato. Esa separación ahorra ciertos costos, pero exige reglas para reconstruir, publicar y mantener el estado correcto.

**Referencia:** PDF 17–18 · impresas 127–128. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=17|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/08 Cache-oblivious layout vEB y packed arrays|Anterior]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/10 Laboratorio y repaso resuelto|Siguiente]] →
