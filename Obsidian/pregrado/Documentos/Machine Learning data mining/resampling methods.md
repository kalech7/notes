Los métodos de remuestreo (*Resampling Methods*) buscan evaluar si un modelo será capaz de reproducir su nivel de desempeño cuando se enfrente a nuevos datos aleatorios que nunca ha visto.

1. **Método Hold Out**
No es el método más eficiente estadísticamente. Consiste en dividir de forma aleatoria el conjunto total de datos en dos partes (basado en un porcentaje de partición o *split*): un dataset de entrenamiento (*training*) y un dataset de prueba (*testing*).
El dataset de entrenamiento es utilizado por el algoritmo de Machine Learning para ajustar y construir el modelo.
Las filas asignadas a cada dataset son seleccionadas de forma aleatoria, respetando la proporción previamente establecida (por ejemplo, 80/20). El objetivo de esta aleatoriedad es minimizar el sesgo al medir el desempeño del modelo.

2. **Validación Cruzada (Cross-Validation)**
Es una técnica más avanzada que realiza múltiples divisiones de los datos para garantizar una evaluación más robusta y menos dependiente del azar.

> [!info] Explicación
> **¿Por qué usar métodos de remuestreo?**
> Son herramientas fundamentales porque nos permiten calcular el "error de generalización". Si evaluamos un modelo con los mismos datos que usó para entrenarse, creeremos que su rendimiento es casi perfecto (provocando *overfitting* sin darnos cuenta). Al separar o remuestrear los datos, simulamos el entorno del mundo real donde el modelo hará predicciones sobre información nueva.
> - *Hold-Out* es rápido computacionalmente pero su evaluación puede tener una alta varianza estadística.
> - *K-Fold Cross-Validation* requiere más poder de cómputo, pero ofrece una estimación del rendimiento futuro que es mucho más estable y realista.

## Notas relacionadas
- [[metodo hold out]]
- [[Validacion Cruzada]]
- [[test harness]]
- [[Ajuste de modelos]]
