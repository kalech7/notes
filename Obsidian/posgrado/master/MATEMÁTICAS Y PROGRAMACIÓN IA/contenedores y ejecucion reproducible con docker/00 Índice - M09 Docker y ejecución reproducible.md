---
title: "Índice - M09 Docker y ejecución reproducible"
modulo: M09
tags:
  - master/matematicas-programacion
  - m09
---

# Índice - M09 Docker y ejecución reproducible

El módulo responde: **¿cómo traslado un entrenamiento a otra máquina y demuestro qué condiciones se conservaron?** Docker empaqueta software; el experimento también depende de datos, configuración y del host.

## Antes de empezar

Un **host** es la máquina que ejecuta; un **runtime** permite ejecutar el programa; una **dependencia** es una biblioteca que utiliza; un **artefacto** es un resultado guardado, como métricas o pesos.

La conexión con M08 es directa: allí aprendiste a entrenar y diagnosticar. Aquí aprendes a ejecutar ese mismo proceso bajo condiciones declaradas.

![[assets/m09-04.png|1000]]

Lee el dibujo de fuera hacia dentro: el host aporta recursos; la imagen aporta software; el contenedor ejecuta el proceso. Abajo, los mounts conectan entradas y salidas con carpetas del host. La imagen sola no contiene toda la identidad del experimento.

## Ruta de estudio

1. [[01 Imagen, contenedor, host y persistencia]]
2. [[02 Contrato de ejecución - opciones, mounts y aislamiento]]
3. [[03 Programa reproducible - semillas, datos y formas]]
4. [[04 Build - Dockerfile, lock, capas y caché]]
5. [[05 Evidencia - preflight, ledger y comparación entre hosts]]
6. [[06 Laboratorio guiado y autoevaluación - M09]]

## Qué cubre cada parte

| Notas | Diapositivas | Pregunta |
|---|---|---|
| 01 | 1–6 | ¿Qué empaqueta Docker y qué persiste? |
| 02 | 7–9, 12, 19 | ¿Qué permite y restringe el comando? |
| 03 | 10–12 | ¿Qué controla el programa? |
| 04 | 13–17 | ¿Cómo se construye e identifica la imagen? |
| 05 | 18–23 | ¿Qué evidencia permite comparar ejecuciones? |
| 06 | integración | ¿Puedo explicar y detectar fallos? |

Las diapositivas contienen valores propuestos y campos «por observar»: son parte del ejercicio original, no resultados verificados en tu equipo. Aquí se explican; no se ha construido ni ejecutado su aplicación de entrenamiento.

Fuente completa: [[assets/module_09.pdf|PDF M09]].

Volver a [[../00 INICIO - Qué es cada cosa y ruta maestra de IA]]. Continuar con [[../modelo relacional y sql analitico/00 Índice - M10 Modelo relacional y SQL analítico|M10: organizar y comparar resultados]].


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- ¿La misma imagen garantiza las mismas métricas?
> No. También influyen datos, configuración, semillas, plataforma, hardware y operaciones numéricas. Se comparan evidencias y se declaran límites.
