---
title: "12 · Arquitectura pipeline — tuberías y filtros"
created: 2026-09-29
capitulo: 12
tags:
  - lecturas/software-architecture
  - arquitectura/pipeline
  - indice
---

# Arquitectura pipeline — tuberías y filtros

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]]

**Un pipeline convierte un trabajo completo en etapas pequeñas: cada filtro realiza una tarea y pasa sus datos a la siguiente etapa por un canal unidireccional.** Así, leer, seleccionar, calcular y guardar pueden cambiar y probarse por separado. Su dificultad principal está en conservar fronteras claras y saber qué hacer cuando una etapa falla.

> [!info] Fuente y cobertura
> Capítulo 12, «Pipeline Architecture Style», PDF **1–12** · impresas **181–192** · figuras **12-1 a 12-4**. La correspondencia es **impresa = PDF + 180**. La primera página no muestra su número, que se deduce de la secuencia; todas las demás lo conservan. Se leyeron las doce páginas, girando las páginas PDF 4–11 para interpretarlas. [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/09 Arquitectura pipeline.pdf#page=1|Abrir el escaneo conservado]].

## Ruta de estudio

1. [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/01 Topología filtros y canales|Topología, filtros y canales]] — qué forma reconoce al estilo y qué significa su despliegue habitual. PDF 1–2 · impresas 181–182 · figura 12-1.
2. [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/02 Roles y composición de filtros|Los cuatro roles y la composición]] — productor, transformador, tester, consumidor y el ejemplo de palabras frecuentes. PDF 2–3 · impresas 182–183.
3. [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/03 Contratos sincronía y rendimiento|Contratos, sincronía y rendimiento]] — qué pasa entre etapas y por qué la etapa lenta limita el flujo. PDF 3 y 6 · impresas 183 y 186; cálculos propios.
4. [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/04 Datos nube y despliegue|Datos, nube y despliegue]] — función de aptitud, almacenes y Step Functions. PDF 4–5 · impresas 184–185 · figura 12-2.
5. [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/05 Riesgos errores y recuperación|Riesgos, errores y recuperación]] — sobrecarga de responsabilidades, retrocesos, fallos y contratos incompatibles. PDF 5–6 · impresas 185–186.
6. [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/06 Gobierno con etiquetas y pruebas|Gobierno con etiquetas y pruebas]] — anotaciones Java, atributos C#, puntos de entrada y sus límites. PDF 6–8 · impresas 186–188.
7. [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/07 Equipos características y elección|Equipos, características y elección]] — los cuatro tipos de equipo, ficha de estrellas y cuándo conviene. PDF 8–11 · impresas 188–191 · figura 12-3.
8. [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/08 Caso de telemetría Kafka|Telemetría de Kafka a MongoDB]] — clasificación y cálculo de duración o uptime. PDF 11–12 · impresas 191–192 · figura 12-4.
9. [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/09 Laboratorio y repaso|Laboratorio y repaso resuelto]] — diseñar un flujo, seguir registros, calcular capacidad y recuperar una escritura incierta.

## Conexión con los capítulos anteriores

El [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/00 Índice|monolito modular]] agrupa por áreas del negocio. El pipeline organiza por **etapas técnicas del procesamiento**. Ambos pueden desplegarse como una sola pieza, pero por razones y con estructuras distintas. La separación entre componente lógico y despliegue viene del [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/02 Arquitectura lógica frente a física|capítulo 8]]; las funciones de aptitud se conectan con el [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/05 Gobierno y funciones de aptitud|capítulo 6]].

## Procedencia y precisiones

La topología, los cuatro roles, el caso de tendencia y el caso Kafka pertenecen al libro. PedidoClaro, los contratos JSON, cálculos, políticas de recuperación y ejercicios son elaboraciones propias. Los tres PNG recrean relaciones del capítulo con rótulos en español y conservan su generador.

Se precisa la analogía del libro entre tester y `reduce`, se distinguen las garantías de Standard y de las dos variantes de Express, y se corrige el ejemplo incompleto de atributo C#. La ficha de estrellas describe el **pipeline monolítico habitual**; no es una garantía para cualquier variante distribuida.
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/01 Topología filtros y canales|Siguiente →]]
