---
title: "Capítulo 9 · Fundamentos de estilos arquitectónicos"
created: 2026-09-28
capitulo: 9
tags:
  - lecturas/software-architecture
  - indice
---

# Capítulo 9 · Fundamentos de estilos arquitectónicos

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]]

**Este capítulo enseña a entender qué cambia al elegir una organización del sistema.** Antes de comparar estilos concretos, distingue estilo y patrón, partición técnica y por dominio, despliegue monolítico y distribuido, costos de comunicación y relación entre arquitectura y equipos.

Las notas explican los mecanismos desde cero, con ejemplos resueltos, imágenes originales, diagramas y preguntas respondidas. Puedes estudiarlas sin consultar el libro; las referencias quedan para verificar el origen de cada idea. No son una transcripción ni una traducción literal.

> [!info] Cobertura exacta
> El escaneo **CamScanner 2026-09-28 23.17.pdf** contiene 23 páginas: PDF 1 es la portada de la Parte II, sin número impreso visible; PDF 2–23 corresponden consecutivamente a las impresas 131–152 del capítulo 9. Se cubre todo el texto del escaneo y se interpretan sus figuras 9-1 a 9-14. Las notas corrigen explícitamente la afirmación de serialización universal en Java (impresa 136) y las unidades del ejemplo de transferencia (impresa 146).

## Ruta de estudio

- [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/01 Estilos patrones y estructura|01 Estilos patrones y estructura]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/02 Partición técnica y por dominio|02 Partición técnica y por dominio]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/03 Silicon Sandwiches y decisiones de partición|03 Silicon Sandwiches y decisiones de partición]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/04 Monolitos distribución y fiabilidad|04 Monolitos distribución y fiabilidad]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/05 Latencia ancho de banda y costo|05 Latencia ancho de banda y costo]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/06 Seguridad topología y coordinación|06 Seguridad topología y coordinación]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/07 Versionado compensación y observabilidad|07 Versionado compensación y observabilidad]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/08 Conway y topologías de equipos|08 Conway y topologías de equipos]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/09 Laboratorio y repaso|09 Laboratorio y repaso]].

## Lo que debes poder explicar al terminar

1. Por qué una estructura modular puede desplegarse como monolito.
2. Qué cambia al agrupar primero por técnica o por dominio y cómo evaluarlo con cambios reales.
3. Por qué un timeout no demuestra que la operación remota falló.
4. Cómo calcular una tasa de transferencia sin confundir bits y bytes, y por qué un promedio no demuestra un objetivo p95.
5. Qué costos agregan contratos versionados, compensaciones y operación distribuida.
6. Cómo equipos, capacidades y fronteras técnicas se condicionan mutuamente.

## Antes y después

La base conceptual está en los capítulos de modularidad, características, quanta y componentes. Este capítulo convierte esos conceptos en preguntas para comparar estilos. La nota de laboratorio integra el razonamiento antes de avanzar a las arquitecturas por capas del capítulo 10.

## Fuente

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/06 Fundamentos de estilos arquitectónicos.pdf#page=1|Abrir el escaneo conservado en Materiales]].
