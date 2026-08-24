---
title: "M03 — NumPy, Pandas, Arrow y Parquet: de una medición a un archivo"
aliases:
  - "Módulo 03 — Del array al archivo columnar"
  - "Misión lunar: soporte vital"
tags:
  - posgrado
  - matemáticas
  - python
  - machine-learning
  - datos
---

# M03 — De una medición a un archivo: NumPy, Pandas, Arrow y Parquet

## Antes de empezar: ¿qué se está aprendiendo realmente?

Este módulo no trata de memorizar cuatro nombres de librerías. Trata de aprender a **no perder el significado de los datos** cuando los transformamos.

El ejemplo utiliza una base lunar con sensores. En cada instante se registra temperatura, CO₂, oxígeno, presión y vibración en distintos módulos de la base. El escenario sirve para aprender a trabajar con datos; no es un sistema real de soporte vital ni los umbrales mostrados son criterios médicos o de seguridad operativa.

La pregunta que guía toda la clase es esta:

> ¿Cómo pasamos de una colección de números a un archivo eficiente, sin olvidar qué mide cada número, de dónde vino y qué significa?

El recorrido será:

~~~text
mediciones de sensores
        ↓
NumPy: cálculo con números
        ↓
Pandas: tabla con nombres y contexto
        ↓
Arrow: tabla con esquema y tipos explícitos
        ↓
Parquet: archivo columnar para guardar y leer eficientemente
        ↓
validación: comprobar que el significado no se perdió
~~~

> [!abstract] Idea principal
> Los datos no son solamente valores. Una lectura de 620 puede ser CO₂, temperatura, presión o un identificador. El valor solo se vuelve útil cuando conservamos su contexto.

---

## 1. El punto de partida: una medición no es solo una fila de números

Imagina que recibimos esta fila:

~~~text
[21.2, 620, 20.8, 101.2, 0.18]
~~~

Por sí sola no sabemos qué significa. Para interpretarla necesitamos un acuerdo previo:

| Posición | Variable | Unidad | Qué responde |
|---:|---|---|---|
| 0 | temperature_c | grados Celsius | ¿qué temperatura hay? |
| 1 | co2_ppm | partes por millón | ¿cuánto CO₂ hay? |
| 2 | oxygen_pct | porcentaje | ¿qué concentración de oxígeno hay? |
| 3 | pressure_kpa | kilopascales | ¿qué presión hay? |
| 4 | vibration_mm_s | milímetros por segundo | ¿cuánta vibración hay? |

Entonces la fila se puede leer así:

~~~text
temperatura = 21.2 °C
CO₂         = 620 ppm
oxígeno     = 20.8 %
presión     = 101.2 kPa
vibración   = 0.18 mm/s
~~~

Pero todavía falta información. También necesitamos conocer el módulo y el instante:

~~~text
módulo: HAB-1
instante: 2038-07-18 08:00
~~~

Ahora sí tenemos una observación completa:

> En el módulo HAB-1, a las 08:00, se midieron 21.2 °C, 620 ppm de CO₂, 20.8 % de oxígeno, 101.2 kPa y 0.18 mm/s de vibración.

Esta frase es la **unidad de observación** del ejercicio.

> [!important] Regla de oro
> Antes de calcular cualquier cosa, debes poder completar la frase: «una fila representa...». Si no puedes hacerlo, no sabes todavía qué estás analizando.

---

## 2. ¿Por qué no usar una sola estructura para todo?

Cada forma de representar datos tiene fortalezas y límites.

| Herramienta | Qué es | Cuándo usarla | Qué no resuelve por sí sola |
|---|---|---|---|
| NumPy | array numérico multidimensional | cálculos matemáticos rápidos | nombres, fechas e identidad |
| Pandas | tabla de filas y columnas | analizar, filtrar, agrupar y trabajar con fechas | intercambio tipado entre sistemas distintos |
| Arrow | tabla columnar con esquema explícito | mover tablas entre herramientas de forma consistente | no es un archivo de almacenamiento |
| Parquet | formato de archivo columnar | guardar muchos datos y leer solo una parte | no hace análisis por sí mismo |

Podemos pensarlo así:

