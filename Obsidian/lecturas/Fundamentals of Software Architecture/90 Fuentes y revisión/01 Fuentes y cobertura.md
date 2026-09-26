---
title: "Fuentes, cobertura y límites · Fundamentals of Software Architecture 2.ª edición"
created: 2026-09-25
tags:
  - lecturas/software-architecture
  - fuentes
---

# Fuentes, cobertura y límites

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Fuentes y revisión](00%20%C3%8Dndice.md)

## Edición y materiales

Se trabaja la **segunda edición** de *Fundamentals of Software Architecture*, de **Mark Richards y Neal Ford**, O’Reilly, 2025. El [índice oficial de la segunda edición](https://www.oreilly.com/library/view/fundamentals-of-software/9781098175504/ch01.html) se utilizó para confirmar edición, autores y nombres de capítulos. El contenido principal de esta guía procede de los archivos facilitados por el usuario, no de una edición distinta.

| Archivo original | Copia conservada en la carpeta | Páginas del PDF | Contenido presente |
|---|---|---:|---|
| CamScanner 2026-09-25 21.32.pdf | [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/01 Introducción y pensamiento arquitectónico.pdf\|01 Introducción y pensamiento arquitectónico]] | 31 | Introducción y pensamiento arquitectónico |
| CamScanner 2026-09-25 21.35.pdf | [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf\|02 Modularidad]] | 18 | Modularidad |
| CamScanner 2026-09-25 21.37.pdf | [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/03 Características e identificación.pdf\|03 Características e identificación]] | 24 | Definición e identificación de características |

Se conservaron copias de los originales sin modificar su contenido. **31 + 18 + 24 = 73 páginas de PDF.** La extracción inicial solo mostraba la marca de CamScanner, por lo que se recurrió a reconocimiento óptico y revisión visual. Se corrigió la orientación para interpretar páginas problemáticas; la numeración de las referencias sigue siendo la del PDF original.

## Numeración y huecos

| Tramo del PDF | Correspondencia impresa |
|---|---|
| 21.32, páginas 1–9 | 1–9 |
| 21.32, página 10 | 11 |
| 21.32, página 11 | 10 |
| 21.32, página 12 | 12 |
| 21.32, páginas 13–31 | 17–35; sumar 4 |
| 21.35, páginas 1–18 | 37–54; sumar 36 |
| 21.37, páginas 1–11 | 55–65; sumar 54 |
| 21.37, páginas 12–24 | 67–79; sumar 55 |

No aparecen las páginas impresas **13–16, 36 y 66** en estos archivos. No se presupone que todos esos huecos contengan texto ni que sean todos páginas en blanco. No se reconstruyen ni se incluyen como páginas revisadas. Por tanto, la expresión «capítulos 1 a 5» describe la organización del material recibido, **no una afirmación de integridad de los cinco capítulos originales**. Tampoco se cubren los capítulos 6 en adelante; las ampliaciones sobre medición, ADR o reintentos se identifican como tales.

## Matriz de cobertura del material disponible

Cada fila ubica un bloque del escaneo y dónde se desarrolla. Los capítulos se distribuyen ahora en 37 notas temáticas dentro de cinco carpetas; los números de sección se conservan en los encabezados de las notas. Las secciones de alcance y referencias generales están en el índice de cada capítulo. Las figuras originales de la guía son reinterpretaciones didácticas, no copias gráficas del libro.

