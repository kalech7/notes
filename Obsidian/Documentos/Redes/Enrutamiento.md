Las **funciones principales** de un router son determinar la mejor ruta para reenviar paquetes basándose en la información de su tabla de enrutamiento, y reenviar paquetes hacia su destino.

La interfaz que usa el router para reenviar el paquete puede ser el destino final o una red conectada a otro router que se usa para llegar a la red de destino.

Las funciones principales de un router son determinar la mejor ruta para reenviar paquetes basándose en la información de su tabla de enrutamiento, y reenviar paquetes hacia su destino.

## Mejor ruta es igual a la coincidencia más larga
La mejor ruta de la tabla de enrutamiento también se conoce como la coincidencia más larga
La coincidencia más larga es un proceso que el router utiliza para encontrar una coincidencia entre la dirección IP de destino del paquete y una entrada de enrutamiento en la tabla de enrutamiento.

Para que haya una coincidencia entre la dirección IPv4 de destino de un paquete y una ruta en la tabla de routing, una cantidad mínima de los bits del extremo izquierdo deben coincidir entre la dirección IPv4 del paquete y la ruta en la tabla de routing.

La máscara de subred de la ruta en la tabla de routing se utiliza para determinar la cantidad mínima de bits del extremo izquierdo que deben coincidir. Recuerde que un paquete IP sólo contiene la dirección IP de destino y no la longitud del prefijo.
### Ejemplo de coincidencia más larga de direcciones IPv4
![[Pasted image 20230702184619.png]]
De las tres rutas, 172.16.0.0/26 tiene la coincidencia más larga y se elige para reenviar el paquete. Recuerde que para que cualquiera de estas rutas se considere una coincidencia debe tener al menos la cantidad de bits coincidentes que se indica en la máscara de subred de la ruta.
### Ejemplo de coincidencia más larga de direcciones IPv6
![[Pasted image 20230702184650.png]]
Las dos primeras entradas de ruta tienen longitudes de prefijo que tienen el número requerido de bits coincidentes como indica la longitud del prefijo. La primera entrada de ruta con una longitud de prefijo de /40 coincide con los 40 bits del extremo izquierdo de la dirección IPv6. La segunda entrada de ruta tiene una longitud de prefijo de /48 y con los 48 bits que coinciden con la dirección IPv6 de destino, y es la coincidencia más larga. La tercera entrada de ruta no coincide porque su prefijo /64 requiere 64 bits coincidentes. Para que el prefijo 2001:db8:c 000:5555: :/64 sea una coincidencia, los primeros 64 bits deben ser la dirección IPv6 de destino del paquete. Solo coinciden los primeros 48 bits, por lo que esta entrada de ruta no se considera una coincidencia.

## Creación de la tabla de enrutamiento
![[Pasted image 20230702193001.png]]
### **Redes conectadas directamente**
son redes que están configuradas en las interfaces activas de un router. Una red conectada directamente se agrega a la tabla de enrutamiento cuando una interfaz se configura con una dirección IP y una máscara de subred (longitud de prefijo) y está activa (arriba y arriba).
### **Redes remotas**
Rutas _**estáticas** : se agrega a la tabla de enrutamiento cuando se configura manualmente una ruta. Protocolos de enrutamiento_ **dinámico** : se han añadido a la tabla de enrutamiento cuando los protocolos de enrutamiento aprenden dinámicamente acerca de la red remota. Estos protocolos incluyen el protocolo de información de routing versión 2 (RIPv2), abrir primero la ruta más corta (OSPF) y el protocolo de routing de gateway interior mejorado (EIGRP).
### **Ruta predeterminada**
Una ruta predeterminada específica un router de salto siguiente que se utilizará cuando la tabla de enrutamiento no contiene una ruta específica que coincida con la dirección IP de destino.
A veces, la ruta predeterminada se conoce como una puerta de enlace de último recurso.
Una ruta predeterminada sobre IPv4 tiene una entrada de ruta de 0.0.0.0/0 y una ruta predeterminada sobre IPv6 tiene una entrada de ruta de: :/0. La longitud del prefijo /0 indica que cero bits o ningún bit deben coincidir con la dirección IP de destino para que se utilice esta entrada de ruta.
## Proceso de decisión de reenvío de paquetes
![[Pasted image 20230702193719.png]]
### **Reenvía el paquete a un dispositivo en una red conectada directamente**
Si la entrada de ruta indica que la interfaz de salida es una red conectada directamente, esto significa que la dirección IP de destino del paquete pertenece a un dispositivo de la red conectada directamente.
Para encapsular el paquete en la trama Ethernet, el router necesita determinar la dirección MAC de destino asociada a la dirección IP de destino del paquete.