~~~text
NumPy     = una hoja cuadriculada llena de números
Pandas    = esa hoja con encabezados, fechas y nombres de filas
Arrow     = una versión con un contrato formal de tipos
Parquet   = la caja archivada, comprimida y preparada para consultas futuras
~~~

No se pasa de una herramienta a otra porque una sea mejor que la anterior. Se pasa porque cambia la necesidad.

---

## 3. Primera capa: NumPy y la idea de matriz

### 3.1 ¿Qué es un array?

Un array de NumPy es una colección ordenada de valores del mismo tipo, preparada para cálculos numéricos.

En el notebook se crea una matriz de ocho observaciones y cinco sensores:

~~~python
measurements = np.array(
    [
        [21.2,  620, 20.8, 101.2, 0.18],
        [21.5,  640, 20.7, 101.0, 0.21],
        [22.0,  710, 20.6, 100.9, 0.25],
        [24.8, 1450, 19.4,  99.8, 0.91],
        [20.9,  600, 20.9, 101.3, 0.17],
        [21.1,  610, 20.8, 101.1, 0.20],
        [23.9, 1280, 19.8, 100.2, 0.72],
        [21.4,  650, 20.7, 101.0, 0.19],
    ],
    dtype=np.float64,
)
~~~

La palabra matriz significa que los datos están organizados en filas y columnas:

~~~text
                    sensores
              temp   CO₂  O₂  presión  vibración
observación 0  21.2  620 20.8 101.2     0.18
observación 1  21.5  640 20.7 101.0     0.21
observación 2  22.0  710 20.6 100.9     0.25
...
~~~

En esta etapa NumPy no conoce los nombres temp, CO₂ u oxígeno. Esos nombres viven en una lista aparte:

~~~python
feature_names = [
    'temperature_c',
    'co2_ppm',
    'oxygen_pct',
    'pressure_kpa',
    'vibration_mm_s',
]
~~~

Por eso NumPy es excelente para operar sobre números, pero no es suficiente cuando necesitamos conservar contexto.

### 3.2 Shape: la forma de los datos

La propiedad shape describe cuántos elementos hay en cada eje:

~~~python
measurements.shape
# (8, 5)
~~~

Se lee como:

~~~text
8 filas: 8 observaciones
5 columnas: 5 sensores
~~~

Shape no es un detalle técnico menor. Es una forma compacta de preguntar: «¿la estructura todavía representa lo que creo que representa?».

Si alguien invirtiera la matriz accidentalmente, el shape sería (5, 8). El código podría seguir ejecutándose, pero ahora las filas ya no serían observaciones y las columnas ya no serían sensores.

> [!warning] Una operación puede no producir errores y estar mal
> El programa solo comprueba si las formas son compatibles. No puede saber si tú cambiaste el significado de los ejes.

El notebook usa aserciones:

~~~python
assert measurements.shape == (8, 5)
assert measurements.ndim == 2
assert measurements.dtype == np.float64
~~~

Una aserción expresa una expectativa. Si el dato no cumple el contrato, el programa se detiene antes de continuar con resultados engañosos.

### 3.3 Ejes: la pregunta determina el cálculo

En una matriz, cada dirección es un eje:

~~~text
axis=0: baja por las filas
axis=1: avanza por las columnas
~~~

La parte que más confunde al principio es esta: el eje no es una receta para memorizar; indica **qué dimensión vas a resumir**.

Supongamos que queremos el promedio de cada sensor. Para temperatura queremos promediar las ocho temperaturas; para CO₂ queremos promediar los ocho valores de CO₂; y así sucesivamente.

~~~python
feature_mean = measurements.mean(axis=0)
~~~

Al resumir las filas, queda una respuesta por columna:

~~~text
temperature_c  -> 22.100
co2_ppm        -> 820.000
oxygen_pct     -> 20.462
pressure_kpa   -> 100.813
vibration_mm_s -> 0.354
~~~

La forma del resultado es (5,), porque quedan cinco sensores.

Ahora mira esta instrucción:

~~~python
row_mean = measurements.mean(axis=1)
~~~

Aquí se resumen las columnas. El resultado tiene una media por observación, por lo que la forma es (8,).

