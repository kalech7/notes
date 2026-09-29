---
title: "Capítulo 7 · El alcance de las características"
created: 2026-09-28
capitulo: 7
orden: 1
tags:
  - lecturas/software-architecture
  - arquitectura/quanta
---

# El alcance de las características

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Capítulo 7 · Alcance y quanta]] · Nota 1 de 7

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, segunda edición, capítulo 7. Fuente local: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Las páginas PDF se cuentan desde el archivo suministrado; la impresa aparece en el libro. «Elaboración» y «ampliación didáctica» identifican material propio.

**Objetivo:** entender por qué «el sistema debe ser escalable» es insuficiente hasta precisar qué parte, con qué dependencias y bajo qué flujo.

## La pregunta central: ¿dónde debe cumplirse una característica?

**Libro — PDF p. 1, impresa 95.** Las características arquitectónicas no tienen siempre un único alcance para toda la aplicación. En ciertos sistemas existe un conjunto de prioridades común; en otros, diferentes partes necesitan conjuntos distintos. Un servicio público puede necesitar absorber variaciones importantes de demanda mientras una función interna prioriza integridad y trazabilidad.

El alcance es el límite dentro del cual analizamos y exigimos esas propiedades. No basta con conocer el comportamiento del código aislado: una base de datos, una dependencia compartida o un servicio remoto pueden condicionar el resultado. Un código capaz de atender muchas solicitudes no convierte automáticamente en elástica a una solución si su almacenamiento se satura primero.

**Elaboración didáctica.** Pensemos en una tienda ficticia: consultar ofertas debe responder con rapidez durante una campaña, mientras cerrar el balance debe dejar un rastro auditable. Ambos procesos requieren seguridad, pero no necesariamente idéntica latencia, frecuencia de despliegue o estrategia de escalado. «Distintas prioridades» no significa «ausencia de garantías mínimas» en las otras partes.

## Por qué no bastan las métricas del código

Una métrica de cohesión o acoplamiento entre clases permite reconocer problemas dentro del código. Sin embargo, no responde por sí sola a preguntas como:

- ¿Qué elementos tienen que estar disponibles para que esta capacidad funcione?
- ¿Qué dependencia compartida puede limitar a varios servicios simultáneamente?
- ¿Qué partes se pueden desplegar y evolucionar de manera independiente?
- ¿La capacidad que medimos es una función local o un recorrido completo del usuario?

El libro introduce el **quantum arquitectónico** para trabajar a ese nivel. La idea es considerar una unidad que funcione de manera independiente, con las dependencias necesarias y un propósito funcional coherente. El plural es **quanta**. No es una analogía que implique física cuántica aplicada a software.

## Delimitar antes de prometer

Un escenario verificable requiere al menos una parte afectada, un estímulo, unas condiciones y una respuesta observable. Esta plantilla es una ampliación didáctica del planteamiento del capítulo:

| Pregunta | Ejemplo propio, no requisito del libro |
|---|---|
| ¿Qué capacidad? | Consultar el estado de un dispositivo. |
| ¿Bajo qué estímulo? | Aumento temporal de consultas. |
| ¿Con qué dependencias? | Servicio de estado y su almacenamiento. |
| ¿Qué observar? | Latencia, errores y saturación de ese recorrido. |
| ¿Qué queda fuera? | Elaboración nocturna de informes, salvo dependencia demostrada. |

El objetivo no es inventar números lo antes posible, sino evitar mezclar comportamientos distintos en una sola afirmación. Después se añaden cargas y umbrales acordados con el dominio.

## Un recorrido de razonamiento

![Del propósito al alcance verificable](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-07-proposito-alcance.png)

*Diagrama didáctico redibujado en PNG; fuente lógica editable: [c07-07-proposito-alcance.mmd](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-07-proposito-alcance.mmd).*

Cada caja representa una pregunta de análisis, no un servicio desplegado. Las flechas indican el orden del razonamiento. Se parte de una capacidad del negocio, se averigua qué necesita para operar y luego se contrasta el límite con la ejecución real. La flecha de vuelta muestra que descubrir una dependencia obliga a revisar el modelo.

**Conclusión y límite.** El quantum ayuda a precisar el alcance, pero dibujarlo no prueba que el sistema cumpla sus objetivos. La validación exige evidencia de funcionamiento y de despliegue. El diagrama es una herramienta propia de estudio; el libro desarrolla el concepto, no esta secuencia exacta.

## Comprueba que lo entendiste

**Pregunta:** si duplicamos las instancias del servicio y el rendimiento no mejora, ¿qué aspecto del alcance pudo omitirse?

**Respuesta razonada:** alguna dependencia necesaria, por ejemplo una base de datos compartida, puede seguir imponiendo el límite. También podrían intervenir bloqueos, conexiones o un servicio remoto. El capítulo enseña a ampliar la observación más allá del código; no permite diagnosticar una causa concreta sin mediciones.


---

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/02 Anatomía de un quantum|Siguiente →]]
