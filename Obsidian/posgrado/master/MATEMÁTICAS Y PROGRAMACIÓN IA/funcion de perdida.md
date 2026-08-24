**Apunte del Módulo.** Guía fundamental sobre cómo evalúa un modelo su propio rendimiento (**Función de Pérdida**) y cómo preparamos la información del mundo real para que el algoritmo pueda aprenderla (**Feature Engineering**).

![[Pasted image 20260819184023.png]]

> [!abstract] La idea central en dos líneas
> - **Feature Engineering:** Es traducir y estructurar la realidad en números informativos para que el modelo pueda *ver* el problema.
> - **Función de Pérdida (Loss Function):** Es la brújula matemática que le dice al modelo qué tan lejos está de la respuesta correcta para que pueda *corregirse*.

## Conexiones con el resto del posgrado

- **Datos de entrada:** [[Estructuras de Python en un experimento de IA]] explica cómo elegir `list`, `tuple` y `dict`, proteger invariantes y conservar historiales de pérdida.
- **Transformación de datos:** [[numpy pandas parquet arrow]] muestra cómo llevar mediciones a matrices, tablas, esquemas y archivos preservando su significado.
- **Modelo y grafo:** [[Programación orientada a objetos aplicada a Machine Learning]] y [[poo ia/06 Grafo computacional y neurona]] construyen la neurona `Scalar`, el grafo y el puente hacia *backpropagation*.
- **Entorno:** [[UV]] permite ejecutar y reproducir los experimentos con sus dependencias.

---

# PARTE 1 — Función de Pérdida (*Loss Function*)

## 1. ¿Qué es intuitivamente?

Imagina que estás aprendiendo a tirar al blanco con un arco y flechas con los ojos vendados:
1. Disparas una flecha.
2. Un entrenador te dice: *"Te quedaste corto por 30 centímetros a la izquierda"*.
3. En el siguiente tiro, ajustas tu postura, fuerza y ángulo.

En Machine Learning:
- **Tu tiro** = la predicción del modelo ($\hat{y}$).
- **El centro de la diana** = el valor real u objetivo ($y$).
- **El entrenador que mide la distancia del fallo** = la **función de pérdida** ($\mathcal{L}$).
- **El ajuste de tus brazos** = la optimización de los pesos ($W$) mediante descenso de gradiente.

> [!important] Definición
> La **función de pérdida** es una función matemática que toma la predicción del modelo y la etiqueta real, y devuelve un **único número escalar** que cuantifica el error o penalización.
> 
> $$\text{Loss} = \mathcal{L}(y, \hat{y})$$
> 
> **Objetivo del entrenamiento:** Encontrar los parámetros (pesos $W$ y sesgos $b$) que hagan que este número sea lo más cercano a **0** posible.

---

## 2. Diferencia clave: *Loss* vs *Cost* vs *Metric*

Es muy común confundir estos tres términos en la literatura:

| Concepto | Término en inglés | ¿Qué evalúa? | Ejemplo |
| :--- | :--- | :--- | :--- |
| **Función de Pérdida** | *Loss Function* | El error en **un solo ejemplo** o muestra individual. | $\mathcal{L}(y^{(i)}, \hat{y}^{(i)}) = (y^{(i)} - \hat{y}^{(i)})^2$ |
| **Función de Costo** | *Cost Function* | El error promedio sobre **todo el dataset** o un lote (*mini-batch*). | $J(W, b) = \frac{1}{N} \sum_{i=1}^N \mathcal{L}(y^{(i)}, \hat{y}^{(i)})$ |
| **Métrica de Evaluación** | *Metric* | Medida pensada para que los **humanos** entiendan el negocio o desempeño. No necesariamente es diferenciable. | Exactitud (*Accuracy*), Precisión, F1-Score, ROC-AUC. |

> [!tip] ¿Por qué no usamos *Accuracy* directamente como función de pérdida?
> Para que los algoritmos de optimización (como el descenso de gradiente) puedan ajustar los pesos, necesitan calcular **derivadas** (gradientes). El *Accuracy* da saltos discretos (ej. 80%, 81%) y su derivada es cero casi siempre. La función de pérdida debe ser continua y diferenciable.

---

## 3. El ciclo de entrenamiento con la función de pérdida

