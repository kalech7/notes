---
title: "82 S07 - HNSW capas conexiones y exploración"
created: 2026-09-29
fecha: 2026-09-22
capitulo: 7
sesion: "07"
tags:
  - maestria/ia-generativa
  - recuperacion
  - bases-vectoriales
---

# 82 S07 - HNSW capas conexiones y exploración

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/79 S07 - Guía de búsqueda vectorial e índices|Guía de sesión 07]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

**HNSW**, *Hierarchical Navigable Small World*, usa un grafo de proximidad con varias capas. Un grafo es una colección de nodos unidos por aristas; aquí los nodos representan vectores y las conexiones ofrecen rutas para llegar a candidatos cercanos sin revisar toda la base.

## 1. Por qué hay capas

La capa base contiene todos los vectores. Capas superiores contienen subconjuntos, asignados mediante el procedimiento de construcción. Esa organización permite orientar primero la búsqueda con pocos nodos y después refinarla entre más vecinos.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/59-s07-hnsw-capas.png|59-s07-hnsw-capas.png]]

Los rectángulos azules representan nodos y las líneas su conectividad esquemática. Las flechas anaranjadas indican descender después de encontrar una zona prometedora. Los nodos superiores también existen abajo. El dibujo usa conexiones ordenadas para explicar la jerarquía; no reproduce un grafo real ni una trayectoria medida.

La analogía de vuelos y taxi expresa escalas de navegación. No significa que cada conexión superior de todo grafo real sea necesariamente más larga que cada conexión inferior. Importan la jerarquía y las opciones de navegación.

## 2. Qué hace una consulta

En términos simplificados, comienza por un punto de entrada superior, se mueve hacia vecinos que mejoran la cercanía y desciende. En la capa base explora un conjunto de candidatos y mantiene opciones de expansión, en lugar de tomar una sola decisión irrevocable en cada nodo.

El recorrido puede perder recall cuando la estructura o el presupuesto de exploración no permiten descubrir una zona que contiene mejores vecinos. No es exactamente la pérdida por omitir una celda de IVF: es una restricción de navegación en el grafo.

## 3. Parámetros de consulta y construcción

| Parámetro | Momento | Qué modifica principalmente |
| --- | --- | --- |
| `ef_search` / `efSearch` | Consulta | Amplitud de exploración y lista de candidatos mantenida |
| M | Construcción | Configuración del número de conexiones por nodo |
| `ef_construction` / `efConstruction` | Construcción | Esfuerzo de búsqueda de vecinos al insertar y construir |

Los nombres exactos y restricciones dependen de la biblioteca. `ef_search` **no equivale exactamente al total de distancias calculadas** ni al número k de resultados. Mantener una lista más grande suele permitir mejor exploración y cuesta más trabajo.

M tampoco es una descripción exacta de todos los grados: ciertas implementaciones permiten más conexiones en la capa base. Subir M suele aumentar memoria y costo de construcción. Aumentar `ef_construction` mejora oportunidades de construir conexiones útiles, pero no se traduce necesariamente en más memoria final si M queda fijo; también requiere memoria y tiempo transitorios durante construcción.

## 4. Cambiar durante consulta o reconstruir

Bajar `ef_search` es una intervención de consulta que normalmente se prueba sin reconstruir el grafo. Si el recall cae demasiado, se revierte. Cambiar M o la calidad de construcción para los puntos ya existentes puede requerir reconstruir; una configuración nueva para futuras inserciones no rehace mágicamente las conexiones antiguas.

El PDF dice que cambiar un parámetro de consulta «cuesta nada». La precisión es que evita el costo de reconstrucción, pero **sí cambia el trabajo y el resultado de cada búsqueda**.

## 5. Cómo interpretar la pregunta recall 0,99 y p99=800 ms

Recall 0,99 es similitud de resultados frente al exacto. p99=800 ms significa un percentil de latencia. No son dos versiones de la misma métrica.

Si se quiere reducir latencia conservando suficiente recall, probar un `ef_search` menor sobre un conjunto representativo es una primera intervención razonable. `nprobe` es de IVF, no de este índice HNSW. Reindexar con menos vectores cambia la cobertura de la base. Subir M cambia construcción y memoria y no promete automáticamente bajar ese percentil.

La prueba debería medir distribución de latencia y recall, bajo misma carga y consultas. Una mejor mediana puede coexistir con un p99 peor.

## 6. Límites de las afirmaciones de complejidad y memoria

El artículo de [Malkov y Yashunin](https://arxiv.org/abs/1603.09320) describe la jerarquía, asignación aleatoria de niveles y navegación. La escala logarítmica observada y analizada no significa garantía uniforme $O(\log N)$ para cualquier base, parámetro y consulta; además existe costo por dimensión y exploración.

El esquema clásico usa vectores y grafo en memoria, pero los motores pueden ofrecer variantes de almacenamiento. Borrar e insertar son problemas de implementación: una biblioteca puede restringir eliminaciones y un servicio puede manejarlas con marcas y mantenimiento. «Insertar es barato» necesita comparador, carga y grado de actualización definidos.

> [!question]- ¿IVF o HNSW tiene siempre mejor curva?
> No se puede concluir sin configuración, corpus, métricas y hardware. El PDF no mide ambos y estas notas tampoco presentan una comparación experimental entre ellos.

Fuente: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-07.pdf#page=11|PDF 11–14]]. Complemento: artículo primario enlazado y [referencia oficial de índices Faiss](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes). Las precisiones evitan convertir tendencias en garantías.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/81 S07 - IVF celdas centroides y nprobe|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/83 S07 - Recall del índice latencia y memoria|Siguiente]] →
