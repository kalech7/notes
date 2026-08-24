---
tags:
  - machine-learning
  - poo
  - python
  - matematicas-programacion-ia
---

> [!tip] Versión separada para estudiar
> Esta nota completa fue reorganizada en notas temáticas dentro de [[poo ia/00 Índice - POO e IA]].

**Apunte del Módulo 02.** El objetivo del módulo no es enseñar POO en abstracto, sino construir una clase `Scalar` que represente **un valor y su historia computacional** dentro de un grafo. Esa clase es la base sobre la que después se implementan los motores de diferenciación automática (*Autodiff*) y la retropropagación (*backpropagation*) en librerías como PyTorch y Micrograd.

> [!abstract] La idea que sostiene todo el módulo
> **POO no deriva por sí sola: organiza el sistema y la historia computacional que harán posible derivar automáticamente.**

> [!info] Cómo leer esta nota
> - La **Parte 1** son los fundamentos de POO en Python explicados desde cero, con énfasis en buenas prácticas y errores comunes en Machine Learning.
> - La **Parte 2** es el tutorial práctico del Módulo 02: la construcción paso a paso de la clase `Scalar`, el grafo computacional de una neurona lineal, el orden topológico y la conexión directa con *Backpropagation*.

## Ubicación en el grafo del posgrado

- **Anterior:** [[Estructuras de Python en un experimento de IA]] — estructuras, invariantes, métricas y copias defensivas.
- **Esta nota:** POO, composición, dunder y construcción de `Scalar`.
- **Siguiente:** [[numpy pandas parquet arrow]] — transformación y almacenamiento de datos con contexto.
- **Aplicación del entrenamiento:** [[funcion de perdida]] — *feature engineering*, pérdida y gradientes.
- **Herramienta transversal:** [[UV]] — entornos y dependencias reproducibles.
- **Ruta dividida para estudiar:** [[poo ia/00 Índice - POO e IA]].

---

# PARTE 1 — Fundamentos de POO en Python

## 1. La idea de fondo: por qué existe la POO

Un programa manipula **datos** y ejecuta **acciones**. Sin POO, esas dos cosas viven separadas:

```python
# los datos
perro = {"nombre": "Toby", "edad": 3}

# las acciones, en otro sitio
def ladrar(animal):
    return f"{animal['nombre']} dice guau"

def cumplir_anios(animal):
    animal["edad"] += 1
```

Funciona, pero **nada conecta el diccionario con esas funciones**. Nadie impide escribir `perro["edad"] = "tres"`, ni pasar un diccionario incompatible a `ladrar()`. La coherencia depende exclusivamente de que el programador se acuerde.

> **POO junta los datos y las acciones que operan sobre ellos en una sola unidad.** Esa unidad es el objeto.

---

## 2. Clase e instancia

- La **clase** es el molde o el **plano** arquitectónico.
- La **instancia (u objeto)** es lo que sale del molde o el **edificio construido**.

```python
class Perro:                      # el molde
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        return f"{self.nombre} dice guau"

toby = Perro("Toby", 3)           # una instancia
luna = Perro("Luna", 5)           # otra instancia, estado independiente

toby.ladrar()                     # 'Toby dice guau'
luna.ladrar()                     # 'Luna dice guau'
```

Comparten el **comportamiento** (`ladrar`), pero cada objeto tiene su propio **estado** (`nombre`, `edad`).

---

## 3. `self`: lo que más confunde al principio

`self` es simplemente **el objeto sobre el que se llamó el método**. No es una palabra clave reservada de Python: es el nombre por convención del primer parámetro.

Cuando escribes:
```python
toby.ladrar()
```
Python internamente ejecuta:
```python
Perro.ladrar(toby)
```

**El objeto antes del punto se pasa como primer argumento.** Por eso el método lo declara en su firma y dentro puede leer `self.nombre`.

### ¿Qué es el método `describe()`?
En el tutorial del módulo se crea un método llamado `describe(self)` en `ScalarV2` y `LabeledScalar` para ilustrar esto:

```python
class ScalarV2:
    def __init__(self, data, label=""):
        self.data = float(data)
        self.label = str(label)

    # Método de instancia: devuelve una cadena descriptiva con el estado del objeto
    def describe(self):
        return f"{self.label}={self.data}"

x = ScalarV2(0.8, "x")

# Ambas líneas hacen EXACTAMENTE lo mismo:
print(x.describe())           # Sintaxis habitual de POO: 'x=0.8'
print(ScalarV2.describe(x))   # Python pasando 'x' explícitamente a self: 'x=0.8'
```

