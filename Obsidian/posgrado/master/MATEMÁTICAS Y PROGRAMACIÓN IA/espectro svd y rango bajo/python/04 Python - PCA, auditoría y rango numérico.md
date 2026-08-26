---
tags:
  - python
  - numpy
  - pca
  - rango-numerico
related: "[[05 Espacio latente, PCA e interpretación]]"
---

# Python: PCA, auditoría y rango numérico

Anterior: [[03 Python - truncamiento, error y espacio latente]] · Volver al [[00 Índice - Demo computacional M05|índice de Python]]

## Celda 22: centrar y conectar SVD con PCA

```python
X_centered = X - X.mean(axis=0, keepdims=True)
```

- `axis=0` calcula una media por columna.
- `keepdims=True` conserva forma `(1, 4)` en vez de `(4,)`.
- El *broadcasting* resta esa fila de medias a cada observación.

El centrado garantiza que cada columna de `X_centered` tenga media aproximadamente cero.

```python
Uc, sc, Vtc = np.linalg.svd(X_centered, full_matrices=False)
covariance = X_centered.T @ X_centered / (X.shape[0] - 1)
```

`X.shape[0]` es el número de observaciones, 5; se divide por `m-1=4` para obtener covarianza muestral.

```python
pca_values, pca_vectors = np.linalg.eigh(covariance)
order = np.argsort(pca_values)[::-1]
```

- `eigh` devuelve los autovalores en orden ascendente.
- `argsort` devuelve los índices que los ordenarían.
- `[::-1]` cambia esos índices a orden descendente.

Los dos cálculos coincidieron:

```text
varianza desde SVD:       [19.9775, 0.6195, 0.0030, 0.0000]
autovalores covarianza:   [19.9775, 0.6195, 0.0030, 0.0000]
```

```python
assert np.allclose(sc**2 / (X.shape[0] - 1), pca_values[order])
```

Comprueba $\lambda_i(\operatorname{Cov}(X))=\sigma_i^2/(m-1)$.

```python
assert all(
    sign_invariant_alignment(Vtc[i], pca_vectors[:, order[i]]) > 1 - 1e-10
    for i in range(4)
)
```

Es una expresión generadora dentro de `all`: exige que las cuatro parejas de direcciones estén alineadas, permitiendo signo opuesto.

## Celda 24: auditoría completa

```python
reconstruction_residual = np.linalg.norm(
    X - U @ np.diag(s) @ Vt, "fro"
)
orthogonality_u = np.linalg.norm(U.T @ U - np.eye(4), "fro")
orthogonality_v = np.linalg.norm(Vt @ Vt.T - np.eye(4), "fro")
```

Se miden tres desviaciones:

1. reconstrucción $X-U\Sigma V^T$;
2. ortonormalidad de columnas de $U$;
3. ortonormalidad de filas de $V^T$.

Los resultados fueron del orden de $10^{-15}$, compatibles con redondeo de punto flotante:

```text
residuo reconstrucción: 4.61e-15
residuo U:              9.66e-16
residuo V:              2.86e-16
```

```python
assert np.all(np.diff(s) <= 0)
```

`np.diff(s)` calcula `s[i+1] - s[i]`. Si todas las diferencias son menores o iguales a cero, los valores están en orden no creciente.

## Celda 26: rango algebraico y efectivo

```python
default_rank = np.linalg.matrix_rank(X)
relative_tolerance = 0.03 * s[0]
effective_rank = int(np.sum(s > relative_tolerance))
```

- `matrix_rank` usa una tolerancia automática basada en valores singulares, dimensiones y precisión de máquina.
- Se declara otra tolerancia: 3 % del mayor valor singular.
- `s > relative_tolerance` produce booleanos.
- `np.sum` cuenta `True` como 1.
- `int` convierte el escalar de NumPy a entero de Python.

Salida:

```text
rango con tolerancia por defecto: 4
tolerancia relativa elegida:      0.341313...
rango efectivo declarado:         2
```

No hay contradicción. «Rango 4» usa la tolerancia por defecto; «rango efectivo 2» usa el criterio explícito de 3 %.

## Qué significan las rutinas del módulo

| Rutina | Pregunta |
| --- | --- |
| `np.linalg.eig(A)` | ¿Cuál es el espectro de una matriz cuadrada general? |
| `np.linalg.eigh(A)` | ¿Cuál es el espectro y base ortonormal de una matriz simétrica? |
| `np.linalg.svd(X)` | ¿Cuáles son ejes y escalas singulares de una matriz cualquiera? |
| `np.linalg.matrix_rank(X)` | ¿Cuál es el rango numérico bajo una tolerancia? |
| `np.linalg.norm(R, "fro")` | ¿Cuál es la magnitud acumulada del residuo? |
| `np.linalg.norm(R, 2)` | ¿Cuál es la peor escala residual? |

## Patrón auditable para futuros experimentos

```python
# 1. Declarar forma y afirmación
print("shape:", X.shape)

# 2. Calcular con la rutina apropiada
U, s, Vt = np.linalg.svd(X, full_matrices=False)

# 3. Medir el residual con norma declarada
residual = np.linalg.norm(X - U @ np.diag(s) @ Vt, "fro")

# 4. Comparar con tolerancia explícita
assert residual < 1e-12

# 5. Interpretar el resultado, no solo imprimirlo
```

> [!important] Cierre
> Las celdas comprueban que la SVD reconstruye, que $k=2$ comprime bien esta matriz bajo Frobenius y que PCA coincide con la SVD centrada. No prueban que $k=2$ sea óptimo para toda tarea ni que las direcciones tengan una semántica concreta.

