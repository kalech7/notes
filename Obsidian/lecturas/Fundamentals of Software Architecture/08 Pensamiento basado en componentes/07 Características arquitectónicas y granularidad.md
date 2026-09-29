---
title: "08 · Características arquitectónicas: cuándo cambia el tamaño del componente"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/componentes
capitulo: 8
---

# Características arquitectónicas: cuándo cambia el tamaño del componente

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 26–27 y 33–34 · impresas 120–121 y 127–128** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Síntesis explicada del capítulo 8; los ejemplos, preguntas, tablas y diagramas adicionales se señalan como elaboración didáctica. Las recreaciones de figuras conservan la idea y las relaciones pertinentes, con rótulos en español; no son facsímiles.

## La coherencia funcional no es el único criterio

Dos actividades pueden parecer la misma función y necesitar comportamientos operativos diferentes. Capturar una puja del postor y capturar una puja presencial registrada por el subastador son funciones parecidas; sin embargo, una atiende potencialmente a miles de usuarios y la otra sostiene un puesto crítico para la continuidad de la subasta.

El capítulo explica que escalabilidad, elasticidad, fiabilidad, disponibilidad, tolerancia a fallos y agilidad pueden influir en el tamaño del componente. Por ello, después de revisar historias y roles, hay que comprobar las características arquitectónicas prioritarias.

## Mecanismo de la decisión

![c08-12-decision-granularidad](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-12-decision-granularidad.png)

La primera caja es un componente candidato; la pregunta central representa una decisión basada en evidencia; las salidas son alternativas, no etapas que siempre deben ejecutarse. Las flechas siguen el razonamiento del arquitecto: no se divide primero para buscar razones después, sino que se comparan necesidades, se elige una opción y se valida. El límite de un componente debe responder a un problema, y el diagrama no ofrece una fórmula universal ni umbrales de carga.

## Comparar perfiles de necesidad

| Dimensión | Pregunta concreta | Cómo podría influir |
|---|---|---|
| Escalabilidad | ¿Qué parte recibe crecimiento sostenido de usuarios o datos? | Evitar que una función de baja demanda dicte el tamaño de toda la unidad |
| Elasticidad | ¿Qué parte recibe picos rápidos? | Preparar límites que permitan responder al pico |
| Disponibilidad | ¿Qué función debe seguir accesible ante fallos de otra? | Identificar fronteras y requisitos de aislamiento |
| Fiabilidad | ¿Qué operación debe completarse correctamente de forma consistente? | Separar rutas críticas o reglas especialmente sensibles |
| Agilidad | ¿Qué conjunto de reglas cambia con frecuencia? | Hacer más local el cambio y sus pruebas |

Las preguntas son herramientas didácticas. Dividir el código puede facilitar ciertos objetivos, pero **no los garantiza**. Dos componentes dentro del mismo proceso pueden seguir compartiendo memoria, hilos, almacenamiento y destino de despliegue. Para aislamiento operativo real habrá que revisar también la arquitectura física.

## Ejemplo de dos entradas de usuario

Supongamos, como ejercicio, que un portal público recibe grandes picos y un panel administrativo solo lo usan cinco personas. Ambos permiten «enviar solicitudes». Si se agrupan sin analizar diferencias, una saturación del público podría comprometer el trabajo interno.

Una separación lógica entre Capturar solicitud pública y Capturar solicitud administrativa permite expresar contratos y prioridades diferentes. Después se evaluará si basta con límites de recursos internos o si hace falta separación física. La mera creación de dos carpetas no evita el fallo compartido.

## Cuándo fusionar en vez de dividir

El proceso también permite combinar componentes. Si dos piezas cambian siempre juntas, requieren abundante intercambio de detalles y no presentan necesidades diferentes, separarlas puede aumentar el coste sin aportar autonomía. Revisa si sus reglas forman una responsabilidad única o si simplemente falta mejorar el contrato.

Una decisión defendible registra: problema observado, alternativas, beneficio esperado, coste añadido y evidencia con la que se evaluará. Esto evita justificar cualquier separación con la frase genérica «será más escalable».

## Ejercicio resuelto

**Propuesta:** separar Captura pública y Captura administrativa porque el público tendrá mucha demanda.

**Lo que sí justifica:** revisar límites de responsabilidad y recursos ante perfiles distintos. **Lo que falta:** estimación de carga, prioridad de cada entrada, comportamiento bajo saturación, dependencias compartidas y forma de verificarlo. **Qué mediríamos en un prototipo:** si la ruta administrativa mantiene su objetivo de respuesta mientras la ruta pública soporta un pico. Los objetivos numéricos se deben definir con el contexto; el capítulo no aporta un umbral universal.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/06 Historias cohesión y distribución de responsabilidades|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/08 Acoplamiento aferente eferente y temporal|Siguiente →]]
