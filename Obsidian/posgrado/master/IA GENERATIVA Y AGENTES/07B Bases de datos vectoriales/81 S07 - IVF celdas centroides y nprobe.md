---
title: "81 S07 - IVF celdas centroides y nprobe"
created: 2026-09-29
fecha: 2026-09-22
capitulo: 7
sesion: "07"
tags:
  - maestria/ia-generativa
  - recuperacion
  - bases-vectoriales
---

# 81 S07 - IVF celdas centroides y nprobe

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/79 S07 - Guía de búsqueda vectorial e índices|Guía de sesión 07]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

**IVF**, de *inverted file*, organiza vectores en listas asociadas a regiones. La metáfora del archivador ayuda: en vez de revisar todas las carpetas, se eligen algunas a partir de su cercanía a la consulta. En la variante IVFFlat, los candidatos elegidos conservan vectores sin compresión y se comparan con la medida correspondiente.

## 1. Construir y consultar son dos fases

Al construir, k-means puede aprender `nlist` centroides: centros representativos de grupos. Cada vector se asigna a una celda según el cuantizador y se guarda en su lista. Aprender esos centroides es entrenamiento del **índice**, no ajuste del modelo que produjo embeddings.

Al consultar se comparan los centroides con la consulta, se eligen `nprobe` listas y se examinan los vectores dentro de ellas. La lista corta final se forma con los mejores candidatos encontrados. `nlist` y `nprobe` no tienen que coincidir con k, que sigue siendo el número de resultados.

## 2. Cómo se pierde un vecino en una frontera

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/57-s07-ivf-frontera.png|57-s07-ivf-frontera.png]]

Las cajas superiores representan dos celdas en una dimensión. La consulta 0,10 está más cerca del centroide +1 que del centroide −1: distancias 0,90 y 1,10. Por eso se abre primero la celda derecha. Sin embargo, el punto A en −0,05 dista 0,15, menos que el punto B en +0,50, que dista 0,40. Con `nprobe=1` se devuelve B porque A ni siquiera se examinó. Abrir ambas celdas permite encontrar A.

La propiedad decisiva es que **la proximidad al centroide no equivale a proximidad a cada punto de la celda**. En la actividad física del PDF, la frontera del aula representa esta misma posibilidad. No hace falta una simulación de clase para entender el mecanismo.

## 3. Costo aproximado de las comparaciones

Si N vectores están distribuidos equilibradamente entre `nlist` listas, cada lista contiene aproximadamente $N/\text{nlist}$ vectores. El conteo simplificado es:

$$C\approx\text{nlist}+\frac{N}{\text{nlist}}\,\text{nprobe}$$

El primer sumando cuenta comparaciones con centroides; el segundo, comparaciones con vectores candidatos. Para aproximar trabajo por coordenadas se incorpora d. Si las listas están desequilibradas, hay que sumar los tamaños reales de las listas elegidas.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/58-s07-ivf-comparaciones.png|58-s07-ivf-comparaciones.png]]

Las barras muestran la fórmula evaluada para N=100000 y nlist=64. El eje mide comparaciones, no tiempo. Abrir 16 listas examina unas 25064 entidades contando centroides, frente a 100000 vectores del exhaustivo. Ese cociente no es una aceleración medida: los accesos dispersos y la coordinación tienen costos diferentes.

| nprobe | Comparaciones aproximadas |
| --- | ---: |
| 1 | 1626,5 ≈ 1627 |
| 2 | 3189 |
| 4 | 6314 |
| 8 | 12564 |
| 16 | 25064 |

La fracción 0,5 surge de una media teórica de tamaños: no se ejecutan «medias comparaciones» en una consulta real.

## 4. Qué controla cada parámetro

Aumentar `nprobe` para el mismo índice IVFFlat, abriendo listas adicionales sin recortar candidatos por otro límite, no elimina candidatos ya examinados; por eso el recall contra el exacto no debería empeorar por esa sola ampliación. La latencia medida puede variar por caché y ruido aunque el trabajo crezca.

Cambiar `nlist` modifica la partición y normalmente requiere reentrenar y reconstruir. Más listas reducen tamaño medio, pero aumentan trabajo de selección de centroides y pueden dejar vecinos relevantes en listas no abiertas. No existe una regla de «más nlist es siempre mejor».

## 5. Cuándo abrir todas las listas equivale al exacto

Con `nprobe=nlist`, todas las listas se examinan. En **IVFFlat**, con distancias completas, mismo conjunto elegible y sin otros cortes, se recupera el top-k exhaustivo, salvo diferencias numéricas o empates. Pero no necesariamente es más rápido: se paga organización adicional y comparación de centroides.

En **IVF-PQ** se comprimen subpartes del vector mediante cuantización de producto. Abrir todas las listas elimina el error de omitir celdas, pero puede persistir error por puntajes calculados sobre representaciones comprimidas. La afirmación del PDF «nprobe=nlist es exacto» requiere distinguir esa variante.

> [!question]- ¿nprobe es cuántos vecinos devuelve IVF?
> No. Es cuántas listas abre. Puede examinar miles de candidatos para devolver k=10.

Fuente: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-07.pdf#page=8|PDF 8–10 y 14]]. Complemento técnico: [Faiss, métodos por celdas y variantes IVF](https://github.com/facebookresearch/faiss/wiki/Faiss-indexes), consultado el 29 de septiembre de 2026. No se ejecutó el notebook `s2-mar` citado por las diapositivas.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/80 S07 - Búsqueda exacta aproximación y costo|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/07B Bases de datos vectoriales/82 S07 - HNSW capas conexiones y exploración|Siguiente]] →
