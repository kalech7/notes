``
1. ¿Cómo se distribuyeron las responsabilidades y funciones entre los diferentes nodos en los primeros días de ARPANET?

1. hilos 
2. concurrencia: 
mutex 
semaforos 
barreras 
variables condicionales 
3. gestionar para hacerlo eficiente
fork crea procesos que necesitan instanteamente el cual se encarga los cuales se encrga de procesar las solicitudes 
en vez del proceso se pueden tener hilos 
prefork crea un pool de procesos se debe tener un nivel maximo de concurrencia 
el browser es un cliente conrurente 

waf (firewall aplicacion solo para trafico web)

instrucciones de control (jumps) debe ser finito 
and not or  sumas restas multiplicaciones  diviciones jumo 
ahora los sistemas operativos son bloqeuandos antes eran concurrentes

computacion evloitva 
bibliotecas estandar 
kernel 
isa( entrada salida entrada salida)
los sockets estan dentro del kernel 
control de accesos hace el sistema operativo 
el kernel adminstra el recurso adminisra el recurso compartido 

optimiza tiempo de respuesta scheduler de tipo batch 

uucp protocolo de copia entre unix transferir archivos
slip()
concurrencia 
counter swtching 

2pc
pki
la unica forma de detactar falla es por timeouts 

1) se pide al servidor 
tolerante a fallas visantinas
conseso signnifica que nodos lleguen al mismo resultado correcto
un socket es una api asi metrica 
tabla de descriptorea abierto en linux 1024 canales de entrada salida 
staandar input 
standar error
stnadar output se crean esos 3 por defecto 

tabla de manejadore de signals 
como se manejas las señales 

se van a replicar 

dead lock 
livelock

peligros del pipeline:
coherencia de cache 
peligro estrutural  fetch
jumps condicionales
dependencias de datos 

ejecucion fuera de orden
alritomo parcial deben coordinar 

tareas administrativas se usan  signals
tercer grupo de signals que deben ignorar 
database versionasda 
mutex degrada el renddieminetpo 

## api de sockets


kernel (abstracciones de socket, archivos)
isa 
hw

vamos a solicitar con la funcion socket(syscall) string y datagram
tdp (flujo de biredccional paquetes)
udp(servicio de datagramas)

* tabla de descriptores abiertos se  crea un 3 para el socket
* sd=(inter, socket string( tcp),datagrama(udp))
* siempre el kernel da un indice =blind(sd,direccion_server)
* ?(da como resultado el numero del indice) =listen(sd,n (llamdas en espera))
* cunado se se conecta el so le da un socket nsd=accept(sd,dir_cliente(vacia) se llena con la direccion ip puerto ,longitud)

se usa un nuevo socket cuand ose psa el 3 way handshake dose(sd)
close(nsd)

para concurrencia se usa procesos o hilos
pid=fork()
r/w(nsd,dir,long)
close(nd)
exit()

* algoritmos del cliente
se usan servicios del directorio que mapeq dns, servicios a puertos
el proceso hijo no necesita el socket
el proceso hijo se comunica con el cliente a tenderle y usa el nuevo el proceso padre no habla con ese cliente

protocolos no tienen estados 
el estandar de 4 bits deben estar en big endian 

accept es bloqueante 
optimaza el kernel para sockets 

tcp es un flujo de octetos buffering se llena el buffer y luego se manda 

inodes se teiene quien es el dueño contiene los metadatos de un a archivo 
datos 

sockets de tipo unix para procesos locales

http header etag (hash)

se abre un canal de entrada salida que se llama socket 

slow start en http

se pone trafico poco a poaco 
las conexiones pagan 
los browser son concurrentes 
se hace paralelismo con pipelining  con una sola conexion
lose serviodres no estan orientalos a conexion datagramas  pull de procesos 
puede durar horas ssh tcp 
solo se tiene un solo socket en tcp 
y en tcp se tiene un socket para cada destinatario 
es un servidor secuencial 

interporcess comunication 
se usan los de tipo unix
se conserva en estado http no tiene estado cada interaccion es autocontenida no hya nada que guardar 
otras apps tienen estados desde efecicia en el srvidor el servidor matiene el estado en su cahce memoria procesos lo vuelve vulnerables se defienden con timeouts

ssll capa de presentacion y sesion todo es tcp ip nativo 
copresion de cabeceras 
codigo 
el envio se hace pro genral 
soloo me najo el tecto que esta en gtml 
hay varias tecnicas para acerlar la carga en el browser en http 2
para reducir las conexiones al servidor 
el tiempo de caarga minimo se mide desde difenretes puntos de internet 
el servicio debe estar cerca del cliente 
geografia de internet 
rize de la imagen es costoso todo se puede hacer ddsde el servidor

