---
title: "Database Internals — Comparar bases y diseñar benchmarks"
created: 2026-09-26
libro: "Database Internals"
tags:
  - lecturas/database-internals
  - fundamentos
  - benchmarks
  - trade-offs
---

# Comparar bases y diseñar benchmarks

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/00 Guía y fundamentos/00 Índice|Guía y fundamentos]]

> [!abstract] Idea que organiza la nota
> No se elige una base por popularidad, lenguaje o una cifra aislada. Se parte del workload y de las garantías necesarias, se construye una prueba representativa y se observa también cómo se opera, falla, recupera y actualiza el sistema.

## El storage engine no define por sí solo al DBMS

El **storage engine** es el componente que almacena, recupera y administra datos en memoria y disco; normalmente expone operaciones granulares sobre registros a las capas superiores del DBMS. Para el motor, claves y valores pueden ser secuencias de bytes. Capas superiores deciden si esos bytes representan enteros, strings, filas o versiones. Esta separación permite reutilizar motores como componentes intercambiables, pero dos productos con el mismo motor pueden comportarse de forma distinta por su protocolo, planificador, transacciones, replicación, configuración y valores por defecto.

Por eso frases como «usa un LSM», «está escrito en C++» o «es el más popular» solo sirven como pistas iniciales. No demuestran que el sistema responda bien a tu carga ni que cumpla tus garantías.

## Describe el workload antes de medir

Una comparación defendible comienza con variables observables:

| Dimensión | Preguntas mínimas |
|---|---|
| datos | ¿qué esquema, tamaño de registro, volumen y crecimiento se esperan? |
| clientes | ¿cuántas conexiones concurrentes y qué coordinación requieren? |
| accesos | ¿predominan igualdad, rangos, joins, agregaciones o escrituras por lote? |
| mezcla | ¿qué proporción de lecturas, inserciones, updates y deletes existe? |
| garantías | ¿qué consistencia, aislamiento, durabilidad y recuperación son obligatorios? |
| operación | ¿cómo se escala, respalda, restaura, observa, repara y actualiza? |

Incluye el futuro razonable: un sistema que hoy cabe en un nodo puede mostrar problemas solo tras horas de compactación, crecimiento del caché, acumulación de tombstones o expansión del clúster.

```mermaid
flowchart LR
  R[Requisitos y SLA] --> W[Modelo de workload]
  W --> E[Entorno parecido a producción]
  E --> P[Prueba prolongada y fallos]
  P --> M[Métricas y evidencia]
  M --> D{Decisión}
  D -->|faltan datos| W
  D -->|candidato viable| O[Ensayo operativo y de upgrade]
```

**Lo que demuestra el ciclo:** la evaluación no avanza linealmente hacia un ganador. Si las métricas no explican el comportamiento real, la evidencia obliga a corregir el modelo de workload. Superar una meta de rendimiento tampoco termina la evaluación: aún deben demostrarse operación, recuperación y upgrades.

## Mide lo que el usuario realmente necesita

El throughput medio no basta. Según el servicio, importan p50, p95 y p99 de latencia; operaciones por segundo sostenidas; tiempo de recuperación; pérdida admisible de datos; consumo de CPU, memoria, red y disco; amplificación; costo por unidad de carga; y comportamiento durante mantenimiento o fallos.

Un benchmark conocido es un vocabulario común, no una garantía de representatividad. YCSB ofrece workloads portables para almacenes de datos. TPC-C modela una mezcla OLTP concurrente de lecturas y updates y exige propiedades funcionales y de durabilidad, no solo velocidad. Ambos pueden ser útiles si su mezcla y configuración se parecen al caso real; de lo contrario contestan otra pregunta.

> [!example] Un ganador falso
> A alcanza 120 000 ops/s y B alcanza 85 000. Sin embargo, A confirma antes de hacer durable el log, usa un dataset que cabe por completo en RAM y degrada a 18 000 ops/s durante compactación. B mantiene 80 000 con fsync, dataset mayor que RAM y p99 estable. Si el servicio exige durabilidad y latencia predecible, A no ganó: la prueba comparó contratos diferentes.

