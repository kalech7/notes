---
title: "Capítulo 5 · Identificar y priorizar características · Personalización diseño y arquitectura"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 6
---

# Personalización diseño y arquitectura

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 6 de 9

**Objetivo:** Decidir el alcance de una variación entre locales.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> La kata hizo candidata la personalización porque locales y franquicias pueden variar. Que una capacidad sea candidata no decide su escala: puede resolverse con datos, diseño interno o una estructura extensible, según independencia y costo.

## 6. Personalización: ¿diseño o arquitectura?

**Libro — PDF p. 21, impresa 76:** un microkernel puede alojar comportamiento común en un núcleo y variaciones en extensiones. Otra arquitectura puede resolverlas con Template Method: una clase base define un flujo y las subclases redefinen pasos. La misma necesidad puede encontrar soluciones a diferente escala.

**Elaboración propia:** en PedidoClaro, cambiar únicamente un descuento por local puede necesitar datos configurables. Si cada franquicia aporta reglas ejecutables independientes, un modelo de extensiones gana atractivo. Ese beneficio implica definir contratos, compatibilidad y tratamiento de fallos. Template Method puede ser suficiente para unas pocas variantes mantenidas por el mismo equipo, aunque la herencia introduce acoplamiento y puede volver difíciles las combinaciones de reglas.

![6. Personalización: ¿diseño o arquitectura? ](../Recursos%20visuales/Diagramas/cap05-diagrama-04.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap05-diagrama-04.mmd)

Primero se identifica qué varía, quién lo cambia y con qué independencia; después se comparan mecanismos. Las tres ramas no forman un algoritmo ni una lista exhaustiva y pueden combinarse.

La fuente pide analizar rendimiento, acoplamiento, otras características y coste. Exige colaborar con desarrollo, responsables técnicos, negocio, gestión y operaciones. Evitar la **torre de marfil** significa contrastar la propuesta con quienes implementarán y operarán sus consecuencias.

### Escalera de mecanismos: elegir el menos costoso que conserve el límite

| Tipo de variación | Mecanismo candidato | Coste o riesgo principal |
|---|---|---|
| Valor distinto por local | Configuración o datos | Validación, historial y permisos de cambio. |
| Varias fórmulas pequeñas controladas por el equipo | Estrategias o funciones intercambiables | Catálogo de reglas y combinaciones crecientes. |
| Un flujo común con pasos que varían | Template Method | Acoplamiento por herencia y dificultad para combinar variantes. |
| Reglas que cambia negocio con frecuencia | Tabla o motor de reglas | Gobernanza, pruebas, explicabilidad y versiones. |
| Extensiones ejecutables independientes | Microkernel y plugins | Contratos, aislamiento, compatibilidad, seguridad y operación. |
| Equipos y ciclos de vida realmente independientes | Componentes o servicios separados | Comunicación remota, datos distribuidos y observabilidad. |

La tabla no es una progresión obligatoria. Sirve para evitar dos extremos: codificar cada diferencia con condicionales dispersos o construir una plataforma de plugins antes de demostrar que las extensiones necesitan independencia.

**Caso propio:** una franquicia cambia el porcentaje de descuento. Guardarlo como dato permite validarlo y auditarlo. Otra franquicia introduce «segundo sándwich gratis solo si ambos pertenecen a una familia y durante dos franjas horarias». Antes de crear un plugin, se comprueba si una estrategia mantenida por el mismo equipo cubre la variación. Un plugin gana justificación si terceros entregan reglas, sus versiones evolucionan aparte o un fallo debe quedar aislado; esas ventajas también exigen límites de recursos y permisos.

> [!warning] Errores frecuentes
> - Confundir «configurable» con «sin riesgo»: los datos pueden cambiar comportamiento crítico.
> - Elegir microkernel por flexibilidad futura sin actores, variaciones ni ciclo de vida concretos.
> - Usar herencia para todas las combinaciones hasta producir una jerarquía difícil de probar.
> - Permitir extensiones sin versionado, aislamiento ni estrategia ante fallos.

> [!question]- Comprobación: cinco locales usan cinco porcentajes de descuento. ¿Necesitan plugins?
> No hay evidencia suficiente. Si solo varía un valor, configuración validada es la opción inicial más simple. Plugins serían defendibles cuando varíe comportamiento ejecutable con independencia que compense contratos, compatibilidad, operación y seguridad adicionales.

---

**Anterior:** [Derivar características candidatas](05%20Derivar%20caracter%C3%ADsticas%20candidatas.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Prioridades y mínimos](07%20Prioridades%20y%20m%C3%ADnimos.md)
