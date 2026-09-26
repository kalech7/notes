---
title: "DDIA — Procedencia de imágenes y prompts"
created: 2026-09-25
tags:
  - lecturas/ddia
  - recursos-visuales
---

# Procedencia de imágenes y prompts

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/00 Índice|Fuentes y revisión]]

Las siete ilustraciones se generaron con la herramienta integrada **image_gen**, se revisaron visualmente y se guardaron en la carpeta `Recursos visuales` del libro. Son analogías didácticas originales, no fotografías ni figuras del libro. El texto de las notas desarrolla las condiciones que la imagen simplifica.

## 1. B-tree y LSM

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/01-btree-y-lsm.png|900]]

La biblioteca de la izquierda representa navegación por rangos y páginas. La de la derecha representa acumulación en memoria, archivos ordenados y compactación. Una compactación real puede combinar rangos solapados y versiones de la misma clave; los carteles de la ilustración no especifican niveles ni un algoritmo de particionamiento. WAL, caché, snapshots y concurrencia se explican en las notas.

### Prompt utilizado

```text
Use case: scientific-educational.
Asset type: illustration for Spanish Obsidian study notes on storage engines.
Create one beautifully clear landscape educational editorial illustration, two balanced panels, warm ivory paper, navy typography, teal and amber accents, detailed hand-painted isometric miniature library metaphor.
Main title EXACT: "Dos formas de organizar los datos".
Left title EXACT: "B-tree: buscar y actualizar páginas". Show librarian following a branching catalog toward indexed filing drawers and replacing a card in a drawer. A small blank branching hierarchy icon reinforces tree search. Caption EXACT: "Navegar por rangos hasta la página".
Right title EXACT: "LSM-tree: acumular y fusionar". Show librarian first writing cards at a small desk, next stacking several sorted bundles, then merging them into one ordered shelf. Clear numbered stages 1, 2, 3 and modest arrows indicate this sequence. Caption EXACT: "Memoria → archivos ordenados → compactación".
Bottom full-width small text EXACT: "Analogía visual: ambos usan cachés y pueden necesitar un registro de recuperación."
Make all text highly readable Spanish, only text specified. Concept must not imply LSM is an unordered pile or B-tree rewrites all data. No performance numbers, no charts, no O'Reilly logo, no book-cover recreation. Generous whitespace, visually memorable professional illustrated study guide.
```

## 2. Lectores de distintas versiones

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/02-compatibilidad-lectores.png|900]]

Las flechas van de datos a lector. Apartar un campo desconocido representa un posible mecanismo para tolerarlo; no asegura conservarlo al reescribir ni interpretar correctamente cambios de significado.

### Prompt utilizado

```text
Use case: scientific-educational.
Asset type: illustrated Spanish study mnemonic for database schema evolution.
Create a landscape editorial educational illustration, elegant ivory background, navy headings, teal and amber accents, two large horizontal rows. Not a book cover. Central metaphor: two generations of friendly robot mail readers at a postal desk receiving data envelopes; all typography clear Spanish.
Title EXACT: "Compatibilidad: mira quién lee".
Top row title EXACT: "Hacia atrás". A clearly old beige envelope on LEFT labelled EXACT "Datos antiguos" travels via one large rightward arrow to a modern teal robot reading it on RIGHT labelled EXACT "Lector nuevo". The robot successfully reads. Below row text EXACT: "El lector nuevo entiende lo que ya existía".
Bottom row title EXACT: "Hacia delante". A modern teal envelope on LEFT labelled EXACT "Datos nuevos" travels via one large rightward arrow to an older amber robot reading it on RIGHT labelled EXACT "Lector antiguo". Envelope has a small extra attached field that the robot sets aside gently. Below row text EXACT: "El lector antiguo tolera lo que llegó después".
Footer EXACT: "Depende del formato, del cambio y de las reglas del lector."
Use only these exact labels. Both arrows strictly go from data LEFT to reader RIGHT. Readers are different generations, both visibly reading envelopes. No absolute guarantee icon, no dates, no binary matrix, no garbled extra text, no reused first-edition cover artwork. Delightful memorable hand-painted isometric illustration with professional layout and plenty of space.
```

## 3. Proyección de columnas

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/03-proyeccion-columnas.png|1000]]

Gráfico calculado con **Matplotlib**, no generado con IA. Sus datos son sintéticos: 1 000 000 filas × columnas seleccionadas × 8 bytes. Se guardaron PNG, SVG y el generador Python. El modelo se explica en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/08 Complemento - Coste de proyectar columnas|Coste de proyectar columnas]].

- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/03-proyeccion-columnas.svg|Gráfico en SVG]]
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/generar_grafico_proyeccion.py|Generador reproducible]]

Los diagramas de procesos están escritos en Mermaid dentro de las notas. El mapa navegable usa JSON Canvas.


## Ampliación visual después de la revisión

Se añadieron cuatro ilustraciones con `image_gen`. Todas se inspeccionaron, se guardaron en esta carpeta y se acompañaron de explicación de mecanismos, ejemplos y límites en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/02 Atlas visual explicado|el atlas visual]]. Las analogías no representan una medición de rendimiento ni un protocolo literal.

### Versiones LSM y compactación

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/05-lsm-versiones-y-compactacion.png|900]]

El prompt exacto de esta imagen anterior no quedó conservado. **Registro verificable de la intención:** representar tres estados de `P42` —versión antigua persistida, versión reciente en memoria y salida nueva tras compactación— sin sugerir que el archivo antiguo se reescribe en el sitio.

### Avro y dos esquemas

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/06-avro-dos-esquemas.png|900]]

El prompt exacto de esta imagen anterior no quedó conservado. **Registro verificable de la intención:** mostrar que Avro combina el esquema escritor con el esquema lector para transformar bytes antiguos en la estructura esperada, incluido un campo nuevo con valor por defecto.

### Timeout y tres historias

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/07-timeout-tres-historias.png|900]]

El prompt exacto de esta imagen anterior no quedó conservado. **Registro verificable de la intención:** contrastar tres historias que producen el mismo timeout observado por el cliente —petición no recibida, trabajo todavía en curso y respuesta perdida después del efecto—.

### Índice invertido y vectorial

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/08-indice-invertido-y-vectorial.png|900]]

El prompt exacto de esta imagen anterior no quedó conservado. **Registro verificable de la intención:** comparar un índice invertido, que conecta términos con documentos, con un índice vectorial, que organiza proximidad semántica aproximada; ninguno verifica por sí solo la verdad del resultado.

### Taller LSM: ciclo de una actualización

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/09-lsm-taller-ciclo-actualizacion.png|1000]]

Imagen generada con la herramienta integrada de imágenes y revisada visualmente antes de insertarla. **Resumen del prompt:** representar un taller isométrico en el que una tarjeta `P42` pasa por un diario rojo, una mesa ámbar, losas inmutables y una salida verde; mantener una secuencia espacial clara y evitar texto técnico excesivo dentro de la ilustración.

Su función pedagógica es reunir en una sola cadena causal las responsabilidades de **WAL/log, memtable, flush, SSTables, compactación y publicación**. Los objetos son una analogía: no describen el hardware ni fijan el protocolo exacto de un motor LSM. La correspondencia y sus límites se explican en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/02 LSM SSTables compactación y Bloom|la nota de LSM]] y en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/02 Atlas visual explicado#5. ¿Cómo pasa una actualización LSM de reciente a publicada?|el atlas visual]].

---

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/00 Índice|← Índice de este bloque]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]]
