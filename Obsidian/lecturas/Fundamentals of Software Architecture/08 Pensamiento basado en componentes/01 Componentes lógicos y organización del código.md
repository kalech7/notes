---
title: "08 · Componentes lógicos: ver funciones antes que clases"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/componentes
capitulo: 8
---

# Componentes lógicos: ver funciones antes que clases

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 13–15 · impresas 107–109 · figuras 8-1, 8-2 y 8-3** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Síntesis explicada del capítulo 8; los ejemplos, preguntas, tablas y diagramas adicionales se señalan como elaboración didáctica. Las recreaciones de figuras conservan la idea y las relaciones pertinentes, con rótulos en español; no son facsímiles.

## Qué significa pensar en componentes

Un **componente lógico** es un conjunto de código relacionado que realiza una responsabilidad reconocible dentro del sistema. El arquitecto observa bloques como «procesar pagos», «preparar pedidos» o «notificar al cliente» y las relaciones entre ellos. Dentro de cada bloque habrá clases, funciones, validaciones y estructuras de datos; esas piezas colaboran para cumplir el propósito del componente.

La palabra **lógico** indica el nivel de descripción: estamos decidiendo qué responsabilidades existen y dónde están sus límites. Todavía no hemos elegido servidores, contenedores, protocolos ni cuántos ejecutables se desplegarán. Esta distinción evita diseñar una colección de servicios cuyo comportamiento interno nadie ha organizado.

## El gráfico del libro, explicado

![c08-01-componentes](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-01-componentes.png)

La parte izquierda conserva la idea de la figura 8-1: una vivienda se entiende mediante habitaciones con propósitos diferenciados. Una cocina tiene utensilios y actividades internas, pero al discutir el plano no comenzamos enumerando cada cuchara. La parte derecha adapta la figura 8-2 con cajas de funciones del sistema. Algunas funciones originales se han omitido para que el esquema siga legible; no es una reproducción completa de su inventario.

Cada rectángulo delimita una responsabilidad; la flecha entre casa y sistema expresa una analogía, no comunicación. La flecha inferior conecta la estructura del código con el componente que representa. Los colores solamente agrupan visualmente; no codifican prioridades o tecnologías.

**Conclusión:** una estructura se entiende mejor cuando sus partes tienen una función identificable. **Límite de la analogía:** las dependencias de software no son pasillos físicos, y dos componentes pueden colaborar sin estar «cerca» en un dibujo. Tampoco debe deducirse que todas las habitaciones o componentes necesitan el mismo tamaño.

## Cómo aparece en el repositorio

El libro vincula componentes con directorios o espacios de nombres. En su ejemplo, `order_entry/ordering/payment` representa procesamiento de pagos; `order_entry/processing/fulfillment` representa preparación del pedido. Los directorios superiores agrupan dominios; las hojas mostradas en ese esquema representan componentes.

```text
order_entry/
├── ordering/
│   ├── placement/     ← registrar pedido
│   ├── validation/    ← validar pedido
│   └── payment/       ← procesar pago
└── processing/
    ├── fulfillment/   ← preparar pedido
    └── shipment/      ← enviar pedido
```

El árbol anterior es una selección didáctica del ejemplo, no la transcripción íntegra de la figura 8-3. Dentro de `payment/` podría haber un servicio de aplicación, reglas de cobro, un adaptador del proveedor y pruebas. Que existan cuatro archivos no significa que existan cuatro componentes. Lo relevante es la responsabilidad común que esos archivos implementan.

> [!warning] No conviertas la forma de las carpetas en una regla automática
> En el modelo del libro las hojas representan componentes, pero un repositorio real puede contener carpetas de pruebas, recursos o subpaquetes internos. Comprueba comportamiento, dependencias y convenciones antes de llamar «componente» a cada directorio final.

## Ejemplo desarrollado: dónde poner una nueva regla

Supongamos que se añade la regla didáctica «no cobrar una tarjeta dos veces por el mismo intento de pago».

1. Identificamos la conducta: evitar duplicación de cobro.
2. Localizamos su propósito: pertenece a procesar pagos, aunque el pedido haya originado la solicitud.
3. Colocamos la regla en el código de pagos y definimos qué identificador necesita recibir.
4. Registrar pedido solicita el cobro por un contrato; no copia la lógica de deduplicación.
5. Las pruebas del componente verifican el comportamiento con solicitudes repetidas.

El beneficio es localizar cambios: una modificación en las reglas de cobro tiene un hogar conceptual. Esto no garantiza aislamiento absoluto, pues cambiar el contrato compartido todavía puede afectar a los consumidores.

## Lo que no debe confundirse

| Concepto | Pregunta que responde | Ejemplo |
|---|---|---|
| Dominio | ¿Qué área de negocio estamos organizando? | Pedidos |
| Componente lógico | ¿Qué responsabilidad coherente realiza el código? | Preparar pedido |
| Clase o función | ¿Cómo se implementa una parte de esa responsabilidad? | SeleccionarCaja |
| Servicio desplegable | ¿Qué unidad se ejecuta y despliega? | Servicio de operaciones |
| Base de datos | ¿Dónde y cómo persisten los datos? | Almacén transaccional |

**Ejercicio resuelto.** `OrderManager` contiene cobro, envíos, correos y preparación. ¿Es necesariamente un componente coherente? No: compartir «pedido» no basta. Es un candidato demasiado amplio y requiere analizar responsabilidades y dependencias. Un nombre genérico puede esconder cuatro motivos distintos para cambiar.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/02 Arquitectura lógica frente a física|Siguiente →]]
