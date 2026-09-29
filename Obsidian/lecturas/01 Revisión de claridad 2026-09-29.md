---
title: "Revisión de claridad de las lecturas — 29 de septiembre de 2026"
created: 2026-09-29
tags:
  - lecturas
  - revision
---

# Revisión de claridad de las lecturas

[[Obsidian/lecturas/00 Índice de lecturas|← Biblioteca de lecturas]]

Las notas tienen una buena base para estudiar: explican problemas antes de introducir soluciones, usan ejemplos propios y ofrecen preguntas con respuestas. La revisión busca corregir puntos donde una simplificación cambia el significado, falta vocabulario previo o un ejemplo necesita indicar sus condiciones.

## Alcance

La revisión se distribuyó entre tres subagentes y una revisión principal. Incluye las 188 notas Markdown que había al comenzar: 115 de *Fundamentals of Software Architecture*, 42 de *Database Internals*, 30 de *Designing Data-Intensive Applications* y el índice general. El conteo incluye índices, glosarios y notas auxiliares.

Se conservaron la estructura, las referencias y los cambios que ya existían. Esta revisión es editorial y conceptual: no sustituye un cotejo completo de cada nota con cada página del libro. Las comprobaciones técnicas dudosas se contrastaron con documentación primaria indicada junto a las explicaciones.

| Libro | Archivos revisados | Archivos mejorados |
|---|---:|---:|
| Fundamentals of Software Architecture | 115 | 39 |
| Database Internals | 42 | 24 |
| Designing Data-Intensive Applications | 30 | 15 |
| Índice general | 1 | 1 |

Se mejoraron 78 archivos de los libros y se actualizó el índice general. Esta nota de revisión es un archivo nuevo, adicional a los 188 revisados.

## Mejoras principales

- **Arquitectura de software:** definiciones de contrato, POC, invariantes, cohesión y pruebas. Se explicitaron las condiciones de la ley de Little y la diferencia entre distribuir mensajes y evitar que circulen campos privados. En monolito modular se separaron aislamiento de fallos, escalado del conjunto y dependencias de código; también se corrigieron referencias desactualizadas a la cobertura del capítulo 11.
- **Database Internals:** distinción entre orden lógico y ubicación física, entre niveles y altura del árbol, y entre identificar una celda y ordenar sus referencias. Se corrigieron ejemplos de fusión, búsqueda y borrado para conservar sus condiciones de ocupación y visibilidad. El flujo de inserción ahora decide cuánto contenido queda dentro de la página antes de comprobar si cabe.
- **DDIA:** siglas definidas al aparecer, operaciones binarias y distancias explicadas paso a paso, un ejemplo numérico de `recall@k` y reglas más precisas de WAL e idempotencia. Se corrigió el enlace a la nota de ETL.

## Por dónde volver a leer

Estas notas concentran cambios útiles para evitar confusiones:

- [[Obsidian/lecturas/Fundamentals of Software Architecture/05 Identificar y priorizar características/03 Requisitos implícitos y promedios|Promedios y capacidad]]: un promedio de llegadas no describe por sí solo los picos ni el período inicial de acumulación.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/02 Pensamiento arquitectónico/08 Preguntas y ejercicio resuelto|Ejercicio de historial]]: separar consumidores no elimina automáticamente información privada del mensaje.
- [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/07 Características y cuándo usarlo|Monolito modular: características y elección]]: las limitaciones de aislamiento entre módulos no significan ausencia absoluta de tolerancia a fallos del sistema.
- [[Obsidian/lecturas/database internals/03 Formatos de archivo/04 Slotted pages e indirección|Slotted pages]]: distinguir un slot de identidad estable de una posición en un directorio ordenado.
- [[Obsidian/lecturas/database internals/04 Implementación de B-Trees/03 Búsqueda binaria y breadcrumbs|Búsqueda binaria]]: cuándo se necesita el primer valor mayor o igual y cuándo el estrictamente mayor.
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/03 B-trees WAL y costos de almacenamiento|B-trees y WAL]]: orden de persistencia y confirmación al cliente.
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/07 Índices espaciales texto completo y vectores|Vectores y recuperación]]: símbolos, distancias y cálculo de recuperación de vecinos.
- [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/06 Workflows durables e idempotencia|Workflows e idempotencia]]: conservar un efecto al repetir una operación y cómo conseguirlo.

## Comprobación final

- Se comprobaron los destinos locales de los wikilinks y los enlaces Markdown detectados, incluidos los recursos insertados. Se reparó el enlace de DDIA a ETL.
- Las 143 referencias a páginas concretas de PDF quedaron dentro del rango de sus documentos.
- Los 111 bloques Mermaid se convirtieron a SVG sin errores tras reparar un punto y coma en un diagrama de secuencia. También se comprobaron los diagramas modificados para que acompañen las explicaciones corregidas.
- El YAML presente es válido. Se conservaron las convenciones de archivos auxiliares: README y prompts de arquitectura no tienen encabezado YAML, y el glosario completo de Database Internals no declara fecha de creación. No se inventó una fecha histórica.

La comprobación se realizó con analizadores locales y Mermaid en un navegador sin interfaz. No incluye inspección visual de todas las imágenes existentes, validación dentro de Obsidian ni ejecución de todos los ejemplos contra motores reales. Los PDF, Canvas y recursos visuales existentes se conservaron.

## Para estudiar sin añadir más texto

Sigue el orden del índice de cada libro. Las notas de apoyo pueden consultarse cuando hagan falta; no es necesario memorizarlas antes. Para comprobar comprensión, cambia un dato del ejemplo y explica qué resultado cambia y por qué. Si puedes repetir la definición pero no predecir esa consecuencia, vuelve al mecanismo y al ejercicio resuelto.
