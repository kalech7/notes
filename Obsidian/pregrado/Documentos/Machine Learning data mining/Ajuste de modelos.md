cuando entrenamos nuestro modelo intentamos hacer encajar (fit) los datos de entrada entre ellos y con la salida 
## generalizacion del conocimiento
la maquinas deben ser capaces de generalizar conceptos cuando entrenamos nuestros modelos computacionales con un conjunto de datos de entrada estamos haciendo que el algoritmo sea capaz de generalizar un concepto para que al consultarle por un nuevo conjunto de datos desconocido este sea capaz de sintentizarlom comprendelo y devolvernos un resultado fiable dada su capacidad de generalizacion
## el problema de la maquina al generalizar
si los datos de entrenamiento son muy pocos nuestra maquina no sera capaz de generalizar el conocimiento y estara incurriendo en underfitting por el contrario si entrenamos a nuestra estrictamente con una caracteristica no podra reconocerlo 
tanto el problema del ajuste por debajo(underfitting) como por encima(overfitting) de los datos son malos porque no permiten que nuestra maquina generalice el conocimiento y no nos dara buenas predicciones

## overfitting
nuestra maquina solo se ajustar a aprender los casos particulares que le enseñamos y sera incapaz de reconocer nuevos datos de entrada. cuando sobre entrenamosa nuestro modelo estara considerando como validos solo los datos identicos a los de nuestro conjunt de entrenamiento incluido sus defectos (muchas veces introducimos muestras atipicas o anomalas )
## equilibrio del aprendizaje
debemos encontrar un punto medio en el aprendizaje de nuestro modelo en el que no estemos en underfitting y tampoco en overfitting 
![[Pasted image 20240603073921.png]]
para solucionar este problema se debe subdividir nuestro conjunto de datos de entrada para entrenamiento en dos uno para entrenamiento y otro para test para lograr que nuestro modelo de buenos resultados iremos revisando y contrastando nuestro entrenammiento con el conjunto de test y su tasa de errores 