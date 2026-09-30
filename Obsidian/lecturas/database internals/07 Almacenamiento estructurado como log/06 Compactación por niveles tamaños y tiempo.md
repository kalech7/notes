---
title: "Database Internals — Capítulo 7 · Compactación por niveles tamaños y tiempo"
created: 2026-09-30
libro: "Database Internals"
capitulo: 7
tags:
  - lecturas/database-internals
  - arquitectura/lsm-trees
  - arquitectura/almacenamiento
---

# Compactación por niveles tamaños y tiempo

[[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice del capítulo 7]]

> [!abstract] El problema que queda pendiente
> Cada flush añade archivos y versiones. Compactar los organiza, pero la política decide cuántos datos antiguos reescribimos y cuántas fuentes tiene que leer una consulta.

## El trabajo común

La compactación elige tablas, recorre sus datos ordenados, reconcilia versiones y escribe salidas nuevas. Las entradas siguen disponibles hasta que las salidas completas se publican. Durante ese intervalo hacen falta **espacio temporal** y ancho de banda para mantener ambas generaciones.

La salida puede ser más pequeña por eliminar versiones innecesarias; también puede dividirse en varias tablas por rango. Compactaciones paralelas deben coordinar sus conjuntos de entrada y la publicación. Dos tareas no deben retirar incoherentemente el mismo archivo.

## Leveled compaction: niveles y rangos sin solapamiento

En **compactación por niveles**, L0 recibe los flushes y admite rangos superpuestos. Desde L1, las tablas de un mismo nivel cubren rangos que no se solapan. Cada nivel tiene una capacidad objetivo, normalmente creciente entre niveles.

Ejemplo propio: una tabla de L1 cubre `[20,50)` y en L2 hay `[0,30)`, `[30,60)` y `[60,90)`. Para moverla a L2 se compacta con las dos primeras tablas solapadas. La tercera puede quedar intacta. Las salidas se particionan para que L2 siga sin solapamiento interno.

Una búsqueda de 25 puede descartar rangos mediante metadatos. En un nivel L1 o posterior necesita como máximo una tabla candidata para esa clave, aunque aún debe considerar varios niveles y varias tablas de L0. El precio es que un movimiento puede reescribir muchos datos del nivel destino.

El crecimiento exponencial suele referirse a **capacidad total por nivel**; el tamaño objetivo de cada archivo puede tener una política independiente. No debemos deducir del esquema del libro que todo motor haga crecer exponencialmente cada SSTable.

## Size-tiered compaction: combinar tamaños parecidos

En **compactación por tamaños**, se agrupan archivos de volumen parecido. Cuatro tablas de 100 MB pueden generar una de alrededor de 400 MB, o menos si muchas versiones quedan ocultas. Esa salida pertenece al grupo correspondiente a su tamaño real.

Conservar varias tablas o runs grandes evita reescribir inmediatamente todo un nivel destino, pero mantiene más fuentes candidatas y más versiones durante más tiempo. La **inanición de tablas** ocurre cuando un grupo no vuelve a reunir suficientes candidatos: los borrados reducen las salidas, que regresan a grupos pequeños, mientras tablas viejas mayores se quedan sin compactar. Puede ser necesario forzar mantenimiento aunque no se alcance el umbral habitual.

## Ventanas de tiempo

Una política por **ventanas temporales** agrupa datos según su periodo de escritura. Si una ventana completa contiene solo datos expirados y no hay dependencias que obliguen a conservarlos, puede retirarse el archivo entero. **TTL**, tiempo de vida, es el plazo tras el cual un dato deja de ser válido.

La ventaja depende de la distribución real de expiraciones: mezclar datos con TTL distinto, introducir datos tardíos o conservar versiones referenciadas puede impedir retirar una tabla completa.

| Política | Organización que favorece | Costo que puede aumentar |
|---|---|---|
| Niveles | Pocos candidatos por nivel, menos redundancia | Reescribir rangos del nivel siguiente |
| Tamaños | Fusión de runs de tamaño parecido | Más runs, lecturas y espacio retenido |
| Tiempo | Retirar ventanas expiradas completas | Restricciones ante datos tardíos o expiración mezclada |

> [!question]- ¿Compactar siempre permite descartar tombstones?
> No. La selección de entradas debe abarcar todas las versiones que la marca oculta o demostrar que no hay otras, y respetar snapshots y condiciones de replicación. Reducir archivos y probar que un borrado es descartable son decisiones diferentes.

**Puente al siguiente tema:** las políticas muestran un intercambio entre lectura, escritura y espacio. Podemos darle medidas concretas a cada costo.

**Referencia:** PDF 13–15 · impresas 141–143 · figura 7-6. [[Obsidian/lecturas/database internals/Materiales/07 Almacenamiento estructurado como log.pdf#page=13|Fuente del capítulo]]. Los ejemplos propios se indican en el texto; las explicaciones son elaboración en español.

---

← [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/05 Merge iteration y reconciliación de versiones|Anterior]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/07 Almacenamiento estructurado como log/07 Amplificación y la conjetura RUM|Siguiente]] →
