---
tags:
  - machine-learning
  - poo
  - python
  - autodiff
---

# `Scalar`: valor, identidad e historia computacional

Anterior: [[04 Buenas prácticas y assert]] · Siguiente: [[06 Grafo computacional y neurona]]

## 1. El problema: un `float` pierde la historia

Una neurona lineal puede calcular $z = wx + b$.

```python
x = 0.8
w = 1.25
b = -0.30

z = (w * x) + b
print(f"z = {z:.2f}")  # 0.70
print(type(z))         # <class 'float'>
```

El valor `0.70` sirve para inferencia, pero ya no recuerda que provino de `w`, `x`, `b`, una multiplicación y una suma. Para calcular derivadas automáticamente necesitamos conservar valor, relaciones y operaciones. `Scalar` representa precisamente esa combinación.

## 2. Fase 1: identidad y valor

```python
class ScalarV1:
    def __init__(self, data, label=""):
        self.data = float(data)
        self.label = str(label)

a = ScalarV1(0.8, "a")
b = ScalarV1(0.8, "b")

print(a.data == b.data)  # True: mismo valor
print(a is b)            # False: objetos distintos
```

Dos nodos pueden tener el mismo valor y representar variables diferentes dentro del grafo.

## 3. Fase 2: comportamiento

```python
class ScalarV2:
    def __init__(self, data, label=""):
        self.data = float(data)
        self.label = str(label)

    def describe(self):
        return f"{self.label}={self.data}"

x = ScalarV2(0.8, "x")
print(x.describe())
```

## 4. Fase 3: invariantes

Una invariante garantiza que los atributos mantengan tipos y estructuras conocidas:

```python
class ScalarV3:
    def __init__(self, data, parents=(), op="", label=""):
        self.data = float(data)
        self.parents = tuple(parents)
        self.op = str(op)
        self.label = str(label)
```

Aquí `data` siempre es `float`, `parents` siempre es `tuple` y `op` y `label` siempre son texto.

## 5. Fase 4: composición de nodos

El resultado de una operación no hereda de sus factores: contiene referencias a ellos.

```python
x = ScalarV3(0.8, label="x")
w = ScalarV3(1.25, label="w")

product = ScalarV3(
    data=w.data * x.data,
    parents=(w, x),
    op="*",
    label="product"
)

print(product.data)     # 1.0
print(product.parents)  # (w, x)
print(product.op)       # *
```

Este es un caso de composición: el nodo resultante tiene operandos y una operación, en lugar de ser una subclase distinta para cada operación.

## 6. Fase 5: herencia y `super()`

```python
class LabeledScalar(ScalarV3):
    def __init__(self, data, label):
        super().__init__(data, label=label)

    def describe(self):
        return f"{self.label}={self.data}"

act = LabeledScalar(1.5, "activation")
print(act.describe())
```

`LabeledScalar` reutiliza la inicialización de `ScalarV3` y añade un comportamiento especializado.

## 7. La clase `Scalar` completa

La sobrecarga de operadores sigue el patrón: convertir los operandos, calcular el valor y conectar los padres guardando la operación.

```python
class Scalar:
    """Nodo escalar para un grafo computacional."""

    def __init__(self, data, parents=(), op="", label=""):
        self.data = float(data)
        self.parents = tuple(parents)
        self.op = str(op)
        self.label = str(label)

    def __repr__(self):
        label = f", label={self.label!r}" if self.label else ""
        return f"Scalar(data={self.data}{label}, op={self.op!r})"

    @staticmethod
    def _coerce(other):
        if isinstance(other, Scalar):
            return other
        try:
            return Scalar(other)
        except (TypeError, ValueError):
            return NotImplemented

    def __add__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return Scalar(self.data + other.data, parents=(self, other), op="+")

    def __mul__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return Scalar(self.data * other.data, parents=(self, other), op="*")

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other
```

## 8. Qué conserva cada nodo

| Atributo | Función |
| :--- | :--- |
| `data` | Valor numérico del nodo. |
| `parents` | Referencias a los nodos que participaron en el cálculo. |
| `op` | Operación que produjo el nodo, como `+` o `*`. |
| `label` | Nombre útil para leer e inspeccionar el grafo. |

## Repaso

- ¿Qué información pierde un `float`?
- ¿Por qué `parents` representa composición?
- ¿Qué tres pasos sigue la sobrecarga de operadores?
