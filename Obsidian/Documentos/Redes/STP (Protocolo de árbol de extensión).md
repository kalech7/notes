<p align="justify">El protocolo de árbol de expansión (STP) es un protocolo de red de prevención de bucles que permite redundancia mientras crea una topología de capa 2 sin bucles. IEEE 802.1D es el estándar original IEEE MAC Bridging para STP. la prioridad predeterminada es 32768</p>


![[Pasted image 20230703151013.png]]
## Problemas con los vínculos de switch redundantes
<p align="justify"> Proporciona múltiples servicios de red al eliminar la posibilidad de un solo punto de falla. Cuando existen múltiples rutas entre dos dispositivos en una red Ethernet, y no hay implementación de árbol de expansión en los conmutadores, se produce un bucle de capa 2.
 Un router disminuirá el TTL (Tiempo de vida) en cada paquete IPv4 y el campo Límite de saltos en cada paquete IPv6. Cuando estos campos se reducen a 0, un router dejará caer el paquete.</p>
## Bucles de la capa 2
Sin STP habilitado, se pueden formar bucles de capa 2, lo que hace que las tramas de difusión, multidifusión y unidifusión desconocidos se reproduzcan sin fin. Esto puede derribar una red en un período de tiempo muy corto, a veces en pocos segundos.
![[Pasted image 20230703151410.png]]
![[Pasted image 20230703151422.png]]
![[Pasted image 20230703151437.png]]
![[Pasted image 20230703151445.png]]
![[Pasted image 20230703151455.png]]
![[Pasted image 20230703151507.png]]
## Tormenta de difusión (Broadcast Storm)
es un número anormalmente alto de emisiones que abruman la red durante un período específico de tiempo. Las tormentas de difusión pueden deshabilitar una red en cuestión de segundos al abrumar los conmutadores y los dispositivos finales.
Las tormentas de difusión pueden deberse a un problema de hardware como una NIC defectuosa o a un bucle de capa 2 en la red.
![[Pasted image 20230703151639.png]]
Un host atrapado en un bucle de capa 2 no está accesible para otros hosts en la red. Además, debido a los constantes cambios en su tabla de direcciones MAC, el conmutador no sabe desde qué puerto reenviar las tramas de unidifusión.
## El algoritmo de árbol de expansión
STP se basa en un algoritmo inventado por Radia Perlman mientras trabajaba para Digital Equipment Corporation, y publicado en el artículo de 1985 "Un algoritmo para la computación distribuida de un árbol de expansión en una LAN extendida". Su algoritmo de árbol de expansión (STA) crea una topología sin bucles al seleccionar un único puente raíz donde todos los demás conmutadores determinan una única ruta de menor costo.
## Pasos para una topología sin bucles
Usando STA, STP crea una topología sin bucles en un proceso de cuatro pasos:
1. Elige el puente raíz.
2. Seleccione los root ports.
3. Elegir puertos designados.
4. Seleccione puertos alternativos (bloqueados).
Durante las funciones STA y STP, los conmutadores utilizan unidades de datos de protocolo de puente (BPDU) para compartir información sobre sí mismos y sus conexiones. Las BPDU se utilizan para elegir el root bridge, los root ports, los puertos designados y los puertos alternativos. Cada BPDU contiene una ID de puente (BID) que identifica qué switch envió la BPDU. El BID participa en la toma de muchas de las decisiones STA, incluidos los roles de puertos y root bridge. El BID contiene un valor de prioridad, la dirección MAC del conmutador y un ID de sistema extendido. El valor de BID más bajo lo determina la combinación de estos tres campos.
los 12 bits vienen contenidos la VLAN ID
![[Pasted image 20230703152409.png]]
### **Prioridad de puente**
El valor de prioridad predeterminado para todos los switches Cisco es el valor decimal 32768. El rango va de 0 a 61440 y aumenta de a 4096. Es preferible una prioridad de puente más baja. La prioridad de puente 0 prevalece sobre el resto de las prioridades de puente.
### **Sistema extendido ID**
El valor de ID del sistema extendido es un valor decimal agregado al valor de prioridad del puente en el BID para identificar la VLAN para esta BPDU.
El ID del sistema extendido permite que las implementaciones posteriores de STP, como Rapid STP (RSTP) tengan diferentes root bridge para diferentes conjuntos de VLAN. Esto puede permitir que enlaces redundantes y sin reenvío en una topología STP para un conjunto de VLAN sean utilizados por un conjunto diferente de VLAN que utilice un root bridge diferente.
### **Dirección MAC**
Cuando dos switches están configurados con la misma prioridad y tienen la misma ID de sistema extendido, el switch que posee la dirección MAC con el menor valor, expresado en hexadecimal, tendrá el menor BID.

