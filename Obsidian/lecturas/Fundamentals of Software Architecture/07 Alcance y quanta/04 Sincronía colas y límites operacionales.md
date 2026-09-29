---
title: "Capítulo 7 · Sincronía colas y límites operacionales"
created: 2026-09-28
capitulo: 7
orden: 4
tags:
  - lecturas/software-architecture
  - arquitectura/quanta
---

# Sincronía colas y límites operacionales

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Capítulo 7 · Alcance y quanta]] · Nota 4 de 7

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, segunda edición, capítulo 7. Fuente local: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Las páginas PDF se cuentan desde el archivo suministrado; la impresa aparece en el libro. «Elaboración» y «ampliación didáctica» identifican material propio.

**Objetivo:** explicar dónde se acumula el trabajo, cómo se propagan los límites de capacidad y por qué una cola amortigua picos pero no crea capacidad infinita.

## El ejemplo del capítulo

**Libro — PDF pp. 5–6, impresas 99–100.** Al finalizar una subasta, el servicio Subastas envía la información de pago a Pagos de forma síncrona. Supongamos, como el texto, que Pagos solo puede atender un pago cada **500 ms**. Cuando terminan muchas subastas al mismo tiempo, la diferencia de capacidades puede provocar fallos: el receptor no acompaña el ritmo del emisor.

La frase «Subastas escala» describe solo una parte de la operación. Si el usuario necesita completar el cobro, el resultado depende también de Pagos. Aumentar las instancias del emisor podría incluso incrementar la presión sobre el receptor.

![02 sincronia cola](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-02-sincronia-cola.png)

## Cómo interpretar el gráfico

- **Cajas Subastas y Pagos:** participantes que ejecutan capacidades distintas. No representan necesariamente una única instancia física.
- **Parte A:** la primera flecha lleva la solicitud; la flecha de vuelta representa la respuesta. El solicitante debe esperar o gestionar un timeout/error. El diagrama no dibuja hilos: «esperar» es una dependencia lógica del resultado, independientemente de cómo se implemente la E/S.
- **Parte B:** Subastas publica trabajo en la cola. Los cuadrados representan mensajes pendientes. Pagos los consume a su ritmo. La aceptación del mensaje y la finalización del pago son momentos diferentes.
- **Cifra de 2 pagos/s:** es una derivación didáctica de 500 ms por pago bajo un supuesto explícito: un único consumidor secuencial, sin paralelismo ni sobrecostes adicionales.

**Conclusión:** la cola desplaza parte de la espera a un almacén de trabajo pendiente y permite absorber ráfagas. **Límite:** el gráfico no demuestra entrega exactamente una vez, persistencia ante fallos ni ausencia de duplicados. Esas propiedades requieren diseño y verificación propios.

## Números para entender una ráfaga

**Ampliación didáctica; las siguientes cifras, salvo los 500 ms, no vienen del libro.** Si llegan 20 pagos simultáneamente y el procesador completa 2 por segundo, terminar el lote requiere aproximadamente 10 segundos, ignorando costes de red, confirmación y preparación. El primer pago puede terminar alrededor de 0,5 s y el último alrededor de 10 s.

Una cola permite registrar la solicitud y responder «pendiente» antes de que el pago termine, si ese comportamiento es aceptable para el negocio. No permite afirmar «pagado» antes de recibir la confirmación correspondiente.

Si llegan continuamente 3 pagos por segundo y se completan 2, el pendiente aumenta aproximadamente 1 pago por segundo. Tras un minuto habría unos 60 adicionales, bajo esos supuestos. La cola no resuelve ese desequilibrio sostenido: se necesitaría aumentar la capacidad efectiva, reducir la llegada o aplicar control de admisión.

Una aproximación útil es:

$$\text{crecimiento del pendiente por segundo}\approx \lambda-\mu$$

Aquí $\lambda$ es la tasa de llegada y $\mu$ la tasa de finalización. Si $\lambda>\mu$ de forma sostenida, la acumulación crece. Esta es una explicación propia y simplificada; no sustituye un modelo completo de colas ni contempla variabilidad, límites de almacenamiento o reintentos.

## Qué cambia con la asincronía

| Aspecto | Interacción síncrona | Interacción mediante cola |
|---|---|---|
| Resultado al solicitante | Puede esperar el resultado final. | Puede confirmar recepción antes de terminar el trabajo. |
| Diferencias temporales de capacidad | Se sienten directamente en espera y errores. | Se amortiguan temporalmente como mensajes pendientes. |
| Experiencia de usuario | Resultado inmediato cuando el servicio responde. | Puede requerir estado pendiente y consulta posterior. |
| Dependencia del dominio | Sigue existiendo. | También sigue existiendo. |
| Sobrecarga sostenida | Saturación o rechazo. | Crecimiento del pendiente y eventual saturación. |

**Ampliación práctica:** una implementación real debe definir cómo manejar duplicados, reintentos y mensajes fallidos, y cómo observar el retraso. La **idempotencia** permite repetir la misma operación sin añadir un efecto de negocio distinto: reenviar el mismo intento de cobro no debería cobrar otra vez. Son asuntos necesarios para llevar la idea a producción, pero el fragmento del capítulo no desarrolla sus mecanismos.

## ¿La sincronía fusiona quanta?

**Libro — PDF p. 9, impresa 103:** la comunicación síncrona puede modificar los límites definidos por el acoplamiento estático en algunos sistemas. Es una advertencia de interacción entre ambos tipos de acoplamiento, no una equivalencia universal.

La edición estudiada permite hablar de comunicación síncrona entre quanta. Por eso conviene mantener dos preguntas: «¿qué unidad se despliega y funciona con sus dependencias?» y «¿de qué participantes depende este resultado de extremo a extremo?». Un recorrido puede compartir límites de capacidad, disponibilidad o latencia aunque existan unidades de despliegue distintas.

**Comprobación:** si Subastas puede desplegarse sin desplegar Pagos, pero no confirmar una venta cuando Pagos falla, existe independencia en un aspecto y dependencia en otro. Describe ambos; no escondas esa diferencia bajo una etiqueta.


---

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/03 Cuatro formas de acoplamiento|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/05 Del alcance al estilo arquitectónico|Siguiente →]]