```
[ Datos de entrada X ]
         │
         ▼
 ┌───────────────┐
 │ Modelo (Red / │ ───► Predicciones (ŷ)
 │   Regresión)  │              │
 └───────────────┘              │
         ▲                      ▼
         │             ┌─────────────────┐
         │             │ Función Loss    │ ◄─── Valores reales (y)
         │             │  L(y, ŷ)        │
         │             └─────────────────┘
         │                      │
 ┌───────────────┐              ▼
 │ Actualización │       Cálculo del error
 │ de pesos (W)  │ ◄───  y Gradientes (∂L/∂W)
 └───────────────┘       (Backpropagation)
```

1. **Paso hacia adelante (*Forward Pass*):** El modelo recibe $X$ y calcula una predicción $\hat{y}$.
2. **Cálculo del error:** La función de pérdida compara $\hat{y}$ con el valor real $y$ y produce un escalar (ej. `0.82`).
3. **Paso hacia atrás (*Backward Pass / Backprop*):** Calculamos la derivada de la pérdida respecto a cada peso del modelo ($\frac{\partial \mathcal{L}}{\partial W}$).
4. **Optimización:** Actualizamos los pesos en dirección contraria al gradiente:
   $$W_{\text{nuevo}} = W_{\text{viejo}} - \alpha \cdot \frac{\partial \mathcal{L}}{\partial W}$$
   *(donde $\alpha$ es la tasa de aprendizaje o learning rate)*.

---

## 4. Principales Funciones de Pérdida

La elección de la función de pérdida depende directamente de la **naturaleza de la variable a predecir**.

### A. Problemas de Regresión (predecir valores numéricos continuos)

Ejemplos: Predecir el precio de una casa, la temperatura de mañana, el salario de un empleado.

#### 1. Error Cuadrático Medio — *MSE (Mean Squared Error)* / Pérdida L2
Eleva al cuadrado la diferencia entre lo real y lo predicho.

$$\text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2$$

- **Ventaja:** Muy sensible a errores grandes (los penaliza fuertemente al elevarlos al cuadrado). Matemáticamente es muy fácil de derivar.
- **Desventaja:** Si tienes *outliers* (valores atípicos corruptos), el modelo se distorsionará tratando de corregir ese único error gigante.

#### 2. Error Absoluto Medio — *MAE (Mean Absolute Error)* / Pérdida L1
Toma el valor absoluto de la diferencia.

$$\text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i|$$

- **Ventaja:** **Robusta frente a outliers**. Un valor atípico no domina el entrenamiento.
- **Desventaja:** Su derivada no es continua en el punto $0$ (la esquina del valor absoluto), lo que puede hacer que oscile cerca del mínimo óptimo.

#### 3. *Huber Loss* (El puente ideal)
Combina lo mejor de MSE y MAE: se comporta como MSE cuando el error es pequeño (convergencia suave) y como MAE cuando el error es grande (tolerante a outliers).

---

### B. Problemas de Clasificación (predecir categorías o probabilidades)

Ejemplos: Diagnóstico médico (enfermo / sano), detección de spam, reconocimiento de dígitos (0 al 9).

#### 1. Entropía Cruzada Binaria — *Binary Cross-Entropy (BCE)* / *Log Loss*
Se usa cuando hay **2 clases** ($y \in \{0, 1\}$) y el modelo entrega una probabilidad $\hat{y} \in [0, 1]$ (normalmente tras una función sigmoide).

$$\mathcal{L}(y, \hat{y}) = - \left[ y \cdot \log(\hat{y}) + (1 - y) \cdot \log(1 - \hat{y}) \right]$$

**¿Cómo funciona la intuición matemática?**
- Si la clase real es **$y = 1$**: la fórmula se reduce a $-\log(\hat{y})$.
  - Si el modelo predice $\hat{y} = 0.99 \rightarrow -\log(0.99) \approx 0.01$ (pérdida casi nula).
  - Si el modelo predice $\hat{y} = 0.01 \rightarrow -\log(0.01) \approx 4.60$ (penalización severa).
- Si la clase real es **$y = 0$**: la fórmula se reduce a $-\log(1 - \hat{y})$.

> [!note] Por qué se usa el logaritmo
> El logaritmo castiga **exponencialmente** los errores donde el modelo está "muy seguro pero equivocado" (por ejemplo, predecir con 99% de seguridad que una transacción es legítima cuando era fraude).

#### 2. Entropía Cruzada Categórica — *Categorical Cross-Entropy (CCE)*
Se usa para **$K$ clases mutuamente excluyentes** (ej. clasificar imágenes entre perro, gato o pájaro). Se combina típicamente con una capa de activación **Softmax**.

$$\mathcal{L}(y, \hat{y}) = - \sum_{c=1}^K y_c \cdot \log(\hat{y}_c)$$

---

