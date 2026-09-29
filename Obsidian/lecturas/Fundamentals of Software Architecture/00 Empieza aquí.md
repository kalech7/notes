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

Esta carpeta desarrolla en español el material de los **capítulos 1 a 11 presente en tus ocho escaneos**, con explicaciones desde los fundamentos, ejemplos originales, gráficos, diagramas y ejercicios con respuestas. Puedes estudiar directamente aquí; los PDF quedan como referencia para contrastar el texto.

La edición corresponde a *Fundamentals of Software Architecture*, **segunda edición**, de Mark Richards y Neal Ford, publicada por O’Reilly en 2025. La [ficha e índice de la editorial](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/ch01.html) confirman edición, autores y organización.

> [!important] Alcance real de esta guía
> Los tres escaneos iniciales reúnen **73 páginas de PDF**. Los dos siguientes aportan **47 páginas** de los capítulos 6–8 y los dos escaneos nocturnos añaden **35 páginas**, incluida la portada de la Parte II y los capítulos 9–10. El escaneo del capítulo 11 aporta **16 páginas** más. La colección suma **171 páginas de PDF en ocho archivos**. No equivalen al libro completo ni a una secuencia impresa sin huecos. El primer PDF omite las páginas impresas 13–16 y termina en la 35; la 36 tampoco está en el siguiente escaneo. Se documentan estos límites en [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/01 Fuentes y cobertura|Fuentes y cobertura]] y las ampliaciones; la [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/05 Ampliación capítulos 9 y 10|ampliación 9–10]] corresponde a las impresas 131–164 y una portada sin numerar, y la [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/06 Ampliación capítulo 11|ampliación del capítulo 11]] a las impresas 165–180. No se inventa el contenido ausente.

## La pregunta que une los capítulos

**¿Cómo organizo un sistema para que haga lo que el negocio necesita, bajo las condiciones que importan, y pueda cambiar sin que cada modificación se propague a todas sus partes?**

La respuesta se construye gradualmente. Primero hay que entender qué se decide; después, cómo comparar alternativas; luego, cómo agrupar responsabilidades y reconocer dependencias. Se aprende a identificar qué capacidades merecen influir en la estructura y cómo priorizarlas junto con el negocio. Los capítulos 6–8 añaden cómo medirlas y gobernarlas, delimitar su alcance e identificar componentes que puedan evolucionar. Los capítulos 9–10 conectan ese análisis con la partición técnica o por dominio, los costes de distribución, los equipos y el estilo de arquitectura por capas. El capítulo 11 invierte esa partición: mantiene un solo despliegue, pero organiza el código por dominios en el monolito modular.

![modularidad](Recursos%20visuales/03-modularidad.png)

*Ilustración original: una aplicación puede tener módulos claros dentro de un despliegue; separar despliegues exige gestionar comunicación y datos; una distribución mal delimitada puede conservar una coordinación excesiva. La imagen es una analogía, no una clasificación basada únicamente en contar cables o bases de datos.*

## Estudiar por capítulos

Cada capítulo tiene su propia carpeta, un **00 Índice** y notas cortas numeradas por tema. Los capítulos 1–5 reúnen **37 notas de estudio**; los capítulos 6–8 añaden **25 notas temáticas**, tres índices y un laboratorio integrador. Los capítulos 9–10 añaden **17 notas temáticas**, dos índices y un atlas con práctica transversal. El capítulo 11 añade **nueve notas temáticas** y su índice. Abre un índice y sigue **Siguiente**; las imágenes y las fórmulas aparecen en la nota que las explica.

| Capítulo | Pregunta central | Lo que aprenderás a hacer |
|---|---|---|
| [[Obsidian/lecturas/Fundamentals of Software Architecture/01 Introducción/00 Índice\|1 · Introducción]] | ¿Qué es arquitectura y de qué responde un arquitecto? | Relacionar características, componentes, estilo y decisiones; aplicar las tres leyes y las ocho expectativas |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/02 Pensamiento arquitectónico/00 Índice\|2 · Pensamiento arquitectónico]] | ¿Cómo se piensa antes de elegir? | Reconocer el espectro diseño/arquitectura, ampliar criterio, comparar compensaciones y evitar cuellos de botella |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/03 Modularidad/00 Índice\|3 · Modularidad]] | ¿Qué debe estar junto y qué debe separarse? | Interpretar cohesión, acoplamiento, LCOM, abstracción, inestabilidad, distancia y las nueve connascencias |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/04 Características arquitectónicas/00 Índice\|4 · Características arquitectónicas]] | ¿Qué capacidades determinan el éxito? | Distinguir familias de características y medir escenarios de rendimiento, escala, disponibilidad y recuperación |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/05 Identificar y priorizar características/00 Índice\|5 · Identificación y priorización]] | ¿Cómo extraer esas capacidades del negocio? | Trabajar la kata Silicon Sandwiches, separar supuestos, completar una hoja de trabajo y acordar prioridades |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice\|6 · Medición y gobierno]] | ¿Cómo comprobar y proteger una característica? | Definir métricas, calcular complejidad y diseñar funciones de aptitud |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice\|7 · Alcance y quanta]] | ¿A qué parte del sistema se aplica cada capacidad? | Identificar dependencias, delimitar quanta y analizar Going Green |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice\|8 · Pensamiento basado en componentes]] | ¿Cómo encontrar y refinar responsabilidades? | Separar vistas lógica y física, asignar historias, aplicar Demeter y resolver Going, Going, Gone |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/00 Índice\|9 · Fundamentos de estilos]] | ¿Qué consecuencias tiene organizar y distribuir el sistema? | Distinguir estilo y patrón, elegir partición, reconocer once falacias y relacionar equipos con arquitectura |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/00 Índice\|10 · Arquitectura por capas]] | ¿Qué protege cada capa y qué costes introduce? | Distinguir capas y despliegue, gobernar aperturas, detectar sumideros y evaluar cuándo usar el estilo |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/00 Índice\|11 · Monolito modular]] | ¿Cómo separar por negocio sin distribuir? | Distinguir sus dos estructuras, controlar la comunicación entre módulos, gobernar fronteras y decidir cuándo usarlo |

