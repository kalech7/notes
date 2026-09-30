---
title: "DDIA 2.ª edición — Guardar, evolucionar, replicar y repartir datos"
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

Esta carpeta desarrolla los **capítulos 4, 5, 6 y 7 de la segunda edición** de *Designing Data-Intensive Applications*, de Martin Kleppmann y Chris Riccomini. Los títulos y números corresponden a la [edición de O’Reilly](https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/). Las explicaciones incluyen ejemplos, diagramas y preguntas; los PDF quedan como referencia opcional.

> [!tip] Empieza aquí
> Abre [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/01 Antes de empezar datos bytes y páginas|Datos, bytes, páginas y contratos]]. Después sigue **Siguiente** al final de cada nota: el recorrido atraviesa los cuatro capítulos. Cada nuevo capítulo termina con laboratorio y repaso resuelto; la práctica anterior de almacenamiento y evolución permanece disponible como apoyo.

## Orden de lectura

| Paso | Abre este índice | Para qué sirve |
|---|---|---|
| 1 · Preparación | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/00 Índice\|Guía y fundamentos]] | Aclarar vocabulario; consultar el atlas cuando necesites una explicación visual |
| 2 · Capítulo 4 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/00 Índice\|Almacenamiento y recuperación]] | Seguir siete notas sobre logs, índices, motores, columnas y búsqueda |
| 3 · Capítulo 5 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/00 Índice\|Codificación y evolución]] | Seguir siete notas sobre versiones, formatos, APIs y mensajes |
| 4 · Capítulo 6 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice\|Replicación]] | Comprender líderes, lag, conflictos, CRDT, cuórums y causalidad en catorce notas |
| 5 · Capítulo 7 | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice\|Sharding y particionado]] | Elegir claves, índices, rebalanceo y enrutamiento en ocho notas |
| Apoyo · Aplicación | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/00 Índice\|Práctica y repaso]] | Resolver el caso, practicar las tarjetas y conectar con tus otras notas |
| Consulta | [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/00 Índice\|Fuentes y revisión]] | Revisar cobertura, escaneos y procedencia de imágenes |

**Cómo interpretar los números:** `04 Almacenamiento`, `05 Codificación`, `06 Replicación` y `07 Sharding` corresponden a capítulos del libro. `01 Guía`, `06 Práctica y repaso` y `90 Fuentes` son apoyo. La carpeta de práctica conservó su número anterior para mantener tus enlaces; no es el capítulo 6. Dentro de cada carpeta, `00 Índice` explica qué leer y en qué orden.

## El hilo que une los capítulos

Una tienda guarda un pedido, lo consulta por cliente y suma ventas por mes. El capítulo 4 explica cómo organizar los datos para escribirlos, encontrarlos y recuperarlos tras un fallo. El capítulo 5 explica cómo representarlos para que programas de distintas versiones puedan interpretarlos correctamente. El 6 mantiene copias en distintas máquinas y explica qué sucede si se atrasan o reciben cambios concurrentes. El 7 reparte datos entre máquinas y estudia el costo de consultar, mover y coordinar esas partes.

Pregunta siempre **qué trabajo estás ahorrando, qué costo añades y qué información debe sobrevivir**. Una nota es una buena unidad de estudio: entiende el problema, sigue el ejemplo y responde las preguntas sin mirar.

## Consultas rápidas

- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/02 Atlas visual explicado|Atlas visual explicado]]: sigue versiones LSM, dos esquemas Avro, timeouts y formas de búsqueda.
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/03 Mapa de decisiones de almacenamiento y evolución|Mapa de decisiones]]: pasa de un requisito a mecanismos, costos, fallos y pruebas sin depender de recetas tecnológicas.
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/02 Glosario y tarjetas de memoria|Glosario y tarjetas de memoria]]: busca un término o repasa lo aprendido.
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Mapa de lectura.canvas|Mapa de lectura]]: recorre las relaciones de forma visual en Obsidian.
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/01 Fuentes y cobertura|Alcance y fuentes]]: identifica qué material se trabajó y sus límites.

Las notas de lectura están en los bloques numerados. **Materiales** contiene los cuatro PDF; **Recursos visuales** contiene imágenes y generadores reproducibles. Las subcarpetas de los capítulos 6 y 7 reúnen recreaciones en español de las 26 figuras del libro. Sus explicaciones y procedencia se encuentran enlazadas desde los índices.

> [!success] Una señal de que ya lo entendiste
> Puedes cambiar los nombres del ejemplo y seguir explicando por qué funciona, cuánto trabajo evita y en qué caso dejaría de ser una buena elección.
