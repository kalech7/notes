Para utilizar la configuración automática de direcciones stateless (SLAAC) o DHCPv6, debe revisar las direcciones globales de unidifusión (GUA) y las direcciones link-local (LLAs).

En un router, una dirección global de unidifusión (GUA) IPv6 se configura manualmente mediante el comando de configuración :

**ipv6 address** _ipv6-address_**_/_**_prefix-length_ interface.
## **IPv6 GUA Assingment**

- fue diseñado para simplificar la forma en que un host puede adquirir su configuración IPv6
    
- Todos los métodos stateless y stateful de este módulo utilizan mensajes de RA ICMPv6 para sugerir al host cómo crear o adquirir su configuración IPv6
    
- se puede asignar dinámicamente utilizando servicios stateless y stateful, como se muestra en la figura
- ![[Screenshots/image 1.png]]
En slaac no se necesia una servidor dhcp
![[Pasted image 20230827223734.png]]

## **Tres flags de mensaje RA**

- **Un flag** - Este es el indicador de configuración automática de direcciones. Usa Stateless Address Autoconfiguration (SLAAC) para crear un GUA de IPv6.
    
- **O flag** - Este es otro indicador de configuración (Other) Otra información está disponible desde un servidor DHCPv6 stateless.
    
- **M flag** - Este es es indicador Managed Address. Utilice un servidor DHCPv6 stateful para obtener una GUA IPv6.
 ![[Pasted image 20230827224304.png]]

## Pasos para habilitar SLAAC

1. asignar una direccion ipv6 a la int del router
```
int g0/0

ipv6 address (dir ipv6)

no shut
```
2. Habilitar el enrutamineto de ipv6
```
ipv6 unicast-routing
```

3. verficamos que SLAAC esta activado

```
ipv6 unicast-routing
```
Si se presenta como en la captura slaac esta activado
![[Screenshots/image 1.png]]

## **Método Sólo SLAAC**

está habilitado de forma predeterminada cuando se configura el **ipv6 unicast-routing** comando.

El **A = 1** flag sugiere al cliente que cree su propio IPv6 GUA usando el prefijo anunciado en la RA. El cliente puede crear su propio ID de interfaz utilizando el método Extended Unique Identifier (EUI-64) o hacer que se genere aleatoriamente.

Los flags **O =0** y **M=0** le indican al cliente que use la información del mensaje RA exclusivamente.

### Preguntas SLAAC
![[image 1 1.png]]\

## **DHCP Puertos**

El servidor DHCP opera en el puerto UDP 67, y el cliente DHCP opera en el puerto UDP 68.

## **Pasos de operación DHCPv6**

DHCPv6 stateless y stateful DHCPv6 stateless utiliza partes de SLAAC para asegurarse de que toda la información necesaria se suministra al host. DHCPv6 stateful no requiere SLAAC.

- Paso 1. El host envía un mensaje RS.
    ![[Pasted image 20230827224529.png]]
    
- Paso 2. El router responde con un mensaje RA.
    ![[Pasted image 20230827224538.png]]
    
- Paso 3. El host envía un mensaje DHCPv6 SOLIT.
    ![[Pasted image 20230827224547.png]]
    
- Paso 4. El servidor DHCPv6 responde con un mensaje ADVERTISE.
    ![[Pasted image 20230827224555.png]]
    
- Paso 5. El host responde al servidor DHCPv6.
    ![[Pasted image 20230827224604.png]]
    
- Paso 6. El servidor DHCPv6 envía un mensaje REPLY
    ![[Pasted image 20230827224614.png]]
    

## **Habilitar DHCPv6 stateless en una interfaz**

DHCPv6 Stateless está habilitado en una interfaz de router mediante el comando

```cisco
ipv6 nd other-config-flag
```

Esto establece el flag O en 1.

![[image 2.png]]


El resultado resaltado confirma que la RA le indicará a los hosts receptores que usen la configuración automática stateless (A flag = 1) y se comunique con un servidor DHCPv6 para obtener otra información de configuración (O flag = 1).

## **Habilitar DHCPv6 stateful en una interfaz**

es habilitado en una interfaz de router mediante el comando **ipv6 nd managed-config-flag** interface configuration Esto establece el flag M en 1.

con el comando
```
ipv6 nd prefix default no-autoconfig
```

se utiliza para deshabilitar la configuración automática de direcciones IPv6 en una interfaz.

```cisco
ipv6 dhcp pool (nombre)
```

```cisco
address prefix (direccion ipv6/prefijo)
```


El resultado resaltado en el ejemplo confirma que RA indicará al host que obtenga toda la información de configuración IPv6 de un servidor DHCPv6 (flag M = 1)
![[image 3.png]]
**Nota**: Puede usar el comando **no ipv6 nd managed-config-flag** para devolver la bandera M a su valor predeterminado de 0. El comando **no** **ipv6 nd prefix default no-autoconfig** devuelve la bandera A a su valor predeterminado de 1.
[[DCHPv4]]
[[SLAAC (Stateless Address Autoconfiguration)]]

## Notas relacionadas
- [[DCHPv4]]
- [[SLAAC (Stateless Address Autoconfiguration)]]
- [[VLAN]]
