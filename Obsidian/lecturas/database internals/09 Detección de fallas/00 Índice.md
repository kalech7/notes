---
title: "Database Internals — Capítulo 9 · Detección de fallas"
created: 2026-09-30
libro: "Database Internals"
capitulo: 9
tags:
  - lecturas/database-internals
  - arquitectura/deteccion-de-fallas
---

# Capítulo 9 · Detección de fallas

[[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice del capítulo 9]]

Una base distribuida necesita dejar de esperar a participantes que ya no pueden ayudar. Pero una respuesta ausente también puede deberse a una cola, una pausa del proceso o un camino de red averiado. Este capítulo explica cómo convertir observaciones incompletas en **sospechas útiles**, y cómo limitar los costos de equivocarse.

Se cubre el capítulo completo: **PDF 1–9, impresas 195–203**. La correspondencia dentro de este capítulo es `impresa = página PDF + 194`. El PDF compartido también incluye los capítulos 10 y 11; en PDF 10 comienza el capítulo 10, impresa 205. No hay una página escaneada con el folio 204.

## Ruta de lectura

1. [[Obsidian/lecturas/database internals/09 Detección de fallas/01 Sospecha garantías y errores|Sospecha, garantías y errores]]: por qué un proceso lento parece caído, qué prometen completitud y exactitud y qué implica una sospecha falsa.
2. [[Obsidian/lecturas/database internals/09 Detección de fallas/02 Pings heartbeats y plazos|Pings, heartbeats y plazos]]: quién inicia la comunicación, cómo se mide el silencio y por qué importa separar frecuencia y timeout.
3. [[Obsidian/lecturas/database internals/09 Detección de fallas/03 Contadores sin timeout y sondeos indirectos|Contadores sin timeout y sondeos indirectos]]: evidencias que atraviesan otras rutas y comprobaciones delegadas del tipo descrito para SWIM.
4. [[Obsidian/lecturas/database internals/09 Detección de fallas/04 Phi-accrual adaptación y umbrales|Phi-accrual, adaptación y umbrales]]: transformar una historia de intervalos en una escala de sospecha sin confundirla con probabilidad de caída.
5. [[Obsidian/lecturas/database internals/09 Detección de fallas/05 Gossip y tablas de latidos|Gossip y tablas de latidos]]: compartir novedades, conservar su frescura y entender el costo de la difusión.
6. [[Obsidian/lecturas/database internals/09 Detección de fallas/06 FUSE y propagación del silencio|FUSE y propagación del silencio]]: cómo una falla individual pasa a significar indisponibilidad de un grupo.
7. [[Obsidian/lecturas/database internals/09 Detección de fallas/07 Laboratorio y repaso resuelto|Laboratorio y repaso resuelto]]: decisiones, cálculos y ejercicios con respuestas.

## El hilo del capítulo

Cada mecanismo añade una clase de evidencia. El sondeo directo comprueba una ruta entre dos participantes. Los intermediarios comprueban rutas alternativas. Gossip propaga lo observado por otros participantes. Phi calibra qué tan extraño resulta el silencio respecto de la historia reciente. FUSE cambia el objetivo: informar que un grupo dejó de funcionar como unidad, en vez de recuperar una descripción precisa del estado físico de cada miembro.

Estos mecanismos no autorizan por sí solos escrituras incompatibles ni reemplazan un protocolo de acuerdo. El sistema que consume las sospechas necesita reglas de seguridad que sigan válidas cuando el detector se equivoca.

## Gráficos y figuras cubiertas

Las figuras 9-1 y 9-2 se explican en la nota 02; la 9-3, en la nota 03; la 9-4, en la nota 05; y la 9-5, en la nota 06. Hay **cinco gráficos originales en español**, con escenarios propios. No son capturas de las figuras ni mediciones de una instalación real. Se regeneran con [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 09/generar_graficos.py|el script de gráficos]], que usa Pillow.

Las notas explican dos precisiones del texto: phi es una transformación de una cola estadística, y la enumeración de FUSE en impresa 202 nombra por error a P1 donde corresponde P4. La tabla de gossip también distingue número de mensajes de volumen de bytes.

La bibliografía de impresa 203 orienta la lectura adicional hacia las abstracciones de detectores y su relación con consenso. Estas notas se basan en el capítulo adjunto; no afirman haber leído esos artículos ni haber comprobado versiones actuales de las herramientas mencionadas por el libro.

**Cobertura y revisión:** [[Obsidian/lecturas/database internals/90 Fuentes y revisión/08 Cobertura y validación de detección liderazgo y replicación|Mapa de páginas, figuras y validación]].

**Referencia:** PDF 1–9 · impresas 195–203. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=1|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Anterior: capítulo 8]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/01 Sospecha garantías y errores|Siguiente]] →
