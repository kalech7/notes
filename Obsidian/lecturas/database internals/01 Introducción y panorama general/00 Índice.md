---
title: "Database Internals — Capítulo 1 · Introducción y panorama general"
created: 2026-09-26
tags:
  - lecturas/database-internals
  - indice
---

# Capítulo 1 · Introducción y panorama general

[[Obsidian/lecturas/database internals/00 Empieza aquí|← Inicio del libro]]

**Pregunta central:** ¿Cómo convierte una base de datos una petición lógica en bytes localizables, modificables y recuperables sin perder las garantías prometidas?

Lee las notas del 01 al 06. Cada una aísla una decisión del motor para que puedas entenderla antes de conectarla con las demás.

| Nota | Lo que podrás explicar |
|---|---|
| [[Obsidian/lecturas/database internals/01 Introducción y panorama general/01 Arquitectura de un DBMS\|01 · Arquitectura de un DBMS]] | Cómo una consulta atraviesa transporte, interpretación, optimización, ejecución y almacenamiento; dónde actúan concurrencia y recuperación |
| [[Obsidian/lecturas/database internals/01 Introducción y panorama general/02 Memoria disco y durabilidad\|02 · Memoria, disco y durabilidad]] | Por qué el medio principal cambia las estructuras y cómo log y checkpoint vuelven recuperable un estado en memoria |
| [[Obsidian/lecturas/database internals/01 Introducción y panorama general/03 Filas columnas y wide-column\|03 · Filas, columnas y wide-column]] | Qué localidad aprovecha cada layout y por qué una wide-column store no es un almacén columnar analítico |
| [[Obsidian/lecturas/database internals/01 Introducción y panorama general/04 Archivos de datos y organización\|04 · Archivos de datos y organización]] | Qué papel cumplen páginas, heap files, organización hash e index-organized tables |
| [[Obsidian/lecturas/database internals/01 Introducción y panorama general/05 Índices primarios secundarios y clustering\|05 · Índices, secundarios y clustering]] | Qué mapea un índice, qué significa clustered y cómo elegir entre localizador físico e indirección por clave primaria |
| [[Obsidian/lecturas/database internals/01 Introducción y panorama general/06 Mutabilidad orden y buffering\|06 · Mutabilidad, orden y buffering]] | Dónde pagan el trabajo B-Trees, LSM Trees y heaps, y por qué buffering, mutabilidad y orden son ejes independientes |

> [!tip] Hilo causal del bloque
> Las flechas de cada diagrama representan movimiento o dependencia, y el estado pendiente revela el costo aplazado. Una ruta rápida casi siempre desplaza trabajo hacia recuperación, mantenimiento de índices o procesos de fondo.

**Al terminar:** [[Obsidian/lecturas/database internals/02 Fundamentos de B-Trees/00 Índice|Continuar con los fundamentos de B-Trees]].
