**<font color="#c3d69b">RA</font>(Router advertisement)**  sugieren a los hosts cómo obtener su información de direccionamiento IPv6.
<font color="#00b050">Un flag</font> indica configuración automática de direcciones
**<font color="#ffc000">M flag</font> (Managed Address)** indica utilizar servidor DHCPv6 stateful para obtener una GUA IPv6
**<font color="#31859b">O flag</font> (Other)** indica que esta  disponible desde un servidor DHCPv6 stateless.


---
El método SLAAC permite a los hosts crear su propia dirección única global IPv6 sin los servicios de un servidor DHCPv6.

SLAAC es un servicio stateless. Esto significa que no hay ningún servidor que mantenga información de direcciones de red para saber qué direcciones IPv6 se están utilizando y cuáles están disponibles.

Un host también puede enviar un mensaje Router Solicitation (RS) solicitando que un router habilitado para IPv6 envíe al host un RA.
SLAAC se puede implementar como SLAAC solamente, o SLAAC con DHCPv6.
## Activacion de SLAAC
![[Pasted image 20230705173240.png]]
#### **Verificar direcciones ipv6**
Como se destaca, a R1 se le han asignado las siguientes direcciones IPv6:
- **Link-local IPv6 address** - fe80::1
Se requiere para nada dispositivo con IPv6 y se usa para comunicarse con otros dispositivos en el mismo enlace local son enrutables y estan confinadas a un unico enlace 
se configuran automanticamnete siemrpe que el protocolo IPv6 habilitado en la interfaz sin necesidad del operador 
siempre se requiere que haya link local porque depende del funiconamiento de ipv6 
comunicacion entre vecinos NDP (neighbor discovery protocol)
- **GUA and subnet** - 2001:db8:acad:1: :1 y 2001:db8:acad:1: :/64
- **IPv6 all-nodes group** - ff02::1
#### Habilitar enrutamiento IPv6
Aunque la interfaz del router tiene una configuración IPv6, todavía no está habilitada para enviar RA que contengan información de configuración de direcciones a hosts que utilicen SLAAC.
Para habilitar el envío de mensajes RA, un router debe unirse al grupo de todos los routers IPv6 mediante el comando **ipv6 unicast-routing** global config
#### Verificar que slaac este habilitado
El grupo de todos los routers IPv6 responde a la dirección de multidifusión IPv6 ff02 :: 2. Puede utilizar el **show ipv6 interface** comando para verificar si un router está habilitado

## Método Sólo SLAAC
El método sólo SLAAC está habilitado de forma predeterminada cuando se configura el 
**ipv6 unicast-routing** comando

El **A = 1** flag sugiere al cliente que cree su propio IPv6 GUA usando el prefijo anunciado en la RA.
Los flags **O =0** y **M=0** le indican al cliente que use la información del mensaje RA exclusivamente. Esto incluye información del prefijo, de la longitud de prefijo, del servidor DNS, de la MTU y del default gateway


Relacionado con: [[DHCP IPV6]]
