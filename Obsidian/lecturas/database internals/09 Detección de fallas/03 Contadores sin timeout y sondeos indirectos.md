---
title: "Database Internals — Contadores sin timeout y sondeos indirectos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 9
tags:
  - lecturas/database-internals
  - arquitectura/deteccion-de-fallas
---

# Contadores sin timeout y sondeos indirectos

[[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice del capítulo 9]]

## Información de avance sin decidir por segundos

El detector **Heartbeat sin timeout** descrito por el libro representa observaciones mediante contadores. El objetivo es proporcionar información de avance sin que el detector dependa de un plazo temporal fijo. Esto no elimina la dificultad de decidir qué acción ejecutar ni crea conocimiento infalible de caídas en un sistema totalmente asíncrono.

Sus supuestos son relevantes: todos los procesos conocen la existencia de los demás y cada par de procesos correctos está conectado mediante un **camino justo**. Un enlace justo permite que, si se retransmite una señal indefinidamente, lleguen señales indefinidamente. No exige que cada envío individual llegue ni que lo haga dentro de un plazo. Un camino compuesto por tales enlaces puede transmitir avance aun cuando falle el enlace directo entre dos participantes.

Cada proceso mantiene vecinos y contadores. Un heartbeat transporta un identificador para evitar difusión duplicada y una ruta de procesos por los que pasó. Al recibir evidencia nueva, el receptor incrementa contadores correspondientes a participantes incluidos en esa ruta. Después añade su propia identidad y transmite por vecinos que aún no aparecen en ella. El capítulo usa la ruta para limitar repeticiones y reconocer qué participantes contribuyeron a propagar la evidencia.

**Ejemplo propio.** A no recibe directamente de C, pero C envía una señal que pasa por B y llega a A con la ruta `[C, B]`. A aprende que una señal reciente pudo atravesar esos participantes. No necesita que funcione A–C para observar avance de C. Si se retransmite otra copia de la misma señal, su identificador evita contarla como nueva evidencia.

Los contadores permiten comparar actividad observada. Pero un valor pequeño puede deberse a poca propagación y no a caída. El propio capítulo señala que interpretar la diferencia entre contadores exige un criterio y que un criterio inadecuado puede producir sospechas falsas. «Sin timeout» describe la construcción de la evidencia, no una autorización para concluir perfectamente quién murió.

## Delegar un sondeo cuando falla la ruta directa

Los **sondeos indirectos**, denominados outsourced heartbeats en el libro, usan intermediarios para comprobar otra ruta. En el mecanismo descrito para SWIM, A pregunta a B; si no obtiene respuesta, elige algunos participantes y les pide intentar contactar a B. Si C obtiene un ACK de B, transmite la confirmación a A.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 09/02-sondeo-indirecto.png]]

El tramo rojo representa un ACK perdido en la consulta directa. Las flechas que pasan por C muestran la consulta delegada y el regreso de su confirmación. El mensaje exitoso permite a A conservar evidencia de que B responde mediante C. La causa inicial puede ser la ruta A–B; no hace falta convertirla en una acusación contra la ejecución de B. Es un escenario conceptual propio y usa un solo intermediario para hacer visible la ruta.

La figura 9-3 del libro usa dos intermediarios, P3 y P4, para verificar P2. Lanzar verificaciones en paralelo permite reunir más información sin esperar una secuencia completa de pruebas. La respuesta positiva de un intermediario puede bastar para evitar una acusación basada exclusivamente en el enlace directo, según la política del protocolo.

## Lo que se gana y lo que sigue incierto

La ventaja es **diversidad de observaciones**: no todas las noticias proceden de un único camino. Se evita difundir la consulta a cada miembro del sistema si basta un subconjunto. El capítulo contrapone esta selección a mecanismos que necesitan conocer a todos los procesos para propagar sus contadores. Esa comparación se refiere a la evidencia y al sondeo descritos aquí; no debe extrapolarse a toda implementación posible de listas de miembros.

La ausencia de respuesta de todos los intermediarios continúa siendo una sospecha. Pueden compartir el mismo switch averiado, la misma región congestionada o una partición que separa a B de todo el subconjunto consultado. «Dos testigos» no equivale a «dos fallas independientes». La robustez depende de las rutas y de los dominios de falla representados por esos testigos.

Una comprobación positiva demuestra capacidad de responder durante esa comprobación. Si B cae inmediatamente después, la noticia aún debe caducar o ser reemplazada por evidencia nueva. Por eso conviene distinguir **existencia de una ruta**, **recencia del mensaje** y **autoridad para actuar sobre el sistema**.

> [!question]- ¿Qué concluye A si C sí obtiene respuesta de B, pero A no?
> Que B pudo responder por la ruta de C en ese momento y que la observación directa de A era incompleta. A puede tratar su ruta directa como problemática. No puede afirmar que todas las rutas a B funcionan ni que B nunca caerá.

> [!question]- ¿Qué concluye A si nadie obtiene respuesta de B?
> Que carece de evidencia positiva dentro del criterio de comprobación. Puede elevar la sospecha y activar una recuperación prevista por el protocolo. La causa puede seguir siendo caída, aislamiento o demora común de las rutas.

**Referencia:** PDF 3–5 · impresas 197–199 · figuras 9-3. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=3|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/09 Detección de fallas/02 Pings heartbeats y plazos|Anterior]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/04 Phi-accrual adaptación y umbrales|Siguiente]] →
