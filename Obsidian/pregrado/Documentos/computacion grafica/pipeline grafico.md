el bus de comunicacion por lo genereal da cuellos de botellas 
la gpu y cpu estan coenctadas por un bus siempre el que tiene el control tienel cpu 
en la cpu nos encargamos de:
i/o 
fisicas 
ai

en la gpu e llevan acabo gemetria rasterizacion fragmentacion y display 

primitiva quiere decir un triangulo que se obitene de los vertices pero  se tiene en coordenadas por lo que no son solo ya puntos 
proceso de dividir el triangulo en pequeños espacios llamados  fragmentos se llama  el proceso rastering  los fragmentos son espacios que no tienen color 

un algoritmo de renderis va a llenar los fragmentos con los colores 

ahora que se tiene la informacion de los pixel se miestra la informacion en la panatalla 


## Notas relacionadas
- [[OpenGl]]
- [[pixeles]]
- [[open gl]]
- [[Untitled 4]]

## transformer
se puede hacer una opercacon de transformacion  de escala es tener difernentes  coordenadas mover transladar agrandar 

## el alogrimo de cliiper 
elimina y descarta vertices y muestra solo la parte visible  del ente 
## proyeccion
da perspectiva desde el punto de observacion 
##  rastering 
muesta los fragmentos 
## libreaia 
### immediate 
es el que esta mas apegado al hardware
no alamacenan los graficos 
procesas la ecena y se borra 
## retailed 
es de mas alto nivel 
tiene memoria y se le da cambios con respecto a la ecena actual  el rendimiento disminuye 

con pixel se pasa le plano cartesiiano 


la zona visble esta dentro de -1 +1 

glvertex3fv(x,y,z) formato 
gl(open gl )
vertex3f)_function name
3 dimencion
f  es el tipo de dato:
f float 
d double 
boolean 
v puntero: 
lee la longitud de tods las datos desde donde empiza en esa dir de memoria los datos hasta donde se llega la otra ventaja es que se carga todos los  graficsos de golpe 
