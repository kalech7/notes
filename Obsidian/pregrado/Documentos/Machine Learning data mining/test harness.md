Un marco de pruebas o "Test Harness" en Machine Learning involucra tres elementos principales:
1. El **método de remuestreo** (como Hold Out o Validación Cruzada) para separar el conjunto de datos de manera correcta.
2. El **algoritmo de Machine Learning** que se está evaluando.
3. La **métrica de rendimiento** mediante la cual se evaluarán las predicciones del modelo (por ejemplo, exactitud, error cuadrático, etc.).

La carga, limpieza y preprocesamiento del dataset es un prerrequisito indispensable que debe completarse antes de pasar los datos al *test harness*.

Un buen *test harness* debe permitir que diferentes algoritmos sean evaluados equitativamente. Para garantizar esto, las particiones de datos y las métricas de rendimiento deben mantenerse constantes en todas las evaluaciones.

> [!info] Explicación
> **El propósito del Test Harness:**
> Funciona como un entorno de laboratorio controlado para experimentación estructurada. Cuando se desea probar y comparar 5 algoritmos distintos (ej. Regresión Logística, Random Forest, SVM, KNN, Naive Bayes), se necesita asegurar que todos compitan en igualdad de condiciones. Si evalúas un algoritmo en un subconjunto de datos fácil, y otro en un subconjunto difícil, la comparación no es válida. El *test harness* automatiza este flujo garantizando equidad y rigor metodológico en la experimentación.
