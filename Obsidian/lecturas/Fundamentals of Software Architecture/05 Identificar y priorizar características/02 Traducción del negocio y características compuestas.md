---
title: "Capítulo 5 · Identificar y priorizar características · Traducción del negocio y características compuestas"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 5
orden: 2
---

# Traducción del negocio y características compuestas

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 5 · Identificar y priorizar características](00%20%C3%8Dndice.md) → Nota 2 de 9

**Objetivo:** Evitar equivalencias automáticas entre negocio y tecnología.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> Las candidatas surgen de preocupaciones del dominio, requisitos explícitos y conocimiento implícito. Una frase comercial no se convierte directamente en una característica: primero debe revelar un resultado, un obstáculo y una forma de observar éxito.

## 2. Traducir preocupaciones sin convertirlas en equivalencias

**Libro — PDF pp. 12–13, impresas 67–68:** negocio y arquitectura suelen emplear vocabularios diferentes. La tabla 5-1 propone estas correspondencias, traducidas aquí:

| Preocupación del negocio | Características relacionadas en el libro |
|---|---|
| Fusiones y adquisiciones | Interoperabilidad, escalabilidad, adaptabilidad, extensibilidad |
| Tiempo de salida al mercado | Agilidad, capacidad de prueba, capacidad de despliegue |
| Satisfacción del usuario | Rendimiento, disponibilidad, tolerancia a fallos, capacidad de prueba y despliegue, agilidad, seguridad |
| Ventaja competitiva | Agilidad, capacidad de prueba y despliegue, escalabilidad, disponibilidad, tolerancia a fallos |
| Tiempo y presupuesto | Simplicidad, viabilidad |

La tabla abre conversaciones; no prescribe paquetes obligatorios. Adquirir otra empresa puede exigir integrar pedidos inmediatamente o sustituir su sistema en dos años: situaciones distintas. Una interfaz confusa también puede explicar insatisfacción aunque el servidor responda rápidamente.

**Elaboración propia:** tres preguntas ayudan a traducir: «¿qué resultado quieren conseguir?», «¿qué lo impediría?» y «¿cómo reconoceremos que lo conseguimos?». Si PedidoClaro necesita publicar promociones sin esperar una semana, primero hay que averiguar dónde transcurre esa semana: desarrollo, pruebas, aprobación comercial o despliegue. Separar servicios no arreglará automáticamente una aprobación manual que tarda seis días.

### Características compuestas: una promesa depende de varias condiciones

**Libro — PDF pp. 13–14, impresas 68–69:** la agilidad es una característica compuesta. No tiene una única medida objetiva; reúne, entre otras cosas, modularidad, capacidad de prueba y capacidad de despliegue. Optimizar solo un componente deja intactos los demás obstáculos.

El ejemplo del libro es calcular a tiempo los precios de fondos al cierre de la jornada por exigencias regulatorias. La cadena causal completa importa:

- **Rendimiento:** cada cálculo y el procesamiento conjunto deben caber en la ventana disponible.
- **Disponibilidad:** el sistema debe estar accesible cuando empieza esa ventana; una máquina rapidísima apagada no procesa fondos.
- **Escalabilidad:** al incorporarse más fondos, el tiempo total no debe crecer hasta incumplir el cierre.
- **Fiabilidad:** el procesamiento necesita continuar sin fallar durante su ejecución.
- **Recuperabilidad:** si falla cuando lleva el 85 %, debe poder retomar el trabajo aprovechable.
- **Auditabilidad:** debe existir evidencia que permita examinar los resultados y su cálculo. La puntualidad carece de valor si los precios son incorrectos.

La fuente vincula la última preocupación con auditabilidad. **Precisión de esta guía:** auditar ayuda a detectar y explicar errores; no garantiza por sí solo que una fórmula sea correcta. También hacen falta reglas de cálculo correctas y comprobación de resultados.

**Ejemplo numérico propio:** una ejecución tarda 50 minutos y dispone de una hora. Un fallo al 85 % ocurre a los 42,5 minutos. Reiniciar desde cero, incluso con recuperación instantánea del servicio, termina a los 92,5 minutos. Si hay puntos de recuperación válidos y restaurar tarda 3 minutos, retomar exactamente el trabajo pendiente permitiría terminar en 53 minutos. Supone que el resultado parcial es consistente, que no hay tareas que repetir y que el fallo no reaparece. Si el volumen se duplica y el coste es lineal, también hará falta aumentar capacidad o reducir trabajo: los puntos de recuperación no resuelven la escalabilidad.

![Características compuestas: una promesa depende de varias condiciones ](../Recursos%20visuales/Diagramas/cap05-diagrama-02.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap05-diagrama-02.mmd)

El objetivo comercial depende de varias condiciones conjuntas; ninguna rama garantiza el resultado por sí sola. Las ramas tampoco son independientes ni cuantifican probabilidades, y aún faltan datos de entrada, dependencias externas y validación del cálculo.

---

**Anterior:** [De necesidades a decisiones](01%20De%20necesidades%20a%20decisiones.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Requisitos implícitos y promedios](03%20Requisitos%20impl%C3%ADcitos%20y%20promedios.md)
