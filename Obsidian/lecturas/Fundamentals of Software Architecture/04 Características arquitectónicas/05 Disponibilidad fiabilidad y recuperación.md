---
title: "Capítulo 4 · Características arquitectónicas · Disponibilidad fiabilidad y recuperación"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 4
orden: 5
---

# Disponibilidad fiabilidad y recuperación

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 4 · Características arquitectónicas](00%20%C3%8Dndice.md) → Nota 5 de 7

**Objetivo:** Distinguir disponibilidad, RTO, RPO y resultados reales.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 5. Disponibilidad, fiabilidad y recuperación

**Ampliación didáctica sobre conceptos presentes en PDF pp. 5 y 8; impresas 59 y 62.** Disponibilidad pregunta si el servicio está utilizable; fiabilidad, si cumple su función durante un intervalo bajo condiciones especificadas. Un servicio accesible que pierde pedidos no es fiable para esa función. Tolerancia a fallos permite seguir funcionando pese a ciertos fallos; recuperabilidad permite restablecer datos y operación después de una interrupción.

Para una medición temporal con disponibilidad binaria:

$$
A=\frac{T_{\text{observado}}-T_{\text{indisponible}}}{T_{\text{observado}}}.
$$

En 30 días de servicio continuo hay 43.200 minutos. Un objetivo de 99,9 % permite como máximo 43,2 minutos de indisponibilidad en esa ventana. Hay que acordar qué significa «disponible», qué horario cuenta y cómo tratar fallos parciales. Una proporción de solicitudes exitosas usa otro denominador y no equivale automáticamente al porcentaje temporal.

Una instancia alternativa puede aportar tolerancia al fallo de otra, pero no a un error compartido por ambas. Una copia de seguridad aporta recuperabilidad potencial; solo una restauración probada demuestra que permite recuperar el estado requerido.

### RTO y RPO: dos pérdidas diferentes

RTO es el **objetivo de tiempo de recuperación**: cuánto puede tardarse en restablecer el servicio definido. RPO es el **objetivo de punto de recuperación**: cuánta antigüedad máxima puede tener el estado recuperado respecto del incidente, expresada en tiempo. Son objetivos, no resultados garantizados por escribirlos.

![RTO y RPO: dos pérdidas diferentes ](../Recursos%20visuales/Diagramas/cap04-diagrama-03.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap04-diagrama-03.mmd)

**Interpretación:** el tramo previo representa una ventana potencial de pérdida de datos de dos minutos; el posterior, ocho minutos de recuperación. **Límite:** no muestra fallos parciales ni recuperación de cada subsistema; hay que definir cuándo se considera restablecido el servicio.

Con RTO = 10 min y RPO = 2 min, este resultado cumple ambos, suponiendo que el estado recuperado sea consistente. El tiempo efectivo es 12:08 − 12:00 = 8 min; la antigüedad del punto recuperable, 12:00 − 11:58 = 2 min. A 30 pedidos confirmados/min, y suponiendo pérdida completa de las escrituras de esa ventana, podrían faltar 60 pedidos. **RPO no mide número de pedidos**: esa conversión depende de la tasa y de qué escrituras se pierdan realmente.

Una copia cada dos minutos no garantiza RPO de dos minutos: puede fallar, estar incompleta o resultar inutilizable. Además, recuperación técnica y reconciliación comercial difieren: restaurar la base no cancela cobros ya aceptados por un proveedor externo.

![recuperacion](../Recursos%20visuales/07-recuperacion.png)

*Otro incidente hipotético: la ventana de datos en riesgo precede al fallo; la interrupción termina cuando el servicio vuelve a operar. Los objetivos se comparan con esos resultados.*

---

**Anterior:** [Rendimiento escalabilidad y elasticidad](04%20Rendimiento%20escalabilidad%20y%20elasticidad.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Lenguaje común y compromisos](06%20Lenguaje%20com%C3%BAn%20y%20compromisos.md)
