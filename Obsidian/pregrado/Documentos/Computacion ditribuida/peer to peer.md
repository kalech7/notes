La entrega de contenido Peer-to-Peer (P2P) es una alternativa muy interesante al modelo cliente-servidor tradicional, ya que no requiere infraestructura dedicada.

> [!info] Explicación: ¿Qué es P2P?
> En una red **P2P (Peer-to-Peer)**, cada computadora (nodo o *peer*) actúa simultáneamente como cliente y como servidor. No hay un servidor central; los recursos (ancho de banda, almacenamiento, procesamiento) son compartidos directamente entre los participantes.

## Contexto
En la entrega tradicional mediante Cliente-Servidor o CDNs (Content Delivery Networks):
- **Ventajas:** Es eficiente, escalable para contenido popular, y al ser un servicio gestionado, resulta altamente confiable.
- **Desventajas:** Necesita una infraestructura dedicada costosa y depende de un control centralizado. *(Nota: Las CDNs son redes de servidores distribuidos geográficamente que trabajan juntos para entregar contenido de internet de manera rápida y eficiente. Estos servidores almacenan en caché contenido estático y dinámico, con el propósito de reducir la latencia).*

La meta principal del modelo P2P es entregar contenido sin depender de una infraestructura dedicada ni de un control centralizado, logrando aún así ser eficiente, escalable y confiable. La idea fundamental es que los propios participantes ayuden a distribuir la información a los demás.

### Retos del modelo P2P
Dado que no existen servidores altamente confiables, toda la comunicación para entregar el contenido ocurre entre los propios participantes. Estos nodos deben organizarse por sí mismos en una arquitectura coherente. Esto conduce a varios problemas al escalar:

1. **Capacidades limitadas:** A diferencia de un servidor de alta gama, los nodos domésticos tienen ancho de banda y recursos limitados.
2. **Iniciativas de participación:** Un nodo que descarga un archivo también debe estar dispuesto a cargar partes de ese archivo para ayudar a otros nodos, lo cual requiere incentivar la cooperación ("yo cargo por ti si tú descargas por mí").
3. **Descentralización y dinamismo (Churn):** Los nodos se conectan y desconectan continuamente. Por lo tanto, es difícil saber a quién contactar en un momento dado para obtener una copia del contenido.

Los nodos pueden enviar contenido a los demás usando árboles de distribución, típicamente con réplicas y con capacidad de autoescalar. Cada nodo juega dos roles combinados: **descarga** (para obtener lo que necesita) y **carga** (para hacer favores a otros nodos).

## Permitiendo la descentralización 
Para que los nodos sepan dónde obtener el contenido sin un servidor central, se utilizan **DHTs (Distributed Hash Tables)**.

> [!info] Explicación: Distributed Hash Table (DHT)
> Una **DHT** es una estructura de datos distribuida que asocia claves con valores. Cada clave se transforma mediante una función hash en un índice. En lugar de estar guardada en un solo servidor, esta "tabla" está fragmentada y repartida entre todos los nodos de la red. Es completamente descentralizada, eficiente y permite que cualquier nodo pueda consultar el índice para localizar quién tiene el contenido deseado.

## BitTorrent
Es el protocolo P2P más conocido y utilizado en la actualidad. Su principal característica es que transfiere archivos dividiéndolos en pequeñas piezas que se descargan en paralelo desde múltiples fuentes.

Puede utilizar un **tracker** (un servidor central que solo mantiene listas de quién tiene qué) o un índice descentralizado mediante **DHT**.

El proceso funciona así:
1. Se empieza obteniendo una descripción del archivo (el archivo `.torrent` o el enlace *magnet*).
2. Se contacta al *tracker* (o se consulta la DHT) para unirse al enjambre y obtener la lista de nodos participantes.
3. El cliente intercambia pedazos del archivo con diferentes nodos.
4. **Mecanismo de incentivo (Tit-for-Tat):** El protocolo favorece otorgando más velocidad de descarga a los nodos que suben datos activamente hacia él, y "asfixia" (choke) o corta la conexión a los nodos que solo descargan sin compartir.

## Notas relacionadas
- [[content delivery networks]]
- [[computacion distribuida]]
- [[servidores]]
- [[Historia del internet]]
