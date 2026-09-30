---
title: "Database Internals — Capítulo 7 · Laboratorio y repaso resuelto"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Laboratorio y repaso resuelto

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] Lo que vamos a comprobar
> La idea central ya está completa. Un modelo pequeño permite comprobar qué información necesita una lectura y cuándo una compactación puede retirar un borrado.

## Programa reproducible

El archivo [[Obsidian/lecturas/database internals/Materiales/Laboratorios/07 lsm_modelo.py|07 lsm_modelo.py]] usa solo la biblioteca estándar de Python. Desde la raíz del vault se ejecuta:

```bash
python3 'Obsidian/lecturas/database internals/Materiales/Laboratorios/07 lsm_modelo.py'
```

Modela fuentes ordenadas con registros `(clave, versión, valor)`. `None` representa tombstone. Incluye consulta actual, snapshot, mezcla por heap, compactación parcial conservadora, purga completa y un filtro Bloom con posiciones explícitas. No implementa discos, WAL durable, recuperación, hilos, transacciones ni borrados de rango; sus aserciones verifican las reglas lógicas de este modelo.

## Escenario resuelto

La tabla antigua tiene `10:rojo@1`, `20:naranja@1`, `30:azul@1`. La reciente tiene `10:verde@2`, `20:BORRADO@3`, `40:gris@2`.

| Pregunta | Resultado | Razón |
|---|---|---|
| Consulta actual de 10 | Verde | Versión 2 domina a 1 |
| Consulta actual de 20 | Ausente | Tombstone 3 domina al valor 1 |
| Snapshot 1 para 10 | Rojo | La versión 2 todavía no es visible |
| Snapshot 2 para 20 | Naranja | El borrado versión 3 queda fuera |
| Rango actual completo | 10:verde, 30:azul, 40:gris | Mezcla ordenada y reconciliación |

Compactar solo la tabla reciente conserva el tombstone 20@3. Si lo quitara, el archivo antiguo volvería a mostrar naranja. Compactar ambas tablas y no tener snapshots vigentes permite quitar tanto el valor viejo como su tombstone: ninguna fuente restante puede resucitarlo. Si snapshots necesitan estados anteriores, el programa conserva todas las versiones como estrategia segura y sencilla; un motor real puede usar una retención más selectiva.

## Bloom resuelto

Insertar hashes `{3,5,10}` y `{5,8,14}` en 16 bits enciende `{3,5,8,10,14}`. Consultar `{3,10,14}` devuelve positivo aunque esa clave no se insertó: es falso positivo. Consultar `{5,9,15}` devuelve negativo. El programa reproduce la figura 7-7 sin simular funciones hash reales.

Para 10 bits por clave y siete hashes, la aproximación es `(1-exp(-7/10))**7 ≈ 0,00819`, alrededor de 0,82 %. Aumentar hashes a veinte con la misma memoria da `(1-exp(-20/10))**20 ≈ 0,0546`, alrededor de 5,46 %: demasiados hashes saturan el filtro y empeoran precisión.

## Cálculo de una compactación

Dos entradas ocupan 150 MB cada una y la salida conserva 220 MB. Mientras se construye deben existir `150+150+220=520 MB` de archivos de esa tarea, sin contar WAL, índices auxiliares ni otros datos del motor. Al retirar las entradas queda la salida de 220 MB. El ahorro final no elimina el pico temporal.

Si en una ventana entran 100 MB lógicos, el WAL escribe 100, los flushes 100 y las compactaciones 400, el motor escribe 600 MB: amplificación 6 incluyendo WAL. Si el SSD tiene amplificación interna 1,5 sobre esos bytes en ese periodo, escribiría unos 900 MB NAND, razón 9 respecto a la carga lógica. Multiplicar requiere que las métricas cubran la misma ventana y las mismas escrituras.

## Repaso con respuestas plegables

> [!question]- ¿Por qué no participa en lecturas la salida de un flush incompleto?
> Porque una entrada ausente puede no haberse escrito aún. Hasta su publicación, la memtable congelada conserva la fuente completa de lectura.

> [!question]- ¿Por qué una compactación recién creada puede contener valores antiguos?
> Reorganiza datos y no cambia su orden lógico de versiones. La fecha de creación del archivo no reemplaza el número de versión de cada registro.

> [!question]- ¿Qué tres condiciones compruebas antes de purgar una marca?
> Que no queden versiones antiguas relevantes fuera de la tarea, que ningún snapshot necesite versiones descartadas y, si hay replicación, que las garantías del motor impidan reintroducir datos borrados desde réplicas atrasadas.

> [!question]- ¿Qué ventaja de niveles se pierde si se permiten rangos superpuestos dentro de L2?
> La garantía de como máximo una tabla candidata por clave dentro de ese nivel. La reconciliación puede seguir siendo correcta, pero aumenta la cantidad de candidatos.

> [!question]- ¿Qué conserva WiscKey para atender consultas por rango?
> Un índice de claves ordenadas. Los valores siguen ubicados en un log y pueden exigir I/O disperso aunque los resultados se entreguen por clave.

> [!question]- ¿Qué mejora LLAMA además de liberar espacio?
> Puede agrupar deltas del mismo nodo y consolidar su significado en una base nueva, reduciendo dispersión física y trabajo de reconstrucción del lector.

## Frase para iniciar una explicación propia

> «Un LSM acepta cambios en memoria y conserva versiones en archivos inmutables; al leer combina esas fuentes, y al compactar paga el trabajo que pospuso para mantener lecturas y espacio bajo control».

Esta frase conecta entrada, lectura y mantenimiento. Para ampliarla, añade la protección del WAL, las condiciones de los tombstones y la política de compactación que cambia los costos.

**Puente a la Parte II:** el motor local ya puede conservar y recuperar datos. La siguiente pregunta es qué ocurre cuando la información y las decisiones se distribuyen entre máquinas.

**Referencia:** PDF 1–36 · impresas 129–162, 165–166. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=1|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/14 Síntesis de la Parte I buffering mutabilidad y orden|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Siguiente: Parte II]] →