¿Es incorrecta? No. ¿Sirve para responder «cuál es el promedio de cada sensor»? Tampoco. Sumar 21.2 °C, 620 ppm, 20.8 %, 101.2 kPa y 0.18 mm/s produce un número, pero mezcla unidades que no se pueden interpretar juntas.

> [!tip] Cómo decidir el eje
> Primero formula la pregunta con palabras. Después pregunta qué dimensión debe desaparecer. Si quieres una respuesta por sensor, desaparecen las observaciones: axis=0.

### 3.4 dtype: el tipo de número importa

dtype indica cómo se guarda e interpreta cada valor.

En el ejercicio se usa float64. Eso permite guardar decimales como 21.2 o 0.18 y realizar cálculos estadísticos.

Veamos otro caso:

~~~python
crew_counts = np.array([4, 5, 6], dtype=np.int32)
half = crew_counts / 2
~~~

La división produce:

~~~text
[2.0, 2.5, 3.0]
~~~

Aunque la entrada era entera, la salida es flotante porque 5 dividido entre 2 es 2.5. NumPy cambia el tipo cuando lo necesita para no perder la parte decimal.

¿Cuándo conviene revisar dtype?

- después de una división;
- al cargar datos desde archivos;
- antes de guardar un dataset;
- si aparecen valores inesperados;
- cuando importa mucho el uso de memoria o la precisión.

### 3.5 Vistas y copias: ¿se modificó el original?

Una variable puede señalar los mismos datos o datos nuevos.

~~~python
window = measurements[:3, :]
~~~

La selección anterior suele ser una **vista**. Una vista no crea una matriz independiente: mira una parte de la misma memoria.

~~~text
measurements ─┐
              ├─ comparte los mismos datos
window ───────┘
~~~

Si se modifica window, puede modificarse measurements.

En cambio:

~~~python
independent_window = measurements[:3, :].copy()
~~~

crea una copia:

~~~text
measurements          independent_window
     │                        │
     └── memoria distinta ────┘
~~~

¿Cuándo usar copy?

- cuando vas a limpiar o corregir un subconjunto;
- cuando quieres ensayar una transformación sin tocar el origen;
- cuando una selección representa una versión independiente del dato;
- cuando no quieres efectos secundarios difíciles de rastrear.

El notebook usa np.shares_memory para verificar este comportamiento.

### 3.6 Strides: cómo NumPy recorre la memoria

Los *strides* indican cuántos **bytes** debe avanzar NumPy en la memoria para llegar al siguiente elemento de cada dimensión del array.

Por ejemplo:

~~~python
arr = np.array([[1, 2, 3],
                [4, 5, 6]], dtype=np.int64)

arr.shape
# (2, 3)

arr.strides
# (24, 8)
~~~

El array tiene 2 filas y 3 columnas. Como cada valor `int64` ocupa 8 bytes:

- `8` significa que para avanzar una columna NumPy salta 8 bytes, es decir, pasa al siguiente número.
- `24` significa que para avanzar una fila NumPy salta 24 bytes, porque una fila contiene 3 valores: `3 × 8 = 24`.

Los *strides* no son los valores del array ni cambian su `shape`. Son instrucciones internas que permiten a NumPy saber cómo están organizados los datos en memoria.

La relación entre estas propiedades es:

~~~text
shape   = cuántos elementos hay en cada dimensión
dtype   = cuánto ocupa cada elemento
strides = cuánto debe avanzar en memoria para recorrer cada dimensión
~~~

Esto ayuda a entender por qué una selección puede ser una vista: una vista puede conservar los mismos datos en memoria, pero usar un `shape` o unos `strides` diferentes. En la mayoría de cálculos cotidianos no necesitas modificar `strides` directamente; basta con conocerlos para entender el rendimiento, las vistas y la disposición de un array.

---

## 4. Cálculo sobre columnas: vectorización, normalización y broadcasting

### 4.1 Vectorización: aplicar una regla a todos los valores

Una transformación vectorizada describe una regla para todo el conjunto, sin escribir manualmente un bucle para cada fila y cada columna.

En el notebook se calcula una media y desviación por sensor:

~~~python
mean = measurements.mean(axis=0)
std = measurements.std(axis=0)
~~~