> [!note] Diferencias: describe() vs __repr__() vs Pandas describe()
> - **En tu clase (`ScalarV2`):** `describe()` es un método normal hecho a mano para mostrar los datos. Tienes que llamarlo tú explícitamente con `x.describe()`.
> - **`__repr__()`:** Es un método especial (*dunder*) que Python usa para obtener una representación inequívoca del objeto. `repr(x)` y la inspección de `x` en la terminal lo invocan; `print(x)` usa `__str__()` si existe y, si no, recurre a `__repr__()`.
> - **En Pandas (`df.describe()`):** En ciencia de datos, `describe()` es el método estándar de los DataFrames para calcular estadísticas rápidas (media, desviación estándar, min, max, cuartiles).

### Regla práctica
Todo lo que quieras **conservar en el objeto**, guárdalo en `self.algo`. Una variable normal dentro de un método muere al terminar la llamada:

```python
def cumplir_anios(self):
    edad = self.edad + 1        # variable local: se pierde al salir de la función
    self.edad = self.edad + 1   # esto SÍ persiste en el objeto
```

---

## 4. Construcción e inicialización (`__new__` y `__init__`)

### ¿Qué ocurre al crear un objeto?
En sentido estricto, `__new__` **crea y devuelve** la instancia, mientras que `__init__` la **inicializa**. En la mayoría de las clases solo necesitamos definir `__init__`; Python hereda un `__new__` adecuado de `object` y ejecuta ambos automáticamente al escribir `Perro("Toby", 3)`.

> [!important] Su misión principal
> `__init__` es el **"acta de nacimiento"** del objeto. Su trabajo es **inicializar su estado interno y asegurar que el objeto nazca en un estado válido, completo y coherente**. La creación de la instancia pertenece a `__new__`.

> [!tip] En resumen: instancia, `__new__` e `__init__`
> - **`__new__`:** Crea y devuelve la instancia.
> - **Inicializador (`__init__`):** Configura los atributos iniciales de esa instancia; no debe devolver otro objeto.
> - **Instancia:** Es el **objeto final ya creado** (el "ente vivo" que reside en la memoria RAM con sus propios datos).

```text
  Llamada de creación:
  perro = Perro("Toby", 3)
             │
             ▼
  ┌────────────────────────────────────────────────────────┐
  │ 1. __new__ crea la instancia                           │
  └──────────────────────────┬─────────────────────────────┘
                             ▼
  ┌────────────────────────────────────────────────────────┐
  │ 2. Se ejecuta automáticamente el inicializador __init__: │
  │    - Recibe 'self' (el objeto recién nacido)           │
  │    - Recibe los argumentos ("Toby", 3)                 │
  │    - Asigna atributos: self.nombre = "Toby", self.edad = 3 │
  │    - Aplica validaciones e invariantes de tipos        │
  └──────────────────────────┬─────────────────────────────┘
                             ▼
  3. El objeto completamente configurado se asigna a 'perro'
```

### Las 3 responsabilidades clave de `__init__`:
1. **Asignar el estado inicial:** Guardar las variables en `self.atributo` para que vivan dentro del objeto y no se borren.
2. **Definir valores por defecto:** Permitir que ciertos parámetros sean opcionales (ej. `label=""`, `parents=()`).
3. **Garantizar invariantes (normalización y validación):** Convertir tipos (`float()`, `tuple()`) o validar datos para que ningún objeto nazca roto o defectuoso.

### Ejemplo detallado:

```python
class Scalar:
    # Inicializador: define el estado inicial de cada nodo del grafo
    def __init__(self, data, label="", parents=(), op=""):
        # 1. Normalización de tipos (Invariantes)
        self.data = float(data)          # Asegura que siempre sea número flotante
        self.label = str(label)          # Asegura que sea texto
        self.parents = tuple(parents)    # Asegura que sea una tupla inmutable
        self.op = str(op)                # Símbolo de operación

# Al instanciar, pasamos los datos que recibirá __init__:
x = Scalar(3, label="entrada")

print(x.data)     # 3.0 (se convirtió automáticamente a float)
print(x.parents)  # ()  (tomó el valor por defecto: tupla vacía)
```

> [!tip] Regla mnemotécnica para acordarte
> **Si no lo guardas en `self` dentro de `__init__`, el objeto lo olvida al nacer.**
> Todo atributo que el objeto necesite recordar durante su vida debe asignarse como `self.nombre_atributo = valor`.

---

## 5. Los cuatro pilares de la POO

### 1. Encapsulamiento
Agrupar datos y comportamiento, y **controlar el acceso** desde fuera. En Python es por convención:

| Escritura | Significado | Convención |
| :--- | :--- | :--- |
| `self.dato` | Público | Se puede leer y modificar libremente. |
| `self._dato` | Protegido / Interno | "Uso interno, no lo toques desde fuera" (aviso formal). |
| `self.__dato` | Privado (*Name Mangling*) | Python altera el nombre interno para evitar colisiones en subclases. |

### 2. Abstracción
Exponer el **qué** hace un componente y ocultar el **cómo**. El usuario solo interactúa con métodos de alto nivel (como `.forward()` o `.fit()`) sin tener que preocuparse por la matemática o los punteros internos.

