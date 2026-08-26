---
tags:
  - machine-learning
  - espacio-latente
  - pca
  - embeddings
related: "[[00 Índice - Espectro, SVD y rango bajo]]"
---

# Espacio latente, PCA e interpretación

Anterior: [[04 Aproximación de rango bajo y elección de k]] · Siguiente: [[06 Resumen y preguntas de repaso]]

## 1. Qué representa cada factor en una matriz de datos

Supón que las filas de $X$ son documentos y las columnas son rasgos:

- las columnas de $V$ o filas de $V^T$ son direcciones en el espacio de características;
- $\Sigma$ indica la escala algebraica de cada dirección;
- $U\Sigma=XV$ contiene las coordenadas latentes de las observaciones.

![[assets/24-factores-datos.jpg|850]]

Para conservar $k$ dimensiones:

$$
Z_k=U_k\Sigma_k=XV_k.
$$

$Z_k$ tiene una fila por observación y una columna por dirección latente conservada.

## 2. Lectura defendible del caso

En la matriz del módulo, las dos primeras columnas suelen activarse juntas en algunos documentos y las dos últimas en otros. La SVD detecta dos patrones dominantes. Es legítimo decir que una dirección pondera principalmente el primer bloque y otra el segundo.

No es legítimo nombrarlas como conceptos semánticos concretos sin saber qué representan las columnas y sin validación externa.

## 3. Ambigüedad de signo

Una implementación puede devolver $v_i$ o $-v_i$. Si simultáneamente cambia $u_i$ por $-u_i$, la matriz no cambia:

$$
\sigma_i(-u_i)(-v_i)^T=\sigma_i u_i v_i^T.
$$

Por eso la interpretación de una dirección debe ser invariante a su signo global. Comparar vectores mediante el valor absoluto de su coseno evita declarar erróneamente que dos implementaciones discrepan.

## 4. SVD de embeddings

Si cada fila es un embedding, la SVD puede:

- encontrar direcciones de variación lineal;
- reducir dimensión;
- eliminar direcciones de escala pequeña;
- producir coordenadas latentes compactas.

Pero no certifica que una dirección sea «sentimiento», «calidad» o cualquier concepto humano. La SVD organiza geometría lineal; la semántica necesita etiquetas, experimentos, análisis de estabilidad o validación en una tarea.

## 5. PCA mediante SVD

PCA comienza centrando cada columna:

$$
X_c=X-\bar X,
$$

donde $\bar X$ contiene las medias de las variables. Si

$$
X_c=U\Sigma V^T,
$$

entonces las columnas de $V$ son direcciones principales y

$$
\lambda_i(\operatorname{Cov}(X))
=\frac{\sigma_i^2}{m-1}
$$

para covarianza muestral con $m$ observaciones.

![[assets/28-pca-centrado.jpg|850]]

Las puntuaciones principales son $X_cV=U\Sigma$.

## 6. PCA frente a TruncatedSVD

| PCA | TruncatedSVD |
| --- | --- |
| Centra las columnas antes de descomponer. | Normalmente opera sobre $X$ sin centrar. |
| Sus direcciones describen varianza respecto de la media. | Sus direcciones describen estructura algebraica respecto del origen. |
| Adecuado para lectura estadística de componentes principales. | Útil en matrices dispersas donde centrar destruiría la dispersidad. |

La álgebra es similar, pero la interpretación cambia. SVD sin centrar no se convierte automáticamente en PCA.

## 7. Secuencia responsable de interpretación

```mermaid
flowchart LR
    A[Predecir estructura] --> B[Descomponer]
    B --> C[Truncar]
    C --> D[Medir error]
    D --> E[Inspeccionar patrones]
    E --> F[Validar significado externamente]
```

## Preguntas rápidas

1. ¿Qué describen $V$, $\Sigma$ y $U\Sigma$ en una matriz de datos?
2. ¿Por qué el signo de una dirección singular es arbitrario?
3. ¿Qué debe hacerse antes de interpretar SVD como PCA?
4. ¿Por qué una dirección latente dominante no equivale a un concepto demostrado?
5. ¿Qué validación adicional pedirías antes de usar $k=2$ en un modelo?

