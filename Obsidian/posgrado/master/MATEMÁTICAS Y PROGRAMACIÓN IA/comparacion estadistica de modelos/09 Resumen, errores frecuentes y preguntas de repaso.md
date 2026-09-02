---
title: Resumen, errores frecuentes y preguntas de repaso
aliases:
  - Repaso del módulo 06
tags:
  - posgrado
  - estadistica
  - repaso
  - comparacion-de-modelos
related: "[[00 Índice - Comparación estadística de modelos]]"
---

# Resumen, errores frecuentes y preguntas de repaso

Anterior: [[08 Cómo redactar una conclusión defendible]] · Volver al [[00 Índice - Comparación estadística de modelos|índice]] · Aplicación final: [[10 Experimento real - Regresión Logística vs Random Forest en Iris]]

## 1. El módulo en una sola cadena

```mermaid
flowchart LR
    A[Pregunta] --> B[Unidad]
    B --> C[Métrica y resta]
    C --> D[Pares y dependencia]
    D --> E[Estimando]
    E --> F[Efecto observado]
    F --> G[Precisión]
    G --> H[Referencia nula]
    H --> I[Conclusión limitada]
```

### Explicación

La cadena comienza con el significado del experimento y termina con una conclusión. No puede invertirse comenzando por el $p$-value, porque el número solo adquiere significado después de fijar el contrato.

## 2. Formulario razonado

### Diferencia por unidad

$$
d_i=\operatorname{loss}_A(i)-\operatorname{loss}_B(i).
$$

Sirve para conservar la identidad del caso. Positivo favorece a B porque menor pérdida es mejor.

### Estimando

$$
\Delta=\mathbb E[D].
$$

Es el promedio poblacional que queremos conocer. Debe acompañarse de unidad, métrica, resta y población.

### Estimación

$$
\widehat\Delta=\bar d=\frac1n\sum_{i=1}^n d_i.
$$

Resume el efecto observado en esta muestra.

### Desviación estándar

$$
s_d=\sqrt{\frac{1}{n-1}\sum_{i=1}^n(d_i-\bar d)^2}.
$$

Mide heterogeneidad entre las diferencias individuales.

### Error estándar

$$
\operatorname{SE}(\bar d)=\frac{s_d}{\sqrt n}.
$$

Mide precisión de la media bajo el modelo de muestreo.

### Estadístico $t$

$$
T=\frac{\bar d-0}{s_d/\sqrt n}.
$$

Expresa la distancia desde cero en unidades de error estándar.

### Intervalo $t$

$$
\bar d\pm t_{0.975,n-1}\operatorname{SE}(\bar d).
$$

Cuantifica valores compatibles y precisión bajo el procedimiento.

### Shapiro-Wilk

$$
H_{0,SW}: D \text{ tiene forma normal}.
$$

Diagnostica la forma de las **diferencias**. Un $p$ pequeño aporta evidencia contra normalidad; un $p$ grande no la demuestra. No comprueba independencia ni compara directamente los modelos.

### Cambios de signo

$$
d_i^{(b)}=s_i^{(b)}|d_i|,
\quad
s_i^{(b)}\in\{-1,+1\}.
$$

Construye una referencia nula discreta cuando la invariancia de signos es defendible.

### *Split* de validación cruzada con $k$ *folds*

Para el experimento de clasificación se usa la variante estratificada de $k$-*fold*. Con $k=5$, cada observación de `X_train` aparece una vez en validación y cuatro veces en entrenamiento:

```python
from sklearn.model_selection import StratifiedKFold

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
splits = list(cv.split(X_train, y_train))

assert len(splits) == 5
assert sorted(
    indice
    for _, indices_validacion in splits
    for indice in indices_validacion
) == list(range(len(X_train)))
```