toda aplicacion vive en anivel de usuario y anivel de kernel 
a nivvel de arquitectura el codigo que yo escribi que son instruccuones privilegias 
el kernel tiene la confianza del harddware
solo usamos dos modo pribvilegiado y no privelegiada 

socktes es una abstracciones (es una facilidad de lsisttema operativo )
a nivel de kernel:
socket 
tcp/udp
ip
eth/wifi

fue el caso para favorecer al caso mas comun servidores concurrente orientados a conexion tcp

cocurrentes{ tcp (string ) udp (datagrama)}
secuenciales{tcp udp}

es una cola de entrada y salida el socket primero tenemos  sd luego se manda un accept(sd) el cual automanticamnete tiengo un socket nsd= accept este nuevo socket se usa para entradas salidas  

dos sockets  cuando esta conectado un cliente

las llamadas al kernel son bloqueates

servicio echo multiprotocolo uno solo con multiples protocolos

send from recieve and read  puede  estar bloquead o 
los sistemas operativos son sincronos  hasta que pueda completar vamos a usar select 
minimo dos sockers pmanejados por dos procesos 

filedescript

set es para preguntar 
fd isset devuelve un boolean

asinacion demorada el tiempo de servicios esa casi deterministico 
ssh debe ser concurrente 

kerberos 

50+1 se cae el sistema en blockchain 

servidores concurrentes udp 
servidores iterativos  tcp 

como implemnetar i/o en un servidor concurrente
asincronus

reviev from sent toen el servidor 
sendto  

cada hilo tiiene su propia pila de ejecucion

tengo condiciones de carrera a las varibles globales o cuando compraten recursos

asincronus input output 

1024 tienen de entradas en la tabla de descirptories abiertos

fd_set* colaa de entrada 

dev/null
se romienda un segemento de la red servidores para auditoria login

syslog d

var/log/

servidor de alta disponibilidad 
supervivencia de datos 

/var/lock  

ara iniciar servicios basicos o de netweling 

todo los servcios tienen dependenccias y hay que respetarlas en el procesos de booteo y shutdown

bin/sh


tres formas de demonizar el proceso  fuera del hosst el sistem opereativo debe ser minimizado el hardware para solo ese servicio para protegerlo.

codificacion xdr 
se reserva el buffer de memorio 
char buff[128]
int i=3 [03] 00 00 00
float f=1.5 00 00 00 3f 
char c=a 61

xdrmem__create (en memoria) (2xdrp,buff,128,xdr_encode)
hay funciones para estos datos basicos 
xder_int(pointerxdrp,&i) es big endian 
xdr_char( &xdrp,&i)
se usan cuatro bites  en xdr 

char buff[128]=00 00 00 03 00 00 00 61 3f 00 00 00

char[125] 
float f
int i
xdr

xdr_decode 
en la primera opcion se espera que se llene todo el buffer lo que se conoce como buffering  es eficiente para el sistema menores costos computacionales 

el otro hay que aramar todas las cabeceras de internert  ir al disco  este se envia uno por uno 

cada arquitectura tiene su esquema de codificiacion 

sedebe pasar como maximo memoria para evitar que sobreescriba

serializar es escneial protocol buffer 


sin los standars no existieria computacion distribuida 
para poder alamacenar de manera eficiente  se usa en un codigo externos lo que permite cominar lo que se tiene codificiado internamente 
32bits big endian independiente delo uqe se tenga en memoria 

es un protocolo de informacion 

unirmode de oblifgaorio cumplkiento 
se usan 7 bits en el ideoma ingles
siempre el bit es 0 

ebcdic

ascci es logintud fija y huffman es varible 

es un apuntador que va al vacio

el kernel hace limpieza 

el servidor va a recibir el flijo de biyes y va a recibit el armo original 

es exactamente la misma 

va a ir recurisivamnete recrando el sub arbol iz yel subarbol derecho 
verificamos



cuando nos topamos con null es falsso 
dato booleano verdadero 
falso se codica con 4 ceros 
el armol esta serializado 

es la direccion de los bytes 

el puerto 111 se debe abrir
rpc binf asigna puertos 
rpc/https

genrpc genera
clt.c svr.c  cltpp.c svrcpp.c

grpc es acutal 
genrpc es antiguo 


la memoria cache se mide con tasa de hitss

http es mas de transporte 

existen 3 algoritmos 
rsa
dh
curva eliptica 

spec
rednimineto se mide por tiempo de respuesta y por throuput 

privilegios logicos(kernel) existe una fincion de acceso se ejecuta co nlos privilegios del administrador de procesamiento de almacenamineto entrada salida 
y fisicos(heardware ) del sistema

kerberos es un estandar v5
autenticacion 
ldap rfc(redifectory access protocol lite) es un standar v3
vrrrp rfc (redundancia principalmente a nivel de hardware software persona)
por el tema de sistemas operativos centralizados con tecnologias 

