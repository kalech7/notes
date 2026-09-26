---
title: "Capítulo 3 · Modularidad · Preguntas y ejercicio resuelto"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 3
orden: 7
---

# Preguntas y ejercicio resuelto

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 3 · Modularidad](00%20%C3%8Dndice.md) → Nota 7 de 7

**Objetivo:** Proponer límites para la cancelación de pedidos.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Evalúa límites con varias lentes: cohesión dentro del módulo, dependencias entre módulos, métricas calculadas con una unidad fija y acuerdos concretos que obligan a coordinar cambios. Ninguna cifra aislada certifica modularidad.

## 7. Preguntas de comprobación

### 1. ¿Extraer Precios como servicio mejora necesariamente la modularidad?

> [!success]- Solución
> No. Hay que evaluar sus fronteras y acuerdos. La extracción física puede conservar dependencias internas mal definidas y añadir coordinación remota. Primero conviene identificar responsabilidad, contrato y motivo del despliegue independiente.

### 2. ¿Qué distingue cohesión secuencial de procedimental?

> [!success]- Solución
> En la secuencial, la salida de una operación alimenta a otra. En la procedimental, la relación exige un orden, sin requerir ese flujo de datos. «Ocurre después» no demuestra cohesión secuencial.

### 3. Cuatro métodos forman dos parejas que comparten campos. ¿Cuánto da LCOM1?

> [!success]- Solución
> Hay seis pares: cuatro disjuntos y dos compartidos. LCOM1 = max(4 − 2, 0) = 2. No se cuentan cuatro métodos como cuatro pares.

### 4. ¿LCOM1 = 0 demuestra una sola componente conexa?

> [!success]- Solución
> No. Tres métodos conectados por un campo y un cuarto aislado producen tres pares compartidos y tres disjuntos: LCOM1 = 0. Sin llamadas adicionales, LCOM4 sigue identificando dos componentes.

### 5. Con tres tipos abstractos, siete concretos, Ca = 6 y Ce = 2, ¿cuáles son A, I y D?

> [!success]- Solución
> A = 3/10 = 0,3; I = 2/8 = 0,25; D = |0,3 + 0,25 − 1| = 0,45. La distancia perpendicular es aproximadamente 0,318. Las líneas de código no intervienen.

### 6. Un módulo sin dependencias, ¿tiene I = 0?

> [!success]- Solución
> La fórmula da 0/0: está indefinida. Asignarle cero sería una convención de herramienta, no una consecuencia matemática ni una prueba de estabilidad.

### 7. ¿Una constante compartida elimina la connascencia de significado?

> [!success]- Solución
> Hace explícita parte del acuerdo mediante un nombre y facilita cambios coordinados. Los consumidores todavía deben interpretar ese estado correctamente; si lo persisten o intercambian externamente, también deben respetar su contrato y evolución.

## 8. Ejercicio aplicado: cancelar en PedidoClaro

**Supuestos propios:** `Clientes` contiene datos personales, consulta pedidos y ejecuta cancelaciones. Cada cancelación modifica el estado, libera existencias y recalcula importes. Web y Kiosco dependen de Clientes; Clientes depende de Inventario, Pagos y Correo. Tiene una interfaz y cuatro clases concretas.

Calcula $A$, $I$ y $D$. Propón una frontera para cancelaciones, identifica dos connascencias y explica cómo verificarías una mejora sin limitarte a bajar métricas.

> [!success]- Una solución razonada
> A = 1/5 = 0,2; Ca = 2; Ce = 3; I = 3/5 = 0,6; D = 0,2. Estos números no deciden la extracción.
>
> Una opción es trasladar el ciclo de vida y la cancelación a Pedidos, con una operación `cancelar(idPedido)` que aplique reglas según el estado. Clientes conserva datos personales. Antes de hacerlo, se comprueba qué datos de cliente necesita realmente la decisión.
>
> Hay connascencia de valores entre estado, existencias e importe; también de ejecución si el proceso exige validar la cancelación antes de ordenar un reembolso. Si intervienen servicios distintos, se deben especificar estados intermedios, reintentos y compensaciones según el negocio, sin suponer atomicidad global.
>
> La mejora se verifica con escenarios de cancelación repetida, fallo del proveedor de pagos y cambios en las reglas de devolución. Interesa que el cambio quede localizado, que los contratos sean comprensibles y que las invariantes se mantengan. Las métricas posteriores se recalculan sobre el grafo nuevo; no se promete que todas disminuyan.

---

**Anterior:** [Connascencia y refactorización](06%20Connascencia%20y%20refactorizaci%C3%B3n.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Comportamiento y capacidades](../04%20Caracter%C3%ADsticas%20arquitect%C3%B3nicas/01%20Comportamiento%20y%20capacidades.md)
