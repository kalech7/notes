---
title: "Database Internals — Capítulo 10 · Elección de líder"
created: 2026-09-30
libro: "Database Internals"
capitulo: 10
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Capítulo 10 · Elección de líder

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Capítulo 10]]

Un líder organiza el trabajo de varios procesos. Puede ordenar operaciones, coordinar una recuperación y evitar que cada decisión exija conversaciones entre todos. Elegirlo parece sencillo cuando todos se ven, pero una red partida cambia la pregunta: cada grupo puede encontrar un ganador diferente. Este capítulo enseña algoritmos de elección y muestra por qué tener un ganador local no basta para proteger los datos.

La fuente contiene el capítulo completo: **PDF 10–18 · impresas 205–213**, incluidas las cinco figuras 10-1 a 10-5, el resumen y la bibliografía final. En este tramo, **impresa = página PDF + 195**. No hay páginas faltantes dentro del capítulo. Las referencias a capítulos 12 y 14 son anticipaciones del libro; sus desarrollos no aparecen en este escaneo.

## Ruta de lectura

| Nota | Pregunta que resuelve |
|---|---|
| [[Obsidian/lecturas/database internals/10 Elección de líder/01 Coordinación estabilidad y garantías\|01 Coordinación y garantías]] | ¿Para qué sirve un líder y qué significa elegirlo correctamente? |
| [[Obsidian/lecturas/database internals/10 Elección de líder/02 Bully rangos y sucesores preparados\|02 Bully y sucesores]] | ¿Cómo gana el mayor rango y cómo se acelera su reemplazo? |
| [[Obsidian/lecturas/database internals/10 Elección de líder/03 Candidatos ordinarios y elecciones simultáneas\|03 Candidatos y ordinarios]] | ¿Cómo reducir candidatos y evitar que todos inicien a la vez? |
| [[Obsidian/lecturas/database internals/10 Elección de líder/04 Invitación y fusión de grupos\|04 Invitación]] | ¿Cómo se unen grupos que ya tienen líderes? |
| [[Obsidian/lecturas/database internals/10 Elección de líder/05 Elección en anillo y máximo acumulado\|05 Anillo]] | ¿Por qué hacen falta una vuelta para descubrir y otra para informar? |
| [[Obsidian/lecturas/database internals/10 Elección de líder/06 Split brain mayorías y relación con consenso\|06 Particiones y consenso]] | ¿Qué falta para que dos líderes no confirmen decisiones incompatibles? |
| [[Obsidian/lecturas/database internals/10 Elección de líder/07 Laboratorio y repaso resuelto\|07 Laboratorio]] | ¿Puedes reconstruir mensajes, calcular quórums y encontrar un contraejemplo? |

## Qué podrás distinguir

**Disponibilidad** significa poder atender trabajo bajo los supuestos del sistema. **Vivacidad** significa que el algoritmo acaba progresando, por ejemplo terminando una elección. **Seguridad** significa que nunca ocurre el resultado prohibido, por ejemplo dos decisiones incompatibles confirmadas para el mismo lugar de un registro. No son intercambiables: un algoritmo puede elegir rápidamente un líder en cada mitad de la red y perder la unicidad global.

Las figuras de estas notas son recreaciones didácticas propias de los ejemplos del libro, con texto en español y los mensajes desglosados. Los cálculos de mensajes, el ejemplo de grupos de tamaños 7 y 2 y los ejercicios son elaboración propia; no son resultados medidos.

**Cobertura y revisión:** [[Obsidian/lecturas/database internals/90 Fuentes y revisión/08 Cobertura y validación de detección liderazgo y replicación|Páginas, figuras y validación del bloque 9–11]].

**Referencia:** PDF 10–18 · impresas 205–213. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=10|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Anterior: capítulo 9]] · [[Obsidian/lecturas/database internals/10 Elección de líder/01 Coordinación estabilidad y garantías|Siguiente]] →
