---
title: "Capítulo 3 · Modularidad · Acoplamiento y dependencias"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 3
orden: 4
---

# Acoplamiento y dependencias

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 3 · Modularidad](00%20%C3%8Dndice.md) → Nota 4 de 7

**Objetivo:** Leer dependencias entrantes y salientes.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Cohesión mira hacia dentro de una frontera; acoplamiento mira las relaciones que la atraviesan. Un módulo puede ser internamente coherente y aun así obligar a muchos otros a cambiar con él.

## 4. Acoplamiento: quién depende de quién

El acoplamiento aferente $C_a$ cuenta dependencias **entrantes**: otros elementos dependen del elemento analizado. El eferente $C_e$ cuenta dependencias **salientes**: el elemento analizado depende de otros.

![4. Acoplamiento: quién depende de quién ](../Recursos%20visuales/Diagramas/cap03-diagrama-03.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap03-diagrama-03.mmd)

Para Pedidos, en este grafo $C_a=3$ y $C_e=2$: la flecha va del dependiente hacia aquello que utiliza. Se cuentan dependencias entre módulos distintos, no llamadas, tráfico, latencia ni pasos de una traza temporal.

Hay que fijar la unidad: tipos, paquetes o componentes. También qué relación cuenta: importación, referencia de tipo o uso efectivo. En este ejemplo contamos módulos distintos y excluimos dependencias internas. Mezclar conteos de clases con conteos de paquetes produciría ratios engañosos.

Un $C_a$ elevado señala un alcance potencial de propagación de cambios: modificar un contrato puede afectar muchos consumidores. Un $C_e$ elevado señala muchos proveedores cuyos cambios podrían afectar al módulo. Ninguno demuestra por sí solo mala arquitectura; un contrato central estable puede tener numerosos consumidores deliberadamente.

### Del conteo al mecanismo de cambio

Los números solo indican **dirección y cantidad de relaciones**. Para decidir si una dependencia duele, hay que seguir el cambio que podría propagarse:

| Cambio en Pedidos | Quién podría verse afectado | Pregunta que descubre el riesgo |
|---|---|---|
| Renombrar un campo del contrato | Clientes que lo consumen | ¿El cambio es compatible o exige desplegar consumidores a la vez? |
| Alterar el significado de `confirmado` | Cocina, cobros y atención | ¿Todos interpretan el estado de la misma manera? |
| Cambiar el orden de dos llamadas | Proveedor o coordinador | ¿Existe una dependencia temporal que el grafo estático no muestra? |
| Cambiar el esquema de datos compartido | Todos los escritores y lectores | ¿Hay propiedad clara de los datos o coordinación oculta? |

Dos módulos pueden tener una sola flecha y, aun así, estar fuertemente acoplados si comparten una tabla, necesitan desplegarse juntos o dependen de una secuencia frágil. También pueden existir muchas flechas hacia un contrato pequeño, estable y versionado sin que cada cambio se propague.

> [!example] Ejemplo razonado
> Promociones consulta el contrato público de Pedidos para saber el total. Si Pedidos añade un campo opcional, los consumidores antiguos pueden seguir funcionando: la dependencia existe, pero el cambio no obliga a coordinarlos. Si Pedidos redefine `total` para excluir impuestos sin cambiar nombre ni versión, el compilador no detecta nada y el error aparece en el significado. El segundo caso tiene el mismo $C_a$ y $C_e$, pero mayor riesgo de propagación.

### Ciclos: cuando nadie puede cambiar primero

Si Pedidos depende de Pagos y Pagos depende de Pedidos, aparece un ciclo. El problema práctico no es la figura circular, sino que una modificación puede exigir comprender, probar o publicar ambas partes juntas. Antes de «romper el ciclo» añadiendo una interfaz, pregunta quién debería poseer la decisión. A veces conviene invertir una dependencia; otras, extraer un contrato o evento; y en otras el límite elegido es incorrecto. Una interfaz añadida sin aclarar responsabilidades puede mejorar el dibujo sin reducir coordinación.

> [!warning] Errores frecuentes
> - Interpretar $C_a$ alto como «malo» y $C_e$ bajo como «bueno» sin estudiar estabilidad ni significado.
> - Contar llamadas en producción como si fueran dependencias distintas: frecuencia y acoplamiento responden preguntas diferentes.
> - Comparar métricas calculadas con unidades distintas, por ejemplo clases en un sistema y módulos en otro.
> - Ignorar dependencias dinámicas: orden, tiempo, valores compartidos o identidad. Se desarrollan en [Connascencia y refactorización](06%20Connascencia%20y%20refactorizaci%C3%B3n.md).

> [!question]- Comprobación: un módulo tiene $C_a=8$ y $C_e=1$. ¿Es mejor que otro con $C_a=2$ y $C_e=3$?
> No puede decidirse con esos datos. Falta conocer la unidad contada, estabilidad y tamaño de los contratos, ciclos, frecuencia de cambio, compatibilidad y coordinación necesaria. Las métricas orientan dónde investigar; no puntúan la calidad de forma universal.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=8|PDF pp. 8–9; impresas pp. 44–45]].

---

**Anterior:** [LCOM y sus variantes](03%20LCOM%20y%20sus%20variantes.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Abstracción inestabilidad y distancia](05%20Abstracci%C3%B3n%20inestabilidad%20y%20distancia.md)
