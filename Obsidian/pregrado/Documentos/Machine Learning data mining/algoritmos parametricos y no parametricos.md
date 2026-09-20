## Paramétricos 
Son técnicas estadísticas que se basan en supuestos específicos sobre la distribución subyacente de la población que se estudia. Suelen suponer que los datos siguen una distribución normal y estiman los parámetros de esta distribución.
La idea básica detrás del método paramétrico es que hay un conjunto de parámetros fijos que se utilizan para determinar un modelo de probabilidad. Son aquellos métodos para los cuales sabemos previamente que la población es normal, o si no es así, podemos aproximarla fácilmente usando una distribución normal, lo cual es posible invocando el teorema del límite central.

* Los parámetros para utilizar la distribución normal son:
- Media (Significar/Mean)
- Desviación estándar

*Los métodos paramétricos requieren varias suposiciones sobre los datos:*
- **Normalidad:** Los datos siguen una distribución normal (gaussiana).
- **Homogeneidad de la varianza:** La varianza de la población es la misma en todos los grupos.
- **Independencia:** Las observaciones son independientes unas de otras.

> [!info] Explicación
> **Algoritmos Paramétricos:** Simplifican el proceso de aprendizaje resumiendo los datos en un conjunto de parámetros fijos (como el peso y el sesgo en una regresión lineal). Independientemente de cuántos datos nuevos se agreguen, el número de parámetros del modelo no cambia. Asumen fuertemente que la función matemática que mapea la entrada a la salida tiene una forma específica.

### ¿Cuáles son?
- **Pruebas estadísticas:**
    - **T-test:** Prueba de la diferencia entre las medias de dos grupos independientes.
    - **ANOVA:** Prueba de la diferencia entre las medias de tres o más grupos.
    - **Prueba F:** Compara las varianzas de dos grupos.
    - **Prueba de Chi-cuadrado:** Prueba de relaciones entre variables categóricas.
    - **Análisis de correlación:** Mide la fuerza y la dirección de la relación lineal entre dos variables continuas.

- **Modelos de aprendizaje automático:**
    - **Regresión lineal:** Predice un resultado continuo basado en una relación lineal con una o más variables independientes.
    - **Regresión logística:** Predice un resultado binario (por ejemplo, sí/no) basado en un conjunto de variables independientes.
    - **Bayes ingenuo (Naive Bayes):** Clasifica los puntos de datos basándose en el teorema de Bayes y asumiendo la independencia entre las características.
    - **Modelos de Markov ocultos:** Modela datos secuenciales con estados ocultos y salidas observables.

### Ventajas
- **Más potente:** Cuando se cumplen los supuestos, las pruebas paramétricas suelen ser más potentes que las pruebas no paramétricas, lo que significa que es más probable que detecten un efecto real cuando existe.
- **Más eficiente:** Las pruebas paramétricas requieren tamaños de muestra más pequeños que las pruebas no paramétricas para lograr el mismo nivel de potencia estadística.
- **Proporcionan estimaciones poblacionales:** Los métodos paramétricos proporcionan estimaciones de la media de la población, la varianza y otros parámetros, que se pueden utilizar para un análisis posterior.

### Límites paramétricos
- **Restringidos:** Al elegir una forma funcional específica, estos métodos están altamente restringidos a esa forma.
- **Complejidad limitada:** Estos métodos son más adecuados para problemas simples.
- **Mal ajuste:** En la práctica, es poco probable que la forma paramétrica elegida coincida exactamente con la función de mapeo subyacente real.

> [!info] Explicación
> La principal desventaja es el **sesgo inherente**; si supones que tus datos siguen una regresión lineal pero en realidad la relación es cuadrática o exponencial, el algoritmo paramétrico nunca podrá ajustarse correctamente (sufrirá de underfitting).

## Notas relacionadas
- [[machine learning]]
- [[machine learning  algoritmos parametricos]]
- [[modelos de regresion]]
- [[tipos de machine learning]]