`StratifiedKFold` conserva aproximadamente la proporción de clases; `KFold` es la versión no estratificada. El ajuste de los modelos debe hacerse de nuevo dentro de cada partición y nunca con el *fold* de validación. La implementación completa está en [[10 Experimento real - Regresión Logística vs Random Forest en Iris#11. Validación cruzada: cinco filas no son cinco estudios|el experimento de Iris]].

## 3. Resultados del caso conductor

| Cantidad | Resultado | Lectura |
| --- | ---: | --- |
| $n$ | 10 | casos pareados |
| Positivas / negativas / cero | 7 / 2 / 1 | ventaja no uniforme |
| $\bar d$ | 0.019 | favorece a B |
| $s_d$ | 0.0260128 | dispersión entre casos |
| $\operatorname{SE}(\bar d)$ | 0.0082260 | precisión de la media |
| $t(9)$ | 2.3097566 | distancia estandarizada |
| $p_t$ bilateral | 0.0462549 | extremidad bajo referencia $t$ |
| $IC_{95\%}$ | $[0.0004,0.0376]$ | efectos compatibles bajo el procedimiento |
| Shapiro-Wilk | $W=0.9752$, $p=0.9347$ | no se detecta desviación; $n=10$ no permite demostrar normalidad |
| $p_{\text{signos}}$ | 0.0664063 | extremidad bajo invariancia de signos |

## 4. Errores frecuentes

### «Dos promedios bastan»

Ocultan identidad, dispersión, concentración y fuente de variabilidad. Corrige conservando las diferencias por unidad.

### «Misma fila significa mismo par»

La posición no crea identidad. Corrige verificando IDs y procedencia.

### «Pareado significa independiente»

El par se define dentro de unidad; la independencia se evalúa entre diferencias. Corrige auditando clústeres, sujetos, datasets y solapamiento.

### «El error estándar describe los casos»

Describe la precisión de la media. La dispersión entre casos corresponde a $s_d$.

### «$p=0.046$ significa 4.6 % de probabilidad de $H_0$»

Invierte el condicional. Corrige comenzando la interpretación con «Bajo $H_0$, el diseño y los supuestos...».

### «$p<0.05$ demuestra que B es mejor»

Un umbral clasifica extremidad bajo un contrato; no decide relevancia práctica ni generalización.

### «$p>0.05$ demuestra igualdad»

No rechazar una diferencia no demuestra equivalencia. Hace falta margen y prueba formal.

### «Shapiro-Wilk con $p>0.05$ demuestra normalidad»

No rechazar su nulidad solo indica falta de evidencia detectable contra la forma normal. Con muestras pequeñas puede haber poca potencia. Corrige combinando Q-Q, asimetría, media-mediana, influencia y procedencia.

### «Si Shapiro-Wilk da $p<0.05$, el software debe cambiar a una prueba no paramétrica»

No existe ese selector automático. Wilcoxon, cambios de signo, permutación y *bootstrap* tienen contratos propios. Corrige fijando estimando, diseño y referencia antes de elegir una función.

### «Exacto significa sin supuestos»

La enumeración no tiene error Monte Carlo, pero requiere una nulidad que autorice cambios de signo.

### «Cinco folds son cinco estudios»

Reutilizan el dataset y solapan entrenamiento. Corrige preservando la estructura o reformulando la inferencia.

### «Puedo probar varios métodos y reportar el menor p»

Eso introduce selección y multiplicidad. Corrige preespecificando el análisis primario y registrando todos los análisis.

## 5. Preguntas conceptuales

1. ¿Por qué $d_i=A_i-B_i>0$ favorece a B en este módulo?
2. ¿Qué diferencia hay entre $\Delta$ y $\bar d$?
3. ¿Qué información se pierde al guardar solo la media de A y la media de B?
4. ¿Por qué se modelan las diferencias y no las pérdidas por separado en una prueba pareada?
5. ¿Qué significa $t(9)=2.31$?
6. ¿Qué probabilidad expresa $p=0.0463$?
7. ¿Por qué el intervalo y la prueba $t$ no son confirmaciones independientes?
8. ¿Qué condición adicional necesita la prueba de cambios de signo?
9. ¿Por qué $p_t$ y $p_{\text{signos}}$ pueden caer a lados distintos de $0.05$?
10. ¿Por qué cinco folds del mismo dataset no equivalen a cinco datasets?
11. ¿Sobre qué vector se calcula Shapiro-Wilk en una prueba pareada?
12. ¿Por qué $p_{SW}>0.05$ no demuestra normalidad ni independencia?

> [!success]- Respuestas
> 1. Porque la métrica es una pérdida: $A_i>B_i$ significa que B perdió menos.
> 2. $\Delta$ es el promedio poblacional desconocido; $\bar d$ es su estimación muestral.
> 3. Dirección por caso, dispersión, atípicos, empates y correspondencia.
> 4. Porque la resta conserva la identidad y elimina parte de la variación compartida dentro del par.
> 5. Que la media observada está a 2.31 errores estándar de cero bajo la escala del estadístico.
> 6. La probabilidad, bajo $H_0$, diseño y supuestos, de un $|T|$ al menos tan extremo.
> 7. Porque usan la misma media, desviación, tamaño muestral y referencia $t$.
> 8. Invariancia conjunta ante las inversiones de signo permitidas.
> 9. Porque usan nulidades y distribuciones de referencia distintas.
> 10. Porque reutilizan el mismo dataset y sus entrenamientos se solapan.
> 11. Sobre las diferencias $d_i=A_i-B_i$, no sobre A y B por separado.
> 12. Porque no rechazar puede deberse a poca potencia y porque Shapiro-Wilk analiza forma, no la dependencia producida por el diseño.

## 6. Ejercicios numéricos

### Ejercicio 1

Si se redefine $d_i=\operatorname{loss}_B(i)-\operatorname{loss}_A(i)$, ¿qué cambia?

> [!success]- Solución
> Cambian los signos de todos los $d_i$, de $\bar d$ y de $T$. El $p$-value bilateral y el ancho del intervalo permanecen iguales; los extremos del intervalo cambian de signo y orden. Ahora un valor negativo favorece a B.

### Ejercicio 2

Dos muestras tienen media $0.019$, pero una tiene $s_d=0.01$ y otra $s_d=0.05$, ambas con $n=10$. ¿Cuál estima con mayor precisión?

> [!success]- Solución
> La primera. Sus errores estándar son aproximadamente $0.00316$ y $0.01581$, respectivamente. La media es la misma, pero la incertidumbre es diferente.

### Ejercicio 3

Si se duplican literalmente las diez filas y se ejecuta una prueba como si hubiera $n=20$, ¿se duplicó la información?

> [!success]- Solución
> No. Se duplicaron registros, no unidades independientes. El error estándar ingenuo disminuiría artificialmente.

### Ejercicio 4

¿Se puede elegir la prueba de cambios de signo porque su nombre dice «exacta»?

> [!success]- Solución
> No. La exhaustividad del cálculo no demuestra que la inversión de signos sea válida para el diseño.

## 7. Ruta de repaso según la duda

| Si dudas sobre... | Revisa |
| --- | --- |
| Vocabulario estadístico | [[01 Conceptos para recordar antes de comparar modelos]] |
| Qué es un par válido | [[02 Diseño pareado, diferencias e independencia]] |
| Media, desviación y error estándar | [[03 Efecto observado, estimando y precisión]] |
| Prueba $t$, $p$ e intervalo | [[04 Prueba t pareada, p-value e intervalo de confianza]] |
| Normalidad, Shapiro-Wilk y Q-Q | [[04A Diagnóstico de normalidad con Shapiro-Wilk]] |
| Enumeración exacta | [[05 Prueba exacta por cambios de signo]] |
| *Split* con $k$ *folds* y unidad de análisis | [[06 Unidad de análisis, dependencia y validación cruzada]] y [[10 Experimento real - Regresión Logística vs Random Forest en Iris#11. Validación cruzada: cinco filas no son cinco estudios|código completo]] |
| Código de SciPy y NumPy | [[07 Implementación reproducible en Python]] |
| Experimento real, gráficos y Python explicado | [[10 Experimento real - Regresión Logística vs Random Forest en Iris]] |
| Escritura del resultado | [[08 Cómo redactar una conclusión defendible]] |

## 8. Frase final del módulo

> [!important]
> La dirección observada favorece a B en estas unidades; la magnitud es $0.019$ puntos de *log-loss*. La fuerza de evidencia depende de la referencia nula y sus supuestos, y el alcance depende de la unidad y del proceso de muestreo.

Anterior: [[08 Cómo redactar una conclusión defendible]] · Volver al [[00 Índice - Comparación estadística de modelos|índice]] · Aplicación final: [[10 Experimento real - Regresión Logística vs Random Forest en Iris]].
