---
title: "Ampliación y cobertura · capítulos 9 y 10"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - fuentes
---

# Fuentes y cobertura de los capítulos 9 y 10

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]]

Esta ampliación explica los dos escaneos compartidos el 28 de septiembre por la noche. Las notas están escritas en español con ejemplos, cálculos y diagramas propios. El propósito es estudiar los conceptos sin depender de una lectura paralela del libro. El alcance sigue siendo el material proporcionado: no se presenta como cobertura de capítulos posteriores.

## Archivos y numeración

| Original | Copia en la colección | Páginas PDF | Páginas impresas |
|---|---|---|---|
| CamScanner 2026-09-28 23.17.pdf | [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/06 Fundamentos de estilos arquitectónicos.pdf\|06 Fundamentos de estilos arquitectónicos]] | 1 | Portada de la Parte II, sin número impreso visible |
| El mismo escaneo | La misma copia 06 | 2–23 | 131–152, capítulo 9 completo en esta secuencia |
| CamScanner 2026-09-28 23.22.pdf | [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/07 Arquitectura por capas.pdf\|07 Arquitectura por capas]] | 1–12 | 153–164, capítulo 10 |

En el PDF 06, para las páginas 2–23, **página impresa = página PDF + 129**. Esta fórmula no se aplica a la portada sin numeración. En el PDF 07, **página impresa = página PDF + 152**.

Se añaden **35 páginas de PDF** a las 120 anteriores: la colección conserva **siete PDF y 155 páginas de PDF**. No se identifican folios numerados 129–130; la portada sin número no permite asignarlos con certeza. Los huecos anteriores siguen documentados en [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/01 Fuentes y cobertura|la cobertura inicial]] y [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/04 Ampliación capítulos 6 a 8|la ampliación 6–8]].

Los escaneos carecen de una capa de texto útil salvo la marca CamScanner. Se realizó OCR y contraste visual; algunas páginas invertidas requirieron reorientación para leerlas. Los PDF conservados no se alteraron. El OCR es un apoyo de lectura y no una fuente independiente. Las instrucciones o ejercicios dentro del libro se trataron como contenido, no como órdenes para ejecutar acciones.

## Mapa de contenido

| Pasaje | Tema | Dónde estudiarlo |
|---|---|---|
| PDF 06, 1–3; impresas 131–132 y portada | Parte II; estilo frente a patrón; componentes, despliegue, comunicación y datos | Capítulo 9, nota 01 |
| PDF 06, 4–7; impresas 133–136 | Big Ball of Mud, arquitectura unitaria, cliente/servidor y tres niveles; consecuencias de decisiones históricas | Capítulo 9, nota 01 |
| PDF 06, 8–11; impresas 137–140 | Partición superior técnica y por dominio; ley de Conway | Capítulo 9, notas 02 y 08 |
| PDF 06, 12–13; impresas 141–142 | Silicon Sandwiches: dominio frente a personalización común/local | Capítulo 9, nota 03 |
| PDF 06, 14–20; impresas 143–149 | Monolitos y distribución; ocho falacias clásicas | Capítulo 9, notas 04–06 |
| PDF 06, 20–21; impresas 149–150 | Versionado, compensaciones y observabilidad | Capítulo 9, nota 07 |
| PDF 06, 22–23; impresas 151–152 | Cuatro tipos de equipo; transición a estilos específicos | Capítulo 9, notas 08–09 |
| PDF 07, 1–3; impresas 153–155 | Topología lógica, despliegue físico y partición técnica | Capítulo 10, notas 01–02 |
| PDF 07, 3–6; impresas 155–158 | Aislamiento, capas abiertas/cerradas y servicios compartidos | Capítulo 10, notas 03–04 |
| PDF 07, 6–7; impresas 158–159 | Sumidero arquitectónico, topología de datos, nube y riesgos | Capítulo 10, notas 04–05 |
| PDF 07, 7–9; impresas 159–161 | Gobierno estructural y tipos de equipo | Capítulo 10, nota 06 |
| PDF 07, 9–11; impresas 161–163 | Ficha de características, compromisos y condiciones de uso | Capítulo 10, nota 07 |
| PDF 07, 11–12; impresas 163–164 | Ejemplos de capas y viabilidad de entrega | Capítulo 10, nota 08 |

