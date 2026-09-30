---
title: "12 · Caso de telemetría: Kafka a MongoDB"
created: 2026-09-29
capitulo: 12
tags:
  - lecturas/software-architecture
  - arquitectura/pipeline
---

# Caso de telemetría: Kafka a MongoDB

[[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/00 Índice|← Índice del capítulo 12]]

**El caso final separa recibir información, decidir de qué tipo es, calcular una métrica y guardarla.** No obliga a que cada dato atraviese todos los cálculos: los testers lo encaminan a la ruta relevante.

## 1. Qué datos entran

**Telemetría** es información emitida por un sistema sobre su funcionamiento. El libro plantea servicios que envían información a Kafka. El productor `Service Info Capture` se suscribe a un tema y obtiene datos para el pipeline. Un **tema** organiza una corriente de mensajes por nombre. Aquí Kafka es el origen externo; la captura es el productor **del pipeline** aunque sea un lector desde el punto de vista de Kafka.

La captura solo se ocupa de conectar y recibir. No calcula duración ni uptime. Esa restricción evita que un cambio en la forma de recibir información obligue a tocar los cálculos.

## 2. El recorrido de la figura 12-4

![Clasificación y cálculo de telemetría](../Recursos%20visuales/Cap%C3%ADtulo%2012/c12-03-telemetria.png)

La captura entrega al tester de duración. Si el dato describe la duración de una petición, baja al calculador correspondiente. Si no, continúa al tester de uptime. Este envía los datos adecuados a su calculador; los que no interesan a ninguna ruta terminan sin guardarse en este flujo. Los dos transformadores convergen en un consumidor que persiste en MongoDB. El verde identifica ese destino común; las cajas azules separan decisiones de cálculos.

La figura usa flechas punteadas para indicar algunas rutas de continuación y rechazo. La recreación escribe «sí» y «no» para hacer explícitas las condiciones que explica el texto. No supone que un dato de duración se entregue también al calculador de uptime.

| Componente del libro | Rol | Responsabilidad delimitada |
|---|---|---|
| Service Info Capture | Productor | Leer información del tema |
| Duration | Tester | Determinar si el dato pertenece a duración |
| Duration Calculator | Transformador | Calcular la métrica de duración |
| Uptime | Tester | Determinar si el dato pertenece a uptime |
| Uptime Calculator | Transformador | Calcular la métrica de uptime |
| Database Output | Consumidor | Persistir el resultado en MongoDB |

El párrafo final describe explícitamente la persistencia desde el calculador de uptime; la figura también conecta el calculador de duración al consumidor. La explicación de ambas rutas se apoya en la figura y en la separación de responsabilidades.

## 3. Seguir tres registros concretos

Estos registros y números son propios; el libro no prescribe su formato ni las fórmulas exactas.

- `tipo=duracion`, inicio `1000 ms`, fin `1180 ms`: el tester de duración lo acepta; el transformador obtiene `1180 − 1000 = 180 ms`; el consumidor guarda ese resultado.
- `tipo=uptime`, ventana `3600 s`, tiempo activo `3540 s`: el primer tester lo pasa hacia delante; el segundo lo acepta; el transformador calcula `3540 / 3600 × 100 ≈ 98,33 %`; el consumidor guarda el resultado.
- `tipo=temperatura`: no corresponde a duración ni uptime; termina sin persistencia en este pipeline. Ese fin es una decisión de clasificación, no un fallo del sistema.

**Uptime** suele referirse al tiempo que el servicio permanece activo. Convertirlo en porcentaje requiere un período observado y una definición de «activo». No debe confundirse automáticamente con éxito de peticiones o disponibilidad percibida por el usuario. El ejemplo porcentual es una ampliación didáctica, no un valor que figure en el escaneo.

## 4. Añadir una métrica sin romper el resto

El libro propone añadir después del tester de uptime otro tester para una métrica nueva, como espera por una conexión a la base de datos. Ese tester conduce a un calculador nuevo y luego a la salida.

La captura puede mantenerse igual si el mensaje ya contiene la información necesaria. Si no la contiene, hay que ampliar el contrato de origen; «extensible» no significa que puedan aparecer datos que nadie produce. El consumidor también necesita aceptar el nuevo tipo de resultado. Así, se evita reescribir toda la cadena, pero sí se revisan las fronteras afectadas.

## 5. Lo que el ejemplo no define

La figura no especifica esquemas, política de duplicados, confirmación de recepción, persistencia de avance ni recuperación de escrituras inciertas. Tampoco prueba que todos los filtros sean despliegues independientes. Kafka y MongoDB aparecen como tecnologías de los extremos; eso no basta para convertir toda la cadena en microservicios.

Para implementar el caso habría que decidir qué ocurre si el consumidor falla después de guardar y antes de confirmar. La nota de recuperación explica el mecanismo general sin atribuir al dibujo garantías de entrega que no declara.

> [!question]- ¿Por qué no conviene que el tester de duración calcule también la métrica?
> Porque identificar el tipo y calcularlo tienen motivos de cambio distintos. Mantenerlos separados permite cambiar el cálculo sin alterar la selección de ruta, que es la ventaja señalada por el libro.

> [!question]- ¿Un dato no reconocido debe considerarse siempre perdido?
> No. En el ejemplo deja de interesar a este flujo. Un sistema real puede contar descartes, registrar tipos desconocidos o encaminarlos a otra ruta; esa política debe acordarse según necesidades.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/09 Arquitectura pipeline.pdf#page=11|PDF 11–12 · impresas 191–192 · figura 12-4]]

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/07 Equipos características y elección|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/09 Laboratorio y repaso|Siguiente →]]
