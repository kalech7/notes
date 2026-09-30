---
title: "Database Internals — Capítulo 11 · Linealizabilidad puntos de efecto y costo"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Linealizabilidad puntos de efecto y costo

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

Una historia es **linealizable** si se puede explicar como una ejecución secuencial válida en la que cada operación toma efecto en algún punto entre su invocación y su respuesta, preservando la precedencia real de las operaciones que no se solapan. Ese instante lógico se llama **punto de linealización**.

No tiene por qué existir un interruptor físico que cambie simultáneamente todas las réplicas. El protocolo debe asegurar que las respuestas observables encajen en ese orden. Puede mantener copias atrasadas internamente y impedir que respondan lecturas incompatibles.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 11/03 Punto de linealización.png]]

La barra azul ocupa el intervalo de la escritura y la línea naranja representa un punto legal para su efecto. En el ejemplo propio, sin otras escrituras, una lectura ubicada antes obtiene 0 y una ubicada después obtiene 1. Una lectura que se solapa puede encajar a cualquiera de los lados, pero una iniciada tras la respuesta debe respetar el cambio. El gráfico sintetiza las figuras 11-3 y 11-4.

## Qué permite el solapamiento

Si `W1: write(x,1)` y `W2: write(x,2)` se solapan, pueden ordenarse W1→W2 o W2→W1 siempre que **toda** la historia lo permita. Que W1 empiece y termine antes que W2 no basta cuando los intervalos se solapan. Lo decisivo para precedencia obligatoria es que W1 termine **antes de que W2 empiece**.

La figura 11-2 presenta dos escrituras solapadas y tres lecturas. En el orden elegido por el libro, W1→W2, la primera lectura puede ver el valor inicial, 1 o 2; una lectura tras completar W1 y mientras W2 sigue pendiente puede ver 1 o 2; una después de ambas ve 2. Estos conjuntos ilustran el orden asumido y las lecturas de una historia deben ser compatibles entre sí.

> [!warning] Precisión de la figura 11-2
> La última lectura de la figura devuelve exclusivamente 2 **porque el texto presupone W1→W2**. Ese orden no se deduce sólo de las barras solapadas. Sin esa condición adicional, el orden W2→W1 puede dejar 1 como valor final. Tampoco se eligen los conjuntos permitidos para cada lectura de manera independiente: una lectura temprana que fija un orden puede limitar las posteriores.

## Versiones recientes, no números crecientes

Una lectura posterior no puede volver a una versión más antigua de la única historia. «Más reciente» no significa un número mayor: una escritura nueva de `saldo=20` puede seguir a una vieja de `saldo=100`. La garantía se refiere al orden de las operaciones, no al valor numérico.

Una operación pendiente puede haber tomado efecto antes de perder su respuesta. En la definición habitual, una historia con invocaciones pendientes puede completarse o descartarlas de la explicación cuando sea admisible. Por tanto, la frase de la impresa 223 sobre no observar escrituras incompletas se interpreta como prohibición de **efectos parciales**, no como prueba de que toda llamada sin respuesta carece de efecto.

## CAS, ABA y publicación

**Compare-and-swap**, CAS, actualiza un registro sólo si aún contiene el valor esperado. Preparar un objeto y publicar su puntero mediante una operación atómica permite elegir un punto para el cambio observable. CAS compara el valor, no necesariamente la historia: si pasa A→B→A, un cliente que esperaba A puede acertar aunque hubo cambios intermedios. Ese es el **problema ABA**; una versión adicional permite distinguir los dos A.

La existencia de CAS no convierte cualquier secuencia de varias llamadas en una operación atómica. Leer, calcular y escribir por separado puede perder actualizaciones aunque cada llamada individual sea linealizable. Hace falta que la operación compuesta tenga su propio protocolo o primitiva.

## Costo y composición

El libro explica costos de sincronización de memoria y coordinación distribuida. En un almacén replicado, consenso puede ordenar operaciones; el camino de lectura también debe respetar autoridad y estado aplicado. Consultar sin más a una réplica atrasada no conserva la garantía porque las escrituras se hayan ordenado mediante consenso.

La linealizabilidad es **local** en su sentido técnico: si cada objeto tiene operaciones linealizables, sus historias se pueden combinar conservando esa propiedad. Esto no vuelve atómica una transferencia con débito en A y crédito en B. Los objetos siguen ofreciendo operaciones individuales; la transacción que debe agrupar ambas necesita sincronización adicional.

**Serializabilidad** exige que transacciones completas equivalgan a alguna ejecución serial. No exige por sí sola precedencia real. **Serializabilidad estricta** añade esa precedencia para transacciones. El capítulo se centra en modelos de operaciones individuales y no desarrolla un protocolo de transacciones serializables.

> [!question]- ¿Linealizabilidad impone una duración máxima a una operación?
> No. Su punto debe quedar dentro de la invocación y respuesta reales, pero el modelo no fija un máximo universal de milisegundos. El intervalo puede ser largo.

**Referencia:** PDF 27–30 · impresas 223–226 · figuras 11-2, 11-3 y 11-4. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=27|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/05 Modelos como contratos de visibilidad|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/07 RIFL reintentos y efectos únicos|Siguiente]] →
