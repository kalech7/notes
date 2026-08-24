**Apunte del Módulo 01.** El objetivo de este módulo no es memorizar la sintaxis de Python en abstracto, sino aprender a elegir y combinar las estructuras de datos fundamentales (`list`, `tuple`, `dict`) haciendo explícitas las **invariantes** del dato dentro de un pipeline o experimento de Inteligencia Artificial.

> [!abstract] La idea central en una frase
> En Inteligencia Artificial, la elección de la estructura de datos no es solo una cuestión de estilo: **es un contrato de diseño que previene la corrupción silenciosa de experimentos y define cómo fluye la información.**

---

# 1. El Concepto Clave: Invariantes en IA

Una **invariante** es una propiedad o condición que debe mantenerse verdadera en todo momento durante la ejecución de un programa.

En proyectos de Machine Learning / Deep Learning, los datos tienen naturalezas muy distintas:
- **Historiales de entrenamiento:** Crecen con cada época/iteración (dinámicos y ordenados).
- **Pesos y nombres de características (*Features*):** Tienen una correspondencia estricta $1:1$ por posición que nunca debe desfasarse (estáticos y posicionales).
- **Métricas de evaluación:** Deben ser interpretables y consultarse por su nombre semántico, no por un índice numérico arbitrario.
- **Configuraciones de hiperparámetros:** Deben actuar como identificadores únicos e inalterables para comparar modelos.

Elegir la estructura correcta hace que el propio lenguaje garantice estas invariantes.

---

# 2. `list`: Secuencias dinámicas y el peligro del *Aliasing*

## ¿Cuándo usar una lista?
Una `list` es una colección **ordenada y mutable**. Es la estructura idónea cuando la membresía o la cantidad de elementos cambia a lo largo del tiempo.

### Caso de uso en IA: Curva de pérdida (*Loss History*)
Durante el entrenamiento de una red neuronal o clasificador, registramos el error (*loss*) al final de cada época para graficar el progreso o aplicar *Early Stopping*.

```python
loss_history = [0.82, 0.57, 0.41]
loss_history.append(0.33)

print("loss por época:", loss_history)
print("mejor loss:", min(loss_history))
# Salida:
# loss por época: [0.82, 0.57, 0.41, 0.33]
# mejor loss: 0.33
```

---

## ⚠️ El peligro crítico en IA: *Aliasing* (Mismo objeto en memoria)

En Python, las variables no son cajas que contienen datos; son **etiquetas (punteros) que apuntan a objetos en memoria**. 

Cuando haces `b = a` sobre una lista, **no estás creando una copia**, sino asignando una segunda etiqueta al mismo objeto en memoria.

```python
baseline_losses = [0.82, 0.57]
reported_losses = baseline_losses      # ¡Aliasing! Apuntan a la misma dirección
reported_losses.append(0.41)

print("baseline:", baseline_losses)
print("mismo objeto:", reported_losses is baseline_losses)
# Salida:
# baseline: [0.82, 0.57, 0.41]
# mismo objeto: True
```

### ¿Por qué esto es catastrófico en IA?
Imagina que estás entrenando un modelo base (*baseline*) y quieres probar una variante. Si compartes la lista por referencia, cualquier modificación en la variante modificará retroactivamente el registro del baseline, contaminando tus métricas y arruinando la reproducibilidad del experimento.

```
                  ┌───────────────────────┐
baseline_losses ──►│ [0.82, 0.57, 0.41]   │ (Mismo bloque de memoria)
                  └───────────────────────┘
reported_losses ──►
```

> [!warning] Regla de Oro
> Para desacoplar dos listas, usa siempre una copia explícita:
> `reported_losses = list(baseline_losses)` o `reported_losses = baseline_losses.copy()`

---

# 3. `tuple`: Inmutabilidad posicional y Hashabilidad

## ¿Cuándo usar una tupla?
Una `tuple` es una colección **ordenada e inmutable**. Una vez creada, no se pueden reasignar, agregar ni eliminar elementos.

### Caso de uso 1: El contrato posicional (Features y Pesos)
En modelos lineales o capas densas, el peso $w_i$ multiplica exactamente a la característica $x_i$. La posición es el contrato matemático:

```python
FEATURES = ("bytes_per_sec", "packets_per_sec", "duration_sec")
WEIGHTS = (0.0010, 0.0350, -0.0750)

# strict=True asegura que ambas tuplas tengan exactamente la misma longitud (Python 3.10+)
for feature, weight in zip(FEATURES, WEIGHTS, strict=True):
    print(f"{feature:18s} -> {weight:+.4f}")

# Salida:
# bytes_per_sec      -> +0.0010
# packets_per_sec    -> +0.0350
# duration_sec       -> -0.0750
```

> [!tip] ¿Por qué no usar una lista aquí?
> Si `FEATURES` fuera una lista, cualquier función externa podría ejecutar accidentalmente un `FEATURES.pop()` o `FEATURES.append()`, desalineando todos los pesos matemáticos silenciosamente. La tupla **protege la integridad estructural**.

---

### Caso de uso 2: Claves compuestas (*Hashability*)
Las tuplas cuyos elementos son inmutables son **hashables**, lo que significa que pueden usarse como claves en diccionarios (`dict`) o elementos en conjuntos (`set`). Las listas **no** pueden ser claves.

```python
# Clave compuesta inmutable: (nombre_modelo, umbral_clasificación)
experiment_key = ("linear-risk-model", 0.5)
print("clave del experimento:", experiment_key)
# Salida: ('linear-risk-model', 0.5)
```

---

## ⚠️ Matiz avanzado: Inmutabilidad Superficial (*Shallow Immutability*)

