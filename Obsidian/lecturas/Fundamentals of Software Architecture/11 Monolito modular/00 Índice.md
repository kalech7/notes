---
title: "11 · Monolito modular"
created: 2026-09-28
capitulo: 11
tags:
  - lecturas/software-architecture
  - arquitectura/monolito-modular
  - indice
---

# Capítulo 11 · El estilo monolito modular

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]]

**Un monolito modular es una sola aplicación desplegable cuyo código está dividido por áreas del negocio.** Combina la sencillez de entregar una única pieza con la claridad de tener «pedidos», «pagos» o «envíos» como bloques reconocibles. Este capítulo explica cómo se construye, cómo se comunican sus módulos, cómo se evita que se degrade en una maraña, qué equipos encajan con él y cuándo conviene elegirlo.

> [!info] Fuente y cobertura
> Capítulo 11, «The Modular Monolith Architecture Style», páginas impresas **165–180**, páginas **1–16** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/08 Monolito modular.pdf|08 Monolito modular.pdf]] (**impresa = PDF + 164**). Se explican todas las secciones, las figuras 11-1 a 11-8 y los ejemplos 11-1 a 11-4. Las notas señalan tres imprecisiones del propio libro: los namespaces de la figura 11-2, la valoración de testabilidad frente al capítulo 10 y el pseudocódigo del ejemplo 11-3.

## Ruta de estudio

1. [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/01 Qué es un monolito modular|Qué es un monolito modular]] — PDF 1–2 · impresas 165–166 · figura 11-1.
2. [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/02 Estructura monolítica y estructura modular|Estructura monolítica y estructura modular]] — PDF 2–4 · impresas 166–168 · figuras 11-2 y 11-3.
3. [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/03 Comunicación entre módulos|Comunicación entre módulos: punto a punto y mediador]] — PDF 4–6 · impresas 168–170 · figuras 11-4 y 11-5.
4. [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/04 Datos nube y riesgos|Datos, nube y riesgos comunes]] — PDF 6–7 · impresas 170–171 · figura 11-6.
5. [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/05 Gobierno automatizado de módulos|Gobierno automatizado de módulos]] — PDF 8–10 · impresas 172–174 · ejemplos 11-1 a 11-4.
6. [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/06 Equipos y topologías|Equipos y topologías]] — PDF 10–11 · impresas 174–175.
7. [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/07 Características y cuándo usarlo|Características y cuándo usarlo]] — PDF 11–13 · impresas 175–177 · figura 11-7.
8. [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/08 Caso EasyMeals|Caso EasyMeals paso a paso]] — PDF 13–16 · impresas 177–180 · figura 11-8.
9. [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/09 Laboratorio y repaso|Laboratorio y repaso resuelto]] — integración de todo el capítulo.

## Lo que debes poder explicar al terminar

1. Por qué un monolito modular es monolítico (un despliegue) y a la vez está particionado por dominio.
2. Qué diferencia hay entre repartir los módulos en carpetas de un repositorio o en artefactos independientes, y cuándo conviene cada opción.
3. Por qué la comunicación entre módulos es un costo y qué acoplamiento conserva un mediador.
4. Cuándo tiene sentido que algunos módulos tengan su propia base de datos dentro de un monolito.
5. Cómo automatizar reglas que protejan las fronteras entre módulos.
6. Por qué el estilo funciona mejor con equipos organizados por dominio.
7. Qué significan sus estrellas, en qué mejora a la arquitectura por capas y en qué sigue igual de limitado.
8. Cómo se reparte un sistema real pequeño (EasyMeals) en módulos y componentes.

## Antes y después

Este capítulo aplica directamente la [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/02 Partición técnica y por dominio|partición por dominio del capítulo 9]] y se entiende mejor comparándolo con la [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/00 Índice|arquitectura por capas del capítulo 10]]: ambos son monolitos, pero agrupan el código con criterios opuestos. La idea de que un módulo contiene varios componentes viene del [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|capítulo 8]], y las reglas automáticas del apartado de gobierno son funciones de aptitud como las del [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/05 Gobierno y funciones de aptitud|capítulo 6]].

## Procedencia de las explicaciones

Las páginas citadas permiten contrastar cada idea con el escaneo. PedidoClaro, los cálculos, el código de ejemplo y las imágenes de `Recursos visuales/Capítulo 11` son elaboración propia; **EasyMeals** y los ejemplos `com.orderentry` pertenecen al libro. Las imágenes recrean relaciones de las figuras con rótulos en español, sin ser copias exactas.
