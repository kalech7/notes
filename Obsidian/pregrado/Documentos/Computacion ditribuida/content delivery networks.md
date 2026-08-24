provee una manera efectiva para distribuir contenido a muchos clientes en internet 
se inserta una replica y esto puedo tener una copia del contenido y restribuir el contenido de es punto 
los beneficios asumindo que tenemos un contenido popular 
reduce el server y la carga de la  red 
mejora la experiencia del usuario(plt)
### como se coloca el contenido cerca de los clientes
usando navegadores y proxy caches  (es una replica del contenido)
ayuda pero es limitado por un cliente o clientes en una organizacion
quiere que las replicas esten atraves de internet para todo uso por todos los clientes cercanos 
hecho por el uso inteligente de los DNS(dns mapea entre los nombre de host y las ips de las reaplicas es lo que va a hacer funcionar)

* la resolucion de dns de un sitio da diferentes respuesta  los clientes 
dice a cada cleitnes que sitio esta mas cerca de la replica (map client ip ) cuando se obitene un query desde el nodo se puede preguntar a todas las replicas hacer ping o trace y con el tiempo de repsuesta en ms se puede obtener diferentes ip y construir un mapa de donde las dir estan y trabajar como porveer la respeusta correcta mas rapido 
## Notas relacionadas
- [[http caching and proxies]]
- [[peer to peer]]
- [[rendimineto de htpp]]
- [[futuro de http]]

## modelo empresarial
es un modelo inteligente impulsado por akamai 
coloca una replica de un sitio en particula  en un isp es win win porue se puede mejorar el sitio y la experiencia del usuario y se peude reducir el ancho de banda cuando sea necesario por el isp cuando se ponen replicas the deployment took offf porque es posible armar esta replica simplemente mejorando los servidores dns por el dominio en especidifco que esta manejado por todas las replcias sin cambiar ningun software  isp y sin cambiar ningun de los user clients que estan usando navegadores para la web sin cambiar nada los podemos  rediregir a las replicas mas cercanas