Entradas: [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/00 Índice|Capítulo 9]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/00 Índice|Capítulo 10]].

## Inventario de figuras de la fuente

Este inventario sirve para comprobar cobertura. Los nuevos gráficos reúnen o amplían conceptos; no se afirma que exista una copia exacta por cada figura original.

| Figura | PDF / impresa | Qué aporta |
|---|---|---|
| 9-1 | 06:5 / 134 | Dependencias difíciles de controlar en un Big Ball of Mud |
| 9-2 | 06:8 / 137 | Dos particiones de nivel superior |
| 9-3 | 06:9 / 138 | Agrupación técnica frente a dominio |
| 9-4 | 06:11 / 140 | Un flujo de negocio repartido entre capas |
| 9-5 y 9-6 | 06:12 / 141 | Dos alternativas de partición para Silicon Sandwiches |
| 9-7 y 9-8 | 06:15 / 144 | Red no fiable; llamada local frente a remota |
| 9-9 | 06:16 / 145 | Ancho de banda finito |
| 9-10 | 06:17 / 146 | Exposición y seguridad de los endpoints |
| 9-11 | 06:18 / 147 | Cambios de topología |
| 9-12 y 9-13 | 06:19 / 148 | Coordinación con administradores y coste monetario |
| 9-14 | 06:20 / 149 | Heterogeneidad de la red |
| 10-1 y 10-2 | 07:2 / 154 | Capas lógicas y variantes de despliegue |
| 10-3 | 07:4 / 156 | Recorrido a través de capas cerradas |
| 10-4 | 07:5 / 157 | Objetos compartidos dentro de Negocio |
| 10-5 | 07:6 / 158 | Capa Servicios abierta bajo Negocio cerrada |
| 10-6 | 07:9 / 161 | Evaluación cualitativa de características |
| Ejemplo 10-1 | 07:7–8 / 159–160 | Reglas estructurales de capas con ArchUnit |

## Correcciones y límites que importan para aprender

