---
title: "DDIA — Capítulo 5 · Codificación y evolución"
created: 2026-09-25
tags:
  - lecturas/ddia
  - indice
---

# Capítulo 5 · Codificación y evolución

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|← Inicio del libro]]

**Pregunta central:** Cómo intercambiar y conservar datos cuando conviven distintas versiones de programas.

Lee las notas del 01 al 07. El número de cada nota ordena el estudio dentro del capítulo. Los enlaces al pie permiten avanzar sin volver a buscar en la carpeta.

| Nota | Lo que podrás explicar |
|---|---|
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/01 Evolución y compatibilidad\|01 · Evolución y compatibilidad]] | Las dos direcciones de compatibilidad y la pérdida de campos al reescribir |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/02 JSON XML CSV y esquemas\|02 · JSON, XML, CSV y esquemas]] | Qué se pierde entre bytes, tipos y significado; qué valida un esquema |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/03 Protocol Buffers y números de campo\|03 · Protobuf]] | Por qué la identidad de un campo vive en su número y por qué no debes reciclarlo |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/04 Avro y resolución de esquemas\|04 · Avro]] | Cómo resolver el esquema escritor contra el lector y qué hacen los defaults |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/05 Bases de datos APIs y RPC\|05 · Bases, APIs y RPC]] | Cómo cambian los papeles de lector y escritor y por qué un timeout deja incertidumbre |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/06 Workflows durables e idempotencia\|06 · Workflows e idempotencia]] | Qué recuerda un historial y qué efectos externos todavía pueden repetirse |
| [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/07 Mensajería actores y repaso\|07 · Mensajes y actores]] | Qué desacopla un broker y qué contratos siguen siendo necesarios |

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/02-compatibilidad-lectores.png|900]]

*Nuevo lee viejo: hacia atrás. Viejo lee nuevo: hacia delante. La imagen muestra el objetivo de compatibilidad, no una garantía de cualquier cambio.*

**Al terminar:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/00 Índice|Aplicar y repasar los dos capítulos]].
