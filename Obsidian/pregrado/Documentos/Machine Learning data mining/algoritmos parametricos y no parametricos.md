## parametricos 
son tecnicas estadisticas que se basan en supuestos especificos sobre la distribucion subyacente de la poblacion que se estudia .Suelen supone que los datos siguen una distribucion normal y estiman los parametros de esta distribucion
la idea basica detas del metodo parametrico es que hay un conjunto de parametrso fijos que se utilizan para determinar un modelo de probabilidad son aquellos métodos para los cuales sabemos previamente que la población es normal, o si no es así, podemos aproximarla fácilmente usando una distribución normal, lo cual es posible invocando el teorema del límite central.
* los parametros para utlizar distribucion normal 
Significar
Desviación estándar
*los metodos parametricos requieren varias supociones sobre los datos*
- ****Normalidad:**** Los datos siguen una distribución normal (gaussiana).
- ****Homogeneidad de la varianza:**** La varianza de la población es la misma en todos los grupos.
- ****Independencia:**** Las observaciones son independientes unas de otras.
### cuales son?
- ****Pruebas estadísticas:****
    - ****t-test:**** Prueba de la diferencia entre las medias de dos grupos independientes.
    - ****ANOVA:**** Prueba de la diferencia entre las medias de tres o más grupos.
    - ****Prueba F:**** Compara las varianzas de dos grupos.
    - ****Prueba de Chi-cuadrado:**** Prueba de relaciones entre variables categóricas.
    - ****Análisis de correlación:**** Mide la fuerza y la dirección de la relación lineal entre dos variables continuas.

 ****Modelos de aprendizaje automático:****
    - ****Regresión lineal:**** predice un resultado continuo basado en una relación lineal con una o más variables independientes.
    - ****Regresión logística:**** predice un resultado binario (por ejemplo, sí/no) basado en un conjunto de variables independientes.
    - ****Bayes ingenuo:**** Clasifica los puntos de datos basándose en el teorema de Bayes y asumiendo la independencia entre las características.
    - ****Modelos de Markov ocultos:**** Modela datos secuenciales con estados ocultos y salidas observables.
### ventajas
- ****Más potente****: Cuando se cumplen los supuestos, las pruebas paramétricas suelen ser más potentes que las pruebas no paramétricas, lo que significa que es más probable que detecten un efecto real cuando existe.
- ****Más eficiente:**** las pruebas paramétricas requieren tamaños de muestra más pequeños que las pruebas no paramétricas para lograr el mismo nivel de potencia.
- ****Proporcionar estimaciones de los parámetros de la población:**** Los métodos paramétricos proporcionan estimaciones de la media de la población, la varianza y otros parámetros, que se pueden utilizar para un análisis posterior.
### limites parametricos
Restringido: Al elegir una forma funcional, estos  métodos están altamente restringidos a la forma especificada.
Complejidad limitada: los métodos son más adecuados para problemas más simples.
Mal ajuste: en la práctica es poco probable que los métodos coincidan la función de mapeo subyacente.
## no parametricos 
son tecnicas estadisticas que no se basan en supuestos especificos sobre le distrivucion subyacente de la poblacion que se estudia . se denominan metodos libres de distribucion 
la idea basica detras del metodo parametrico es que no es necesario hacer suposcion de parametros para la poblacion dada
no es necesario hacer ninguna suposicion de parametros para la poblacion de hecho los metodos no depende la poblacion . aqui no hay un conjunto fijo de parametros disponibles y tampoco hay distribucion de ningun tipo disponible
- La razón principal es que no hay necesidad de ser educado mientras se usan métodos paramétricos.
- La segunda razón importante es que no necesitamos hacer más y más suposiciones sobre la población dada (o tomada) sobre la que estamos trabajando.
- La mayoría de los métodos no paramétricos disponibles son muy fáciles de aplicar y de entender, es decir, la complejidad es muy baja.
*los metodos no parametricos requieren varias suposiciones sobre los datos:*
1. ****Independencia: Los**** puntos de datos son independientes y no están influenciados por otros.
2. ****Muestreo aleatorio: Los**** datos representan una muestra aleatoria de la población.
3. ****Homogeneidad de la medición:**** Las mediciones son consistentes en todos los puntos de datos.
## cuales son?
- ****Pruebas estadísticas:****
    - ****Prueba U de Mann-Whitney:**** Prueba de la diferencia entre las medianas de dos grupos independientes.
    - ****Prueba de Kruskal-Wallis:**** prueba la diferencia entre las medianas de tres o más grupos.
    - ****Correlación de rango de Spearman:**** Mide la fuerza y la dirección de la relación monótona entre dos variables.
    - ****Prueba de rango con signo de Wilcoxon:**** prueba la diferencia entre las medianas de dos muestras pareadas.
- ****Modelos de aprendizaje automático:****
    - ****K-Vecinos más cercanos (KNN):**** Clasifica los puntos de datos en función de los k vecinos más cercanos.
    - ****Árboles de decisión:**** Realiza clasificaciones basadas en una serie de preguntas de sí/no sobre las características.
    - ****Máquinas de vectores de soporte (SVM):**** crea un límite de decisión que maximiza el margen entre las diferentes clases.
    - ****Redes neuronales:**** se pueden diseñar con arquitecturas específicas para manejar datos no paramétricos, como redes neuronales convolucionales para datos de imágenes y redes neuronales recurrentes para datos secuenciales.

### Ventajas 
- ****Pruebas estadísticas:****
    - ****Prueba U de Mann-Whitney:**** Prueba de la diferencia entre las medianas de dos grupos independientes.
    - ****Prueba de Kruskal-Wallis:**** prueba la diferencia entre las medianas de tres o más grupos.
    - ****Correlación de rango de Spearman:**** Mide la fuerza y la dirección de la relación monótona entre dos variables.
    - ****Prueba de rango con signo de Wilcoxon:**** prueba la diferencia entre las medianas de dos muestras pareadas.
- ****Modelos de aprendizaje automático:****
    - ****K-Vecinos más cercanos (KNN):**** Clasifica los puntos de datos en función de los k vecinos más cercanos.
    - ****Árboles de decisión:**** Realiza clasificaciones basadas en una serie de preguntas de sí/no sobre las características.
    - ****Máquinas de vectores de soporte (SVM):**** crea un límite de decisión que maximiza el margen entre las diferentes clases.
    - ****Redes neuronales:**** se pueden diseñar con arquitecturas específicas para manejar datos no paramétricos, como redes neuronales convolucionales para datos de imágenes y redes neuronales recurrentes para datos secuenciales.
### Limitaciones no parametricos
Más datos: se requieren muchos más datos de entrenamiento para estimar
la función de mapeo.
Más lento: mucho más lento para entrenar ya que a menudo tienen mucho más
Parámetros a entrenar.
Sobreajuste: existe un mayor riesgo de sobreajustar los datos de entrenamiento.
Es difícil explicar por qué se hacen predicciones específicas.