**Serialización Java.** El recuadro de la impresa 136 generaliza incorrectamente que todo objeto implementa una interfaz que exige serialización. La capacidad se habilita implementando `Serializable`, directamente o por herencia; `Object` no la implementa. La lección sobre las consecuencias duraderas de decisiones de diseño se mantiene, pero no esa afirmación técnica. Fuentes primarias: [API de Serializable, Java SE 25](https://docs.oracle.com/en/java/javase/25/docs/api/java.base/java/io/Serializable.html) y [explicación de Oracle sobre Object y serialización](https://www.oracle.com/technical-resources/articles/java/serializationapi.html).

**Unidades de transferencia.** En la impresa 146, 200 bytes por respuesta a 2.000 respuestas/s producen 400.000 bytes/s: **400 kB/s o 3,2 Mbit/s**, usando unidades decimales. No son 400 kilobits/s. El contrato de 500 kB produce 1 GB/s o 8 Gbit/s. Son tasas agregadas de carga útil, no el consumo de una única llamada. Faltan cabeceras, solicitudes, cifrado y reintentos.

**Latencia y distribución.** Las cifras del libro son ejemplos. La latencia depende del sistema y la carga. Las medias de tramos secuenciales pueden sumarse para ese recorrido; los percentiles no se suman de esa forma. Distribuir permite determinadas estrategias de escala y aislamiento, pero introduce dependencias que pueden reducir disponibilidad o empeorar el tiempo de respuesta.

**Capas, módulos y quanta.** Modularidad lógica, despliegue independiente y aislamiento de fallos son dimensiones diferentes. La ficha de un quantum y las puntuaciones bajas describen el estilo por capas tradicional analizado por los autores. No prueban que cualquier programa con capas tenga idénticos límites o comportamiento.

**Disponibilidad y replicación.** Un fallo que agota la memoria puede derribar el proceso completo. Aun así, un monolito puede tener réplicas, balanceo y recuperación. Eso mejora la tolerancia a ciertos fallos de instancia, sin separar las responsabilidades dentro de cada proceso ni eliminar dependencias compartidas. Los tiempos de arranque citados por el libro no son constantes universales.

**Capas abiertas.** «Abierta» significa que esa capa puede omitirse en un recorrido autorizado. No vuelve públicas todas las capas inferiores y no permite saltarse otra capa cerrada. La apertura debe documentarse y verificarse.

**Sumidero y estrellas.** La proporción 80/20 es una heurística para discutir el diseño, no un umbral estadístico probado. Las estrellas de la ficha son valoraciones comparativas del libro, no resultados medidos de tu sistema. Las notas explican las causas de cada valoración.

**Ejemplos de redes.** Las páginas 163–164 mezclan referencias al modelo OSI con una representación pedagógica de cinco capas de Internet. OSI tiene siete; no se enseña la lista de cinco como si fuera el modelo OSI completo. La fiabilidad de TCP tampoco debe atribuirse a todos los protocolos de transporte. La recomendación [ITU-T X.200, apartado 6.1 y figura 11](https://www.itu.int/rec/dologin_pub.asp?id=T-REC-X.200-199407-I%21%21PDF-E&lang=e&type=items) define las siete capas del modelo OSI. El [RFC 768 de UDP](https://www.rfc-editor.org/info/rfc768/) especifica que la entrega y la protección contra duplicados no están garantizadas. Son referencias primarias para la precisión conceptual, no una ampliación del alcance del capítulo.

## Imágenes y elaboración propia

Hay ocho PNG nuevos en `Recursos visuales/Capítulos 9 y 10`, creados mediante un generador Python editable. Se integran en las notas temáticas y en el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/06 Atlas y práctica de estilos y capas|atlas y práctica de estilos y capas]]. Representan partición, respuesta perdida, latencia y tráfico, tipos de equipo, capas/despliegue, apertura/cierre, sumidero y replicación. No son recortes del libro ni resultados de mediciones reales.

Además, los diagramas Mermaid de las notas expresan dependencias, secuencias y decisiones con etiquetas en español. Los casos propios se distinguen de **Silicon Sandwiches**, que pertenece al libro. Los ejemplos no prescriben una arquitectura universal.

## Trabajo y revisión

Dos subagentes analizaron y redactaron los capítulos por separado; un tercero revisó fuentes, figuras y precisiones técnicas. La integración central preparó imágenes, rutas de estudio, vínculos y ejercicios transversales. La validación final se completó el 28 de septiembre:

- **Enlaces:** 320 wikilinks y 475 enlaces Markdown de la guía resuelven a archivos existentes; las anclas `#page=` no superan las páginas de cada PDF (23 en el 06, 12 en el 07).
- **Propiedades:** todas las notas tienen `title`, `created` y `tags` válidos en YAML; las notas del capítulo 9 usan la etiqueta `arquitectura/estilos`, coherente con los capítulos 6–10.
- **Diagramas:** los doce bloques Mermaid se renderizan sin errores. Se corrigió una nota de secuencia del capítulo 10 cuyo `;` cortaba el diagrama.
- **Contraste con el escaneo:** se verificaron la lista de estilos monolíticos de la impresa 143, que omite el monolito modular, y la cifra de 400 Kbps de la impresa 146, cuya corrección se mantiene. Los cálculos de disponibilidad, latencia y transferencia de las notas son correctos.
- **Estilo:** las explicaciones de gráficos y diagramas se redactan como texto directo, sin rótulos del tipo «cómo leerlo».
