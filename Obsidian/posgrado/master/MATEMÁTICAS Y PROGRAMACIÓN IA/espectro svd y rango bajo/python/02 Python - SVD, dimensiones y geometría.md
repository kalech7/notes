---
tags:
  - python
  - numpy
  - svd
related: "[[03 Descomposición en valores singulares - SVD]]"
---

# Python: SVD, dimensiones y geometría

Anterior: [[01 Python - preparación, funciones auxiliares y espectro]] · Siguiente: [[03 Python - truncamiento, error y espacio latente]]

## Celda 10: calcular la SVD reducida

```python
U, s, Vt = np.linalg.svd(X, full_matrices=False)
```

NumPy devuelve los valores singulares como vector `s`, no como matriz diagonal. Para `X.shape == (5, 4)`, $q=\min(5,4)=4$:

```text
U.shape  = (5, 4)
s.shape  = (4,)
Vt.shape = (4, 4)
s = [11.3771, 8.0925, 0.2492, 0.1068]
```

`full_matrices=False` solicita la forma reducida. Si fuera `True`, `U` tendría forma `(5, 5)` y la matriz rectangular completa de $\Sigma$ requeriría más cuidado al reconstruir.

```python
assert U.shape == (5, 4) and s.shape == (4,) and Vt.shape == (4, 4)
assert np.allclose(U @ np.diag(s) @ Vt, X)
```

La primera aserción audita dimensiones. La segunda convierte `s` en diagonal y verifica $U\Sigma V^T=X$.

> [!warning] `Vt` no es `V`
> NumPy devuelve directamente $V^T$. Sus **filas** son las direcciones singulares derechas. Para obtener $V$, usa `Vt.T`.

## Celda 12: seguir un vector a través de los factores

```python
x = np.array([1., -1., 2., 0.5])
coordinates = Vt @ x
scaled = s * coordinates
reconstructed_output = U @ scaled
```

Las formas son:

```text
x:                    (4,)
coordinates = Vt @ x: (4,)
scaled:                (4,)
U @ scaled:            (5,)
```

`s * coordinates` es multiplicación elemento a elemento. Equivale a `np.diag(s) @ coordinates`, pero evita construir la matriz diagonal.

La salida observada fue:

```text
coordenadas V^T x: [-0.0930, -1.7256, -1.3131, -1.2408]
U Sigma V^T x:     [-1.0, -1.0, 11.0, 8.5, -1.0]
```

```python
assert np.allclose(reconstructed_output, X @ x)
```

Esto comprueba que aplicar los tres pasos de la SVD produce exactamente la misma transformación lineal que multiplicar por `X`.

## Celda 14: cuadrados singulares y contraejemplo

```python
positive_lambda = np.linalg.eigvalsh(X.T @ X)[::-1]
```

`eigvalsh` devuelve orden ascendente; `[::-1]` invierte el vector para alinearlo con `s`, que viene descendente.

```python
B = np.array([[0., 1.], [0., 0.]])
print("sigma(X)^2:", s**2)
print("lambda(X^T X):", positive_lambda)
```

`s**2` eleva cada elemento al cuadrado. Ambos resultados fueron:

```text
[129.4384, 65.4881, 0.0621, 0.0114]
```

Así se comprueba $\sigma_i^2=\lambda_i(X^TX)$.

```python
np.linalg.eigvals(B)
np.linalg.svd(B, compute_uv=False)
```

`compute_uv=False` pide solo valores singulares y ahorra calcular los vectores. Para `B`, los autovalores son `[0, 0]` y los valores singulares `[1, 0]`.

```python
assert np.allclose(s**2, positive_lambda)
assert not np.allclose(
    np.sort(np.abs(np.linalg.eigvals(B))),
    np.sort(np.linalg.svd(B, compute_uv=False)),
)
```

`not` exige que la igualdad aproximada sea falsa. `abs` y `sort` eliminan excusas de signo u orden: incluso así, ambos conceptos difieren.

## Mapa de las funciones usadas

| Expresión | Resultado |
| --- | --- |
| `np.linalg.svd(X, full_matrices=False)` | $U$, vector `s`, $V^T$ reducidos |
| `np.diag(s)` | matriz diagonal $\Sigma$ |
| `s * coordinates` | escalado componente a componente |
| `array[::-1]` | orden inverso |
| `compute_uv=False` | solo valores singulares |