Después normaliza:

~~~python
normalized = (measurements - mean) / safe_std
~~~

La fórmula es:

~~~text
z = (valor - media de su sensor) / desviación de su sensor
~~~

El resultado ya no conserva las unidades originales. Expresa distancia relativa respecto al comportamiento típico de cada sensor.

Por ejemplo, la fila anómala del ejercicio queda aproximadamente así:

~~~text
[ 1.996, 1.975, -2.065, -2.051, 2.049 ]
~~~

Interpretación:

| Sensor | Lectura relativa |
|---|---|
| temperatura | casi 2 desviaciones por encima de su media |
| CO₂ | casi 2 desviaciones por encima |
| oxígeno | algo más de 2 desviaciones por debajo |
| presión | algo más de 2 desviaciones por debajo |
| vibración | casi 2 desviaciones por encima |

Este patrón no diagnostica un problema real. Lo que hace es mostrar que esa observación es muy distinta del comportamiento medio registrado en el ejemplo.

### 4.2 ¿Por qué hace falta safe_std?

Si todos los valores de una columna fueran iguales, su desviación estándar sería cero. Dividir entre cero no tiene sentido.

~~~python
safe_std = np.where(std == 0, 1.0, std)
~~~

La instrucción significa:

~~~text
si la desviación es 0, usa 1.0;
en caso contrario, usa la desviación calculada.
~~~

Así se evita el error matemático. En un proyecto real también sería importante registrar que el sensor no tuvo variación, porque puede ser un dato relevante.

### 4.3 Broadcasting: cómo una columna se aplica a muchas filas

En la normalización tenemos:

~~~text
measurements: (8, 5)
mean:         (5,)
~~~

El vector mean tiene cinco valores: una media para cada sensor. NumPy entiende que debe aplicar el mismo vector a cada una de las ocho filas.

Eso es broadcasting.

No crea ocho copias reales de mean. NumPy se comporta como si estuvieran presentes para realizar el cálculo.

Ahora queremos un desplazamiento distinto por observación:

~~~python
row_offset = np.linspace(0.0, 0.7, num=8)[:, np.newaxis]
adjusted = measurements - row_offset
~~~

La primera parte crea ocho valores. np.newaxis convierte el vector de forma (8,) en una columna de forma (8, 1):

~~~text
0.0
0.1
0.2
...
0.7
~~~

Entonces cada desplazamiento de fila se aplica a sus cinco sensores:

~~~text
(8, 5) menos (8, 1) da (8, 5)
~~~

> [!tip] Método para no perderse con broadcasting
> Escribe las formas antes de ejecutar. Alinea los números desde la derecha. Una dimensión de tamaño 1 puede repetirse conceptualmente.

---

## 5. Filtrar observaciones: máscaras booleanas

Una máscara es una lista de respuestas verdadero o falso. Permite transformar una pregunta en una selección de filas.

En el ejemplo queremos revisar una observación si:

- CO₂ es mayor que 1000 ppm; o
- vibración es mayor que 0.70 mm/s.

~~~python
co2 = measurements[:, 1]
vibration = measurements[:, 4]

high_co2 = co2 > 1000
high_vibration = vibration > 0.70
needs_review = high_co2 | high_vibration
~~~

La salida es:

~~~text
CO2 alto       : [False False False  True False False  True False]
Vibración alta : [False False False  True False False  True False]
Revisar        : [False False False  True False False  True False]
~~~

La barra vertical significa OR: basta con que se cumpla una de las dos condiciones.

La máscara se usa para conservar solo las filas necesarias:

~~~python
review_rows = measurements[needs_review]
~~~

Así aparecen dos filas: las observaciones 3 y 6.

| Observación | CO₂ | Oxígeno | Vibración |
|---:|---:|---:|---:|
| 3 | 1450 | 19.4 | 0.91 |
| 6 | 1280 | 19.8 | 0.72 |

¿Cuándo se usan máscaras?

- filtrar datos que cumplen una condición;
- detectar valores fuera de un rango;
- separar entrenamiento y prueba;
- identificar filas faltantes;
- crear subconjuntos para análisis.

