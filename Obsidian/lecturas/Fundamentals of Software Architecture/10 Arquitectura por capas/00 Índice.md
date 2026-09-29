---
title: "10 · Arquitectura por capas"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/capas
capitulo: 10
---

# Arquitectura por capas

La arquitectura por capas organiza el sistema por responsabilidades técnicas. Ayuda a separar interfaz, reglas y almacenamiento, pero esa claridad lógica no proporciona automáticamente independencia de despliegue, escalado ni recuperación. Este recorrido desarrolla ambos lados con ejemplos y decisiones razonadas.

> [!info] Fuente y cobertura
> Capítulo 10, «Layered Architecture Style», páginas impresas **153–164**, páginas **1–12** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/07 Arquitectura por capas.pdf|07 Arquitectura por capas.pdf]]. Se explican todas las secciones del fragmento, las figuras 10-1 a 10-6 y el ejemplo 10-1. No se atribuyen contenidos de otros capítulos no presentes a esta fuente.

## Recorrido recomendado

- [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/01 Responsabilidades topología y despliegue|Responsabilidades, topología y despliegue]] — PDF 1–3 · impresas 153–155 · figuras 10-1 y 10-2.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/02 Partición técnica y cambios de negocio|Partición técnica y cambios de negocio]] — PDF 3 · impresa 155; PDF 8–11 · impresas 160–163.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/03 Capas cerradas abiertas y aislamiento|Capas cerradas, abiertas y aislamiento del cambio]] — PDF 3–6 · impresas 155–158 · figuras 10-3, 10-4 y 10-5.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/04 Servicios compartidos y sumidero arquitectónico|Servicios compartidos y sumidero arquitectónico]] — PDF 5–7 · impresas 157–159 · figuras 10-4 y 10-5.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/05 Datos nube fallos y recuperación|Datos, nube, fallos y recuperación]] — PDF 7 · impresa 159; PDF 9–10 · impresas 161–162.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/06 Gobierno pruebas estructurales y equipos|Gobierno, pruebas estructurales y equipos]] — PDF 7–9 · impresas 159–161 · ejemplo 10-1; PDF 10 · impresa 162.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/07 Características tradeoffs y cuándo elegir|Características, tradeoffs y cuándo elegir el estilo]] — PDF 9–12 · impresas 161–164 · figura 10-6.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/08 Casos de uso laboratorio y repaso|Casos de uso, laboratorio y repaso resuelto]] — PDF 11–12 · impresas 163–164; integración didáctica de PDF 1–12 · impresas 153–164.

## Lo que deberías poder explicar después

- Diferenciar una capa lógica de una unidad de despliegue.
- Predecir el alcance de un cambio técnico y uno del negocio.
- Justificar qué capas deben ser abiertas o cerradas.
- Detectar un sumidero sin convertir cada delegación en un problema.
- Razonar sobre base de datos compartida, latencia y recuperación.
- Diseñar una regla estructural y distinguirla de una prueba funcional.
- Interpretar las estrellas como valoraciones cualitativas de la fuente.
- Decidir cuándo la sencillez del estilo compensa sus límites.

## Distinciones para no memorizar errores

Una capa abierta no anula otra cerrada. Una capa lógica no es un servidor. Una réplica no equivale automáticamente a un quantum. La modularidad del código no garantiza autonomía operativa. El 80/20 del sumidero es una heurística, y los minutos de recuperación son ejemplos. El esquema de cinco capas del ejemplo de redes no es el modelo OSI de siete capas.

## Procedencia de las explicaciones

Las referencias de cada nota apuntan al fragmento escaneado. Los casos de tienda y biblioteca, los cálculos y los diagramas adicionales son elaboración didáctica. Las imágenes propias sirven para explicar relaciones; no son facsímiles de las figuras del libro. Los matices técnicos se separan expresamente de las formulaciones de la fuente.
