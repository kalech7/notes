---
tags:
  - numpy
  - algebra-lineal
  - verificacion
related: "[[00 Índice - Espacios vectoriales y embeddings]]"
---

# Comprobación con NumPy

Anterior: [[04 Embeddings y representación de objetos]] · Siguiente: [[06 Resumen, errores frecuentes y preguntas de repaso]]

## 1. El código comprueba; la definición justifica

NumPy permite verificar ejemplos concretos, pero no reemplaza una definición ni una demostración. El orden correcto es:

1. formular la afirmación matemática;
2. predecir el resultado;
3. calcularlo con NumPy;
4. interpretar si el resultado coincide y con qué tolerancia.

![[assets/25-numpy.jpg|850]]

## 2. Combinación lineal

Para $u=(1,1)$ y $v=(2,0)$ esperamos $2u+v=(4,2)$:

```python
import numpy as np

u = np.array([1.0, 1.0])
v = np.array([2.0, 0.0])
w = 2 * u + v

assert np.allclose(w, np.array([4.0, 2.0]))
```

`np.allclose` compara con tolerancia. Es preferible a `w == esperado` para cálculos de punto flotante, porque muchos números reales no tienen representación binaria exacta.

## 3. Coordenadas en otra base

Sea la base $B=(b_1,b_2)$, con

$$
b_1=(1,1),\qquad b_2=(1,-1),
$$

y sea $x=(3,2)$. Construimos una matriz colocando los vectores de la base como **columnas**:

```python
b1 = np.array([1.0, 1.0])
b2 = np.array([1.0, -1.0])
B = np.column_stack([b1, b2])
x = np.array([3.0, 2.0])

c = np.linalg.solve(B, x)
assert np.allclose(c, np.array([2.5, 0.5]))
assert np.allclose(B @ c, x)
```

La ecuación $Bc=x$ significa

$$
c_1b_1+c_2b_2=x.
$$

Por eso `c` contiene $[x]_B$. `np.linalg.solve` requiere una matriz cuadrada invertible; aquí eso equivale a que $b_1$ y $b_2$ formen una base de $\mathbb{R}^2$.

> [!warning] Filas vs. columnas
> Si apilas los vectores como filas, el producto ya no representa la misma combinación. En esta convención, cada vector de la base es una columna.

## 4. Rango e independencia

Considera

$$
a_1=(1,0),\quad a_2=(0,1),\quad a_3=(1,1).
$$

Como $a_3=a_1+a_2$, hay tres columnas pero solo dos direcciones independientes:

```python
a1 = np.array([1.0, 0.0])
a2 = np.array([0.0, 1.0])
a3 = np.array([1.0, 1.0])
A = np.column_stack([a1, a2, a3])

rank = np.linalg.matrix_rank(A)
assert rank == 2
assert np.allclose(a3, a1 + a2)
```

Interpretación: `rank == 2` es el número de direcciones independientes, no el número total de columnas.

## 5. Dependencia exacta y casi dependencia

### Dependencia exacta

Si $a_3=a_1+a_2$ por construcción algebraica, la dependencia es exacta. La igualdad proporciona una prueba clara.

### Casi dependencia

En datos reales, una columna podría ser casi combinación de otras debido a ruido o redondeo:

```python
eps = 1e-12
A_casi = np.column_stack([
    np.array([1.0, 0.0]),
    np.array([0.0, 1.0]),
    np.array([1.0, 1.0 + eps]),
])

np.linalg.matrix_rank(A_casi)
```

El rango numérico puede depender de la escala y la tolerancia. Internamente se examinan valores singulares y se trata como cero aquello que cae por debajo de un umbral. Por eso el resultado computacional debe interpretarse, especialmente si el problema está mal condicionado.

Puedes inspeccionar los valores singulares:

```python
s = np.linalg.svd(A_casi, compute_uv=False)
print(s)
```

Un valor singular muy pequeño respecto de los otros sugiere una dirección casi redundante.

## 6. Comprobar pertenencia a un `span`

Para preguntar si $x$ pertenece al `span` de las columnas de una matriz no cuadrada, podemos resolver por mínimos cuadrados:

```python
A = np.column_stack([
    np.array([1.0, 2.0, 0.0]),
    np.array([0.0, 1.0, 1.0]),
])
x = np.array([2.0, 5.0, 1.0])

c, *_ = np.linalg.lstsq(A, x, rcond=None)
residuo = np.linalg.norm(A @ c - x)

print(c, residuo)
```

Si el residuo es cero en aritmética exacta, $x$ pertenece al `span`. Numéricamente comprobamos si es suficientemente pequeño para la escala y precisión del problema.

## 7. Lista de comprobación antes de aceptar el resultado

- ¿Qué afirmación matemática estoy evaluando?
- ¿Coloqué los vectores como columnas?
- ¿El resultado esperado es exacto o numérico?
- ¿Qué significa el rango en este contexto?
- ¿La escala de los datos hace razonable la tolerancia?
- ¿Estoy comprobando un ejemplo o demostrando una propiedad general?

## Ejercicios

1. Verifica que $(5,1)=3(1,1)+(2,-2)$.
2. Halla con `solve` las coordenadas de $(4,1)$ en la base $((1,1),(1,-1))$.
3. Construye una matriz con cuatro columnas en $\mathbb{R}^3$ y explica por qué no pueden ser todas independientes.
4. Modifica `eps` y observa cuándo cambia el rango numérico.

