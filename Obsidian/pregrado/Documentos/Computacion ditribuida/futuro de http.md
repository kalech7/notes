siempre habra la necesitas de hacer html mas rpaido 
el diagram de cascada indicasa la progession de una pagina cargando
la cascada y plt depnede de varios factories 
my difernete de browsers 
muy diferente para repitir paginas view
depende la conexion de la red
## trabajos recientes para reducir plt
los paginas crecen mas complejas
es mas grande dinamico y seguro 
mejor uso de network
mejor struturas de contenido  (mode pagespeed)
* spdy (speedy 
un conuunto de mejoras: multiplexio (paralela ) http
el cliente prioriza solicitudes paralelas 
encabezados http comprimidos 

> [!info] Explicación: SPDY y HTTP/2
> **SPDY** fue un protocolo experimental desarrollado por Google para reducir la latencia de carga de páginas web. Sus ideas principales (multiplexación de varias peticiones sobre una misma conexión TCP, compresión de cabeceras, priorización) fueron la base para la estandarización de **HTTP/2**. A diferencia de HTTP/1.1 que requería múltiples conexiones para cargar recursos en paralelo (o dependía de un *pipelining* a menudo defectuoso), HTTP/2 permite streams concurrentes sin bloqueo de cabeza de línea a nivel de HTTP (Head-of-Line Blocking).

* mod_pagespeed
la manera que las paginas estan escirtas afecta que tan rapido cargan 
la idea principal es que tener un servidor que reescriba(compile) paginas para ayudarlas a que carguen rapido
extension de apache server 
reescribe paginas en el vuelo con las reglas basadas en las mejores practicas 
## Optimizacion
### Contenido
- Gzip
- Imágenes pequeñas
- Variables, CSS embebidas
### HTTP
- Optimizar el uso del ancho de banda
- Browser – paralelo
- Conexiones persistentes
- Pipelining

> [!info] Explicación: Evolución de HTTP hacia HTTP/3
> Para el futuro del protocolo HTTP, la última evolución es **HTTP/3**. Utiliza el protocolo **QUIC** (basado en UDP) en lugar de TCP. Esto soluciona el bloqueo de cabeza de línea a nivel de transporte (donde un paquete TCP perdido detenía todos los flujos multiplexados en HTTP/2). QUIC también reduce enormemente la latencia de los handshakes iniciales, integrando la seguridad (TLS 1.3) por defecto.

### Caching y Proxies  (CARP)
### CDN

## Notas relacionadas
- [[Http introduccion]]
- [[http caching and proxies]]
- [[content delivery networks]]
- [[rendimineto de htpp]]
