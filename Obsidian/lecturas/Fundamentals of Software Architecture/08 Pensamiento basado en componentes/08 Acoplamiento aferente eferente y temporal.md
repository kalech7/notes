---
title: "08 · Acoplamiento: entradas, salidas y dependencias invisibles"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/componentes
capitulo: 8
---

# Acoplamiento: entradas, salidas y dependencias invisibles

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 27–28 · impresas 121–122 · figuras 8-11, 8-12 y 8-13** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Síntesis explicada del capítulo 8; los ejemplos, preguntas, tablas y diagramas adicionales se señalan como elaboración didáctica. Las recreaciones de figuras conservan la idea y las relaciones pertinentes, con rótulos en español; no son facsímiles.

## Qué hace que dos componentes estén acoplados

Hay acoplamiento cuando los componentes se comunican o cuando un cambio en uno puede afectar al otro. La segunda condición es importante: no encontrar una flecha de llamada directa no demuestra independencia. Compartir un formato, una regla implícita o un orden obligatorio también puede propagar cambios.

El capítulo llama **acoplamiento estático** al contexto de comunicación sincrónica y distingue dependencias aferentes y eferentes. Estas notas siguen esa terminología del texto; no pretenden convertirla en la única clasificación usada en toda la literatura.

> [!note] Puente con el capítulo 7
> Aquí se analizan relaciones entre **componentes lógicos** y el texto usa esta clasificación para explicar Ca y Ce. El capítulo 7 utiliza el acoplamiento para analizar **límites de quanta y comportamiento operativo**. Son niveles y enfoques distintos: esta sección no redefine el límite de un quantum, ni afirma que toda comunicación sincrónica fusione automáticamente dos quanta. Para decidir ese límite hay que recuperar las condiciones y el contexto del capítulo 7, no trasladar sin más una etiqueta de este capítulo.

![c08-08-acoplamiento](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-08-acoplamiento.png)

## Aferente: cuántos otros dependen de mí

El acoplamiento aferente, `Ca`, también se llama entrante o *fan-in*. En el panel superior, Registrar pedido y Enviar pedido utilizan Notificar. Mirando desde Notificar, llegan dos dependencias:

$$C_a(\text{Notificar}) = 2$$

Esto nos hace preguntar quién podría verse afectado si cambia el contrato de Notificar. Un valor alto no es automáticamente malo: una función útil y estable puede tener muchos consumidores. Sí exige cuidar compatibilidad, estabilidad y pruebas de integración.

## Eferente: de cuántos otros dependo

El acoplamiento eferente, `Ce`, también se llama saliente o *fan-out*. En el panel central, Registrar depende de Preparar:

$$C_e(\text{Registrar}) = 1$$

El cálculo se hace **solo sobre ese panel**, que es un ejemplo independiente. No se deben sumar relaciones de todos los dibujos de la guía como si pertenecieran a un único sistema completo.

En el gráfico, el origen de cada flecha depende de su destino. La misma arista A → B incrementa `Ce(A)` y `Ca(B)`. No son dos llamadas diferentes: son dos perspectivas de una relación.

**Conclusión del gráfico:** el componente objetivo cambia lo que se cuenta. **Límite:** contar conexiones no explica por sí solo su gravedad. Una dependencia con un contrato cambiante puede ser más costosa que varias dependencias estables.

## Cálculo completo, paso a paso

Elaboración propia. Un grafo contiene A → B, A → C, D → B y B → C.

| Componente | Entradas | Ca | Salidas | Ce |
|---|---|---:|---|---:|
| A | Ninguna | 0 | B, C | 2 |
| B | A, D | 2 | C | 1 |
| C | A, B | 2 | Ninguna | 0 |
| D | Ninguna | 0 | B | 1 |

Hay cuatro aristas; la suma de `Ca` es cuatro y la suma de `Ce` también es cuatro. Esta igualdad permite comprobar que no se ha olvidado una conexión al contar. No significa que el sistema tenga «ocho dependencias»: cada arista aparece una vez en cada perspectiva.

El cálculo cuenta componentes distintos relacionados, no peticiones por segundo. Si A llama cien veces a B durante una operación, la frecuencia afecta rendimiento y comportamiento, pero no convierte automáticamente una relación estructural en cien destinos distintos.

## Acoplamiento temporal

Existe cuando una actividad necesita que otra suceda antes, o cuando ambas están relacionadas por una unidad de trabajo. El ejemplo del libro: registrar el pedido debe ocurrir antes de enviarlo. El contrato temporal puede existir incluso cuando las dos piezas no se llaman directamente.

Como desarrollo didáctico, imagina que un evento «enviar pedido» llega antes de que el pedido esté disponible. Si el sistema da por hecho el orden pero nunca lo valida, el error aparece en ejecución. Hay que explicitar precondiciones, estados y manejo de situaciones fuera de orden; agregar una cola no elimina por sí mismo la dependencia temporal.

## Dependencia de cambio sin llamada

Dos componentes podrían interpretar el mismo campo `estado=3` como «listo para despacho». Si uno cambia esa convención y el otro no, el sistema falla aunque no exista una llamada directa entre ambos. El capítulo enfatiza este tipo de afectación; el ejemplo del código de estado es una ampliación didáctica.

**Ejercicio resuelto.** Pago deja de llamar a Inventario y publica un evento que Inventario entiende. ¿Desapareció todo acoplamiento? No. Puede cambiar el tipo de comunicación, pero siguen existiendo dependencia del significado del evento, del esquema y posiblemente del momento en que se procesa. Para evaluar la mejora debemos especificar qué dependencia se redujo y cuál permanece.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/07 Características arquitectónicas y granularidad|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/09 Ley de Demeter y conocimiento mínimo|Siguiente →]]