### 3. Herencia
Permite que una clase hija **reutilice y especialice** el código de una clase padre.

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
        super().__init__(nombre)   # Delega en Animal/Perro la inicialización del nombre
        self.chip_id = chip_id
```

> [!warning] La prueba de oro de la herencia (*Principio de Sustitución*)
> Usa herencia únicamente cuando exista una relación estricta de **"es un"** y puedas sustituir la clase base por la subclase sin romper el comportamiento esperado del sistema.

### 4. Polimorfismo (*Duck Typing*)
Distintos objetos responden **al mismo método** de maneras diferentes:

```python
class Robot:
    def hablar(self): return "Beep"

for entidad in [Perro("Toby", 3), Robot()]:
    print(entidad.hablar())  # Guau / Beep
```

En Python no se requiere una interfaz formal previa: *"si camina como pato y suena como pato, es un pato"* (*Duck Typing*).

---

## 6. Composición: La alternativa superior a la herencia

La **composición** es el principio de diseño mediante el cual **un objeto complejo se construye ensamblando objetos más simples como piezas de LEGO**. 

En lugar de heredar comportamiento de una clase padre, una clase **guarda instancias de otras clases dentro de sus propios atributos** (`self.componente = OtroObjeto()`) y delega trabajo en ellas.

### La regla lingüística: *"Es un"* vs *"Tiene un"*

- **Herencia (*Is-A* / "Es un"):** Úsala únicamente si existe una relación ontológica estricta.
  - *Un `Perro` **es un** `Animal`.*
- **Composición (*Has-A* / "Tiene un"):** Úsala para ensamblar sistemas a partir de piezas modulares.
  - *Un `Coche` **tiene un** `Motor`.* (Un coche no *es* un motor; si el motor se apaga o se cambia, el coche sigue siendo un vehículo).
  - *Una `Neurona` **tiene un** `Peso` y un `Sesgo`.*
  - *Un `Nodo` del grafo **tiene** `Padres`.*

---

### Ejemplo en código: Composición y Delegación

```python
class Motor:
    def __init__(self, tipo="Eléctrico"):
        self.tipo = tipo

    def encender(self):
        return f"Motor {self.tipo} en marcha (brrr...)"

class Coche:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor  # El coche GUARDA una instancia de Motor (Composición)

    def arrancar(self):
        # Delegación: el coche le pide a su motor interno que haga el trabajo
        mensaje_motor = self.motor.encender()
        return f"Coche {self.modelo}: {mensaje_motor}"

# Creamos las piezas de forma independiente:
motor_v8 = Motor(tipo="V8 Gasolina")
tesla_motor = Motor(tipo="Eléctrico 400kW")

