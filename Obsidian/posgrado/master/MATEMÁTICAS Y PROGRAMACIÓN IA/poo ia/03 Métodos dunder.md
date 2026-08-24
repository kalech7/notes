---
tags:
  - machine-learning
  - poo
  - python
---

# Métodos dunder y sobrecarga de operadores

Anterior: [[02 Herencia y composición]] · Siguiente: [[04 Buenas prácticas y assert]]

## 1. ¿Qué son?

Los métodos con doble guion bajo (`__nombre__`) se llaman **dunder**, abreviatura de *double underscore*. Son métodos especiales definidos dentro de una clase. Python los invoca al usar una operación del lenguaje.

No son atributos, palabras reservadas ni funciones independientes:

```python
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __add__(self, other):
        return Numero(self.valor + other.valor)
```

Un método normal se llama explícitamente, como `x.describe()`. Un dunder suele activarse automáticamente: `x + y` busca `x.__add__(y)`.

> [!warning] Dunder no significa `@classmethod`
> “Método especial” describe el protocolo que activa Python. `__add__` y `__repr__` suelen recibir `self`; `__new__` recibe `cls`. No todos son métodos decorados con `@classmethod`.

## 2. Tabla de operaciones

| Sintaxis | Método que Python busca |
| :--- | :--- |
| `Scalar(2.0)` | `__new__` crea y `__init__` inicializa |
| `repr(x)` | `x.__repr__()` |
| `print(x)` | `x.__str__()`; si no existe, usa `x.__repr__()` |
| `a + b` | `a.__add__(b)` |
| `a * b` | `a.__mul__(b)` |
| `2 + a` | `a.__radd__(2)` si la suma normal devuelve `NotImplemented` |
| `2 * a` | `a.__rmul__(2)` si la multiplicación normal devuelve `NotImplemented` |
| `len(x)` | `x.__len__()` |
| `x[i]` | `x.__getitem__(i)` |
| `x(...)` | `x.__call__(...)` |

## 3. `self` y `other` en `__add__`

La definición correcta es:

```python
def __add__(self, other):
    ...
```

La coma va dentro de los paréntesis. `other` no es una palabra reservada: es la convención para llamar al **otro operando**, normalmente el que está a la derecha de `+`.

```python
a = Numero(2)
b = Numero(3)
c = a + b
```

Python transforma conceptualmente la última línea en:

```python
c = Numero.__add__(a, b)
```

Por tanto:

- `self` es `a`, el operando izquierdo.
- `other` es `b`, el operando derecho.
- El método devuelve normalmente un nuevo objeto.

También puede ser un número:

```python
def __add__(self, other):
    if isinstance(other, (int, float)):
        other = Numero(other)
    if not isinstance(other, Numero):
        return NotImplemented
    return Numero(self.valor + other.valor)
```

La expresión `def __add__(self), other)` es incorrecta: cierra los paréntesis antes de `other` y produce un `SyntaxError`.

## 4. Operadores reflejados

En `3 + x`, Python intenta primero `int.__add__(x)`. Si el entero no sabe sumar un `Scalar`, devuelve `NotImplemented` y Python prueba:

```python
x.__radd__(3)
```

Aquí `self` vuelve a ser `x` y `other` es `3`. Por eso `__radd__` y `__rmul__` permiten que el objeto personalizado aparezca a la derecha.

`NotImplemented` significa “este tipo no sabe realizar esta operación”; permite que Python pruebe otra posibilidad. No es lo mismo que `None`.

## 5. `__repr__`: representación técnica

`__repr__` define la representación técnica de un objeto. Python la utiliza con `repr(obj)`, al inspeccionar un objeto en la consola y al mostrarlo dentro de listas, tuplas o diccionarios.

```python
class Resultado:
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Resultado(valor={self.valor!r})"

r = Resultado(0.7)
print(repr(r))  # Resultado(valor=0.7)
print([r])      # [Resultado(valor=0.7)]
```

Debe devolver siempre un `str`, ser informativo y preferiblemente permitir identificar cómo se construyó el objeto. `{valor!r}` usa `repr(valor)`, por eso conserva comillas y hace visibles caracteres especiales.

## 6. `__repr__` frente a `__str__`

- `__repr__`: representación técnica para programadores, depuración, logs y pruebas.
- `__str__`: representación amigable para personas; la usa `str(obj)` y `print(obj)`.
- Si no defines `__str__`, `print(obj)` utiliza `__repr__` como alternativa.

```python
class Resultado:
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Resultado(valor={self.valor!r})"

    def __str__(self):
        return f"Resultado: {self.valor:.2f}"

r = Resultado(0.7)
print(r)        # Resultado: 0.70
print(repr(r))  # Resultado(valor=0.7)
```

### Cuándo usar y qué evitar

- Implementa `__repr__` en casi todas tus clases propias.
- Hazlo corto e informativo: incluye los atributos esenciales.
- Implementa `__str__` cuando necesites una presentación amigable para usuarios finales.
- No uses `__repr__` como texto final si muestra detalles internos o información sensible.
- No provoques efectos secundarios ni cálculos costosos dentro de `__repr__`.
- Normalmente usa `repr(obj)` en vez de llamar directamente a `obj.__repr__()`.

## 7. Dunder usados por `Scalar`

- `__init__`: guarda `data`, `parents`, `op` y `label`.
- `__repr__`: muestra una representación técnica del nodo.
- `__add__` y `__mul__`: implementan suma y multiplicación, calculan el valor y conectan los operandos en `parents`.
- `__radd__` y `__rmul__`: soportan operaciones reflejadas con números normales.

```python
class Scalar:
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

> [!tip] No mutación
> `a + b` no modifica `a` ni `b`: devuelve una nueva instancia de `Scalar` y conserva los operandos originales.

## Repaso

- ¿Por qué `other` no es una palabra reservada?
- ¿Qué diferencia hay entre `__repr__` y `__str__`?
- ¿Qué ocurre cuando `__add__` devuelve `NotImplemented`?