> [!warning] Los umbrales son reglas del ejemplo
> La condición CO₂ mayor que 1000 o vibración mayor que 0.70 ilustra cómo funciona una máscara. No debe interpretarse como un límite de seguridad real.

---

## 6. Segunda capa: Pandas devuelve identidad a los datos

NumPy es ideal para cálculo, pero el array no sabe qué módulo produjo una fila ni en qué instante ocurrió.

Pandas introduce un DataFrame: una tabla con nombres y tipos de columnas.

~~~python
modules = [
    'HAB-1', 'HAB-1', 'LAB-1', 'LAB-1',
    'POWER-1', 'POWER-1', 'LAB-1', 'HAB-1'
]

timestamps = pd.to_datetime([
    '2038-07-18 08:00',
    '2038-07-18 08:05',
    '2038-07-18 08:00',
    '2038-07-18 08:05',
    '2038-07-18 08:00',
    '2038-07-18 08:05',
    '2038-07-18 08:10',
    '2038-07-18 08:10',
])

df = pd.DataFrame(measurements, columns=feature_names)
df.insert(0, 'module', modules)
df.insert(1, 'timestamp', timestamps)
~~~

Ahora una fila se lee así:

~~~text
módulo + instante + mediciones de sensores
~~~

Pandas permite tener columnas distintas en la misma tabla:

| Columna | Tipo conceptual |
|---|---|
| module | texto |
| timestamp | fecha y hora |
| temperature_c | número decimal |
| co2_ppm | número decimal |
| oxygen_pct | número decimal |
| pressure_kpa | número decimal |
| vibration_mm_s | número decimal |

La utilidad del DataFrame no es solo que se vea bonito. Ahora podemos hacer preguntas con nombres comprensibles.

---

## 7. Cómo seleccionar datos en Pandas

### 7.1 loc: seleccionar por significado

loc se utiliza cuando interesan nombres, etiquetas o condiciones.

~~~python
co2_alerts = df.loc[
    df['co2_ppm'] > 1000,
    ['module', 'timestamp', 'co2_ppm']
]
~~~

Esta instrucción se lee casi como una frase:

> Dame las filas cuyo CO₂ sea mayor que 1000 y, de ellas, muéstrame módulo, instante y CO₂.

El resultado son las dos mediciones de LAB-1 con CO₂ alto.

### 7.2 iloc: seleccionar por posición

iloc se utiliza cuando interesa la ubicación:

~~~python
first_three = df.iloc[:3, :]
~~~

Significa:

> Dame las primeras tres filas y todas las columnas.

- Usa loc cuando importa el significado del nombre.
- Usa iloc cuando importa la posición dentro de la tabla.

### 7.3 Por qué se hace copy antes de añadir una columna

El notebook crea alertas así:

~~~python
alerts = df.loc[
    (df['co2_ppm'] > 1000) | (df['vibration_mm_s'] > 0.70)
].copy()

alerts.loc[:, 'severity'] = 'high'
~~~

Aquí ocurren dos ideas:

1. se seleccionan las filas que requieren revisión;
2. se crea una tabla independiente y se le añade una columna.

La copia es importante porque alerts se convierte en una nueva versión del conjunto: una lista de alertas. Si se modificara una selección sin copiar, podría existir ambigüedad sobre si también se modificó df.

---

## 8. El índice: identidad antes que posición

Pandas al sumar o comparar Series intenta alinear por índice.

~~~python
left = pd.Series([10, 20], index=['HAB-1', 'LAB-1'])
right = pd.Series([1, 2], index=['LAB-1', 'POWER-1'])
result = left + right
~~~

El resultado es:

~~~text
HAB-1       NaN
LAB-1      21.0
POWER-1     NaN
~~~

Pandas no suma 10 con 1 solamente porque ocupan la primera posición. Suma los valores de LAB-1 porque comparten la misma etiqueta.

¿Por qué aparecen valores NaN?

- HAB-1 solo existe en la primera serie;
- POWER-1 solo existe en la segunda;
- LAB-1 existe en ambas.

Este comportamiento protege contra un error frecuente: combinar entidades distintas por accidente.

> [!question] ¿Cuál es la identidad de una lectura?
> En este ejercicio, module por sí solo no siempre basta porque hay varias lecturas del mismo módulo. La identidad más natural es probablemente module más timestamp.

