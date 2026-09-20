El rendimiento en la web suele medirse considerando el uso de conexiones en paralelo y conexiones persistentes.

## PLT (Page Load Time)
El **Page Load Time (PLT)** es la principal métrica del rendimiento web. Mide el tiempo que transcurre desde que el usuario hace clic en un enlace hasta que visualiza la página completamente cargada en su navegador.

> [!info] Explicación: Importancia del PLT
> Pequeños aumentos en el PLT pueden provocar disminuciones significativas en las ventas y retención de usuarios. Por ejemplo, Amazon determinó que por cada 100 milisegundos extra de latencia, perdían un 1% en ventas.

El PLT depende de múltiples factores:
* La estructura y complejidad de la página (cantidad de imágenes, scripts).
* El rendimiento de los protocolos HTTP y TCP.
* El tiempo de ida y vuelta en la red (RTT - Round Trip Time) y el ancho de banda disponible.

### Rendimiento temprano (Problemas iniciales de HTTP)
Inicialmente, HTTP/1.0 utilizaba una conexión TCP nueva para buscar cada recurso web. Estaba diseñado así porque era muy fácil de construir, pero resultaba en un PLT muy pobre.

Existen varias razones por las que este enfoque generaba tiempos de carga más largos de lo necesario:
- Cada recurso requería una configuración completa de conexión TCP, incluyendo el *Three-Way Handshake*.
- Al abrir múltiples conexiones TCP hacia un mismo servidor, cada una debía pasar por la fase de **"slow-start"** (donde TCP inicia enviando datos lentamente para medir la congestión de la red).
- En consecuencia, la red no se utilizaba eficientemente, lo cual empeoraba al tener páginas con muchísimos recursos pequeños (iconos, scripts, estilos).

## Maneras de reducir el PLT
Para mejorar el tiempo de carga, se aplican varias estrategias:
1. **Reducir el tamaño del contenido transferido:** Utilizar imágenes más pequeñas y optimizadas, y aplicar compresión (como Gzip o Brotli) a los archivos de texto (HTML, CSS, JS).
2. **Mejorar el uso de HTTP:** Modificar o actualizar HTTP para aprovechar mejor el ancho de banda disponible (por ejemplo, usando conexiones persistentes *Keep-Alive* o migrando a HTTP/2 o HTTP/3).
3. **Evitar transferencias repetidas:** Utilizar mecanismos de **Caché** y **Proxies** para no descargar el mismo contenido múltiples veces.
4. **Acercar el contenido al cliente:** Implementar **CDNs** (Content Delivery Networks) para servir recursos desde servidores geográficamente más próximos al usuario.

## Conexiones paralelas
Una forma sencilla e inicial de reducir el PLT en navegadores modernos es el uso de conexiones paralelas.
Los navegadores web abren múltiples conexiones TCP simultáneas (típicamente hasta 6 u 8 por dominio) para solicitar varios recursos al mismo tiempo.
Esto permite que el servidor atienda solicitudes concurrentes, acelerando la descarga global, aunque sigue sin ser la solución perfecta frente a la multiplexación real que introdujo HTTP/2.

> [!info] Explicación: Conexiones Persistentes y Pipelining
> Para solventar la creación excesiva de conexiones, HTTP/1.1 introdujo **Conexiones Persistentes** (`Connection: keep-alive`), permitiendo reutilizar un solo socket TCP para múltiples peticiones. Luego se intentó usar **Pipelining** (enviar varias peticiones sin esperar la respuesta de la anterior), pero falló debido al bloqueo de cabeza de línea (Head-of-Line Blocking), un problema finalmente resuelto en versiones modernas del protocolo.

## Notas relacionadas
- [[Http introduccion]]
- [[http caching and proxies]]
- [[content delivery networks]]
- [[futuro de http]]
- [[tiempo de respuesta vs Throughput]]
