---
title: "Database Internals — Capítulo 5 · Procesamiento de transacciones y recuperación"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/transacciones
---

# Capítulo 5 · Procesamiento de transacciones y recuperación

[[Obsidian/lecturas/database internals/00 Empieza aquí|← Inicio del libro]]

Este capítulo explica cómo las páginas y B-Trees ya estudiados se vuelven parte de un sistema que puede confirmar transacciones, atender concurrencia y recuperarse de un fallo. La pregunta que une las notas es: **¿qué información y qué coordinación hacen falta para conservar un resultado correcto?**

Las notas desarrollan el material en español, con términos definidos, ejemplos completos y preguntas resueltas. Diez gráficos explican mecanismos concretos; algunos adaptan figuras del libro y otros desarrollan ejemplos propios. Cada imagen está explicada en la nota donde aparece.

## Ruta del capítulo

| Nota | Qué podrás explicar | PDF · impresas |
|---|---|---|
| [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/01 Transacciones ACID y componentes\|01 · Transacciones y ACID]] | Separar atomicidad, consistencia, aislamiento y durabilidad; conectar los componentes | 1–2 · 79–80 |
| [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/02 Caché de páginas y gestión de buffers\|02 · Caché de páginas]] | Distinguir páginas, frames, dirty, pinning, flush y eviction | 3–7 · 81–85 |
| [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/03 Reemplazo de páginas FIFO LRU CLOCK y TinyLFU\|03 · Políticas de reemplazo]] | Predecir víctimas y comparar recencia, segunda oportunidad y frecuencia | 7–10 · 85–88 |
| [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/04 WAL checkpoints y registros de recuperación\|04 · WAL y checkpoints]] | Explicar el orden de persistencia, LSN, logging y límites del checkpoint | 10–13 · 88–91 |
| [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/05 Políticas steal force y recuperación ARIES\|05 · Steal, force y ARIES]] | Decidir cuándo faltan redo y undo y resolver un crash completo | 13–15 · 91–93 |
| [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/06 Aislamiento anomalías y serialización\|06 · Aislamiento y anomalías]] | Identificar lecturas sucias, fantasmas, actualización perdida y write skew | 16–19 · 94–97 |
| [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/07 Control optimista multiversión y orden temporal\|07 · OCC, MVCC y orden temporal]] | Entender validación, versiones y reglas de orden sin confundir técnicas con niveles | 15, 20–22 · 93, 98–100 |
| [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/08 Bloqueos transaccionales y deadlocks\|08 · Bloqueos y deadlocks]] | Comparar bloqueos, 2PL y resolución de ciclos de espera | 22–24 · 100–102 |
| [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/09 Latches y concurrencia en B-Trees\|09 · Latches y B-Trees]] | Comprender lectores/escritores, crabbing, upgrades y splits B-link | 25–30 · 103–108 |
| [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/10 Laboratorio y repaso resuelto\|10 · Laboratorio y repaso]] | Calcular reemplazos, recuperar fallos y comprobar dependencias con Python | Elaboración propia |

PDF de 31 páginas · capítulo 5, *Transaction Processing and Recovery* · páginas impresas 79–109. La correspondencia es **impresa = PDF + 78**. Dos páginas venían giradas y se revisaron rotadas. La última contiene lecturas adicionales y termina con una referencia bibliográfica cortada; los temas del capítulo y su resumen están presentes.

## Un ejemplo para orientar la lectura

Transferir 30 de una cuenta a otra requiere que ambos cambios se conserven juntos. Mientras se ejecuta, la caché guarda modificaciones en RAM, el control de concurrencia impide interacciones prohibidas y el WAL registra lo necesario para recuperarlas. Después de un fallo se distingue lo confirmado de lo incompleto. Las notas 01, 04 y 05 recorren esas mismas responsabilidades desde ángulos diferentes.

Si lo que más te interesa es entender fallos, sigue 01 → 02 → 04 → 05. Para concurrencia, sigue 01 → 06 → 07 → 08 → 09. El recorrido completo 01–10 deja claras las conexiones y termina en experimentos reproducibles.

## Precisiones que evitan errores

- Dirty no significa no confirmado; describe una diferencia entre RAM y disco.
- No-force de páginas no significa omitir la persistencia del WAL.
- ARIES repite historia y después deshace las transacciones incompletas.
- Snapshot isolation puede permitir write skew.
- Pin, lock y latch protegen aspectos distintos.

Se documentan las erratas y simplificaciones de la fuente sin trasladarlas a las explicaciones. La revisión de cobertura conserva páginas, figuras y cotejos complementarios.

[[Obsidian/lecturas/database internals/90 Fuentes y revisión/04 Cobertura y validación del capítulo 5|Fuentes, figuras y validación del capítulo 5]] · [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=1|PDF original conservado]].

**Continuidad:** [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/00 Índice|Capítulo 4]] → este capítulo → [[Obsidian/lecturas/database internals/05 Práctica y repaso/00 Índice|Repaso general de capítulos 1–4]]. La carpeta anterior «05 Práctica y repaso» conserva su nombre porque es material de apoyo; este índice corresponde al capítulo 5 del libro.

---

← [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/00 Índice|Capítulo anterior]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/01 Transacciones ACID y componentes|Siguiente →]]
