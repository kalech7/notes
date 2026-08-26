---
tags:
  - python
  - numpy
  - rango-bajo
  - espacio-latente
related: "[[04 Aproximación de rango bajo y elección de k]]"
---

# Python: truncamiento, error y espacio latente

Anterior: [[02 Python - SVD, dimensiones y geometría]] · Siguiente: [[04 Python - PCA, auditoría y rango numérico]]

## Celda 16: construir todas las aproximaciones

```python
approximations = {k: reconstruct(U, s, Vt, k) for k in range(1, 5)}
```

Es una comprensión de diccionario. `range(1, 5)` produce `1, 2, 3, 4`. Cada clave `k` apunta a $X_k$.

```python
for k, Xk in approximations.items():
    print(
        f"k={k}: rango={np.linalg.matrix_rank(Xk)}, "
        f"error_rel_F={relative_frobenius_error(X, Xk):.5f}"
    )
    assert np.linalg.matrix_rank(Xk, tol=1e-10) <= k
```

- `.items()` entrega pares clave-valor.
- `f"...{variable}..."` es una *f-string*.
- `:.5f` muestra cinco decimales.
- `matrix_rank(..., tol=1e-10)` cuenta valores singulares mayores que la tolerancia.

Resultados:

| $k$ | rango observado | error relativo F |
| ---: | ---: | ---: |
| 1 | 1 | 0.57984 |
| 2 | 2 | 0.01941 |
| 3 | 3 | 0.00765 |
| 4 | 4 | 0.00000 |

La caída enorme entre $k=1$ y $k=2$ confirma que hay dos patrones dominantes.

## Celda 18: tres criterios de error

```python
rows = []
for k, Xk in approximations.items():
    rel_f = relative_frobenius_error(X, Xk)
    retained = np.sum(s[:k] ** 2) / np.sum(s ** 2)
    spectral = np.linalg.norm(X - Xk, 2)
    rows.append((k, rel_f, retained, spectral))
```

- `rows = []` crea una lista vacía.
- `np.sum(s[:k] ** 2)` suma cuadrados conservados.
- `np.linalg.norm(..., 2)` calcula la norma espectral matricial.
- `.append((...))` agrega una tupla con los resultados.

Para $k=2$ se obtuvo:

```text
error_rel_F       = 0.01941
energia_algebraica= 0.99962
error_2           = 0.24915
```

```python
assert np.isclose(rows[1][1], 0.01941, atol=5e-5)
assert np.isclose(rows[1][2], 0.99962, atol=5e-5)
```

`rows[1]` es la segunda fila, correspondiente a `k=2`; el segundo índice selecciona la columna. `atol=5e-5` fija la tolerancia absoluta. Estas aserciones convierten cifras de la explicación en pruebas reproducibles.

## Celda 20: coordenadas latentes

```python
scores = U[:, :2] * s[:2]
```

Aquí NumPy aplica *broadcasting*: `U[:, :2]` tiene forma `(5, 2)` y `s[:2]` forma `(2,)`. Cada columna de $U_2$ se multiplica por su valor singular. El resultado es

$$
\texttt{scores}=U_2\Sigma_2=XV_2.
$$

Cada fila ubica una observación en dos coordenadas latentes:

```text
[[-6.3394,  0.9010],
 [-4.9497,  0.6865],
 [-1.6785, -6.2588],
 [-1.4817, -4.8773],
 [-7.7291,  1.1155]]
```

Los signos podrían invertirse en otra implementación sin cambiar la estructura.

```python
np.abs(Vt[:2, :2]).sum(axis=1)
np.abs(Vt[:2, 2:]).sum(axis=1)
```

Paso a paso:

- `Vt[:2, :2]`: dos direcciones latentes y las dos primeras características;
- `Vt[:2, 2:]`: las mismas direcciones y las dos últimas características;
- `np.abs`: ignora el signo para medir peso total;
- `.sum(axis=1)`: suma horizontalmente dentro de cada dirección.

El primer componente tiene mucho peso en el primer bloque (`1.3897` frente a `0.1968`), y el segundo en el bloque final (`1.3815` frente a `0.2145`). Esto demuestra una separación algebraica de bloques, no una semántica humana.

```python
assert np.allclose((-U[:, 0]) * s[0], -scores[:, 0])
```

La celda hace explícita la ambigüedad de signo: invertir $u_1$ invierte sus puntuaciones, pero una inversión simultánea en $v_1$ preservaría la reconstrucción.

## Para recordar

- Una comprensión construye todas las aproximaciones sin repetir código.
- El *broadcasting* permite formar $U_k\Sigma_k$ sin `diag`.
- `axis=1` agrega por filas; `axis=0`, por columnas.
- Una cifra latente necesita interpretación y validación, no solo impresión.

