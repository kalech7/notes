 es un protocolo de routing de estado de enlace como alternativa del vector distancia (RIP,OSPF)
 el protocolo de routing sin clase que utiliza el concepto de areas para realizar escalabilidad.se puede dividir el dominio de enrutamiento en areas distintas que ayudan a controlar el trafico de actualozacion de enrutamiento 
 todos los protocolos de routin comparten componentes similares todos usan mensajes de protocolo de routing para intercambiar informacion de la ruta 
 **Tienen 5 tipos de paquetes:**
 - paquete de saludo 
 - paquete de descripcion de la base de datos
 - paquete de solicitud de estado de enlace 
 - paquete de actualizacion e estado de enlace 
 - paquete de acuse de recibo de estado de enlace 
 
 | base de datos           | tabla              | descripcion                                                                                                                                                                                                                                          |
 | ----------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
 | Adyacencia              | tabla de vecinos   | - lista de todos los routers vecinos con los que un router establecio comunicacion bidireecional<br>-es unica para cada router<br> <br>-show ip ospf neighbor                                                                                        |
 | estado de enlace (LSDB) | Tabla de topologia | Muestra información sobre todos los otros routers en la red <br><br> Esta base de datos representa la topología de la red<br><br> Todos los routers dentro de un área tienen LSDB idénticas<br><br> Se puede ver con elcomando show ip ospf database |
 |Datos de reenvio    |   tabla de routing    |   Lista de rutas generada cuando se ejecuta un algoritmo en la base de datos de estado de enlace.<br><br> La tabla de routing de cada router es única y contiene información sobre cómo y dónde enviar paquetes para otros routers.<br><br> Se puede ver con el comando show ip route.  

El router arma la tabla de topología; para ello, utiliza los resultados de cálculos realizados a partir del algoritmo SPF (Primero la ruta más corta) de Dijkstra. El algoritmo SPF se basa en el costo acumulado para llegar a un destino.
El algoritmo SPF crea un árbol SPF posicionando cada router en la raíz del árbol y calculando la ruta más corta hacia cada nodo. Luego, el árbol SPF se usa para calcular las mejores rutas. OSPF coloca las mejores rutas en la base de datos de reenvío, que se usa para crear la tabla de routing.
## Operación Link-State
los routers OSPF realizan el siguiente proceso genérico de routing de estado de enlace para alcanzar un estado de convergencia:
1. Establecimiento de adyacencias de vecinos
2. Intercambio de anuncios de estado de enlace
3. Crear la base de datos de estado de vínculo
4. Ejecución del algoritmo SPF
5. Elija la mejor ruta

### OSPF de area unica 
todos los routers estan en un area la mejor practica es usar area 0

### Multiarea OSPF 
OSPF se imprementa mediante varias areas de manera jerarquica todas las areas deben conectarse al area trolcal (area 0)  Los routers que interconectan las áreas se denominan “routers fronterizos de área” (ABR).

- **Tablas de enrutamiento más pequeñas:** las tablas son más pequeñas porque hay menos entradas de tabla de enrutamiento. Esto se debe a que las direcciones de red se pueden resumir entre áreas. La sumarización de ruta no está habilitada de manera predeterminada.
- **Sobrecarga de actualizaciones de estado de enlace reducida**  multiárea con áreas más pequeñas minimiza el procesamiento y los requisitos de memoria.
- **Menor frecuencia de cálculos de SPF**  localiza el impacto de un cambio de topología dentro de un área. Por ejemplo, minimiza el impacto de las actualizaciones de routing debido a que la saturación con LSA se detiene en el límite del área.

## OSPFv3
es el equivalente a OSPFv2 para intercambiar prefijos IPv6
intercambia información de routing para completar la tabla de routing de IPv6 con prefijos remotos.
utiliza IPv6 como transporte de la capa de red, por lo que se comunica con peers OSPFv3 y anuncia rutas IPv6. OSPFv3 también utiliza el algoritmo SPF como motor de cómputo para determinar las mejores rutas a lo largo del dominio de routing
Los procesos y las operaciones son básicamente los mismos que en el protocolo de routing IPv4, pero se ejecutan de forma independiente. 

## Paquetes de OSPF
1. Hola
2. Descriptores de bases de datos (DBD)
3. solicitud de link-state (LSR)
4. Actualización de link-state (LSU)
5. Acuse de recibo de estado de enlace (LSAck)
![[Pasted image 20231114001414.png]]
### Actualizaciones de estado de enlace
Los paquetes LSU también se usan para reenviar actualizaciones de routing OSPF. Un paquete LSU puede contener 11 tipos de LSA OSPFv2 OSPFv3 cambió el nombre de varias de estas LSA y también contiene dos LSA adicionales.
LSU y LSA a menudo se utilizan indistintamente, pero la jerarquía correcta es que los paquetes LSU contienen mensajes LSA
![[Pasted image 20231114002249.png]]

