---
tags:
  - python
  - numpy
  - autovalores
related: "[[02 Autovalores, autovectores y espectro]]"
---

# Python: preparación, funciones auxiliares y espectro

Anterior: [[00 Índice - Demo computacional M05]] · Siguiente: [[02 Python - SVD, dimensiones y geometría]]

## Celda 2: importar, configurar y preparar datos

```python
import numpy as np

np.set_printoptions(precision=4, suppress=True)
```

- `import numpy as np` importa NumPy y le asigna el alias convencional `np`.
- `precision=4` muestra cuatro decimales; no reduce la precisión almacenada.
- `suppress=True` evita notación científica para números pequeños al imprimirlos.

### Error relativo de Frobenius

```python
def relative_frobenius_error(original, approximation):
    return np.linalg.norm(original - approximation, "fro") / np.linalg.norm(original, "fro")
```

1. `original - approximation` construye el residuo.
2. `np.linalg.norm(..., "fro")` calcula su norma de Frobenius.
3. Se divide por la norma del original para obtener un error relativo sin unidades.

Si devuelve `0.02`, la pérdida global equivale aproximadamente al 2 % de la magnitud Frobenius de la matriz original. La función presupone que `original` no es la matriz cero; de lo contrario dividiría por cero.

### Reconstrucción truncada

```python
def reconstruct(U, s, Vt, k):
    return U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]
```

- `U[:, :k]`: todas las filas y las primeras `k` columnas, es $U_k$.
- `s[:k]`: primeros `k` valores singulares.
- `np.diag(...)`: convierte el vector en $\Sigma_k$ diagonal.
- `Vt[:k, :]`: primeras `k` filas de $V^T$.
- `@`: multiplicación matricial.

La salida es $U_k\Sigma_kV_k^T$ y tiene la misma forma que la matriz original.

### Alineación invariante al signo

```python
def sign_invariant_alignment(a, b):
    """Cosine alignment ignoring the unavoidable global sign ambiguity."""
    return abs(float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))))
```

Calcula el valor absoluto de la similitud coseno. Si `a=b` o `a=-b`, devuelve aproximadamente `1`. `abs` es necesario porque los vectores singulares y autovectores pueden cambiar globalmente de signo. `float(...)` convierte el escalar de NumPy en un `float` de Python.

### Matriz del caso

```python
X = np.array([
    [4., 5., 0., 0.],
    [3., 4., 0., 0.],
    [0., 1., 5., 4.],
    [0., 1., 4., 3.],
    [5., 6., 0., 0.],
])
print("X shape:", X.shape)
```

Los puntos como `4.` fuerzan tipo flotante. `X.shape` devuelve `(5, 4)`: cinco observaciones y cuatro características.

## Celda 4: `eigh` para una matriz simétrica

```python
A = np.array([[2., 1.], [1., 2.]])
eigenvalues, Q = np.linalg.eigh(A)
residuals = [
    np.linalg.norm(A @ Q[:, i] - eigenvalues[i] * Q[:, i])
    for i in range(2)
]
```

`np.linalg.eigh` está especializado en matrices simétricas o hermíticas. Devuelve:

- `eigenvalues`: autovalores en orden ascendente, aquí `[1., 3.]`;
- `Q`: autovectores ortonormales colocados como columnas.

La comprensión de lista recorre `i=0,1`. Para cada par calcula el residual

$$
\lVert Aq_i-\lambda_iq_i\rVert_2.
$$

Los dos residuos fueron exactamente `0.0` en esta ejecución.

```python
assert np.allclose(Q.T @ Q, np.eye(2))
assert max(residuals) < 1e-12
```

- `Q.T` es la transpuesta.
- `np.eye(2)` crea la identidad $2\times2$.
- `np.allclose` compara con tolerancia.
- `assert` detiene la ejecución si la condición es falsa; sirve como comprobación automática.

## Celda 6: `eig` frente a `eigh`

```python
w_general, V_general = np.linalg.eig(A)
print("eig:", np.sort(w_general))
print("eigh:", eigenvalues)
assert np.allclose(np.sort(w_general), eigenvalues)
```

`eig` es la rutina general para matrices cuadradas. Puede devolver autovalores complejos y no explota la simetría. `np.sort` ordena su salida para compararla con `eigh`. Que coincidan aquí se debe a que `A` es simétrica; no vuelve intercambiables ambas funciones en todos los problemas.

## Celda 8: construir los dos Gram

```python
gram_right = X.T @ X
gram_left = X @ X.T
lambda_right = np.linalg.eigvalsh(gram_right)
lambda_left = np.linalg.eigvalsh(gram_left)
```

- `gram_right` tiene forma `(4, 4)` y actúa sobre características.
- `gram_left` tiene forma `(5, 5)` y actúa sobre observaciones.
- `eigvalsh` devuelve solo autovalores de una matriz simétrica, sin calcular autovectores.

La salida fue:

```text
X^T X: [0.0114, 0.0621, 65.4881, 129.4384]
X X^T: [0, 0.0114, 0.0621, 65.4881, 129.4384]
```

El cero adicional en $XX^T$ aparece porque es $5\times5$ pero el rango no puede superar 4. Las aserciones permiten una pequeña negatividad de `-1e-10` por redondeo, aunque matemáticamente ambas matrices son semidefinidas positivas.

## Para recordar

- `eig`: matriz cuadrada general.
- `eigh`: matriz simétrica, autovalores y autovectores.
- `eigvalsh`: matriz simétrica, solo autovalores.
- `allclose`: igualdad numérica aproximada.
- `assert`: documenta y verifica una expectativa.

