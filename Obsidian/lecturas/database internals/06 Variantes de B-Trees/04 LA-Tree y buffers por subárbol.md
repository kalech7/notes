---
title: "Database Internals — LA-Tree y buffers por subárbol"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - arquitectura/buffers
  - arquitectura/almacenamiento
---

# LA-Tree y buffers por subárbol

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

WiredTiger ilustra cambios asociados a páginas. El **Lazy-Adaptive Tree**, o **LA-Tree**, amplía el alcance del buffer: asocia las operaciones a un **subárbol**, la región que contiene un nodo y todos sus descendientes. Así puede reunir modificaciones de varias hojas antes de repartirlas.

La adaptación que explica el capítulo consiste en mover trabajo en lotes por una jerarquía de buffers. Las operaciones entran arriba, se separan según el rango al que pertenecen y descienden cuando corresponde vaciar el buffer. Esto no convierte las hojas finales en runs inmutables: el diseño continúa aplicando cambios al árbol.

## Un lote puede contener destinos distintos

Supongamos un separador 50: las claves menores que 50 van al subárbol izquierdo y las restantes al derecho. El buffer superior recibe:

`PUT(12,a), PUT(18,b), DELETE(70), PUT(80,c)`

Al propagarse, se divide en dos lotes. El izquierdo lleva 12 y 18; el derecho lleva el borrado de 70 y la inserción de 80. Si un buffer inferior también se llena, la propagación continúa hasta llegar a las hojas. Cuando se aplica el lote en una hoja, se resuelven juntas las inserciones, actualizaciones y eliminaciones que afectan a esa región.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/04-la-tree.png]]

La caja superior contiene las operaciones que aún no llegaron a las hojas. El separador 50 determina los destinos verde y violeta. Las cajas azules representan la materialización final por lotes. Una búsqueda de 80 debe considerar el buffer que ya guarda su inserción aunque la hoja derecha todavía no la incluya; ese detalle conecta el recorrido de lectura con el recorrido de propagación.

Si seis operaciones cambian una hoja y otras cuatro cambian su vecina, el objetivo es visitar esas páginas y transformar sus contenidos por lote, evitando diez rondas independientes cuando sea posible. Los splits y merges resultantes pueden propagarse también agrupados. El número exacto de accesos depende de qué páginas ya estén cargadas y de cuánto trabajo estructural requiera el resultado.

## Leer mientras las operaciones todavía están arriba

El estado lógico puede estar repartido entre la hoja y los buffers de su ruta. La búsqueda localiza la base y reúne las operaciones que afectan a la clave o al rango consultado. Luego las reconcilia según su orden y visibilidad.

```mermaid
flowchart LR
 A[Consulta de una clave] --> B[Recorrer separadores]
 B --> C[Consultar buffers de la ruta]
 C --> D[Localizar estado base en la hoja]
 D --> E[Resolver cambios aplicables]
 E --> F[Devolver el estado visible]
```

Los pasos no obligan a una implementación a copiar todo el contenido de todos los buffers. Expresan qué información puede ser necesaria. Una consulta puntual puede filtrar por clave; un rango necesita combinar varias claves manteniendo orden y borrados. El resultado lógico debe ser el mismo antes y después de mover las operaciones físicamente hacia abajo.

## Una operación no debe aplicarse dos veces durante la propagación

Si copiamos una operación del buffer superior al inferior y durante un tiempo aparece en ambos, el lector no puede tratar las dos copias como dos operaciones independientes. Esto es especialmente evidente con `incrementar contador`: aplicarlo dos veces duplicaría el resultado. La propagación necesita un protocolo que preserve identidad, orden y visibilidad de cada cambio.

El capítulo presenta el mecanismo a alto nivel y no proporciona ese protocolo completo. El ejemplo anterior es una consecuencia de corrección elaborada para estudiar: los buffers permiten demorar la materialización, pero no alterar la historia lógica.

## Comparación con buffers por página

| Aspecto | Buffer asociado a página | Buffer asociado a subárbol |
|---|---|---|
| Destino que agrupa | Cambios de una página | Cambios de varias páginas bajo un nodo |
| Propagación representada | Reconciliar la página | Separar lotes y descender niveles |
| Información extra al leer | Actualizaciones de la página | Actualizaciones en buffers pertinentes de la ruta |
| Costo desplazado | Construcción de la imagen física | Reparto de operaciones y materialización por lotes |

Ambos reducen trabajo repetido, pero requieren memoria y lecturas auxiliares. Si una clave solo cambia una vez antes de cada reconciliación, queda menos repetición que amortizar. Si el buffer crece más rápido de lo que puede vaciarse, la escritura de fondo se convierte en deuda que el sistema debe pagar.

> [!question]- ¿Una inserción tiene que llegar a la hoja para que una lectura la vea?
> No necesariamente. Puede ser visible en un buffer. Lo indispensable es que la lectura consulte ese cambio y que el protocolo transaccional autorice verlo.

> [!question]- ¿LA-Tree y FD-Tree son lo mismo porque ambos agrupan cambios?
> No. LA-Tree hace descender cambios hacia páginas del árbol. FD-Tree transforma lotes en runs inmutables y fusiona niveles. El lugar donde queda la información después de materializarse es diferente.

**Referencia:** PDF 6–7 · impresas 116–117 · figura 6-4. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=6|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/03 Lazy B-Trees y reconciliación en WiredTiger|Anterior]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/05 FD-Tree runs fences y fractional cascading|Siguiente]] →
