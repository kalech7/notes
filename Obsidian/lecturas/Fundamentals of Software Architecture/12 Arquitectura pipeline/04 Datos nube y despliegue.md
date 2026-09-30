---
title: "12 · Datos, nube y despliegue"
created: 2026-09-29
capitulo: 12
tags:
  - lecturas/software-architecture
  - arquitectura/pipeline
---

# Datos, nube y despliegue

[[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/00 Índice|← Índice del capítulo 12]]

**La forma de procesar y la forma de guardar datos son decisiones separadas.** El pipeline monolítico suele asociarse a una única base de datos, pero el libro admite desde un almacén compartido hasta uno por filtro.

## 1. La función de aptitud del libro

Una **función de aptitud** comprueba si la arquitectura conserva una propiedad importante. El ejemplo de la figura 12-2 se ejecuta continuamente sobre datos de producción para analizar una característica operativa, como tiempo de respuesta o escalabilidad.

![Datos y etapas de la función de aptitud](../Recursos%20visuales/Cap%C3%ADtulo%2012/c12-02-datos.png)

El productor captura datos brutos. El selector aplica reglas, como el intervalo temporal que interesa analizar. El analizador calcula tendencias y guarda resultados analíticos. El consumidor genera un informe. Las cajas verdes son almacenes que apoyan etapas concretas; las flechas horizontales llevan el trabajo entre ellas. Guardar un resultado intermedio no convierte automáticamente al analizador en consumidor: aún entrega datos para continuar.

El texto llama *Time Series Selector* al selector; el rótulo de la figura parece decir *Time Series Sector*. Las notas usan «selector de series temporales», coherente con la responsabilidad descrita.

Una **serie temporal** es un conjunto de observaciones asociadas a instantes, por ejemplo la duración de peticiones cada minuto. Un ejemplo propio de selección es conservar solo la última hora. Un ejemplo de análisis es calcular cómo cambió el percentil 95 de duración entre intervalos. **Percentil 95** significa un valor por debajo del cual queda el 95 % de las observaciones. El capítulo no prescribe ese cálculo concreto: lo añadimos para hacer visible la responsabilidad del analizador.

## 2. Un almacén o varios

| Decisión | Ventaja posible | Costo que hay que examinar |
|---|---|---|
| Una base compartida | Menos infraestructura y respaldo central | Dependencia común, permisos amplios y cambios de esquema compartidos |
| Almacenes por etapa | Ajustar formato y acceso a cada responsabilidad | Más operación, sincronización y recuperación |
| Persistir solo al final | Menos escrituras intermedias | Repetir todo si se pierde el trabajo en memoria |
| Persistir puntos intermedios | Reiniciar desde un punto guardado | Definir versiones, limpieza y consistencia de esos puntos |

Las dos primeras alternativas aparecen en el libro; los efectos y las dos últimas filas son ampliaciones propias. Tener varios almacenes no prueba que haya varios despliegues ni varios quanta. Tampoco vuelve automáticamente independientes las etapas si comparten dependencias críticas.

## 3. Opciones en la nube

El capítulo considera el estilo adecuado para la nube por su separación de responsabilidades y su complejidad habitualmente contenida. Ofrece tres posibilidades: toda la cadena en una aplicación, filtros como funciones y filtros en contenedores. Un **contenedor** empaqueta una aplicación y su entorno de ejecución; una **función sin servidor** permite ejecutar una tarea sin administrar directamente el servidor que la aloja. Ninguna elimina la necesidad de contratos y recuperación.

El ejemplo de Step Functions convierte cada filtro en una tarea que invoca una función Lambda. **Step Functions** es el coordinador del flujo, y **Lambda** ejecuta las tareas. La definición del libro utiliza:

| Campo | Papel en el ejemplo |
|---|---|
| `StartAt` | Nombre del primer estado |
| `States` | Catálogo de etapas |
| `Type: Task` | Estado que ejecuta trabajo |
| `Resource` | Recurso invocado, una Lambda en este caso |
| `Next` | Estado al que continúa la ejecución |
| `End: true` | Última etapa del recorrido |

El encadenamiento es capturar → seleccionar → analizar → generar informe. Los ARN del escaneo contienen marcadores de región y cuenta: ilustran la estructura, pero no son recursos listos para ejecutar. **ARN** es un identificador de recursos AWS. La definición tampoco establece por sí sola permisos, contratos, tiempos máximos o política de fallos. El campo `Type: Task` se contrastó con la [documentación oficial de estados Task](https://docs.aws.amazon.com/step-functions/latest/dg/state-task.html).

## 4. Precisión sobre las garantías de ejecución

El libro contrapone Standard («exactamente una vez») y Express («puede repetirse»). La [documentación oficial de AWS](https://docs.aws.amazon.com/step-functions/latest/dg/choosing-workflow-type.html), consultada el 29 de septiembre de 2026, distingue **Standard: exactamente una vez, salvo `Retry` explícito; Express asíncrono: al menos una vez; Express síncrono: como máximo una vez**. «Al menos una vez» permite duplicados; «como máximo una vez» no garantiza que todo trabajo complete.

Por ello, las tareas con efectos externos necesitan una política de repetición. **Idempotencia** significa que repetir una operación con la misma identidad conserva el efecto previsto; por ejemplo, guardar un resultado con el mismo identificador en lugar de añadir otro. La garantía del coordinador no debe interpretarse como prueba automática de unicidad de todas las escrituras externas.

> [!question]- ¿Para usar pipeline en la nube hace falta repartirlo en funciones?
> No. El libro admite un único servicio que contenga todos los filtros. La distribución se justifica por necesidades concretas de capacidad, aislamiento o despliegue, junto con sus costos.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/09 Arquitectura pipeline.pdf#page=4|PDF 4–5 · impresas 184–185 · figura 12-2 y definición Step Functions]]

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/03 Contratos sincronía y rendimiento|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/05 Riesgos errores y recuperación|Siguiente →]]
