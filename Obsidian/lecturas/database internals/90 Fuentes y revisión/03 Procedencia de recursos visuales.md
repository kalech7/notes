---
title: "Database Internals — Procedencia de recursos visuales"
created: 2026-09-26
tags:
  - lecturas/database-internals
  - recursos-visuales
---

# Procedencia de recursos visuales

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice|Fuentes y revisión]]

Los recursos `01`–`08` son SVG técnicos originales creados directamente como geometría y texto vectorial. Este método permite controlar claves, offsets, flechas y estados con precisión. El recurso `09` es una imagen raster generada con la herramienta integrada de generación de imágenes y se conserva por su función pedagógica, no decorativa.

| Recurso | Función explicativa |
|---|---|
| [[Obsidian/lecturas/database internals/Recursos visuales/01-arquitectura-dbms.svg\|01 · Arquitectura DBMS]] | Distinguir pipeline de consulta y controles transversales |
| [[Obsidian/lecturas/database internals/Recursos visuales/02-split-btree.svg\|02 · Split B-Tree]] | Mostrar reparto de hoja y copia del separador al padre |
| [[Obsidian/lecturas/database internals/Recursos visuales/03-slotted-page.svg\|03 · Slotted page]] | Separar orden lógico de ubicación física |
| [[Obsidian/lecturas/database internals/Recursos visuales/04-vacuum-page.svg\|04 · Vacuum]] | Comparar espacio fragmentado y contiguo |
| [[Obsidian/lecturas/database internals/Recursos visuales/05-filas-columnas.svg\|05 · Filas y columnas]] | Visualizar qué bytes lee una proyección |
| [[Obsidian/lecturas/database internals/Recursos visuales/06-fanout-altura.svg\|06 · Fanout y altura]] | Relacionar ancho del nodo con page reads |
| [[Obsidian/lecturas/database internals/Recursos visuales/07-endianness.svg\|07 · Endianness]] | Mostrar que el orden de bytes es parte del contrato |
| [[Obsidian/lecturas/database internals/Recursos visuales/08-rightmost-highkey-overflow.svg\|08 · Bordes del nodo]] | Explicar el intervalo derecho y el payload derramado |
| [[Obsidian/lecturas/database internals/Recursos visuales/09-split-btree-archivo.png\|09 · Split como archivo]] | Relacionar página llena, reparto ordenado y separador promovido al padre mediante una analogía concreta |

La explicación completa de cada figura está en [[Obsidian/lecturas/database internals/00 Guía y fundamentos/02 Atlas visual explicado|Atlas visual explicado]].

## Principios usados

- el título expresa la relación, no un tema genérico;
- las etiquetas usan claves o tamaños concretos;
- el color distingue estados o tipos, pero la información también se entiende por posición y texto;
- las flechas tienen significado descrito en la nota;
- toda simplificación se declara;
- la figura original del libro se usa como referencia conceptual, no se copia.

Los diagramas Mermaid dentro de las notas cubren secuencias y decisiones que cambian con el texto. Los SVG se reservan para layouts que se benefician de posiciones exactas.

## Recurso generado con herramienta integrada

**`09-split-btree-archivo.png`.** Resumen del prompt: una archivera reorganiza un cajón lleno en dos cajones de distinto color, coloca la clave `67` en el cajón derecho y publica una tarjeta `60` en un estante superior para representar la frontera del padre. La composición debía ser legible, sobria y semejante a un archivo físico, sin pretender copiar una figura del libro.

Su función es fijar cuatro correspondencias: cajón lleno → página antes del overflow; cajones azul y verde → páginas resultantes; `67` a la derecha → orden conservado porque `67 > 60`; tarjeta `60` arriba → separador publicado en el padre. La imagen no prescribe una convención universal: el separador puede ser la primera clave derecha o una frontera equivalente.

---

**Anterior:** [[Obsidian/lecturas/database internals/90 Fuentes y revisión/02 Revisión de estructura y calidad|Revisión de calidad]] · **Índice:** [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice|Fuentes]] · **Inicio:** [[Obsidian/lecturas/database internals/00 Empieza aquí|Ruta de estudio]]
