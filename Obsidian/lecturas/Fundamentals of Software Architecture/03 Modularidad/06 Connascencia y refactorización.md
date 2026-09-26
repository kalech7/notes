---
title: "Capítulo 3 · Modularidad · Connascencia y refactorización"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 3
orden: 6
---

# Connascencia y refactorización

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 3 · Modularidad](00%20%C3%8Dndice.md) → Nota 6 de 7

**Objetivo:** Identificar las nueve formas de connascencia.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 6. Connascencia: precisar qué debe coincidir

Dos elementos presentan connascencia cuando cambiar uno exige adaptar el otro para conservar la corrección. El libro la presenta como **vocabulario de análisis**, no como una única puntuación comparable a $C_a$ o $C_e$.

### Cinco formas estáticas

Las formas estáticas pueden identificarse principalmente examinando código y contratos. Los siguientes ejemplos de PedidoClaro son propios.

| Forma | Acuerdo necesario | Ejemplo y consecuencia |
|---|---|---|
| Nombre | Identificador de una entidad | Renombrar `confirmarPedido` exige actualizar referencias. Un refactor automático ayuda dentro del código accesible; no actualiza por sí solo clientes externos. |
| Tipo | Tipo o estructura esperada | Cambiar `Importe` por una cadena exige adaptar operaciones y consumidores. En lenguajes dinámicos también existen expectativas de estructura. |
| Significado o convención | Interpretación de valores | Si `2` significa «confirmado», todos deben interpretarlo igual. Un nombre explícito reduce interpretaciones dispersas. |
| Posición | Orden de los valores | `entregar(origen, destino)` puede aceptar dos cadenas intercambiadas sin error de tipos y enviar el pedido a otro sitio. |
| Algoritmo | Procedimiento de cálculo | Caja y facturación deben aplicar la misma regla de redondeo si ambas calculan el importe exigible. |

Para el último caso, supongamos un importe decimal exacto de **2,345** y redondeo a dos decimales. Redondear los empates hacia arriba produce **2,35**; redondear al dígito par produce **2,34**. Ambos sistemas pueden parecer razonables y discrepar por un centavo. La solución requiere acordar la regla, su momento de aplicación y su versión; una función compartida o un único propietario del cálculo puede reducir duplicación. Este ejemplo presupone representación decimal exacta.

### Cuatro formas dinámicas

Las formas dinámicas dependen de cómo interactúan los elementos durante la ejecución.

| Forma | Acuerdo necesario | Ejemplo y consecuencia |
|---|---|---|
| Ejecución | Orden de operaciones | Confirmar antes de fijar las líneas deja un pedido incompleto. Un constructor validado puede impedir crear ese estado. |
| Timing o temporización | Momento, duración o concurrencia | Dos cajas leen que queda un pan y ambas lo reservan; el resultado depende de la intercalación de operaciones. |
| Valores | Relación entre varios valores | `total = subtotal - descuento` debe conservarse al modificar cantidades. Almacenar los tres sin control permite contradicciones. |
| Identidad | Referencia a la misma entidad | Cocina y caja deben actualizar el mismo pedido persistido; dos registros con atributos iguales no son necesariamente la misma entidad. |

La diferencia entre ejecución y timing importa: la primera exige un orden lógico; la segunda depende de la coordinación temporal. Introducir una espera fija no garantiza que el otro participante haya terminado. Para inventario, una operación atómica de reserva con comprobación del stock puede proteger la invariante en su frontera transaccional.

La connascencia de valores tampoco impone por sí sola una transacción distribuida. **Aclaración propia:** hay que determinar si la relación debe cumplirse inmediatamente o admite convergencia posterior, y diseñar el protocolo correspondiente. El requisito de negocio decide qué estados intermedios son aceptables.

### Fuerza, localidad y grado

La **fuerza** expresa cuánto cuesta reconocer y modificar el acuerdo: un nombre referenciado suele ser más fácil de cambiar que una carrera entre procesos. La **localidad** indica cuán próximos están los participantes; una regla dentro de un módulo es más fácil de coordinar que entre equipos y despliegues independientes. El **grado** considera cuántos participantes están involucrados: cambiar un acuerdo en dos lugares difiere de hacerlo en cuarenta.

![Fuerza, localidad y grado ](../Recursos%20visuales/Diagramas/cap03-diagrama-04.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap03-diagrama-04.mmd)

**Interpretación:** los refactors hacen explícito el acuerdo o concentran su mantenimiento. **Límite:** no eliminan todas las dependencias. Una constante conserva semántica compartida; un objeto necesita contrato; una operación solo protege los datos bajo su control.

El libro recomienda debilitar acuerdos difíciles y mantener los más fuertes cerca. No conviene transformar su tipología en una clasificación universal: cambiar un nombre público usado por miles de clientes puede ser más costoso que ajustar un algoritmo privado en dos funciones vecinas.

La recomendación de concentrar connascencia dentro de fronteras debe leerse como **encapsular relaciones necesarias**, no crear dependencias gratuitas. También hay una ambigüedad terminológica: la «Rule of Degree» citada en la página impresa 53 habla de convertir formas fuertes en débiles, aunque la propiedad *grado* se había definido por cantidad de participantes. Mantener separadas ambas ideas evita confundir fuerza y alcance.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=13|PDF pp. 13–17; impresas pp. 49–53]].

---

**Anterior:** [Abstracción inestabilidad y distancia](05%20Abstracci%C3%B3n%20inestabilidad%20y%20distancia.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Preguntas y ejercicio resuelto](07%20Preguntas%20y%20ejercicio%20resuelto.md)
