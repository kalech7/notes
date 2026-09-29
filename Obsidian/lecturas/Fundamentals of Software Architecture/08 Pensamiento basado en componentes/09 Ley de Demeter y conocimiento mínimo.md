---
title: "08 · Ley de Demeter: limitar lo que cada componente necesita saber"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/componentes
capitulo: 8
---

# Ley de Demeter: limitar lo que cada componente necesita saber

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 29–31 · impresas 123–125 · figuras 8-14 y 8-15** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Síntesis explicada del capítulo 8; los ejemplos, preguntas, tablas y diagramas adicionales se señalan como elaboración didáctica. Las recreaciones de figuras conservan la idea y las relaciones pertinentes, con rótulos en español; no son facsímiles.

## El problema no es solo cuántas tareas ejecuta una caja

Un componente puede delegar todas las tareas y aun conocer demasiado sobre el resto del sistema. Si Registrar pedido sabe cómo reaccionar a existencias bajas, cuándo reponer, cuándo subir precios y cuándo notificar, participa en reglas que quizá deberían pertenecer a otros componentes.

La **Ley de Demeter**, presentada como principio de mínimo conocimiento, propone limitar el conocimiento que un componente o servicio tiene de otros. Aplicada al ejemplo, pregunta qué decisiones necesita realmente conocer Registrar pedido para cumplir su propósito.

![c08-09-demeter](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-09-demeter.png)

## Antes: Registrar conoce demasiadas consecuencias

En el panel superior, Registrar tiene cuatro dependencias salientes: Inventario, Notificar, Precios y Reponer stock. Al aceptar un pedido solicita disminuir existencias. Además, conoce la condición «si el stock queda bajo» y las dos acciones que se desencadenan: reposición y ajuste del precio.

La preocupación no es que Registrar ejecute internamente el cálculo del precio. Aunque lo delegue a Precios, todavía sabe **que debe ocurrir** ante una condición del inventario. Cambiar esa política puede obligar a modificar el flujo de registro de pedidos.

## Después: trasladar la decisión al responsable adecuado

En el panel inferior, Registrar solicita disminuir inventario y notificar. Inventario evalúa la condición de stock bajo y decide colaborar con Precios y Reponer stock. Así se mueve el conocimiento relacionado con existencias al componente que ya representa esa responsabilidad.

Cada flecha es una colaboración necesaria en el ejemplo. El cambio gráfico consiste en trasladar el origen de dos flechas desde Registrar hacia Inventario. La línea no desaparece del sistema: cambia quién debe conocerla.

| Medida del ejemplo | Antes | Después |
|---|---:|---:|
| Ce de Registrar | 4 | 2 |
| Ce de Inventario | 0 | 2 |
| Número de relaciones dibujadas | 4 | 4 |

**Conclusión:** Registrar tiene menos razones para cambiar cuando evoluciona la política de stock. **Límite:** el sistema completo no necesariamente reduce su número de dependencias. El libro aclara en p. 125 que aplicar Demeter suele **redistribuir** acoplamiento. Inventario tiene ahora más colaboraciones y debe conservar un propósito claro.

## Por qué un intermediario vacío no basta

Si insertamos una caja entre Registrar e Inventario pero Registrar sigue teniendo que ordenar «disminuye existencias», su dependencia saliente simplemente apunta al intermediario. No hemos retirado el conocimiento relevante. Agregar una capa o un «coordinador» no es una aplicación automática de Demeter.

Para que haya una mejora, identifica qué decisión deja de conocer el consumidor. Por ejemplo, Registrar no sabe el umbral exacto que causa reposición ni que ese umbral pueda cambiar con la temporada. Sigue conociendo que aceptar un pedido afecta existencias, porque esa colaboración es parte de su función.

## Ejemplo de evolución

Elaboración didáctica: mañana la política dice que el stock bajo debe avisar a compras, pero no modificar precios. En el diseño anterior, Registrar participa en ese cambio. En el revisado, el cambio se concentra principalmente en Inventario y sus colaboradores. Habrá que comprobar contratos y pruebas, pero el flujo de registro tiene menos conocimiento de esa política.

No debe interpretarse esto como que toda regla disparada por una compra pertenece a Inventario. La colocación depende de quién representa la decisión del dominio. Si una política realmente coordina varios ámbitos, podría requerir una responsabilidad de coordinación explícita y bien delimitada.

## Costes que deben mantenerse visibles

La distribución puede hacer que el recorrido completo ya no se vea en una sola función. Hay que conservar diagramas, trazabilidad y pruebas de escenarios completos. Si Inventario crece hasta decidir marketing, facturación y atención al cliente, simplemente hemos desplazado el componente excesivo a otra caja.

**Ejercicio resuelto.** Registrar llama a un nuevo `DoEverythingService`, que llama a Inventario, Precios y Notificar. ¿Se solucionó el problema? No puede afirmarse. Se redujo un número local de llamadas, pero tal vez se creó un componente sin propósito coherente. Debemos preguntar qué conocimiento se ocultó, si el nuevo componente tiene una responsabilidad legítima y qué cambios seguirán propagándose.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/08 Acoplamiento aferente eferente y temporal|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/10 Kata Going Going Gone y repaso resuelto|Siguiente →]]
