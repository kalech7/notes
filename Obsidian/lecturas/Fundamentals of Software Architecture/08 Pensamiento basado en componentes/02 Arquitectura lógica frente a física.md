---
title: "08 · Arquitectura lógica y física: dos vistas del mismo sistema"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/componentes
capitulo: 8
---

# Arquitectura lógica y física: dos vistas del mismo sistema

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 16–17 · impresas 110–111 · figuras 8-4 y 8-5** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Síntesis explicada del capítulo 8; los ejemplos, preguntas, tablas y diagramas adicionales se señalan como elaboración didáctica. Las recreaciones de figuras conservan la idea y las relaciones pertinentes, con rótulos en español; no son facsímiles.

## La pregunta de cada vista

La arquitectura lógica describe **las funciones principales y su colaboración**. Puede mostrar actores y repositorios abstractos cuando ayudan a entender dónde se utiliza o transfiere información. La arquitectura física muestra **las unidades de ejecución y otros artefactos concretos**: interfaces, servicios, bases de datos y mensajería.

Separarlas permite decidir primero los límites de responsabilidad sin confundirlos con decisiones de despliegue. No son dos sistemas diferentes: son dos explicaciones complementarias del mismo sistema.

![c08-02-logica-fisica](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-02-logica-fisica.png)

## El diagrama lógico

Las cajas A–E corresponden a componentes, como en la figura 8-4. El actor utiliza A y C; A colabora con B; C colabora con D y con un repositorio; D colabora con E y con otro repositorio. Los repositorios son **abstracciones de información**: no afirman que existan tres motores de base de datos, tres servidores ni tres esquemas independientes.

Cada entrada del actor puede seguirse hasta otro componente preguntando qué información requiere esa colaboración. A → B indica una relación funcional. B → Repositorio 2 indica que B utiliza esa información. D también utiliza Repositorio 2; esto permite discutir información compartida antes de elegir una implementación.

Con este diagrama podemos conversar sobre responsabilidades y dependencias, pero no sabemos si las flechas son llamadas locales, HTTP o eventos; tampoco si las operaciones ocurren dentro de una transacción. Las flechas del ejemplo no documentan por sí mismas tiempos ni fallos.

![c08-03-fisica](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-03-fisica.png)

## El diagrama físico

Aquí las cajas son servicios o elementos de ejecución y los cilindros representan bases de datos. La interfaz se comunica con B y C. B llama a A. A, B y C usan un mismo almacén; C además se comunica con D mediante un elemento de mensajería. D utiliza su propio almacén. Se conserva la topología general de la figura 8-5, con rótulos aclaratorios añadidos.

Una solicitud entra por la interfaz, llega a un servicio, puede involucrar otros servicios y persistencia. En la rama derecha aparece una mediación de mensajería. La imagen muestra un posible reparto físico, pero no asigna todos los componentes A–E del diagrama lógico a esos servicios. Las letras de ambas imágenes no establecen una correspondencia automática.

Ahora es posible discutir unidades operativas y almacenamiento, aunque faltan decisiones como protocolos, reintentos, redundancia, particiones y políticas de seguridad; el dibujo no garantiza disponibilidad o desacoplamiento.

## Un mismo conjunto de componentes, distintos despliegues

Elaboración didáctica: un sistema tiene Registrar pedido, Cobrar y Notificar.

| Alternativa física | Organización lógica que puede conservar | Consecuencias que habría que evaluar |
|---|---|---|
| Un ejecutable modular | Tres componentes internos separados | Llamadas locales sencillas; despliegue conjunto |
| Dos servicios | Registrar y Cobrar juntos; Notificar aparte | Separación operativa de correo; aparece comunicación remota |
| Tres servicios | Un servicio por componente | Más autonomía potencial; más contratos y fallos de red |

La tabla no recomienda una alternativa universal. Muestra por qué dibujar primero tres cajas lógicas **no obliga** a crear tres servicios. La distribución física debe responder a las características arquitectónicas y restricciones del caso.

## Por qué empezar directamente con infraestructura puede fallar

Si el primer dibujo solo contiene «API», «worker» y «database», quizá sepamos dónde corre el código, pero no qué parte decide descuentos o quién es responsable de aplicar un pago. Una funcionalidad puede quedar dispersa entre servicios. Los desarrolladores reciben un plano operativo con poca orientación para organizar el código.

El libro recomienda construir una arquitectura lógica para evitar esa pérdida de estructura. Como matiz práctico, ambas vistas pueden evolucionar mediante retroalimentación: una restricción operativa descubierta tarde puede exigir revisar los límites lógicos.

**Ejercicio resuelto.** Un componente Notificar está en un monolito. ¿Hay contradicción? Ninguna. Componente expresa organización del código y responsabilidad; monolito expresa una unidad de despliegue. Si mañana Notificar se extrae a un servicio, su propósito puede mantenerse aunque cambien comunicación, pruebas y operación.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/01 Componentes lógicos y organización del código|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/03 Ciclo de identificación y refinamiento|Siguiente →]]
