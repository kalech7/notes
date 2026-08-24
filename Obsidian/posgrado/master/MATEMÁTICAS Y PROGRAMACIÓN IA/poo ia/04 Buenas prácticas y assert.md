---
tags:
  - machine-learning
  - poo
  - python
---

# Buenas prácticas: atributos mutables y `assert`

Anterior: [[03 Métodos dunder]] · Siguiente: [[05 Scalar y autodiferenciación]]

## 1. El problema de los atributos de clase mutables

Una lista o un diccionario definido directamente en el cuerpo de una clase pertenece a la clase y puede ser compartido por todas sus instancias.

```python
class BadTrainingRun:
    metrics = []  # Una sola lista compartida

    def __init__(self, name):
        self.name = name

    def add_metric(self, value):
        self.metrics.append(value)

r1 = BadTrainingRun("baseline")
r2 = BadTrainingRun("candidate")
r1.add_metric(0.81)

print(r2.metrics)  # [0.81]: contaminación cruzada
```

El error es especialmente peligroso en experimentos de Machine Learning porque una ejecución puede contaminar silenciosamente las métricas de otra.

### Forma correcta

Crear la lista dentro de `__init__` produce una lista independiente por instancia:

```python
class TrainingRun:
    def __init__(self, name):
        self.name = name
        self.metrics = []

    def add_metric(self, value):
        self.metrics.append(value)

r1 = TrainingRun("baseline")
r2 = TrainingRun("candidate")
r1.add_metric(0.81)

print(r2.metrics)  # []
```

> [!important] Regla
> Los atributos de clase sirven para valores constantes o compartidos intencionadamente. El estado mutable propio de cada experimento debe vivir en `self`.

## 2. ¿Qué es `assert`?

`assert` comprueba una condición durante la ejecución:

```python
condicion = 3 > 2
assert condicion, "La condición debe cumplirse"
```

- Si la condición es `True`, Python continúa silenciosamente.
- Si es `False`, Python lanza `AssertionError` y detiene esa ejecución.

Conceptualmente equivale a:

```python
condicion = 3 > 2
if not condicion:
    raise AssertionError("La condición debe cumplirse")
```

## 3. Usos en Machine Learning

### Comprobar cálculos con tolerancia

Los `float` pueden contener pequeños errores de precisión. Por eso suele ser mejor comparar con una tolerancia:

```python
assert abs(z - 0.70) < 1e-12
```

### Verificar invariantes

```python
assert isinstance(x.data, float)
assert isinstance(x.parents, tuple)
```

### Comprobar identidad de objetos

Dos nodos pueden tener el mismo valor pero ser objetos distintos:

```python
assert a is not b
```

### Validar dimensiones

```python
assert len(features) == len(weights), "Desfase entre features y pesos"
```

## 4. Cuándo usar `assert`

Úsalo para pruebas, invariantes internas y comprobaciones durante el desarrollo. No lo uses para validar entradas de usuarios en APIs o formularios públicos: las aserciones pueden desactivarse con `python -O`. Para validación externa usa condiciones explícitas y errores adecuados:

```python
if edad < 0:
    raise ValueError("La edad no puede ser negativa")
```

## Repaso

- ¿Por qué `metrics = []` puede contaminar dos experimentos?
- ¿Dónde debe crearse una lista propia de cada instancia?
- ¿Qué diferencia hay entre `assert` y `raise ValueError`?
