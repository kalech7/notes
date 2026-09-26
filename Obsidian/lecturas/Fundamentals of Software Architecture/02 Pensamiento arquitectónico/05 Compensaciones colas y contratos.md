---
title: "Capítulo 2 · Pensamiento arquitectónico · Compensaciones colas y contratos"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 2
orden: 5
---

# Compensaciones colas y contratos

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 2 · Pensamiento arquitectónico](00%20%C3%8Dndice.md) → Nota 5 de 8

**Objetivo:** Comparar alternativas de mensajería y sus costos.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 5. Analizar compensaciones: el caso de las subastas

El ejemplo del libro contiene un productor de pujas y tres servicios: captura, seguimiento y analítica. Todos necesitan información de la puja. Se comparan una publicación a un *topic* y publicaciones dirigidas a colas separadas. **Fuente: PDF pp. 26–29; impresas pp. 30–33.**

En la topología dibujada con colas, el productor conoce tres destinos. Añadir un servicio de historial obliga a añadir otro destino y modificar esa coordinación. Con publicación/suscripción, el productor publica para suscriptores y el nuevo servicio puede incorporarse sin cambiar su lógica. Esa ventaja procede del **desacoplamiento respecto a los receptores**, no de una propiedad mágica del nombre «topic».

El libro después examina acceso a datos, contratos y supervisión. Su intención pedagógica es valiosa: buscar costos después de identificar beneficios. Sin embargo, algunas afirmaciones son demasiado generales. La propia página PDF 29 introduce una excepción basada en separar *exchange* y cola.

> [!warning] Matiz técnico respaldado por documentación externa
> Un topic no es intrínsecamente inseguro ni impide supervisión o autoescalado. RabbitMQ combina un exchange de publicación/suscripción con una cola por suscriptor lógico; las réplicas sobre una misma cola reparten trabajo, no reciben cada una todas las copias. Hay controles de acceso y métricas de colas; el autoescalado requiere una política y un mecanismo adicionales. Referencias: [publicación/suscripción](https://www.rabbitmq.com/tutorials/tutorial-three-python), [control de acceso](https://www.rabbitmq.com/docs/access-control), [monitorización](https://www.rabbitmq.com/docs/monitoring).

### Aplicación propia: un pedido, varios intereses

En PedidoClaro, cocina, notificaciones y analítica representan tres intereses diferentes. **Supuesto:** cada pedido confirmado debe producir una tarea para cada interés. El siguiente esquema adapta la separación entre distribución y procesamiento; no reproduce la figura del libro.

![Aplicación propia: un pedido, varios intereses ](../Recursos%20visuales/Diagramas/cap02-diagrama-03.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap02-diagrama-03.mmd)

**Interpretación:** hay una ruta independiente por interés; los trabajadores de cocina comparten su carga. **Límite:** el dibujo no especifica persistencia, confirmaciones, reintentos ni orden. Un evento puede volver a entregarse si se reintenta; procesarlo no debe equivaler a cobrar o preparar dos veces por accidente.

**Cálculo didáctico:** llegan 120 eventos por segundo a analítica y cada trabajador procesa 50. Con dos trabajadores, la capacidad nominal es 100 y se acumulan 20 eventos por segundo: 12.000 en diez minutos. Tres trabajadores ofrecerían 150 y, manteniendo la entrada, vaciarían esa acumulación a 30 por segundo, aproximadamente en 400 segundos.

El cálculo supone trabajo uniforme, capacidad sumable y ausencia de otro cuello de botella. Una base saturada puede impedir que el tercer trabajador aporte capacidad. Además de profundidad de cola, interesa cuánto tiempo lleva esperando el evento más antiguo: una acumulación estable también puede incumplir el servicio esperado.

### Contratos: compartir información no elimina la evolución

Un contrato define campos, tipos y significado. El ejemplo del libro observa que modificar un mensaje común puede afectar a varios consumidores. **Afectar exige evaluar compatibilidad; no equivale a romperlos automáticamente.** Esta precisión es elaboración técnica propia sobre el ejemplo.

Si añadimos `canalOrigen` como campo opcional y los consumidores toleran campos desconocidos, el cambio puede ser compatible. Si renombramos `total` o cambiamos su significado de centavos a unidades, podemos romperlos aunque el mensaje siga siendo sintácticamente válido. Una cola dedicada tampoco vuelve seguro cualquier cambio: su receptor sigue teniendo expectativas.

La pregunta arquitectónica es qué consumidores necesitan qué información, quién puede acceder, cómo evolucionan los contratos y cómo se recuperan fallos. Agregar un suscriptor puede evitar cambios en el productor y aun así exigir permisos, configuración, capacidad y pruebas. El desacoplamiento reduce determinadas dependencias; no elimina todo trabajo de integración.

---

**Anterior:** [Radar tecnológico personal](04%20Radar%20tecnol%C3%B3gico%20personal.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Negocio y agilidad](06%20Negocio%20y%20agilidad.md)
