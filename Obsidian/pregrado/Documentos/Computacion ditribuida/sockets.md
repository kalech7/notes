define como las apps usan la red
permite que las apps hablen por medio de hosts 
esconde los detalles de la red 
el proposito de usar APR es dejar las apps hablar con otras apps

## aplicacion
configracuion simple cliente servidor 
server app retorna una respuesta larga 
cliente app manda una solicitoas al servidor 
![[Pasted image 20240520223126.png]]
es lo basico para muchas apps 
file transfer,web,echo
## socket api
para escribir un socket necesitamos algo concreto API el cual muchas aplicaciones corren en un hostar pueden interacturar en la red
es una abstraccion para  usar la red 
sockets se usan para usar todas las app the internet
estan en la mayoria de sistemas operativos y librerias
existen dos diferentes tipos de tipos de servicios de red que api sockets
streams: confiablemente envia un stream de bytes
datagramas: no confiable manda separados mensajes 

sockets permiten apps adjuntarse a la local network a diferentes puertos api sockets esta entre la aplicacion y la red
sockets usan estructura de datos que es llamda socket
![[Pasted image 20240520224457.png]]
## uso 
1. connect<->
2. request ->
3. replay <-
4. close <->

## Notas relacionadas
- [[Http introduccion]]
- [[Remote Procedure Call (rpc)]]
- [[servidores]]
- [[computacion distribuida]]
