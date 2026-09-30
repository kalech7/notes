---
title: "Database Internals — Copy-on-write y snapshots en LMDB"
created: 2026-09-30
libro: "Database Internals"
capitulo: 6
tags:
  - lecturas/database-internals
  - arquitectura/b-trees
  - arquitectura/copy-on-write
  - arquitectura/concurrencia
---

# Copy-on-write y snapshots en LMDB

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Capítulo 6]]

**Copy-on-write**, abreviado **CoW**, significa copiar antes de escribir. Cuando una página publicada debe cambiar, el escritor crea una copia, modifica esa copia y deja intacta la versión que ya pueden estar usando los lectores.

La regla importante es que las páginas **publicadas** son inmutables mientras pertenezcan a esas versiones. El escritor puede trabajar en sus páginas privadas antes de publicarlas. No hay que copiar todo el árbol: solo las páginas afectadas y los ancestros que deben apuntar a las copias nuevas.

## Por qué cambiar una hoja obliga a copiar sus ancestros

Imaginemos `raíz R0 → rama I0 → hoja L0`, con `70=10` en L0. Queremos publicar `70=12`:

1. Crear L1 con el contenido de L0 y el nuevo valor 12.
2. Crear I1 a partir de I0, sustituyendo su referencia a L0 por L1.
3. Crear R1 a partir de R0, sustituyendo I0 por I1.
4. Completar las nuevas páginas y publicar la nueva raíz de forma atómica.

Si cambiáramos I0 directamente para apuntar a L1, un lector de R0 podría encontrar el valor nuevo y perder su vista antigua. Copiar el camino mantiene coherente cada versión completa.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 06/01-copy-on-write.png]]

Las cajas naranjas pertenecen al camino anterior y las verdes al camino nuevo. Las azules se comparten porque no cambió su contenido. R1 conduce a L1 para la clave 70, pero reutiliza las demás ramas. Un lector que ya conserva R0 continúa obteniendo 10; uno que empieza con R1 obtiene 12. Las flechas representan referencias entre páginas, no copias completas del árbol.

Con tres páginas de 4096 bytes, el ejemplo puede escribir `3 × 4096 = 12288 bytes` por un cambio de 16 bytes: `12288 / 16 = 768`. Es un caso simplificado con un cambio aislado, sin splits ni metadatos. Una transacción que modifica varias claves de la misma hoja puede reutilizar las copias privadas y amortizar parte de ese costo.

## Una raíz publicada actúa como snapshot

Un **snapshot** es una vista consistente de una versión de los datos. El lector toma una raíz y navega páginas que el escritor no transformará bajo sus pies. La coexistencia de esas versiones ofrece **MVCC**, control de concurrencia con múltiples versiones.

Los lectores no necesitan un latch para impedir que se edite la página que están leyendo. Pero aún hay coordinación para elegir la raíz, registrar lectores y evitar reutilizar páginas vivas. Los escritores también necesitan coordinación entre ellos. CoW simplifica un conflicto específico: leer páginas que otro hilo modifica en el sitio.

## Publicar una raíz y sobrevivir a un fallo

```mermaid
flowchart LR
 A[Preparar páginas privadas] --> B[Persistir páginas nuevas]
 B --> C[Publicar y persistir raíz nueva]
 C --> D[Confirmar bajo la política de durabilidad]
 D --> E[Retirar páginas antiguas cuando sea seguro]
```

La nueva raíz solo sirve para recuperarse si sus páginas ya son recuperables. Un cambio de puntero atómico en RAM evita una observación intermedia por otros hilos; el protocolo de persistencia evita que un reinicio seleccione una raíz que apunta a páginas que no llegaron al almacenamiento estable. La figura condensa el orden conceptual, no un procedimiento universal de `fsync`.

Antes de publicar R1, la versión R0 sigue siendo válida. Después de publicar R1 de manera durable, puede recuperarse el estado nuevo. El espacio de páginas preparadas que nunca se publicaron tendrá que gestionarse como espacio no utilizado. Por eso CoW cambia el protocolo de recuperación, pero no elimina el problema de la recuperación.

**Referencia:** PDF 2–2 · impresas 112 · figura 6-1. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=2|Fuente del capítulo]].

## LMDB como ejemplo del capítulo

**LMDB**, *Lightning Memory-Mapped Database*, es el ejemplo de CoW del libro. Un archivo **mapeado en memoria** permite acceder a los bytes del archivo mediante direcciones de memoria; el sistema operativo se ocupa de traer sus páginas. Eso no significa que el archivo entero quepa en RAM ni que una página nunca falle en caché.

El capítulo describe una arquitectura que evita una caché adicional propia del motor y un WAL tradicional. **WAL**, *write-ahead log*, es el registro de cambios que otros motores persisten antes de las páginas de datos. LMDB se apoya en versiones y publicación de metadatos para conservar un estado consistente.

Symas confirma que LMDB usa la caché del sistema operativo y serializa las escrituras. Los lectores pueden continuar mientras trabaja el escritor. [Descripción oficial de LMDB](https://www.symas.com/lmdb.php).

> [!note] Dos páginas de metadatos no equivalen a solo dos snapshots vivos
> La impresa 113 habla de dos versiones de la raíz. El código de LMDB distingue **dos páginas de metadatos que se alternan al confirmar**, y también rastrea la transacción lectora más antigua para reutilizar páginas. Pueden coexistir lectores con vistas anteriores: no se debe interpretar aquella frase como un límite de dos transacciones lectoras o dos estados alcanzables. [Código de LMDB: `MDB_meta`, `NUM_METAS` y `mdb_find_oldest`](https://github.com/LMDB/lmdb/blob/mdb.master/libraries/liblmdb/mdb.c).

El libro señala además que los recorridos ordenados pueden volver a los padres al no usar enlaces laterales de hojas en este diseño. La idea es evitar referencias laterales que compliquen mantener las distintas versiones del árbol. Es una decisión de la implementación descrita, no una prohibición general sobre toda estructura CoW.

## Cuándo reaparece el costo

Un lector largo puede mantener páginas antiguas vivas aunque la raíz actual ya no las alcance. Mientras exista ese lector, esas páginas no se pueden reutilizar sin alterar su snapshot. El costo queda en espacio retenido, además de las copias y del tráfico de escritura. Una vez que ninguna versión activa necesita una página antigua, puede volver al conjunto reutilizable.

> [!question]- ¿Una página compartida se puede liberar cuando termina el lector más antiguo?
> Solo si ninguna raíz ni operación vigente la necesita. Compartida significa precisamente que puede pertenecer también a la versión nueva. Terminar un lector no vuelve libre todo su árbol.

> [!question]- ¿Qué gana CoW si puede escribir más páginas que una actualización en el sitio?
> Una publicación con versiones completas y páginas estables para lectores. El objetivo principal aquí es simplificar integridad y lectura concurrente; el costo por escritura depende del trabajo concreto.

**Referencia:** PDF 3–3 · impresas 113. [[Obsidian/lecturas/database internals/Materiales/06 Variantes de B-Trees.pdf#page=3|Fuente del capítulo]].

---

← [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/01 El costo de modificar un B-Tree y representar sus nodos|Anterior]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/06 Variantes de B-Trees/03 Lazy B-Trees y reconciliación en WiredTiger|Siguiente]] →
