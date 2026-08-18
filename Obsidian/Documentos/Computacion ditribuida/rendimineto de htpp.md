paralelo y persistente en conexiones 
## plt (page load time)
es la principal medida del rendimiento de la web 
desde el click hasta que el usuario mira la pagina 
pequeños aumentos en plt decresen las ventas
depende de muchos fatosres 
* strutura de una pagina
* http y tcp protocolo
* network rtt y ancho de banda
### rendimiento temprano
http usa una conexion tcp para buscar un recurso web
esta hecho con http muy facil para construir
pero da muy poco plt 
muy pocas razones porque plt mas largo de lo necesario
las secuencias de solicitudes y respuestas incluso cuando para diferentes servidores
multiples configuraciones de conexiones de tcp para el mismo servidor
multiples tcp tienen fases slow-start
la red es no usada efecientemente 
es peor con muchos recursos pequeños
## maneras para reducir plt
reduce el tamaño del contenido a transferir imagenes mas pequeñas,gzip
cambiar http para hacerlo mejor con el ancho de banda disponible 
cambiar http para evitar repetidas transferencias de un mismo contenido(cache y proxies)
mover el contenido cerca del cliente (cdns)

## conexiones paralelas
una simple manera para recducir plt
los navegadores corren multiples (8say) http instacias en paralelo
el server se mantiene esta soportando concurrentes solicitudes para muchos clientes 
* como ayuda esto?
conexionnes paralelas no son relentizadas mucho
t