# Ensamblamos mediante composición:
mi_auto = Coche("Sedán", tesla_motor)
print(mi_auto.arrancar())
# Salida: Coche Sedán: Motor Eléctrico 400kW en marcha (brrr...)
```

---

### ¿Por qué la industria prefiere Composición sobre Herencia?

> [!tip] Principio de Diseño de Software
> **"Favorece la composición de objetos sobre la herencia de clases"** (*Design Patterns: Gang of Four*).

1. **Bajo acoplamiento:** Si modificas la clase `Motor`, la clase `Coche` no se rompe mientras `Motor` mantenga su método `encender()`. En herencia, cambiar un método en la clase base puede romper inesperadamente múltiples subclases (*fragile base class problem*).
2. **Intercambiabilidad en tiempo de ejecución:** Puedes cambiar el motor de un coche en cualquier momento (`mi_auto.motor = motor_v8`). Con herencia, la estructura de clases queda congelada al definir el código.
3. **Evita la explosión combinatoria de clases:** Si intentas modelar variaciones con herencia, terminas con clases complejas y rígidas como `VehiculoVoladorAnfibioElectrico`. Con composición, simplemente combinas piezas: `[Alas, Helice, Bateria, Ruedas]`.

---

### Tabla Comparativa: Herencia vs Composición

| Criterio | Herencia (*Inheritance*) | Composición (*Composition*) |
| :--- | :--- | :--- |
| **Idea teórica** | La clase hija **es un tipo de** la clase padre (*Is-A*). | La clase contiene y utiliza otros objetos (*Has-A*). |
| **Ejemplo** | `Perro` es un `Animal`. | `Coche` tiene un `Motor`. |
| **Estructura** | Se construye una jerarquía de clases. | Se construye un objeto ensamblando componentes. |
| **Acoplamiento** | **Alto**: la hija depende de la implementación y el contrato del padre. | **Bajo**: cada componente puede evolucionar de forma más independiente. |
| **Reutilización** | Hereda métodos y puede sobrescribirlos. | Delega trabajo a los objetos que contiene. |
| **Flexibilidad** | Menor: la relación queda fijada al definir la clase. | Mayor: los componentes pueden cambiarse en tiempo de ejecución. |
| **Polimorfismo** | Se basa en una jerarquía común y métodos sobrescritos. | Se basa en contratos, protocolos o *duck typing*. |
| **Pruebas** | Puede requerir probar efectos heredados de toda la jerarquía. | Facilita probar cada componente por separado y sustituirlo por un *mock*. |
| **Riesgo principal** | Jerarquías rígidas, frágiles y con sobrescrituras inesperadas. | Crear demasiados métodos pequeños de delegación. |
| **Cuándo usarla** | Cuando existe una relación estable de **“es un”**, la subclase puede sustituir al padre y comparte su contrato. | Cuando existe una relación de **“tiene un”**, se quieren combinar comportamientos o cambiar componentes sin modificar la clase principal. |

### Teoría: ¿cuándo usar herencia y cuándo composición?

#### Usa herencia cuando

- La relación **“es un”** sea verdadera y estable, no solo una forma de reutilizar código.
- La subclase pueda utilizarse allí donde se espera la clase padre sin romper las reglas del programa. Esta es la idea central del **Principio de Sustitución de Liskov**.
- La clase hija necesite especializar o ampliar el comportamiento del padre manteniendo su contrato.
- Exista una jerarquía natural y pequeña, por ejemplo `Perro` y `Gato` como tipos de `Animal`.

No uses herencia únicamente para copiar métodos. Si la clase hija necesita ignorar, desactivar o reinterpretar gran parte del comportamiento heredado, probablemente la relación no es una verdadera relación **“es un”**.

#### Usa composición cuando

- La relación sea **“tiene un”**, **“usa un”** o **“está formado por”**.
- Quieras intercambiar una pieza en tiempo de ejecución, como cambiar un `Motor` por otro.
- Necesites combinar comportamientos sin crear una jerarquía extensa.
- Quieras reducir el acoplamiento y facilitar las pruebas unitarias.
- El sistema tenga muchas variaciones independientes. En Machine Learning, una red suele componerse de capas, funciones de activación, optimizadores y tensores en lugar de heredar de cada uno de ellos.

> [!tip] Regla práctica
> Primero intenta modelar la solución con composición. Elige herencia cuando puedas explicar con claridad: **“la clase hija es sustituible por la clase padre y respeta el mismo contrato”**.

---

### 🧠 ¿Por qué la Composición es el corazón de Machine Learning y PyTorch?

Todo el ecosistema moderno de IA (PyTorch, Keras, Micrograd, JAX) se basa casi exclusivamente en **composición**:

1. **En grafos de Autodiferenciación (`Scalar`):**
   - Cuando multiplicas `w * x`, el nodo resultante no "hereda" de `w` ni de `x`.
   - El nuevo nodo `Scalar` **contiene una referencia** a sus operandos en `self.parents = (w, x)`. El grafo computacional es una red de composición.
2. **En PyTorch (`nn.Module`):**
   - Una red neuronal no hereda de cada capa matemática.
   - La red **compone** múltiples sub-módulos: `self.fc1 = nn.Linear(...)`, `self.conv = nn.Conv2d(...)`, `self.relu = nn.ReLU()`.
   - En su método `forward(x)`, la red simplemente pasa los tensores de un componente compuesto al siguiente.

---

## 7. Métodos Especiales (*Dunder Methods*)

Los métodos con doble guion bajo (`__nombre__`) son los ganchos que conectan tu clase con la sintaxis nativa de Python:

Se llaman **dunder** por *double underscore*. Python los invoca en respuesta a una operación del lenguaje; normalmente no necesitas llamarlos directamente. Por ejemplo, `a + b` busca `a.__add__(b)`. Si ese método devuelve `NotImplemented`, Python puede probar el método reflejado del otro operando, como `b.__radd__(a)`.

### Los dunder son métodos

Un dunder es un **método especial definido dentro de una clase**. Es decir, se escribe con `def`, recibe argumentos y contiene instrucciones, igual que cualquier otro método:

```python
class Scalar:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        return Scalar(self.data + other.data)
```

No es un atributo, una palabra reservada ni una función independiente. La diferencia está en **quién lo llama**:

- Un método normal se llama explícitamente: `x.describe()`.
- Un dunder suele ser llamado automáticamente por Python: `x + y` activa `x.__add__(y)`.

En `def __add__(self, other)`, `self` se recibe automáticamente porque el método pertenece a la instancia; `other` es el argumento que entrega la operación. La palabra **especial** significa que Python reconoce ese nombre como parte de un protocolo del lenguaje.

> [!warning] No confundir conceptos
> “Método especial” no significa necesariamente “método de clase” (`@classmethod`). `__add__` y `__repr__` suelen trabajar con una instancia y reciben `self`; `__new__` recibe `cls` porque participa en la creación de la instancia. Todos son dunder, pero no todos son métodos de clase.

| Sintaxis en Python | Método especial invocado |
| :--- | :--- |
| `Scalar(2.0)` | `__new__` crea la instancia y `__init__` la inicializa |
| `repr(x)` | `x.__repr__()` |
| `print(x)` | `x.__str__()`; si no existe, usa `x.__repr__()` |
| `a + b` | `a.__add__(b)`; si devuelve `NotImplemented`, puede probar `b.__radd__(a)` |
| `a * b` | `a.__mul__(b)`; si devuelve `NotImplemented`, puede probar `b.__rmul__(a)` |
| `2 + a` (reflejado) | `a.__radd__(2)` |
| `2 * a` (reflejado) | `a.__rmul__(2)` |
| `len(x)` | `__len__` |
| `x[i]` | `__getitem__` |
| `x(...)` | `__call__` |

### ¿Qué significan `self` y `other` en `__add__`?

La definición correcta es:

```python
def __add__(self, other):
    ...
