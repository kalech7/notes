---
title: "Capítulo 5 · Identificar y priorizar características · Hoja de trabajo PedidoClaro"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 8
---

# Hoja de trabajo PedidoClaro

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 8 de 9

**Objetivo:** Relacionar necesidades, escenarios, decisiones y evidencia.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> La priorización separa conductoras, mínimos no negociables y candidatas consideradas. Una hoja útil conserva además el escenario, la evidencia pendiente, el costo aceptado y la condición que reabrirá la decisión.

## 8. Hoja de trabajo completa: PedidoClaro

**Elaboración propia; todos los objetivos numéricos siguientes son inventados.** Esta hoja adapta el método, no reproduce la figura 5-3 literalmente.

| Campo | Acuerdo provisional |
|---|---|
| Sistema y alcance | PedidoClaro: catálogo, aceptación de pedidos y confirmación para una red de locales. |
| Equipo participante | Representante comercial, responsable de local, desarrollo, UX y operaciones. |
| Resultado buscado | Aceptar pedidos de almuerzo que los locales puedan atender. |
| Escenario de carga | 200 sesiones activas normalmente; 2.000 durante veinte minutos. El modelo de solicitudes se medirá por separado. |
| Restricción | Equipo de cuatro desarrolladores; preferencia por operación sencilla. |
| Evidencia pendiente | Historial horario, capacidad de cocina, presupuesto operativo y comportamiento de proveedores. |

### Lista corta y selección conjunta

| ¿Top 3? | Conductora candidata | Objetivo provisional y evidencia para revisarlo |
|---|---|---|
| Sí | Disponibilidad | 99,9 % de solicitudes válidas de creación aceptadas técnicamente durante horario comercial; acordar exclusiones y medir extremo a extremo. |
| Sí | Elasticidad | Soportar el paso de 200 a 2.000 sesiones en cinco minutos manteniendo los límites acordados de errores y latencia. |
| Sí | Simplicidad operativa | Desplegar y revertir mediante procedimientos que dos integrantes diferentes puedan ejecutar en una prueba de quince minutos. |
| No | Escalabilidad | Validar 4.000 sesiones con capacidad adicional y revisar coste, saturación y latencia. |
| No | Rendimiento | Percentil 95 de creación de pedido inferior a dos segundos con 2.000 sesiones y mezcla documentada de solicitudes. |
| No | Recuperabilidad | Recuperar aceptación de pedidos en diez minutos en un simulacro y reconciliar todos los pedidos ya confirmados. |
| No | Personalización | Probar si promociones locales necesitan estructura especial; si bastan configuración y diseño, retirar esta conductora. |

«No» significa fuera del conjunto principal, no descartada. Los objetivos siguen abiertos a negociación. Disponibilidad mide aquí solicitudes; no debe convertirse sin más en minutos de caída. Asimismo, sesiones no determinan por sí solas la carga: la prueba debe documentar acciones, pausas, volumen de datos y dependencias.

| Zona de la hoja | Contenido y acción |
|---|---|
| Implícitas como mínimo | Seguridad, integridad de pedidos y modularidad. Desarrollo define controles; operaciones y negocio revisan riesgos y resultados. |
| Otras consideradas | Internacionalización: pospuesta por ausencia de expansión confirmada. Extensibilidad por plugins: pospuesta hasta demostrar variaciones que la necesiten. |
| Compensación aceptada | Ante fallo de tráfico, ofrecer direcciones básicas; conservar capacidad de pedir. Confirmar el comportamiento con UX. |
| Alternativas a contrastar | Aplicación modular con configuración; microkernel si aparecen extensiones independientes justificadas. |
| Validación próxima | Prueba de carga, simulacro de dependencia caída y comparación del coste operativo. |
| Reapertura | Revisar ante expansión, incumplimiento medido o nuevas reglas por franquicia. Responsable: equipo técnico y representante comercial. |

La simplicidad puede favorecer capacidad preparada antes del almuerzo; la elasticidad exige comprobar si basta. La hoja permite discutir esa tensión.

---

**Anterior:** [Prioridades y mínimos](07%20Prioridades%20y%20m%C3%ADnimos.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Preguntas y ejercicio resuelto](09%20Preguntas%20y%20ejercicio%20resuelto.md)
