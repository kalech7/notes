En las diecciones ip privadas no se deben pagar en cambio las direcciones publicas son pagadas ya que permiten el enroutamiento de paquetes a traves del internet 
Para la ip publica se le pide al: 
1) isp  (proveedores de servicios de Internet) luego el isp pide a
2) LACNIC   (Registros Regionales de Internet) luego la lacnic se le pide al IANA 
3) IANA (Autoridad de Asignación de Números de Internet) la IANA registra la dir publica y se le asigna la ip solicitada
Como maximo se puede asignarse a 10 ip publicas 
**Rango de ip de clases:** 

| Clase | rango ips                       |
| ----- | ------------------------------- |
| A     | 0.0.0.0 hasta 127.255.255.255   |
| B     | 128.0.0.0 hasta 191.255.255.255 |
| C      |       192.0.0.0 hasta 223.255.255.255                          |
**Rango para ip privadas:**

| Clase |           rango ips            |
|:-----:|:------------------------------:|
|   A   |   10.0.0.0 - 10.255.255.255    |
|   B   |  172.16.0.0 - 172.31.255.255   |
|   C   | 192.168.0.0 - 192.168.255.255. |

## Red stub
tiene una unica conexion de salida hacia la infraestructura del isp se da en en router de borde 
## NAT
NAT es una técnica que se utiliza para traducir direcciones IP privadas en una red local a una dirección IP pública en el enrutador o dispositivo de conexión a Internet. Esto permite que varios dispositivos en una red local compartan una única dirección IP pública para acceder a Internet. NAT se utiliza comúnmente en redes domésticas y pequeñas empresas para ahorrar direcciones IP públicas, ya que las direcciones IP públicas son limitadas y valiosas.
NAT (Network Address Translation = Traducción de Direcciones de Red) tiene muchos usos, pero el principal es **conservar las direcciones IPv4 públicas**. Esto se logra al permitir que las redes utilicen direcciones IPv4 privadas internamente y al proporcionar la traducción a una dirección pública solo cuando sea necesario.
![[Pasted image 20230816085427.png]]
>*Local=privado*, *Global=publico*
1) Ip publica especifica
2) Ip(pool dir)
### Comando
1) 
```cisco
int (interfaz con dir privado)
ip nat inside 
```
en el ambiente outside inside  Local es la misma afuera de la red 
la parte inside outside Global se va a llenar cuando hagamos peticiones 
Para conectar dos routers de borde su usa el protocolo de BGP(Border Gateway Protocol)
El proceso de nat generalmente siempre inicia desde la red interna pero no siempre

```cisco
show ip nat translations
```
muestra las truducciones de la tabla nat

```cisco
 ip nat inside source static local-ip  global-ip(ip_dada_del_isp)
```
Se establece la traducción estática entre una dirección local interna y la dirrecion publica dada por el isp
### NAT Estatica
se agina una dirección IP pública específica a un dispositivo en una red interna
la signacion es uno a uno
se usa para administrar dispositivos de manera remota o algun servicio 
### NAT Dinamica
Se van asginando a medida de las peticiones que se hagan 
Se usa un pool de direcciones
se deben tener las suficientes direcciones publicas para las diferentes peticiones que realicen los dispositivos porque si no hay los suficientes no pueden realizarse la traduduccion nat al dipositivos que lo requiere
![[Pasted image 20230821233813.png]]

0. Definir interfaces
1. POOL-> direcciones publicas (net mask)
2. Crear las listas de control de acceso (ACLs)-> Identificador usando wildcard
3. Enlazar las ACLs con las pool publicas
no se prensentan en primer momento el ip local y la ip global

### Configuracion

```cisco
ip nat pool (nombre)(ip inicio)(ip final) netmask (mascara)
```
#### Sumarisar  redes
Sumamos las redes que tengan coincidencia si no hay concidencia se coloca 0 ejemplo:
192.168.10.0
192.168.11.0
__________
192.168.0.0

```cisco
access-list (numero) permit/deny (ip permitida) (wildcard)
ip nat inside source list (numero) pool (nombre)
```
#### **Lista de acceso extendida** 
```cisco
ip access-list extended (nombre)
permit ip (dir red)(wildcard) any
```

## Wildcard
tienen la misma estrutura que la mascara de red  pero tienen diferente proposito
en la wilcard (0->coincidencia y 1-> no coincidencia)
indica qué partes de una dirección de IP son relevantes para la ejecución de una determinada acción. Se utilizan para especificar un rango de direcciones de red. Se suelen utilizar con protocolos de enrutamiento (como OSPF) y listas de control de acceso. Al igual que una máscara de subred, una máscara wildcard tiene 32 bits)
 
255.255.255.0 (mascara )
0.     0.    0. 255 (wildcard)
## PAT
PAT es una extensión de NAT que permite traducir no solo las direcciones IP, sino también los números de puerto. En un escenario de PAT, múltiples dispositivos internos en una red comparten la misma dirección IP pública, pero se diferencian por los números de puerto. Esto permite que varios dispositivos internos se comuniquen con recursos externos utilizando diferentes puertos, manteniendo así la distinción de las conexiones.
Es un nat con sobrecarga ademas de traducir las dir ips se traducen los puertos varias direcciones probadas se pueden traducir por una o pocas direcciones publicas para que no exista confucion en la entrega de paquetes se usa el puerto 
es aleatorio la asignacion del puerto en el lado inside en el lado outside se tienen puertos especificos

grupo de puertos 0-511,512-1023 o  1024-65535 de acuerdo a los grupos se va asignando de acuerdo a la disponibilidad 

```cisco
ip nat inside source list (lista) interface (interface) overload
debug ip nat  # todas las traducciones se muestren en tiempo real en el modo global
```