Cada capítulo tiene explicaciones causales, referencias al escaneo, diagramas interpretados y preguntas con soluciones plegables. **PedidoClaro** es nuestro ejemplo inventado de una tienda de sándwiches; **Silicon Sandwiches**, **Going Green** y **Going, Going, Gone** son casos del libro, con problemas distintos. Sus nombres y cifras no deben confundirse.

## Ruta de estudio sugerida

1. Lee el capítulo 1 y explica una decisión usando las cuatro dimensiones. Después cambia una restricción: presupuesto, equipo o carga. Observa si conservarías la misma decisión.
2. En el capítulo 2, elige dos alternativas y escribe también sus costos. «Depende» debe continuar con condiciones concretas y evidencia por conseguir.
3. Divide el capítulo 3 en tres sesiones: límites y cohesión; métricas calculadas; connascencia y refactorización. Reproduce los cálculos antes de mirar las respuestas.
4. Estudia el capítulo 4 definiendo operación, carga, entorno y umbral para cada característica. «Rápido» y «seguro» solos no permiten verificar una arquitectura.
5. Resuelve la kata del capítulo 5 antes de leer su análisis. Compara por qué priorizaste cada capacidad, sin asumir que existe una única estructura correcta.
6. Continúa por los capítulos 6–8: formula una medición objetiva, dibuja su alcance y revisa las responsabilidades de sus componentes. Cada gráfico nuevo va acompañado de su explicación y una referencia a la figura del libro cuando corresponde.
7. Resuelve el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/05 Laboratorio de componentes quanta y gobierno|laboratorio de componentes, quanta y gobierno]] para conectar los tres capítulos nuevos.
8. Estudia los capítulos 9–10 y resuelve el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/06 Atlas y práctica de estilos y capas|atlas y laboratorio de estilos y capas]]: compara alternativas antes de decidir distribuir o abrir una capa.
9. Estudia el [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/00 Índice|capítulo 11]] y resuelve su laboratorio: decide, con datos de cambios reales, entre capas y monolito modular, y escribe las reglas que protegen sus módulos.
10. Completa también el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/02 Laboratorio integrador|laboratorio integrador]] y usa el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/03 Glosario y repaso|glosario]] para localizar dudas.

Para repasar visualmente, abre el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/01 Atlas visual explicado|atlas visual]]. El atlas de los capítulos 1–5 reúne 33 imágenes PNG: seis ilustraciones, siete gráficos y veinte diagramas, insertados en los capítulos con sus explicaciones. Cada composición del atlas se explica junto con sus límites de interpretación. Los gráficos de los capítulos 6–8 se guardan en `Recursos visuales/Capítulos 6 a 8` y aparecen junto a la explicación de cada tema; su [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/04 Ampliación capítulos 6 a 8|mapa de cobertura]] permite volver a las figuras del escaneo. Los diagramas conservan sus fuentes editables. Los capítulos 9–10 añaden ocho PNG explicados y diagramas Mermaid dentro de las notas; el capítulo 11, otros ocho PNG en `Recursos visuales/Capítulo 11`. El [README](README.md) ofrece navegación compatible con GitHub.

Si prefieres aprender el proceso completo antes de volver a los detalles, usa el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/04 Método completo para tomar decisiones|método de decisión de principio a fin]]. Integra los capítulos 1–5 mediante un flujo visual, una comparación de alternativas y un caso resuelto sin presentar una arquitectura como respuesta universal.

## Material de apoyo y fuentes

- [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/00 Índice|Apoyo y repaso]]: método integrador, atlas, laboratorio y glosario.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/00 Índice|Fuentes y revisión]]: cobertura, procedencia y prompts.
- **Recursos visuales:** archivos de imágenes, diagramas y generadores.
- **Materiales:** copias de los ocho PDF.

## Cómo distinguir procedencias

- **Base del libro:** conceptos y ejemplos identificados con páginas del PDF.
- **Elaboración propia:** analogías, gráficos, cálculos, ejercicios y ampliaciones para hacer comprensible el mecanismo.
- **Supuesto didáctico:** números y requisitos inventados para resolver un ejemplo; requieren validación antes de utilizarlos en un proyecto real.
- **Matiz técnico:** precisión necesaria cuando una afirmación del ejemplo depende de una implementación o cuando una métrica admite varias convenciones.

La meta es poder explicar **qué propiedad intentas proteger, qué decisión la favorece, qué costo introduce y qué observación te haría revisarla**.
