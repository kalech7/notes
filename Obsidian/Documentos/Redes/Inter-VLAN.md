Inter-VLA routing es el proceso de reenviar el tráfico de red de una VLAN a otra VLAN.
Hay tres opciones inter-VLAN routing:
- **Inter-VLAN Routing heredado** - Esta es una solución antigua. No escala bien
- **Router-on-a-stick** - Esta es una solución aceptable para una red pequeña y mediana.
- **Switch de capa 3 con interfaces virtuales (SVIs)** : esta es la solución más escalable para organizaciones medianas y grandes.


## Inter-VLAN Routing heredado

Se basó en el uso de un router con múltiples interfaces Ethernet. Cada interfaz del router estaba conectada a un puerto del switch en diferentes VLAN.
![[Pasted image 20230704212348.png]]
Inter-VLAN routing heredado, usa las interfaces fisicas funciona, pero tiene limitaciones significantes. No es razonablemente escalable porque los routers tienen un número limitado de interfaces físicas. Requerir una interfaz física del router por VLAN agota rápidamente la capacidad de la interfaz física del router
## Router-on-a-Stick Inter-VLAN Routing
 Solo requiere una interfaz Ethernet física para enrutar el tráfico entre varias VLAN de una red.
 Las subinterfaces configuradas son interfaces virtuales basadas en software. Cada uno está asociado a una única interfaz Ethernet física. Estas subinterfaces se configuran en el software del router. Cada una se configura de forma independiente con sus propias direcciones IP y una asignación de VLAN.
 ![[Pasted image 20230704213844.png]]
## Inter-VLAN Routing en un switch de capa 3

es utilizar switches de capa 3 e interfaces virtuales del switch (SVI). Una SVI es una interfaz virtual configurada en un switch multicapa, como se muestra en la figura.
![[Pasted image 20230704214121.png]]
Los SVIs entre VLAN se crean de la misma manera que se configura la interfaz de VLAN de administración. El SVI se crea para una VLAN que existe en el switch. Aunque es virtual, el SVI realiza las mismas funciones para la VLAN que lo haría una interfaz de router.
- Es mucho más veloz que router-on-a-stick, porque todo el switching y el routing se realizan por hardware.
- El routing no requiere enlaces externos del switch al router. No se* limitan a un enlace porque los EtherChannels de Capa 2 se pueden utilizar como enlaces troncal entre los switches para aumentar el ancho de banda.
- La latencia es mucho más baja, dado que los datos no necesitan salir del switch para ser enrutados a una red diferente. Se* implementan con mayor frecuencia en una LAN de campus que en routers.

La única desventaja es que los switches de capa 3 son más caros.

## Escenario Router-on-a-Stick
### S1 VLAN and configuraciones de enlaces troncales

**Paso 1**. Crear y nombrar las VLANs.

**Paso 2**. Crear la interfaz de administración

**Paso 3**. Configurar puertos de acceso.

**Paso 4**. Configurar puertos de enlace troncal.![[Pasted image 20230704222147.png]]
### Configuración de subinterfaces de R1
cada subinterfaz se configura con los dos comandos siguientes:
- **encapsulation dot1q** _vlan_id_  - This command configures the subinterface to respond to 802.1Q encapsulated traffic from the specified _vlan-id_. The **native** keyword sólo se agrega para establecer la VLAN nativa en algo distinto de VLAN 1.
- **ip address** _ip-address subnet-mask_ - Este comando configura la dirección IPv4 de la subinterfaz. Esta dirección normalmente sirve como default gateway para la VLAN identificada.
Repita el proceso para cada VLAN que se vaya a enrutar. Es necesario asignar una dirección IP a cada subinterfaz del router en una subred única para que se produzca el routing.
Cuando se hayan creado todas las subinterfaces, habilite la interfaz física mediante el comando de configuración de **no shutdown** interfaz. Si la interfaz física está deshabilitada, todas las subinterfaces están deshabilitadas.


## Inter-VLAN Routing en Switch de capa 3
Las redes empresariales modernas rara vez usan router-on-a-stick porque no se escalan fácilmente para cumplir los requisitos. En estas redes muy grandes, los administradores de red utilizan switches de capa 3 para configurar el inter-VLAN routing.

El inter-VLAN routing. mediante el método router-on-a-stick es fácil de implementar para una organización pequeña y mediana. Sin embargo, una gran empresa requiere un método más rápido y mucho más escalable para proporcionar inter-VLAN routing.
Las capacidades de un switch de capa 3 incluyen la capacidad de hacer lo siguiente:

