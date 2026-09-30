---
title: "13 · Datos y propiedad del estado"
created: 2026-09-29
capitulo: 13
tags:
  - lecturas/software-architecture
  - arquitectura/microkernel
---

# Datos y propiedad del estado

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/00 Índice|← Índice del capítulo 13]]

**Un plugin puede tener datos propios sin acceder directamente a las tablas comunes del núcleo.** La propiedad del dato define quién controla su significado y su evolución; su ubicación física es otra decisión.

## La forma habitual

El libro describe aplicaciones monolíticas con una sola base de datos, normalmente relacional. El núcleo administra el acceso a los datos comunes y pasa al plugin lo necesario. Eso protege a la extensión de detalles de esquema, consultas y almacenamiento que no pertenecen a su regla especializada.

Un **esquema** define estructuras como tablas y columnas. Si todos los plugins consultan `devices.condition_code`, cambiar esa columna puede exigir editar muchos evaluadores. Si reciben un objeto de entrada cuyo campo `condicion` mantiene significado estable, el núcleo puede adaptar la nueva tabla a ese contrato. El cambio sigue existiendo, pero su impacto queda contenido.

![Propiedad de datos comunes y privados](../Recursos%20visuales/Cap%C3%ADtulo%2013/c13-05-propiedad-datos.png)

La base gris conserva dispositivos, estados y resultados comunes. La extensión verde recibe una entrada preparada por el núcleo. El almacén amarillo pertenece únicamente a la extensión y contiene reglas del modelo. Las flechas representan quién accede a cada almacén; la independencia de la extensión se perdería si otros plugins comenzaran a consultar directamente sus tablas privadas.

## Almacenes privados de plugins

La figura 13-8 muestra que cada extensión puede poseer su almacén externo. El texto admite también bases embebidas o en memoria. Una **base embebida** forma parte del proceso o del producto; un **almacén en memoria** conserva datos en memoria durante la ejecución. No todos ofrecen la misma durabilidad. La topología permite estas opciones sin exigir que cada plugin tenga obligatoriamente una base.

En Going Green, un evaluador puede poseer reglas específicas del producto o un motor de reglas. El núcleo no necesita conocer cómo representa internamente umbrales o fórmulas, siempre que el resultado cumpla el contrato. Una extensión sencilla puede usar configuración inmutable en lugar de una base; introducir persistencia propia se justifica si hay datos que realmente necesita administrar.

## Tres tipos de estado en un ejemplo propio

| Estado | Dueño razonable | Motivo |
|---|---|---|
| Expediente del dispositivo y su propietario | Núcleo | Es común al proceso completo |
| Regla de descuento por batería del modelo A | Plugin A | Cambia por la variante |
| Identificador y estado de evaluación pendiente | Coordinación del núcleo | Enlaza la solicitud con su resultado |

Esta división evita que el núcleo se convierta en intérprete de todas las reglas, y evita que cada plugin replique todo el expediente. Pasar menos datos también hace explícita la dependencia real. Si una extensión solo necesita modelo, estado de batería y daños, no necesita recibir todo el historial de clientes.

El objeto de entrada no debería entregar referencias mutables a todo el estado interno. Si el plugin modifica directamente el expediente compartido, el núcleo pierde el control de invariantes. Una **invariante** es una condición que debe mantenerse, como «un expediente cerrado no vuelve a pendiente sin una reapertura registrada». Una entrada específica y un resultado validado permiten conservar ese control.

## Consistencia y trazabilidad

Como ampliación propia, almacenar en dos lugares introduce una pregunta: ¿qué se considera completado si el plugin guardó su evaluación, pero el núcleo todavía no registró el resultado? Una transacción local en la base común no cubre automáticamente un almacén externo. Se necesita definir quién conserva el resultado, cómo se reenvía y cómo se reconoce un duplicado.

Para poder explicar una decisión anterior, conviene guardar la versión de las reglas que produjo el resultado. «La evaluación dijo 80» no basta si mañana cambió la tabla de depreciación. Registrar entrada relevante, identificador de operación, versión de plugin/reglas y resultado permite reconstruir qué ocurrió. Esto es una propuesta didáctica, no una exigencia detallada por el capítulo.

La propiedad privada tampoco equivale a incapacidad de observar. El plugin puede publicar un resultado o métricas por contrato; lo que se evita es exponer libremente sus tablas y permitir que otros componentes interpreten su estado interno.

## El coste de una entrada demasiado amplia

Un contrato que recibe un `ContextoGlobal` con acceso a bases, red y objetos del núcleo parece flexible, pero permite que la extensión dependa de todo. La independencia aparente oculta un acoplamiento alto. Un contrato que recibe solo datos insuficientes obliga a realizar muchas consultas de vuelta. La elección busca una entrada coherente para completar la operación, con capacidades adicionales limitadas y explícitas cuando sean necesarias.

> [!question]- ¿Una base privada convierte al plugin en microservicio?
> No. Puede estar embebida dentro del monolito. Propiedad de datos y frontera de proceso son decisiones diferentes; la clasificación de la arquitectura requiere examinar ejecución y despliegue completos.

> [!question]- ¿El núcleo debe conocer cómo se calcula el precio?
> No necesita conocer las reglas de cada modelo para coordinar. Sí necesita un resultado con unidades y significado conocidos, y puede validar condiciones comunes como importes válidos o una versión de contrato aceptada.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/10 Arquitectura microkernel.pdf#page=10|PDF 10–11 · impresas 202–203 · figura 13-8]]. Ejemplos de invariantes, trazabilidad y consistencia son elaboraciones propias.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/05 Acceso remoto nube y quantum|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/07 Riesgos dependencias y gobierno|Siguiente →]]