## No paramétricos 
Son técnicas estadísticas que no se basan en supuestos específicos sobre la distribución subyacente de la población que se estudia. A menudo se denominan "métodos libres de distribución".
La idea básica detrás de los métodos no paramétricos es que no es necesario hacer suposiciones sobre los parámetros de la población dada.
De hecho, estos métodos no dependen de las características rígidas de la población. Aquí no hay un conjunto fijo de parámetros disponibles y tampoco se asume una distribución de probabilidad subyacente.

- La razón principal para usarlos es que no hay necesidad de adherirse estrictamente a las restricciones de los métodos paramétricos.
- La segunda razón importante es que no necesitamos hacer suposiciones fuertes sobre la población con la que estamos trabajando.
- La mayoría de los métodos no paramétricos disponibles son muy fáciles de aplicar y de entender, dado que su complejidad conceptual es baja.

*Los métodos no paramétricos requieren algunas suposiciones básicas sobre los datos:*
1. **Independencia:** Los puntos de datos son independientes y no están influenciados por otros.
2. **Muestreo aleatorio:** Los datos representan una muestra verdaderamente aleatoria de la población.
3. **Homogeneidad de la medición:** Las mediciones son consistentes en todos los puntos de datos.

> [!info] Explicación
> **Algoritmos No Paramétricos:** A pesar del nombre, "no paramétrico" no significa que no tengan parámetros, sino que el número de parámetros no es fijo y crece a medida que se proporcionan más datos. Son mucho más flexibles porque no asumen una forma funcional rígida para mapear las entradas a las salidas, adaptándose libremente a la forma natural de los datos de entrenamiento.

### ¿Cuáles son?
- **Pruebas estadísticas:**
    - **Prueba U de Mann-Whitney:** Prueba de la diferencia entre las medianas de dos grupos independientes.
    - **Prueba de Kruskal-Wallis:** Prueba la diferencia entre las medianas de tres o más grupos.
    - **Correlación de rango de Spearman:** Mide la fuerza y la dirección de la relación monótona entre dos variables.
    - **Prueba de rango con signo de Wilcoxon:** Prueba la diferencia entre las medianas de dos muestras pareadas.

- **Modelos de aprendizaje automático:**
    - **K-Vecinos más cercanos (KNN):** Clasifica los puntos de datos en función de las similitudes con sus K vecinos más cercanos.
    - **Árboles de decisión:** Realiza clasificaciones basadas en una serie de reglas condicionales (preguntas de sí/no) sobre las características.
    - **Máquinas de vectores de soporte (SVM):** Crea un límite de decisión que maximiza el margen entre las diferentes clases (usando kernels no lineales).
    - **Redes neuronales:** Se pueden diseñar con arquitecturas específicas para manejar datos complejos, como redes neuronales convolucionales para imágenes o redes recurrentes para secuencias.

### Ventajas 
- **Flexibilidad y Poder de Adaptación:** Permiten modelar relaciones complejas y no lineales sin imponer formas predeterminadas.
- **Menores suposiciones previas:** No se necesita saber de antemano la distribución de la población o la relación subyacente.
*(Nota: Se eliminaron textos repetidos en el original en esta sección)*

### Limitaciones de los métodos no paramétricos
- **Más datos:** Se requieren muchos más datos de entrenamiento para estimar adecuadamente la función de mapeo.
- **Más lento:** Son mucho más lentos para entrenar y predecir, ya que a menudo tienen muchísimos parámetros que aprender o deben comparar contra todo el dataset.
- **Sobreajuste:** Existe un mayor riesgo de sobreajustar (*overfitting*) los datos de entrenamiento.
- **Interpretabilidad:** Es más difícil explicar por qué se hacen predicciones específicas (modelos de caja negra).

> [!info] Explicación
> La principal desventaja es el riesgo de **overfitting**, ya que la excesiva flexibilidad del modelo puede llevarle a adaptarse al ruido de los datos de entrenamiento si no se usa regularización o no se cuenta con datos suficientes. Además, modelos como KNN pueden volverse extremadamente pesados computacionalmente en la fase de predicción, dado que almacenan y procesan todo el dataset.
