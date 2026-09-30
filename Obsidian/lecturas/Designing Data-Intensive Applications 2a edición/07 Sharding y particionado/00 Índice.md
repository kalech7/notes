---
title: "DDIA — Capítulo 7 · Sharding y particionado"
created: 2026-09-29
capitulo: 7
tags:
  - lecturas/ddia
  - arquitectura/sharding
---

# Capítulo 7 · Sharding y particionado

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|← Inicio del libro]]

**Pregunta central:** cómo repartir datos y consultas entre varias máquinas cuando una sola ya no basta, sin crear nodos saturados ni convertir cada lectura en una búsqueda por todo el clúster.

El capítulo de la segunda edición se llama simplemente *Sharding* (en la primera edición el tema equivalente se titulaba *Partitioning* y tenía otra organización). Las notas siguen el orden lógico del capítulo, pero agrupan temas para que cada una se pueda estudiar sola. En todos los ejemplos propios se usa la misma plataforma de **pedidos en línea**, para que las decisiones de una nota se puedan comparar con las de otra.

| Nota | Lo que podrás explicar |
|---|---|
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/01 Shards réplicas y carga\|01 · Shards, réplicas y carga]] | Qué es un shard, cómo convive con la replicación, cuándo compensa fragmentar y qué aporta el sharding por inquilino |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/02 Particionado por rangos y hotspots\|02 · Rangos y hotspots]] | Por qué los rangos ordenados facilitan escaneos, cómo aparecen shards calientes y qué cuesta «salar» una clave popular |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/03 Hash claves compuestas y orden\|03 · Hash, claves compuestas y orden]] | Qué gana y qué pierde el hash, cómo una clave compuesta recupera consultas por rango dentro de una partición |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/04 Índices secundarios locales y globales\|04 · Índices secundarios]] | La diferencia entre índices por documento (locales) y por término (globales), y el riesgo de los índices globales asíncronos |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/05 Rebalanceo fijo dinámico y proporcional\|05 · Rebalanceo]] | Por qué `hash % N` es mala idea y cómo funcionan los shards fijos, la división dinámica, los rangos proporcionales y el hashing consistente |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/06 Enrutamiento y ejecución de consultas\|06 · Enrutamiento y consultas]] | Cómo llega una petición al nodo correcto, qué hace un servicio de coordinación y dónde está el límite de las transacciones entre shards |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/07 Diseño integrado y decisiones\|07 · Diseño integrado]] | Cómo encadenar todas las decisiones anteriores en un diseño coherente y qué señales indican que algo va mal |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/08 Laboratorio y repaso resuelto\|08 · Laboratorio y repaso]] | Resolver cálculos de movimiento de datos, latencia de cola, salado y reparto de rangos con respuestas explicadas |

## Mapa de secciones del libro

| Sección del capítulo | PDF | Impresas | Figuras | Nota |
|---|---|---|---|---|
| Introducción y recuadro *Sharding and Partitioning* | 1–2 | 251–252 | 7-1 | 01 |
| *Pros and Cons of Sharding* (incluye sharding en una máquina) | 3–4 | 253–254 | — | 01 |
| *Sharding for Multitenancy* | 4–5 | 254–255 | — | 01 |
| *Sharding of Key-Value Data* (sesgo, hot spot, hot key) | 5–6 | 255–256 | — | 01 y 02 |
| *Sharding by Key Range* y su rebalanceo | 6–8 | 256–258 | 7-2 | 02 y 05 |
| *Sharding by Hash of Key*: módulo N y número fijo de shards | 8–11 | 258–261 | 7-3, 7-4 | 05 |
| *Sharding by hash range*, recuadro de almacenes de datos | 11–13 | 261–263 | 7-5, 7-6 | 03 y 05 |
| *Consistent hashing* | 13 | 263 | — | 05 |
| *Skewed Workloads and Relieving Hot Spots* | 13–14 | 263–264 | — | 02 |
| *Operations: Automatic Versus Manual Rebalancing* | 14–15 | 264–265 | — | 05 |
| *Request Routing* | 15–18 | 265–268 | 7-7, 7-8 | 06 |
| *Sharding and Secondary Indexes*: locales y globales | 18–21 | 268–271 | 7-9, 7-10 | 04 |
| *Summary* | 21–22 | 271–272 | — | 07 |

La equivalencia es constante: **página impresa = página PDF + 250**. Se comprobó con los pies de página impresos 251, 252, 254–258, 260–263 y 265–272.

## Cómo estudiar el capítulo

Las notas 01 a 03 construyen el vocabulario: qué es un shard, qué es la clave de partición y cómo se asigna una clave a un shard. La 04 añade el problema que más sorprende en la práctica: buscar por algo que no es la clave de partición. La 05 y la 06 tratan la operación del clúster (mover datos y encontrarlos). La 07 lo junta todo en un diseño completo y la 08 sirve para comprobar que puedes hacer los cálculos sin mirar las notas.

**PDF del capítulo:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/07 Sharding.pdf#page=1|07 Sharding.pdf · PDF 1 · impresa 251]].

---

**Empezar:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/01 Shards réplicas y carga|01 · Shards, réplicas y carga →]]

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|← Capítulo 6]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/01 Shards réplicas y carga|Primera nota →]]