La tupla garantiza que **las referencias a sus posiciones no cambiarán**, pero si uno de los objetos contenidos dentro de la tupla es mutable (como una lista), **el estado interno de ese objeto sí puede cambiar**.

```python
epoch_losses = [0.82, 0.57]
run_record = (epoch_losses, "train")

# Modificamos la lista externa que está dentro de la tupla:
epoch_losses.append(0.41)

print(run_record)
# Salida: ([0.82, 0.57, 0.41], 'train')
```

```
┌────────────────────────────────────────┐
│ Tupla run_record                       │
│ ┌──────────────┐     ┌───────────────┐ │
│ │ Puntero [0]  │     │ "train" [1]   │ │
│ └──────┬───────┘     └───────────────┘ │
└────────┼───────────────────────────────┘
         ▼
┌───────────────────────────┐
│ Lista epoch_losses        │  <--- Esta lista SÍ puede mutar
│ [0.82, 0.57, 0.41]        │
└───────────────────────────┘
```

> [!important] Cuidado
> Meter una lista dentro de una tupla anula la inmutabilidad global y hace que la tupla deje de ser *hashable* (no podrás usar `run_record` como clave de diccionario).

---

# 4. `dict`: Acceso semántico por pares clave–valor

## ¿Cuándo usar un diccionario?
Un `dict` mapea claves únicas a valores. Se utiliza cuando el acceso a los datos debe hacerse mediante **nombres semánticos** y no mediante posiciones numéricas.

### Caso de uso en IA: Almacenamiento de Métricas
Acceder a una métrica como `metrics[2]` es frágil y poco legible (¿era *Recall* o *Precision*?). Un diccionario hace explícito el significado:

```python
metrics = {
    "accuracy": 1.00,
    "precision": 1.00,
    "recall": 1.00,
    "f1": 1.00,
}

print("F1:", metrics["f1"])

# Acceso seguro mediante .get() con valor por defecto
print("AUC disponible:", metrics.get("auc", "no calculado"))
# Salida:
# F1: 1.0
# AUC disponible: no calculado
```

> [!tip] Uso de `.get()`
> En pipelines de experimentación, no todos los modelos calculan las mismas métricas (ej. *AUC-ROC* solo aplica a probabilidades). Usar `metrics.get("auc", default)` previene caídas por `KeyError` cuando se procesan modelos heterogéneos.

---

# 5. Integración: Registro de Experimentos (*Experiment Registry*)

En el notebook se combinan las tres estructuras para construir un sistema de registro de modelos robusto y desacoplado:

1. **`tuple`**: Identificador compuesto e inmutable del experimento `(modelo, umbral)`.
2. **`dict`**: Estructura general y almacenamiento de métricas nombradas.
3. **`list`**: Historial cronológico de la pérdida por época.

```python
registry = {}

def register_run(model_name, threshold, metrics, losses):
    key = (model_name, threshold)            # tuple: identidad estable y hashable
    registry[key] = {                        # dict: campos semánticos
        "metrics": dict(metrics),            # COPIA DEFENSIVA del diccionario
        "loss_history": list(losses),        # COPIA DEFENSIVA de la lista
    }

# Registrar una corrida:
register_run("linear-risk-model", 0.5, metrics, loss_history)
print(registry)
```

**Salida estructurada:**
```python
{
    ('linear-risk-model', 0.5): {
        'metrics': {'accuracy': 1.0, 'precision': 1.0, 'recall': 1.0, 'f1': 1.0},
        'loss_history': [0.82, 0.57, 0.41, 0.33]
    }
}
```

### ¿Por qué son vitales las Copias Defensivas (`dict()`, `list()`)?
Si dentro de `register_run` hicieras simplemente:
```python
# ❌ INCORRECTO:
registry[key] = {
    "metrics": metrics,
    "loss_history": losses
}
```
Cualquier entrenamiento posterior que reutilice y modifique las variables `metrics` o `losses` sobrescribiría los valores ya almacenados en el `registry`. 
Hacer `dict(metrics)` y `list(losses)` genera un nuevo bloque de memoria que "congela" el estado del experimento en ese instante.

---

# 6. Resumen y Criterio de Decisión

| Estructura | Mutabilidad | Ordenada | Clave de Dict (*Hashable*) | Rol ideal en proyectos de IA / ML |
| :--- | :--- | :--- | :--- | :--- |
| **`list`** | **Mutable** | Sí | ❌ No | Secuencias temporales, curvas de pérdida (*loss*), lotes dinámicos de datos. |
| **`tuple`** | **Inmutable** | Sí |  Sí (si su contenido es inmutable) | Definición estática de *features*, dimensiones de tensores (`shape`), claves compuestas de experimentos. |
| **`dict`** | **Mutable** | Sí (por inserción) | ❌ No | Hiperparámetros de modelos, métricas nombradas, registros de experimentos, metadatos. |

---

# 7. Conexión con los siguientes temas

- **Módulo anterior:** [[UV]] prepara el entorno reproducible donde se ejecutan estos experimentos.
- **Hacia la Programación Orientada a Objetos:** Cuando las combinaciones de `dict`, `tuple` y `list` requieren comportamientos complejos o validaciones automáticas, pasamos a encapsularlas en clases y objetos. La ruta de estudio está en [[poo ia/00 Índice - POO e IA]] y la explicación completa en [[Programación orientada a objetos aplicada a Machine Learning]].
- **Hacia los datos tabulares:** Las estructuras de Python se convierten después en arrays, tablas y archivos en [[numpy pandas parquet arrow]].
- **Hacia el entrenamiento:** `loss_history`, métricas y features alimentan el flujo de [[funcion de perdida]].
