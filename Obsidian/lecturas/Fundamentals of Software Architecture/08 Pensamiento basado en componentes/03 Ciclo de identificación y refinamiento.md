---
title: "08 · El ciclo de componentes: una hipótesis que se revisa"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/componentes
capitulo: 8
---

# El ciclo de componentes: una hipótesis que se revisa

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 18–19 y 26–27 · impresas 112–113 y 120–121 · figura 8-6** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Síntesis explicada del capítulo 8; los ejemplos, preguntas, tablas y diagramas adicionales se señalan como elaboración didáctica. Las recreaciones de figuras conservan la idea y las relaciones pertinentes, con rótulos en español; no son facsímiles.

## Un diseño inicial no es una decisión definitiva

Crear arquitectura lógica consiste en proponer componentes y refinarlos con evidencia. El primer inventario es una **hipótesis de organización**, no una predicción perfecta del sistema terminado. El libro advierte contra invertir demasiado esfuerzo en acertar cuando todavía se sabe poco sobre los requisitos.

![c08-04-ciclo](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-04-ciclo.png)

## Explicación del ciclo

La caja de entrada identifica funciones principales. Después se entra en un circuito de cuatro actividades. Las flechas expresan orden de revisión, no ejecución del software:

1. **Identificar candidatos.** Nombrar los grandes bloques que parecen necesarios según acciones o recorridos del usuario.
2. **Asignar historias y requisitos.** Relacionar comportamientos concretos con los bloques que los implementarán. Una **historia de usuario** expresa una necesidad desde el punto de vista de quien la usa; por ejemplo: «Como cliente, quiero elegir un horario para recoger mi pedido». Sus criterios de aceptación concretan cuándo está satisfecha.
3. **Analizar roles y responsabilidades.** Revisar si cada conjunto de comportamientos corresponde a un propósito coherente y manejable.
4. **Analizar características arquitectónicas.** Comprobar si rendimiento, disponibilidad, elasticidad, mantenibilidad y otras necesidades justifican límites distintos.
5. **Reestructurar o añadir.** Dividir, fusionar, mover responsabilidades o crear componentes; regresar a la asignación para verificar el resultado.

El paso 5 no significa que siempre debamos cambiar algo. Una revisión puede confirmar que los límites actuales son adecuados. El retorno a 2 es esencial: una separación aparentemente elegante puede dejar historias sin dueño o duplicar reglas.

**Conclusión visual:** el conocimiento se incorpora por iteración. **Límite del gráfico:** no indica duración de las iteraciones ni obliga a una ceremonia específica. Una conversación breve, una prueba o el análisis de un incidente pueden iniciar el ciclo.

## Aplicación: recoger un pedido en tienda

El libro propone el caso de un sistema que antes enviaba pedidos a domicilio y ahora debe admitir recogida en tienda. Desarrollemos su razonamiento:

| Momento | Pregunta | Posible resultado |
|---|---|---|
| Función nueva | ¿Cómo elige el cliente lugar y horario? | Candidato Programar recogida |
| Historias | ¿Quién muestra los turnos disponibles y confirma el elegido? | Responsabilidad de programación |
| Roles | ¿Registrar pedido está calculando capacidad de cada tienda? | Mover esa regla al componente adecuado |
| Características | ¿La consulta de horarios recibe mucha más carga que la confirmación? | Evaluar límites y comportamiento diferentes |
| Revisión | ¿Preparar pedido sabe si se envía o se recoge? | Ajustar contrato y trazabilidad del flujo |

Solo la idea general de añadir recogida procede del ejemplo del libro; las preguntas detalladas son elaboración didáctica. No es obligatorio crear exactamente Programar recogida: un sistema pequeño podría resolverla dentro de un componente existente si sus responsabilidades siguen siendo coherentes.

## Evidencia útil para decidir

Un límite mejora cuando puede justificarse mediante observaciones: reglas que cambian juntas, pruebas difíciles de aislar, demasiadas dependencias, ritmos de carga diferentes o necesidad de limitar el impacto de fallos. «Me gusta el nombre» es evidencia débil. «Cada modificación de precios obliga a tocar registro de pedidos» es una pista concreta de conocimiento mal distribuido.

Los desarrolladores participan porque descubren detalles durante la implementación. El arquitecto no puede anticipar todos los casos extremos. El conocimiento sobre quién debería ser dueño de una regla se vuelve más preciso a medida que se construye el sistema.

## Cuándo detener una iteración

No hay un punto final permanente, pero sí podemos cerrar una revisión: las historias actuales tienen responsables, los contratos son comprensibles, los límites responden a prioridades conocidas y las dudas restantes están registradas. Seguir cambiando componentes sin nuevas razones genera trabajo sin mejorar la estructura.

**Ejercicio resuelto.** Un equipo descubre después de programar que Notificar contiene generación de facturas y envío de correos. ¿Es un fallo haber cambiado el diseño? El descubrimiento es parte del proceso. Debe analizar si crear documentos fiscales y transportar mensajes constituyen responsabilidades distintas, revisar requisitos y refactorizar con pruebas de comportamiento. Lo incorrecto sería preservar un límite inadecuado solo porque estaba en el primer diagrama.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/02 Arquitectura lógica frente a física|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/04 Descubrir componentes por flujos y acciones|Siguiente →]]