- **Paquete IPv4** - El router comprueba su tabla ARP para la dirección IPv4 de destino y una dirección MAC Ethernet asociada. Si no hay coincidencia, el router envía una solicitud ARP. El dispositivo de destino devolverá una respuesta ARP con su dirección MAC. El router ahora puede reenviar el paquete IPv4 en una trama Ethernet con la dirección MAC de destino adecuada.
- **PaqueteIPv6** - El router comprueba su caché vecino para la dirección IPv6 de destino y una dirección MAC Ethernet asociada. Si no hay coincidencia, el router envía un mensaje ICMPv6 Solicitud de vecino (ICMPv6 Neighbor Solicitation) (NS). El dispositivo de destino devolverá un mensaje ICMPv6 Neighbor Advertisement (NA) con su dirección MAC. El router ahora puede reenviar el paquete IPv6 en una trama Ethernet con la dirección MAC de destino adecuada.
### **Reenvía el paquete a un router de salto siguiente**
Si la entrada de ruta indica que la dirección IP de destino está en una red remota el paquete debe ser reenviado a otro enrutador, específicamente a un router de siguiente salto. La dirección de salto siguiente se indica en la entrada de ruta.
### **Descarta el paquete - No coincide en la tabla de enrutamiento**
Si no hay ninguna coincidencia entre la dirección IP de destino y un prefijo en la tabla de enrutamiento, y si no hay una ruta predeterminada, se descartará el paquete.\

## Reenvío de paquetes
principal de la función de switching es la de encapsular los paquetes en el tipo de marco de enlace de datos correcto para el enlace de datos de salida.
### **PC1 envía paquete a PC2**
En la primera animación, PC1 envía un paquete a PC2. Ya que la PC2 está en una red diferente, la PC1 reenviará los paquetes a su puerta de enlace predeterminada (gateway). PC1 buscará en su caché ARP la dirección MAC de gateway predeterminada y agregará la información de trama indicada.
![[Pasted image 20230702205733.png]]
### **El R1 reenvía el paquete a la PC2**
R1 ahora reenvía el paquete a PC2. Debido a que la interfaz de salida se encuentra en una red Ethernet, el R1 debe resolver la dirección IPv4 de siguiente salto con una dirección MAC de destino mediante ARP: Si no existe ninguna entrada ARP para la interfaz del proximo salto 192.168.2.2 en la tabla ARP, R1 envía una solicitud de ARP. R2 devolvería una respuesta ARP.
![[Pasted image 20230702205917.png]]
### **El R2 reenvía el paquete al R3**
R2 ahora reenvía el paquete a R3. Debido a que la interfaz de salida no es una red Ethernet, el R2 no tiene que resolver la dirección IPv4 del siguiente salto con una dirección MAC de destino
Debido a que no hay direcciones MAC en las interfaces seriales, el R2 establece la dirección de destino de enlace de datos en el equivalente a una difusión.
![[Pasted image 20230702210052.png]]
### **El R3 reenvía el paquete a la PC2**
R3 ahora reenvía el paquete a PC2. Dado que la interfaz de salida es una red Ethernet conectada directamente, el R3 debe resolver la dirección IPv4 de destino del paquete con una dirección MAC de destino: Si la entrada no aparece en la caché ARP, el R3 envía una solicitud de ARP por la interfaz FastEthernet 0/0. La PC2 envía a cambio una respuesta ARP con su dirección MAC.
![[Pasted image 20230702210159.png]]
## Mecanismos de reenvío de paquetes
### **Conmutación de procesos (Process Switching)**
Cuando un paquete llega a una interfaz, se reenvía al plano de control, donde la CPU hace coincidir la dirección de destino con una entrada de la tabla de routing y, a continuación, determina la interfaz de salida y reenvía el paquete. Es importante comprender que el router hace esto con cada paquete, incluso si el destino es el mismo para un flujo de paquetes. Este mecanismo de switching de procesos es muy lento y rara vez se implementa en las redes modernas.
![[Pasted image 20230702210328.png]]
### **Conmutación rápida(Fast Switching)**
Fast switching usa una memoria caché de switching rápido para almacenar la información de siguiente salto. Cuando un paquete llega a una interfaz, se reenvía al plano de control, donde la CPU busca una coincidencia en la caché de switching rápido. Si no encuentra ninguna, se aplica el switching de procesos al paquete, y este se reenvía a la interfaz de salida.
La información de flujo del paquete también se almacena en la caché de switching rápido. Si otro paquete con el mismo destino llega a una interfaz, se vuelve a utilizar la información de siguiente salto de la caché sin intervención de la CPU.
![[Pasted image 20230702210534.png]]
### **CEF**
Es el mecanismo de reenvío de paquetes más reciente y predeterminado del IOS de Cisco. Al igual que el switching rápido, CEF arma una base de información de reenvío (FIB) y una tabla de adyacencia. Sin embargo, las entradas de la tabla no se activan por los paquetes como en el switching rápido, sino que se activan por los cambios, como cuando se modifica un elemento en la topología de la red.
Cuando se converge una red, la FIB y las tablas de adyacencia contienen toda la información que el router debe tener en cuenta al reenviar un paquete. Cisco Express Forwarding es el mecanismo de reenvío más rápido y la opción más utilizada en los routers Cisco y en los Multilayer Switches.
CEF crea la FIB y las tablas de adyacencia una vez que se converge la red. Los cinco paquetes se procesan rápidamente en el plano de datos.
![[Pasted image 20230702210709.png]]