- Ruta de una VLAN a otra mediante múltiples interfaces virtuales de switch (SVIs).
- Convierta un puerto de switch de capa 2 en una interfaz de capa 3 (es decir, un puerto enrutado). Un puerto enrutado es similar a una interfaz física en un router Cisco IOS.

Para proporcionar enrutamiento entre VLAN, los switches de capa 3 utilizan SVIs. Los SVIs se configuran utilizando el mismo comando **interface vlan** _vlan-id_ utilizado para crear el SVI de administración en un switch de capa 2. Se debe crear un SVI de Capa 3 para cada una de las VLAN enrutables.

## Configuracion de switch de capa 3

**Paso 1**. Crear las VLAN.

```cisco
D1(config)# vlan 10
D1(config-vlan)# name LAN10
D1(config-vlan)# vlan 20
D1(config-vlan)# name LAN20
D1(config-vlan)# exit
D1(config)#
```

**Paso 2**. Crear las interfaces VLAN SVI.
Configurar el SVI para VLANs 10 y 20 Las direcciones IP configuradas servirán como default gateways para los hosts de las VLAN respectivas
```cisco
D1(config)# interface vlan 10 
D1(config-if)# **description Default Gateway SVI for 192.168.10.0/24
D1(config-if)# **ip add 192.168.10.1** **255.255.255.0
D1(config-if)# **no shut
D1(config-if)# **exit
D1(config)# 
D1(config)# **int vlan 20
D1(config-if)# **description Default Gateway SVI for 192.168.20.0/24 
D1(config-if)# **ip add 192.168.20.1 255.255.255.0
D1(config-if)# **no shut
D1(config-if)# **exit
D1(config)#
```

**Paso 3**. Configurar puertos de acceso.

```cisco
D1(config)# interface GigabitEthernet1/0/6 
D1(config-if)# description Access port to PC1 
D1(config-if)# switchport mode access
D1(config-if)# switchport access vlan 10 
D1(config-if)# exit
D1(config)# 
D1(config)# interface GigabitEthernet1/0/18
D1(config-if)#description Access port to PC2
D1(config-if)# switchport mode access 
1(config-if)# switchport access vlan 20 
D1(config-if)# exit
```

**Paso 4**. Habilitar IP routing.
Por último, habilite el enrutamiento IPv4 con el comando de configuración **ip routing** global para permitir el intercambio de tráfico entre las VLAN 10 y 20. Este comando debe configurarse para habilitar el inter-VAN routing en un switch de capa 3 para IPv4.

```cisco
D1(config)# ip routing 
D1(config)#
```

## Problemas comunes de Inter-VLAN routing

En primer lugar, compruebe la capa física para resolver cualquier problema en el que un cable pueda estar conectado al puerto incorrecto. Si las conexiones son correctas, utilice la lista de la tabla para otras razones comunes por las que puede fallar la conectividad entre VLAN.
![[Pasted image 20230704224851.png]]

### VLAN faltantes

Un problema de conectividad entre VLAN podría deberse a la falta de una VLAN. La VLAN podría faltar si no se creó, se eliminó accidentalmente o no se permite en el enlace troncal.

Utilice el **show interface** comando **switchport** _interface-id_ para verificar la pertenencia a VLAN.

### Problemas con el puerto troncal del switch
el enrutamiento entre VLAN incluye puertos de switch mal configurados. En una solución interVLAN heredada, esto podría deberse a que el puerto del router de conexión no está asignado a la VLAN correcta.
Sin embargo, con una solución router-on-a-stick, la causa más común es un puerto troncal mal configurado
### Problemas en los puertos de acceso de switch
utilice los distintos comandos de verificación para examinar la configuración e identificar el problema.

## Temas de configuración del router
Los problemas de configuración del router-on-a-stick suelen estar relacionados con configuraciones incorrectas de la subinterfaz.
Verificó el enlace troncal del switch y todo parece estar en orden. Verificar el estatus de las interfaces usando el **show ip interface brief**

Compruebe en qué VLAN se encuentra cada una de las subinterfaces. Para ello, el **show interfaces** comando es útil, pero genera una gran cantidad de resultados adicionales no requeridos. El resultado del comando se puede reducir utilizando filtros
Compruebe en qué VLAN se encuentra cada una de las subinterfaces. Para ello, el **show interfaces** comando es útil, pero genera una gran cantidad de resultados adicionales no requeridos. El resultado del comando se puede reducir utilizando filtros
*Relacionado con:*  [[Enrutamiento]]
