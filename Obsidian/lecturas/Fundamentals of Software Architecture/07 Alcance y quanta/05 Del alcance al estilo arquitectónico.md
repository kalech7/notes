---
title: "Capítulo 7 · Del alcance al estilo arquitectónico"
created: 2026-09-28
capitulo: 7
orden: 5
tags:
  - lecturas/software-architecture
  - arquitectura/quanta
---

# Del alcance al estilo arquitectónico

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Capítulo 7 · Alcance y quanta]] · Nota 5 de 7

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, segunda edición, capítulo 7. Fuente local: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Las páginas PDF se cuentan desde el archivo suministrado; la impresa aparece en el libro. «Elaboración» y «ampliación didáctica» identifican material propio.

**Objetivo:** usar conjuntos de características para orientar decisiones de estilo, límites, persistencia y comunicación sin convertir un diagrama orientativo en una receta automática.

## Leer el árbol completo

**Libro — PDF pp. 6–9, impresas 100–103; figuras 7-1 a 7-4.** La figura 7-1 presenta el recorrido general. Las figuras siguientes aíslan decisiones: familia arquitectónica, límites de quanta y persistencia. El redibujo reúne esas etapas en español y conserva cajas, cilindros y fronteras punteadas para facilitar la comparación.

![03 decision estilo](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-03-decision-estilo.png)

## Explicación de los símbolos y las flechas

Las **cajas grandes** son decisiones o resultados del análisis. Los **cilindros** representan persistencia. Los **contornos punteados** agrupan elementos en quanta candidatos. Las **flechas verticales y diagonales** señalan el orden de las decisiones; no son llamadas de red. Las letras A, B, C y D son identificadores didácticos, no servicios de una aplicación especificada por el libro.

La rama izquierda corresponde a la posibilidad de resolver el problema con una familia monolítica; la derecha abre decisiones adicionales propias de una arquitectura distribuida. Los ejemplos de agrupamiento ilustran que varios componentes o servicios pueden compartir un límite. La figura no obliga a usar exactamente tres quanta ni esas bases.

## Paso 1: analizar características y dominio

La primera pregunta es si un conjunto común de características puede satisfacer la solución. Si puede, una arquitectura monolítica es una candidata que reduce algunas decisiones posteriores. Si existen varios conjuntos diferenciados o restricciones del dominio que requieren separación, una arquitectura distribuida merece análisis.

**Matiz:** «un conjunto» significa un conjunto de prioridades compatible para ese alcance, no una sola característica. Un monolito puede necesitar seguridad, disponibilidad, rendimiento y mantenibilidad a la vez. Tampoco basta encontrar prioridades diferentes en una lista para justificar automáticamente microservicios: hay que demostrar que separarlas produce beneficios suficientes.

## Paso 2: delimitar quanta cuando se distribuye

Agrupar componentes implica preguntar qué propósito comparten y qué dependencias los atan. Separar unidades sin resolver una base compartida o un componente común puede dejar un límite más amplio del previsto. La granularidad resultante debe poder explicarse desde el dominio y desde las características, no solamente desde el tamaño del código.

El libro remite el detalle adicional de granularidad a capítulos posteriores. Esta nota cubre lo que muestran las páginas suministradas: la necesidad de decidir los límites y revisar la relación entre ellos.

## Paso 3: elegir la persistencia

En el recorrido monolítico, el capítulo considera habitual una base monolítica alineada con el desarrollo y despliegue de la aplicación. En el distribuido, presenta tanto una base compartida —menciona arquitecturas dirigidas por eventos— como datos particionados conforme a los servicios, habituales en microservicios.

La distribución de procesos no obliga por definición a distribuir todos los datos; pero compartir datos tiene consecuencias para el acoplamiento y los quanta. Si una frontera dibujada como independiente depende del mismo esquema que otra, hay que revisar lo prometido por esa frontera.

**Ampliación didáctica:** separar bases también puede trasladar complejidad a consultas, sincronización o coordinación entre dominios. No es una mejora gratuita ni un objetivo suficiente por sí solo.

## Paso 4: elegir cómo se comunican

En el caso distribuido queda decidir entre comunicación síncrona y asíncrona según los recorridos del negocio. La elección modifica la espera, el tratamiento de ráfagas y el comportamiento ante fallos. Como advierte el texto, puede obligar a revisar límites previamente propuestos.

El árbol se lee de arriba hacia abajo para aprender, pero el diseño real requiere volver atrás. Esa iteración se indica al pie del redibujo; el original también agrupa las etapas para mostrar sus alternativas. No hay garantía de acertar con una sola pasada.

## Un ejemplo de uso, con supuestos visibles

**Ejemplo propio:** una aplicación interna de veinte usuarios tiene una operación estable, cambios coordinados y el mismo objetivo de disponibilidad para todas sus funciones. Un monolito modular sería un candidato razonable por estas condiciones; la cifra y la elección son didácticas, no una regla del libro.

Si después aparece una interfaz pública con demanda muy variable y una función de valoración que cambia diariamente, se revisan los conjuntos de características. La separación podría tener sentido, pero habría que estudiar contratos, datos, costes de operación y necesidades de consistencia antes de concluir que es conveniente.

**Conclusión del gráfico:** el alcance ayuda a formular y reducir alternativas. **Límite:** no selecciona automáticamente un producto de base de datos, un proveedor, un protocolo ni una cantidad óptima de servicios. Esas decisiones necesitan requisitos y evidencia adicionales.


---

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/04 Sincronía colas y límites operacionales|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/06 Going Green explicado paso a paso|Siguiente →]]
