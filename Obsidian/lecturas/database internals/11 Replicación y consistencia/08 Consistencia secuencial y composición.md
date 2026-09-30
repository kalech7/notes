---
title: "Database Internals — Capítulo 11 · Consistencia secuencial y composición"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Consistencia secuencial y composición

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

La **consistencia secuencial** exige que exista un único orden total de las operaciones que explique las respuestas y conserve el orden de programa de cada cliente. Relaja la obligación de respetar el tiempo real entre clientes distintos. Una escritura puede haber terminado antes de una lectura de otro cliente y aun aparecer después de ella en la explicación secuencial.

Ejemplo propio: Ana escribe 1 y luego 2. Todos los lectores deben poder encajar en un orden que coloque esas escrituras 1→2. Si Ana escribe 1 y Bruno escribe 2 de forma independiente, el orden compartido podría ser 1→2 o 2→1 aunque sus tiempos reales sugieran otra cosa. No se permite que unos lectores observen ambas escrituras en un orden y otros en el orden inverso dentro de la misma explicación global.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 11/04 Orden secuencial y causal.png]]

La tarjeta azul utiliza el mismo orden A→B→C para ambos lectores. La verde sólo obliga a que A preceda a B porque hay dependencia, y permite que C, independiente, aparezca en otra posición. El dibujo compara los contratos sin equiparar las secuencias mostradas con un calendario físico.

## Qué enseña la figura 11-5

El libro muestra dos escrituras de orígenes distintos: se escribió 1 antes que 2 según el reloj real, pero ambos lectores observan 2 y después 1. Bajo consistencia secuencial puede elegirse un orden global W2→W1. Los lectores pueden avanzar a velocidades distintas por esa misma historia: mientras uno ya llegó a 1, el otro todavía observa 2.

Esto no significa que cualquier lectura vieja sea válida. La explicación debe conservar **todas** las operaciones locales, incluyendo lecturas y escrituras, y existir para el conjunto completo. Si un cliente escribe y luego lee el mismo registro, su orden local condiciona el valor de esa lectura; no puede usar «la propagación tarda» para ignorar el contrato.

## Por qué no se compone por objeto

La propiedad secuencial de cada objeto por separado no implica consistencia secuencial del sistema combinado. Ejemplo propio, inicialmente `x=y=0`:

```text
P1: write(x,1); read(y) -> 0
P2: write(y,1); read(x) -> 0
```

Para x, podemos ordenar la lectura de P2 antes de la escritura de P1. Para y, podemos ordenar la lectura de P1 antes de la escritura de P2. Cada registro admite su explicación aislada.

Al combinar los órdenes locales, P1 exige `Wx < Ry` y P2 exige `Wy < Rx`. Obtener 0 exige `Ry < Wy` y `Rx < Wx`. Aparece el ciclo `Wx < Ry < Wy < Rx < Wx`, imposible en un orden total. Por eso validar cada objeto por separado no basta para esta garantía.

## Memoria y fences

El capítulo vincula el modelo con multiprocesadores y explica que el hardware puede reordenar accesos. Una **barrera de memoria** o *fence* establece restricciones de orden necesarias para publicar datos entre hilos. Su alcance depende de la arquitectura y del modelo del lenguaje; no convierte automáticamente todas las instrucciones de un programa en una historia secuencial global.

La analogía ayuda a comprender orden y visibilidad, pero un algoritmo para memoria compartida no se traslada directamente a nodos que intercambian mensajes y pueden quedar incomunicados. Cambian las condiciones de comunicación, latencia y fallas.

> [!question]- ¿Secuencial significa que todos leen el mismo valor al mismo tiempo?
> No. Pueden estar en puntos distintos de una historia común. La obligación es que exista un orden total compatible con todas sus observaciones y su orden de programa.

**Referencia:** PDF 31–33 · impresas 227–229 · figura 11-5. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=31|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/07 RIFL reintentos y efectos únicos|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/09 Consistencia causal y dependencias|Siguiente]] →
