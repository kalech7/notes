Conocemos como acceder a los modos del switch, como colocar nombres, contraseñas etc.

```cisco
Switch#(config) enable secret myPassword
```
## Acceso local al Switch a traves del **puerto de consola**

Este acceso es desde un dispositivo final.

- Debemos preparar el dispositivo para poder acceder de forma local, queremos acceder a su IOS.
<span style="background:rgba(136, 49, 204, 0.2)"><font color="#ccc1d9">Acceso fuera de banda: El acceso fuera de banda hace referencia a un tipo de acceso por medio de un cable de administración dedicado, este tipo de cable sabe especificamente que no puede enviar y recibir datos de usuarios finales</font></span>
- En este caso el acceso fuera de banda lo realizamos con el **cable de consola o Roll-Over cable** Cable color celeste
- Se conecta desde un puerto **serial (RS-232)** en la Laptop al **Puerto de consola (RJ45)**
- Este puerto se utiliza para configurar el switch de forma local.
- El puerto de consola también se utiliza cuando se caen los servicios de red.
- En la primera ocasión podemos acceder sin configuración previa.
## Acceso Remoto al Switch: Telnet

Partamos de los siguiente:

- No se puede asignar una dirección IP a los puertos del switch.
- Como no puedo asignar una dirección IP a los puertos se la asignaré a una **Interfaz virtual (SVI) que está asociada con una VLAN.**
    - La VLAN a la cual se asociará la SVI **debe existir.**
    - Por lo general la SVI se asocia siempre a la VLAN 1

### Configuración de los servicios de red

Pasos:

1. Activo los servicios de red.
2. Lineas vty
    1. Lineas virtuales de acceso al dispositivo.
    2. Sirven para acceder **remotamente**
    3. Cisco emite hasta 16 lineas vty (0 - 15)
    4. Tienen un uso en funcion al número de administradores. Cada linea puede tener su propia contraseña.
3.  El Servicio remoto debe estar levantado (**TELNET**)
    1. En el switch debe estar levantado el servicio
    2. En el switch cisco, viene por defecto levantado el servicio de Telnet.
    3. Cliente —> PC (Cliente Telnet) ..... Servidor —> Switch (Servicio telnet)
    4. comando: **Telnet (IP de donde me quiero conectar)**
    5. Puedo conectarme de una switch a otro por Telnet. El switch está configurado para trabajar como cliente o servidor.
Levantamos los servicios de red:

```cisco
Switch(config)# interface vlan 1
Switch(config-if)# ip address 192.168.57.10 255.255.255.0 // [Dir Ip] [Mask]
Switch(config-if)# no shutdown // con esto activamos la interfaz
```

Una vez hemos levantado el servicio de red debemos configurar las **Lineas vty**
La VLAN para asociar el SVI debe existir , debe estar creada, por lo general el SVI se asocia siempre a la VLAN 1
## Acceso remoto al Switch : SSH

Partamos de lo siguiente:

- Es un protocolo mucho más seguro que Telnet.
- Proporciona autenticación de contraseña (**Datos viajan encriptados)**
- En la gran mayoria ya viene instalado por defecto.
- El comando es: **ssh -l [admin] [IP]**

```cisco
ssh -l [admin][IP]
```

- En SSH necesitamos 2 tipos de autenticacion es por ello que se usará **login local.**
Levantamos los servicios de red:

```cisco
Switch# configure terminal
Switch(config)# interface vlan 1 
Switch(config-if)# ip adress 192.168.10.2 255.255.255.0
Switch(config-if)# no shutdown
```

**Configuramos el SSH como tal junto a las lineas vty.**


```cisco
Switch# configure terminal
Switch(config)# ip domain-name epn.com
Switch(config)# crypto key generate rsa // Los bits de la clave empiezan de 512 en 512

Switch(config)# username admin secrete my_password
Switch(config-line)# line vty 0 15 
Switch(config-line)# transport input ssh // si usare telnet seria transport input all
Switch(config-line)# login local
Switch(config-line)# exit
Switch(config)# ip ssh version 2
Switch(config)# exit	

```

---

## Acceso remoto al Switch: Auxiliar.
- Forma antigua de acceder a consola de forma remota
- Se prefiere el puerto de consola sobre el auxiliar.

## Notas relacionadas
- [[Comandos para examinar el IOS]]
- [[VLAN]]
- [[STP (Protocolo de árbol de extensión)]]
- [[EthernetChannel]]
- [[Port Security]]
