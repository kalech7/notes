http es un protocolo el cual mueve recursos de web que componen una pagina web entre clientes y servidores 
![[Pasted image 20240429220901.png]]
http es request/response protocol para buscar recursos en la web 
corre en tcp tipicamente en el puerto 80
es parte del browser/server app
http esta implementado en a nivel de usuario 
## Buscando la web con http
empieza con la url
protocolo(http:) server(en.wikipedio.org) page on server(wiki/vegemite)
*pasos*
se resuelve el server a la direccion ip (dns)
se configura una conexion tcp en el server
se envia http request para la pagina 
(espera la respuesta http de la pagina)
ejecuta/busca rescursos embebidos/renderiza
limpia cualquier idle  de conexiones tcp
## estatico vs dinamico 
* paginas web estatica es un contenido en archivo ej imagen
* web dinamica es el resultado de un programa en ejecucion (javascript en un cliente,php en un servidor o ambos)