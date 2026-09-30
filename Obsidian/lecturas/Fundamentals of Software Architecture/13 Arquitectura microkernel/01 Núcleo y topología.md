---
title: "13 · Núcleo y topología"
created: 2026-09-29
capitulo: 13
tags:
  - lecturas/software-architecture
  - arquitectura/microkernel
---

# Núcleo y topología

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/00 Índice|← Índice del capítulo 13]]

**Microkernel organiza una aplicación como un núcleo estable rodeado de extensiones que contienen las variantes.** También se llama arquitectura de plugins. Un **plugin** es un componente que aporta una capacidad especializada mediante un punto de extensión definido por el núcleo. El núcleo descubre, selecciona y utiliza esa capacidad sin incorporar sus reglas particulares.

## Qué problema resuelve

El problema no es únicamente tener mucho código. Es que una misma operación admite muchas variantes que cambian de forma independiente. Una empresa de reciclaje procesa teléfonos, tabletas y portátiles: la recepción del equipo puede seguir siempre el mismo flujo, pero las pruebas y reglas de valoración varían por modelo. Una aseguradora tramita siniestros con un proceso común, pero aplica reglas distintas según la jurisdicción. Si cada nueva variante modifica una gran cadena de condiciones en el centro, el centro se convierte en el lugar donde coinciden todos los cambios.

El estilo busca una frontera: **lo que permanece relativamente estable se conserva en el núcleo; lo que cambia por modelo, cliente, región o capacidad se coloca en plugins**. La estabilidad es relativa al negocio. Un método corto que decide todas las variantes sigue siendo un punto de cambio frecuente; un núcleo más grande que coordina un flujo verdaderamente estable puede respetar mejor el propósito.

El libro lo presenta como especialmente natural para productos instalables, pero también para aplicaciones internas que necesitan personalización. El producto puede distribuirse como una sola entrega monolítica: **monolito** describe la unidad de despliegue, no una obligación de mezclar todas las responsabilidades.

## Las dos piezas

El **núcleo** proporciona la base y los puntos de extensión. El libro ofrece dos definiciones compatibles: la funcionalidad mínima para ejecutar el sistema y el *happy path*, es decir, el flujo general con poca personalización. Ese segundo significado no exige ignorar errores. Un núcleo bien definido sigue teniendo responsabilidades comunes como rechazar una solicitud inválida o registrar que una evaluación falló; las reglas particulares de cada evaluación quedan fuera.

El **plugin** contiene una variante autocontenida. Autocontenida significa que encapsula su comportamiento y puede probarse con su contrato. No significa que funcione sin una plataforma, configuración o dependencias técnicas. Lo que se intenta evitar son dependencias hacia las implementaciones internas de otros plugins.

![Núcleo estable y plugins de evaluación](../Recursos%20visuales/Cap%C3%ADtulo%2013/c13-01-nucleo-plugins.png)

El marco exterior representa una entrega habitual. Las cajas verdes contienen reglas particulares; la azul conserva recepción, elección, persistencia y comunicación. Las flechas indican invocación desde el núcleo, no una cadena de transformaciones entre extensiones. Aunque existan tres plugins, una solicitud para un teléfono normalmente utiliza el correspondiente al teléfono, sin atravesar los otros dos.

## Por qué reduce el impacto de los cambios

En Going Green, el caso del libro, la versión inicial decide el modelo con una secuencia de `if` y `else`. Cada nuevo dispositivo exige editar esa selección y ampliar las pruebas del centro. La versión revisada consulta un registro, obtiene el plugin y llama a su operación de evaluación. El flujo del núcleo permanece igual; cambian el catálogo de capacidades y la implementación de una regla.

**La complejidad no desaparece: cambia de lugar.** La complejidad ciclomática estima los caminos independientes de control en una función. Extraer condiciones de negocio del núcleo puede bajar su complejidad, pero cada plugin sigue teniendo sus propias decisiones. La ganancia es que las decisiones del teléfono no se mezclan con las de la tableta. Un cambio de batería no debería obligar a entender la valoración de todos los demás equipos.

Este diseño exige que el núcleo dependa de un **contrato**, una definición común de entradas, salidas y comportamiento, en lugar de depender de cada clase concreta. Un registro que devuelve nombres de clases pero termina en otro gran `switch` especializado solo mueve la lista de variantes: todavía hay que cambiar el centro para cada nueva capacidad.

## Qué no promete por sí solo

Una buena frontera facilita mantener y probar, pero no crea automáticamente aislamiento de fallos. Dos plugins dentro del mismo proceso pueden compartir memoria, hilos y conexiones. Un plugin que consume toda la memoria puede afectar al núcleo. Tampoco garantiza actualización en caliente: eso depende de cómo se cargan y retiran las extensiones.

> [!question]- ¿Un plugin es lo mismo que un filtro del capítulo 12?
> No. El filtro define una transformación dentro de un recorrido de datos. El plugin define una variante o capacidad que el núcleo puede seleccionar. Un plugin puede contener un pipeline interno, pero la relación núcleo–extensión y la relación etapa–etapa responden a problemas diferentes.

> [!question]- ¿Qué evidencia muestra una buena separación?
> Al agregar un modelo de dispositivo cambian el nuevo plugin, su registro y sus pruebas, pero no el flujo general de recepción y evaluación. Si la operación pide también cambiar el contrato, hay que revisar si existe una nueva capacidad común o si se está filtrando una particularidad hacia el núcleo.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/10 Arquitectura microkernel.pdf#page=1|PDF 1–3 · impresas 193–195 · figura 13-1 y caso Going Green]]. La explicación de memoria compartida y los criterios de revisión son elaboración didáctica.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/00 Índice|← Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/02 Composición espectro e interfaz|Siguiente →]]
