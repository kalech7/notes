  
RESTful (Representational State Transfer) es un estilo arquitectónico para diseñar sistemas de software distribuidos. Se basa en el concepto de recursos, que son entidades de información, y utiliza métodos HTTP estándar (GET, POST, PUT, DELETE) para manipular estos recursos
## get
se obtiene toda la informacion de la pagina web
## post
se utiliza para enviar datos a un servidor para crear un recurso. Es comúnmente utilizado en formularios web y en solicitudes que requieren enviar datos al servidor
## put
es para actualiza y recuperar informacion guardada 
## delete
elimina recursos identificados por la URI de la solicitud. Es idempotente, lo que significa que si eliminas un recurso, se quita de la colección de recursos.
## head
es un metodo el que solo se solicita los encabezados de la respuesta 
## patch
se utiliza para aplicar modificaciones parciales a un recurso. Es especialmente útil cuando se quiere actualizar solo una parte de un recurso en lugar de enviar y actualizar todo el recurso completo.
## options
es una forma de consultar informacion sobre las opciones de comunicacion disponibles para un recurso web especifico se puden modifcar los ussos de los demas metodos 

### codigos de errores 
100-199 respuestas informativas
200-299 respuestas satisfactorias
300-399 redireciones 
400-499 errores de los clientes
 500-599 errores de los servidores

se debe hacer el modelo vista controlador 
## cookies
son pequeños fragmentos de informacion que retroalimentan a las paginas web y ayudan a recordar datos que se digitan en la pag web
