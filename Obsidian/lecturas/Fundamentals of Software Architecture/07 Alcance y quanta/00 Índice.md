---
title: "07 · Alcance y quanta · Capítulo 7"
created: 2026-09-28
capitulo: 7
tags:
  - lecturas/software-architecture
---

# Capítulo 7 · Alcance de las características y quanta

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]]

**Idea central:** una característica arquitectónica necesita un alcance explícito. Un quantum ayuda a delimitar una unidad coherente con sus dependencias; después hay que analizar también cómo interactúa con las demás.

Este capítulo contiene **7 notas detalladas**, **9 gráficos PNG**, con explicación de elementos, flechas, conclusiones y límites. Los gráficos mantienen cajas, cilindros, conexiones y contornos como los del libro, con rótulos en español.

## Orden de lectura

| Nota | Lo que podrás explicar |
|---|---|
| [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/01 El alcance de las características\|01 El alcance de las características]] | Por qué una propiedad del código no garantiza una propiedad del sistema. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/02 Anatomía de un quantum\|02 Anatomía de un quantum]] | Qué incluye un quantum y por qué no equivale a un servicio. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/03 Cuatro formas de acoplamiento\|03 Cuatro formas de acoplamiento]] | Cómo distinguir semántica, implementación, estructura e interacción. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/04 Sincronía colas y límites operacionales\|04 Sincronía colas y límites operacionales]] | Cómo se propagan las restricciones y qué consigue una cola. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/05 Del alcance al estilo arquitectónico\|05 Del alcance al estilo arquitectónico]] | Cómo orientar estilo, quanta, persistencia y comunicación. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/06 Going Green explicado paso a paso\|06 Going Green explicado paso a paso]] | Por qué Going Green agrupa siete servicios en tres quanta. |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/07 Nube aplicación y repaso\|07 Nube aplicación y repaso]] | Cómo incluir la nube y comprobar la comprensión con ejercicios. |

## Procedencia y cobertura

**Fuente:** Mark Richards y Neal Ford, *Fundamentals of Software Architecture*, segunda edición. Escaneo «CamScanner 2026-09-28 15.56.pdf», **PDF pp. 1–12 / impresas 95–106**. La copia local es [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Ese archivo contiene también el capítulo 8 a partir de PDF p. 13 / impresa 107.

| Páginas PDF | Impresas | Contenido cubierto |
|---|---|---|
| 1–3 | 95–97 | Necesidad de alcance, definición, despliegue, cohesión y contexto delimitado. |
| 4–5 | 98–99 | Acoplamiento semántico, de implementación, estático y dinámico. |
| 5–6 | 99–100 | Sincronía, Subastas/Pagos y amortiguación mediante cola. |
| 7–9 | 101–103 | Figuras 7-1 a 7-4: estilo, quanta, persistencia y comunicación. |
| 9–11 | 103–105 | Kata Going Green; figuras 7-5, 7-6 y 7-7. |
| 11–12 | 105–106 | Alcance y recursos de nube. |

## Correspondencia de las figuras

| Figura del libro | Recurso de estas notas | Tratamiento |
|---|---|---|
| 7-1, 7-2, 7-3, 7-4 | `c07-03-decision-estilo.png` | Redibujo conceptual combinado en español; conserva la secuencia y la notación, simplifica el número de cajas. |
| 7-5 | `c07-04-going-green-flujo.png` | Redibujo del flujo con numeración didáctica. |
| 7-6 | `c07-05-going-green-prioridades.png` | Redibujo de los tres grupos y sus prioridades. |
| 7-7 | `c07-06-going-green-quanta.png` | Conserva siete servicios, tres bases y tres límites. |
| Sin figura equivalente | `c07-01-limites.png`, `c07-02-sincronia-cola.png` y `c07-07` a `c07-09` | Diagramas didácticos originales basados en el texto. |

Los PNG y el archivo editable `c07-graficos.py` están en **Recursos visuales/Capítulos 6 a 8**. El script usa Pillow para regenerar las imágenes. Los tres diagramas adicionales conservan también su lógica en fuentes `.mmd` editables, y se insertan como PNG para no depender del renderizador Mermaid. No son capturas exactas ni se presentan como figuras originales del libro: son redibujos explicativos. El PDF permite contrastarlos con el material suministrado.

> [!important] Precisión conceptual de esta edición
> Se admite comunicación síncrona entre quanta. No se aplica la regla automática «una llamada síncrona = un solo quantum». Se distinguen el límite de la unidad y las dependencias operacionales del recorrido; el capítulo señala que la comunicación puede exigir revisar los límites en algunos sistemas.

## Cómo estudiar los gráficos

Primero identifica qué representan las cajas y qué significa cada flecha. Después explica el recorrido y el resultado. Finalmente comprueba qué no demuestra el dibujo. Un flujo físico del negocio, una dependencia de datos y una llamada de red tienen significados distintos aunque todos puedan representarse mediante líneas.

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/01 El alcance de las características|Comenzar el capítulo →]]
