## La limitación crítica del Gateway Predeterminado
En una red conmutada tradicional, cada cliente final (PC, teléfono IP) recibe la configuración de un único gateway predeterminado (Puerta de enlace). Si este router o la interfaz específica que funciona como gateway falla, los hosts configurados para usarlo quedan inmediatamente aislados, perdiendo toda comunicación con las redes externas y con Internet.

No existe una forma nativa o automática en la que un cliente común pueda usar un gateway secundario simultáneamente, incluso si existe un segundo router físico en la oficina que podría encargarse de transportar los paquetes.
![[Pasted image 20230731230517.png]]

Por lo general, los dispositivos finales se configuran (ya sea estáticamente o vía DHCP) con una única dirección IPv4 para su gateway predeterminado. Esta dirección no se modifica automáticamente si cambia la topología de la red o si un router se apaga, lo que convierte al Default Gateway en un **punto único de falla (Single Point of Failure - SPOF)** inaceptable para redes de alta disponibilidad.

*(Nota: Los dispositivos modernos con IPv6 reciben dinámicamente su dirección de puerta de enlace de forma activa a través de los mensajes de anuncio de router ICMPv6 (SLAAC). Sin embargo, también se benefician enormemente de una conmutación por error (failover) transparente y mucho más rápida hacia un nuevo router cuando se utiliza una tecnología de redundancia).*

## Redundancia del router (FHRP)
Para solucionar este problema estructural, se necesita un mecanismo para proporcionar gateways predeterminados alternativos de manera transparente y automática. Este mecanismo es proporcionado por los **Protocolos de Redundancia de Primer Salto (FHRP - First Hop Redundancy Protocols)**.

Una forma elegante de evitar un único punto de falla en el gateway es implementar la ilusión de un "router virtual". 
Para ello, se configuran varios routers físicos independientes para que funcionen juntos en equipo, dando la ilusión a todos los hosts de la LAN de que solo existe un único e infalible router. Al compartir una misma dirección IP virtual y una dirección MAC virtual, dos o más routers pueden respaldarse entre sí activamente.

> [!info] Explicación: ¿Qué es el Primer Salto?
> El "primer salto" (First Hop) es literalmente el primer router físico por el que debe pasar obligatoriamente el tráfico de tu computadora para lograr salir de la red local. Redundancia de primer salto significa tener siempre un segundo router físico listo y a la espera para actuar inmediatamente si el router principal explota o se desconecta, sin que las computadoras deban darse cuenta o ser reconfiguradas.

```mermaid
flowchart TD
    subgraph "Hosts en la LAN"
        PC1(PC 1)
        PC2(PC 2)
    end
    
    subgraph "Grupo FHRP (Router Virtual)"
        RV(("Router Virtual\nIP: 192.168.1.1\nMAC: 0000.0C07.AC01"))
        R1[Router Físico 1\n(Activo)]
        R2[Router Físico 2\n(Reserva/Standby)]
        
        RV -.-> R1
        RV -.-> R2
    end
    
    PC1 --> |Tráfico a 192.168.1.1| RV
    PC2 --> |Tráfico a 192.168.1.1| RV
```

La dirección IPv4 del router virtual se configura como el default gateway en las estaciones de trabajo del segmento. Cuando los dispositivos envían tramas hacia el gateway, utilizan el protocolo ARP para resolver la dirección MAC de esa IP. El router físico que actualmente es el "Activo" del grupo virtual responde a esa solicitud entregando la dirección MAC virtual compartida, engañando efectivamente a la PC.

Un protocolo FHRP proporciona la matemática y los temporizadores para determinar automáticamente qué router físico debe cumplir la función de reenvío, y en qué milisegundo exacto un router de reserva debe asumir el trono en caso de emergencia.

### Pasos para la conmutación por falla (Failover)
1. El router de reserva deja de recibir los vitales mensajes periódicos de "saludo" (keepalives/hellos) provenientes del router de reenvío (el router activo).
2. Tras agotarse un temporizador de seguridad, el router de reserva asume la muerte del principal y se convierte de inmediato en el nuevo router de reenvío.
3. Debido a que este nuevo router asume de forma transparente y sin cambios tanto la dirección IPv4 como la dirección MAC del router virtual, los switches redirigen el tráfico de hardware hacia él, y las conexiones de red de los hosts no se caen.

![[Pasted image 20230731232109.png]]

## Opciones y Protocolos de la familia FHRP

| Protocolo FHRP | Descripción e Implementación |
|:---:| --- |
| **HSRP (Hot Standby Router Protocol)** | Protocolo propietario clásico de Cisco. Diseñado para permitir la conmutación por error en IPv4 e IPv6. Selecciona explícitamente un dispositivo Activo (el que trabaja) y uno en Espera (el que vigila). |
| **VRRPv2 / VRRPv3 (Virtual Router Redundancy Protocol)** | Protocolo **estándar abierto** de la industria (IEFT RFC) equivalente a HSRP. Permite la redundancia virtual pero puede funcionar cruzando diferentes marcas. Elige un router como "Master" (Maestro) y los demás operan como "Backups" (Respaldos). |
| **GLBP (Gateway Load Balancing Protocol)** | Protocolo avanzado y propietario de Cisco que, además de ofrecer un respaldo de emergencia (como HSRP/VRRP), permite realizar un **balanceo de carga inteligente** repartiendo el tráfico simultáneamente entre todos los routers físicos del grupo. |

> [!info] Explicación: HSRP vs VRRP vs GLBP
> - **HSRP y VRRP:** Ambos operan bajo un modelo "Activo/Pasivo" estricto. Uno de los routers trabaja procesando el 100% de los paquetes y el otro router está literalmente de brazos cruzados, cobrando polvo y electricidad, esperando que el primero falle para empezar a trabajar.
> - **GLBP:** Funciona bajo un brillante modelo "Activo/Activo". Si tienes dos routers físicos en el grupo GLBP, el protocolo le asignará a la mitad de tus PCs la MAC del Router 1 y a la otra mitad la MAC del Router 2. De este modo, ambos routers reenvían el 50% de la carga de Internet, aprovechando económicamente todo tu hardware. Si uno falla, el otro asume el 100% de la carga.

## Notas relacionadas
- [[HSRP (Hot Standby Router Protocol)]]
- [[Enrutamiento]]
- [[VLAN]]
