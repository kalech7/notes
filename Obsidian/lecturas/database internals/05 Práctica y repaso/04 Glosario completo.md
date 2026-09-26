---
title: "Glosario — Database Internals"
type: glossary
tags:
  - lecturas/database-internals
  - glosario
---

# Glosario — Database Internals

Los términos están explicados según su función dentro de un motor de almacenamiento, no solo como definiciones aisladas.

## A–C

**Access method / método de acceso**
: Estructura y algoritmos que permiten localizar registros —por ejemplo, B-Tree o tabla hash— sin escanear todo el archivo.

**Amplificación de escritura**
: Relación entre bytes escritos físicamente y bytes que el usuario pidió modificar. Splits, logs, compacción y reescrituras pueden hacerla mayor que uno.

**B-Tree**
: Árbol de búsqueda balanceado y de alto fanout, diseñado para reducir accesos a páginas. En la práctica, “B-Tree” suele abarcar variantes donde los valores se concentran en hojas.

**Binary search / búsqueda binaria**
: Algoritmo que descarta la mitad del espacio ordenado en cada comparación. Dentro de una página puede operar sobre offsets y seguir indirecciones hacia las celdas.

**Breadcrumb**
: Entrada en una pila en memoria que recuerda un nodo y el hijo elegido durante el descenso. Permite propagar splits o merges hacia la raíz.

**Buffer manager**
: Componente que decide qué páginas de disco permanecen en memoria, traduce page IDs a frames y coordina carga, expulsión y flush.

**Bulk loading**
: Construcción de un índice desde datos preordenados, formando hojas y luego niveles superiores, en vez de realizar inserts individuales.

**Cell / celda**
: Unidad lógica dentro de una página; puede contener clave, valor, metadatos y/o punteros.

**Checksum**
: Resumen calculado sobre bytes para detectar corrupción. No suele buscar seguridad criptográfica, sino errores accidentales con bajo costo.

**Clustered index**
: Índice cuyo orden determina el orden físico o primario de los registros. Solo puede existir un orden físico principal por conjunto de datos.

**Column-oriented store**
: Layout que agrupa valores de la misma columna. Favorece proyecciones, agregaciones, compresión y procesamiento vectorizado.

**Compactación / vacuum**
: Proceso que reescribe contenido vivo, recupera huecos dejados por datos inalcanzables y devuelve páginas vacías a la freelist.

## D–H

**Data file**
: Archivo que almacena registros de datos. Puede ser heap, hash-organized o index-organized.

**DBMS**
: Sistema de gestión de bases de datos. Integra consultas, ejecución, transacciones, concurrencia, recovery y almacenamiento.

**Endianness**
: Orden de los bytes de un valor multibyte. Big-endian coloca primero el byte más significativo; little-endian, el menos significativo.

**Execution engine**
: Componente que ejecuta los operadores de un plan y solicita datos a los métodos de acceso.

**Fanout**
: Número de hijos que puede referenciar un nodo interno. Un fanout alto reduce la altura del árbol y los page reads por búsqueda.

**Freelist**
: Estructura persistente de page IDs disponibles para reutilizar. Debe sobrevivir a reinicios sin perder ni duplicar páginas.

**Fragmentación interna de página**
: Situación en la que el espacio libre existe pero está repartido en huecos; puede impedir una inserción que requiere bytes contiguos.

**Hash file**
: Organización que usa el hash de una clave para escoger bucket. Es buena para igualdad, pero no conserva orden para rangos.

**Heap file**
: Archivo donde los registros no siguen un orden de clave obligatorio. Facilita inserción, pero requiere índices o escaneo para localizar valores.

**High key**
: Límite superior explícito del rango cubierto por un nodo. Ayuda a representar el extremo derecho y a navegar bajo cambios concurrentes.

**HTAP**
: Procesamiento híbrido transaccional y analítico. Intenta servir OLTP y OLAP sobre un sistema o datos estrechamente integrados.

## I–P

**Índice primario**
: Índice principal usado para organizar o identificar registros. Según el motor, puede coincidir con el almacenamiento de las filas.

**Índice secundario**
: Índice adicional sobre otra clave. Su hoja suele guardar un identificador de fila o la clave primaria, introduciendo una segunda búsqueda.