```

La coma va **dentro** de los paréntesis. `other` no es una palabra reservada de Python: es un nombre elegido por convención para representar al **otro operando**, normalmente el que está a la derecha del signo `+`. También podríamos llamarlo `otro`, pero `other` es el nombre habitual en ejemplos y librerías.

Si escribimos:

```python
a = Scalar(2)
b = Scalar(3)
c = a + b
```

Python transforma conceptualmente la última línea en:

```python
c = Scalar.__add__(a, b)
```

Por tanto:

- `self` es `a`, el operando de la izquierda.
- `other` es `b`, el operando de la derecha.
- El método debe devolver el resultado de la suma, normalmente un nuevo objeto.

También puede ser un número normal:

```python
x = Scalar(2)
y = x + 3
```

En este caso, `self` es `x` y `other` es `3`. Por eso la clase usa `_coerce(other)` para convertir ese `3` en `Scalar(3)` antes de operar. La expresión `def __add__(self), other)` es incorrecta: cierra los paréntesis demasiado pronto y produce un `SyntaxError`.

Cuando escribimos `3 + x`, Python intenta primero la suma del entero. Si ese tipo no sabe sumar un `Scalar`, Python prueba el método reflejado:

```python
x.__radd__(3)
```

Aquí `self` vuelve a ser `x` y `other` es `3`. Por eso existen `__radd__` y `__rmul__`: permiten que el objeto personalizado aparezca a la derecha del operador.

### ¿Qué es exactamente `__repr__`?

`__repr__` es el dunder que define la **representación técnica** de un objeto. Su nombre viene de *representation*. Python lo utiliza cuando llamamos a `repr(obj)` y, normalmente, cuando inspeccionamos un objeto directamente en la consola interactiva. También se usa para mostrar objetos dentro de listas, tuplas y diccionarios.

En la clase `Scalar`:

```python
def __repr__(self):
    label = f", label={self.label!r}" if self.label else ""
    return f"Scalar(data={self.data}{label}, op={self.op!r})"
```

El resultado es informativo y permite identificar rápidamente el estado del nodo:

```python
x = Scalar(0.8, label="x")
print(repr(x))  # Scalar(data=0.8, label='x', op='')
```

La expresión `{self.label!r}` usa la conversión `repr()` del texto, por eso aparece con comillas (`'x'`). Es útil para distinguir un texto vacío, espacios, saltos de línea o caracteres especiales.

### `__repr__` frente a `__str__`

- **`__repr__`**: representación técnica para programadores, depuración y diagnóstico. Debe ser clara, precisa y devolver siempre un `str`.
- **`__str__`**: representación amigable para personas, usada por `str(obj)` y por `print(obj)`.
- Si una clase no define `__str__`, `print(obj)` utiliza su `__repr__` como alternativa.

```python
class Resultado:
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Resultado(valor={self.valor!r})"

    def __str__(self):
        return f"Resultado: {self.valor:.2f}"

r = Resultado(0.7)
print(r)        # Resultado: 0.70  -> usa __str__
print(repr(r))  # Resultado(valor=0.7) -> usa __repr__
```

### ¿Cuándo usar `__repr__` y cuándo no?

- **Úsalo** en casi todas las clases propias: ayuda a inspeccionar objetos en notebooks, terminales, logs y pruebas.
- **Hazlo informativo y corto**: incluye los atributos esenciales, no todo el grafo completo ni cálculos costosos.
- **Usa `__str__` además** cuando el objeto necesite una presentación pensada para usuarios finales.
- **No uses `__repr__` como texto final para usuarios** si contiene detalles internos, nombres técnicos o información sensible.
- **No provoques efectos secundarios** dentro de `__repr__`: representar un objeto no debería modificarlo, entrenar un modelo ni ejecutar operaciones costosas.
- Normalmente no llames `obj.__repr__()` directamente; usa `repr(obj)` y deja que Python aplique el protocolo correctamente.

### Dunder usados por `Scalar`

- **`__init__`**: guarda el estado inicial (`data`, `parents`, `op` y `label`).
- **`__repr__`**: devuelve una representación técnica útil para depuración. Debe devolver siempre un `str`; en `Scalar` muestra `data`, `label` y `op`.
- **`__add__` y `__mul__`**: implementan `+` y `*`; convierten números normales a `Scalar`, calculan el valor y conectan los operandos en `parents`.
- **`__radd__` y `__rmul__`**: permiten que el `Scalar` aparezca a la derecha de un número, como en `2 + x` o `2 * x`.
- **`NotImplemented`**: indica que la operación no es compatible con ese tipo; no es lo mismo que `None` ni que lanzar manualmente un `TypeError`.

```python
class Numero:
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return f"Numero({self.valor!r})"

    def __str__(self):
        return str(self.valor)

    def __add__(self, otro):
        if not isinstance(otro, Numero):
            return NotImplemented
        return Numero(self.valor + otro.valor)

