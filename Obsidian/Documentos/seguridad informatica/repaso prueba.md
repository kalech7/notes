# ISO
**ISO/IEC 27011 (Guía para la gestión de seguridad de la información en telecomunicaciones)**
proporciona directrices específicas para la gestión de la seguridad de la información en la industria de las telecomunicaciones. Está centrado en el entorno de telecomunicaciones, no en la protección de información personal o en la privacidad de los clientes

**ISO/IEC 27007 (Guía para la auditoría de sistemas de gestión de seguridad de la información)**
proporciona directrices para auditar los sistemas de gestión de seguridad de la información (SGSI), pero no está enfocado en la protección de la privacidad de la información personal.

**ISO/IEC 27018 (Protección de la privacidad en la nube)**
es una norma específica que proporciona directrices para proteger la privacidad de la información personal identificable (PII) en servicios de computación en la nube. Esta norma ayuda a los proveedores de servicios en la nube a establecer controles de seguridad adecuados para proteger la privacidad de los datos personales de sus clientes.

**ISO/IEC 27001 (Sistema de gestión de seguridad de la información)**
establece los requisitos para implementar un sistema de gestión de seguridad de la información (SGSI). Si bien cubre una amplia gama de controles de seguridad, no se centra exclusivamente en la privacidad de los datos personales.

