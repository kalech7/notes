---
title: "DDIA 2.ª edición — Entender cómo se guardan y evolucionan los datos"
created: 2026-09-25
autores:
  - Martin Kleppmann
  - Chris Riccomini
editorial: "O'Reilly"
tags:
  - lecturas/ddia
  - indice
  - bases-de-datos
---

# DDIA — Ruta de estudio

[[Obsidian/lecturas/00 Índice de lecturas|← Biblioteca de lecturas]]

Esta carpeta desarrolla los **capítulos 4 y 5 de la segunda edición** de *Designing Data-Intensive Applications*, de Martin Kleppmann y Chris Riccomini. Los títulos y números corresponden a la [edición de O’Reilly](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/). Las explicaciones incluyen ejemplos, diagramas y preguntas; los PDF quedan como referencia opcional.

> [!tip] Empieza aquí
> Abre [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/01 Antes de empezar datos bytes y páginas|Datos, bytes, páginas y contratos]]. Después sigue **Siguiente** al final de cada nota: el recorrido atraviesa los dos capítulos y termina en la práctica y el repaso.

## Orden de lectura

| Paso | Abre este índice | Para qué sirve |
|---|---|---|
| 1 · Preparación | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/00 Índice\|Guía y fundamentos]] | Aclarar vocabulario; consultar el atlas cuando necesites una explicación visual |
| 2 · Capítulo 4 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/00 Índice\|Almacenamiento y recuperación]] | Seguir siete notas sobre logs, índices, motores, columnas y búsqueda |
| 3 · Capítulo 5 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/00 Índice\|Codificación y evolución]] | Seguir siete notas sobre versiones, formatos, APIs y mensajes |
| 4 · Aplicación | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/00 Índice\|Práctica y repaso]] | Resolver el caso, practicar las tarjetas y conectar con tus otras notas |
| Consulta | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/00 Índice\|Fuentes y revisión]] | Revisar cobertura, escaneos y procedencia de imágenes |

**Cómo interpretar los números:** `04` y `05` son los capítulos del libro. `01`, `06` y `90` ordenan materiales de apoyo; no representan otros capítulos del libro. Dentro de cada carpeta, `00 Índice` explica qué leer y en qué orden.

## El hilo que une los capítulos

Una tienda guarda un pedido, lo consulta por cliente y suma ventas por mes. El capítulo 4 explica cómo organizar los datos para escribirlos, encontrarlos y recuperarlos tras un fallo. El capítulo 5 explica cómo representarlos para que programas de distintas versiones puedan interpretarlos correctamente.

Pregunta siempre **qué trabajo estás ahorrando, qué costo añades y qué información debe sobrevivir**. Una nota es una buena unidad de estudio: entiende el problema, sigue el ejemplo y responde las preguntas sin mirar.

## Consultas rápidas

- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/02 Atlas visual explicado|Atlas visual explicado]]: sigue versiones LSM, dos esquemas Avro, timeouts y formas de búsqueda.
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/02 Glosario y tarjetas de memoria|Glosario y tarjetas de memoria]]: busca un término o repasa lo aprendido.
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Mapa de lectura.canvas|Mapa de lectura]]: recorre las relaciones de forma visual en Obsidian.
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/01 Fuentes y cobertura|Alcance y fuentes]]: identifica qué material se trabajó y sus límites.

Las notas de lectura están en los bloques numerados. **Materiales** contiene los dos PDF; **Recursos visuales** contiene imágenes y el generador del gráfico. Sus explicaciones y procedencia se encuentran enlazadas desde los índices.

> [!success] Una señal de que ya lo entendiste
> Puedes cambiar los nombres del ejemplo y seguir explicando por qué funciona, cuánto trabajo evita y en qué caso dejaría de ser una buena elección.