---

## 9. Valores faltantes: desconocido no es cero

Supongamos que el sensor de oxígeno de LAB-1 no reportó a las 08:05.

~~~python
df_missing = df.copy()

df_missing.loc[
    (df_missing['module'] == 'LAB-1')
    & (df_missing['timestamp'] == pd.Timestamp('2038-07-18 08:05')),
    'oxygen_pct'
] = np.nan
~~~

El código localiza una sola celda mediante dos condiciones:

- el módulo debe ser LAB-1;
- el instante debe ser 08:05.

Después se cuentan los nulos:

~~~python
nulls = df_missing.isna().sum()
~~~

Y se crea una bandera:

~~~python
df_missing['oxygen_missing'] = df_missing['oxygen_pct'].isna()
~~~

La bandera vale True justo donde falta oxígeno.

¿Por qué no se reemplaza el nulo por cero?

Porque 0 % de oxígeno sería una lectura numérica real y extrema. Un nulo significa que no conocemos la lectura. Confundir ambas cosas altera la interpretación de los datos.

Opciones posibles ante un nulo:

| Decisión | Cuándo puede tener sentido |
|---|---|
| conservarlo | se quiere separar ausencia de medición y valor real |
| eliminar la fila | el análisis no puede usar observaciones incompletas |
| imputar | existe una regla justificada para estimar el dato |
| usar una bandera | se quiere conservar la fila y registrar la ausencia |

No hay una respuesta universal. Depende de la pregunta, el dominio y las consecuencias de inventar un valor.

---

## 10. Agrupar: cuando una fila deja de ser una medición

Hasta aquí una fila representa una lectura concreta. Ahora queremos un resumen por módulo:

~~~python
summary = (
    df_missing
    .groupby('module', as_index=False)
    .agg(
        observations=('module', 'size'),
        mean_co2_ppm=('co2_ppm', 'mean'),
        max_temperature_c=('temperature_c', 'max'),
        max_vibration_mm_s=('vibration_mm_s', 'max'),
    )
)
~~~

El resultado es:

| module | observaciones | CO₂ medio | temperatura máxima | vibración máxima |
|---|---:|---:|---:|---:|
| HAB-1 | 3 | 636.67 | 21.5 | 0.21 |
| LAB-1 | 3 | 1146.67 | 24.8 | 0.91 |
| POWER-1 | 2 | 605.00 | 21.1 | 0.20 |

La operación groupby hace dos cosas:

1. divide las filas según el valor de module;
2. calcula una función resumen en cada grupo.

La idea que no se debe perder es esta:

~~~text
antes de groupby: una fila representa una medición
después de groupby: una fila representa un módulo
~~~

La granularidad cambió. La tabla resumen es muy útil para comparar módulos, pero ya no permite reconstruir el orden temporal de cada lectura.

---

## 11. Tercera capa: Arrow y el esquema explícito

Pandas es muy cómodo para analizar datos en Python. Pero cuando una tabla necesita viajar entre herramientas, lenguajes o sistemas, conviene declarar su estructura de forma explícita.

Arrow representa una tabla columnar en memoria junto con un esquema.

Un esquema responde:

- ¿cómo se llama cada columna?
- ¿qué tipo tiene?
- ¿qué estructura debe tener la tabla?

Por ejemplo:

~~~text
module          : texto
timestamp       : fecha y hora
temperature_c   : decimal
co2_ppm         : decimal
oxygen_pct      : decimal
oxygen_missing  : booleano
~~~

El notebook convierte Pandas a Arrow:

~~~python
table = pa.Table.from_pandas(df_missing, preserve_index=False)
~~~

La opción preserve_index=False evita convertir el índice técnico de Pandas en una columna adicional. Es importante porque el índice 0, 1, 2, ... no forma parte del contrato de la medición.

> [!tip] Diferencia esencial
> Pandas es una herramienta cómoda para trabajar. Arrow es una forma explícita y estandarizada de describir una tabla tipada en memoria.

---

## 12. Parquet: guardar de forma columnar

Arrow Table todavía vive en memoria. Para conservar los datos en disco se usa Parquet.

