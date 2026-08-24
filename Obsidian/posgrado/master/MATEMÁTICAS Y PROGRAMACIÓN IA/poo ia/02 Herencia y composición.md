---
tags:
  - machine-learning
  - poo
  - python
---

# Herencia y composición

Anterior: [[01 Fundamentos de POO]] · Siguiente: [[03 Métodos dunder]]

## 1. Herencia

La herencia permite que una clase hija reutilice y especialice una clase padre.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "..."

class Perro(Animal):
    def hablar(self):
        return "Guau"

class PerroConChip(Perro):
    def __init__(self, nombre, chip_id):
        super().__init__(nombre)
        self.chip_id = chip_id
```

`super()` delega en la clase padre la parte de la inicialización o del comportamiento que queremos reutilizar.

### Condición teórica: relación “es un”

La herencia es adecuada cuando la clase hija **es realmente un tipo de** la clase padre. Un `Perro` es un `Animal`; por eso puede utilizarse donde el programa espera un `Animal`.

La subclase debe respetar el contrato del padre. Esta idea se conoce como **Principio de Sustitución de Liskov**: sustituir un objeto de la clase base por uno de la subclase no debe romper el comportamiento esperado.

## 2. Composición

La composición construye un objeto complejo guardando otros objetos como atributos y delegando trabajo en ellos.

### Condición teórica: relación “tiene un”

La composición es adecuada cuando un objeto **tiene**, **usa** o **está formado por** otro objeto:

- Un `Coche` tiene un `Motor`.
- Una `Neurona` tiene un peso y un sesgo.
- Un nodo del grafo tiene padres.

```python
class Motor:
    def __init__(self, tipo="Eléctrico"):
        self.tipo = tipo

    def encender(self):
        return f"Motor {self.tipo} en marcha"

class Coche:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor

    def arrancar(self):
        return f"Coche {self.modelo}: {self.motor.encender()}"

motor_electrico = Motor("Eléctrico 400kW")
mi_auto = Coche("Sedán", motor_electrico)
print(mi_auto.arrancar())
```

`Coche` no hereda de `Motor`: conserva una instancia de `Motor` y delega en ella la operación `encender()`.

## 3. Diferencias fundamentales

| Criterio | Herencia | Composición |
| :--- | :--- | :--- |
| **Relación mental** | “Es un” (*Is-A*). | “Tiene un” o “usa un” (*Has-A*). |
| **Ejemplo** | `Perro` es un `Animal`. | `Coche` tiene un `Motor`. |
| **Estructura** | Jerarquía de clases. | Objeto ensamblado con componentes. |
| **Acoplamiento** | Alto: la hija depende del padre. | Más bajo: los componentes son reemplazables. |
| **Reutilización** | Hereda y sobrescribe métodos. | Delega trabajo a objetos internos. |
| **Flexibilidad** | La relación queda fijada al definir la clase. | Los componentes pueden cambiarse en ejecución. |
| **Polimorfismo** | Jerarquía común y sobrescritura. | Contratos, protocolos o *duck typing*. |
| **Pruebas** | Puede arrastrar comportamiento heredado. | Facilita sustituir componentes por *mocks*. |
| **Riesgo** | Jerarquías frágiles y rígidas. | Demasiados métodos pequeños de delegación. |

## 4. ¿Cuándo usar cada una?

### Usa herencia cuando

- La relación “es un” sea verdadera y estable.
- La subclase pueda sustituir a la clase padre sin romper el programa.
- La clase hija necesite especializar o ampliar el comportamiento del padre.
- Exista una jerarquía natural y pequeña, como `Perro` y `Gato` dentro de `Animal`.

No uses herencia únicamente para copiar métodos. Si la clase hija necesita desactivar o reinterpretar gran parte de lo heredado, probablemente no existe una relación real “es un”.

### Usa composición cuando

- La relación sea “tiene un”, “usa un” o “está formado por”.
- Quieras intercambiar un componente en tiempo de ejecución.
- Necesites combinar comportamientos sin crear muchas subclases.
- Quieras reducir el acoplamiento y facilitar pruebas unitarias.
- El sistema tenga variaciones independientes.

> [!tip] Regla práctica
> Primero intenta modelar la solución con composición. Elige herencia cuando puedas afirmar con claridad: **“la clase hija es sustituible por la clase padre y respeta el mismo contrato”**.

## 5. Aplicación en Machine Learning

La composición es central en los grafos de autodiferenciación:

```python
product = Scalar(
    data=w.data * x.data,
    parents=(w, x),
    op="*"
)
```

El resultado no hereda de `w` ni de `x`; contiene referencias a ambos en `parents`.

En PyTorch, una red compone submódulos como `nn.Linear`, `nn.Conv2d` y `nn.ReLU`; en `forward()` conecta sus salidas. No se crea una subclase diferente para cada combinación posible de capas.

## Repaso

- ¿La relación entre una `Neurona` y un `Scalar` es herencia o composición?
- ¿Qué significa el Principio de Sustitución de Liskov?
- ¿Qué ventaja ofrece poder cambiar un componente en tiempo de ejecución?
