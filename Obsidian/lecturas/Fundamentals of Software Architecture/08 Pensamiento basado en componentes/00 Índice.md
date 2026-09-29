---
title: "08 · Pensamiento basado en componentes"
created: 2026-09-28
tags:
  - lecturas/software-architecture
capitulo: 8
---

# Capítulo 8 · Pensamiento basado en componentes

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]]

El propósito es aprender a **organizar el sistema en responsabilidades coherentes**, comprobarlas mediante historias y características arquitectónicas, y entender cómo las dependencias afectan a los cambios. Este capítulo contiene diez notas extensas, once gráficos PNG recreados a partir de las figuras del libro, un diagrama de decisión PNG adicional y ejercicios resueltos.

> [!info] Fuente verificada
> *Fundamentals of Software Architecture*, capítulo 8, páginas impresas **107–128**, correspondientes a las páginas **13–34** del PDF de las 15.56. Se revisaron las veintidós páginas, su OCR y todas las figuras 8-1 a 8-17. La última página contiene el cierre del caso; no hay frases cortadas ni páginas internas ausentes en este intervalo. El escaneo conserva algunas marcas y recortes de margen, pero permite leer el contenido utilizado.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]].

## Orden de lectura

| Nota | Pregunta que aprenderás a responder |
|---|---|
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/01 Componentes lógicos y organización del código\|01 Componentes lógicos y organización del código]] | ¿Qué es un componente y cómo aparece en el código? |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/02 Arquitectura lógica frente a física\|02 Arquitectura lógica frente a física]] | ¿Qué muestra cada vista y qué no permite inferir? |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/03 Ciclo de identificación y refinamiento\|03 Ciclo de identificación y refinamiento]] | ¿Cómo revisar el diseño con requisitos nuevos? |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/04 Descubrir componentes por flujos y acciones\|04 Descubrir componentes por flujos y acciones]] | ¿Cómo derivar candidatos desde recorridos y acciones? |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/05 Trampa de entidades y nombres responsables\|05 Trampa de entidades y nombres responsables]] | ¿Por qué una entidad no define por sí sola una responsabilidad? |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/06 Historias cohesión y distribución de responsabilidades\|06 Historias cohesión y distribución de responsabilidades]] | ¿Cómo asignar historias y detectar exceso de responsabilidad? |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/07 Características arquitectónicas y granularidad\|07 Características arquitectónicas y granularidad]] | ¿Cuándo la carga o la criticidad justifican separar? |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/08 Acoplamiento aferente eferente y temporal\|08 Acoplamiento aferente eferente y temporal]] | ¿Cómo contar dependencias y reconocer las ocultas? |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/09 Ley de Demeter y conocimiento mínimo\|09 Ley de Demeter y conocimiento mínimo]] | ¿Cómo reducir conocimiento local sin fingir desacoplamiento total? |
| [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/10 Kata Going Going Gone y repaso resuelto\|10 Kata Going Going Gone y repaso resuelto]] | ¿Cómo aplicar el proceso completo a una subasta? |

## Mapa de procedencia de los gráficos

| Recurso recreado | Figuras de origen | Páginas impresas / PDF | Dónde se explica |
|---|---|---|---|
| Componentes y código | 8-1, 8-2, 8-3 | 108–109 / 14–15 | Nota 01 |
| Arquitectura lógica | 8-4 | 110 / 16 | Nota 02 |
| Arquitectura física | 8-5 | 111 / 17 | Nota 02 |
| Ciclo iterativo | 8-6 | 112 / 18 | Nota 03 |
| Recipientes e historias | 8-7, 8-9 | 113, 117 / 19, 23 | Nota 04 |
| Trampa de entidades | 8-8 | 116 / 22 | Nota 05 |
| Notificación compartida | 8-10 | 118 / 24 | Nota 06 |
| Acoplamiento | 8-11, 8-12, 8-13 | 121–122 / 27–28 | Nota 08 |
| Demeter antes y después | 8-14, 8-15 | 123–124 / 29–30 | Nota 09 |
| Decisión de granularidad (adicional) | Elaboración didáctica | 120 / 26 | Nota 07 |
| GGG inicial | 8-16 | 126 / 32 | Nota 10 |
| GGG revisado | 8-17 | 128 / 34 | Nota 10 |

Cada imagen incorpora una explicación de **elementos, flechas, recorrido, conclusión y límites**. Los colores añadidos facilitan la lectura; no introducen requisitos del libro. Los gráficos son adaptaciones didácticas, con geometría simplificada y traducciones, no copias exactas del estilo tipográfico original.

## Cómo estudiar a profundidad

1. Lee las notas 01–03 para distinguir responsabilidad, despliegue y proceso de revisión.
2. Dibuja el flujo de una compra y contrástalo con los actores de la nota 04.
3. Escribe una declaración de responsabilidad por componente; utiliza las notas 05–07 para criticarla.
4. Cuenta Ca y Ce en un pequeño grafo; explica una dependencia temporal que no aparezca como llamada directa.
5. Redibuja Demeter y demuestra por qué el total de relaciones del ejemplo sigue siendo cuatro.
6. Resuelve el caso GGG sin mirar el gráfico revisado; después compara compromisos, no solo nombres.

## Distinciones que no debes perder

- Componente lógico no significa microservicio.
- Un directorio puede representar un componente, pero no toda carpeta real es un componente arquitectónico.
- Compartir entidad no prueba cohesión suficiente.
- Dividir código puede facilitar objetivos; no garantiza escalabilidad ni aislamiento operativo.
- Ausencia de comunicación directa no demuestra ausencia de acoplamiento.
- Demeter limita conocimiento y puede redistribuir dependencias sin reducirlas globalmente.
- La primera arquitectura es una propuesta que se revisa, no una respuesta única.

Fuente editable de los doce gráficos: [[Obsidian/lecturas/Fundamentals of Software Architecture/Recursos visuales/Capítulos 6 a 8/c08-generar-graficos.py|c08-generar-graficos.py]].

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/01 Componentes lógicos y organización del código|Comenzar lectura →]]
