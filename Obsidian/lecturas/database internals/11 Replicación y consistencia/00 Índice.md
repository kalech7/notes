---
title: "Database Internals — Capítulo 11 · Índice"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Índice

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]]

Replicar aumenta las posibilidades de seguir operando cuando fallan componentes y obliga a decidir qué significa ver una escritura. Este capítulo explica esa decisión mediante registros, historias y contratos de consistencia; después desarrolla sesiones, quórums, testigos y tipos que convergen por construcción.

Se cubre **todo el capítulo 11 compartido**, PDF 19–45, impresas 215–241, incluido el resumen. La relación es **impresa = PDF + 196**, sin páginas faltantes dentro de ese tramo. Las explicaciones se basan en la fuente; los casos nuevos y el laboratorio se identifican como elaboración propia. Las menciones de productos reflejan ejemplos del libro, no información verificada sobre versiones actuales.

## Ruta de lectura

| Nota | Qué permite entender |
|---|---|
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/01 Replicar para tolerar fallas\|01 Replicar para tolerar fallas]] | Copias, failover y tres momentos |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/02 CAP PACELC y sus límites\|02 CAP PACELC y sus límites]] | Qué se puede prometer durante una partición |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/03 Disponibilidad parcial harvest y yield\|03 Disponibilidad parcial harvest y yield]] | Cómo medir servicio degradado |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/04 Registros e intervalos concurrentes\|04 Registros e intervalos concurrentes]] | Qué significa solaparse y qué puede devolver un registro |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/05 Modelos como contratos de visibilidad\|05 Modelos como contratos de visibilidad]] | Cómo restringir historias posibles |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/06 Linealizabilidad puntos de efecto y costo\|06 Linealizabilidad puntos de efecto y costo]] | Puntos de efecto, CAS, ABA y composición |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/07 RIFL reintentos y efectos únicos\|07 RIFL reintentos y efectos únicos]] | Deduplicación durable y leases |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/08 Consistencia secuencial y composición\|08 Consistencia secuencial y composición]] | Un orden común que no exige precedencia real |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/09 Consistencia causal y dependencias\|09 Consistencia causal y dependencias]] | Publicar dependientes cuando llega su contexto |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/10 Relojes vectoriales y conflictos\|10 Relojes vectoriales y conflictos]] | Detectar ramas sin inventar una fusión |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/11 Garantías de sesión y PRAM\|11 Garantías de sesión y PRAM]] | Qué conserva cada cliente al cambiar de réplica |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/12 Consistencia eventual y convergencia\|12 Consistencia eventual y convergencia]] | Por qué eventual no es una cota de segundos |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/13 N R W quórums y sus límites\|13 N R W quórums y sus límites]] | Intersección, mayorías y escritura incompleta |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/14 Réplicas testigo y reparación\|14 Réplicas testigo y reparación]] | Cuándo metadatos necesitan un dato temporal |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/15 CRDTs contadores registros y conjuntos\|15 CRDTs contadores registros y conjuntos]] | Convergencia diseñada y sus restricciones |
| [[Obsidian/lecturas/database internals/11 Replicación y consistencia/16 Laboratorio y repaso resuelto\|16 Laboratorio y repaso resuelto]] | Modelo reproducible y 12 respuestas explicadas |

## Figuras y precisiones

La figura 11-1 se desarrolla en la nota 04; las 11-2, 11-3 y 11-4 en la 06; la 11-5 en la 08; las 11-6, 11-7 y 11-8 en la 09; la 11-9 en la 10. Ocho PNG conceptuales propios complementan las explicaciones; su script está en [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 11/generar_graficos.py|generar_graficos.py]]. No contienen mediciones de latencia ni series empíricas.

Las notas separan linealizabilidad de atomicidad e invariantes ACID, explicitan el orden asumido en la figura 11-2 y distinguen una operación pendiente de un efecto parcial. También aclaran que intersección de quórums no basta para linealizabilidad, que metadatos testigo no reemplazan el valor y que los CRDTs requieren reglas de entrega y fusión concretas.

**Cobertura y validación:** [[Obsidian/lecturas/database internals/90 Fuentes y revisión/08 Cobertura y validación de detección liderazgo y replicación|Mapa de páginas y revisión]]. La reparación de lectura y anti-entropía sólo se introducen en el nivel explicado aquí: el capítulo 12 no forma parte del PDF compartido.

**Referencia:** PDF 19–45 · impresas 215–241. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=19|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Capítulo 10]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/01 Replicar para tolerar fallas|Siguiente]] →
