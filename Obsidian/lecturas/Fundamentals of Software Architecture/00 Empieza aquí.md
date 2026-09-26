---
title: "Fundamentals of Software Architecture · 2.ª edición · Guía de estudio"
created: 2026-09-25
autores:
  - Mark Richards
  - Neal Ford
edicion: 2
tags:
  - lecturas/software-architecture
  - indice
---

# Fundamentals of Software Architecture · 2.ª edición

[[Obsidian/lecturas/00 Índice de lecturas|← Biblioteca de lecturas]]

Esta carpeta desarrolla en español el material de los **capítulos 1 a 5 presente en tus tres escaneos**, con explicaciones desde los fundamentos, ejemplos originales, gráficos, diagramas y ejercicios con respuestas. Puedes estudiar directamente aquí; los PDF quedan como referencia para contrastar el texto.

La edición corresponde a *Fundamentals of Software Architecture*, **segunda edición**, de Mark Richards y Neal Ford, publicada por O’Reilly en 2025. La [ficha e índice de la editorial](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/ch01.html) confirman edición, autores y organización.

> [!important] Alcance real de esta guía
> Se revisaron las **73 páginas de PDF** que compartiste. No equivalen al libro completo ni a una secuencia impresa sin huecos. El primer PDF omite las páginas impresas 13–16 y termina en la 35; la 36 tampoco está en el siguiente escaneo. Se documentan estos límites en [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/01 Fuentes y cobertura|Fuentes y cobertura]]. No se inventa el contenido ausente.

## La pregunta que une los cinco capítulos

**¿Cómo organizo un sistema para que haga lo que el negocio necesita, bajo las condiciones que importan, y pueda cambiar sin que cada modificación se propague a todas sus partes?**

La respuesta se construye gradualmente. Primero hay que entender qué se decide; después, cómo comparar alternativas; luego, cómo agrupar responsabilidades y reconocer dependencias. Finalmente se aprende a identificar qué capacidades merecen influir en la estructura y cómo priorizarlas junto con el negocio.

![modularidad](Recursos%20visuales/03-modularidad.png)

*Ilustración original: una aplicación puede tener módulos claros dentro de un despliegue; separar despliegues exige gestionar comunicación y datos; una distribución mal delimitada puede conservar una coordinación excesiva. La imagen es una analogía, no una clasificación basada únicamente en contar cables o bases de datos.*

## Estudiar por capítulos

Cada capítulo tiene su propia carpeta, un **00 Índice** y notas cortas numeradas por tema. En total son **37 notas de estudio**. Abre un índice y sigue **Siguiente**; las imágenes y las fórmulas aparecen en la nota que las explica.

| Capítulo | Pregunta central | Lo que aprenderás a hacer |
|---|---|---|
| [[Obsidian/lecturas/Fundamentals of Software Architecture/01 Introducción/00 Índice\|1 · Introducción]] | ¿Qué es arquitectura y de qué responde un arquitecto? | Relacionar características, componentes, estilo y decisiones; aplicar las tres leyes y las ocho expectativas |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/02 Pensamiento arquitectónico/00 Índice\|2 · Pensamiento arquitectónico]] | ¿Cómo se piensa antes de elegir? | Reconocer el espectro diseño/arquitectura, ampliar criterio, comparar compensaciones y evitar cuellos de botella |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/03 Modularidad/00 Índice\|3 · Modularidad]] | ¿Qué debe estar junto y qué debe separarse? | Interpretar cohesión, acoplamiento, LCOM, abstracción, inestabilidad, distancia y las nueve connascencias |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/04 Características arquitectónicas/00 Índice\|4 · Características arquitectónicas]] | ¿Qué capacidades determinan el éxito? | Distinguir familias de características y medir escenarios de rendimiento, escala, disponibilidad y recuperación |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/05 Identificar y priorizar características/00 Índice\|5 · Identificación y priorización]] | ¿Cómo extraer esas capacidades del negocio? | Trabajar la kata Silicon Sandwiches, separar supuestos, completar una hoja de trabajo y acordar prioridades |

Cada capítulo tiene explicaciones causales, referencias al escaneo, diagramas interpretados y preguntas con soluciones plegables. **PedidoClaro** es nuestro ejemplo inventado de una tienda de sándwiches; **Silicon Sandwiches** es la kata que aparece en el libro. Sus nombres y cifras no deben confundirse.

## Ruta de estudio sugerida

1. Lee el capítulo 1 y explica una decisión usando las cuatro dimensiones. Después cambia una restricción: presupuesto, equipo o carga. Observa si conservarías la misma decisión.
2. En el capítulo 2, elige dos alternativas y escribe también sus costos. «Depende» debe continuar con condiciones concretas y evidencia por conseguir.
3. Divide el capítulo 3 en tres sesiones: límites y cohesión; métricas calculadas; connascencia y refactorización. Reproduce los cálculos antes de mirar las respuestas.
4. Estudia el capítulo 4 definiendo operación, carga, entorno y umbral para cada característica. «Rápido» y «seguro» solos no permiten verificar una arquitectura.
5. Resuelve la kata del capítulo 5 antes de leer su análisis. Compara por qué priorizaste cada capacidad, sin asumir que existe una única estructura correcta.
6. Termina con el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/02 Laboratorio integrador\|laboratorio integrador]] y usa el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/03 Glosario y repaso\|glosario]] para localizar dudas.

Para repasar visualmente, abre el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/01 Atlas visual explicado|atlas visual]]. La carpeta contiene 32 imágenes PNG: cinco ilustraciones, siete gráficos y veinte diagramas, insertados en los capítulos con sus explicaciones. Cada composición del atlas tiene una lectura guiada y límites de interpretación. Los diagramas conservan sus fuentes editables. El [README](README.md) ofrece navegación compatible con GitHub.

## Material de apoyo y fuentes

- [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/00 Índice|Apoyo y repaso]]: atlas, laboratorio y glosario.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/00 Índice|Fuentes y revisión]]: cobertura, procedencia y prompts.
- **Recursos visuales:** archivos de imágenes, diagramas y generadores.
- **Materiales:** copias de los tres PDF.

## Cómo distinguir procedencias

- **Base del libro:** conceptos y ejemplos identificados con páginas del PDF.
- **Elaboración propia:** analogías, gráficos, cálculos, ejercicios y ampliaciones para hacer comprensible el mecanismo.
- **Supuesto didáctico:** números y requisitos inventados para resolver un ejemplo; requieren validación antes de utilizarlos en un proyecto real.
- **Matiz técnico:** precisión necesaria cuando una afirmación del ejemplo depende de una implementación o cuando una métrica admite varias convenciones.

La meta es poder explicar **qué propiedad intentas proteger, qué decisión la favorece, qué costo introduce y qué observación te haría revisarla**.
