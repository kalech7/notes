---
title: "Capítulo 2 · Pensamiento arquitectónico · Negocio y agilidad"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 2
orden: 6
---

# Negocio y agilidad

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 2 · Pensamiento arquitectónico](00%20%C3%8Dndice.md) → Nota 6 de 8

**Objetivo:** Traducir objetivos de negocio en capacidades.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Una alternativa solo puede juzgarse contra un resultado y sus costos. Los contratos y topologías técnicas del ejemplo anterior no tienen valor por sí mismos: deben proteger algo que el negocio reconoce.

## 6. Traducir negocio y entender la agilidad compuesta

El libro exige comprender los objetivos comerciales y convertirlos en características arquitectónicas. Las conversaciones con responsables del negocio son parte del trabajo técnico porque revelan qué resultados justifican los costos. **Fuente: PDF p. 29; impresa p. 33.**

«Queremos crecer» es insuficiente. Para PedidoClaro debemos distinguir más tiendas, más pedidos simultáneos o más cambios de menú. Cada crecimiento impone problemas diferentes. **Supuestos didácticos:** aceptar 120 pedidos por segundo durante una promoción plantea capacidad; confirmar el 95 % en menos de dos segundos plantea latencia; incorporar promociones semanalmente plantea facilidad para cambiar, probar y desplegar.

La **agilidad compuesta —composite agility—** se desarrolla aquí como ampliación propia: cambiar rápido depende de varias capacidades que deben funcionar juntas. Escribir código deprisa aporta poco si las pruebas tardan días o cada publicación exige coordinar todos los servicios.

![6. Traducir negocio y entender la agilidad compuesta ](../Recursos%20visuales/Diagramas/cap02-diagrama-04.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap02-diagrama-04.mmd)

La agilidad emerge del recorrido completo y queda limitada por su espera dominante. No es una ecuación universal: el proceso real contiene trabajo paralelo, retroalimentación y esperas.

En un modelo secuencial, desarrollar una promoción tarda un día, probarla tres y esperar su despliegue cinco: nueve días. Reducir programación a medio día solo ahorra medio día. Reducir pruebas a uno y espera a uno deja un recorrido de tres días, aun conservando el día de programación. La arquitectura ayuda cuando limita el impacto del cambio y facilita pruebas y despliegues; la organización también determina las esperas.

---

**Anterior:** [Compensaciones colas y contratos](05%20Compensaciones%20colas%20y%20contratos.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Programar sin ser cuello de botella](07%20Programar%20sin%20ser%20cuello%20de%20botella.md)
