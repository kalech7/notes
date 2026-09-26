---
title: "Capítulo 5 · Identificar y priorizar características · De necesidades a decisiones"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 1
---

# De necesidades a decisiones

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 1 de 9

**Objetivo:** Convertir preocupaciones en preguntas verificables.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Una característica es una capacidad relevante para el éxito que puede influir en la estructura; debe expresarse mediante escenarios y lenguaje compartido. El catálogo del capítulo anterior ofrece nombres, pero todavía no indica cuáles importan en este dominio.

## 1. Identificar significa convertir necesidades en decisiones justificables

Una funcionalidad describe algo que el sistema permite hacer: registrar un pedido. Una característica describe una condición relevante para hacerlo: seguir aceptándolo durante un pico de demanda. Identificar características consiste en descubrir qué condiciones importan tanto que pueden orientar la estructura del sistema. No consiste en reunir palabras terminadas en «-idad».

**Libro — PDF p. 12, impresa 67:** hay al menos tres fuentes: preocupaciones del dominio, requisitos del proyecto y conocimiento implícito del dominio. Deben combinarse. Los requisitos pueden indicar cuántas personas usarán una aplicación; el conocimiento del negocio puede revelar que todas intentarán entrar a la misma hora.

En PedidoClaro, «no perder el almuerzo de las oficinas» expresa una preocupación comercial. Debemos preguntar cuándo se concentra la demanda y qué puede fallar. Aceptar pedidos durante un pico importa, pero recibir más de los que la cocina puede preparar empeora el problema.

![1. Identificar significa convertir necesidades en decisiones justificables ](../Recursos%20visuales/Diagramas/cap05-diagrama-01.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap05-diagrama-01.mmd)

Las preocupaciones del dominio, los requisitos y el conocimiento implícito convergen en situaciones concretas antes de justificar decisiones. El proceso es iterativo: probar una decisión puede revelar requisitos omitidos y obligar a volver atrás.

### Plantilla mínima para no saltar a una solución

Convierte cada preocupación en una cadena que pueda discutirse:

| Paso | Pregunta | Ejemplo provisional de PedidoClaro |
|---|---|---|
| Resultado | ¿Qué valor o pérdida importa? | No perder ventas de almuerzo por saturación digital. |
| Escenario | ¿Quién hace qué, cuándo y bajo qué carga? | A las 12:30 llegan solicitudes de confirmación durante una promoción. |
| Respuesta esperada | ¿Qué debe seguir ocurriendo? | Aceptar solo pedidos que un local pueda preparar y comunicar esperas. |
| Medida | ¿Cómo distinguimos éxito de fallo? | Tasa de aceptación válida, errores y p95, separados por operación. |
| Restricción | ¿Qué limita las alternativas? | Equipo y operación pequeños; capacidad física de cada cocina. |
| Decisión candidata | ¿Qué cambio estructural podría ayudar? | Control de admisión por local y aislamiento de integraciones auxiliares. |
| Evidencia | ¿Qué observación la confirmaría o refutaría? | Prueba de pico más simulación de cocina saturada y proveedor lento. |

La decisión aparece **después** del escenario y la medida. «Necesitamos microservicios porque vamos a crecer» invierte el orden: nombra una solución antes de saber qué crece, a qué ritmo, con qué límite y qué parte se satura.

> [!warning] Errores frecuentes
> - Traducir una palabra comercial a una tecnología fija: crecimiento no equivale automáticamente a distribución.
> - Confundir usuarios registrados con usuarios simultáneos o solicitudes por segundo.
> - Elegir una característica solo porque su nombre suena importante, sin demostrar influencia estructural.
> - Tratar una intuición del dominio como hecho. Lo implícito se formula como hipótesis y se valida.

> [!question]- Comprobación: «debe ser rápido» ¿ya es una característica útil?
> Señala rendimiento, pero aún no orienta ni verifica una decisión. Faltan operación, población, carga, punto de medición, umbral y período. «El p95 de confirmar pedido será inferior a 2 s durante 100 confirmaciones/s durante 15 minutos, incluyendo la persistencia» es discutible y comprobable; sus números siguen siendo acuerdos por validar.

---

**Anterior:** [Preguntas y ejercicio resuelto](../04%20Caracter%C3%ADsticas%20arquitect%C3%B3nicas/07%20Preguntas%20y%20ejercicio%20resuelto.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Traducción del negocio y características compuestas](02%20Traducci%C3%B3n%20del%20negocio%20y%20caracter%C3%ADsticas%20compuestas.md)