## Pasos 
### 1. Elige el root bridge

El STA designa un único switch como root bridge y lo utiliza como punto de referencia para todos los cálculos de rutas. Los switches intercambian BPDU para crear la topología sin bucles comenzando con la selección del root bridge.

Un proceso de elección determina el switch que se transforma en el puente raíz.

Todos los switches del dominio de difusión participan del proceso de elección. Una vez que el switch arranca, comienza a enviar tramas BPDU cada dos segundos
El switch que tiene el BID más bajo se convierte en el puente raíz. Al principio, todos los conmutadores se declaran a sí mismos como el puente raíz con su propio BID establecido como ID raíz. Eventualmente, los switches aprenden a través del intercambio de BPDU qué switch tiene el BID más bajo y acordarán un puente raíz.
![[Pasted image 20230703153038.png]]
#### Impacto de las pujas por defecto

Dado que el BID predeterminado es 32768, es posible que dos o más switches tengan la misma prioridad. En este escenario, donde las prioridades son las mismas, el conmutador con la dirección MAC más baja se convertirá en el puente raíz. Para asegurar que el puente raíz elegido cumpla con los requisitos de la red, se recomienda que el administrador configure el switch de puente raíz deseado con una prioridad menor.![[Pasted image 20230703153137.png]]
#### Determinar el costo de la ruta raíz

el STA comienza el proceso para determinar las mejores rutas hacia el puente raíz desde todos los destinos en el dominio de difusión. La información de la ruta, conocida como el costo interno de la ruta raíz, está determinada por la suma de todos los costos de los puertos individuales a lo largo de la ruta desde el conmutador hasta el puente raíz.
Los costos de los puertos predeterminados se definen por la velocidad a la que funcionan los mismos. La tabla muestra los costos de puerto predeterminados sugeridos por IEEE. Los switches Cisco utilizan de forma predeterminada los valores definidos por el estándar IEEE 802.1D
![[Pasted image 20230703153759.png]]
### 2. Elegir los puertos raíz
Después de determinar el puente raíz, se utiliza el algoritmo STA para seleccionar el puerto raíz. Cada switch que no sea root seleccionará un puerto raíz. El puerto raíz es el puerto más cercano al root bridge en términos de costo general para el puente raíz.
El costo interno de la ruta raíz es igual a la suma de todos los costos del puerto a lo largo de la ruta al root bridge, como se muestra en la figura. Las rutas con el costo más bajo se convierten en las preferidas, y el resto de las rutas redundantes se bloquean
![[Pasted image 20230703153936.png]]
### 3. Seleccionar puertos designados
La parte de prevención de bucles del árbol de expansión se hace evidente durante estos dos pasos siguientes. Después de que cada switch selecciona un puerto raíz, los switches seleccionarán los puertos designados.

Cada segmento entre dos switches tendrá un puerto designado. El puerto designado es un puerto en el segmento (con dos switches) que tiene el costo de ruta raíz interna al puente raíz. En otras palabras, el puerto designado tiene la mejor ruta para recibir el tráfico que conduce al puente raíz.
#### **Puertos designados en el puente raíz**
Todos los puertos en el root bridge son puertos designados. Esto se debe a que el root bridge tiene el costo más bajo para sí mismo.
![[Pasted image 20230703154127.png]]
#### **Puerto designado cuando hay un puerto raíz**
Si un extremo de un segmento es un puerto raíz, el otro extremo es un puerto designado. Para demostrar esto, la figura muestra que el conmutador S4 está conectado a S3. La interfaz Fa0/1 en S4 es su puerto raíz porque tiene la mejor y única ruta al root bridge.
![[Pasted image 20230703154217.png]]
#### **Puerto designado cuando no hay puerto raíz**
Esto deja solo segmentos entre dos switches donde ninguno de los switches es el puente raíz. En este caso, el puerto del switch con la ruta de menor costo al puente raíz es el puerto designado para el segmento.
![[Pasted image 20230703154242.png]]
### 4. Seleccionar puertos alternativos (bloqueados)