## 5. Implementación práctica en Python

Así es como monitoreamos la evolución del *loss* durante las épocas de entrenamiento (conectando con el ejemplo de la imagen):

```python
import numpy as np

# Datos simulados: 4 muestras
y_real = np.array([1.0, 0.0, 1.0, 1.0])

def binary_cross_entropy(y_true, y_pred, eps=1e-15):
    # eps evita log(0) que daría infinito o NaN
    y_pred = np.clip(y_pred, eps, 1 - eps)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

# Registro histórico de épocas
loss_history = []

# Supongamos 4 épocas donde el modelo va mejorando sus predicciones
predicciones_por_epoca = [
    np.array([0.60, 0.40, 0.55, 0.50]), # Época 1 (pésima)
    np.array([0.75, 0.30, 0.70, 0.65]), # Época 2 (mejor)
    np.array([0.90, 0.15, 0.85, 0.88]), # Época 3 (buena)
    np.array([0.96, 0.05, 0.94, 0.95]), # Época 4 (excelente)
]

for epoca, y_pred in enumerate(predicciones_por_epoca, start=1):
    loss_actual = binary_cross_entropy(y_real, y_pred)
    loss_history.append(loss_actual)
    print(f"Época {epoca} -> Loss: {loss_actual:.4f}")

print("\nHistorial completo:", [round(x, 4) for x in loss_history])
print(f"Mejor loss alcanzado: {min(loss_history):.4f}")
```

---

# PARTE 2 — Feature Engineering (Ingeniería de Características)

## 1. ¿Qué es y por qué existe?

> *"Caracterizar a los problemas: observar el problema y caracterizarlo (identificar variables)."*

El adagio más famoso en inteligencia artificial es:
$$\textbf{Garbage In} \longrightarrow \textbf{Garbage Out}$$

Un algoritmo de Machine Learning no tiene sentido común, no comprende el contexto del mundo real ni sabe qué es una "casa", un "cliente" o una "enfermedad". El modelo solo ve una **matriz numérica $X$** y calcula operaciones algebraicas sobre ella.

> [!important] ¿Qué es Feature Engineering?
> Es el proceso de **transformar datos crudos** (*raw data*) en **variables numéricas estructuradas** (*features*) que representen de forma explícita los patrones relevantes del dominio para que el modelo pueda aprender eficientemente.
> 
> - **Los datos crudos** son lo que recoges: fechas como `"2026-08-19"`, texto libre `"Excelente servicio pero llegó tarde"`, precios en texto `"$1,200.50"`, IDs de cliente `48912`.
> - **Las *features*** son las variables diseñadas para aportar señal predictiva al modelo.

---

## 2. Los 6 Pasos Fundamentales del Feature Engineering

```
┌─────────────────────────────────────────────────────────────┐
│ 1. Identificación y Formulación del Problema               │
│    (Definir qué queremos predecir y qué variables importan) │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. Limpieza e Imputación                                    │
│    (Manejo de nulos NaN, corrección de tipos, outliers)     │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. Codificación de Variables Categóricas (Encoding)         │
│    (Convertir texto / categorías en representaciones num.)  │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. Creación y Extracción de Variables (Feature Creation)    │
│    (Ratios, descomposición temporal, agregaciones, text)    │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. Escalado y Normalización (Scaling)                       │
│    (Llevar variables a rangos numéricos homogéneos)         │
└──────────────────────────────┬──────────────────────────────┘
                               ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. Selección de Variables (Feature Selection)               │
│    (Eliminar redundancias, ruido y multicolinealidad)       │
└─────────────────────────────────────────────────────────────┘
```

---

### Paso 1: Identificación y caracterización del problema

Antes de escribir código, observamos el fenómeno:
- ¿Qué información define el resultado?
- **Ejemplo (Predecir si un cliente cancelará su suscripción - *Churn*):**
  - No basta con guardar su `ID_Cliente` o su `Nombre`.
  - Lo que de verdad explica la cancelación es: *¿Cuántos días lleva sin iniciar sesión?*, *¿Cuántas quejas puso a soporte?*, *¿Bajó su uso en el último mes?*.

---

### Paso 2: Tratamiento de Valores Faltantes (*Missing Values*) y Atípicos (*Outliers*)

Los modelos matemáticos no aceptan valores vacíos (`NaN` / `None`).

