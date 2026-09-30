---
title: "Database Internals — Capítulo 7 · Síntesis de la Parte I buffering mutabilidad y orden"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/motores-de-almacenamiento
  - arquitectura/almacenamiento
---

# Síntesis de la Parte I buffering mutabilidad y orden

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] Un cierre que conecta los capítulos
> Ya podemos describir un motor con preguntas más precisas que el nombre de su árbol: ¿acumula cambios antes de integrarlos?, ¿sobrescribe su representación física?, ¿qué datos permanecen ordenados?

## Los tres ejes de la conclusión

**Buffering** significa acumular actualizaciones para procesarlas en lotes. La tabla del libro usa el término para los mecanismos de la estructura, no para cualquier buffer del SO, WAL o caché. **Mutabilidad** se refiere a modificar en el lugar las representaciones del diseño; un motor con archivos inmutables sigue ofreciendo actualizaciones lógicas. **Orden** describe la disposición de registros y no basta por sí solo para deducir qué consultas admite una API.

La figura I-1 de las impresas 165–166 sintetiza las estructuras de la Parte I. La tabla siguiente conserva su clasificación y explicita las notas a pie:

| Estructura del libro | Buffering en su estructura | Representación mutable | Registros ordenados |
|---|---|---|---|
| B+Tree clásico | No | Sí | Sí |
| WiredTiger, variante descrita | Sí | Sí | Sí |
| LA-Tree | Sí | Sí | Sí |
| Copy-on-write B-Tree | No | No | Sí |
| LSM de dos componentes | Sí | No | Sí |
| LSM multicomponente | Sí | No | Sí |
| FD-Tree | Sí | No | Sí |
| Bitcask | No | No | No |
| WiscKey | Sí, para las claves | No | Sí, para las claves |
| Bw-Tree | No, según este eje del cuadro | No | Solo las bases consolidadas |

El “No” de buffering para Bw-Tree no niega buffers de flush en LLAMA. Clasifica el mecanismo del índice frente a árboles que acumulan lotes por rango. Del mismo modo, “mutable” para WiredTiger refleja el tratamiento del índice del capítulo; no exige que cada checkpoint sobrescriba el mismo offset físico.

## Tres contrastes que evitan confusiones

**CoW frente a LSM:** ambos pueden conservar representaciones físicas inmutables. CoW crea páginas nuevas para un camino del árbol y publica una raíz; la LSM agrupa muchos registros en una memtable y publica tablas que después compacta. Coinciden en un eje y pagan costos distintos en otro.

**WiscKey frente a Bitcask:** ambos mantienen valores en logs sin orden de clave. WiscKey conserva un índice LSM ordenado que puede recorrerse por rango; Bitcask usa un keydir hash completo en memoria. El orden de claves del primero no convierte sus valores en contiguos.

**Bw-Tree y rangos:** sus deltas físicos pueden estar dispersos y no formar una secuencia ordenada. El nodo lógico se reconstruye a partir de base y deltas, y el árbol organiza las claves para navegar y consultar. La clasificación “No” con nota a pie no significa que carezca de consultas por rango.

## Buffering reduce trabajo presente y puede aplazar otro

En un árbol mutable, combinar diez cambios de la misma página antes de escribirla puede ahorrar nueve escrituras respecto a escribirla cada vez. En un LSM, agruparlos mejora el flush, pero mover registros entre tablas añade escrituras futuras. Buffering e inmutabilidad resuelven problemas diferentes y suelen combinarse.

La inmutabilidad facilita lectores sobre imágenes estables y páginas densas; no prueba que el espacio total sea mínimo. Las versiones viejas y los snapshots pueden mantener datos adicionales. El cierre del libro describe tendencias del diseño, que deben relacionarse con esas condiciones.

## De arquitectura a funcionamiento completo

Las estructuras son una parte del motor. Formatos binarios, gestión de memoria, WAL, recuperación, aislamiento, publicación de vistas y reclamación física convierten el índice en un sistema correcto. Para leer código de un motor sirve preguntar dónde aparecen estos mecanismos y cómo se conectan, no buscar únicamente una implementación de “árbol”.

Los avances mencionados al final —estructuras probabilísticas, aprendizaje automático y memoria no volátil— se presentan como líneas de investigación en el contexto del libro. La lección duradera es reconocer qué costo cambia una propuesta nueva y qué garantías conserva.

> [!question]- ¿Dos motores en la misma fila conceptual tendrán igual rendimiento?
> No. Estos ejes no incluyen todas las decisiones de caché, compresión, selección de compactaciones, formato, concurrencia o hardware. Sirven para explicar mecanismos, no para reemplazar una medición de la carga concreta.

**Puente al laboratorio:** usaremos versiones, snapshots, filtros y compactación en un modelo pequeño para comprobar las reglas y calcular sus costos.

**Referencia:** PDF 35–36 · impresas 165–166 · figura I-1. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=35|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/13 Logs apilados FTL y cooperación con LLAMA|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/15 Laboratorio y repaso resuelto|Siguiente]] →