Si un puerto no es un puerto raíz o un puerto designado, se convierte en un puerto alternativo (o de copia de seguridad). Los puertos alternativos y los puertos de respaldo están en estado de descarte o bloqueo para evitar bucles.
![[Pasted image 20230703154312.png]]
### Seleccione un puerto raíz a partir de varias rutas de igual coste
usando un switch tiene varias rutas de igual costo al puente raíz, el switch determinará un puerto utilizando los siguientes criterios:
1. Oferta de remitente más baja
2. Prioridad de puerto del remitente más baja
3. ID de puerto del remitente más bajo
#### **1. Oferta de remitente más baja**
![[Pasted image 20230703154603.png]]
#### **2. Prioridad de puerto del remitente más baja**
![[Pasted image 20230703154707.png]]
#### **3. ID de puerto del remitente más bajo**
![[Pasted image 20230703154741.png]]
## Temporizadores STP y Estados de puerto

- **Temporizador de saludo** - El tiempo de saludo es el intervalo entre BPDU. El valor predeterminado es 2 segundos, pero se puede modificar entre 1 y 10 segundos.
- **Temporizador de retardo de reenvío** - El retraso directo es el tiempo que se pasa en el estado de escucha y aprendizaje. El valor predeterminado es 15 segundos, pero se puede modificar a entre 4 y 30 segundos.
- **Temporizador de antigüedad máxima** - La antigüedad máxima es la duración máxima de tiempo que un switch espera antes de intentar cambiar la topología STP. El valor predeterminado es 20 segundos, pero se puede modificar entre 6 y 40 segundos.

STP facilita la ruta lógica sin bucles en todo el dominio de difusión. El árbol de expansión se determina a través de la información obtenida en el intercambio de tramas de BPDU entre los switches interconectados.
![[Pasted image 20230703155051.png]]
![[Pasted image 20230703155138.png]]
## Detalles Operativos de cada Estado Portuario
![[Pasted image 20230703155155.png]]
## Per-VLAN Spanning Tree
STP se puede configurar para que funcione en un entorno con varias VLAN.
In Per-VLAN Spanning Tree (PVST) versions of STP, there is a root bridge elected for each spanning tree instance. Esto hace posible tener diferentes puentes raíz para diferentes conjuntos de VLAN. STP opera una instancia independiente de STP para cada VLAN individual. Si todos los puertos de todos los switches pertenecen a la VLAN 1, solo se da una instancia de árbol de expansión.

## Diferentes versiones de STP
![[Pasted image 20230703160305.png]]
Los switches de Cisco con IOS 15.0 o posterior ejecutan PVST+ de manera predeterminada. Esta versión incluye muchas de las especificaciones IEEE 802.1D-2004, como puertos alternativos en lugar de los puertos no designados anteriores

## Conceptos de RSTP
RSTP aumenta la velocidad del recálculo del árbol de expansión cuando cambia la topología de la red de Capa 2. RSTP puede lograr una convergencia mucho más rápida en una red configurada en forma adecuada, a veces sólo en unos pocos cientos de milisegundos. Si un puerto está configurado como puerto alternativo o de respaldo, puede cambiar automáticamente al estado de reenvío sin esperar a que converja la red.
## Estados de puerto RSTP y roles de puerto
### **Estados de puertos STP y RSTP**
Solo hay tres estados de puerto en RSTP que corresponden a los tres estados operativos posibles en STP. Los estados de desactivación, bloqueo y escucha 802.1D se fusionan en un único estado de descarte 802.1w.
![[Pasted image 20230703161010.png]]

### **Estados de puertos STP y RSTP**
 hay dos roles de puerto RSTP que corresponden al estado de bloqueo de STP. En STP, un puerto bloqueado se define como no ser el puerto designado o raíz. RSTP tiene dos funciones de puerto para este propósito.