---

Una analogía frecuente que se usa para describir los tres mecanismos de reenvío de paquetes es la siguiente:

- El switching de procesos resuelve un problema realizando todos los cálculos matemáticos, incluso si los problemas son idénticos.
- El switching rápido resuelve un problema realizando todos los cálculos matemáticos una vez y recuerda la respuesta para los problemas posteriores idénticos.
- CEF soluciona todos los problemas posibles antes de tiempo en una hoja de cálculo.
## Tabla de routing
Una tabla de enrutamiento contiene una lista de rutas a redes conocidas (prefijos y longitudes de prefijo). La fuente de esta información se deriva de lo siguiente:
- Redes conectadas directamente
- Rutas estáticas
- Protocolos de enrutamiento dinámico
### comandos

```cisco
ip route (ip de destino)(ip de donde va a ir el paquete)
```
define la ruta por donde va a ir el mensaje
```cisco
show ip route
```
muestra todas las rutas 

- **L** - Identifica la dirección asignada a la interfaz de un router. Esto permite que el router determine de forma eficaz si recibe un paquete para la interfaz o para reenviar.
- **C** - Identifica una red conectada directamente.
- **S** - Identifica una ruta estática creada para llegar a una red específica.
- **O** - Identifica una red que se descubre de forma dinámica de otro router con el protocolo de routing OSPF.
- ***** - la ruta es candidata para una ruta predeterminada.

---
Se agrega una red conectada directamente a la tabla de routing cuando se cumplen estas tres condiciones: 
1la interfaz está configurada con una dirección IP válida
2 se activa con el comando no shutdown 
3 recibe una señal portadora de otro dispositivo conectado a la interfaz. Una máscara de subred incorrecta para una dirección IPv4 no evita que aparezca en la tabla de routing, aunque el error puede evitar que se produzca una comunicación satisfactoria.
![[Pasted image 20230703000201.png]]

## Distancia administrativa
Representa la "confiabilidad" de la ruta. Cuanto menor es la AD, mayor es la confiabilidad de la ruta. Dado que EIGRP tiene un AD de 90 y OSPF tiene un AD de 110, la entrada de ruta EIGRP se instalaría en la tabla de enrutamiento.
Una entrada de ruta para una dirección de red específica (longitud de prefijo y prefijo) sólo puede aparecer una vez en la tabla de enrutamiento. Sin embargo, es posible que la tabla de enrutamiento aprenda acerca de la misma dirección de red desde más de un origen de enrutamiento.
**Nota**: Las redes conectadas directamente tienen el AD más bajo de 0. Sólo una red conectada directamente puede tener un AD de 0.
![[Pasted image 20230702211904.png]]

## Rutas estáticas
Las rutas estáticas se configuran de forma manual.
definen una ruta explícita entre dos dispositivos de red. se deben reconfigurar de forma manual si se modifica la topología de la red. Los beneficios de utilizar rutas estáticas incluyen la mejora de la seguridad y la eficacia de los recursos. Las rutas estáticas consumen menos ancho de banda que los protocolos de routing dinámico, y no se usa ningún ciclo de CPU para calcular y comunicar las rutas
**<u>El routing estático tiene tres usos principales:</u>**
- Facilita el mantenimiento de la tabla de routing en redes más pequeñas en las cuales no está previsto que crezcan significativamente.
- Utiliza una única ruta predeterminada para representar una ruta hacia cualquier red que no tenga una coincidencia más específica con otra ruta en la tabla de routing. Las rutas predeterminadas se utilizan para enviar tráfico a cualquier destino que esté más allá del próximo router ascendente.
- Enruta trafico de y hacia redes internas. Una red de rutas internas es aquella a la cual se accede a través un de una única ruta y cuyo router tiene solo un vecino.
## Protocolos de routing dinámico
compartir información sobre el estado y la posibilidad de conexión de redes remotas. Los protocolos de routing dinámico realizan diversas actividades, como la detección de redes y el mantenimiento de las tablas de routing.
seleccionar una mejor ruta y la capacidad de descubrir automáticamente una nueva mejor ruta cuando se produce un cambio en la topología.
El descubrimiento de redes es la capacidad de un protocolo de enrutamiento de compartir información sobre las redes que conoce con otros routers que también están usando el mismo protocolo de enrutamiento. En lugar de depender de las rutas estáticas configuradas manualmente hacia redes remotas en cada router, los protocolos de routing dinámico permiten que los routers descubran estas redes de forma automática a través de otros routers.
![[Pasted image 20230702223017.png]]
En la entrada de la tabla de enrutamiento,  [1/0] a 172.16.2.2, los números dentro del corchete indican la distancia administrativa y la métrica respectivamente


[[VLAN]]
