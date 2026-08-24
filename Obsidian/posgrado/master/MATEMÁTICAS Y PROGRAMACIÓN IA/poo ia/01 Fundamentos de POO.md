---
tags:
  - machine-learning
  - poo
  - python
---

# Fundamentos de POO en Python

Anterior: [[00 Índice - POO e IA]] · Siguiente: [[02 Herencia y composición]]

## 1. ¿Por qué existe la POO?

Un programa manipula **datos** y ejecuta **acciones**. Sin POO, ambos pueden quedar separados:

```python
perro = {"nombre": "Toby", "edad": 3}

def ladrar(animal):
    return f"{animal['nombre']} dice guau"

def cumplir_anios(animal):
    animal["edad"] += 1
```

La coherencia depende de que el programador recuerde qué datos acepta cada función. La **programación orientada a objetos** agrupa datos y comportamientos relacionados en una unidad: el objeto.

## 2. Clase e instancia

- **Clase:** molde o plano que define atributos y comportamientos.
- **Instancia:** objeto concreto creado a partir de una clase.
- Cada instancia tiene su propio estado, aunque comparta los métodos definidos por la clase.

```python
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return f"{self.nombre} dice guau"

toby = Perro("Toby", 3)
luna = Perro("Luna", 5)

print(toby.ladrar())
print(luna.ladrar())
```

## 3. `self`: el objeto receptor

`self` es el objeto sobre el que se llamó el método. No es una palabra reservada: es el nombre usado por convención para el primer parámetro.

```python
toby.ladrar()
```

Equivale conceptualmente a:

```python
Perro.ladrar(toby)
```

Por eso `self.nombre` permite acceder al atributo de esa instancia. Todo lo que deba persistir en el objeto debe guardarse en `self`:

```python
def cumplir_anios(self):
    edad_temporal = self.edad + 1  # desaparece al terminar el método
    self.edad = self.edad + 1      # queda guardado en el objeto
```

## 4. Métodos normales y `describe()`

Un método de instancia recibe `self` y normalmente trabaja con el estado del objeto.

```python
class ScalarV2:
    def __init__(self, data, label=""):
        self.data = float(data)
        self.label = str(label)

    def describe(self):
        return f"{self.label}={self.data}"

x = ScalarV2(0.8, "x")
print(x.describe())
print(ScalarV2.describe(x))
```

`describe()` es un método normal: Python no lo activa por una sintaxis especial. Debemos llamarlo explícitamente con `x.describe()`.

## 5. Construcción e inicialización

En sentido estricto:

- `__new__` crea y devuelve la instancia.
- `__init__` inicializa los atributos de esa instancia.
- La instancia es el objeto final que podemos utilizar.

En la mayoría de las clases solo definimos `__init__`, porque Python hereda un `__new__` adecuado de `object`.

```python
class Scalar:
    def __init__(self, data, label="", parents=(), op=""):
        self.data = float(data)
        self.label = str(label)
        self.parents = tuple(parents)
        self.op = str(op)

x = Scalar(3, label="entrada")
print(x.data)     # 3.0
print(x.parents)  # ()
```

Las responsabilidades de `__init__` son guardar el estado inicial, establecer valores por defecto y garantizar invariantes mediante normalización o validación.

> [!tip] Regla mnemotécnica
> Si no guardas un dato en `self` dentro de `__init__`, el objeto no lo conservará como atributo.

## 6. Los cuatro pilares

### Encapsulamiento

Agrupa datos y comportamiento y controla el acceso por convención:

| Escritura | Significado |
| :--- | :--- |
| `self.dato` | Público. Se puede usar desde fuera. |
| `self._dato` | Interno o protegido por convención. |
| `self.__dato` | Name mangling para evitar colisiones en subclases. |

### Abstracción

Expone qué hace un componente y oculta cómo lo hace. En Machine Learning, el usuario puede llamar a `.forward()` o `.fit()` sin manipular cada detalle interno.

### Herencia

Permite que una clase hija reutilice y especialice una clase padre. Se estudia con más detalle en [[02 Herencia y composición]].

### Polimorfismo y Duck Typing

Distintos objetos responden al mismo método de maneras diferentes:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Robot:
    def hablar(self):
        return "Beep"

for entidad in [Perro("Toby"), Robot()]:
    print(entidad.hablar())
```

Python no exige una interfaz formal previa: si un objeto responde al método requerido, puede utilizarse (*duck typing*).

## 7. Tipos de métodos

```python
class Circulo:
    PI = 3.14159

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return Circulo.PI * self.radio ** 2

    @classmethod
    def desde_diametro(cls, diametro):
        return cls(diametro / 2)

    @staticmethod
    def es_positivo(valor):
        return valor > 0
```

- **Método de instancia:** recibe `self` y trabaja con el objeto.
- **Método de clase:** recibe `cls` y trabaja con la clase; se marca con `@classmethod`.
- **Método estático:** no recibe automáticamente `self` ni `cls`; se marca con `@staticmethod`.

## Repaso

- ¿Qué diferencia hay entre una clase y una instancia?
- ¿Qué objeto representa `self`?
- ¿Qué diferencia hay entre `__new__` y `__init__`?
- ¿Cuándo es útil `@classmethod`?
