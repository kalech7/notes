Servicio DHCP  tienes una estrutura cliente/servidor
se necesita  un servidor dedicado para redes grandes y medianas en redes pequeñas se instala en el router de la compañia 
en los routers vienen ya configurados en la asignacion  
se llama arrendamiento el momento que el cliente pide una direccion ip y el servidor asigna una ip la cual esta arrendada que puede ir de 24h a 1 semana o mas dependiendo del administador 
lo proporciona de un pool de direcciones IPv4

nos permite asignar direcciones ip de manera dinamica
Se usa en redes grandes medidas y tambien en pequeñas 

## Origen de arrendamiento
[[dhcpv4.excalidraw]]
### **Paso 1. Detección DHCP (DHCPDISCOVER)**

![[Pasted image 20230628102128.png]]
MAC ORIGEN
MAC DESTINO 
DIR IP ORIGEN
DIR DESTINO
## **Paso 2. Oferta DHCP**
DIR IP  (posible)
MAC  (posible)
TIEMPO ARRENDAMIENTO
DIR IP SERVER DHCP v4
![[Pasted image 20230628102245.png]]
### **Paso 3. Solicitud de DHCP (DHCPREQUEST)**
es un mensaje broadcasta donde dice a todos los servidores que acepto la solicitud
se utiliza para el origen del arrendamiento, el mensaje DHCPREQUEST sirve como notificación de aceptación vinculante al servidor seleccionado para los parámetros que ofreció y como un rechazo implícito a cualquier otro servidor que pudiera haber proporcionado una oferta vinculante al cliente.
![[Pasted image 20230628102635.png]]
## **Paso 4. Confirmación de DHCP (DHCPACK)**
el servidor verifica la información del arrendamiento con un ping ICMP a esa dirección para asegurarse de que no esté en uso, crea una nueva entrada ARP para el arrendamiento del cliente y responde con un mensaje DHCPACK.
![[Pasted image 20230628102730.png]]
## Pasos para renovar un contrato de arrendamiento
## **Detección DHCP (DHCPREQUEST)**
el cliente envía un mensaje DHCPREQUEST directamente al servidor de DHCPv4 que ofreció la dirección IPv4 en primera instancia. Si no se recibe un mensaje DHCPACK dentro de una cantidad de tiempo especificada, el cliente transmite otro mensaje DHCPREQUEST de modo que uno de los otros servidores de DHCPv4 pueda extender el arrendamiento.

## **Ofrecimiento de DHCP (DHCPACK)**
Al recibir el mensaje DHCPREQUEST, el servidor verifica la información del arrendamiento al devolver un DHCPACK.
![[Pasted image 20230628103129.png]]
los dispositivos que deben ser administrados deben ser fijas nunca deben ser propocionadas por dhcp 
## Configuracion
Se deben excluir todas las direcciones ip que tienen direccionamiento manual va en orden

```cisco
ip dhcp excluded-address (dir a excluir)
```
crear el pool con ese identificador 
(solo se le asigna un nombre)
```cisco
ip dhcp pool (nombre)
```
se le especifica el rango de dir ips y el gateway

```cisco
network (dir red) (mask)
default-router (gateway)
dns-server (ip del servidor dns)
```
en el cliente  debe estar asignado la conf automatica 
oara definir la duracion de la consecion dhcp

```cisco
lease {_days_ [_hours_ [ _minutes_]] | infinite}
```
para  definrar el nombre de dominio 

```cisco
domain-name (domain)
```

**Verificar las asignaciones de DHCP**

```cisco
show ip dhcp binding ----Muestra una lista de todos los enlaces de direcciones IPv4 a direcciones MAC proporcionados por el servicio DHCPv4.

show running-config | section dhcp --Muestra los comandos DHCPv4 configurados en el router.

show ip dhcp server statistics --Muestra información de conteo con respecto a la cantidad de mensajes DHCPv4 que han sido enviados y recibidos.
```
## DHCP relay
conocido con El Agente de **retransmisión** sucede cuando hay varios routers  el router inicial es el que ayuda a los demas proporcionando las ips 
sirve para cuando un cliente requiere de una configuración IP utilizando un DHCP Server en la interfaz del router de donde se manda el mensaje
```cisco
ip helper-address (ip de ayuda)
```
![[Pasted image 20230802105235.png]]
![[Pasted image 20230802105245.png]]



### Resumen
![[Pasted image 20230822103529.png]]

**1) D (DISCOVER)**
Se envia primiero un mensaje de tipo discover en el que va intentar descubrir si existe un servidor  dhcp  en la red  para que le ofrezca la informacion necesaria 
Es una forma de decirle a la red que necesito una direccion ip y este mensaje de discover nos interesa que llegue a todos los elementos de la red (broadcast) 
Entonces se mandara en este mensaje el campo mac destino de la trama contendra la direccion de broadcast (ffff.ffff.ffff.ffff) asi la red enviara esta trama a todos los equipos que se encuentren en el mismo segemento de red  
**2) O (OFFER)**
Cuando llegue al servidor dhcp este buscara una ip que tenga libre y respondera con un mensaje dhcp OFFER con toda la configuracion tcp/ip que le ofrece al cliente ademas se le indicara un parametro lease time el cual sirve para indicarle por cuanto tiempo se le concede la direccion ip. Esto se hace porque se necesita reasignar las ips y no ocuparlas eternamente con conscesiones antiguas
Ahora el cliente ya conoce la direccion mac del servidor ya que la aprendido con el mensaje offer 
**3) R (REQUEST)**
el cliente responde con un mensaje dhcp request donde confirma al servidor dhcp que quiere asignarse esta direccion ip concedida. el cliente utiliza la direccion mac destino del servidor ahora se envia una trama del tipo unicast
**4) A (ACKNOLEDGE)**
el servidor responde con un acknoledge confirmando asi la consecion de la direccion ip


Ahora tiene el cliente tedras configuarado de manera automatica una direccion ip y los parametros tcp/ip
[[DHCP IPV6]]

## Notas relacionadas
- [[VLAN]]
- [[Enrutamiento]]
- [[SLAAC (Stateless Address Autoconfiguration)]]
