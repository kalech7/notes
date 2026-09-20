1. Arpanet (1969-1982): 10^3 hosts fue usado por us fue el precursos del internet  motivado para compartir recursos, fue lanzado por 4 nodos in 1969 crecio con miles de hosts, la primera killer app fue el email 
packet switching (kleinrock), control decentralizado (baran), internetworking (es conectar diferentes redes juntas en una sola larga red )

> [!info] Explicación: Packet Switching vs Circuit Switching
> El **Packet Switching (conmutación de paquetes)** fue una innovación clave de ARPANET. A diferencia de las redes telefónicas de la época que dedicaban un circuito físico completo para una llamada (Circuit Switching), los datos se dividen en paquetes pequeños que viajan de forma independiente por múltiples rutas dinámicas hacia su destino. Esto maximiza la eficiencia y la tolerancia a fallos.

2. NSFNET:  conectar gente que estaba haciendo negocios con la defensa de estados unidos fue conectada a supercompitadores que se convertirian en el backbone de toda la red, comenzaron nuevos protocolos de internet tcp/ip,dns,socket(api) 
demasiado creciemitno desde pcs y ethernets lans (casas,educacion,empresas)
**arquitectura temprana de internet**
1. nsfnet backbone
2. regional network
3. customer

> [!info] Explicación: Estandarización de Protocolos (TCP/IP)
> Durante la época de la transición de ARPANET a NSFNET, fue fundamental la adopción unificada de la suite de protocolos **TCP/IP** (Transmission Control Protocol / Internet Protocol) en 1983. IP se encarga de direccionar y enrutar los paquetes, mientras TCP garantiza la entrega en el orden correcto y sin errores.

3. internet moderno: la conectividad esta dado por grandes isps quienes son competidores, la web estalla en 93 la mayoria de bits son video(temprano)
**arquitectura moderna del internet**
* esta todavia descentalizada 
![[Pasted image 20240429220138.png]]

> [!info] Explicación: Arquitectura Moderna de ISP
> El Internet moderno es una "red de redes" estructurada jerárquicamente. 
> - **Tier 1 ISPs:** Proveedores globales que forman el "backbone" de internet y hacen *peering* (intercambio gratuito de tráfico) entre ellos.
> - **Tier 2/3 ISPs:** Proveedores regionales y locales que pagan a los de Tier 1 para acceder al resto de internet y brindan acceso a los usuarios finales (hogares, empresas).

## Notas relacionadas
- [[Http introduccion]]
- [[sockets]]
- [[computacion distribuida]]
- [[administracion de redes]]
