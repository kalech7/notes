---
title: "DDIA — Coste de proyectar columnas"
created: 2026-09-25
tags:
  - lecturas/ddia
  - almacenamiento-columnar
---

# DDIA — Coste de proyectar columnas

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/00 Índice|Almacenamiento y recuperación]]

La nota de almacenamiento columnar afirma que pedir menos columnas puede mover menos bytes. Este complemento aísla esa variable con números para mostrar cuánto contenido de valores cambia y, al mismo tiempo, por qué ese cociente no predice la latencia total.

> [!info] Recuerda antes
> - **Proyectar** es elegir columnas; no significa filtrar filas ni predecir cuánto tardará la consulta.
> - La organización columnar permite omitir columnas solo si el formato y el lector aprovechan esa disposición.
> - Bytes de valores, bytes leídos y tiempo de respuesta son magnitudes relacionadas, pero no equivalentes.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/03-proyeccion-columnas.png|1000]]

El gráfico muestra un **cálculo sintético de contenido de valores**, no resultados medidos en una base de datos. Sirve para entender por qué una consulta analítica puede beneficiarse de leer únicamente las columnas que utiliza. *Proyectar* significa escoger columnas del resultado; el lector necesita poder aprovechar esa selección para evitar trabajo físico.

## Supuestos y cálculo

Imagina un millón de filas, veinte columnas y ocho bytes por valor, todos de tamaño fijo. La comparación conserva todas las filas: no hay filtro que descarte registros.

- Filas completas: `1 000 000 × 20 × 8 = 160 000 000 bytes = 160 MB`.
- Dos columnas: `1 000 000 × 2 × 8 = 16 000 000 bytes = 16 MB`.
- Cinco columnas: `40 MB`; diez columnas: `80 MB`.

Usamos MB **decimales**: un MB equivale a un millón de bytes. Leer dos de veinte columnas corresponde al 10 % del contenido; la diferencia es el 90 %. No significa que la consulta dure un 90 % menos.

## Qué queda fuera del modelo

El cálculo excluye metadatos, compresión, encabezados, representación de nulos y estructuras auxiliares. Tampoco modela páginas, caché, red, CPU ni filtros. La columna usada para filtrar puede necesitar leerse aunque no aparezca en el resultado.

La barra gris supone recuperar filas completas. Un motor por filas con un índice que cubra la consulta puede evitar parte de ese trabajo; una consulta columnar tampoco lee necesariamente exactamente los bytes calculados. Las barras representan el contenido ideal necesario bajo estos supuestos, no una garantía universal sobre E/S real.

> [!tip] Para recordar
> **Menos columnas necesarias → menos contenido potencialmente leído.** El ahorro real depende del formato, el lector, los índices y la consulta.

**Pregunta de repaso:** si solicitas las veinte columnas, ¿cuánto ahorro por proyección queda? Ninguno en este modelo; otras ventajas o costos requieren otro análisis.

Conecta con [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/01 Caso práctico de pedidos a analítica|el caso de pedidos a analítica]] y [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|la ruta de lectura]].

Generador reproducible: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/generar_grafico_proyeccion.py|script Python]]; versión vectorial: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/03-proyeccion-columnas.svg|SVG]]. Requiere `matplotlib`.

---

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/00 Índice|← Índice de este bloque]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/05 Almacenamiento columnar y compresión|Volver a columnas y compresión]]
