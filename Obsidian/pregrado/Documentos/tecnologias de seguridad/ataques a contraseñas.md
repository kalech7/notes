funciones hash
toma un dato de cualquiera tamaño a un valor fijo 
solo se puede calcular de una sola direccion no es posible volver al valor original 

en linux usa salt y el valor hash de la contraseña + salt (salt es randomico )
se tiene el salt aqui en este **`/etc/passwd`** y el valor de hash esta en *`/etc/shadow`*
en system32 sam estan los valores hash de la contraseña esta protegido por el kernel pero se puede ver el archivo con un live 

ataque de fuerza bruta 
hace uso de combinacion de caracteres 
ataque de disccionario 
hace uso de una lista de palabtras pregeneradas

## tablas arcoiris 
contienen los valroes hash calculados 
crackstation 

es un live de linux trinity rescue key para acceder a SAMm 

## ataques de cumpleaños
### colision hash: 
hace uun barrido de todos los usuarios con la misma contraseña