x = Numero(2)
print(x)        # 2: usa __str__
print(repr(x))  # Numero(2): usa __repr__
```

> [!warning] No todos los dunder son constructores
> `__init__`, `__repr__`, `__add__` y `__call__` son métodos especiales, pero cada uno responde a una operación distinta. No se ejecutan todos al crear una instancia.

---

## 8. Tipos de métodos en una clase

```python
class Circulo:
    PI = 3.14159                       # Atributo de CLASE

    def __init__(self, radio):
        self.radio = radio             # Atributo de INSTANCIA

    def area(self):                    # Método de INSTANCIA (recibe self)
        return Circulo.PI * self.radio ** 2

    @classmethod
    def desde_diametro(cls, d):        # Método de CLASE (recibe cls, constructor alternativo)
        return cls(d / 2)

    @staticmethod
    def es_positivo(val):              # Método ESTÁTICO (utilidad independiente)
        return val > 0
```

---

## 9. 🚨 La Trampa Mortal en ML: Atributos de Clase Mutables

> [!danger] El error más destructivo en experimentos de IA
> Definir listas o diccionarios en el cuerpo de la clase crea **una sola lista en memoria compartida por todos los experimentos**.

```python
# ❌ ERROR CATASTRÓFICO:
class BadTrainingRun:
    metrics = []  # Atributo de CLASE: ¡compartido globalmente!

    def __init__(self, name):
        self.name = name

    def add_metric(self, val):
        self.metrics.append(val)

r1 = BadTrainingRun("baseline")
r2 = BadTrainingRun("candidate")
r1.add_metric(0.81)

print("r2 metrics:", r2.metrics)  # [0.81] -> ¡Contaminación cruzada silenciosa!
```

```python
# ✅ FORMA CORRECTA:
class TrainingRun:
    def __init__(self, name):
        self.name = name
        self.metrics = []  # Atributo de INSTANCIA: lista independiente por objeto

    def add_metric(self, val):
        self.metrics.append(val)

r1 = TrainingRun("baseline")
r2 = TrainingRun("candidate")
r1.add_metric(0.81)

print("r2 metrics:", r2.metrics)  # [] -> Aislado y reproducible
```

---

## 10. `assert`: El inspector de calidad e invariantes

### ¿Qué es `assert`?
`assert` (afirmar/asegurar) es una instrucción de Python que valida condiciones durante la ejecución:

> **"Asegúrate de que esta condición sea `True`. Si no se cumple, detén el programa inmediatamente y lanza un error `AssertionError`."**

```python
condicion = 3 > 2
assert condicion, "La condición debe cumplirse"
```

- **Si la condición es `True`:** Python continúa silenciosamente a la siguiente línea.
- **Si la condición es `False`:** Python interrumpe el programa y muestra el error.

Equivale a:
```python
condicion = 3 > 2
if not condicion:
    raise AssertionError("La condición debe cumplirse")
```

---

### ¿Para qué se usa en los notebooks de IA y Machine Learning?

#### 1. Comprobar cálculos matemáticos con tolerancia decimal:
Las computadoras tienen pequeñas imprecisiones al calcular con números flotantes (`float`). Por eso no se compara con == , sino con una tolerancia:
```python
# Verifica que el error sea menor que 0.000000000001
assert abs(z - 0.70) < 1e-12
```

#### 2. Verificar invariantes y tipos de datos:
```python
# Comprueba que el objeto Scalar haya normalizado bien sus atributos
assert isinstance(x.data, float)
assert isinstance(x.parents, tuple)
```

#### 3. Comprobar identidades en memoria (`is not`):
```python
# Verifica que dos nodos sean objetos distintos aunque tengan el mismo valor
assert a is not b
```

#### 4. Validar dimensiones de matrices y tensores:
```python
# Asegura que las dimensiones de entrada coincidan con los pesos antes de operar
assert len(features) == len(weights), "Desfase entre features y pesos"
```

> [!tip] Cuándo usar `assert`
> - **Úsalo:** Para pruebas unitarias, verificar invariantes internas y asegurar que tu lógica matemática no tenga fallos mientras desarrollas.
> - **No lo uses:** Para validar entradas de usuario final en formularios web o APIs públicas (para eso usa `if` y `raise ValueError`).

---

# PARTE 2 — De la Neurona Lineal al Grafo Computacional (`Scalar`)

## 1. El Problema: Un `float` pierde la historia computacional

Consideremos el cálculo de una neurona lineal con una entrada $x$, un peso $w$ y un sesgo $b$:

$$
z = wx + b
$$

En Python plano:

```python
x = 0.8
w = 1.25
b = -0.30

