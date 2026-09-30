---
title: "Database Internals — Capítulo 11 · Relojes vectoriales y conflictos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Relojes vectoriales y conflictos

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

Un **reloj vectorial** es un vector de contadores lógicos, uno por participante, que resume qué eventos conoce un proceso. Permite representar un orden parcial y distinguir antecedentes de eventos concurrentes. No es un reloj físico compartido ni una estrategia de fusión de valores.

En el esquema básico de eventos, cada proceso incrementa su propia casilla al registrar un nuevo evento y adjunta el vector al enviar. Al recibir, toma máximos por casilla entre su vector y el recibido, e incrementa su casilla para registrar la recepción. Las convenciones de vectores de versiones de una clave pueden diferir: es necesario declarar qué evento cuenta cada componente.

## Comparar componente por componente

Dados A y B, `A ≤ B` significa que cada componente de A es menor o igual que el correspondiente de B. Si además al menos uno es menor, escribimos `A < B`: A precede causalmente a B dentro del esquema. Si ni `A ≤ B` ni `B ≤ A`, los vectores son incomparables y representan concurrencia.

Ejemplos propios:

| A | B | Comparación | Interpretación |
|---|---|---|---|
| `[1,0,0]` | `[2,1,0]` | A < B | B conoce los eventos de A y más |
| `[2,0,0]` | `[1,1,0]` | Incomparables | Ninguno incorpora todo el pasado del otro |
| `[1,1,0]` | `[1,1,0]` | Iguales | Mismo resumen vectorial en este esquema |

En el segundo caso A gana en la primera casilla y B en la segunda. Sumar los componentes produciría 2 en ambos y borraría información; ordenar lexicográficamente elegiría uno, pero ese orden artificial no probaría causalidad.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 11/05 Ramas causales.png]]

Las flechas representan dependencia. Las ramas comparten las versiones 1 y 5; una continúa con 7 y 8 y la otra escribe 3. Ninguna flecha conecta 3 con 7, de modo que conservar una rama como si la otra nunca hubiera existido requiere una política adicional. Es una recreación en español de la estructura de la figura 11-9.

## Detectar frente a reconciliar

En una clave, una versión cuyo contexto domina a otra puede representar una actualización que ya incorporó el antecedente. Dos contextos incomparables identifican versiones concurrentes, a veces llamadas **siblings**. Se pueden devolver ambas para una reconciliación explícita o usar un tipo que tenga una fusión bien definida.

Ejemplo propio: dos usuarios parten de `etiquetas={azul}`. Uno añade rojo y otro verde. Si la semántica deseada es unión, una reconciliación produce `{azul,rojo,verde}`. Si se tratara de dos direcciones de envío, unir cadenas no tendría sentido. El vector informa del conflicto; el dominio decide la respuesta.

El libro cita Dynamo y Riak como usos de este enfoque y contrasta con almacenes que resuelven mediante **last-write-wins**, LWW, «gana la última escritura». Una etiqueta de tiempo permite elegir un ganador, pero no conserva necesariamente todos los cambios de negocio ni demuestra cuál ocurrió después causalmente.

## Metadatos y recolección

Los vectores y contextos ocupan espacio. Si cambian los participantes o se retiran versiones, se necesita una política de recolección que no elimine información todavía necesaria para distinguir una dependencia o un duplicado. El capítulo señala ese costo; no desarrolla un algoritmo completo de membresía y compactación.

La afirmación de la impresa 232 sobre simular tiempo o estado global se utiliza como intuición. Técnicamente, los vectores proporcionan orden parcial causal: no sincronizan relojes reales, no hacen que todos conozcan inmediatamente todos los eventos y no eligen por sí solos una fusión correcta.

> [!question]- ¿`[3,0]` es posterior a `[2,1]` porque 3 es mayor que 2?
> No. La primera componente aumenta y la segunda disminuye respecto al otro vector. Son incomparables: no existe dominación componente por componente.

**Referencia:** PDF 36–37 · impresas 232–233 · figura 11-9. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=36|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/09 Consistencia causal y dependencias|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/11 Garantías de sesión y PRAM|Siguiente]] →
