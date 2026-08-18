el obejtivo de machine learning es construir un modelo que tome unos datos de entrada y que sea capaz de generar predicciones sobre esos datos
cuando construimos el modelo lo que buscamos es encontrar una serie de parametros(coeficientes numericos internos del modelo y que se obtienn de forma automatica con el entrenamiento) ademas para construir ese modelo se necesita definir los hiper parametros que son tambien unos coeficientes numericos pero que nosotros como programadores del algoritmo tenemos que definir buscando generar las mejores predicciones posibles
es usualmente necesario entrenar multiples modelos con diferentes parametros e hiper parametros para elegir cual es el mas adecuado de todos estos modelos para el problema que estamos intentando y para lograr esto debemos ajustar los parametros e hiper parametro de cada modelo medir su desempeño y escojer el modelo que haga las mejores predicciones 
## capacidad de generalizacion
es simplemente la capacidad de generar buenas predicciones sobre datos que no ha visto previamente 
## sets de validacion y prueba 
partimos nuestros datos en entrenamineto dependiendo del tamaño de los regsitros se tomaria aproximadamente el 70% validacion alrededor del 15% y prueba 15% 
* el set de entrenamineto nos permite obtener los parametros del modelo y 
* * el de validacion nos permite ajustar los hiper parametros y seleccionar el mejor modelo entre varios posibles
* el set de purbea nos permite medir la capacidad de generalizacion del modelo
el problema de este enfoque es que para poder usarlo es que generalmente requerimos muchos datos y esto no resulta vialbe pero ademas puede ocurrir que al hacer la particion no necesariamente estos tres subsets tengan las mismas distribuciones entonces es posible que por ejemplo el set de entrenamiento tenga datos ligeramente diferentes de los sets validacion y prueba y esto afecta en el entrenamiento y validacion del modelo
## k fold cross validation
en lugar de usar diferentes sets sets para entrenamiento validacion y prueba en la validacion cruazada vamos a usar  la totatlidad de los datos aunque existen muchos metodos para lograr este objetivo se usa la validacion crazada de k iteraciones 
### algoritmo 
*inicia*
con la mezcla aleatoria de los datos con la inicializacion del parametro k(es el numero que define el numero de particiones de nuestro set de datos asi como el numero de iteraciones de entrenamiento y validacioness que se usaran al construir el modelo)
*entrenamiento y validacion*
se toma una de las k particiones y se mantiene  oculta el modelo
se toman k-1 particiones restantes  y con ellas se entrena el modelo y almacena el desempeño 
validar con la particion oculta y almacenar desempeño
*finalmente*
se repite k veces cambiando la particion oculta  una vez terminadas la iteraciones tendremos k medidas de desempeño para los sets y entrenamiento y validacion usados en cada iteracion 
asi que el desemeño final del modelo sera simplemtne el promedio de los desempeños anteriores 
## numero adecuado de particiones
no existe una unica respuesta todo depende del modelo que estemos construyendo y los datos que estemos usando. podria ser adecuando estos valores de kni muy pequeños ni muy grandes para evitar el uso excesivo de poder computacional y si es muy pequeño es posible que no detecte muy bien los patrones de nuestro modelo