1. **Estrategias para valores faltantes:**
   - **Imputación por estadística:** Rellenar con la media (para distribuciones simétricas) o la mediana (para distribuciones con sesgo).
   - **Imputación por modelo / vecinos:** Usar KNN Imputer para estimar el valor basándose en filas similares.
   - **Indicador de ausencia (*Missing Indicator*):** Crear una columna booleana auxiliar `fue_nulo = 1/0`. A veces, el hecho de que el dato falte es una señal predictiva en sí misma (ej. si no declaró ingresos, podría tener mayor riesgo crediticio).

2. **Estrategias para valores atípicos (*Outliers*):**
   - **Recorte (*Clipping / Winsorization*):** Limitar los valores al percentil 1% y 99%.
   - **Transformación logarítmica:** Aplicar $\log(1 + x)$ para comprimir colas largas en variables con distribuciones muy asimétricas (como salarios o precios inmobiliarios).

---

### Paso 3: Codificación de Variables Categóricas (*Encoding*)

Las computadoras no multiplican palabras como `"Rojo"`, `"Verde"` o `"Azul"`. Debemos convertirlas en números con cuidado:

```
Variable Original: [ "Rojo", "Verde", "Azul" ]

1. Ordinal Encoding (¡Cuidado si no hay orden!):
   Rojo = 0, Verde = 1, Azul = 2
   (El modelo pensará erróneamente que Azul > Rojo)

2. One-Hot Encoding (Recomendado para categorías sin jerarquía):
   ┌─────────┬────────┬──────────┐
   │ es_rojo │ es_verde│ es_azul │
   ├─────────┼────────┼──────────┤
   │    1    │   0    │    0     │  <- Rojo
   │    0    │   1    │    0     │  <- Verde
   │    0    │   0    │    1     │  <- Azul
   └─────────┴────────┴──────────┘
```

- **One-Hot Encoding:** Crea una columna binaria por cada categoría única. Ideal cuando la cardinalidad es baja (< 15 categorías).
- **Ordinal Encoding:** Se usa **únicamente** cuando existe un orden natural (ej. `Nivel_Educativo`: Primaria = 1, Secundaria = 2, Maestría = 3, Doctorado = 4).
- **Target Encoding / Frequency Encoding:** Para variables con miles de categorías (ej. código postal, marca de coche).

---

### Paso 4: Creación de Nuevas Variables (*Feature Creation / Extraction*)

Aquí es donde reside la mayor ventaja competitiva en ciencia de datos. Consiste en combinar o descomponer datos para que la relación matemática sea evidente.

| Tipo de dato | Dato crudo | Nuevas *Features* creadas |
| :--- | :--- | :--- |
| **Fechas** | `"2026-08-19 18:45:00"` | `dia_semana (Miércoles)`, `es_fin_de_semana (0)`, `hora (18)`, `es_hora_pico (1)` |
| **Inmobiliario** | `Precio`, `Metros_Totales`, `Num_Habitaciones` | `precio_por_metro_cuadrado = Precio / Metros_Totales`, `metros_por_habitacion = Metros / Num_Habitaciones` |
| **Finanzas** | `Ingreso_Mensual`, `Pago_Deuda` | `ratio_endeudamiento = Pago_Deuda / Ingreso_Mensual` |
| **Texto** | `"El producto llegó roto y muy tarde"` | `longitud_texto`, `conteo_palabras_negativas`, `embeddings_vectoriales` |

---

### Paso 5: Escalado de Variables (*Feature Scaling*)

¿Por qué es obligatorio escalar?
Supongamos que entrenas un modelo con dos variables:
- `Edad`: rango de 18 a 80.
- `Salario`: rango de 10,000 a 2,000,000.

El gradiente del peso asociado a `Salario` será gigantesco comparado con el de `Edad`. La función de pérdida formará un "valle estrecho y alargado", haciendo que el descenso de gradiente oscile de forma inestable y tarde muchísimo en converger.

```
       SIN ESCALAR                         ESCALADO
(Superficie alargada / lenta)      (Superficie esférica / rápida)

      Salario                            Salario
        │                                   │    /---\
        │   /-------------------\           │   |     |
        │  (                     )          │    \---/
        │   \-------------------/           └───────────── Edad
        └──────────────────── Edad          Convergencia directa
      Oscilaciones bruscas                   al mínimo global
```

1. **Estandarización (*Z-Score / StandardScaler*):**
   $$z = \frac{x - \mu}{\sigma}$$
   Transforma los datos para que tengan **media = 0** y **desviación estándar = 1**. Es el método estándar para la mayoría de algoritmos basados en gradiente y redes neuronales.

2. **Normalización (*Min-Max Scaler*):**
   $$x_{\text{norm}} = \frac{x - x_{\text{min}}}{x_{\text{max}} - x_{\text{min}}}$$
   Comprime todos los valores en el intervalo cerrado $[0, 1]$.

