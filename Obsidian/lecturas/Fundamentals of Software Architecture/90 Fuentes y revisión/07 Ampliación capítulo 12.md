---
title: "Ampliación y cobertura · capítulo 12"
created: 2026-09-29
capitulo: 12
tags:
  - lecturas/software-architecture
  - arquitectura/pipeline
  - fuentes
---

# Fuentes y cobertura del capítulo 12

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]]

Esta ampliación cubre el escaneo completo de «Pipeline Architecture Style». Se crearon nueve notas temáticas y un índice, con explicaciones propias en español, ejemplos, preguntas resueltas y un laboratorio. El contenido del PDF se trató como fuente de estudio, sin interpretar sus ejemplos o instrucciones como órdenes para ejecutar servicios.

## Archivo y numeración

| Original | Copia preservada | Páginas PDF | Impresas |
|---|---|---:|---|
| CamScanner 2026-09-29 18.49.pdf | [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/09 Arquitectura pipeline.pdf\|09 Arquitectura pipeline]] | 12 | 181–192 |

**Impresa = PDF + 180.** La página inicial no muestra el 181, que se infiere de la secuencia; las restantes muestran 182–192. No se detectaron huecos en este capítulo. Las páginas PDF 4–11 se giraron para su revisión visual, sin modificar el archivo original ni la copia conservada. El PDF carece de texto del libro extraíble: solo aparece la marca CamScanner. Se renderizaron y leyeron las doce páginas; el OCR se utilizó como apoyo, no como sustituto de la revisión.

La colección reúne **nueve PDF y 183 páginas de PDF**. Esto amplía el alcance hasta el capítulo 12, sin eliminar los huecos históricos documentados en las fuentes iniciales.

## Mapa de cobertura

| Fuente | Contenido | Notas |
|---|---|---|
| PDF 1–2 · impresas 181–182 | Introducción, forma habitual, topología, figura 12-1 y variantes de despliegue | 01 |
| PDF 2–3 · impresas 182–183 | Filtros, cuatro roles, composición y ejemplo de palabras frecuentes | 02 |
| PDF 3 y 6 · impresas 183 y 186 | Canales, formatos, sincronía y contratos | 03 y 05 |
| PDF 4–5 · impresas 184–185 | Topologías de datos, función de aptitud, figura 12-2, nube y definición Step Functions | 04 |
| PDF 5–6 · impresas 185–186 | Responsabilidades excesivas, bidireccionalidad, errores y contratos | 05 |
| PDF 6–8 · impresas 186–188 | Gobierno, Java/C#, roles y puntos de entrada | 06 |
| PDF 8–9 · impresas 188–189 | Los cuatro tipos de equipo | 07 |
| PDF 9–11 · impresas 189–191 | Figura 12-3, fortalezas, costos y criterios de uso; EDI/ETL | 07 |
| PDF 11–12 · impresas 191–192 | Figura 12-4, telemetría, duración, uptime, MongoDB y extensión | 08 |
| Integración propia | Diseño, contratos, capacidad, recuperación y repaso | 09 |

Entrada: [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/00 Índice|Capítulo 12 · Pipeline]].

## Precisiones de la fuente

**Tester y reduce.** El libro compara el tester con `reduce`, pero sus ejemplos son selección/enrutamiento. Una reducción acumula elementos en un resultado; no es sinónimo de descartar según una condición. Se explica la distinción con la [definición oficial de Python](https://docs.python.org/3/library/functools.html#functools.reduce).

**Step Functions.** La distinción de Standard y Express se matiza según sus variantes y los reintentos explícitos. La nota 04 cita [las garantías oficiales de AWS](https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html), consultadas el 29 de septiembre de 2026, y distingue la coordinación de los efectos en almacenes externos. El escaneo aporta una definición ilustrativa, con ARN de ejemplo, que no se ejecutó ni se presentó como configuración lista para producción.

**C#.** La definición impresa del atributo no muestra un constructor para recibir el argumento empleado en su uso posterior; la variante didáctica de la nota 06 incluye ese constructor, siguiendo la [definición de atributos personalizados de Microsoft](https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/reflection-and-attributes/creating-custom-attributes). En Java se califica el enum anidado para que se entienda su ubicación. Las etiquetas describen intención y no prueban automáticamente comportamiento.

**Nombre del selector.** El texto dice «Time Series Selector» y el rótulo de la figura 12-2 parece «Time Series Sector». Se usa «selector de series temporales» siguiendo la descripción funcional.

**Quantum y características.** La figura 12-3 valora la forma monolítica habitual; la afirmación de un quantum no se aplica sin análisis a la variante distribuida admitida antes. La estrella baja de escalabilidad no significa imposibilidad absoluta de replicar un monolito. La fuente vincula tolerancia baja a compartir proceso; se distingue un fallo grave de una excepción controlada.

**Caso Kafka.** El texto detalla la salida a MongoDB de la ruta de uptime; la figura también dibuja la conexión de duración al mismo consumidor. Se usan ambas evidencias para explicar el recorrido completo. No se atribuyen garantías de entrega a Kafka ni a la cadena a partir del dibujo.

## Elaboraciones propias

PedidoClaro, contratos JSON, cifras de capacidad, datos concretos de telemetría, cálculo de porcentaje activo, contrapresión y políticas de recuperación son ejemplos didácticos. No son valores ni algoritmos transcritos del capítulo. El código Unix es una variante explicada para ASCII; se contrastaron [tr](https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html) y [uniq](https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html). El campo de tarea se contrastó con [Task en AWS](https://docs.aws.amazon.com/step-functions/latest/dg/state-task.html).

Tres PNG propios en `Recursos visuales/Capítulo 12`, con `generar_diagramas.py` (Pillow): topología y despliegue, función de aptitud con almacenes, y selección de telemetría. Se revisaron visualmente los tres y se explican en prosa inmediatamente debajo. Las valoraciones de estrellas se conservan en una tabla cotejada con la figura 12-3; no se convierten en una serie de datos cuantitativos.

## Validación

Validación completada el **29 de septiembre de 2026**: **445 wikilinks y 496 enlaces Markdown locales** comprobados en la guía y el índice de lecturas, sin destinos ausentes; **45 anclas PDF** dentro del rango de sus archivos; YAML válido en las diez notas del capítulo y la nota de cobertura, con `title`, `created`, `capitulo` entero y `tags`; **cinco diagramas Mermaid** renderizados con Mermaid CLI y Chrome sin errores; **tres PNG** revisados visualmente. La tabla de estrellas se cotejó ampliando la figura 12-3. El ejemplo Unix se ejecutó con la entrada didáctica y devolvió `3 blue`, `2 red`, `1 green`.

El original y la copia tienen el mismo SHA-256: `83d08533db84578acbcb0cd8d86837e3ba9e595c6e42cbe2243fdf07d9214d8e`. Los índices generales incluyen el capítulo 12 y la biblioteca refleja nueve escaneos y 183 páginas de PDF. Los registros temporales de OCR y renderizado no forman parte de las notas entregadas.
