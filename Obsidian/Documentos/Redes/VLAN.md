Dentro de una red conmutada, las VLAN proporcionan la segmentación y la flexibilidad organizativa. Un grupo de dispositivos dentro de una VLAN se comunica como si cada dispositivo estuviera conectados al mismo cable. Las VLAN se basan en conexiones lógicas, en lugar de conexiones físicas.
Las VLAN permiten que el administrador divida las redes en segmentos según factores como la función, el equipo del proyecto o la aplicación, sin tener en cuenta la ubicación física del usuario o del dispositivo. Cada VLAN se considera una red lógica diferente. Los dispositivos dentro de una VLAN funcionan como si estuvieran en su propia red independiente, aunque compartan una misma infraestructura con otras VLAN. Cualquier puerto de switch puede pertenecer a una VLAN.
Los paquetes de unidifusión, difusión y multidifusión se reenvían solamente a terminales dentro de la VLAN donde los paquetes son de origen.
Una VLAN crea un dominio de difusión lógico que puede abarcar varios segmentos LAN físicos. Las VLAN mejoran el rendimiento de la red mediante la división de grandes dominios de difusión en otros más pequeños
la nic 802.1Q es de vlans
## Tipos de VLAN
### **VLAN predeterminada**
La VLAN predeterminada para los switches Cisco es la VLAN 1.
Entre los datos importantes que hay que recordar acerca de la VLAN 1 se incluyen los siguientes:
- Todos los puertos se asignan a la VLAN 1 de manera predeterminada.
- De manera predeterminada, la VLAN nativa es la VLAN 1.
- De manera predeterminada, la VLAN de administración es la VLAN 1.
- No es posible eliminar ni cambiar el nombre de VLAN 1.
### **VLAN de datos**
Las VLAN de datos son VLAN configuradas para separar el tráfico generado por el usuario. Las VLAN de datos se usan para dividir la red en grupos de usuarios o dispositivos. Una red moderna tendría muchas VLAN de datos en función de los requisitos organizativos. Tenga en cuenta que no se debe permitir el tráfico de administración de voz y red en las VLAN de datos.
### **VLAN nativa**
El tráfico de usuario de una VLAN debe etiquetarse con su ID de VLAN cuando se envía a otro switch. Los puertos troncal se utilizan entre conmutadores para admitir la transmisión de tráfico etiquetado.
Es posible que un switch también tenga que enviar tráfico sin etiqueta a través de un enlace troncal. El tráfico sin etiquetas es generado por un switch y también puede provenir de dispositivos heredados. El puerto de enlace troncal 802.1Q coloca el tráfico sin etiquetar en la VLAN nativa.
### **VLAN de administración**
Una VLAN de administración es una VLAN de datos configurada específicamente para el tráfico de administración de red, incluyendo SSH, Telnet, HTTPS, HHTP y SNMP.
### **VLAN de voz**
Se necesita una VLAN separada para admitir la tecnología de voz sobre IP (VoIP). Para el tráfico de VoIP, se necesita lo siguiente:

- Ancho de banda garantizado para asegurar la calidad de la voz
- Prioridad de la transmisión sobre los tipos de tráfico de la red
- Capacidad para ser enrutado en áreas congestionadas de la red
- Una demora inferior a 150 ms a través de la red

Para cumplir estos requerimientos, se debe diseñar la red completa para que admita VoIP

## Ventajas
![[Pasted image 20230705180558.png]]

## Identificación de VLAN con etiqueta
### **Detalles del campo VLAN Tag**
el campo de etiqueta de la VLAN consta de un campo de tipo, un campo de prioridad, un campo de identificador de formato canónico y un campo de ID de la VLAN:

- **Tipo** - Un valor de 2 bytes denominado “ID de Protocolo de Etiqueta” (TPID). Para Ethernet, este valor se establece en 0x8100 hexadecimal.
- **Prioridad de usuario** - Es un valor de 3 bits que admite la implementación de nivel o de servicio.
- **Identificador de Formato Canónico (CFI)** - Es un identificador de 1 bit que habilita las tramas Token Ring que se van a transportar a través de los enlaces Ethernet.
- **VLAN ID (VID)** - Es un número de identificación de VLAN de 12 bits que admite hasta 4096 ID de VLAN.
![[Pasted image 20230705181010.png]]
### VLAN nativas y etiquetado de 802.1Q
El estándar IEEE 802.1Q especifica una VLAN nativa para los enlaces troncal, que por defecto es VLAN 1. Cuando un marco sin etiqueta llega a un puerto troncal, se asigna a la VLAN nativa.
#### **Marcos etiquetados en la VLAN nativa**
 El tráfico de control que se envía por la VLAN nativa no se debe etiquetar. Si un puerto de enlace troncal 802.1Q recibe una trama etiquetada con la misma ID de VLAN que la VLAN nativa, descarta la trama

#### **Marcos sin etiquetas en la VLAN nativa**
recibe tramas sin etiquetar (poco usuales en las redes bien diseñadas), envía esas tramas a la VLAN nativa. Si no hay dispositivos asociados a la VLAN nativa (lo que es usual) y no existen otros puertos de enlace troncal (es usual), se descarta la trama



















Relacionado con: [[Inter-VLAN]]
[[DCHPv4]]
