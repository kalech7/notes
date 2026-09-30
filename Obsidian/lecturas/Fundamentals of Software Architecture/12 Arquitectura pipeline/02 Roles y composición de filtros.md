---
title: "12 · Los cuatro roles y la composición"
created: 2026-09-29
capitulo: 12
tags:
  - lecturas/software-architecture
  - arquitectura/pipeline
---

# Los cuatro roles y la composición

[[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/00 Índice|← Índice del capítulo 12]]

**Los cuatro roles describen el papel de una etapa en el flujo.** «Filtro» es el nombre general del componente; solo uno de sus tipos, el tester, se dedica a decidir qué datos continúan. Por tanto, un filtro no siempre elimina datos.

## 1. Productor, transformador, tester y consumidor

| Rol del libro | Función | Entrada/salida dentro del pipeline | Ejemplo propio |
|---|---|---|---|
| **Productor** (*producer*, también *source*) | Iniciar el flujo obteniendo datos | Salida hacia otras etapas | Leer un archivo CSV |
| **Transformador** (*transformer*) | Cambiar, enriquecer o calcular datos | Entrada y salida | Convertir precios a centavos y calcular importe |
| **Tester** | Evaluar un criterio y decidir si continuar o qué ruta seguir | Entrada; salida opcional según la decisión | Rechazar cantidades negativas o clasificar una métrica |
| **Consumidor** (*consumer*, también *sink*) | Terminar el flujo usando el resultado | Entrada, sin siguiente etapa de procesamiento | Guardar un informe o mostrarlo |

Un productor sí puede leer un archivo, una base o un mensaje externo. «Solo salida» describe su conexión con el **interior del pipeline**, no que no reciba información de ningún sitio. Igualmente, un consumidor puede devolver confirmación al ejecutor; sigue siendo el final del recorrido funcional de los datos.

El transformador puede cambiar todos los campos, algunos o incluso pasar el dato sin cambio cuando no hay transformación aplicable. Su responsabilidad sigue siendo la transformación definida. El tester puede actuar como una compuerta («importe mínimo de cinco dólares») o como selector de una rama. **Tester aquí no significa una prueba unitaria ejecutada por el equipo de QA**: es una etapa del sistema que examina datos durante su funcionamiento.

## 2. Map, selección y reduce no son lo mismo

El capítulo relaciona el transformador con `map`: aplicar una función a cada elemento para obtener resultados transformados. Esa analogía es útil. Relaciona el tester con `reduce`, pero el ejemplo que ofrece —continuar o descartar según una condición— se parece más a **filtrar** o a **enrutar**.

Una reducción combina elementos en un acumulador: sumar `[2, 3, 4]` produce `9`. Una selección deja pasar los que cumplen un predicado: conservar valores mayores que `2` produce `[3, 4]`. Es posible construir una selección usando una reducción, pero no son la misma operación. Esta precisión es externa al libro y coincide con la definición de [reduce en la documentación de Python](https://docs.python.org/3/library/functools.html#functools.reduce).

| Operación | Entrada propia | Salida | Pregunta |
|---|---|---|---|
| Transformar | `[2, 3, 4]` | `[4, 6, 8]` | ¿Qué valor corresponde a cada dato? |
| Seleccionar | `[2, 3, 4]` | `[3, 4]` | ¿Qué datos cumplen la condición? |
| Reducir | `[2, 3, 4]` | `9` | ¿Qué acumulado representa el conjunto? |

Un filtro arquitectónico puede implementar cualquiera de estas operaciones; el rol lo determina su responsabilidad en ese flujo, no el nombre de una función de biblioteca.

## 3. Por qué la composición permite reutilizar

Si un lector entrega palabras, un normalizador entrega palabras en minúsculas y un contador recibe palabras, se pueden combinar sin que cada uno conozca a todos los demás. Después se puede cambiar el origen de archivo a entrada de consola manteniendo el contador.

El libro ilustra la idea con la anécdota de un problema de palabras frecuentes: contar las palabras de un texto y mostrar las más usadas. El relato contrapone un programa extenso en Pascal con una cadena pequeña de utilidades Unix. La enseñanza es que piezas ya disponibles se pueden componer para resolver un trabajo nuevo; no demuestra que cualquier problema deba resolverse con comandos de shell.

## 4. Un ejemplo equivalente explicado

Esta variante didáctica conserva la idea, añade un archivo explícito y muestra las tres primeras palabras. Está pensada para texto ASCII en inglés; no es un tokenizador adecuado para español o Unicode.

```bash
export LC_ALL=C
tr -cs 'A-Za-z' '\n' < texto.txt |
  tr 'A-Z' 'a-z' |
  sed '/^$/d' |
  sort |
  uniq -c |
  sort -rn |
  head -n 3
```

`LC_ALL=C` fija el tratamiento de caracteres y la ordenación para este ejemplo. El primer `tr` sustituye secuencias de caracteres que no son letras por saltos de línea; el segundo pasa mayúsculas a minúsculas. `sed` elimina líneas vacías, `sort` agrupa palabras iguales y `uniq -c` cuenta repeticiones contiguas. El último ordenamiento pone primero las frecuencias grandes y `head` limita la salida. El requisito de adyacencia de `uniq` y las opciones de `tr` se contrastaron con los manuales de [GNU uniq](https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html) y [GNU tr](https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html).

Para `Blue blue red BLUE green red`, la secuencia de palabras normalizadas es `blue, blue, red, blue, green, red`. Tras ordenar queda `blue, blue, blue, green, red, red`; el conteo da `3 blue`, `1 green`, `2 red`, y la salida final coloca `blue`, `red`, `green` en ese orden.

## 5. Sus límites también enseñan arquitectura

`sort` necesita reunir y ordenar datos antes de terminar: una cadena de etapas no garantiza que todas produzcan salida inmediatamente. La tokenización ASCII rompe palabras con tildes. Y si dos palabras empatan, hay que definir si el desempate importa para el negocio.

Reutilizar exige contratos compatibles y supuestos conocidos. Una utilidad excelente para una entrada puede ser incorrecta para otra aunque técnicamente conecte con la siguiente.

> [!question]- ¿Por qué no basta con `uniq -c` para contar `blue, red, blue`?
> Porque las dos apariciones de `blue` no son contiguas. Ordenar primero las agrupa y permite que el conteo represente la frecuencia total.

> [!question]- ¿Guardar en una base vuelve consumidor a cualquier filtro?
> No necesariamente. El analizador de tendencias del libro guarda resultados y luego los entrega a otra etapa; conserva el rol de transformador. El consumidor se reconoce porque termina el procesamiento de ese flujo.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/09 Arquitectura pipeline.pdf#page=2|PDF 2–3 · impresas 182–183 · tipos de filtros y ejemplo Unix]]

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/01 Topología filtros y canales|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/03 Contratos sincronía y rendimiento|Siguiente →]]
