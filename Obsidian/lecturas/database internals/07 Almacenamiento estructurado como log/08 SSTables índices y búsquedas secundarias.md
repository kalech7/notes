---
title: "Database Internals — Capítulo 7 · SSTables índices y búsquedas secundarias"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# SSTables índices y búsquedas secundarias

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] La pregunta concreta
> Ya sabemos que una tabla de disco es inmutable y ordenada. Ahora veremos cómo se transforma una clave en una posición física y cómo se busca por otro campo.

## Dos componentes, aunque compartan archivo

Una **SSTable**, *Sorted String Table*, almacena registros en orden de clave. Tiene un componente de datos y uno de índice. Pueden ocupar archivos distintos o regiones del mismo archivo; la organización conceptual no obliga a un número de archivos fijo.

El componente de datos contiene registros concatenados. El índice asocia claves o separadores de bloques con **offsets**, distancias en bytes desde el inicio del archivo, y tamaños. Ejemplo propio: el índice señala `10→0`, `30→180`, `50→360`; para buscar 35 se entra al bloque cuyo separador es 30 y se busca dentro de ese bloque. El índice puede ser disperso: no necesita una entrada por registro si cada entrada identifica un bloque con varias claves.

Los offsets se conocen cuando se construye el archivo. Como la tabla publicada no cambia, ningún registro posterior desplaza físicamente otro y no hay que reparar posiciones tras cada actualización. Durante compactación se crean offsets nuevos para un archivo nuevo.

## Orden y estructura del índice son decisiones separadas

Un B-Tree o un índice ordenado facilita localizar el primer registro mayor o igual que el límite inicial de un rango. Después se recorre el archivo secuencialmente. Un hash puede acelerar una consulta exacta, pero por sí solo no determina el sucesor ordenado de una clave ausente. Para un rango que empieza en una clave inexistente necesita otro mecanismo que encuentre la primera clave válida.

La afirmación del capítulo de que un índice hash no impide rangos debe entenderse con ese requisito: el archivo sí conserva orden, aunque la estructura que localiza el comienzo debe aportar la posición adecuada. Orden físico y API de búsqueda del índice no son equivalentes.

## Qué cambia con un índice secundario

La **clave primaria** identifica el registro principal. Un **índice secundario** permite buscar por otro campo, como ciudad, y devuelve claves primarias candidatas. Buscar `ciudad=Quito` puede producir identificadores 8 y 19, que luego se verifican y recuperan en el almacenamiento principal.

El capítulo describe **SASI**, *SSTable-Attached Secondary Indexes*, como ejemplo histórico de Cassandra: cada SSTable tiene estructuras secundarias que nacen, se compactan y se retiran junto con ella. La memtable conserva su contraparte en memoria. Construir el índice durante flush o compactación aprovecha que el motor ya recorre los registros.

Si un registro antiguo dice Quito y uno nuevo Guayaquil, un índice viejo puede seguir proponiendo la clave. La consulta necesita reconciliar y verificar la versión visible antes de devolverla. Un candidato del índice no demuestra que el registro actual satisfaga el predicado.

## Un recorrido razonable de consulta

Primero se descartan tablas cuyos rangos no contienen la clave. Para una consulta puntual, se revisa su filtro Bloom. En las restantes, el índice localiza un bloque, la caché o el disco lo entrega, se decodifican registros y se resuelven versiones con las demás fuentes. Cada etapa evita un costo distinto; ninguna sustituye la reconciliación.

> [!question]- ¿Por qué compactar puede construir un índice sin hacer búsquedas repetidas?
> Porque los registros ya se recorren en orden y se conoce cada nueva posición al escribirla. El motor puede producir índices y metadatos junto con los datos, en lugar de consultar y modificar el archivo de salida registro por registro.

**Puente al siguiente tema:** incluso un índice eficiente cuesta algo al consultarlo. El filtro Bloom responde una pregunta más barata: ¿podemos descartar esta tabla completa?

**Referencia:** PDF 17–18 · impresas 145–146. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=17|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/07 Amplificación y la conjetura RUM|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/09 Filtros Bloom y falsos positivos|Siguiente]] →
