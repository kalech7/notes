Cuando entrenamos nuestro modelo, intentamos hacer encajar (*fit*) los datos de entrada entre ellos y con la salida esperada.

## Generalización del conocimiento
Las máquinas deben ser capaces de generalizar conceptos. Cuando entrenamos nuestros modelos computacionales con un conjunto de datos de entrada, estamos haciendo que el algoritmo sea capaz de abstraer y generalizar un concepto. De esta forma, al consultarle por un nuevo conjunto de datos desconocido, será capaz de sintetizarlo, comprenderlo y devolvernos un resultado fiable, gracias a su capacidad de generalización.

> [!info] Explicación
> **Generalización:** Es el objetivo último de cualquier modelo de ML. Un modelo que generaliza bien ha capturado el "patrón subyacente" real de los datos, en lugar de memorizar ejemplos. Esto le permite hacer predicciones precisas sobre datos completamente nuevos (datos de validación o del mundo real) que nunca vio durante su fase de entrenamiento.

## El problema de la máquina al generalizar
Si los datos de entrenamiento son muy pocos, nuestra máquina no será capaz de generalizar el conocimiento y estará incurriendo en subajuste (*underfitting*). Por el contrario, si entrenamos a nuestra máquina estrictamente con una sola característica o sobre un conjunto muy limitado con todos sus defectos, no podrá reconocer casos nuevos. 
Tanto el problema del ajuste por defecto (*underfitting*) como por exceso (*overfitting*) de los datos son negativos, porque impiden que nuestra máquina generalice el conocimiento adecuadamente, lo que resultará en malas predicciones.

> [!info] Explicación
> - **Underfitting (Subajuste):** Ocurre cuando el modelo es demasiado simple (o se entrenó poco tiempo/con pocos datos) para capturar la estructura subyacente de los datos. Falla tanto en los datos de entrenamiento como en los nuevos.
> - **Overfitting (Sobreajuste):** Ocurre cuando el modelo es demasiado complejo y se aprende los datos de entrenamiento de memoria (incluyendo el "ruido" y los errores aleatorios). Rinde perfecto en entrenamiento, pero fracasa con datos nuevos.

## Overfitting
Nuestra máquina solo se ajustará a aprender los casos particulares que le enseñamos, siendo incapaz de reconocer y predecir sobre nuevos datos de entrada. Cuando sobreentrenamos a nuestro modelo, este considerará como válidos únicamente los datos idénticos a los de nuestro conjunto de entrenamiento, incluyendo sus defectos (ya que muchas veces introducimos muestras atípicas o anómalas).

> [!info] Explicación
> El overfitting es como un estudiante que memoriza las preguntas exactas de un examen de prueba, pero no entiende los conceptos. Cuando se le presenta una pregunta ligeramente diferente en el examen real, no sabe qué responder. Se puede combatir utilizando técnicas de regularización, aumentando el tamaño del dataset, o aplicando técnicas de validación cruzada.

## Notas relacionadas
- [[machine learning]]
- [[Validacion Cruzada]]
- [[metodo hold out]]
- [[bias y viarianza]]
- [[test harness]]

## Equilibrio del aprendizaje
Debemos encontrar un punto medio en el aprendizaje de nuestro modelo en el que no caigamos en *underfitting* y tampoco en *overfitting*. 
![[Pasted image 20240603073921.png]]

Para solucionar este problema, se debe subdividir nuestro conjunto inicial de datos en dos partes: una para entrenamiento y otra para testeo. Para lograr que nuestro modelo ofrezca buenos resultados, iremos revisando y contrastando nuestro entrenamiento con el conjunto de test y evaluaremos su tasa de errores.

> [!info] Explicación
> **Equilibrio Sesgo-Varianza (Bias-Variance Tradeoff):** Encontrar el punto medio ideal significa buscar un modelo que no sea ni muy sesgado (underfitting) ni tenga mucha varianza ante pequeños cambios en los datos (overfitting). Dividir los datos en *Train* y *Test* (o incluso añadir un set de *Validation*) es la estrategia estándar para medir el error de generalización de forma empírica y detener el entrenamiento en el punto óptimo (Early Stopping).