# infraestuctura pki
![[Pasted image 20250119150945.png]]
- **Claves de PKI**: Un par de claves que permite el [cifrado](https://www.entrust.com/es/resources/learn/encryption), un proceso de ocultación de datos para impedir que otras personas diferentes al destinatario previsto puedan leerlos. En criptografía, a cada clave pública le corresponde una clave privada. La clave pública se distribuye libre y abiertamente, mientras que la privada es secreta para el propietario.
- **Certificados digitales**: Credenciales electrónicas que vinculan la identidad del titular del certificado a un par de claves que pueden utilizarse para cifrar y firmar información. 
- **Autoridad de certificados (CA)**: Una entidad de confianza que emite certificados digitales. 
- **Autoridad de registro (RA)**: Se encarga de aceptar las solicitudes de certificados y autenticar a la persona u organización que las presenta.
- **Repositorios de certificados**: Ubicaciones seguras donde se almacenan los certificados y pueden recuperarse para su validación.
- **Software de gestión centralizada**: Un panel en el que las organizaciones pueden gestionar sus claves criptográficas y certificados digitales.
- **Módulo de seguridad de hardware (HSM)**: Dispositivos físicos que proporcionan un entorno seguro para realizar operaciones criptográficas y almacenar/gestionar claves digitales.
- **Validation Authority (VA):**
Se encarga de validar certificados digitales ya emitidos.

# comunicion iot
1. **Device-to-cloud model (Dispositivo a la nube):**
    - **Descripción:**
        - En este modelo, los dispositivos IoT envían datos directamente a una nube centralizada.
        - La nube almacena, analiza, y procesa los datos, proporcionando análisis avanzados como patrones de uso o estadísticas.
    - **Aplicación:**
        - Es ideal para escenarios donde los dispositivos generan grandes volúmenes de datos que necesitan ser procesados y analizados de manera centralizada.
        - En el caso descrito, la empresa utiliza los datos de consumo energético enviados a la nube para realizar análisis mensuales o anuales y optimizar el gasto energético.
    - **Relación con el caso:**
        - Este modelo permite el análisis centralizado de los datos de consumo de energía, lo que es fundamental para el propósito mencionado.

---

2. **Device-to-gateway model (Dispositivo a pasarela):**
    - **Descripción:**
        - En este modelo, los dispositivos IoT no se conectan directamente a la nube, sino a través de una **pasarela** intermedia (gateway).
        - La pasarela puede filtrar o procesar datos antes de enviarlos a la nube.
    - **Aplicación:**
        - Ideal para redes locales o para reducir el volumen de datos enviados a la nube.
    - **Relación con el caso:**
        - No es el mejor modelo para análisis centralizado de consumo energético, ya que requiere datos directamente en la nube.

---

3. **Cloud-to-cloud model (Nube a nube):**
    - **Descripción:**
        - Permite la comunicación entre diferentes servicios o plataformas en la nube.
        - Por ejemplo, datos recolectados por una nube de sensores pueden ser compartidos con otra nube para análisis o integración.
    - **Aplicación:**
        - Es útil para integrar múltiples sistemas o servicios de diferentes proveedores.
    - **Relación con el caso:**
        - No aplica aquí, ya que el análisis energético no requiere integración entre múltiples nubes.

---

4. **Device-to-device model (Dispositivo a dispositivo):**
    - **Descripción:**
        - Permite la comunicación directa entre dispositivos IoT sin pasar por la nube.
        - Los dispositivos pueden compartir información entre sí, normalmente en un entorno local.
    - **Aplicación:**
        - Útil para sistemas donde se requiere respuesta rápida entre dispositivos (como domótica).
    - **Relación con el caso:**
        - No es apropiado, ya que el caso implica análisis centralizado de datos, no comunicación entre dispositivos.

# deteccion 
#### **Dtex Systems**:

- **Descripción:**
    - Es una herramienta especializada en **User Behavior Analytics (UBA)**, que recopila detalles sobre la actividad del usuario desde múltiples fuentes, como dispositivos, aplicaciones, y redes.
    - Utiliza **inteligencia artificial (IA)** y **algoritmos de machine learning** para analizar los patrones de comportamiento de los usuarios.
    - Ayuda a identificar actividades anómalas, prevenir amenazas internas y detectar riesgos de seguridad antes de que se produzcan fraudes.
- **Aplicación:**
    - Muy utilizada en la detección y prevención de amenazas avanzadas, como accesos no autorizados, movimientos laterales en redes, o actividades sospechosas.
- **Relación con el caso:**
    - La herramienta cumple exactamente con la descripción dada, ya que emplea análisis de comportamiento para prevenir y detectar amenazas.

---

#### 2. **Wireshark**:

- **Descripción:**
    - Es una herramienta de análisis de tráfico de red (sniffer) que captura y examina paquetes en tiempo real.
    - Se utiliza principalmente para diagnosticar problemas de red, monitorear tráfico, y analizar protocolos.
- **Aplicación:**
    - Ideal para ingenieros de redes y administradores para rastrear problemas técnicos.
- **Relación con el caso:**
    - No realiza análisis de comportamiento del usuario ni utiliza IA o machine learning.

---

#### 3. **ClamWin**:

- **Descripción:**
    - Es un software antivirus gratuito de código abierto.
    - Detecta y elimina malware, pero no realiza análisis de comportamiento del usuario ni emplea algoritmos avanzados de IA.
- **Aplicación:**
    - Usado para proteger dispositivos contra amenazas conocidas.
- **Relación con el caso:**
    - No se ajusta a la descripción, ya que no utiliza análisis de comportamiento ni previene amenazas avanzadas.

---

#### 4. **Nmap**:

- **Descripción:**
    - Es una herramienta de escaneo de redes que permite identificar hosts, servicios, y sistemas operativos en una red.
    - Utilizada para pruebas de penetración y auditorías de seguridad.
- **Aplicación:**
    - Detecta vulnerabilidades en dispositivos o redes, pero no realiza análisis de comportamiento del usuario.
- **Relación con el caso:**
    - No es una herramienta UBA y no cumple con el propósito descrito.

# encriptacion wifi
1. **WPA3 (Wi-Fi Protected Access 3):**
    - **Seguridad: Alta**
        - Es la versión más avanzada y segura de WPA.
        - Utiliza **SAE (Simultaneous Authentication of Equals)** en lugar de PSK, lo que la hace más resistente a ataques de fuerza bruta y garantiza mayor seguridad incluso si la contraseña es débil.
        - Ofrece cifrado de **128 bits** en redes personales y **192 bits** en redes empresariales.
    - **Coloca a WPA3 como la opción más segura.**

---

2. **WPA2 Enterprise con RADIUS:**
    - **Seguridad: Muy alta**
        - Utiliza **EAP (Extensible Authentication Protocol)** para autenticar usuarios.
        - Integra un servidor **RADIUS (Remote Authentication Dial-In User Service)**, que agrega una capa de autenticación y administración centralizada.
        - Requiere credenciales únicas para cada usuario, lo que lo hace ideal para entornos empresariales.
    - **Menos avanzado que WPA3, pero más seguro que WPA2 PSK.**

---

3. **WPA2 Enterprise (sin RADIUS):**
    - **Seguridad: Alta**
        - Similar a WPA2 Enterprise con RADIUS, pero sin la integración de un servidor de autenticación RADIUS.
        - Es más vulnerable si no se configura correctamente, ya que la autenticación depende más de la red local.

---

4. **WPA2 PSK (Pre-Shared Key):**
    - **Seguridad: Media**
        - Utiliza una clave compartida entre los usuarios de la red.
        - Es adecuado para redes personales o pequeñas oficinas, pero es menos seguro porque:
            - Todos los usuarios comparten la misma clave.
            - Si se compromete la clave, toda la red queda vulnerable.
    - **Es el método más inseguro de los listados.**

# red de contendores cdm 
1. **Network drivers (Controladores de red):**
    - **Descripción:**
        - Son los responsables de implementar la funcionalidad de red en los contenedores, determinando cómo se conectan y comunican entre sí.
        - Estos controladores manejan la creación y configuración de las redes de contenedores, pero no contienen archivos de configuración individuales del contenedor.

---

2. **Endpoint (Punto final):**
    - **Descripción:**
        - Se refiere a la representación de un contenedor dentro de una red, es decir, una interfaz de red específica para ese contenedor.
        - Los endpoints definen las conexiones de un contenedor a una red, pero no almacenan los archivos de configuración completos de la pila de red del contenedor.

---

3. **Sandbox (Caja de arena):**
    - **Descripción:**
        - El **sandbox** es el objeto que contiene los archivos de configuración de la pila de red de un contenedor, como la tabla de enrutamiento, las interfaces del contenedor, y la configuración de DNS.
        - Este es el entorno donde se gestionan los aspectos específicos de la configuración de red de un contenedor.
    - **Relación con la pregunta:**
        - El sandbox es el que contiene la configuración interna completa del contenedor, incluyendo los detalles específicos de la red (tablas de enrutamiento, interfaces, DNS).

---

4. **IPAM drivers (Controladores IPAM):**
    - **Descripción:**
        - **IPAM (IP Address Management)** es responsable de la asignación y gestión de direcciones IP dentro de las redes de contenedores.
        - Aunque maneja las direcciones IP, no gestiona directamente las configuraciones completas de la red de un contenedor, como las tablas de enrutamiento o las interfaces.

# tipos de criptografia
1. **Public-key cryptography (Criptografía de clave pública):**
    - **Descripción:**
        - La criptografía de clave pública utiliza un par de claves: una clave pública para cifrar los datos y una clave privada para descifrarlos. La clave pública se comparte abiertamente, mientras que la clave privada se mantiene en secreto.
    - **Relación con el caso:**
        - Este tipo de criptografía no es aplicable en el escenario descrito, ya que en este caso ambas partes usan una clave compartida para cifrar y descifrar el archivo, lo que corresponde a criptografía simétrica.

---

2. **RSA cryptosystem (Criptosistema RSA):**
    - **Descripción:**
        - RSA es un algoritmo específico dentro de la criptografía de clave pública, que se utiliza para cifrar datos mediante un par de claves (pública y privada).
    - **Relación con el caso:**
        - Aunque RSA utiliza un par de claves, en este caso se menciona que se usa la misma clave para cifrar y descifrar los datos, lo que implica criptografía simétrica, no RSA.

---

3. **Asymmetric cryptography (Criptografía asimétrica):**
    - **Descripción:**
        - La criptografía asimétrica utiliza un par de claves diferentes: una clave pública para cifrar y una clave privada para descifrar (o viceversa).
    - **Relación con el caso:**
        - Este tipo de criptografía no es aplicable aquí, ya que Jamie y Alice están utilizando la misma clave para ambas operaciones (cifrado y descifrado), lo que indica que están usando criptografía simétrica.

---

4. **Symmetric cryptography (Criptografía simétrica):**
    - **Descripción:**
        - En la criptografía simétrica, tanto el emisor como el receptor usan la **misma clave secreta** para cifrar y descifrar los datos. Este tipo de criptografía es eficiente y rápida, pero requiere que ambas partes mantengan la clave secreta compartida.
    - **Relación con el caso:**
        - En el escenario descrito, Jamie y Alice utilizan la misma clave secreta para cifrar y descifrar el archivo, lo que es característico de la criptografía simétrica.

# Tipos de cloud
- **Community cloud (Nube comunitaria):**
    - Se comparte entre varias organizaciones con intereses similares, como cumplir con regulaciones específicas o compartir costos.
    - No asegura control total sobre los datos, ya que se comparte entre las organizaciones participantes.
- **Public cloud (Nube pública):**
    - Ofrecida por proveedores como AWS, Azure, o Google Cloud. Los recursos son compartidos entre múltiples clientes.
    - No permite un control completo de los datos, ya que la infraestructura es administrada por el proveedor.
- **Private cloud (Nube privada):**
    - Exclusiva para una sola organización. Puede ser gestionada internamente o por un tercero, pero se dedica exclusivamente a esa organización.
    - **Proporciona control total sobre los datos y una mayor seguridad**, siendo ideal para información sensible.
- **Multi cloud (Multinube):**
    - Uso de múltiples proveedores de nubes públicas o privadas.
    - Aunque ofrece flexibilidad, no garantiza el control total sobre los datos porque pueden estar distribuidos en varios entornos.

# Protocolos
1. **RADIUS (Remote Authentication Dial-In User Service):**
    - Es un protocolo de autenticación utilizado principalmente para administrar el acceso a redes.
    - No tiene relación directa con el cifrado y la firma de correos electrónicos.
2. **S/MIME (Secure/Multipurpose Internet Mail Extensions):**
    - Es un estándar ampliamente utilizado para proporcionar **cifrado de extremo a extremo** y **firmas digitales** en correos electrónicos.
    - Emplea algoritmos como **DSS (Digital Signature Standard)** para firmas digitales y **Triple DES** para cifrado de mensajes.
3. **EAP (Extensible Authentication Protocol):**
    - Se utiliza para la autenticación en redes, especialmente en conexiones inalámbricas como WPA/WPA2.
    - No está diseñado para cifrar o firmar correos electrónicos.
4. **TACACS+ (Terminal Access Controller Access-Control System Plus):**
    - Es un protocolo para controlar el acceso a dispositivos de red y autenticar usuarios.
    - No tiene relación con el cifrado o las firmas digitales en correos electrónicos.

- **Composite-signature-based analysis:**
    
    - Analiza patrones de actividad en múltiples paquetes o eventos a lo largo del tiempo.
    - Requiere correlacionar información entre diferentes paquetes o flujos de datos para identificar ataques complejos.
    - No se ajusta al caso, ya que Joseph analiza cada paquete de forma independiente.
- **Atomic-signature-based analysis:**
    
    - Examina paquetes individuales o eventos únicos.
    - Busca cambios en características como direcciones IP de origen/destino o números de puerto en los encabezados de los paquetes.
    - Es la técnica utilizada en el caso, ya que Joseph analiza información puntual en los encabezados de los paquetes.
- **Context-based signature analysis:**
    
    - Analiza el comportamiento en un contexto más amplio, considerando la actividad previa o eventos relacionados en un flujo de datos.
    - Sería relevante si Joseph estuviera evaluando cómo los cambios afectan al flujo completo, pero no es el caso.
- **Content-based signature analysis:**
    
    - Se enfoca en analizar el contenido del paquete, como datos o payload, en lugar de los encabezados.
    - Es inapropiado aquí, ya que Joseph analiza los encabezados (direcciones IP y números de puerto) y no el contenido.

1. **Orchestrators:**
    - Son herramientas diseñadas para automatizar y gestionar el despliegue, escalado y funcionamiento de contenedores en un entorno de producción.
    - Permiten convertir imágenes en contenedores, desplegarlas en los hosts, monitorizar el flujo de trabajo, y manejar tareas como balanceo de carga, asignación de recursos, y actualizaciones.
    - Ejemplos comunes: **Kubernetes**, **Docker Swarm**, y **OpenShift**.
    - **Aplicación al caso:** Joseph está utilizando una solución que automatiza el manejo de contenedores desde su creación hasta su monitoreo, lo que corresponde a un **orquestador.**

---

2. **Sniffers:**
    
    - Herramientas que capturan y analizan el tráfico de red.
    - Útiles para diagnosticar problemas de red o detectar actividades maliciosas, pero no están relacionadas con la gestión de contenedores.
3. **Network monitors:**
    
    - Supervisan el rendimiento y la disponibilidad de una red.
    - Son usados para identificar problemas de red o cuellos de botella, pero no gestionan contenedores.
4. **Port scanners:**
    
    - Herramientas que buscan puertos abiertos en un host o red.
    - Son usadas para evaluar la seguridad de un sistema o identificar servicios en ejecución, pero no gestionan el ciclo de vida de contenedores.

# Proxy 
1. **Anonymous Proxy:**
    - Un **proxy anónimo** oculta la identidad del usuario al navegar por Internet.
    - Su función principal es proteger la privacidad del usuario al no revelar su dirección IP ni otros datos identificativos al servidor destino.
    - Ideal para mantener el anonimato en línea y evitar el rastreo.
    - **Aplicación al caso:** Mary quería ocultar sus detalles y actividad de navegación, por lo que utilizó un proxy que hace su actividad en línea no rastreable. Esto corresponde a un **proxy anónimo.**

---

2. **Explicit Proxy:**
    
    - Se requiere configuración manual en el navegador o sistema para que el tráfico pase a través de este proxy.
    - Normalmente, este proxy no está diseñado específicamente para ocultar la identidad del usuario, sino para gestionar el acceso a Internet, como ocurre en redes empresariales.
    - No es relevante en este caso.
3. **Reverse Proxy:**
    
    - Este tipo de proxy se utiliza para **gestionar y proteger servidores**, no usuarios individuales.
    - Actúa como intermediario entre los clientes y el servidor para funciones como balanceo de carga, seguridad, y almacenamiento en caché.
    - No sirve para ocultar la identidad del usuario.
4. **SOCKS Proxy:**
    
    - Es un tipo de proxy versátil que puede gestionar diferentes tipos de tráfico (HTTP, FTP, etc.) a través de aplicaciones específicas.
    - Si bien puede usarse para ocultar la IP, no está diseñado específicamente para proteger la privacidad como lo hace un proxy anónimo

#### **Roles de los actores en la arquitectura NIST:**

1. **Cloud Provider (Proveedor de la nube):**
    
    - Ofrece servicios de nube (IaaS, PaaS, SaaS) a los consumidores.
    - Administra la infraestructura, las plataformas y las aplicaciones.
2. **Cloud Consumer (Consumidor de la nube):**
    
    - Utiliza los servicios proporcionados por el cloud provider.
    - Puede ser una organización o un individuo que contrata los servicios.
3. **Cloud Carrier (Transportista de la nube):**
    
    - Proporciona la infraestructura de red y los servicios de transporte que permiten la conectividad entre el consumidor y el proveedor.
    - Ejemplo: Proveedores de servicios de Internet (ISP) que facilitan la comunicación entre los actores.
4. **Cloud Auditor (Auditor de la nube):**
    
    - Verifica la seguridad, privacidad y cumplimiento de los servicios en la nube.
    - Evalúa los controles implementados por el proveedor para garantizar la conformidad con las normas.

# cipher
Un **transposition cipher** (cifrado por transposición) es un método de cifrado en el cual los caracteres del texto plano no se sustituyen, sino que **se reordenan según un patrón específico** para generar el texto cifrado. En este tipo de cifrado:

1. **Los caracteres permanecen iguales:** No se cambian los caracteres individuales, como ocurre en un cifrado por sustitución.
2. **El orden de los caracteres cambia:** Se reorganizan las posiciones para ocultar el significado original.

- **Stream cipher:**
    
    - Este tipo de cifrado trabaja con bits o caracteres individuales y los encripta uno por uno.
    - Requiere una clave que interactúa con cada bit de entrada, lo cual no encaja con la descripción.
- **Block cipher:**
    
    - Cifra bloques de datos (por ejemplo, 64 o 128 bits) a la vez.
    - Aunque puede reorganizar los datos internamente, generalmente combina transposición y sustitución, no solo reordenamiento.
- **Substitution cipher:**
    
    - En este tipo de cifrado, los caracteres del texto original se sustituyen por otros (por ejemplo, cambiar 'A' por 'X').
    - Kevin no cambió los caracteres, solo los reordenó, por lo que esta opción es incorrecta.
# wifi crack 
- **WPA2**:
    
    - **WPA2 (Wi-Fi Protected Access 2)** es un protocolo de seguridad que utiliza el estándar de encriptación AES (Advanced Encryption Standard).
    - En las redes **WPA2**, el proceso de autenticación se basa en un **four-way handshake**. Durante este proceso, el **PMK (Pairwise Master Key)** se utiliza para generar las claves de sesión que cifran los datos.
    - Los atacantes pueden **capturar** el **handshake** durante el proceso de conexión y **crackear la contraseña** usando el **PMK** y herramientas como **aircrack-ng** para obtener acceso no autorizado a la red.
- **WPA**:
    
    - **WPA** (Wi-Fi Protected Access) es una versión anterior de WPA2 y utiliza un protocolo de encriptación diferente, llamado TKIP (Temporal Key Integrity Protocol), que es menos seguro que AES.
    - Sin embargo, la descripción de capturar el PMK y usar un handshake es más común en **WPA2**.
- **WEP**:
    
    - **WEP** (Wired Equivalent Privacy) es un protocolo de encriptación muy antiguo y vulnerable. Los ataques a **WEP** no implican un proceso de **four-way handshake** ni el uso del **PMK** como en WPA2.
    - WEP se puede crackear de manera más sencilla, pero no involucra este tipo de proceso como el que describe el escenario.
- **WPA3**:
    
    - **WPA3** es una versión más reciente de WPA, que mejora la seguridad en comparación con WPA2, especialmente contra ataques de diccionario y otras técnicas de crackeo.
    - WPA3 tiene un mecanismo de autenticación más robusto y no es vulnerable al mismo tipo de ataque que afecta a WPA2 mediante la captura de PMK en el handshake.

- **Reference monitor**: Es un concepto en seguridad que se refiere a un componente del sistema que controla el acceso a los recursos del sistema, asegurándose de que se cumplan las políticas de seguridad. No es el término que se aplica al archivo en este contexto.
    
- **Subject**: En un modelo de control de acceso, el **sujeto** es el **usuario o proceso** que intenta acceder a un recurso o realizar una operación sobre un objeto. En este caso, **Fernandez** sería el **sujeto**, no el archivo.
    
- **Object**: El término **objeto** se refiere a los **recursos del sistema** que son accedidos o manipulados, como archivos, bases de datos, impresoras, etc. En este escenario, el archivo que Fernandez intenta acceder es el **objeto**.
    
- **Operation**: Se refiere a la **acción** que el sujeto desea realizar sobre el objeto, como leer, escribir o ejecutar el archivo. Aunque se menciona que Fernandez está intentando acceder a un archivo, el término **operación** se refiere a la acción, no al archivo en sí.

# control
- **System access controls**: Son controles que se utilizan para restringir el acceso a los sistemas informáticos y aplicaciones. No aplican a situaciones físicas, como el acceso a un edificio.
    
- **Physical security controls**: Estos controles están diseñados para proteger los activos físicos, como edificios, equipos y otras instalaciones, contra el acceso no autorizado o daños. El ejemplo de escanear tarjetas o huellas dactilares para acceder a las instalaciones es un **control de seguridad física**.
    
- **Administrative security controls**: Son políticas y procedimientos administrativos establecidos para gestionar y controlar la seguridad de la organización. Aunque las políticas pueden incluir aspectos como controles de acceso, en este caso el proceso físico está siendo descrito, no la política.
    
- **Technical security controls**: Son controles relacionados con la seguridad tecnológica, como firewalls, encriptación o autenticación basada en tecnología. Aunque los sistemas de autenticación pueden estar involucrados, el control descrito es físico, no técnico.

# iot 
- **Streaming data processor**: Este componente procesa datos en tiempo real, pero no está específicamente diseñado para la recopilación de datos o la preprocesamiento de datos provenientes de dispositivos IoT, como se menciona en la pregunta.
    
- **Machine learning**: Aunque el aprendizaje automático (Machine learning) se puede utilizar para analizar los datos, no es el componente que se encargue de la recopilación o el preprocesamiento. El aprendizaje automático se utiliza generalmente para análisis o modelado de datos, no para la recolección.
    
- **Data lakes**: Los lagos de datos (data lakes) son repositorios de almacenamiento que permiten almacenar grandes cantidades de datos. No se utilizan específicamente para preprocesar datos o para recopilar datos de dispositivos IoT.
    
- **Gateway**: Un **gateway** IoT es un dispositivo que conecta los dispositivos IoT a una red más amplia, permitiendo la recopilación de datos de los dispositivos IoT y, en muchos casos, también realiza tareas de preprocesamiento antes de enviar los datos a un servidor o la nube para su almacenamiento y análisis. En este caso, el gateway se encarga de la recopilación de datos de los dispositivos y de la realización del preprocesamiento.

# notify

- **Push notification**: Es una característica de mensajería que permite a una aplicación enviar mensajes o datos a un dispositivo móvil sin necesidad de que el usuario haga una solicitud explícita. Estas notificaciones se originan desde un servidor y se envían directamente a los dispositivos móviles, incluso cuando la aplicación no está activa en el dispositivo.
    
- **PIN feature**: El **PIN** (Personal Identification Number) es una característica utilizada para autenticar a los usuarios, generalmente en sistemas de seguridad. No está relacionada con el envío de mensajes o notificaciones.
    
- **Geofencing**: **Geofencing** es una tecnología que utiliza la ubicación geográfica para activar ciertos eventos o acciones, como el envío de una notificación cuando un dispositivo entra o sale de un área geográfica definida. Aunque puede activar notificaciones, no es un mecanismo directo de mensajería desde un servidor.
    
- **Containerization**: **Containerization** es una técnica utilizada en la seguridad de dispositivos móviles que permite separar los datos personales y los datos de la empresa, asegurando que las aplicaciones y los datos estén aislados en "contenedores". No está relacionada con la mensajería en tiempo real.
# tipos de access
- **Role-based access control (RBAC)**: En este modelo, el acceso a los recursos del sistema se controla según los roles asignados a los usuarios. En el escenario descrito, Carol no puede instalar aplicaciones porque no tiene privilegios de administrador, lo que indica que los permisos de instalación están basados en el rol de usuario. El modelo RBAC asigna permisos de acceso a roles (en este caso, el rol de administrador tiene los permisos para instalar aplicaciones).
    
- **Discretionary access control (DAC)**: En el DAC, el propietario de un recurso tiene la libertad de asignar permisos a otros usuarios para acceder a esos recursos. Este modelo no se ajusta a la situación, ya que no se menciona que Carol tenga la capacidad de conceder permisos para la instalación de aplicaciones.
    
- **Rule-based access control (RB-RBAC)**: Este modelo está relacionado con reglas predefinidas que determinan el acceso. Aunque las reglas pueden existir en RBAC, el concepto principal de este escenario no está relacionado con reglas adicionales, sino con roles asignados.
    
- **Mandatory access control (MAC)**: En MAC, el acceso a los recursos se controla de acuerdo con políticas centralizadas y no depende de los permisos otorgados por los usuarios. Este modelo es más estricto y no está basado en roles como el RBAC.

# leyes 
- **The Digital Millennium Copyright Act (DMCA)**: Fue promulgada en 1998, Esta ley de derechos de autor en los Estados Unidos establece, entre otras cosas, que las personas autorizadas a reparar o mantener sistemas pueden hacer copias de programas informáticos, pero siempre bajo ciertas condiciones. En el escenario descrito, Daniel hace una copia de un programa para realizar reparaciones o mantenimiento, lo cual está cubierto por las excepciones del DMCA, que permite hacer copias para este propósito sin infringir las leyes de derechos de autor.
- **Payment Card Industry-Data Security Standard (PCI-DSS)**: Es un conjunto de estándares de seguridad diseñado para proteger la información de tarjetas de crédito y débito, no relacionado con la exactitud de las divulgaciones corporativas.
- **Data Protection Act 2018 (DPA)**: Esta ley del Reino Unido regula el tratamiento de los datos personales. Aunque tiene que ver con la protección de la información, no se aplica directamente al escenario de copiar programas informáticos con fines de mantenimiento o reparación.
    
- **Sarbanes-Oxley Act (SOX)**: Fue promulgada en 2002 con el objetivo de proteger al público y a los inversores aumentando la precisión y la confiabilidad de las divulgaciones corporativas. La ley exige que las empresas públicas implementen controles internos y procedimientos para garantizar la exactitud de los estados financieros y que los ejecutivos sean responsables de la veracidad de la información presentada.
    
- **Gramm-Leach-Bliley Act (GLBA)**: Esta ley de EE. UU. se enfoca en la protección de la información financiera personal y la privacidad de los clientes en instituciones financieras. No se aplica a la copia de programas informáticos en el contexto de mantenimiento.

- **Geofencing**: Esta técnica utiliza la ubicación del usuario para crear una "cerca virtual" alrededor de una zona geográfica específica. Cuando el dispositivo del usuario entra o sale de esta zona, se activan eventos, como el envío de notificaciones o la recopilación de datos relacionados con la ubicación del usuario. A menudo se utiliza para fines de marketing, recopilación de datos sobre las actividades del usuario y personalización de servicios basados en la ubicación.
    
- **Push notification**: Se refiere a los mensajes que una aplicación envía a un dispositivo móvil sin que el usuario lo solicite. Aunque se puede utilizar en combinación con geofencing, no está directamente relacionado con la recopilación de datos de ubicación.
    
- **Containerization**: Es una técnica de seguridad en la que las aplicaciones y los datos se almacenan de forma aislada en un "contenedor" dentro del dispositivo móvil, evitando que aplicaciones no autorizadas accedan a ellos. No se relaciona con la recolección de datos de ubicación.
    
- **Full device encryption**: Esta técnica cifra todo el dispositivo móvil, protegiendo los datos almacenados en él, pero no tiene relación con la recopilación de datos de ubicación o actividades offline.

# wireless 
- **Wireless repeater (Repetidor inalámbrico)**: Es un dispositivo que recibe una señal de una red inalámbrica existente y la amplifica o "repite" para extender su alcance. En el escenario descrito, Robert está utilizando un repetidor inalámbrico para aumentar la señal y permitir la cobertura de áreas inaccesibles, mejorando así la conectividad en ubicaciones remotas.
    
- **Wireless NIC (Tarjeta de interfaz de red inalámbrica)**: Es un componente que permite a los dispositivos conectarse a una red inalámbrica, pero no amplifica ni extiende la señal de la red.
    
- **Wireless bridge (Puente inalámbrico)**: Conecta dos redes o segmentos de red inalámbrica diferentes, permitiendo que la comunicación fluya entre ellos. Aunque puede extender la cobertura, no necesariamente amplifica la señal de un solo punto de acceso.
    
- **Mobile hotspot (Punto de acceso móvil)**: Es un dispositivo que permite a los dispositivos conectarse a Internet a través de una conexión móvil, pero no amplifica una señal existente.

# partes del iot
- **Device layer**: Se encarga de los dispositivos y sensores físicos que recogen datos del entorno. Esta capa incluye los dispositivos de IoT que interactúan con el mundo real.
- **Cloud layer**: Se encarga del almacenamiento, procesamiento y análisis de los datos en la nube. Los datos recolectados por los dispositivos se envían a la nube para su procesamiento y almacenamiento a largo plazo.
- **Process layer**: Esta capa es responsable de procesar los datos recibidos, incluyendo su análisis y la toma de decisiones basadas en esos datos. Utiliza algoritmos de procesamiento para generar información útil.
- El **Communication layer** (capa de comunicación) en la arquitectura del Internet de las Cosas (IoT) es responsable de emplear los **protocolos y redes** necesarios para conectar, enviar y recibir datos entre dispositivos y redes.

El **SIEM** es una solución de seguridad que proporciona monitoreo en tiempo real, correlación de eventos, detección de amenazas y gestión de incidentes de seguridad. Las principales funciones de un SIEM incluyen la recolección de registros de eventos de diversos sistemas, la correlación de esos eventos para identificar patrones sospechosos o amenazas, y la capacidad de generar alertas y respuestas ante incidentes de seguridad.

- **VPN (Virtual Private Network)**: Una VPN proporciona seguridad en la comunicación a través de redes inseguras, como Internet, al cifrar el tráfico. No está diseñada para monitorear o gestionar eventos de seguridad.
- **SOCKS (Socket Secure)**: SOCKS es un protocolo de red que permite el tráfico de datos entre clientes y servidores a través de un servidor proxy. Aunque puede ser útil para redirigir el tráfico de red, no es una solución de monitoreo o gestión de eventos de seguridad.
- **MDM (Mobile Device Management)**: El MDM es una solución para gestionar y asegurar dispositivos móviles dentro de una red corporativa. Aunque es útil para la seguridad de dispositivos móviles, no proporciona las capacidades de monitoreo y correlación de eventos que se describen en el escenario.

# herrramientas
**HitmanPro** es una herramienta de seguridad diseñada específicamente para detectar y eliminar malware, incluyendo troyanos, virus y otras formas de software malicioso, en computadoras y dispositivos electrónicos. Es una herramienta de eliminación de malware que trabaja en segundo plano para encontrar y erradicar amenazas que otras soluciones de seguridad podrían haber pasado por alto.
- **HOIC (High Orbit Ion Cannon)**: Es una herramienta de Denegación de Servicio Distribuida (DDoS), diseñada para realizar ataques de saturación en servidores y sitios web. No está diseñada para detectar o prevenir malware.
    
- **Hulk**: Al igual que HOIC, Hulk es una herramienta utilizada para realizar ataques DDoS, especialmente en sitios web. No está relacionada con la detección de malware o Trojans.
    
- **Hashcat**: Es una herramienta utilizada para la recuperación y descifrado de contraseñas mediante ataques de fuerza bruta. No es una herramienta diseñada para prevenir o detectar malware.

# control 
- **Retrospective approach**: Este enfoque se centra en analizar incidentes de seguridad después de que ocurren, lo que no es el caso aquí, ya que Alice está tomando medidas preventivas antes de cualquier incidente.
    
- **C. Reactive approach**: Se refiere a responder a un ataque o acceso no autorizado una vez que ya ha ocurrido. Alice no está reaccionando ante una intrusión, sino tomando medidas para evitar que suceda.
    
- **D. Proactive approach**: Aunque este enfoque también implica tomar medidas para prevenir incidentes, se refiere más a una actitud general de anticipación y planificación a largo plazo (por ejemplo, protegerse ante amenazas futuras de manera continua)


# dipositivos
### **COBO (Corporate-Owned, Business-Only):**

- Significa que el dispositivo es propiedad de la empresa **y está restringido únicamente para tareas laborales**.
- Los empleados no pueden usar estos dispositivos para actividades personales.
- Ejemplo: Un teléfono o laptop proporcionado por la empresa, configurado para acceder únicamente a recursos corporativos (correo, aplicaciones de trabajo) y con restricciones para redes sociales o aplicaciones personales.

**En el caso de Finch, esta es la política implementada, ya que los dispositivos están restringidos a tareas exclusivamente relacionadas con el trabajo.**

---

### 2. **COPE (Corporate-Owned, Personally-Enabled):**

- Significa que el dispositivo es propiedad de la empresa, pero permite un uso personal limitado.
- Los empleados pueden instalar ciertas aplicaciones o usar el dispositivo para algunas actividades personales, mientras que la empresa sigue controlando la seguridad y el acceso.
- Ejemplo: Un empleado puede usar el teléfono de la empresa para revisar su correo personal, pero la empresa tiene control sobre qué aplicaciones están permitidas.

---

### 3. **CYOD (Choose Your Own Device):**

- Significa que los empleados eligen un dispositivo de una lista aprobada por la empresa.
- La empresa sigue siendo propietaria del dispositivo, pero los empleados tienen la flexibilidad de escoger el modelo o el sistema operativo que prefieran.
- Ejemplo: La empresa ofrece opciones como iPhone, Samsung Galaxy, o laptops Dell y Lenovo, y el empleado selecciona el dispositivo que mejor se adapte a sus necesidades.

---

### 4. **BYOD (Bring Your Own Device):**

- Significa que los empleados utilizan sus propios dispositivos personales para acceder a los recursos de la empresa.
- La empresa establece políticas y medidas de seguridad para proteger los datos corporativos, pero el dispositivo sigue siendo propiedad del empleado.