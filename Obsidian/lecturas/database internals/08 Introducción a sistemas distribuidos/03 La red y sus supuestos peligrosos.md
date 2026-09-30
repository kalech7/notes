---
title: "Database Internals — La red y sus supuestos peligrosos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 8
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# La red y sus supuestos peligrosos

[[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice del capítulo 8]]

Una conexión abierta demuestra que se pudo establecer comunicación en cierto instante. Lo que necesitamos saber para una operación es más exigente: si el mensaje llegó, si la respuesta volvió y qué ocurrió durante la espera.

## La llamada que termina sin respuesta

Un cliente envía «guardar pedido 42». Puede ocurrir que la solicitud se pierda, que espere en una cola, que el servidor la procese y pierda la respuesta o que el servidor se caiga en un punto intermedio. Desde el cliente, varias historias diferentes producen el mismo síntoma: silencio. Un **timeout** es el vencimiento de un plazo local; permite decidir dejar de esperar o reintentar, pero no demuestra que el servidor esté muerto ni que la operación haya fallado.

El capítulo revisa las conocidas falacias de la computación distribuida atribuidas a Peter Deutsch. La función de la lista es revelar supuestos que parecen inocentes cuando todo funciona.

| Supuesto peligroso | Por qué puede fallar | Consecuencia práctica |
|---|---|---|
| La red es fiable | Pérdida, desconexión, rutas defectuosas | Modelar respuestas ausentes y operaciones inciertas |
| La latencia es cero | Transporte y software necesitan tiempo | No sustituir indiscriminadamente llamadas locales por remotas |
| El ancho de banda es infinito | Varios emisores compiten por enlaces finitos | Presupuestar bytes, límites y tráfico de recuperación |
| La red es segura | Existen accesos indebidos y mensajes adversarios | Autenticar y autorizar según el entorno |
| La topología no cambia | Se reemplazan nodos y rutas | Mantener información de ubicación y membresía |
| Hay una única autoridad administradora | Componentes dependen de equipos distintos | Evitar suponer control total sobre configuraciones |
| El transporte no tiene costo | Consume CPU, memoria y tiempo | Incluir serialización y retransmisiones en el costo |
| Todos los componentes son homogéneos | Versiones y recursos pueden diferir | Especificar compatibilidad de mensajes y capacidades |

La impresa 175 desarrolla varios de esos puntos sin imprimir una lista numerada de ocho. La tabla organiza las falacias como vocabulario de estudio; no inventa una enumeración adicional de páginas del libro.

## Latencia y ancho de banda son dimensiones diferentes

**Latencia** es cuánto tarda una operación o un mensaje. **Ancho de banda** es la cantidad de datos que puede atravesar un enlace por unidad de tiempo. Un enlace puede transportar mucho por segundo y aun así tardar bastante en iniciar o completar una ida y vuelta. Para una solicitud sencilla, un modelo didáctico de duración es:

`tiempo total = ida + espera en cola + procesamiento + vuelta`.

Con 8 ms de ida, 25 ms de cola, 4 ms de trabajo y 8 ms de vuelta obtenemos `8 + 25 + 4 + 8 = 45 ms`. Mejorar el enlace a 4 ms en cada dirección lo reduce a 37 ms; la cola sigue dominando. Las cifras son propias y excluyen otros costos posibles.

El libro usa la reducción de milisegundos en mercados financieros para mostrar el interés económico de la latencia y cita una discusión sobre sus efectos. Esa mención contextual no convierte la latencia en una ventaja universal ni se utiliza aquí como consejo financiero.

## Reintentar añade otra decisión

Si no sabemos si se ejecutó «guardar pedido», repetirlo puede ayudar a completar la tarea o duplicarla. Una buena interfaz necesita decir qué significa confirmar, cómo identificar una misma operación y qué errores permiten reintento. La nota 08 resolverá ese caso con deduplicación y un efecto durable. Antes veremos por qué el servidor puede tardar aunque la red funcione.

**Referencia:** PDF 7–8 · impresas 174–175. [[Obsidian/lecturas/database internals/Materiales/08 Sistemas distribuidos.pdf#page=7|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/02 Concurrencia interleavings y estado compartido|Anterior]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/04 Colas procesamiento y backpressure|Siguiente]] →