**In-place update**
: Modificación que intenta actualizar la ubicación existente. Reduce versiones adicionales, pero puede causar escrituras aleatorias y exigir logging cuidadoso.

**LSN (Log Sequence Number)**
: Posición monotónica en el log usada para ordenar cambios y recovery. Puede guardarse en el encabezado de página.

**Magic number**
: Constante binaria en una posición conocida que ayuda a reconocer tipo, formato o alineación de un bloque.

**Merge**
: Combinación de nodos con poca ocupación. Recupera densidad y puede propagarse hacia arriba si el padre pierde un separador.

**MVCC**
: Control de concurrencia multiversión. Conserva versiones para que transacciones con distintos snapshots puedan leer estados coherentes.

**OLAP**
: Procesamiento analítico: escaneos, agregaciones y consultas sobre muchas filas, normalmente con menos escrituras puntuales.

**OLTP**
: Procesamiento transaccional: operaciones breves, concurrentes y selectivas que leen o modifican pocos registros.

**Overflow page**
: Página que contiene la continuación de un payload demasiado grande para guardarse completo en la página primaria.

**Page / página**
: Unidad lógica de transferencia, caché y organización del motor. Suele tener tamaño fijo aunque los registros sean variables.

**Page header**
: Metadatos que describen tipo, versión, celdas, espacio libre, enlaces y otras propiedades necesarias para interpretar una página.

**Page ID**
: Identificador estable o lógico de una página. El buffer manager o la capa de archivos lo traduce a una ubicación.

**Point query**
: Consulta por una clave concreta, a diferencia de un rango.

## Q–Z

**Query processor**
: Analiza, valida y optimiza consultas para producir un plan de ejecución.

**Range query**
: Consulta por un intervalo ordenado. Los B-Trees la facilitan porque conservan el orden y suelen enlazar hojas.

**Rebalanceo**
: Redistribución de entradas entre hermanos para mejorar ocupación y posponer splits o merges.

**Recovery manager**
: Componente que usa log y metadatos para llevar la base a un estado correcto tras un fallo.

**Rightmost pointer**
: Puntero al intervalo final de un nodo interno. Con `N` separadores existen `N + 1` hijos, por lo que uno puede quedar sin clave pareja.

**Row-oriented store**
: Layout que mantiene juntos los campos de una fila. Favorece lecturas y escrituras de registros completos.

**Separator key**
: Clave de un nodo interno que divide rangos y guía hacia un hijo; no necesariamente es un registro de usuario completo.

**Serialization / serialización**
: Conversión de tipos y estructuras a bytes mediante un contrato de layout, orden, longitudes y versiones.

**Sibling link**
: Puntero directo entre páginas del mismo nivel. Acelera recorridos laterales, pero complica splits, merges y concurrencia.

**Slotted page**
: Layout donde un arreglo ordenado de offsets crece desde un extremo y las celdas variables desde el otro. Separa orden lógico de ubicación física.

**Split**
: División de un nodo sin espacio en dos nodos y promoción de una clave al padre. Puede propagarse hasta crear una raíz nueva.

**Storage engine**
: Subsistema responsable de almacenar, recuperar y modificar datos en memoria y disco, exponiendo primitivas a capas superiores.

**Tombstone**
: Marcador lógico de eliminación. Evita o pospone la reescritura inmediata, pero debe procesarse posteriormente.

**Write-ahead log (WAL)**
: Log que registra un cambio antes de que la página modificada se considere persistida. Permite redo/undo según el protocolo.

## Navegación

- [[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]]
- [[Obsidian/lecturas/database internals/01 Introducción y panorama general/00 Índice|Capítulo 1 · Introducción y panorama general]]
- [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/00 Índice|Capítulo 2 · Fundamentos de B-Trees]]
- [[Obsidian/lecturas/database internals/03 Formatos de archivo/00 Índice|Capítulo 3 · Formatos de archivo]]
- [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/00 Índice|Capítulo 4 · Implementación de B-Trees]]

**Anterior:** [[Obsidian/lecturas/database internals/05 Práctica y repaso/03 Ejercicios integradores|Ejercicios integradores]] · **Índice:** [[Obsidian/lecturas/database internals/05 Práctica y repaso/00 Índice|Práctica y repaso]]
