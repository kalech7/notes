---
title: "Lecturas — libros explicados y conectados"
created: 2026-09-25
tags:
  - lecturas
  - indice
---

# Lecturas

Este espacio está al mismo nivel que **freelance**, **posgrado** y **pregrado**. Aquí cada libro tiene una ruta de lectura, conceptos explicados con ejemplos, recursos visuales y conexiones con lo que ya estudiaste.

## Biblioteca

| Lectura | Material trabajado | Punto de entrada |
|---|---|---|
| *Designing Data-Intensive Applications*, segunda edición — Martin Kleppmann y Chris Riccomini | Capítulos 4 y 5 de los dos escaneos compartidos | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí\|Empezar DDIA]] |
| *Fundamentals of Software Architecture*, segunda edición — Mark Richards y Neal Ford | Material de los capítulos 1 a 5 presente en tres escaneos; 73 páginas revisadas, con huecos documentados | [[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí\|Empezar arquitectura de software]] |
| *Database Internals* — Alex Petrov | Parte I del PDF compartido: arquitectura del DBMS, B-Trees, formatos de archivo e implementación | [[Obsidian/lecturas/database internals/00 Empieza aquí\|Empezar Database Internals]] |

## Mapas para comprender el conjunto

Estas notas condensan las decisiones que atraviesan cada lectura. Son un buen punto de entrada después de los fundamentos y antes de los ejercicios:

- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/03 Mapa de decisiones de almacenamiento y evolución|DDIA · mapa de decisiones de almacenamiento y evolución]]: conecta carga, patrón de acceso, estructura de almacenamiento, representación y compatibilidad.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/04 Método completo para tomar decisiones|Arquitectura · método completo para tomar decisiones]]: recorre necesidad, escenario, prioridades, límites, alternativas, evidencia y revisión.
- [[Obsidian/lecturas/database internals/00 Guía y fundamentos/02 Atlas visual explicado|Database Internals · atlas visual explicado]]: sigue el recorrido desde el DBMS hasta bytes, páginas, splits y mantenimiento.

## Cómo estudiar una nota

1. Lee la pregunta que intenta resolver y explica el problema con tus propias palabras.
2. Relaciona el ejemplo con el mecanismo representado: identifica qué se guarda, quién lo consume y qué trabajo se evita o se añade.
3. Cierra la explicación y responde una pregunta de memoria.
4. Abre un enlace relacionado y explica **la relación**, no solo las dos definiciones por separado.

> [!tip] Regla para saber si ya puedes avanzar
> No memorices solo el nombre del mecanismo. Intenta predecir qué lectura, escritura, coordinación o recuperación cambia cuando modificas la carga, el formato o un requisito. Si tu predicción coincide con el ejemplo resuelto, entendiste la causa y no solo la definición.

La fuente original, una ampliación externa y un ejemplo inventado cumplen funciones distintas. En cada lectura se indica la procedencia para que puedas volver al material cuando tengas dudas.