![[Pasted image 20230703161042.png]]
### **Puertos RSTP alternativos y de copia de seguridad**
![[Pasted image 20230703161102.png]]
el puerto alternativo tiene una ruta alternativa al puente raíz. El puerto de copia de seguridad es una copia de seguridad en un medio compartido, como un concentrador. Un puerto de copia de seguridad es menos común porque ahora los concentradores se consideran dispositivos heredados.

## PortFast y protección BPDU

Cuando un dispositivo está conectado a un puerto del conmutador o cuando un conmutador se enciende, el puerto del conmutador pasa por los estados de escucha y aprendizaje, esperando cada vez que expire el temporizador de retardo de reenvío.
Cuando un puerto de conmutador se configura con PortFast, ese puerto pasa del bloqueo al estado de reenvío inmediatamente, omitiendo los estados de escucha y aprendizaje STP y evitando un retraso de 30 segundos. Use PortFast en los puertos de acceso para permitir que los dispositivos conectados a estos puertos, como los clientes DHCP, accedan a la red de inmediato, en lugar de esperar a que STP converja en cada VLAN. Debido a que el propósito de PortFast es minimizar el tiempo que los puertos de acceso deben esperar a que el árbol de expansión converja, solo debe usarse en los puertos de acceso
![[Pasted image 20230703161405.png]]
En una configuración de PortFast válida, nunca se deben recibir BPDU, ya que esto indicaría que hay otro puente o switch conectado al puerto, lo que podría causar un bucle de árbol de expansión. Esto potencialmente causa un bucle de árbol de expansión.
Para evitar que se produzca este tipo de escenario, los switches Cisco admiten una función llamada guardia BPDU.
Para evitar que se produzca este tipo de escenario, los switches Cisco admiten una función llamada guardia BPDU.
## Alternativas a STP
Aunque es muy probable que STP siga utilizándose como mecanismo de prevención de bucles en la empresa, en los conmutadores de capa de acceso también se están utilizando otras tecnologías, incluidas las siguientes:
Agregación de enlaces de
- Múltiples sistemas (MLAG)
- Puente de ruta más corta (SPB)
- Interconexión transparente de muchos enlaces. (TRILL)

STP era y sigue siendo un protocolo de prevención de bucles Ethernet. A lo largo de los años, las organizaciones requerían una mayor resiliencia y disponibilidad en la LAN. Las LAN Ethernet pasaron de unos pocos conmutadores interconectados conectados conectados a un único enrutador, a un sofisticado diseño de red jerárquica que incluye conmutadores de acceso, distribución y capa central, como se muestra en la figura.
![[Pasted image 20230703161744.png]]
Dependiendo de la implementación, la capa 2 puede incluir no solo la capa de acceso, sino también la distribución o incluso las capas principales. Estos diseños pueden incluir cientos de switches, con cientos o incluso miles de VLAN. STP se ha adaptado a la redundancia y complejidad añadida con mejoras, como parte de RSTP y MSTP.
Un aspecto importante del diseño de red es la convergencia rápida y predecible cuando se produce un error o un cambio en la topología. El árbol de expansión no ofrece las mismas eficiencias y predecibilidades proporcionadas por los protocolos de enrutamiento en la Capa 3. La figura muestra un diseño de red jerárquica tradicional con los conmutadores multicapa de distribución y núcleo que realizan enrutamiento.
La topología de red física muestra cuatro conmutadores de capa 3, tres conmutadores de capa 2 y seis PC. Dos switches de capa 3 en la parte superior de la topología están en el núcleo. Dos switches de capa 3 están en la capa de distribución. Los tres conmutadores de capa 2 y los seis equipos están en la capa Access.

![[Pasted image 20230703161826.png]]
El enrutamiento de capa 3 permite rutas y bucles redundantes en la topología, sin bloquear puertos. Por esta razón, algunos entornos están en transición a la capa 3 en todas partes, excepto donde los dispositivos se conectan al conmutador de capa de acceso. En otras palabras, las conexiones entre los conmutadores de capa de acceso y los conmutadores de distribución serían Capa 3 en lugar de Capa 2, como se muestra en la siguiente figura.
![[Pasted image 20230703161855.png]]

en 
conf t
int range f0/1-24
sw mode acc
sw  acc vlan 10
vlan 10
name videojuegos

*Relacionado con:* [[EthernetChannel]]
