Nuestro objetivo principal en Machine Learning es obtener una mayor precisión y una menor tasa de error en las predicciones.
El método Hold-Out significa reservar o apartar un subconjunto de datos en particular. Básicamente, evaluamos el rendimiento de nuestro modelo utilizando este conjunto de datos que no fue visto durante el entrenamiento.

Lo que hace este método de reserva es dividir aleatoriamente nuestro dataset en dos conjuntos separados:
1. **Data de entrenamiento:** Se utiliza para construir el modelo y encontrar los parámetros o valores de corte adecuados.
2. **Data de testeo (prueba):** Se utiliza exclusivamente para evaluar el modelo ya entrenado, permitiendo calcular la precisión, la especificidad, entre otras métricas.

> [!info] Explicación
> **Método Hold Out:**
> Es la forma más simple de validación. Consiste en dividir el dataset original en dos (por ejemplo, 80% para entrenar y 20% para probar). 
> - **Ventaja:** Es muy rápido de ejecutar porque el modelo se entrena una sola vez.
> - **Desventaja:** La evaluación del modelo puede variar mucho dependiendo de qué ejemplos caigan en el conjunto de prueba (alta varianza en la estimación del error). Si por azar el conjunto de prueba contiene ejemplos muy fáciles o muy difíciles, las métricas no serán representativas del verdadero rendimiento del modelo. Para solucionar esto se suele usar la *Validación Cruzada (Cross-Validation)*.

## Notas relacionadas
- [[resampling methods]]
- [[Validacion Cruzada]]
- [[Ajuste de modelos]]
- [[metricas para clasificadores]]
