---
title: "02 Pensamiento arquitectónico · 2.ª edición"
created: 2026-09-25
tags:
  - lecturas/software-architecture
---

# Capítulo 2 · Pensamiento arquitectónico

[← Inicio del libro](../00%20Empieza%20aqu%C3%AD.md)

Este capítulo está dividido en **8 notas**. Lee en orden y usa **Anterior / Siguiente** al final de cada una. La última reúne las preguntas y el ejercicio resuelto.

## Orden de lectura

| Nota | Lo que podrás explicar |
|---|---|
| [01 · Arquitectura y diseño](01%20Arquitectura%20y%20dise%C3%B1o.md) | Evaluar el alcance de una decisión. |
| [02 · Amplitud y profundidad](02%20Amplitud%20y%20profundidad.md) | Administrar lo que sabes y lo que necesitas explorar. |
| [03 · Experiencia y aprendizaje](03%20Experiencia%20y%20aprendizaje.md) | Detectar conocimiento desactualizado y ampliar criterio. |
| [04 · Radar tecnológico personal](04%20Radar%20tecnol%C3%B3gico%20personal.md) | Organizar la exploración de tecnologías. |
| [05 · Compensaciones colas y contratos](05%20Compensaciones%20colas%20y%20contratos.md) | Comparar alternativas de mensajería y sus costos. |
| [06 · Negocio y agilidad](06%20Negocio%20y%20agilidad.md) | Traducir objetivos de negocio en capacidades. |
| [07 · Programar sin ser cuello de botella](07%20Programar%20sin%20ser%20cuello%20de%20botella.md) | Colaborar con el equipo sin concentrar el trabajo. |
| [08 · Preguntas y ejercicio resuelto](08%20Preguntas%20y%20ejercicio%20resuelto.md) | Justificar una solución para el historial de pedidos. |

## Alcance y modo de lectura

Esta guía desarrolla el capítulo 2, *Architectural Thinking*, de **Mark Richards y Neal Ford, Fundamentals of Software Architecture, segunda edición**. La fuente disponible corresponde al **PDF 21.32, páginas 13–31**, equivalentes a las **páginas impresas 17–35**. Se consultó el texto extraído de cada página y se revisaron las imágenes del escaneo. El archivo de consulta es [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/01 Introducción y pensamiento arquitectónico.pdf|01 Introducción y pensamiento arquitectónico]]. Los números «PDF» de esta nota se refieren a ese fragmento, no a una edición digital completa.

> [!info] Libro, elaboración y supuestos
> Las referencias identifican las ideas del libro. **PedidoClaro es una tienda de sándwiches inventada para esta guía**, distinta de la kata *Silicon Sandwiches*. Sus cifras, decisiones y ejercicios son elaboración didáctica propia. La explicación de agilidad compuesta es una ampliación: no aparece desarrollada con ese nombre en las páginas asignadas. La corrección sobre RabbitMQ se distingue y enlaza a documentación oficial.

Pensar arquitectónicamente significa preguntar qué consecuencias tendrá una decisión sobre el sistema y las personas que lo construyen y operan. Elegir una biblioteca puede parecer un detalle local; si condiciona los despliegues de diez equipos durante cinco años, sus consecuencias dejan de ser locales. La mirada arquitectónica conecta estructura, restricciones, conocimiento y negocio. **Fuente: PDF p. 13; impresa p. 17.**

## Referencias y límites de la fuente

La correspondencia de este fragmento es **página impresa = página PDF + 4**. El encabezado inicial y el último pie presentan ruido OCR; 17 y 35 se reconstruyen por continuidad con páginas interiores legibles. Los diagramas de esta guía son elaboraciones propias, no reproducciones de figuras escaneadas.

| Tema | Páginas del PDF 21.32 | Páginas impresas |
| --- | --- | --- |
| Espectro arquitectura/diseño | 13–16 | 17–20 |
| Pirámide y mantenimiento del conocimiento | 16–19 | 20–23 |
| Frozen Caveman y veinte minutos | 20–21 | 24–25 |
| Burbujas y radar | 21–25 | 25–29 |
| Subastas y compensaciones | 26–29 | 30–33 |
| Negocio y trabajo con código | 29–31 | 33–35 |

![colas y publicacion](../Recursos%20visuales/02-colas-y-publicacion.png)

*Figura original: repartir entregas dentro de una cola y difundir eventos entre intereses son operaciones distintas.* Las afirmaciones generales de mensajería deben leerse con el matiz documentado; la agilidad compuesta y las cifras de PedidoClaro son ampliaciones explícitas. Esta nota no presupone contenido de páginas ausentes.

---

[← Capítulo anterior](../01%20Introducci%C3%B3n/00%20%C3%8Dndice.md) · [Comenzar este capítulo](01%20Arquitectura%20y%20dise%C3%B1o.md) · [Capítulo siguiente →](../03%20Modularidad/00%20%C3%8Dndice.md)
