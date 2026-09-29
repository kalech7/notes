---
title: "08 · La trampa de las entidades y los nombres ambiguos"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/componentes
capitulo: 8
---

# La trampa de las entidades y los nombres ambiguos

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 21–22 · impresas 115–116 · figura 8-8** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Síntesis explicada del capítulo 8; los ejemplos, preguntas, tablas y diagramas adicionales se señalan como elaboración didáctica. Las recreaciones de figuras conservan la idea y las relaciones pertinentes, con rótulos en español; no son facsímiles.

## Por qué la entidad no basta para encontrar el componente

En un sistema de pedidos aparecen Cliente, Artículo y Pedido. Es tentador crear `CustomerManager`, `ItemManager` y `OrderManager` y colocar dentro todo lo que mencione esas entidades. El capítulo llama **Entity Trap** a este enfoque cuando produce componentes ambiguos y demasiado amplios.

Una entidad describe algo relevante del dominio. Un componente describe una responsabilidad del software. La relación entre ambos no es necesariamente uno a uno: un pedido participa en validación, preparación, transporte y pago, pero esas actividades pueden tener reglas, dependencias y ritmos de cambio diferentes.

![c08-06-entidades](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-06-entidades.png)

## Gestores genéricos frente a nombres concretos

La franja superior adapta la figura 8-8: tres gestores genéricos absorben listas cada vez mayores de actividades. Las flechas significan «este componente se hace cargo de estas tareas», no un orden de ejecución. Los puntos suspensivos implícitos de esas listas representan la facilidad con la que se sigue agregando funcionalidad.

La franja inferior añade una pregunta diagnóstica y nombres más concretos. «Validar pedido» permite anticipar qué comportamiento pertenece allí; «Gestionar pedido» permite casi cualquier comportamiento relacionado con el pedido.

Nombres imprecisos facilitan límites imprecisos. Aun así, renombrar una caja no arregla la implementación. Deben moverse responsabilidades, aclararse contratos y verificarse comportamiento. Tampoco basta contar verbos para decidir cuántos componentes crear.

## Los tres problemas del capítulo

**1. El nombre no explica el propósito.** Preguntar qué hace un gestor de pedidos y responder «gestiona pedidos» no agrega información. En cambio, «valida que el pedido contenga datos suficientes para continuar» delimita un resultado verificable.

**2. El componente se vuelve un contenedor de todo.** Cualquier nueva historia que mencione la entidad parece pertenecer allí. Con el tiempo se mezclan reglas de inventario, correo, transportistas y tarjetas. El componente acumula dependencias y hace difícil saber dónde corregir un comportamiento.

**3. La granularidad se vuelve demasiado gruesa.** El componente crece hasta ser difícil de comprender y probar. Un cambio pequeño puede exigir recorrer mucho código y preparar muchos colaboradores para ejecutarlo. No es el número de líneas por sí mismo, sino la mezcla de responsabilidades y dependencias lo que produce el problema.

## Señales que requieren investigar

El libro menciona sufijos como Manager, Supervisor, Controller, Handler, Engine y Processor como posibles indicios. No son palabras prohibidas: un `PaymentProcessor` con responsabilidad bien delimitada puede ser perfectamente comprensible. El problema aparece cuando el nombre sustituye una definición precisa de lo que hace el componente.

Una ficha útil, añadida como herramienta didáctica, contiene:

- **Propósito:** resultado que produce.
- **Incluye:** decisiones y reglas que posee.
- **Excluye:** responsabilidades de otros componentes.
- **Entradas y salidas:** información intercambiada.
- **Colaboradores:** de quién depende y por qué.
- **Motivos de cambio:** qué reglas provocarían modificarlo.

Si no puedes completar la ficha sin una lista de obligaciones poco relacionadas, revisa el límite.

## Ejemplo de descomposición razonada

`OrderManager` cobra, reserva existencias, prepara paquetes y envía correos. Una propuesta inicial sería Registrar pedido, Procesar pago, Gestionar inventario, Preparar pedido y Notificar. No es una orden de crear cinco microservicios: estos componentes pueden seguir dentro del mismo ejecutable.

La separación añade contratos y llamadas, por lo que también tiene coste. Hay que comprobar si los beneficios de claridad, pruebas y evolución justifican esos límites. Dividir todo en funciones minúsculas puede sustituir un componente gigante por una red de fragmentos inseparables.

## El caso de CRUD sencillo

El capítulo sugiere herramientas o marcos CRUD cuando el sistema realmente solo crea, consulta, modifica y elimina entidades. El punto es evitar inventar complejidad innecesaria. Como matiz didáctico, incluso una aplicación CRUD conserva decisiones sobre acceso, datos y operación; no debe interpretarse la frase del libro como que carece de cualquier necesidad arquitectónica.

**Ejercicio resuelto.** «Cambiar el domicilio del cliente» y «calcular la ruta del repartidor» comparten una dirección. ¿Deben estar juntas? No necesariamente. La primera pertenece a mantener información del cliente; la segunda a planificar entrega. Compartir datos es una relación que documentar, no una prueba de responsabilidad única.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/04 Descubrir componentes por flujos y acciones|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/06 Historias cohesión y distribución de responsabilidades|Siguiente →]]
