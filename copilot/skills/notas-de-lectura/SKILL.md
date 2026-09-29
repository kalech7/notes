---
name: notas-de-lectura
description: Crear o ampliar notas de estudio en Obsidian a partir de un libro, capítulo o PDF escaneado (carpeta Obsidian/lecturas). Úsala cuando el usuario comparta un PDF o capítulo y pida notas, explicaciones, resúmenes a detalle, diagramas o imágenes para entender el libro sin tener que leerlo.
metadata:
  copilot-enabled-agents: claude, codex, opencode
---

# Notas de lectura

Objetivo: que el lector **entienda de forma sencilla y completa lo que dice el libro sin necesidad de leerlo**. Las notas explican; el PDF queda solo como referencia para contrastar.

## 1. Leer la fuente de verdad

- Lee **todas** las páginas del PDF. Si es un escaneo sin capa de texto, renderiza cada página a imagen (`uv run --with pymupdf`) y léela; gira las páginas apaisadas. Amplía tablas y figuras antes de citar cifras o estrellas.
- Anota la correspondencia página PDF ↔ página impresa (p. ej. «impresa = PDF + 164»), el número de cada figura/ejemplo y los huecos.
- Contrasta cifras, unidades y afirmaciones técnicas. Si el libro se contradice o se equivoca (unidades, tablas que no coinciden con el texto, pseudocódigo con errores), dilo explícitamente y explica la versión correcta.
- Copia el PDF a `Materiales/NN Tema.pdf` del libro sin alterarlo.

## 2. Estructura en el vault

- Una carpeta por capítulo: `NN Título/00 Índice.md` + notas temáticas cortas numeradas (`01 …`, `02 …`) + una nota final de laboratorio y repaso resuelto.
- Propiedades YAML en cada nota: `title`, `created` (fecha real), `capitulo` (entero) y `tags` con `lecturas/<libro>` y `arquitectura/<tema>` (o el equivalente del libro). Sigue la convención de los capítulos vecinos.
- Navegación con wikilinks de ruta completa: enlace al índice arriba y pie `← Anterior · Siguiente →`; la última nota enlaza al capítulo siguiente o al índice.
- Actualiza los índices generales: `00 Empieza aquí`, `README.md`, la nota de fuentes y cobertura (`90 Fuentes y revisión/…`) y el índice de lecturas si cambia el alcance.

## 3. Cómo explicar

- Explica **a detalle y con lenguaje sencillo**: define cada término la primera vez, da la causa («por qué ocurre») y la consecuencia («qué cambia para ti»), y profundiza en cada tópico en lugar de resumirlo.
- Usa ejemplos propios concretos, cálculos paso a paso, tablas comparativas y preguntas con respuesta plegable (`> [!question]-`).
- Distingue siempre qué es del libro y qué es elaboración propia, pero sin convertir la nota en una lista de avisos.
- **Referencias solamente como cita**: «PDF 3–4 · impresas 167–168 · figura 11-2» y un enlace `[[…/Materiales/NN.pdf#page=N|…]]`. No mandes al lector a leer el libro para entender algo: la explicación tiene que estar en la nota.
- Nada de traducción literal ni transcripción de párrafos del libro.

## 4. Imágenes y diagramas

- Crea imágenes cuando ayuden a entender: recreaciones en español de las figuras del libro, comparaciones lado a lado, gráficos de cifras y conteos. Genéralas con un script Python (Pillow o matplotlib) guardado junto a las imágenes en `Recursos visuales/Capítulo NN/`, para poder regenerarlas.
- Usa diagramas **Mermaid** dentro de las notas para flujos, secuencias y decisiones. En `sequenceDiagram` no uses `;` dentro de las notas (corta el diagrama).
- Para gráficos con series de datos, carga la skill `dataviz` y valida la paleta.
- **Explica cada imagen o diagrama directamente en prosa**, justo debajo, como parte del texto: qué muestra, qué significan cajas, flechas y colores, y qué conclusión permite. **No pongas rótulos** como «Cómo leerlo», «Lectura guiada», «Lectura del gráfico», «Elementos:», «Recorrido paso a paso», ni encabezados de ese estilo, ni instrucciones al lector («sigue la flecha…», «observa…»). Solo la explicación.
- Revisa visualmente cada PNG generado (texto cortado, solapes) antes de enlazarlo.

## 5. Validar antes de entregar

- Todos los wikilinks, enlaces Markdown e imágenes resuelven; las anclas `#page=` no superan las páginas del PDF.
- El YAML de cada nota es válido y tiene las propiedades de la sección 2.
- Todos los bloques Mermaid se renderizan (por ejemplo con `npx -p @mermaid-js/mermaid-cli mmdc` y Chrome del sistema).
- Registra el resultado de la validación en la nota de fuentes y entrega al usuario la ruta de lectura.