simple sign on
el servidor kerberos esta foramdo por un serviccio de ticket garanting service y AD debe ser una sola 
LDAP 
se le entrega credenciales y kerberos da un ticket(secuencia de bits que contiene n sevuencia criptografica es esxplisoivamente para presentar a los servidores tienen un tiempo de vida el ticket es conocido como tgt)


1) infraestructura
2) aplicaciones
3) gente 
elserividor kerberos tiene dos deamos 
administracion 
kds(centro de distrubucion de llaves)

tmp es importante para los tickets 

llave publica kerberos userypass

se debe crear un log para todos los servicios independientemente 

center for internet security 
pki 
se soluciona el problema de distribucion de certificados 
seguridad computacional 
son exponenciales 

firmas digitales diffie hellman algortimos discretos distribucion de llaves 

curva elepticams n(numero de veces) P() =x (se consigue el mismo resultado que rsa pero con menos computacion)

dsa digital signature algorithm 

procesos de auditoria 

no olvidarse del passhprse 

se  necesita el cerificado digital porque ahi esta llave prublica 

reduncdancia 
aplicacion procesos 
gente 
infraestructura 


opeacion es lo mmejor
reduncia fisica nos ayuda a la alta disponibilidad 

opereciones entre porceso y genete

1) clasificacion por nueves nueves nueves las interrupciones se pueden 
2) mtbf(tiempo medio entre fallas)
3) mttr(tiempo medio en que lo reparo y lo ponga up)
4) rto(significa cual es el periodo maximo que puedo perder de transacciones)
los routers calculan las tablas de enroutamineto esta distribuida poor miles de nods

sistemas autonomos sirve para mantener la tabla de enrutamiento esta altamente distribuido 

vrrrp(virtuall rendundancy protocol)
oravle rac 

dicrectorio es in protocolo y una base de datos jerarquica 
no se puede tener todo C(consistencia)A(disponibilidad)P(particiones) solo se deben tener como maximo 2 
en dns se debe tenr uno primerio y secundarios  
bases de datos relacional no sse usa en dns no escalaria 
la base de datos jerarquica es programacion orientada a objetos

inet org person es una persona que usa internet se define por una serie de atributos 
arbol de directorio 
son los atributos los cuales nos interesan 

fully coulified domain name 
cada nodo se llama entidad (cada entidad tiene atributos y estos atributos tienen llave valor )
smime rfc
se envia en base 64


computacion paralela 
3)isa mmmx
2 pipelining varias ejecucioens al a vez aquneu difenretes fases 
peligros 
estucturales: ambos procesos s quieren entrar al misma memoria
dependencia de datos: algunos procesos dependen de otros y por lo tanto se desperdician ciclos del procesador 
3 branches condicionales  no se dsabe por donde irse si por if o la rama else se debe esperar y desperdiciarse 
mitigacion esos peligros
para soluciones estructurales tner por ejem
para pipelining algoritmos fuera de orden 
para las branches con prediccion de branches existen alogirtmos de prediccion de ramas

throuput tiempo de respuesta 

multhethering
usar paralelimos en hilos o procesos
paralelismo a nivel de datos 

paralelos con memria compartida  es una sola memoria 
paralelismo con memoria distribuida con forma de  mensajes  lo que se debe usar sockets de una computacion distribuida en general 
es un sistema distribuida 
donde los nodos estan sincronizados  reducir 

biblioteca open mpi 

send_recv sincornizados 
gpu/tpu 

non stop kernel 
trusted computer system evaluation criteria  alta tolerancia misdmultiples programas procesadno los mismos daots de forma independiente 
A  
B
c2 segruo 
d no seguro
simd modelo que se aplica a la gpu
mimd  es cpu en cada nucleo puedo aplicar diferentes procesos

computaciones de tipo matricial vectorial
4 gpus y 4cpus 
flynn 

primero se tiene el problema luego el modelo el metodo numerico y luego se realiza el algoritmo y finalmente   promgramacion 

mientras mayor resolcion necesite neceito 

orden parcial de instrucciones me dla paralelismo y concurrrencia 
overhead 
paralelismo ideal=w/s 



que scheduler se debe usar
fork-join patron de computacion paralea mas usado 

mutex lock unlock 
cada hilo manipula sus propias variables reduce cada hilo maneja su propia varible la operacion aritmetica y se haace de forma automatica  
prgama paralel se creo la seecion paralela y  existe una barrera 
y los hilos esperan por parte del hilo maestro 
se denomina fork join todos los hilos deben finalizar 

buffering se hace por optimizacion 

dinamico la a signacion es fija 

gnumber: 80088001 
user: achavez24@slb.com
call center: 022979411

slb.ABC.944