### paquete de saludo
OSPF de tipo 1 es el paquete de saludo. Los paquetes Hello se utilizan para hacer lo siguiente:
1. Descubrir vecinos OSPF y establecer adyacencias de vecinos.
2. Publicar parámetros en los que dos routers deben acordar convertirse en vecinos.
3. Elige el router designado (DR) y el router designado de respaldo (BDR) en redes multiacceso, como Ethernet. Los enlaces punto a punto no requieren DR o BDR.
![[Pasted image 20231114002230.png]]
## Funcionamiento de OSPF
![[Pasted image 20231114002348.png]]
![[Pasted image 20231114002357.png]]
### Establecimiento de adyacencias de vecinos
Para determinar si hay un vecino OSPF en el vínculo, el router envía un paquete Hello que contiene su ID de router fuera de todas las interfaces habilitadas para OSPF. El paquete Hello se envía a la dirección de multidifusión IPv4 224.0.0.5 reservada- Todos los routers OSPF. Sólo los enrutadores OSPFv2 procesarán estos paquetes. 
El proceso OSPF utiliza la ID del router OSPF para identificar cada router en el área OSPF de manera exclusiva. La ID de router es un número de 32 bits con formato similar a una dirección IP que se asigna para identificar un router de forma exclusiva entre pares OSPF.
Cuando un router vecino con OSPF habilitado recibe un paquete de saludo con una ID de router que no figura en su lista de vecinos, el router receptor intenta establecer una adyacencia con el router que inició la comunicación.
![[Pasted image 20231114002503.png]]
## Sincronizacion de las bases de datos OSPF 
despues del estado two-way los routers pasan a los estados de sincronizacion de bases de datos
- decidir primer router
- DBDs de Exchange tantos como sea necesario para transmitr la base de datos. el otro router debe reconocer cada dbd con un paquete Lsack
- enviar un LSR cada router comprar la informacion DND con el LSDB local si el paquete DBD tiene una entrada de estado de enlace mas actual,el router pasa al estado loading
---
despues de cumplir con todas las LSR para un router determinado los routers adyacentes se considerena sincronizados y en estado full. se envian actualizaciones (LSU)
- cuando se percive un cambio (actualizaciones incrementales)
- cada 30 min
## la necesidad de una recuperacion ante desastres
las redes multiacces pueden crear dos restos para OSPF en relacion con la saturacion de LSA
- creacion de varias adyacencias: las redes ethernet podrian interconectar muchos rotuers OSPF con un enlace comun . La creacion de varias adyacencias con cada router conduciria al intercambio de una cantidad excesitva de LSA entre routers de la misma red
- Saturacion intensa con LSA  Los routers de estado de enlace saturan con sus LSA cada vez que se inicializa OSPF  o cuando se produce un cmabio en la topologia. la saturacion puede ser excesiva
![[Pasted image 20231115163602.png]]

## LSA inundacion con DR
* Un aumento en el número de routers en una red multiacceso también aumenta el número de LSA intercambiados entre los routers. Esta inundación de LSA afecta significativamente el funcionamiento de OSPF.
* Si cada router en una red multiacceso tuviera que saturar y reconocer todas las LSA recibidas a todos los demás routers en la misma red multiacceso, el tráfico de la red se volvería bastante caótico.
* En las redes multiacceso, OSPF elige un DR como punto de recolección y distribución de las LSA enviadas y recibidas. También se elige un BDR en caso de que falle el DR. Todos los otros routers se convierten en DROTHER. Un DROTHER es un router que no funciona como DR ni como BDR.
*Nota:  El DR se utiliza solo para la transmisión de LSA. El router seguirá usando el mejor router de siguiente salto indicado en la tabla de routing para el reenvío de los demás paquetes.* 

## Configuracion 
### OSPF en una sola area 

```cisco
ospf process-id global 
```


```cisco
router-id id-value 
int loopback (number) 
ip add (ip)(mask)
network ip-address wildcard-mask area area-id 
```
### OSPF multiarea 





## Resumen 

protocolos de enrotamiento EGP y IGP (comprende link state y distance vector)
distance vector (se basa en la cantidad de saltos de un lugar A a un luga B)

link state (estados de los links) va a describir como son todas sus conexiones esto va aformar una base de datos para tomar desciones 

Ospf separa por areas de backbone

## Notas relacionadas
- [[Enrutamiento]]
- [[estado de enlace]]
- [[Vector distancia]]
