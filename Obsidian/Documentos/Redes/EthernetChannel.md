![[Pasted image 20230628090704.png]]

es una tecnología de Cisco que permite combinar múltiples enlaces físicos entre dos dispositivos de red en una única interfaz lógica
Esto proporciona mayor ancho de banda, redundancia y balanceo de carga
Deben tener la misma interfaz y deben estar a la misma velocidad
proporciona tolerancia a fallos. Si uno o más enlaces individuales en el grupo fallan, el tráfico se redistribuye automáticamente a través de los enlaces restantes, evitando interrupciones en la conectividad
el balanceo de carga es una técnica utilizada en redes de computadoras para distribuir equitativamente el tráfico o la carga de trabajo entre múltiples recursos o enlaces de red. Proporciona una mejor utilización de los recursos, mayor rendimiento y disponibilidad, y es esencial en entornos de red con alta demanda de tráfico o sistemas críticos.

to (utx velocidad mbps) Base(Base band) Tx(twisted pair)

deben permitar las mismas vlan tambien debe estar en el mismo tipo de comunicacion

solo pueden haber 6 configuarionces(port channel) y 8 enlaces en cada port channel

uso de enlace compartida se divide por varios trozos y se va por cada uno de los trozos

en el balanceo de carga se va por varios enlaces tomando en cuenta el trafico
## **<font color="#5f497a"> Se ayuda de dos protocolas PAGP (agregacion) LACP(link agregation control protocol) ON (agregacion manual) </font>**

### **PAGP**

es permitir la creación dinámica de grupos de enlaces físicos (puertos) para formar una interfaz lógica de mayor capacidad y proporcionar redundancia y balanceo de carga. Al utilizar PAgP, los dispositivos Cisco intercambian mensajes para negociar y establecer el grupo de enlaces.

Las interfaces forman el canal de manera manual sin mandar mensajes pagp

en el modo desseable esta en modo negociacion mensajes de pagp debe existir siempre interfaces en modo deseable para que se establesca la conexion

no se puede establecer conexion entre el modo manual y automantico
![[Pasted image 20230628091026.png]]
### **LACP**

permite agrupar varios puertos físicos para formar un único canal lógico. LACP permite que un switch negocie un grupo automático mediante el envío de paquetes LACP al otro switch
![[Pasted image 20230628091056.png]]
Este es un protocolo estandar el otro es propietario de cisco

se necesita en modo troncal para conectar los portchannel

solo funcionan entre routers switch y servidor

**mostrar una única línea de información por canal de puertos**

```jsx
sh ethernetchannel summary
```

**muestra el estado general de la interfaz de canal de puerto**

```jsx
sh interfaces port-channel
```

**mostrar información sobre la interfaz del canal de puertos específica**

```jsx
show etherchannel port-channel
```

**crea la interfaz port channel**

```jsx
channel-group number  mode  (lacp(on,active,pasive),pagp(ON,desireable,auto))
```

**configuro la interfaz port channel**

```jsx
int port-channel number
```

```jsx
sw mode (acces,trunk)
```

## **Common Issues**

deben tener la misma configuración de velocidad y modo dúplex, de VLAN nativas y permitidas en los enlaces troncales, y de VLAN de acceso en los puertos de acceso

DTP se usa para automatizar la creación de enlaces troncales.



*Relacionado con:* [[STP (Protocolo de árbol de extensión)]] 
[[VLAN]]
