---
title: "72 S12 - Pasos presupuestos timeouts y condiciones de parada"
created: 2026-09-29
fecha: 2026-09-29
capitulo: 12
sesion: "12"
tags:
  - maestria/ia-generativa
  - agentes
  - estudio
---

# 72 S12 - Pasos presupuestos timeouts y condiciones de parada

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Un agente necesita reglas de terminación aunque su prompt diga «no te repitas». El texto orienta al modelo; **el programa decide cuántas oportunidades y recursos permite**. Hay que definir además qué unidad se cuenta.

## 1. Cuatro contadores que no son equivalentes

| Unidad | Qué cuenta | Ejemplo |
| --- | --- | --- |
| Decisión del modelo | Una llamada que pide la siguiente salida | Pedir estadísticas o producir texto final |
| Llamada de herramienta | Una ejecución externa | Consultar marzo |
| Evento de traza | Un registro | Solicitud, observación y cierre por separado |
| Intento | Una corrida completa para resolver la tarea | ReAct entero antes de recibir una crítica |

En el lunes adaptado, una consulta de estadísticas más texto final usa dos decisiones y una herramienta. Con `max_pasos=1`, el dato puede haberse obtenido, pero falta la segunda decisión para redactar. Una parada por límite es un estado distinto de «la herramienta no funcionó».

## 2. Tres protecciones con responsabilidades distintas

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/52-s12-tres-cortes.png|52-s12-tres-cortes.png]]

La primera caja limita vueltas, la segunda identifica solicitudes repetidas y la tercera reserva recursos. La caja inferior representa la salida controlada con razón registrada. Ninguna caja comprueba que el total o la respuesta sean correctos: esa responsabilidad corresponde a la evaluación.

Un máximo de pasos corta incluso acciones distintas e inútiles. Un detector puede explicar el estancamiento, pero falla ante paráfrasis o cambios de estado no modelados. Un presupuesto frena gasto, pero permite una respuesta barata y equivocada. El sistema puede comprobar las tres condiciones antes de ejecutar una propuesta.

## 3. El presupuesto se aplica antes de gastar

Si cada paso cuesta dos unidades ficticias y el presupuesto es siete, caben tres pasos: gasto 2, 4 y 6. El cuarto se rechaza porque $6+2=8>7$. Comprobar solo después permitiría exceder el límite.

Estas unidades son una simulación; no equivalen a tokens ni dólares. En un servicio real, un cálculo conservador reserva recursos antes de enviar la petición y después actualiza el contador con el uso reportado. Si hay varias tareas en paralelo, el presupuesto debe ser global y la reserva no puede permitir que dos tareas gasten el mismo saldo.

Un máximo de salida por llamada tampoco limita toda la corrida. Cinco decisiones pueden consumir cinco entradas y cinco salidas; las entradas tienden a crecer al reenviar el historial. Si $I_j$ y $O_j$ son tokens de entrada y salida de la llamada $j$:

$$T_{\text{corrida}}=\sum_{j=1}^{m}(I_j+O_j)$$

Para estimar dinero se usan tarifas verificadas del servicio y la distinción entre clases de tokens y caché que corresponda. Estas notas no asumen precios ni disponibilidad actual de los modelos nombrados en el notebook.

## 4. Un `for` finito no resuelve una operación bloqueada

La página 9 dice que el límite de pasos «siempre termina». Esa afirmación necesita una condición: **cada operación debe terminar o poder interrumpirse**. Si una llamada de red nunca devuelve, el programa no llega a incrementar el paso.

Por eso también hacen falta timeouts por operación y, cuando corresponda, una fecha límite para toda la corrida. Un timeout es el tiempo máximo de espera; no prueba que el efecto no se produjera. Si una operación de escritura pudo completarse pero se perdió la respuesta, reintentar sin idempotencia puede duplicarla.

La cancelación también depende del entorno: una herramienta o proceso que no coopera puede requerir aislamiento y cierre por parte del supervisor. Un límite en el prompt no aporta esa capacidad.

La nota 3 de ReAct informa que **entre las trayectorias con respuesta correcta** solo 0,84 % de HotpotQA usaron siete pasos y 1,33 % de FEVER cinco. Esos valores describen la longitud de casos acertados del estudio: no son la proporción de todas las corridas que agotaron un presupuesto, ni demuestran que recortar a ese máximo sea inocuo en una tarea distinta. La página 9 de clase los resume; el denominador precisa qué permiten concluir.

El texto de un prompt como «se puede repetir N veces» no prueba dónde se impone el límite. A la inversa, que una construcción de librería no pase explícitamente un parámetro tampoco demuestra que carezca de valor predeterminado interno. Estas notas no ejecutaron esa versión de LangChain: la propiedad que se debe verificar es si el **ejecutor efectivo**, con su configuración concreta, aplica el máximo.

## 5. Estados de salida útiles

Conviene distinguir `respuesta_final`, `verificado`, `max_pasos`, `repeticion`, `presupuesto`, `timeout` y `error_irrecuperable`. `respuesta_final` significa que el modelo dejó de pedir acciones; `verificado` significa que pasó un criterio explícito. No se deben mezclar.

Puede conservarse una **respuesta parcial**: «obtuve marzo, falta abril». Esto mantiene lo aprendido sin inventar el dato faltante. La traza registra el último resultado y la razón de parada, incluso cuando ocurre un error.

En Reflexion, tres intentos de hasta cinco decisiones permiten hasta 15 decisiones del actor, más evaluación y reflexión si usan modelos. En Plan-and-Execute, los replanes también consumen recursos. Presupuestos locales y globales deben diseñarse conjuntamente.

> [!question]- ¿La detección de una llamada repetida siempre debe bloquearla?
> Depende del contrato. En la simulación se adopta una política conservadora para entender el corte; una consulta repetida puede ser válida si el estado cambió o hay un reintento temporal limitado.

Fuentes: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-12.pdf#page=9|PDF 9]] y [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-12.pdf#page=19|PDF 19]], notebook del martes celdas 8–10. Timeouts, reservas y presupuestos anidados son precisiones de ingeniería añadidas a la explicación.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/71 S12 - Autopsia de trazas y detector de repetición|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/73 S12 - Reflexion entre intentos memoria y aprendizaje|Siguiente]] →

