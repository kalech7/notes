---
title: "Capítulo 3 · Modularidad · Cohesión y responsabilidades"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 3
orden: 2
---

# Cohesión y responsabilidades

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 3 · Modularidad](00%20%C3%8Dndice.md) → Nota 2 de 7

**Objetivo:** Explicar qué debería permanecer junto.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Un módulo es una frontera lógica y su granularidad indica cuánto abarca. Tener varios módulos no demuestra que la división sea útil; hace falta explicar por qué cada conjunto cambia por razones relacionadas.

## 2. Cohesión: razones para permanecer juntos

La cohesión responde esa pregunta interna: qué mantiene unidas las partes de un módulo. Sin ella, separar archivos o paquetes solo redistribuye una misma confusión.

![Responsabilidades mezcladas frente a módulos cohesivos de pedidos, pagos y entregas](../Recursos%20visuales/09-cohesion-responsabilidades.png)

A la izquierda, cada contenedor mezcla pedidos, pagos y entregas, de modo que un cambio puede atravesar varias fronteras. A la derecha, cada responsabilidad tiene un lugar reconocible y se comunica mediante interfaces. Los puentes muestran que sigue habiendo acoplamiento. La frase «baja dependencia» expresa el objetivo de este ejemplo, no una garantía: hacen falta contratos y límites efectivos para conseguirlo. Los contenedores son módulos lógicos; no obligan a desplegar tres servicios.

La cohesión expresa cuánto sentido tiene que las partes pertenezcan al mismo módulo. Una intuición útil es preguntar si colaboran para una responsabilidad reconocible y cambian por razones relacionadas. Separar piezas muy cohesionadas puede obligarlas a compartir tantos detalles que el acoplamiento externo empeore.

### Las siete formas de cohesión

El libro las presenta desde funcional hasta accidental. Es una orientación cualitativa, **no una escala numérica ni un orden rígido aplicable sin contexto**. Además, aunque algunas descripciones del texto hablan de dos módulos, aquí examinamos la razón para agrupar operaciones dentro de la unidad evaluada.

1. **Funcional.** Todas las partes contribuyen a una función concreta. `CalcularTotalPedido` valida cantidades, aplica las reglas pertinentes y obtiene el total. La unidad se entiende por el resultado que produce. No significa que deba contener también envío de correos o persistencia de clientes: una finalidad excesivamente amplia, como «gestionar todo el negocio», no demuestra cohesión.

2. **Secuencial.** La salida de una operación alimenta a la siguiente. PedidoClaro transforma líneas de pedido en subtotales y después los subtotales en una base para descuentos. Existe una dependencia de datos que explica la agrupación. No basta con que las operaciones se ejecuten una después de otra: debe haber ese flujo de salida a entrada.

3. **Comunicacional.** Varias operaciones trabajan sobre los mismos datos o contribuyen a una salida común. Preparar el recibo y preparar el resumen de cocina pueden utilizar la misma instantánea confirmada del pedido. Eso ofrece una razón para agruparlas, aunque el hecho de compartir datos no garantiza que deban permanecer juntas si evolucionan con reglas distintas.

4. **Procedimental.** La agrupación se explica por un orden de pasos, sin exigir que cada salida sea la entrada siguiente. Un procedimiento de cierre puede cerrar la caja y después emitir el informe diario. La relación está en el procedimiento; las responsabilidades internas todavía pueden ser diferentes.

5. **Temporal.** Las operaciones se reúnen porque ocurren en un momento común. Al arrancar PedidoClaro se carga configuración, se preparan conexiones y se registran tareas. Coinciden en el inicio, pero sus causas de cambio son distintas. Un coordinador de arranque puede ser apropiado sin convertirse en propietario de todas esas implementaciones.

6. **Lógica.** Las operaciones pertenecen a una categoría amplia: convertir cadenas, leer formatos o validar entradas. `Conversores` puede incluir conversión de fechas, importes y direcciones. La semejanza nominal no crea una única función de negocio. Un argumento que selecciona entre muchas operaciones suele hacer visible esta agrupación, aunque no es obligatorio para clasificarla así.

7. **Accidental o coincidente.** Las partes solo comparten ubicación. Un archivo con redondeo monetario, limpieza de archivos temporales y generación de colores no tiene una responsabilidad común. Cambiarlo obliga a revisar consumidores ajenos y amplía innecesariamente el alcance de pruebas y permisos de modificación.

Una misma unidad puede mostrar varias relaciones. La clasificación ayuda a formular preguntas, no a condenar automáticamente módulos de inicialización o bibliotecas de funciones puras.

### El caso Customer/Order del libro

El libro compara un módulo de mantenimiento de clientes que añade, actualiza, consulta y notifica clientes, pero también consulta y cancela sus pedidos, con una separación entre `Customer Maintenance` y `Order Maintenance`.

La separación no se decide contando verbos. Si consultar y cancelar son las únicas operaciones de pedidos y requieren conocer profundamente al cliente, extraerlas puede producir una interfaz muy conversadora. Si los pedidos crecerán con estados, devoluciones y reservas, una responsabilidad independiente gana sentido.

**Aplicación propia:** en PedidoClaro, cancelar un pedido confirmado puede liberar inventario y solicitar un reembolso. Esa regla pertenece probablemente a Pedidos. Clientes puede solicitarla mediante el identificador del cliente y del pedido. Si Pedidos exige doce campos internos del cliente, hay que revisar el contrato: cambiar de carpeta no eliminó el conocimiento compartido. La evidencia decisiva son las invariantes, los cambios esperados y las dependencias resultantes.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=5|PDF pp. 5–7; impresas pp. 41–43]].

---

**Anterior:** [Módulos y separación física](01%20M%C3%B3dulos%20y%20separaci%C3%B3n%20f%C3%ADsica.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [LCOM y sus variantes](03%20LCOM%20y%20sus%20variantes.md)
