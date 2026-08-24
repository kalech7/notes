peer to peer entrega de contenido es una alternativa interesante porque provee una alternativa cliente servidor usando cdns(content delivery network: es una red de servidores distribuidos geograficamentre que tebajan juntos para entregar contenido de internet de manera rapida y eficneiente. estos servidores alamcenan en cache contenido estatico y dinaminco, su proposito es reducir la latencia )
corre sin una infraestructura dedicada 
## contexto
entrega con cliente servidor CDNs: 
eficiente escalable para contenido popular
confiable manegado para un buen servicio
sus desventajas son: 
necesita infraestructura dedicada
control centralizado

la metaa de p2p es entregar sin una infraestrutura dedicada o control centralizada lo que lo hace  aun eficiente en escala y confiable
la idea principal es tener parcipantes que ayuden a los demas 

los retos que presenta p2p es que no tienen servidores confiables ya que toda la comunicacion para entregar el contenido estara entre los participantes y estos peers van a organizarse ellos mismo de alguna manera en una arquitectura coherente para lograr la tarea de entregar contenido mas no cliente-servidor
conduce varios problemas a escala:
1. limitadas capacidades no se tiene el privilegio de tener una highend servers que puede distribuir contenido a diferentes clientes
2. iniciativas de participacion: los peers estan ayudando a todos pero si alguien quiere descargar contenido va a tener una copia del archivo apesar de eso estas ayudando a los demas nodos
3. decentralizacion los nodos cambian con el tiempo no esta tan claro a quien contactar para tener una copia del contenido

los nodos pueden enviar contenido a los demas usnado un arbol de distribucion tipicamente con replicas y con la capacidad de  auto escalar
los nodos juegan dos roles: 
descarga para ayudar  a los demas y carga  para completar favores a otros nodos
combinan los dos roles  yo cargo por ti si tu decargas por mi 
fomenta la cooperacion 
## permitiendo la decentralizacion 
los nodos deben aprender donde obtener el contenido  se usand dhts(distributed hash tables: es una estructura de datos que asocia claves con valores cada clave transdorma mediante una funciona hash en un indice de una tabla)  estos dhts son completamente desentralizados, eficientes  para un indice distribuido, el indice esta espacrido en todos los nodos 
la lista de indices se usan   para contactar el contenido 
cualquier noodo puede ver el indice 
## bittorrent
principal p2p se usa aun 
trafieree arhcigo en piezas por paralelismo 
usa tracker o un decentralizado indice dht 
1. se empiza con una descripcion de l torrent
2. se contacta al tracker para unir y obtener la lista de nodos o un dht 
3. intercambia pedazos con diferentes nodos 
4. favorece a los nodos que pueden cargar hacia a mi y axifixia nodos que no bajando la carga hacia ellos

## Notas relacionadas
- [[content delivery networks]]
- [[computacion distribuida]]
- [[servidores]]
- [[Historia del internet]]
