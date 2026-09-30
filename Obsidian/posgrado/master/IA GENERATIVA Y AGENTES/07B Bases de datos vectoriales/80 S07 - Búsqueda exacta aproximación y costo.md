---
title: "80 S07 - Búsqueda exacta aproximación y costo"
created: 2026-09-29
fecha: 2026-09-22
capitulo: 7
sesion: "07"
tags:
  - maestria/ia-generativa
  - recuperacion
  - bases-vectoriales
---

# 80 S07 - Búsqueda exacta aproximación y costo

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/79 S07 - Guía de búsqueda vectorial e índices|Guía de sesión 07]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Una búsqueda **kNN**, de *k nearest neighbors*, devuelve los k vecinos más cercanos a una consulta según una medida declarada. Con coseno se suelen elegir los puntajes mayores; con distancia euclídea, los menores. «Vecino verdadero» en una evaluación del índice significa vecino según esa representación y medida, no verdad sobre el mundo.

## 1. Qué calcula la búsqueda exacta

La búsqueda exhaustiva compara el vector consulta $q$ con cada uno de los $N$ vectores de dimensión $d$. Para producto punto, cada comparación calcula:

$$q\cdot x=\sum_{j=1}^{d}q_jx_j$$

Una comparación usa aproximadamente d multiplicaciones y d−1 sumas. N comparaciones dan trabajo de orden $O(Nd)$. La notación O describe crecimiento asintótico, no un número de milisegundos. Además hay costo de seleccionar los k mejores y mover datos por memoria.

En el ejemplo del PDF:

$$N=10\,000\,000,\quad d=768$$
$$N\times d=7\,680\,000\,000$$

Es el conteo de multiplicaciones de un producto punto por vector, sin convertirlo en tiempo real ni asumir que todos los motores lo ejecutan con esa misma organización. Vectorización, GPU, lotes, selección top-k y caché cambian el tiempo.

**N** cuenta vectores; **d** cuenta coordenadas por vector; **k** cuenta resultados solicitados. Ninguna de esas cantidades es la longitud del prompt en tokens. Un documento dividido en muchas partes puede generar más de un vector, de modo que documentos y vectores tampoco tienen el mismo N.

## 2. «Exacto» tiene un alcance preciso

Si el índice devuelve el top-k exacto según coseno, no se deduce que todos los documentos respondan a la pregunta. Exactitud del algoritmo significa fidelidad a la operación solicitada sobre la base y representación disponibles. Puede haber empates: comparar listas de IDs necesita una política de desempate o una evaluación que acepte vecinos igualmente cercanos.

«Exacto no escala» es una advertencia sobre costo creciente. No significa que sea siempre inadecuado. Para una base pequeña, un exacto optimizado puede ser más simple y suficientemente rápido. Se decide con mediciones y requisitos de latencia, no con un umbral universal de volumen.

## 3. La aproximación reduce dónde se busca

**ANN**, *approximate nearest neighbors*, renuncia a garantizar siempre el mismo top-k que el exacto para examinar menos candidatos. La ganancia se mide con recall del índice, latencia y memoria. No debe asumirse que devuelve «casi siempre» lo correcto sin medir la configuración.

IVF selecciona regiones o celdas; HNSW explora conexiones de un grafo. En ambos casos puede no llegar al vecino que el exacto habría encontrado. Más exploración suele recuperar parte de lo perdido a cambio de trabajo.

## 4. Por qué un KD-tree puede ayudar menos en alta dimensión

Un KD-tree divide el espacio y usa distancias a regiones para descartar ramas. Si muchas regiones no pueden descartarse, la consulta debe visitar muchas y se acerca al trabajo exhaustivo. El deterioro depende de distribución, dimensión efectiva, métrica y consulta; «todos los árboles se vuelven fuerza bruta» es una simplificación demasiado amplia.

Esta dificultad no prueba que coseno sea siempre mejor que euclídea. Elegir una medida y organizar una búsqueda son problemas distintos. Para vectores unitarios, coseno y distancia euclídea incluso producen el mismo ranking, según la derivación de [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07 Embeddings y recuperación/31 S06 - Coseno producto punto y normalización|31 S06 - Coseno producto punto y normalización]].

## 5. Cómo hacer una comparación útil

Se fijan base de vectores, consultas, métrica y k; se obtiene el exacto como referencia y se compara el aproximado. La generación de embeddings puede medirse aparte. También hay que declarar calentamiento, lotes, hardware, concurrencia y si la lectura de disco está incluida.

Cambiar simultáneamente embedding, medida e índice impide atribuir el efecto solo a ANN. Si se aplican filtros, la referencia exacta debe usar el **mismo subconjunto elegible**.

> [!question]- ¿Pedir k=5 significa comparar solo cinco vectores?
> No. k fija cuántos resultados se devuelven. Una búsqueda exhaustiva puede comparar todos los vectores y después seleccionar cinco.

Fuente: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-07.pdf#page=4|PDF 4–5]]. Las precisiones de medición y empates son ampliación propia; la documentación de [índices de Faiss](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes) distingue búsqueda exhaustiva y métodos que examinan subconjuntos.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/79 S07 - Guía de búsqueda vectorial e índices|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/81 S07 - IVF celdas centroides y nprobe|Siguiente]] →
