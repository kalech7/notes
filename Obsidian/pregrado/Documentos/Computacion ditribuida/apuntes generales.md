# Apuntes Generales de Computación Distribuida

> [!info] Explicación General
> Este documento consolida múltiples conceptos avanzados de sistemas operativos, arquitectura de computadoras, redes y seguridad, que son los pilares fundamentales para construir sistemas distribuidos eficientes y tolerantes a fallos.

## 1. Concurrencia y Sincronización
Para gestionar recursos y hacer eficiente el procesamiento concurrente, se utilizan diversas primitivas y estrategias:
- **Hilos y Procesos:** `fork` crea procesos independientes (clones) que atienden solicitudes inmediatamente. En lugar de procesos completos, se pueden usar hilos (*threads*) que comparten memoria, reduciendo el costo computacional.
- **Preforking:** Se crea un "pool" de procesos por adelantado para manejar un nivel máximo de concurrencia. (Ej. un navegador web es un cliente concurrente).
- **Primitivas de sincronización:** Se utilizan mecanismos como *mutex*, semáforos, barreras y variables condicionales para coordinar hilos. 
- **Problemas comunes:** Condiciones de carrera, *Deadlocks* (bloqueos mutuos) y *Livelocks*. El uso excesivo de *mutex* puede degradar drásticamente el rendimiento.

## 2. API de Sockets y Redes
Los sockets operan a nivel del Kernel del sistema operativo y proporcionan una abstracción para interactuar con la red.
- **Protocolos:** Se utiliza TCP (flujo bidireccional y confiable de bytes) o UDP (servicio de datagramas no confiable).
- **Flujo en Servidores (Syscalls):**
  1. `socket()`: Crea el socket (devuelve un descriptor).
  2. `bind()`: Asigna una dirección y puerto local al socket.
  3. `listen()`: Configura el socket para recibir conexiones entrantes.
  4. `accept()`: Es una llamada bloqueante. Al conectarse un cliente, el OS crea un nuevo socket dedicado para esa comunicación.
- Para lograr concurrencia, generalmente se hace un `fork()` después del `accept()`. El proceso hijo maneja la conexión con el nuevo socket, y el padre sigue escuchando.

## 3. Arquitectura de Computadoras y Paralelismo
El paralelismo a nivel de hardware enfrenta varios peligros (hazards) en el *Pipelining*:
- **Peligros estructurales:** Varios procesos intentan acceder a la misma memoria o recurso simultáneamente.
- **Dependencias de datos:** Algunas instrucciones dependen del resultado de otras, forzando ciclos de espera ("burbujas").
- **Saltos condicionales (*branches*):** No se sabe qué rama del `if` se ejecutará. Se mitiga mediante algoritmos de predicción de saltos.
- **Soluciones:** Ejecución fuera de orden (*Out-of-order execution*) y memorias caché (que a su vez traen el problema de la coherencia de caché).

Existen dos enfoques principales:
- **Memoria compartida:** Un solo bloque de memoria accesible por múltiples hilos/procesos.
- **Memoria distribuida:** Cada nodo tiene su memoria; se comunican mediante paso de mensajes (Sockets, MPI). Este es el fundamento real de la computación distribuida.

## 4. Representación de Datos y Serialización
En un entorno distribuido, las máquinas pueden tener arquitecturas distintas (ej. *Big Endian* vs *Little Endian*).
- **XDR (External Data Representation):** Estandariza la codificación de datos antes de transmitirlos por la red. Se reserva un buffer de memoria y se serializan los datos básicos (`int`, `float`) asegurando que el receptor pueda decodificarlos correctamente independientemente de su arquitectura.
- Serializar es esencial en tecnologías modernas como *Protocol Buffers* (Google) y RPC.

## 5. Seguridad y Autenticación
La seguridad es vital cuando los datos viajan por la red.
- **Kerberos (v5):** Estándar de autenticación en redes que utiliza un "Centro de Distribución de Llaves" (KDC) y un "Ticket Granting Service" (TGS). El usuario se autentica una vez (Single Sign-On) y recibe un *ticket* (TGT) con un tiempo de vida limitado para acceder a otros servicios sin enviar contraseñas en texto claro.
- **LDAP (Lightweight Directory Access Protocol):** Base de datos jerárquica para buscar información (ej. usuarios, credenciales). 
- **PKI (Public Key Infrastructure):** Infraestructura de llaves públicas que soluciona el problema de distribución de certificados digitales, utilizando algoritmos asimétricos como RSA o Curva Elíptica (menor carga computacional, mismos resultados de seguridad).

## 6. Alta Disponibilidad y Tolerancia a Fallos
- **Redundancia:** Aplicar redundancia física a infraestructura, procesos, datos y redes (protocolos como VRRP para hardware) ayuda a garantizar una Alta Disponibilidad (High Availability).
- **Métricas:** 
  - *MTBF* (Tiempo Medio Entre Fallas).
  - *MTTR* (Tiempo Medio de Reparación).
  - *RTO* (Tiempo Objetivo de Recuperación).
- **Consenso y Tolerancia:** Los algoritmos distribuidos (como el Commit de 2 o 3 fases, o tolerancia a Fallas Bizantinas) aseguran que los nodos lleguen al mismo resultado correcto.

> [!info] Explicación: Teorema CAP
> En sistemas distribuidos (ej. bases de datos distribuidas y directorios como DNS), el **Teorema CAP** establece que es imposible tener simultáneamente Consistencia (C), Disponibilidad (A) y Tolerancia a Particiones (P). Se debe elegir como máximo dos de las tres propiedades.