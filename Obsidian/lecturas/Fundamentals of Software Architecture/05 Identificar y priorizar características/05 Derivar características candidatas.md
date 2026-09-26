---
title: "Capítulo 5 · Identificar y priorizar características · Derivar características candidatas"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 5
---

# Derivar características candidatas

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 5 de 9

**Objetivo:** Razonar sobre requisitos explícitos e implícitos.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Silicon Sandwiches combina requisitos funcionales, cifras de crecimiento y restricciones de franquicias, expansión y personal. Derivar una candidata significa explicar qué evidencia del enunciado la sugiere y qué dato falta validar.

## 5. Derivar características: explícitas, implícitas y candidatas

**Libro — PDF pp. 17–21, impresas 72–76:** «explícita» no exige que el documento use el nombre técnico. Una previsión de usuarios puede expresar escalabilidad en lenguaje comercial. «Implícita» indica que la necesidad se deduce del dominio o de condiciones generales. Una inferencia sigue necesitando validación.

### Crecimiento, picos, rapidez y continuidad

Los miles de usuarios y la posibilidad de millones señalan **escalabilidad**. Para dimensionar, hace falta distinguir usuarios registrados, activos y concurrentes: un millón de cuentas no significa un millón de pedidos simultáneos.

Las horas de comida sugieren **elasticidad**, aunque el enunciado no la solicite literalmente. El libro la presenta como capacidad de afrontar ráfagas. Como elaboración operativa, podemos evaluar además cuánto tarda en ajustarse la capacidad y cómo se reduce después. Soportar crecimiento sostenido no demuestra que el sistema responda a un pico súbito.

El **rendimiento** requiere tiempos de respuesta aceptables, especialmente en móvil y durante esos picos. Debe definirse junto con la carga: «responde en un segundo» carece de contexto si solo se probó con una persona. La **disponibilidad**, implícita, permite acceder al servicio; la estabilidad de las interacciones evita conexiones interrumpidas y sesiones que obligan a empezar de nuevo.

![Crecimiento, picos, rapidez y continuidad ](../Recursos%20visuales/Diagramas/cap05-diagrama-03.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap05-diagrama-03.mmd)

Escalabilidad, elasticidad y rendimiento imponen condiciones diferentes: crecer de forma sostenida, reaccionar a picos y mantener tiempos o trabajo útil. Esa distinción no define una topología ni demuestra que añadir servidores elimine un cuello de botella en base de datos o cocina.

### Recorrer todos los requisitos sin inflar la arquitectura

| Evidencia del enunciado | Derivación y límite razonable |
|---|---|
| Pedir y elegir recogida o reparto | Comportamiento funcional; el libro no deriva una característica especial por ese solo hecho. |
| Hora, direcciones y mapas con tráfico | Integraciones que pueden afectar fiabilidad. Preguntar si perder tráfico permite mostrar direcciones básicas, evitando una dependencia fatal. |
| Despachar al repartidor | Funcionalidad sin exigencia arquitectónica especial en el enunciado disponible. |
| Acceso móvil | Decisiones de experiencia y rendimiento. El libro considera una web optimizada por simplicidad y presupuesto, pero exige colaborar con UX y negocio: una función necesaria podría justificar aplicaciones nativas. |
| Promociones nacionales y locales | Variaciones de comportamiento que hacen candidata la personalización o *customizability*. |
| Tres modalidades de pago | El pago en línea exige seguridad; no demuestra por sí solo que haga falta una estructura extraordinaria. |
| Franquicias con propietarios distintos | Examinar viabilidad, costes, plazos y capacidades del personal. No presupone automáticamente aislamiento mediante servicios separados. |
| Expansión internacional | Internacionalización; puede abordarse mediante diseño sin una estructura especial, y afecta a UX. |
| Contratación de personal de bajo coste | El libro infiere importancia de usabilidad. La elaboración práctica es comprobar formación y facilidad de uso, sin asumir incapacidad individual. |

**Referencias:** PDF pp. 18–20, impresas 73–75. En PDF p. 21, impresa 76, el libro amplía su discusión de personalización con recetas, ofertas y direcciones locales; las recetas aparecen en el análisis, no como un requisito separado del enunciado original.

### Seguridad implícita no significa seguridad resuelta

El libro supone que un tercero podría procesar los pagos y que, en este escenario, prácticas adecuadas permitirían atender la seguridad sin una estructura especial. **Ese supuesto no garantiza la seguridad de la aplicación.** Como elaboración propia, siguen existiendo autenticación, autorización entre locales, protección de datos y validación del resultado de pago. Si esas necesidades requieren aislamiento estructural crítico, la seguridad asciende a característica conductora. Estar fuera del «top 3» nunca autoriza omitir controles básicos.

---

**Anterior:** [Kata Silicon Sandwiches](04%20Kata%20Silicon%20Sandwiches.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Personalización diseño y arquitectura](06%20Personalizaci%C3%B3n%20dise%C3%B1o%20y%20arquitectura.md)