---

### Paso 6: Selección de Variables (*Feature Selection*)

Tener demasiadas variables no siempre es bueno (*La Maldición de la Dimensionalidad*). Las variables innecesarias introducen ruido y provocan sobreajuste (*overfitting*).

- **Eliminar varianza cero / casi nula:** Columnas donde el 99.9% de las filas tienen el mismo valor.
- **Eliminar correlaciones redundantes:** Si `metros_cuadrados` y `pies_cuadrados` tienen correlación 1.0, eliminamos una.
- **Regularización L1 (Lasso):** Métodos que fuerzan a cero los coeficientes de las variables inútiles durante la optimización.

---

## 3. Machine Learning Clásico vs Deep Learning

| Aspecto | Machine Learning Clásico (XGBoost, SVM, Regresión) | Deep Learning (Redes Neuronales, LLMs) |
| :--- | :--- | :--- |
| **Rol del Feature Engineering** | **Crítico y manual.** El 80% del éxito depende de la creatividad humana al crear features. | **Parcialmente automatizado.** La red aprende representaciones jerárquicas en capas ocultas (*Representation Learning*). |
| **Datos no estructurados (Imágenes, Audio, Texto)** | Requiere extractores manuales complejos (SIFT, HOG, TF-IDF). | La red procesa píxeles o tokens directamente y extrae patrones automáticamente. |
| **Datos tabulares (Tablas SQL, Excel)** | El Feature Engineering manual sigue siendo el rey y suele superar a Deep Learning. | Sigue requiriendo limpieza, normalización y buen diseño de entradas. |

---

## 4. Ejemplo práctico completo con Pandas y Scikit-Learn

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# 1. Datos crudos observados
data = pd.DataFrame({
    "edad": [25, 45, np.nan, 35, 52],
    "salario": [30000, 85000, 50000, 62000, 120000],
    "deuda": [5000, 12000, 25000, 8000, 15000],
    "nivel_educativo": ["Licenciatura", "Maestría", "Licenciatura", "Doctorado", "Maestría"],
    "ciudad": ["Bogotá", "Madrid", "Madrid", "Lima", "Bogotá"]
})

print("=== DATOS CRUDOS ===")
print(data)

# 2. Feature Creation (Ingeniería de nuevas variables basadas en el dominio)
# Ratio deuda / salario: indicador clave de salud financiera
data["ratio_endeudamiento"] = data["deuda"] / data["salario"]

# 3. Definir transformaciones por tipo de variable
numeric_features = ["edad", "salario", "deuda", "ratio_endeudamiento"]
categorical_features = ["nivel_educativo", "ciudad"]

numeric_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")), # Tratamiento de NaNs
    ("scaler", StandardScaler())                  # Escalado Z-Score
])

categorical_transformer = Pipeline(steps=[
    ("encoder", OneHotEncoder(drop="first", sparse_output=False)) # One-Hot Encoding
])

# 4. Pipeline unificado de Preprocesamiento
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features)
    ]
)

# 5. Matriz final lista para alimentar al modelo y calcular la Función de Pérdida
X_procesado = preprocessor.fit_transform(data)
print("\n=== MATRIZ NUMÉRICA LISTA PARA EL MODELO (X) ===")
print(np.round(X_procesado, 2))
```

---

# Resumen: ¿Cómo se conectan ambos mundos?

```
┌─────────────────────────────────────────────────────────────┐
│                    MUNDO REAL (DATOS CRUDOS)                │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 FEATURE ENGINEERING                         │
│  "Prepara el terreno de juego y los ojos del modelo"       │
│  Transforma datos brutos en una representación numérica $X$  │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 MODELO PREDICTIVO                           │
│  Calcula $\hat{y} = f(X; W, b)$                             │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│                 FUNCIÓN DE PÉRDIDA                          │
│  "La brújula y juez del entrenamiento"                      │
│  Compara $\hat{y}$ con $y$, mide el error $\mathcal{L}$     │
│  y guía el ajuste de pesos $W$ mediante gradientes.         │
└─────────────────────────────────────────────────────────────┘
```

- **Sin Feature Engineering:** El modelo recibe ruido o representaciones incoherentes, por lo que la función de pérdida jamás podrá llegar a un valor bajo de error.
- **Sin Función de Pérdida:** El modelo tendría datos impecables, pero no sabría hacia dónde ajustar sus pesos ni cómo medir si está mejorando o empeorando.
