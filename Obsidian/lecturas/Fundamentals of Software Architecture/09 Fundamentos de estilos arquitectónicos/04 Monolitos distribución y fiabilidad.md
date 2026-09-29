---
title: "Monolitos distribución y fiabilidad"
created: 2026-09-28
capitulo: 9
tags:
  - lecturas/software-architecture
  - arquitectura/estilos
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/00 Índice|← Índice del capítulo 9]]

# Monolitos, distribución y fiabilidad

**Distribuir cambia el modo de fallar.** Un sistema puede tener componentes correctos y sanos, pero no completar una operación porque la comunicación entre ellos falla o porque un participante ignora qué ocurrió en el otro.

## 1. Qué se está clasificando

El capítulo distingue estilos **monolíticos**, con una unidad de despliegue del código de la aplicación, de estilos **distribuidos**, con varias unidades que colaboran mediante protocolos remotos. Esta es una clasificación útil de estilos, no una afirmación de que el monolito viva aislado de toda red.

| Categoría presentada | Estilos que menciona el capítulo |
|---|---|
| Monolítica | Capas, pipeline, microkernel; el capítulo también usa el monolito modular como ejemplo en su explicación de partición |
| Distribuida | Basada en servicios, dirigida por eventos, basada en espacio, orientada a servicios, microservicios |

El listado formal de la impresa 143 omite el monolito modular pese a haberlo descrito en la 137 y dedicarle el capítulo 11. Se conserva el contexto para que la omisión no se interprete como una clasificación opuesta.

El libro presenta la distribución como una vía para ciertas capacidades operacionales. **No se debe convertir eso en «distribuido siempre rinde mejor».** Separar permite escalar o aislar partes bajo ciertas condiciones, pero añade red y coordinación. El beneficio depende de carga, datos, fronteras, protocolos y capacidad operativa.

**Fuente:** PDF p. 14, impresa 143; contexto del monolito modular en PDF p. 8, impresa 137.

## 2. Primera falacia: suponer que la red es fiable

La figura 9-7 muestra que A puede no alcanzar B aunque B funcione. Hay que distinguir:

1. La petición no sale o no llega.
2. La petición llega, pero B falla antes de terminar.
3. B termina y la respuesta se pierde.
4. La respuesta tarda más que el tiempo que A está dispuesto a esperar.

Desde A, varios casos pueden parecer el mismo timeout. **No recibir respuesta no demuestra que la operación no ocurrió.** Esta incertidumbre es central en un pago, una reserva o una transferencia.

![Operación completada cuya respuesta se pierde](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c09-02-respuesta-perdida.png)

La petición de cobro llega al servicio, que registra el resultado, pero la respuesta no vuelve. El emisor sabe que esperó demasiado, pero no puede concluir si se cobró. Un nuevo intento con la misma identidad de operación permite consultar o recuperar el resultado sin introducir un segundo efecto, si el receptor implementa correctamente esa garantía.

La imagen es una elaboración propia inspirada en la falacia 1. El reintento idempotente es una ampliación didáctica: la imagen no demuestra cómo se conserva la clave, su retención o su atomicidad con el efecto. Esos detalles determinan la garantía real.

**Fuente:** PDF p. 15, impresa 144, figura 9-7.

## 3. Qué resuelven los mecanismos habituales

Un **timeout** limita cuánto espera el llamador. Evita retener recursos indefinidamente, pero no cancela necesariamente el trabajo remoto ni revela su resultado.

Un **circuit breaker** deja de intentar temporalmente llamadas a una dependencia que está fallando según una política. Protege recursos y reduce presión. No repara la red ni decide cómo resolver una operación de negocio incompleta.

Un **reintento** puede superar un fallo transitorio. También puede repetir un efecto o multiplicar la carga cuando todos reintentan. Una política necesita límite, espera y criterios de qué errores justifican otro intento.

La **idempotencia**, como ampliación de estudio, significa que repetir una operación identificada conserva el efecto previsto sin ejecutarlo de nuevo indebidamente. No basta generar una clave en el cliente: el servidor debe reconocerla y guardar la decisión de forma coherente con el cambio de estado. Puede requerir comparar que el mismo identificador no se reutilice con un contenido distinto.

## 4. Ejemplo razonado: reservar la última unidad

**Supuesto propio.** Pedidos solicita a Inventario reservar la última unidad con identificador `reserva-742`. Inventario acepta y confirma internamente. La respuesta se pierde.

**Diseño ingenuo:** Pedidos crea una nueva reserva porque interpreta el timeout como rechazo. Puede acabar duplicando una intención o mostrando «sin existencias» aunque su primera reserva sí exista.

**Diseño a evaluar:** Pedidos conserva el identificador de la intención y consulta su estado o reintenta la misma operación. Inventario puede devolver «ya aceptada» sin una segunda reserva. Si el estado sigue desconocido, el flujo informa un estado pendiente y tiene un procedimiento de reconciliación.

**Costo:** estado adicional, retención de identificadores, observabilidad y una política para solicitudes que permanecen inciertas. **Beneficio:** distinguir una operación nueva de la repetición de una operación anterior.

## 5. Más dependencias no equivalen automáticamente a más disponibilidad

Como cálculo didáctico simplificado, si una operación requiere tres participantes simultáneamente disponibles, cada uno con probabilidad de éxito 0,999, y se asume independencia, su probabilidad conjunta sería:

$$
0{,}999^3 = 0{,}997002999 \approx 99{,}7003\,\%
$$

Este cálculo no es un SLA ni predice una instalación real: los fallos pueden correlacionarse y existir redundancia, cachés, recuperación o degradación. Su función es mostrar que una cadena de dependencias obligatorias puede empeorar la probabilidad de completar el recorrido aunque cada componente parezca muy fiable.

> [!question] ¿Un monolito no necesita timeouts?
> Sí los necesita cuando llama a bases remotas, APIs u otras dependencias. La diferencia analizada es cuántas comunicaciones internas se convierten en remotas y qué alcance de fallo se introduce.

> [!question] ¿Un timeout significa «pago rechazado»?
> No. Significa que no se obtuvo respuesta dentro del plazo. Rechazo es un resultado de negocio; incertidumbre de comunicación es otro estado.

> [!question] ¿Se puede resolver todo con una cola?
> No. Una cola cambia la coordinación temporal, pero conserva contratos, posibilidad de duplicados, retrasos y necesidad de conocer el estado final.

## Fuente principal

- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/06 Fundamentos de estilos arquitectónicos.pdf#page=14|Fundamentals of Software Architecture, 2.ª ed., capítulo 9, PDF pp. 14–15; impresas 143–144]].

Las explicaciones, diagramas y ejemplos identificados como propios son elaboraciones didácticas; las páginas indicadas permiten contrastar los conceptos con el escaneo.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/03 Silicon Sandwiches y decisiones de partición|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/05 Latencia ancho de banda y costo|Siguiente →]]
