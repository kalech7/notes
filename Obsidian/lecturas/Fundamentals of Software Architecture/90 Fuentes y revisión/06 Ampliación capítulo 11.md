---
title: "Ampliación y cobertura · capítulo 11"
created: 2026-09-29
tags:
  - lecturas/software-architecture
  - fuentes
---

# Fuentes y cobertura del capítulo 11

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]]

Esta ampliación documenta el escaneo del capítulo 11, «The Modular Monolith Architecture Style». Las notas explican el capítulo completo en español con ejemplos, cálculos, imágenes y diagramas propios, de modo que pueda estudiarse sin leer el original.

## Archivo y numeración

| Original | Copia en la colección | Páginas PDF | Páginas impresas |
|---|---|---|---|
| CamScanner 2026-09-28 23.32.pdf | [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/08 Monolito modular.pdf\|08 Monolito modular]] | 1–16 | 165–180, capítulo 11 completo |

**Página impresa = página PDF + 164.** Las páginas PDF 8, 9, 13, 14 y 15 están escaneadas en horizontal y se leyeron girándolas; la numeración impresa de la 170 y la 176 no es visible en el escaneo, pero la secuencia es continua. Con este archivo, la colección suma **ocho PDF y 171 páginas de PDF**.

## Mapa de contenido

| Pasaje | Tema | Nota |
|---|---|---|
| PDF 1–2 · impresas 165–166 | Origen del estilo, topología, figura 11-1, namespaces técnicos frente a de dominio | 01 |
| PDF 2–4 · impresas 166–168 | Estructura monolítica (figura 11-2) y estructura modular (figura 11-3) | 02 |
| PDF 4–6 · impresas 168–170 | Comunicación punto a punto (figura 11-4), JAR/DLL Hell y mediador (figura 11-5) | 03 |
| PDF 6–7 · impresas 170–171 | Topologías de datos (figura 11-6), nube y riesgos comunes | 04 |
| PDF 8–10 · impresas 172–174 | Gobierno automatizado, herramientas y ejemplos 11-1 a 11-4 | 05 |
| PDF 10–11 · impresas 174–175 | Equipos por dominio y los cuatro tipos de equipo | 06 |
| PDF 11–13 · impresas 175–177 | Ficha de características (figura 11-7), cuándo usarlo y cuándo no | 07 |
| PDF 13–16 · impresas 177–180 | Caso EasyMeals (figura 11-8), módulos y componentes | 08 |

Entrada: [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/00 Índice|Capítulo 11]].

## Precisiones sobre la fuente

**Namespaces de la figura 11-2.** Los rótulos dibujados usan `com.orderentry.placement` y `com.orderentry.payment`; la lista del texto y los ejemplos de gobierno usan `orderplacement` y `paymentprocessing`. Las notas adoptan la versión de la lista.

**Testabilidad frente a capas.** El texto de la impresa 175 dice que desplegabilidad y testabilidad puntúan algo más alto que en la arquitectura por capas. Las figuras 10-6 y 11-7 muestran que la desplegabilidad sube de una a dos estrellas, pero la testabilidad tiene dos en ambos estilos. Ambas figuras se verificaron ampliando el escaneo.

**Modularidad como fortaleza.** El texto la presenta como fortaleza principal y la ficha le da dos estrellas. Las notas explican la diferencia como modularidad lógica frente a modularidad comparada con estilos distribuidos, e indican que esa interpretación es propia.

**Ejemplo 11-3.** El título habla del total por módulo, el comentario del total del sistema y el pseudocódigo calcula totales por archivo sin acumularlos; también contiene errores de sintaxis. La nota de gobierno conserva la intención (limitar el acoplamiento de cada módulo) y ofrece una versión consistente.

**Erratas menores.** El ejemplo 11-2 escribe `namepace`; la frase de la impresa 178 sobre las interfaces de EasyMeals repite «through» y se interpreta con ayuda de la figura 11-8.

## Imágenes y diagramas propios

Ocho PNG en `Recursos visuales/Capítulo 11`, generados por `generar_diagramas.py` (Pillow): namespaces, estructuras, comunicación, topologías de datos, conteo de dependencias, comparación de estrellas, EasyMeals y componentes por módulo. La paleta del gráfico de estrellas se validó para daltonismo y contraste. Además, las notas incluyen ocho diagramas Mermaid (flujos, secuencias y decisiones). Todas las explicaciones de imágenes están redactadas como texto directo.

## Validación

Validación del 29 de septiembre: los 382 wikilinks y 488 enlaces Markdown de la guía resuelven; las anclas `#page=` del PDF 08 no superan sus 16 páginas; las diez notas del capítulo tienen YAML válido con `title`, `created`, `capitulo` y `tags`; los ocho bloques Mermaid se renderizan sin errores; las ocho imágenes se revisaron visualmente y ninguna explicación usa rótulos del tipo «cómo leerlo».