z = (w * x) + b
print(f"z = {z:.2f}")  # 0.70
print(type(z))         # <class 'float'>
```

> [!danger] La limitación del tipo `float`
> El número `0.70` es suficiente para inferencia, pero **ha olvidado por completo cómo se calculó**:
> - No sabe que provino de `w` y `x`.
> - No sabe qué operaciones se ejecutaron (`*` y luego `+`).
> - Sin esa historia, es imposible calcular derivadas automáticamente (*Backpropagation*).

Para entrenar un modelo, necesitamos transformar el valor numérico en una **representación conjunta**:
$$\text{Valor numérico} \quad \Longrightarrow \quad \text{Estado} + \text{Relaciones (padres)} + \text{Operaciones}$$

---

## 2. Construcción Incremental de la Clase `Scalar`

### Fase 1: Identidad vs Igualdad de Valor (`ScalarV1`)

```python
class ScalarV1:
    def __init__(self, data: float, label: str = ""):
        self.data = float(data)
        self.label = str(label)

a = ScalarV1(0.8, "a")
b = ScalarV1(0.8, "b")

print("Mismo valor (==):", a.data == b.data)  # True
print("Mismo objeto (is):", a is b)           # False
```

> [!important] Identidad en IA
> Dos nodos pueden tener el mismo valor ($0.8$), pero representan variables distintas en el grafo (ej. una entrada y un sesgo). Usar objetos garantiza que tengan identidades únicas en memoria.

---

### Fase 2: Comportamiento y el método `.describe()` (`ScalarV2`)

Añadimos un método para inspeccionar el estado propio de cada nodo:

```python
class ScalarV2:
    def __init__(self, data, label=""):
        self.data = float(data)
        self.label = str(label)

    def describe(self):
        return f"{self.label}={self.data}"

x2 = ScalarV2(0.8, "x")
print(x2.describe())  # 'x=0.8'
```

---

### Fase 3: Invariantes y Conversión de Tipos (`ScalarV3`)

Una **invariante** asegura que los datos siempre mantengan tipos conocidos y seguros:

```python
class ScalarV3:
    def __init__(self, data, parents=(), op="", label=""):
        self.data = float(data)          # Invariante: siempre float
        self.parents = tuple(parents)    # Invariante: tupla inmutable de padres
        self.op = str(op)                # Símbolo de la operación ('+', '*')
        self.label = str(label)
```

---

### Fase 4: Composición de Nodos (`ScalarV4`)

El resultado de una multiplicación no es un subtipo de sus factores: **contiene referencias a sus factores**.

```python
x4 = ScalarV3(0.8, label="x")
w4 = ScalarV3(1.25, label="w")

product = ScalarV3(
    data=w4.data * x4.data,
    parents=(w4, x4),  # COMPOSICIÓN: Guarda referencias a los nodos de entrada
    op="*",
    label="product"
)

print(product.data)     # 1.0
print(product.parents)  # (w4, x4)
print(product.op)       # '*'
```

> [!important] ¿Por qué Composición y no Herencia en el Grafo?
> Si usáramos herencia, tendríamos que crear decenas de subclases como `class AddScalar(Scalar)` o `class MulScalar(Scalar)`. 
> Con **composición**, una única clase `Scalar` modela cualquier nodo del grafo simplemente guardando referencias a sus operandos de entrada (`parents=(w4, x4)`) y la operación ejecutada (`op='*'`).

---

### Fase 5: Herencia y `super()` (`LabeledScalar`)

Cuando queremos especializar un `Scalar` para que incluya `describe()` usando herencia:

```python
class LabeledScalar(ScalarV3):
    def __init__(self, data, label):
        super().__init__(data, label=label)

    def describe(self):
        return f"{self.label}={self.data}"

act = LabeledScalar(1.5, "activation")
print(act.describe())  # 'activation=1.5'
```

---

## 3. La Clase `Scalar` Completa

Implementamos la sobrecarga de operadores con el patrón **Convertir $\rightarrow$ Calcular $\rightarrow$ Conectar**:

```python
class Scalar:
    """Nodo escalar para un grafo computacional con memoria topológica."""

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
        """Permite operar con números estándar de Python (int, float)."""
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
        return Scalar(
            self.data + other.data,
            parents=(self, other),
            op="+"
        )

    def __mul__(self, other):
        other = self._coerce(other)
        if other is NotImplemented:
            return NotImplemented
        return Scalar(
            self.data * other.data,
            parents=(self, other),
            op="*"
        )

    # Operadores reflejados para soportar: 2 + x  o  2 * x
    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other
