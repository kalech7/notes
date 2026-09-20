Las suposiciones pueden simplificarse de mejor manera en el proceso de aprendizaje mediante el uso de algoritmos paramétricos, pero esto también impone un límite rígido sobre lo que el modelo puede aprender.
Estos algoritmos simplifican la relación entre los datos de entrada y salida utilizando una forma funcional conocida y predefinida. Por esta razón, se les llama algoritmos de "forma paramétrica" en Machine Learning, ya que asumen una función matemática específica.

El *overfitting* es la incapacidad del modelo para generalizar sus predicciones hacia nuevos datos. Ocurre cuando las predicciones están excesivamente basadas y ajustadas a las etiquetas específicas del conjunto de entrenamiento, memorizando incluso el ruido de los datos.

> [!info] Explicación
> **Algoritmos Paramétricos:**
> Un buen ejemplo de algoritmo paramétrico es la **Regresión Lineal**. Asume que la relación entre la variable de entrada y la de salida es una línea recta. Esta suposición hace que el aprendizaje sea muy rápido y necesite menos datos, porque solo tiene que descubrir los parámetros (la pendiente y el intercepto de la línea). Sin embargo, si la verdadera relación es una curva compleja, el modelo paramétrico fallará al capturarla (underfitting).

## Notas relacionadas
- [[machine learning]]
- [[algoritmos parametricos y no parametricos]]
- [[Ajuste de modelos]]
- [[bias y viarianza]]