## Ensaya el ciclo de vida, no solo el estado estable

Una prueba útil también debe responder:

1. ¿Qué ocurre al reiniciar un nodo durante carga?
2. ¿Cuánto tarda recovery y cuánta capacidad queda mientras tanto?
3. ¿Cómo se añade capacidad y se rebalancean datos?
4. ¿Se pueden diagnosticar consultas lentas, corrupción y presión de almacenamiento?
5. ¿Un backup restaurado produce un sistema verificable?
6. ¿Cómo se instala una versión nueva y cómo se revierte?

La comunidad, documentación y herramientas también forman parte del riesgo. Ejecutar la prueba enseña si el equipo puede operar y depurar el sistema, no solo si este responde rápido en el caso feliz.

## Trade-offs: toda optimización paga en otra parte

Un storage engine debe escoger layout, serialización, orden, mutabilidad, recolección de basura, concurrencia y recuperación. Guardar en orden de llegada puede abaratar la escritura inmediata y encarecer la lectura ordenada. Comprimir aumenta densidad y gasta CPU. Mantener más índices acelera rutas concretas y multiplica el trabajo de cada cambio.

La pregunta útil no es «¿qué diseño es mejor?», sino:

- ¿qué costo reduce bajo este workload?;
- ¿dónde reaparece ese trabajo?;
- ¿qué garantía o caso extremo puede debilitar?;
- ¿cómo sabremos en producción que el supuesto dejó de cumplirse?

## Errores frecuentes

| Error | Por qué invalida la conclusión | Corrección |
|---|---|---|
| dataset demasiado pequeño | mide RAM y no el camino de almacenamiento | exceder la memoria disponible y declarar el estado del caché |
| configuraciones con garantías distintas | compara contratos diferentes | igualar durabilidad, consistencia, replicación e aislamiento |
| medir pocos minutos | oculta compactación, checkpoints y crecimiento | ejecutar hasta observar varios ciclos de mantenimiento |
| reportar solo el promedio | esconde colas y pausas | incluir percentiles, máximos razonados y series temporales |
| omitir warm-up y datos iniciales | favorece al candidato con caché o preparación distinta | documentar carga, calentamiento y reinicios |
| probar solo el caso feliz | no mide recuperabilidad ni operación | inyectar fallos, restaurar backups y ensayar upgrades |

## Comprueba que lo entendiste

> [!question]- ¿Por qué dos bases que usan el mismo storage engine no tienen por qué rendir ni garantizar lo mismo?
> Porque el DBMS añade planificación, transacciones, buffer management, replicación, protocolos, configuración y operación. El motor es un componente, no el producto completo.

> [!question]- ¿Qué debes igualar antes de comparar throughput?
> El contrato: workload, dataset, hardware, concurrencia y garantías de durabilidad, consistencia, replicación e aislamiento. Si difieren, las cifras responden preguntas distintas.

> [!question]- ¿Por qué una prueba prolongada puede invertir el resultado de una prueba corta?
> Porque aparecen checkpoints, compactaciones, garbage collection, crecimiento de índices, presión de caché y recuperación de fallos que la fase inicial aún no pagó.

**Fuente:** [[Obsidian/lecturas/database internals/Materiales/Database Internals - Parte I (fuente).pdf#page=1|PDF, introducción de la Parte I, pp. 1–6]]. El ejemplo y el diagrama son didácticos y originales.

---

**Anterior:** [[Obsidian/lecturas/database internals/00 Guía y fundamentos/02 Atlas visual explicado|Atlas visual explicado]] · **Índice:** [[Obsidian/lecturas/database internals/00 Guía y fundamentos/00 Índice|Guía]] · **Siguiente:** [[Obsidian/lecturas/database internals/01 Introducción y panorama general/00 Índice|Capítulo 1]]