| Fuente y páginas de PDF | Ideas verificadas | Desarrollo |
|---|---|---|
| 21.32 · 1–2 | Contexto del rol, arquitectura accidental, costos históricos y definición | Cap. 1, secciones 1–2 |
| 21.32 · 3–6 | Características, componentes, estilos y decisiones; estructura | Cap. 1, sección 2; atlas 1 |
| 21.32 · 6–8 | Tres leyes y dos corolarios | Cap. 1, sección 3 |
| 21.32 · 8–9 | Decisiones, análisis continuo y actualización tecnológica | Cap. 1, sección 4 |
| 21.32 · 10–12 | Dominio, liderazgo, cumplimiento, diversidad técnica y política | Cap. 1, sección 4 |
| 21.32 · 13–15 | Arquitectura y diseño como espectro; estrategia, esfuerzo y compensaciones | Cap. 2, sección 1 |
| 21.32 · 16–19 | Amplitud, profundidad y mantenimiento del conocimiento | Cap. 2, sección 2 |
| 21.32 · 20–21 | Frozen Caveman, regla de veinte minutos y aprendizaje | Cap. 2, sección 3 |
| 21.32 · 21–25 | Burbujas, portafolio y radar personal: cuatro cuadrantes y cuatro anillos | Cap. 2, secciones 3–4 |
| 21.32 · 26–29 | Subastas, colas, temas, contratos y análisis de costos | Cap. 2, sección 5; atlas 2 |
| 21.32 · 29–31 | Objetivos de negocio, programación, cuello de botella, POC, deuda, bugs, automatización y revisión | Cap. 2, secciones 6–7 |
| 21.35 · 1–4 | Modularidad, granularidad, módulos, separación lógica/física, historia y namespaces | Cap. 3, sección 1 |
| 21.35 · 5–6 | Siete cohesiones y ejemplo Customer/Order | Cap. 3, sección 2 |
| 21.35 · 7–8 | LCOM, variantes, ejemplos y límites | Cap. 3, sección 3; atlas 5 |
| 21.35 · 8–9 | Acoplamiento entrante y saliente | Cap. 3, sección 4 |
| 21.35 · 9–12 | A, I, D, secuencia principal, zonas y límites de métricas | Cap. 3, sección 5; atlas 4 |
| 21.35 · 13–14 | Connascencia estática: nombre, tipo, significado, posición y algoritmo | Cap. 3, sección 6 |
| 21.35 · 14–15 | Connascencia dinámica: ejecución, tiempo, valores e identidad | Cap. 3, sección 6 |
| 21.35 · 15–17 | Fuerza, localidad, grado y guías de refactorización | Cap. 3, sección 6 |
| 21.35 · 18 | De módulos a componentes | Cap. 3, sección 9 |
| 21.37 · 1–4 | Comportamiento/capacidad, terminología y tres criterios; implícitas/explícitas | Cap. 4, sección 1 |
| 21.37 · 5 | Tabla operacional | Cap. 4, sección 2 |
| 21.37 · 6 | Tablas estructural y nube | Cap. 4, sección 2 |
| 21.37 · 7 | Tabla transversal y ambigüedades terminológicas | Cap. 4, secciones 2–3 |
| 21.37 · 8–10 | Familias ISO presentadas en el libro, adecuación funcional y lenguaje compartido | Cap. 4, secciones 3 y 6 |
| 21.37 · 10–11 | Interacciones entre características, costos e iteración | Cap. 4, sección 6 |
| 21.37 · 12–14 | Extracción desde negocio y requisitos; características compuestas, fondos y matrículas | Cap. 5, secciones 1–3 |
| 21.37 · 15–16 | Katas, sus secciones y enunciado Silicon Sandwiches | Cap. 5, sección 4 |
| 21.37 · 17–18 | Escalabilidad, elasticidad y primeros requisitos | Cap. 5, sección 5; atlas 6 |
| 21.37 · 19–21 | Mapas, móvil, promociones, pagos, franquicias, internacionalización, usabilidad y personalización | Cap. 5, secciones 5–6 |
| 21.37 · 22–24 | Limitar/priorizar, analogía Vasa, lista corta y top tres | Cap. 5, secciones 7–8 |

## Precisiones que evitan aprender una simplificación como regla absoluta

1. **Colas y temas.** La topología del ejemplo de subastas se distingue de las capacidades concretas de un broker. Se contrastaron [publicación/suscripción](https://www.rabbitmq.com/tutorials/tutorial-three-python), [control de acceso](https://www.rabbitmq.com/docs/access-control) y [monitorización](https://www.rabbitmq.com/docs/monitoring) con documentación oficial. Tener un tema no implica ausencia de permisos o de métricas.
2. **LCOM.** Se cuentan pares de métodos en LCOM1; no se confunde su resultado con componentes conexas. La ecuación 3-2 se comprobó visualmente en la página impresa 43 y se desarrolla por separado con su normalización.
3. **Abstracción.** A cuenta tipos abstractos y concretos; el relato de líneas de código no es un cálculo válido de esa proporción.
4. **Inestabilidad.** I mide relación de dependencias, no probabilidad empírica de fallo. D es distancia normalizada, no una certificación de calidad.
5. **Distribución.** Un monolito puede escalar horizontalmente; servicios separados no garantizan independencia, buen rendimiento ni aislamiento de fallos.
6. **Seguridad y pagos.** Usar un tercero no elimina los controles que siguen correspondiendo a la aplicación. Se explica el principio sin inventar obligaciones legales específicas.
7. **Clasificaciones.** Las familias ISO se presentan como aparecen en el libro, no como declaración de vigencia o conformidad con una edición normativa actual.
8. **Vasa.** Se conserva su función de analogía sobre requisitos acumulados; no se usa el relato simplificado como explicación histórica verificada del hundimiento.

## Qué se añadió para aprender mejor

PedidoClaro, sus cálculos, el laboratorio, los diagramas y el atlas son elaboraciones propias. Las cifras varían entre ejemplos porque ilustran preguntas diferentes; solo los supuestos dentro de cada ejercicio deben combinarse. Se añadieron percentiles, RTO/RPO, ley de Little, una plantilla ADR y explicaciones sobre reintentos para hacer visibles consecuencias prácticas de los conceptos.

Los cinco capítulos se redactaron con cinco subagentes, con revisión e integración central de terminología, recursos, ecuaciones y referencias. La cobertura se mide por temas del material recibido y sus mecanismos explicados, no por reproducir cada frase del libro.

## Comprobaciones de entrega

Se comprobaron los enlaces internos y las propiedades YAML de las notas, se renderizaron sin errores los 20 diagramas Mermaid y se revisaron los recursos visuales. Las copias de los tres PDF tienen el mismo SHA-256 que sus originales. Los capítulos reúnen 35 preguntas con respuesta y cinco ejercicios resueltos; el laboratorio añade cinco soluciones desplegables.

La ampliación visual contiene **33 imágenes PNG distintas: seis ilustraciones generadas, siete gráficos originales y veinte diagramas**. Los SVG y archivos Mermaid son versiones editables de esas mismas composiciones, no imágenes adicionales. Los PNG se insertan mediante Markdown relativo para verse en GitHub y Obsidian. El README ofrece navegación para GitHub. El intento de una ilustración generada adicional para priorización alcanzó el límite de uso y no se cuenta como entregado; el capítulo 5 mantiene su gráfico y sus cuatro diagramas explicados.

---

[← Índice de este bloque](00%20%C3%8Dndice.md)