~~~python
pq.write_table(table, parquet_path, compression='zstd')
~~~

Parquet no guarda los datos como una lista de filas completas. Los organiza por columnas. Esta diferencia importa cuando las tablas son grandes.

Imagina una tabla con cien columnas, pero un análisis solo necesita module y co2_ppm.

Con un archivo columnar se puede pedir solo esas columnas:

~~~python
partial = pq.read_table(
    parquet_path,
    columns=['module', 'co2_ppm'],
)
~~~

Esto evita leer temperatura, oxígeno, presión y vibración cuando no son necesarias.

| Formato de acceso | Lectura típica |
|---|---|
| orientado a filas | se lee la fila completa aunque uses pocas columnas |
| orientado a columnas | se leen solo las columnas requeridas |

Parquet es útil cuando:

- hay muchas filas;
- hay muchas columnas;
- se hacen análisis por subconjuntos de columnas;
- se quiere compresión;
- se necesita almacenar datasets de forma eficiente.

La compresión zstd reduce el tamaño del archivo. No cambia el significado de los datos.

---

## 13. Round trip: escribir no basta

Guardar un archivo no demuestra que se guardó correctamente.

Por eso el notebook hace un round trip:

~~~text
DataFrame
   ↓
Arrow Table
   ↓
archivo Parquet
   ↓
Arrow Table restaurada
   ↓
comparación
~~~

La lectura es:

~~~python
restored = pq.read_table(parquet_path)
~~~

Y después se comprueban propiedades distintas:

~~~python
assert restored.num_rows == table.num_rows
assert restored.column_names == table.column_names
assert restored.schema == table.schema
assert restored.equals(table)
~~~

Cada comprobación responde una pregunta:

| Comprobación | Pregunta |
|---|---|
| número de filas | ¿se perdió o añadió alguna observación? |
| nombres de columnas | ¿la estructura sigue siendo la misma? |
| esquema | ¿los tipos se conservaron? |
| igualdad | ¿los valores restaurados coinciden? |

Después se validan reglas del problema:

~~~python
assert set(restored_df['module']).issubset(expected_modules)
assert (restored_df['co2_ppm'] >= 0).all()
assert (restored_df['pressure_kpa'] > 0).all()
assert restored_df['oxygen_missing'].dtype == bool
~~~

El esquema puede decir «esta columna es numérica», pero no puede saber que una presión negativa no tiene sentido para el ejemplo. Por eso hacen falta dos tipos de validación:

1. validación estructural: forma, columnas, tipos;
2. validación de dominio: valores permitidos y reglas del contexto.

## 15. Mapa mental final

Cuando tengas dudas, vuelve a esta secuencia:

~~~text
1. ¿Qué representa una fila?
   Una medición de un módulo en un instante.

2. ¿Necesito calcular con números?
   Uso NumPy.

3. ¿Necesito nombres, fechas, filtros o grupos?
   Uso Pandas.

4. ¿Necesito una tabla con tipos y esquema explícitos?
   Uso Arrow.

5. ¿Necesito guardar y leer pocas columnas de un dataset grande?
   Uso Parquet.

6. ¿Cómo sé que no dañé el dato?
   Valido forma, tipos, esquema, valores y reglas del dominio.
~~~

> [!summary] En una frase
> El recorrido NumPy → Pandas → Arrow → Parquet consiste en transformar la misma información para distintos fines, sin perder nunca la respuesta a tres preguntas: qué se midió, de dónde vino y qué representa cada fila.

## Conexiones con otras notas

- [[Estructuras de Python en un experimento de IA]] — identidad, mutabilidad y copias.
- [[Programación orientada a objetos aplicada a Machine Learning]] — objetos, invariantes y composición para representar operaciones.
- [[poo ia/00 Índice - POO e IA]] — ruta separada para estudiar POO, `Scalar` y grafos.
- [[poo ia/04 Buenas prácticas y assert]] — validación de invariantes y estado mutable.
- [[poo ia/06 Grafo computacional y neurona]] — conexión entre una representación numérica y un modelo con historia computacional.
- [[funcion de perdida]] — operaciones numéricas, *feature engineering* y entrenamiento.
- [[UV]] — creación de entornos e instalación de dependencias.
