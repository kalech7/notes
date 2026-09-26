---
title: "Capítulo 5 · Identificar y priorizar características · Prioridades y mínimos"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 7
---

# Prioridades y mínimos

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 7 de 9

**Objetivo:** Elegir pocas conductoras sin olvidar los mínimos.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Derivar candidatas amplía el espacio de discusión; no todas necesitan tratamiento estructural especial. Cada capacidad optimizada añade costo y puede entrar en tensión con simplicidad, rendimiento, seguridad u operación.

## 7. Priorizar: pocas conductoras y mínimos explícitos

**Libro — PDF pp. 22–24, impresas 77–79:** cada característica añade obligaciones y puede complicar la solución. Una prueba útil es preguntar cuál eliminaríamos primero. En Silicon Sandwiches podría dejarse la personalización al diseño; también podría reducirse la prioridad relativa del rendimiento frente a disponibilidad o escala. Eso no significa construir deliberadamente una aplicación lenta.

La hoja del libro tiene **siete espacios**, pero los autores aclaran que seis u ocho también servirían. Es una restricción práctica para conversar, no una ley científica ni un máximo universal. Las características implícitas se mantienen visibles; si necesitan atención estructural especial, pasan a la lista conductora. Una candidata desplazada se registra en **«Otras consideradas»**.

Finalmente se eligen **tres conductoras principales sin orden interno**. No se exige acordar un ranking completo: negociar cada posición consume tiempo y puede crear una precisión ficticia. El conjunto principal orienta las compensaciones sin borrar las demás condiciones.

El recuadro del Vasa, PDF p. 23, impresa 78, sirve aquí únicamente como **analogía de sobredimensionar y acumular objetivos incompatibles**. No utilizamos su narración como explicación histórica verificada del naufragio.

### Separar tres listas evita dos errores opuestos

| Lista | Pregunta | Consecuencia |
|---|---|---|
| Conductoras | ¿Cuáles cambian de verdad la estructura o dominan sus compensaciones? | Reciben inversión y evidencia explícita en las decisiones principales. |
| Mínimos no negociables | ¿Qué debe cumplirse aunque no diferencie la estructura? | Se conserva como condición y se verifica; no desaparece por quedar fuera del top 3. |
| Consideradas | ¿Qué podría importar si cambian hechos o alcance? | Se registra con la condición que haría reabrirla. |

**Ejemplo propio:** para una tienda pequeña, seguridad básica es un mínimo; elasticidad puede ser conductora por campañas; internacionalización queda considerada hasta existir una fecha de expansión. Si un requisito de aislamiento de datos obliga a separar responsabilidades o despliegues, seguridad deja de ser solo mínimo y pasa a conducir estructura.

### Un procedimiento de priorización defendible

1. Formula escenarios antes de votar palabras.
2. Elimina duplicados y descompón características compuestas.
3. Pregunta qué decisión estructural cambiaría cada candidata.
4. Explicita el costo de optimizarla y con qué otra candidata entra en tensión.
5. Obliga a quitar una: si nada puede desplazarse, aún no existe prioridad.
6. Conserva mínimos y «otras consideradas» con disparadores de revisión.
7. Elige tres conductoras como conjunto; no inventes diferencias de ranking que nadie puede justificar.

> [!warning] Errores frecuentes
> - Convertir la lista en concurso de importancia moral: «seguridad importa» no demuestra que conduzca esta estructura.
> - Puntuar de 1 a 10 sin explicar escenario, evidencia ni costo; los decimales no crean conocimiento.
> - Borrar lo que queda fuera del top 3 en lugar de conservar mínimos.
> - Elegir sin participantes de negocio y operación, que conocen pérdidas y restricciones diferentes.

> [!question]- Comprobación: disponibilidad queda cuarta. ¿Debe dejar de medirse?
> No. Si es un mínimo necesario, conserva un objetivo y pruebas. El top 3 señala dónde las compensaciones estructurales necesitan énfasis; no concede permiso para incumplir el resto. Si el objetivo de disponibilidad exige redundancia o aislamiento que cambia la estructura, hay que revisar la priorización.

---

**Anterior:** [Personalización diseño y arquitectura](06%20Personalizaci%C3%B3n%20dise%C3%B1o%20y%20arquitectura.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Hoja de trabajo PedidoClaro](08%20Hoja%20de%20trabajo%20PedidoClaro.md)
