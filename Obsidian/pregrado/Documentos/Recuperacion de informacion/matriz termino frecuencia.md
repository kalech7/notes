0las dimsiones del espaacio vectorial es el tamaño del  vocabulario 
se pasa a de una matriz termino documento a termino frecuencia y luego se pasa un una matriz tf idf 
preprocesamiento es hacer la matriz termino decrementeo precencia ausencia 
nos da un inicide el cual es O(1)

coeficiente jaccard se caclcula con los 1 de la matriz 
| a interseccion b | /   | a union B |

inverise document sun termino paarece muchas veces aporta poca informacion 
 term frequency

cloude shannnon el hizo la formula de  entropia (caos impredectibilidad que entrga infomavion )
tf (f,d)= numero de veces que aparece el termino t en d 
idf= log(N/nt)

donde:
N: es el numero de docs en el corpus 
nt: numero de documentos que aparece el termino t 1 por cada termino en el corpuus 

se eliminan stop words 
se debe crear el diccionario cuantas palabras va a tener 

tf x idf  para la matriz tf-idf


el vector que tenga menor agunlo entre el vector es el que mas se asemeja los angulos 
depende de mismo coordenadas df idf 

pca es una analisis estadisitco de la columan matriz tf fd es reducir la dimensionalidad del vocabularioo las columnas que se parecen mas se suman 
idf es vector 

## pasos 
1) encontrar vocabulario (n terminos) 
2) la matriz tf  (n cols / filas )
3) el vector idf  (n terminos) 
4) la matriz tf y idff (n x 8)
5) pca a dos dimensiones matriz 2 col 8 filas 

la compraciones se hacen elemento por elemento 
indicie jarccard  cuentos los unos jaccard(q,doc)
q interseccion doc
q union do

## Notas relacionadas
- [[que es recuperacion de informacion]]
- [[ranking]]
- [[retrival augmented generation]]
- [[Untitled 2]]
