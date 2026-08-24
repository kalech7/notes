un protcolo es un dialogo estructurado entre 2 o mas entidades en un contexto distribuido controlando la sintaxis(estuctura),semantica(significado que tienen estas estructuras) y sincronizacion (conectados desdde la misma hora para que se puedan entender) 
un protocolo criptografico usa mecanismo de seguridad para logar una funcion de seguridad (confidencialidad)
## objetivos:
* unicidad: secreto compartido entre dos entidades
* integridad: el mensaje con verificacion de origen 
* confidencialidad: el contenido del mensaje no es accesible por una persona no autorizada 
* no repudio de origen: el transmisor no puede negar el envio 
* no repudio de destino: el recptor no puede negar la recepcio
## fundamentos
todos protocolos criptograficos comparten 
1. algunas entidaddes estan intercambiando mensajes 
2. estas entidades intentan lograr funciones de seguridad 
3. estas entidades estan operenado en un ambiente hostil e inseguro 
el protocolo debe ser robusto y confiable para enfrentarse a un determinado atacante 
involucra una secuencia  de intercambio de mensajes de la forma 

A(la computadora a)->(envia) B(la computadora b):M(el mensaje)
{M}k(es la llave) (se represta la encriptaacion simetrica  con las llaves {})
## Ataques
* known-key attack: el atacante logra obtener algunas llaves usado anteriormente y usa esta informacion
* replay:el atacante guarda mensajes y los reutiliza despues
* impersonation: el atacante asume la identidad de una de las entidades legitimas de la red
* man in the middle: el atacante se interpone entre dos entidades
* interleaving attack: el atacante inyecta mensajes adulteradas en un protcolo para interrumpilo o subertirlo

## Notas relacionadas
- [[protocolo needham schroeder]]
- [[seguridad informatica]]
- [[fundamentos de seguridad]]
- [[ataques a contraseñas]]