```

> [!tip] Principio de No Mutación
> `a + b` nunca modifica `a` ni `b`. Siempre retorna una nueva instancia de `Scalar`. Los operandos originales permanecen inalterados.

---

## 4. Caso Integrado: La Neurona Lineal con Memoria

Ahora repetimos el cálculo de la neurona usando `Scalar`:

```python
x = Scalar(0.8, label="x")
w = Scalar(1.25, label="w")
b = Scalar(-0.30, label="b")

product = w * x
score = product + b
score.label = "score"

print("product =", product)  # Scalar(data=1.0, op='*')
print("score   =", score)    # Scalar(data=0.7, label='score', op='+')
```

### Visualización del Grafo Acíclico Dirigido (DAG):

```text
  w (1.25) ──┐
             ├──► [*] product (1.00) ──┐
  x (0.80) ──┘                         ├──► [+] score (0.70)
                                       │
  b (-0.30) ───────────────────────────┘
```

---

## 5. Algoritmo de Orden Topológico (*Topological Sort*)

Para evaluar el grafo o propagar gradientes, necesitamos procesar los nodos en orden causal (los padres antes que los hijos).

```python
def topo(root):
    ordered = []
    visited = set()

    def visit(node):
        # Usamos id(node) para identificar el objeto por su posición exacta en memoria
        if id(node) in visited:
            return
        visited.add(id(node))

        for parent in node.parents:
            visit(parent)

        ordered.append(node)

    visit(root)
    return ordered

def node_name(node):
    return node.label or node.op or str(node.data)

ordered = topo(score)
names = [node_name(n) for n in ordered]
print(" -> ".join(names))
# Salida: w -> x -> * -> b -> score
```

> [!important] ¿Por qué id(node)?
> `id(node)` devuelve un identificador entero único para ese objeto durante su vida; no es necesario interpretarlo como una dirección física de memoria. Esto evita colisiones de identidad si dos nodos tienen el mismo valor numérico o si se personaliza la igualdad `__eq__`.

---

## 6. Abstracción de Alto Nivel: `LinearNeuron`

Podemos componer los objetos `Scalar` dentro de una clase que modele la neurona completa:

```python
class LinearNeuron:
    def __init__(self, weight, bias):
        self.weight = Scalar(weight, label="w")
        self.bias = Scalar(bias, label="b")

    def forward(self, x):
        x = x if isinstance(x, Scalar) else Scalar(x, label="x")
        output = self.weight * x + self.bias
        output.label = "score"
        return output

neuron = LinearNeuron(1.25, -0.30)
prediccion = neuron.forward(0.8)

print(prediccion)  # Scalar(data=0.7, label='score', op='+')
```

---

## 7. El Puente hacia *Backpropagation* (Autodiferenciación)

La POO construyó el andamiaje del grafo. Para convertir esto en un motor como **Micrograd** o **PyTorch Autograd**, solo falta añadir:

1. **`self.grad = 0.0`**: Para acumular $\frac{\partial \mathcal{L}}{\partial \text{nodo}}$.
2. **`self._backward()`**: La derivada local para cada operación:
   - **Suma** ($c = a + b$): $\frac{\partial \mathcal{L}}{\partial a} = \frac{\partial \mathcal{L}}{\partial c} \cdot 1$
   - **Multiplicación** ($c = a \cdot b$): $\frac{\partial \mathcal{L}}{\partial a} = \frac{\partial \mathcal{L}}{\partial c} \cdot \text{b.data}$
3. **Paso hacia atrás**: Recorrer `reversed(topo(loss))` ejecutando `node._backward()`.
4. **Acumulación (`+=`)**: Para aplicar la regla de la cadena multivariable cuando una variable se reutiliza en varias ramas.

---

# Resumen General

| Concepto | En una línea |
| :--- | :--- |
| **Clase / Instancia** | El molde vs el objeto concreto con estado propio. |
| **`self`** | El objeto receptor de la llamada: `a.f()` es `Clase.f(a)`. |
| **`__init__`** | Constructor que fija el estado inicial y las invariantes. |
| **Composición sobre Herencia** | Un nodo *tiene* operandos (`parents`); no *es* un tipo de suma. |
| **Atributos de Clase Mutables** | ⚠️ Trampa: nunca pongas listas o dicts a nivel de clase para experimentos. |
| **`Scalar`** | Representación conjunta: `data` + `parents` + `op` + `label`. |
| **Dunder Methods** | Conectan la sintaxis nativa (`+`, `*`, `repr`) con el grafo. |
| **Orden Topológico** | Ordena las dependencias del grafo de causas a efectos para hacer posible *Backprop*. |
