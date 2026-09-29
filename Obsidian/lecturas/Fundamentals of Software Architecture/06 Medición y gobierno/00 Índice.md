---
title: "06 · Medición y gobierno de características arquitectónicas"
created: 2026-09-28
tags:
  - lecturas/software-architecture
---

# Capítulo 6 · Medición y gobierno de características arquitectónicas

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]]

La pregunta de este capítulo es **cómo convertir cualidades deseadas en evidencia verificable y conservarlas mientras el software cambia**. Las ocho notas desarrollan los mecanismos, sus límites, ejemplos calculados y ejercicios. Incluyen nueve gráficos PNG con fuentes SVG editables: cuatro recrean las figuras del libro y cinco amplían su explicación.

## Recorrido recomendado

| Nota | Qué podrás explicar |
|---|---|
| [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/01 De características a medidas\|01 De características a medidas]] | De características arquitectónicas a medidas compartidas. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/02 Medidas operativas y rendimiento\|02 Medidas operativas y rendimiento]] | Medidas operativas: promedios, colas y presupuestos. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/03 Complejidad ciclomática\|03 Complejidad ciclomática]] | Medidas estructurales y complejidad ciclomática. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/04 Medidas de proceso y testabilidad\|04 Medidas de proceso y testabilidad]] | Proceso: testabilidad, cobertura y desplegabilidad. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/05 Gobierno y funciones de aptitud\|05 Gobierno y funciones de aptitud]] | Gobierno arquitectónico y funciones de aptitud. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/06 Ciclos y distancia a la secuencia principal\|06 Ciclos y distancia a la secuencia principal]] | Gobernar modularidad: ciclos y distancia a la secuencia principal. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/07 Capas y reglas de dependencia\|07 Capas y reglas de dependencia]] | Gobernar capas: del dibujo a una regla ejecutable. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/08 Gobierno en operación y práctica integradora\|08 Gobierno en operación y práctica integradora]] | Gobierno en operación, ingeniería del caos y práctica integradora. |

## Procedencia y cobertura

Fuente: *Fundamentals of Software Architecture*, segunda edición, Mark Richards y Neal Ford, capítulo 6, **páginas impresas 81–93**. El archivo original «CamScanner 2026-09-28 15.53.pdf» contiene 13 páginas consecutivas. Se conserva en [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf|Materiales/04 Medición y gobierno.pdf]]. En este archivo, **página impresa = página del PDF + 80**.

| PDF | Impresas | Contenido cubierto |
|---|---|---|
| 1–2 | 81–82 | Ambigüedad, definiciones compartidas, características compuestas y operación |
| 3 | 83 | Presupuestos de rendimiento, bytes y medidas estructurales |
| 4–5 | 84–85 | Complejidad ciclomática, figura 6-1 y límites de los umbrales |
| 6–7 | 86–87 | Medidas de proceso, gobierno y definición de fitness functions |
| 8–9 | 88–89 | Figuras 6-2 y 6-3, mecanismos y detección de ciclos |
| 10–11 | 90–91 | Distancia a la secuencia principal, capas, figura 6-4 y ArchUnit |
| 12–13 | 92–93 | NetArchTest, manipulación de métricas, caos, gobierno operativo y listas |

No faltan páginas dentro del tramo 81–93 proporcionado. El escaneo tiene márgenes recortados y OCR imperfecto; las cuatro figuras y sus ejemplos relevantes se contrastaron visualmente. Las referencias a otros capítulos no implican que aquí se reconstruya material no recibido.

## Atlas de las figuras

| Figura del libro | Recreación y explicación | Qué se conserva o se aclara |
|---|---|---|
| 6-1, p. 84 | [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/03 Complejidad ciclomática\|Complejidad ciclomática]] | Condiciones y tres salidas; grafo completo con conteo coherente y precisión sobre erratas |
| 6-2, p. 88 | [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/05 Gobierno y funciones de aptitud\|Mecanismos de fitness functions]] | Círculos superpuestos y mismas familias de mecanismos |
| 6-3, p. 89 | [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/06 Ciclos y distancia a la secuencia principal\|Dependencias cíclicas]] | Triángulo de tres componentes con dependencias mutuas |
| 6-4, p. 91 | [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/07 Capas y reglas de dependencia\|Capas y reglas]] | Bloque de cuatro capas y base de datos; relaciones permitidas explicadas aparte |

Cada figura tiene una guía que explica cajas o ejes, significado de las flechas cuando existen, secuencia causal, conclusión y límites. Los PNG se visualizan directamente en Obsidian; los SVG del mismo nombre permiten editar líneas y rótulos sin depender de una generación de imágenes.

> [!note] Separar fuente y elaboración
> Las figuras son recreaciones pedagógicas, no facsímiles. Los casos numéricos, la plantilla de medición, los percentiles, el gráfico de distancia y PedidoClaro son ampliaciones o supuestos señalados. Las herramientas y métricas nombradas por el libro se explican en su contexto, sin afirmar que sus API o su vigencia actual hayan sido verificadas.

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/01 De características a medidas|Comenzar →]]
