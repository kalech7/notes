---
title: "DDIA — Capítulo 6 · Replicación"
created: 2026-09-29
capitulo: 6
tags:
  - lecturas/ddia
  - arquitectura/replicacion
---

# Capítulo 6 · Replicación

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|← Inicio del libro]]

**Pregunta central:** cómo mantener copias de datos que cambian, conservar lo confirmado y dar lecturas comprensibles cuando hay retrasos, fallos o ediciones concurrentes.

El capítulo empieza con un solo líder, estudia qué puede ver el usuario durante el retraso de replicación y después desarrolla multilíder y sistemas sin líder. La segunda edición incluye almacenamiento de objetos, motores de sincronización y software local-first; las notas mantienen esos temas del escaneo.

## Ruta de lectura

| Nota |
|---|
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/01 Por qué replicar y cómo funciona un líder\|01 Por qué replicar y cómo funciona un líder]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/02 Sincronía confirmaciones y durabilidad\|02 Sincronía confirmaciones y durabilidad]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/03 Snapshots recuperación y failover\|03 Snapshots recuperación y failover]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/04 Logs físicos lógicos y almacenamiento de objetos\|04 Logs físicos lógicos y almacenamiento de objetos]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/05 Retraso y lectura de tus propias escrituras\|05 Retraso y lectura de tus propias escrituras]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/06 Lecturas monótonas causalidad y garantías\|06 Lecturas monótonas causalidad y garantías]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/07 Multilíder regiones topologías y orden causal\|07 Multilíder regiones topologías y orden causal]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/08 Sync engines y software local-first\|08 Sync engines y software local-first]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/09 Conflictos LWW siblings y reglas del dominio\|09 Conflictos LWW siblings y reglas del dominio]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/10 CRDT y transformación operacional\|10 CRDT y transformación operacional]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/11 Sin líder reparación y cuórums\|11 Sin líder reparación y cuórums]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/12 Límites de cuórums rendimiento y regiones\|12 Límites de cuórums rendimiento y regiones]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/13 Causalidad versiones y vectores\|13 Causalidad versiones y vectores]] |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/14 Laboratorio y repaso resuelto\|14 Laboratorio y repaso resuelto]] |

Las notas 01–04 explican el mecanismo y la recuperación. Las 05–06 explican las garantías de lectura con historias concretas. Las 07–10 desarrollan escritura en varias regiones o dispositivos y resolución de conflictos. Las 11–13 explican cuórums y cómo registrar conocimiento causal. La 14 permite practicar con un programa pequeño y preguntas resueltas. Cada imagen tiene una explicación en prosa debajo; los dibujos adaptan las figuras del libro al español.

## Correspondencia con el libro

| Sección | PDF | Impresas | Notas |
|---|---|---|---|
| Introducción, backups y un líder | 1–3 | 197–199 | 01 |
| Síncrona y asíncrona | 4–5 | 200–201 | 02 |
| Crear seguidores y recuperar nodos | 5–6, 8–10 | 201–202, 204–206 | 03 |
| Almacenamiento de objetos y logs | 6–7, 10–12 | 202–203, 206–208 | 04 |
| Lag y leer tus propias escrituras | 13–15 | 209–211 | 05 |
| Regiones, monotonía, prefijo y garantías | 16–19 | 212–215 | 06 |
| Multilíder, regiones y topologías | 19–24 | 215–220 | 07 |
| Sync engines y local-first | 24–26 | 220–222 | 08 |
| Conflictos, LWW y siblings | 26–30, 32–33 | 222–226, 228–229 | 09 |
| Fusión automática, CRDT y OT | 30–32 | 226–228 | 10 |
| Sin líder, reparación y cuórums | 33–37 | 229–233 | 11 |
| Límites, rendimiento y multirregión | 37–41 | 233–237 | 12 |
| Causalidad, versiones y vectores | 41–46 | 237–242 | 13 |
| Resumen y laboratorio propio | 47–48 | 243–244 | 14 |

**Impresa = PDF + 196.** El escaneo tiene 48 páginas consecutivas. El texto del capítulo llega al resumen y a las dos primeras referencias bibliográficas; el resto de esa bibliografía no está adjunto.

Referencia: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=1|PDF 1 · impresa 197]]. Las explicaciones no requieren abrirla.

---

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/00 Índice|← Capítulo 5]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/01 Por qué replicar y cómo funciona un líder|Empezar →]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|Capítulo 7 →]]
