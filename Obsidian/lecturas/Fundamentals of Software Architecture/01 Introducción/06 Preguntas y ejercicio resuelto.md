---
title: "Capítulo 1 · Introducción · Preguntas y ejercicio resuelto"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 1
orden: 6
---

# Preguntas y ejercicio resuelto

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 1 · Introducción](00%20%C3%8Dndice.md) → Nota 6 de 6

**Objetivo:** Aplicar el capítulo al almuerzo de PedidoClaro.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 6. Preguntas de comprensión

### 1. ¿Por qué un diagrama de servicios no describe toda la arquitectura?

> [!success]- Solución
> Puede mostrar estructura, pero omitir condiciones de éxito, responsabilidades precisas y razones de las restricciones. Sin ellas no sabemos si esa organización responde al problema ni qué se perdería al cambiarla.

### 2. ¿Tener cuatro componentes lógicos exige cuatro despliegues?

> [!success]- Solución
> No. La separación de responsabilidades puede existir dentro de un único despliegue. Distribuir añade decisiones sobre comunicación y operación que necesitan una justificación propia.

### 3. ¿Qué falta si la caché reduce el tiempo medio de 80 a 13 ms?

> [!success]- Solución
> Evaluar vigencia de datos, fallos, mantenimiento y la operación completa. El promedio calculado solo corresponde al acceso modelado y depende del porcentaje de aciertos supuesto; no garantiza el tiempo de confirmación de pedidos.

### 4. ¿Un estándar elimina futuros análisis de compensaciones?

> [!success]- Solución
> No. Reduce trabajo repetido cuando siguen siendo válidos sus supuestos. El segundo corolario exige reevaluar el equilibrio al cambiar el contexto; aplicar el estándar requiere reconocer su ámbito de validez.

### 5. ¿Por qué incumplir una regla puede afectar una característica?

> [!success]- Solución
> La regla puede proteger una dependencia o frontera necesaria. Si la interfaz consulta tablas directamente, un cambio de esquema puede propagarse hasta ella. Detectar el incumplimiento exige conocer también la razón de la regla.

### 6. ¿Qué distingue liderazgo de imponer una decisión?

> [!success]- Solución
> Liderar incluye explicar razones, escuchar costos y facilitar la implementación. La autoridad puede imponer una restricción, pero no sustituye acuerdos, capacidades ni recursos para cumplirla.

### 7. ¿La tercera ley recomienda elegir siempre un término medio?

> [!success]- Solución
> No. Recomienda reconocer opciones graduadas. Los extremos pueden ser apropiados; una mezcla puede añadir complejidad. Hay que evaluar cada posición según objetivos y restricciones.

## 7. Ejercicio aplicado: el almuerzo de PedidoClaro

**Supuestos inventados:** el equipo tiene cuatro desarrolladores; caja y web comparten pedidos; el objetivo es confirmar el 95 % en menos de dos segundos a veinte solicitudes por segundo. Cocina solicita que ningún pedido pagado desaparezca de su lista. Finanzas consulta tablas directamente y teme perder sus informes.

Redacta una propuesta de una página: identifica las cuatro dimensiones, formula una decisión y su principio, explica dos compensaciones, plantea una verificación y propone cómo negociar con Finanzas. No es necesario escoger productos concretos. Señala cualquier dato adicional que necesites antes de comprometer una garantía.

> [!success]- Orientación de solución
> **Características:** rendimiento bajo la carga indicada y conservación de pedidos pagados, cuyo alcance debe aclararse ante fallos. **Componentes:** Pedidos, Cobros, Cocina e Informes. **Estilo candidato:** una aplicación organizada por módulos, pendiente de validación. **Decisión:** interfaces e informes usarán contratos definidos, sin consultas directas a tablas operativas. **Principio:** limitar la propagación de cambios internos.
>
> Las compensaciones incluyen el trabajo de construir contratos y la posible concentración de dependencias. Verificaríamos el objetivo temporal con carga representativa y comprobaríamos recuperación de pedidos ante interrupciones definidas. Negociaríamos con Finanzas un contrato de informes y una transición con responsables. Faltan datos sobre fallos tolerados, duración del pico y significado exacto de «confirmado». Ninguna cifra de carga permite deducir por sí sola cuántos servidores hacen falta.

---

**Anterior:** [Principios decisiones y ADR](05%20Principios%20decisiones%20y%20ADR.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Arquitectura y diseño](../02%20Pensamiento%20arquitect%C3%B3nico/01%20Arquitectura%20y%20dise%C3%B1o.md)
