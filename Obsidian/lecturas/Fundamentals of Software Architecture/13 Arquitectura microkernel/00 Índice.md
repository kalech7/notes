---
title: "13 · Arquitectura microkernel"
created: 2026-09-29
capitulo: 13
tags:
  - lecturas/software-architecture
  - arquitectura/microkernel
  - indice
---

# Arquitectura microkernel

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]]

**Un núcleo conserva el proceso común y los plugins encapsulan las variantes.** Esa división permite ampliar un producto o cambiar reglas específicas sin reescribir su coordinación, siempre que el contrato se mantenga coherente y las extensiones no queden entrelazadas.

Estas notas explican el capítulo 13 completo del escaneo de las 19:11: 16 páginas PDF, correspondientes a las impresas 193–208. Incluyen los nueve diagramas del libro desarrollados en prosa, seis imágenes didácticas originales, diagramas Mermaid, todos sus casos y un laboratorio propio con reglas y respuestas. El PDF permanece como evidencia para contrastar.

## Recorrido de estudio

1. [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/01 Núcleo y topología|Núcleo y topología]]: qué se separa, qué cambia y por qué la complejidad se contiene.
2. [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/02 Composición espectro e interfaz|Composición, espectro e interfaz]]: núcleo por capas o dominios, funcionalidad autónoma y tres ubicaciones de la interfaz.
3. [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/03 Plugins y mecanismos de carga|Plugins y mecanismos de carga]]: paquetes, bibliotecas, compilación, reflexión y ciclo de vida.
4. [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/04 Registro contratos y adaptación|Registro, contratos y adaptación]]: descubrimiento, significado de datos, terceros y compatibilidad.
5. [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/05 Acceso remoto nube y quantum|Acceso remoto, nube y quantum]]: sincronía, mensajes, latencia, fallos y quanta.
6. [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/06 Datos y propiedad del estado|Datos y propiedad del estado]]: datos comunes, reglas privadas y trazabilidad.
7. [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/07 Riesgos dependencias y gobierno|Riesgos, dependencias y gobierno]]: núcleo volátil, dependencias transitivas y verificaciones útiles.
8. [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/08 Equipos características y elección|Equipos, características y elección]]: tabla de valoración contrastada y criterios de encaje.
9. [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/09 Casos del libro y variaciones|Casos del libro y variaciones]]: reciclaje, pagos, impuestos, seguros y herramientas extensibles.
10. [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/10 Laboratorio y repaso resuelto|Laboratorio y repaso resuelto]]: EcoEval, cálculos, contratos, pruebas y preguntas plegables.

## Tres distinciones que conviene conservar

- **Plugin frente a filtro:** una extensión representa una capacidad o variante; una etapa pipeline representa una transformación en un recorrido. Pueden combinarse, pero no son intercambiables.
- **Separación del código frente a independencia operacional:** un componente local puede tener contrato limpio y compartir proceso, recursos y entrega con todos los demás.
- **Núcleo mínimo frente a núcleo estable:** el tamaño no prueba la calidad de la frontera. Lo decisivo es evitar que cada personalización cambie la coordinación común.

El ejemplo resuelto conserva valores monetarios en centavos y deja ausente el precio cuando no hay recomendación de venta. Estas precisiones muestran cómo pasar de cajas a un contrato con significado, sin convertir la simplificación del libro en una implementación supuestamente completa.

## Comparar con otros estilos

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/07 Comparación visual de módulos filtros plugins y servicios|Comparación visual de módulos, filtros, plugins y servicios]]: conecta el propósito de cada separación con publicación, datos y fallos.

## Materiales y revisión

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/10 Arquitectura microkernel.pdf#page=1|PDF original · capítulo 13]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/08 Ampliación capítulo 13|Cobertura, figuras y precisiones]]

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/00 Índice|← Capítulo 12: pipeline]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/01 Núcleo y topología|Comenzar →]]
