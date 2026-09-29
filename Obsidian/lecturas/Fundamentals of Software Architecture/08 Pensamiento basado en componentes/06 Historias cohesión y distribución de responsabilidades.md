---
title: "08 · Historias, cohesión y responsabilidades que se pueden explicar"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/componentes
capitulo: 8
---

# Historias, cohesión y responsabilidades que se pueden explicar

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 23–26 · impresas 117–120 · figuras 8-9 y 8-10** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Síntesis explicada del capítulo 8; los ejemplos, preguntas, tablas y diagramas adicionales se señalan como elaboración didáctica. Las recreaciones de figuras conservan la idea y las relaciones pertinentes, con rótulos en español; no son facsímiles.

## Llenar los componentes con comportamientos concretos

Asignar historias convierte los nombres iniciales en decisiones de implementación. Una historia debe permitir reconocer qué código cumplirá el comportamiento y qué componentes colaborarán. Una historia puede necesitar colaboración de varios componentes sin que cada uno duplique toda la implementación.

El libro muestra tres necesidades: validar el pedido, elegir el tamaño de caja y avisar por correo de los cambios de estado. Validar puede asignarse inicialmente a Registrar pedido; elegir caja corresponde a Preparar pedido. El aviso aparece en varios momentos y hace surgir Notificar al cliente.

![c08-07-notificaciones](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-07-notificaciones.png)

## Explicación paso a paso de la figura

Registrar pedido utiliza Inventario y hace avanzar el trabajo a Preparar pedido. Preparar conduce a Enviar pedido. Desde los tres momentos del proceso salen flechas hacia Notificar. Estas flechas muestran que varias funciones solicitan una responsabilidad común.

1. Al registrar el pedido hay un cambio de estado que puede comunicarse.
2. Al preparar el pedido aparece otro cambio relevante.
3. Al despacharlo aparece un tercero.
4. En lugar de copiar composición y envío de correos en los tres lugares, se identifica un componente responsable de notificaciones.

**Conclusión:** una nueva historia puede revelar una responsabilidad que el inventario inicial no contemplaba. **Límite:** centralizar notificaciones no define si habrá una cola, envío inmediato o almacenamiento de pendientes. Esas decisiones pertenecen a un análisis posterior. Los orígenes todavía necesitan expresar qué sucedió; no desaparece la colaboración.

## Cohesión: qué tan relacionadas están las operaciones

La cohesión pregunta si las operaciones de un componente forman un conjunto que tiene sentido. No equivale a «todas mencionan pedido». El ejemplo del libro muestra que Registrar pedido puede acabar validando, mostrando carrito, resolviendo dirección, recogiendo información de pago, generando identificador, cobrando, ajustando inventario y enviando correo.

Todo participa en el proceso de compra, pero el componente posee demasiadas responsabilidades. Para revisarlo conviene escribir una declaración: «Este componente es responsable de…». Una sucesión de «y además», «también» y cláusulas heterogéneas puede mostrar acumulación de tareas. Es una heurística de lectura, no un algoritmo que cuenta conjunciones.

## Refinamiento del ejemplo

| Componente tras la revisión | Responsabilidades agrupadas |
|---|---|
| Registrar pedido | Validar datos, representar carrito, resolver dirección, recoger datos de pago y generar identificador |
| Procesar pago | Aplicar el cobro |
| Gestionar inventario | Ajustar existencias de los artículos pedidos |
| Notificar al cliente | Comunicar el resumen del pedido |

Esta asignación sigue el ejemplo de pp. 119–120. No fija la única descomposición posible. En otro contexto, validar o mostrar el carrito podrían justificar límites adicionales; la decisión depende de complejidad y características requeridas.

## Separar conocimiento de colaboración

Registrar pedido puede seguir solicitando un cobro sin implementar todas las reglas del proveedor. Separar responsabilidad no significa que el flujo se desintegre. Significa definir un contrato por el que un componente pide a otro que cumpla su propósito.

Por ejemplo didáctico, `cobrar(intento, importe)` podría devolver aceptado, rechazado o pendiente. Registrar pedido necesita decidir qué hacer con esos resultados, pero no debería conocer los detalles de la tarjeta o del reintento interno. El contrato debe permitir una colaboración suficiente sin obligar al consumidor a conocer detalles innecesarios.

## Costes y límites de separar

Crear componentes añade fronteras y exige acordar información compartida. Si una división obliga a pasar decenas de detalles internos y a cambiar siempre ambos lados, quizá el límite sea artificial. Si no se divide nada, las pruebas y cambios quedan atrapados en una unidad demasiado grande. El objetivo es una granularidad útil, no el mayor número de cajas.

**Ejercicio resuelto.** La nueva historia exige enviar SMS además de correo. ¿Registrar, Preparar y Enviar deben implementar SMS? Si su responsabilidad es informar que ocurrió un cambio y Notificar decide la entrega, la evolución se concentra principalmente en Notificar. Habrá que revisar si su contrato contiene información suficiente y si el usuario puede elegir canales. El resultado depende de cómo se distribuyó el conocimiento, no solo de haber dibujado una caja común.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/05 Trampa de entidades y nombres responsables|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/07 Características arquitectónicas y granularidad|Siguiente →]]
