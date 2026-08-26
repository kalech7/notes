---
epoch: 1787718627338
mode: agent
backendId: codex
sessionId: "01a03c55-3648-7062-9aef-cbbbc9f836ac"
agentLabel: "que es column_stack([b1, b2]) ? y explica mejor que eall clo…"
usage: '{"usedTokens":30660,"contextWindow":258400,"updatedAt":1787756215199}'
tags:
  - copilot-conversation
---

**user**: que es column_stack([b1, b2]) ? y explica mejor que eall cloase para que sirve
[Timestamp: 2026/08/25 23:30:27]

**ai**: Voy a leer el fragmento de [[05 Comprobación con NumPy]] donde aparece `column_stack([b1, b2])` para explicarlo usando exactamente las variables y clases del ejemplo.En [[05 Comprobación con NumPy]] aparecen dos funciones distintas:

### `np.column_stack([b1, b2])`

Une varios vectores colocándolos como **columnas** de una matriz.

```python
b1 = np.array([1.0, 1.0])
b2 = np.array([1.0, -1.0])

B = np.column_stack([b1, b2])
print(B)
```

Resultado:

```text
[[ 1.  1.]
 [ 1. -1.]]
```

Esto representa:

$$
B=
\begin{pmatrix}
\vert & \vert\\
b_1 & b_2\\
\vert & \vert
\end{pmatrix}
=
\begin{pmatrix}
1 & 1\\
1 & -1
\end{pmatrix}.
$$

Se usa así porque, al multiplicar la matriz por un vector de coeficientes,

```python
c = np.array([2.5, 0.5])
B @ c
```

NumPy calcula:

$$
Bc=2.5b_1+0.5b_2.
$$

En este caso:

$$
2.5(1,1)+0.5(1,-1)=(3,2).
$$

Por eso `column_stack` resulta útil para:

- construir una matriz a partir de vectores;
- colocar los vectores de una base como columnas;
- representar combinaciones lineales mediante `B @ c`;
- estudiar independencia lineal, rango y `span`.

---

### `np.allclose(a, b)`

Comprueba si todos los elementos de `a` y `b` son **aproximadamente iguales**.

```python
np.allclose(
    np.array([3.0, 2.0]),
    np.array([3.0, 2.0])
)
```

Devuelve:

```python
True
```

También puede devolver `True` cuando existe una diferencia diminuta:

```python
a = np.array([0.1 + 0.2])
b = np.array([0.3])

print(a == b)             # [False]
print(np.allclose(a, b))  # True
```

Esto sucede porque muchos números decimales no pueden almacenarse exactamente en formato binario. Internamente, `0.1 + 0.2` puede quedar como algo parecido a:

```text
0.30000000000000004
```

Matemáticamente esperamos `0.3`, pero la computadora guarda una pequeña diferencia de redondeo.

`np.allclose` pregunta esencialmente:

> ¿Las diferencias entre estos valores son tan pequeñas que podemos considerarlos iguales para este cálculo?

Por eso en la nota se escribe:

```python
assert np.allclose(B @ c, x)
```

Su significado es:

1. `B @ c` reconstruye el vector usando la base.
2. `np.allclose(B @ c, x)` comprueba que el resultado sea aproximadamente `x`.
3. `assert` genera un error si la comprobación resulta falsa.

Ejemplo:

```python
resultado = B @ c
esperado = x

assert np.allclose(resultado, esperado)
```

En resumen:

- `column_stack` **construye la matriz** colocando vectores como columnas.
- `B @ c` **calcula la combinación lineal**.
- `allclose` **comprueba el resultado tolerando pequeños errores decimales**.
- `assert` **detiene el programa si la comprobación falla**.
[Timestamp: 2026/08/25 23:30:27]

**user**: y eso linalg.solve
[Timestamp: 2026/08/25 23:32:57]

**ai**: ### `np.linalg.solve(B, x)`

Sirve para resolver un sistema de ecuaciones lineales de la forma:

$$
Bc=x.
$$

En el ejemplo de [[05 Comprobación con NumPy]]:

```python
B = np.array([
    [1.0,  1.0],
    [1.0, -1.0]
])

x = np.array([3.0, 2.0])

c = np.linalg.solve(B, x)
print(c)
```

Resultado:

```text
[2.5 0.5]
```

Esto significa que:

$$
c=
\begin{pmatrix}
2.5\\
0.5
\end{pmatrix}.
$$

Como las columnas de `B` son $b_1$ y $b_2$, la ecuación $Bc=x$ equivale a:

$$
2.5b_1+0.5b_2=x.
$$

Comprobación:

$$
2.5(1,1)+0.5(1,-1)
=(2.5,2.5)+(0.5,-0.5)
=(3,2).
$$

Por tanto:

```python
c = np.linalg.solve(B, x)
```

encuentra los coeficientes necesarios para formar `x` utilizando los vectores de la base `B`. Es decir, `c` contiene las coordenadas de $x$ en esa base:

$$
[x]_B=(2.5,0.5).
$$

También puede entenderse como resolver estas ecuaciones:

$$
\begin{cases}
c_1+c_2=3,\\
c_1-c_2=2.
\end{cases}
$$

La solución es:

$$
c_1=2.5,\qquad c_2=0.5.
$$

`np.linalg.solve` requiere que `B` sea:

- cuadrada: mismo número de filas y columnas;
- invertible: sus columnas deben ser linealmente independientes.

Si `B` no es invertible, NumPy genera un error porque el sistema no tiene una solución única. En una frase:

> `np.linalg.solve(B, x)` encuentra el vector `c` que hace verdadera la ecuación `B @ c = x`.
[Timestamp: 2026/08/25 23:32:57]

**user**: haz push de todo
[Timestamp: 2026/08/26 09:56:41]

**ai**: Voy a revisar el estado del repositorio y la rama actual para enviar todos los cambios pendientes al remoto.El repositorio está en modo de solo lectura para su carpeta `.git`, así que el commit no pudo crear `index.lock`. Solicitaré permiso para preparar el commit y hacer el push.
[Timestamp: 2026/08/26 09:56:41]