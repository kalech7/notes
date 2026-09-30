---
title: "79 S07 - Guía de búsqueda vectorial e índices"
created: 2026-09-29
fecha: 2026-09-22
capitulo: 7
sesion: "07"
tags:
  - maestria/ia-generativa
  - recuperacion
  - bases-vectoriales
---

# 79 S07 - Guía de búsqueda vectorial e índices

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/79 S07 - Guía de búsqueda vectorial e índices|Guía de sesión 07]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

La sesión 06 explicó cómo convertir un texto en un vector. La sesión 07 responde **dónde guardarlo y cómo encontrar vecinos sin comparar siempre contra todos los vectores**. Es el puente que faltaba antes de estudiar RAG.

## El problema concreto

Imagina un millón de fragmentos de reglamentos y una consulta convertida en vector. La similitud permite ordenarlos, pero calcularla un millón de veces por pregunta puede consumir demasiado tiempo. Un **índice vectorial** organiza los vectores para reducir los candidatos examinados. Una **base de datos vectorial** añade almacenamiento, identificadores, metadatos, filtros y operaciones de actualización según su implementación.

No son lo mismo que el modelo de embeddings. El modelo define la representación y su espacio; el índice busca dentro de ese espacio. Una organización muy rápida no vuelve semánticamente útil una representación inadecuada.

## Ruta de lectura

| Nota | Lo que podrás explicar |
| --- | --- |
| [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/80 S07 - Búsqueda exacta aproximación y costo|80 S07 - Búsqueda exacta aproximación y costo]] | Qué significan N, d, k y por qué una búsqueda exhaustiva cuesta |
| [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/81 S07 - IVF celdas centroides y nprobe|81 S07 - IVF celdas centroides y nprobe]] | Por qué una frontera puede ocultar el vecino y cómo abrir más celdas |
| [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/82 S07 - HNSW capas conexiones y exploración|82 S07 - HNSW capas conexiones y exploración]] | Cómo un grafo guía la búsqueda y qué cambia al construir o consultar |
| [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/83 S07 - Recall del índice latencia y memoria|83 S07 - Recall del índice latencia y memoria]] | Qué se mide, contra qué referencia y cómo se paga en recursos |
| [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/84 S07 - Colecciones payload filtros y operación|84 S07 - Colecciones payload filtros y operación]] | Qué agrega una base vectorial y qué demuestra una demo |
| [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/85 S07 - Ejercicios resueltos de búsqueda vectorial|85 S07 - Ejercicios resueltos de búsqueda vectorial]] | Si puedes diagnosticar y calcular sin confundir métricas |

## Tres preguntas que se deben separar

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/60-s07-tres-evaluaciones.png|60-s07-tres-evaluaciones.png]]

Las tres cajas evalúan partes diferentes. La primera compara los vecinos del índice aproximado con la búsqueda exacta sobre los mismos vectores. La segunda pregunta si esos resultados contienen la evidencia necesaria. La tercera evalúa si la respuesta se fundamenta en el contexto. Las flechas indican una cadena de dependencias; no una garantía de calidad. Un índice puede reproducir perfectamente un ranking poco útil para la pregunta.

Esta separación explica por qué aumentar la exploración del índice no arregla siempre un RAG. Si el dato fue omitido al ingerir, si el embedding no representa el fragmento o si la respuesta inventa una causa, el defecto se encuentra en otra etapa.

## Qué se incorporó y qué no se supone

Fuente principal: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-07.pdf#page=1|sesión 07]], *Bases de datos vectoriales*, Daniel Andrés Riofrío Almeida, 22 de septiembre de 2026. Se leyeron el texto completo y las figuras de sus 24 páginas; página PDF = número visible. Las páginas 1, 3, 6, 15 y 20 son portada o separadores.

El PDF se encontró en Descargas durante esta revisión y se conservó intacto en `Materiales`. Su notebook `s2-mar` no está entre los materiales disponibles: las cuentas, figuras y ejemplos de estas notas son propios, no salidas de ese cuaderno. Las consignas docentes se explican como contenido académico; no se instalaron servicios ni se levantaron contenedores.

La teoría y las cuentas cubren todas las secciones académicas de la presentación. Las referencias a líneas internas, versiones y demos se atribuyen al PDF cuando no están verificadas por una copia local. Se consultó documentación primaria para precisar IVF/HNSW y operación; los enlaces aparecen junto a las aclaraciones correspondientes.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07 Embeddings y recuperación/33 PRÁCTICA - Embeddings y similitud semántica|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/80 S07 - Búsqueda exacta aproximación y costo|Siguiente]] →
