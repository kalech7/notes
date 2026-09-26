---
title: "Capítulo 4 · Características arquitectónicas · Familias ISO y terminología"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 4
orden: 3
---

# Familias ISO y terminología

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 4 · Características arquitectónicas](00%20%C3%8Dndice.md) → Nota 3 de 7

**Objetivo:** Interpretar la clasificación que presenta el libro.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 3. Las familias ISO tal como aparecen en el libro

Los autores presentan una selección de definiciones ISO **reformuladas por ellos**. Esta sección reproduce esa organización conceptual; **no afirma cuál es la versión vigente de una norma ni su conformidad literal**. **Fuente: PDF pp. 8–10; impresas 62–64.**

| Familia presentada | Subcaracterísticas y lectura práctica |
|---|---|
| Eficiencia del rendimiento | Comportamiento temporal, utilización de recursos y capacidad. No basta responder rápido: importa con qué recursos y bajo qué límites. |
| Compatibilidad | Coexistencia e interoperabilidad. Compartir un entorno sin interferencia excesiva es distinto de intercambiar información utilizable. |
| Usabilidad | Reconocimiento de adecuación, facilidad de aprendizaje, protección frente a errores del usuario y accesibilidad. Comprender que una pantalla sirve para cancelar no significa poder operarla fácilmente. |
| Fiabilidad | Madurez, disponibilidad, tolerancia a fallos y recuperabilidad. Agrupa operación normal, acceso, continuidad ante fallos y restauración. |
| Seguridad | Confidencialidad, integridad, no repudio, responsabilidad trazable (*accountability*) y autenticidad. Identificar al actor y conservar evidencia de acciones resuelven necesidades diferentes. |
| Mantenibilidad | Modularidad, reutilización, analizabilidad, modificabilidad y testabilidad. Entender un fallo, modificarlo y comprobar la corrección son capacidades complementarias. |
| Portabilidad | Adaptabilidad, instalabilidad y reemplazabilidad. Cambiar entorno y sustituir una pieza no son la misma operación. |
| Adecuación funcional | Completitud, corrección y pertinencia funcional. Cubrir tareas, producir resultados correctos y facilitar objetivos son dimensiones diferentes. |

Los autores **excluyen la adecuación funcional** de su catálogo porque describe motivaciones y funciones del dominio. No significa que la corrección importe menos: «cobrar el importe correcto» es indispensable, aunque pertenezca a otra categoría de su marco.

En la discusión previa, el libro diferencia interoperabilidad como facilidad de integración y compatibilidad como atención a estándares. Después, la clasificación ISO presentada incluye interoperabilidad dentro de compatibilidad. No conviene fundir ambas organizaciones como si fueran idénticas: muestran por qué hace falta declarar el vocabulario utilizado.

---

**Anterior:** [Catálogo de características](02%20Cat%C3%A1logo%20de%20caracter%C3%ADsticas.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Rendimiento escalabilidad y elasticidad](04%20Rendimiento%20escalabilidad%20y%20elasticidad.md)
