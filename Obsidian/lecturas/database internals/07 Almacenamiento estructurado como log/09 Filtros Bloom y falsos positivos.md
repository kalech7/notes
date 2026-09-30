---
title: "Database Internals — Capítulo 7 · Filtros Bloom y falsos positivos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Filtros Bloom y falsos positivos

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] Para situar el filtro
> Una clave puede pertenecer al rango de un archivo y aun así no existir allí. El filtro Bloom reduce esas búsquedas innecesarias usando una pequeña cantidad de memoria.

## Un resumen probabilístico de pertenencia

Un **filtro Bloom** es un arreglo de bits y varias funciones hash. Una función **hash** transforma una clave en un número; ese número determina una posición del arreglo. Al insertar una clave se ponen en 1 sus posiciones. Para consultarla se calculan las mismas posiciones.

Si cualquiera está en 0, la clave no se insertó en ese filtro. Si todas están en 1, la clave **puede** estar presente: otras claves pudieron encender esas posiciones. Una respuesta positiva es un permiso para buscar en la tabla, no un valor ni una prueba de presencia.

## El ejemplo verificado del libro

El filtro tiene 16 posiciones, numeradas 0–15, y tres hashes:

| Clave | Posiciones | Resultado después de insertar key1 y key2 |
|---|---|---|
| key1 | 3, 5, 10 | Insertada |
| key2 | 5, 8, 14 | Insertada |
| key3 | 3, 10, 14 | Positivo aunque no se insertó |
| key4 | 5, 9, 15 | Negativo porque 9 y 15 están a cero |

La posición 5 es compartida por dos claves: una **colisión**. El filtro guarda bits, no quién los encendió. key3 combina posiciones encendidas por claves distintas y por eso produce un **falso positivo**.

El filtro Bloom estándar no tiene falsos negativos para elementos realmente insertados, si se usa completo y correctamente. Eso presupone funciones coherentes, ausencia de corrupción y que todas las claves relevantes hayan sido incluidas. Las marcas de borrado puntuales también representan información para la clave y deben contemplarse. Los borrados de rango necesitan su propio tratamiento: un filtro de claves puntuales no basta para probar que ninguna marca de rango afecta una consulta.

## Más hashes no siempre es mejor

El capítulo simplifica diciendo que revisar más hashes puede mejorar precisión. Con tamaño fijo, llega un punto en que muchos hashes saturan el arreglo y empeoran los falsos positivos. La relación depende del número de claves, bits y hashes.

Como elaboración matemática propia, para n claves, m bits y k hashes aproximadamente independientes:

$$p \approx (1-e^{-kn/m})^k$$

El número k que minimiza esa aproximación está cerca de `(m/n) ln 2`. Con 10 bits por clave, k≈6,93; siete hashes producen una probabilidad aproximada de 0,82 %. Con 100 tablas que no contienen la clave esperaríamos alrededor de 0,82 falsos positivos, además de trabajo de metadatos y filtros. Es una expectativa del modelo, no una garantía por consulta ni un benchmark.

## Lo que ahorra y lo que cuesta

Un filtro negativo permite omitir la búsqueda de datos en esa SSTable. Aumentar bits usa RAM o espacio de caché; calcular hashes usa CPU. Las SSTables inmutables ayudan porque su conjunto de claves se conoce al construir el filtro, y no necesita mantenimiento registro por registro después.

No se deben borrar bits de un Bloom estándar para eliminar una clave: un bit puede estar compartido y se crearían falsos negativos. Al retirar una SSTable se retira su filtro entero; una compactación crea un filtro nuevo para sus salidas.

> [!question]- ¿Un Bloom positivo para una clave implica que sigue viva?
> No. Podría ser un falso positivo, una versión vieja o un tombstone. La tabla y la reconciliación determinan el resultado lógico.

**Puente al siguiente tema:** los filtros resumen tablas de disco. En memoria necesitamos otra estructura: mantener orden mientras llegan inserciones concurrentes.

**Referencia:** PDF 19–21 · impresas 147–149 · figura 7-7. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=19|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/08 SSTables índices y búsquedas secundarias|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/10 Skiplists caché y bloques comprimidos|Siguiente]] →
