from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
OUT=Path(__file__).parent
W,H=1800,1200
BG='#f5f7fb';INK='#192b42';BLUE='#dce8fa';TEAL='#d6f0eb';ORANGE='#ffebd1';GREY='#e8edf3';EDGE='#506781'
FONT='/System/Library/Fonts/Supplemental/Arial.ttf';BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def font(n=30,b=False): return ImageFont.truetype(BOLD if b else FONT,n)
def canvas(title,subtitle):
 im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
 sz=48
 while d.textlength(title,font=font(sz,True))>1660: sz-=1
 d.text((70,42),title,fill=INK,font=font(sz,True));d.text((70,108),subtitle,fill=EDGE,font=font(27))
 d.line((70,157,1730,157),fill='#c8d3e0',width=2)
 return im,d
def box(d,x,y,w,h,txt,color=BLUE,size=30):
 d.rounded_rectangle((x,y,x+w,y+h),radius=20,fill=color,outline='#8295ad',width=2)
 lines=txt.split('\n');lh=size+10;sy=y+(h-len(lines)*lh)/2
 for i,l in enumerate(lines):
  tw=d.textlength(l,font=font(size,True));d.text((x+(w-tw)/2,sy+i*lh),l,font=font(size,True),fill=INK)
 return (x,y,w,h)
def arrow(d,a,b,label=None,color=EDGE):
 d.line((*a,*b),fill=color,width=5);ang=math.atan2(b[1]-a[1],b[0]-a[0]);s=17
 d.polygon([b,(b[0]-s*math.cos(ang-.45),b[1]-s*math.sin(ang-.45)),(b[0]-s*math.cos(ang+.45),b[1]-s*math.sin(ang+.45))],fill=color)
 if label:
  x=(a[0]+b[0])/2;y=(a[1]+b[1])/2;tw=d.textlength(label,font=font(24));d.rectangle((x-tw/2-8,y-34,x+tw/2+8,y-2),fill=BG);d.text((x-tw/2,y-33),label,font=font(24),fill=INK)
def label(d,x,y,t):
 bbox=d.textbbox((x,y),t,font=font(24));d.rectangle((bbox[0]-4,bbox[1]-4,bbox[2]+4,bbox[3]+4),fill=BG);d.text((x,y),t,font=font(24),fill=INK)
def footer(d,lines):
 for i,l in enumerate(lines):d.text((70,1080+i*37),l,fill=EDGE,font=font(27))
def save(im,name): im.save(OUT/name)

im,d=canvas('Broker: publicar un hecho y permitir varias reacciones','Síntesis original en español de las figuras 15-1 y 15-2')
box(d,90,340,330,160,'Productor\nPedido registrado')
box(d,690,300,380,700,'Broker\n\nCanal de eventos\n\nSuscripciones',TEAL)
for y,t in [(230,'Pago'),(520,'Inventario'),(810,'Notificación')]:
 box(d,1340,y,360,160,'Procesador\n'+t);arrow(d,(1070,y+80),(1340,y+80),'copia / suscripción')
arrow(d,(420,420),(690,420),'publica');arrow(d,(1490,970),(1070,960),'nuevo hecho')
footer(d,['El broker distribuye eventos; el orden completo del negocio emerge de los contratos y reacciones.','Canal, suscripción e instancia son conceptos diferentes. El broker no decide por sí solo el flujo.'])
save(im,'c15-01-broker.png')

im,d=canvas('Pedido del libro: una publicación abre varias ramas','Recreación conceptual de la figura 15-3; flechas = hechos que provocan nuevas reacciones')
box(d,80,250,330,110,'Registro de pedido');box(d,660,230,370,140,'Pedido registrado',TEAL);arrow(d,(410,305),(660,305))
for x,t in [(70,'Inventario'),(680,'Pago'),(1320,'Notificación')]:box(d,x,490,360,100,t)
arrow(d,(700,370),(250,490));arrow(d,(845,370),(860,490));arrow(d,(1030,305),(1495,490))
box(d,70,700,360,110,'Almacén\nReponer existencias');arrow(d,(250,590),(250,700));arrow(d,(100,700),(100,590));label(d,170,605,'inventario actualizado');label(d,20,665,'stock repuesto')
box(d,680,740,360,100,'Preparar pedido');arrow(d,(860,590),(860,740),'pago aplicado');arrow(d,(1040,540),(1320,540),'pago rechazado')
box(d,680,950,360,90,'Envío');arrow(d,(860,840),(860,950),'pedido preparado');arrow(d,(1040,790),(1320,590),'pedido preparado');arrow(d,(1040,995),(1500,590),'pedido enviado')
footer(d,['Notificación también anuncia el correo enviado; hoy puede no haber consumidores para ese hecho.','El retorno de reposición no debe volver a disparar el ciclo de reposición indefinidamente.'])
save(im,'c15-02-pedido-broker.png')

im,d=canvas('Payload: datos disponibles frente a una clave para consultar','Recreación de las figuras 15-10 y 15-12; cada evento puede elegir una solución diferente')
for x,title in [(80,'Con datos'),(960,'Con clave')]:d.text((x,210),title,font=font(40,True),fill=INK)
box(d,80,300,710,130,'Pedido + datos necesarios',TEAL);box(d,960,300,710,130,'ID del pedido',ORANGE)
for x in [80,960]:
 box(d,x,590,310,130,'Pago');box(d,x+400,590,310,130,'Inventario');arrow(d,(x+180,430),(x+160,590));arrow(d,(x+530,430),(x+560,590))
box(d,1040,850,550,120,'Base / API propietaria',GREY);arrow(d,(1115,720),(1170,850),'consulta');arrow(d,(1510,720),(1460,850),'consulta')
box(d,80,850,710,120,'Procesar la instantánea\ndel evento recibido',GREY)
footer(d,['Datos: menos consultas, más tráfico, contratos y versiones. Clave: menos tráfico, más dependencia de lectura.','Consultar el estado actual no reconstruye automáticamente el estado que existía cuando ocurrió el hecho.'])
save(im,'c15-03-payloads.png')

im,d=canvas('Granularidad: contexto suficiente y eventos con sentido','Síntesis de las figuras 15-13 a 15-17; payload y cantidad de eventos son ejes distintos')
for x,t,c in [(80,'Demasiado poco',ORANGE),(665,'Contexto del cambio',TEAL),(1250,'Demasiado disperso',ORANGE)]:
 d.text((x,220),t,font=font(33,True),fill=INK)
 box(d,x,320,470,190,{'Demasiado poco':'Perfil actualizado\nSolo ID del cliente','Contexto del cambio':'Perfil actualizado\nCampos modificados\nAntes / después','Demasiado disperso':'Dirección cambiada\nTeléfono cambiado\nCada campo por separado'}[t],c,size=28)
box(d,80,680,470,240,'No sé qué cambió\nni los valores previos',GREY,size=28)
box(d,665,680,470,240,'Decisión de negocio\ncon contexto suficiente',TEAL,size=28)
box(d,1250,680,470,240,'Más canales y eventos\npara una sola acción',GREY,size=28)
for x in [80,665,1250]:arrow(d,(x+235,510),(x+235,680))
footer(d,['Fraude detectado / no detectado separa resultados relevantes; un evento por campo puede crear un enjambre.','La frontera adecuada depende de la decisión de negocio que necesitan tomar los consumidores.'])
save(im,'c15-04-granularidad.png')

im,d=canvas('Workflow Event: delegar el error y continuar con otros mensajes','Recreación conceptual de las figuras 15-18 y 15-19')
box(d,70,300,300,120,'Cola original',TEAL);box(d,630,300,480,120,'Procesador de operaciones');arrow(d,(370,360),(630,360),'recibe')
box(d,1340,300,370,120,'Trabajo válido\ncontinúa',TEAL);arrow(d,(1110,360),(1340,360))
box(d,660,610,430,130,'Delegado de errores',ORANGE);arrow(d,(870,420),(870,610),'error + contexto')
box(d,80,840,450,120,'Corregir y reenviar',TEAL);arrow(d,(660,710),(530,900),'reparable');arrow(d,(170,840),(170,420),'reingresa')
box(d,1240,840,470,120,'Revisión humana',ORANGE);arrow(d,(1090,710),(1240,900),'sin solución segura')
footer(d,['El ejemplo corrige «8756 SHARES» a un número válido; no debe inventar la intención de una operación.','El reenvío cambia el orden. Si importa por cuenta, retener esa cuenta y permitir que las demás avancen.'])
save(im,'c15-05-errores.png')

im,d=canvas('Entrega fiable: cada confirmación cubre una frontera','Síntesis de figuras 15-20 y 15-21, con ampliación propia: outbox e idempotencia')
for x,t,c in [(60,'Productor\nDato + outbox',BLUE),(490,'Broker\nPersistencia',TEAL),(940,'Consumidor\nProcesamiento',BLUE),(1390,'Base del\nconsumidor',GREY)]:box(d,x,390,350,170,t,c,size=30)
for a,b,lab in [((410,450),(490,450),'envío'),((840,450),(940,450),'entrega'),((1290,450),(1390,450),'transacción')]:arrow(d,a,b,lab)
arrow(d,(490,650),(250,650),'confirmación del broker');arrow(d,(1140,750),(660,750),'ack después del commit')
box(d,90,860,740,140,'Si el efecto ocurrió y el ack se perdió:\nel mensaje puede llegar otra vez',ORANGE,size=29)
box(d,950,860,740,140,'event_id + efecto + registro procesado\nen una misma transacción local',TEAL,size=29)
footer(d,['Confirmar publicación no confirma la operación de negocio. Persistir un mensaje no basta para atomicidad global.','Outbox cubre la doble escritura del productor; idempotencia controla el efecto de entregas repetidas.'])
save(im,'c15-06-entrega.png')

im,d=canvas('Request-reply: transporte asíncrono, dependencia de una respuesta','Recreación de las figuras 15-22 y 15-23; ID de mensaje y correlación cumplen papeles distintos')
box(d,70,310,380,170,'Solicitante\nEnvia ID = 124');box(d,690,260,390,130,'Cola de solicitudes',TEAL);box(d,1330,310,390,170,'Consumidor\nProcesa solicitud')
arrow(d,(450,350),(690,325));arrow(d,(1080,325),(1330,350))
box(d,690,720,390,160,'Cola de respuestas\nID = 857\nCID = 124',TEAL,size=28)
arrow(d,(1510,480),(1080,800),'responde');arrow(d,(690,800),(250,480),'selecciona CID 124')
box(d,70,800,420,160,'Sin esa respuesta\nel solicitante no\npuede continuar',ORANGE,size=29)
footer(d,['El ID 857 identifica la respuesta; el CID 124 la conecta con la solicitud inicial.','Timeout significa que no llegó una respuesta a tiempo; por sí solo no demuestra que la acción haya fallado.'])
save(im,'c15-07-request-reply.png')

im,d=canvas('Mediador: estado, secuencia y decisiones explícitas','Síntesis de figuras 15-25 a 15-32; el mediador coordina y los procesadores ejecutan')
box(d,90,210,360,130,'Evento iniciador');arrow(d,(270,340),(270,450))
box(d,90,450,1620,200,'Mediador: estado del pedido + reglas + checkpoints',TEAL)
for x,t in [(60,'Registrar pedido'),(650,'Pago + inventario'),(1240,'Preparar + envío')]:
 box(d,x,850,500,150,t,BLUE,size=30)
 arrow(d,(x+190,650),(x+190,850));arrow(d,(x+380,850),(x+380,650))
 label(d,x+70,690,'orden de trabajo');label(d,x+320,765,'resultado')
footer(d,['El flujo del libro agrupa pasos paralelos y otros dependientes; los checkpoints marcan progreso del mediador.','Un coordinador exige durabilidad y recuperación de su estado. Sus comandos no hacen una transacción ACID global.'])
save(im,'c15-08-mediador.png')

im,d=canvas('Características de EDA: valoraciones ordinales del libro','Figura 15-39, PDF 52 / impresa 278. Cinco círculos = cinco estrellas, no una medición')
rows=[('Simplicidad',2),('Modularidad',4),('Mantenibilidad',4),('Testabilidad',2),('Desplegabilidad',3),('Evolución',5),('Capacidad de respuesta',5),('Escalabilidad',4),('Elasticidad',3),('Tolerancia a fallos',5)]
for i,(name,n) in enumerate(rows):
 y=230+i*70
 if i%2==0:d.rounded_rectangle((80,y-9,1180,y+49),radius=8,fill='#e8eef7')
 d.text((110,y),name,font=font(30),fill=INK)
 for j in range(5):d.ellipse((735+j*70,y,765+j*70,y+30),fill='#157c80' if j<n else '#d3dce6')
 d.text((1110,y),str(n),font=font(30,True),fill=INK)
box(d,1250,260,460,190,'Costo: $$$\nPartición: técnica\nQuanta: 1 a muchos',ORANGE,size=28)
box(d,1250,580,460,330,'Fortalezas:\nrespuesta y evolución\n\nCostes:\nflujos dinámicos\ny pruebas complejas',TEAL,size=28)
footer(d,['Las estrellas comparan tendencias del estilo: no predicen el comportamiento de cualquier implementación.','Base compartida y request-reply necesario pueden reunir varios procesadores en el mismo quantum.'])
save(im,'c15-09-caracteristicas.png')

im,d=canvas('Elegir un modelo: decidir por el trabajo y sus garantías','Síntesis de la tabla 15-2; puede haber solicitudes y eventos en la misma aplicación')
box(d,70,270,730,170,'Solicitud bien estructurada\nConsulta o respuesta inmediata',BLUE)
box(d,1000,270,730,170,'Hecho que provoca reacciones\nTrabajo paralelo o diferido',TEAL)
box(d,70,590,730,350,'Modelo de solicitudes\n\nControl explícito del recorrido\nResultado requerido para avanzar\nDependencia temporal de respuestas',GREY,size=30)
box(d,1000,590,730,350,'Modelo de eventos\n\nNuevas reacciones y extensibilidad\nMayor independencia temporal\nConsistencia y recuperación explícitas',GREY,size=30)
arrow(d,(440,440),(440,590));arrow(d,(1370,440),(1370,590))
footer(d,['«¿Ya aceptamos la puja?» puede exigir una decisión inmediata; «la puja fue aceptada» abre otras reacciones.','EDA no elimina invariantes: el diseño debe impedir que una puja inválida sea anunciada como aceptada.'])
save(im,'c15-10-decision.png')

im,d=canvas('Going, Going, Gone: aceptar una puja y difundir sus efectos','Recreación conceptual de figura 15-40; anunciar aceptación requiere validar primero')
box(d,70,330,360,160,'Usuario\nPuja: $100');box(d,650,310,440,200,'Captura de pujas\nComparar y aceptar');arrow(d,(430,410),(650,410))
box(d,650,690,440,130,'Puja registrada',TEAL);arrow(d,(870,510),(870,690))
for x,t in [(70,'Subastador\nActualizar precio'),(650,'Difusor\nTransmitir historial'),(1230,'Rastreador de pujador\nPersistir para auditoría')]:
 box(d,x,930,500,120,t,BLUE,size=29);arrow(d,(870,820),(x+250,930))
footer(d,['Tres reacciones consumen el mismo hecho sin obligar al usuario a esperar todas las tareas.','La concurrencia, el cierre y la validez de la puja requieren reglas propias además del canal de eventos.'])
save(im,'c15-11-subasta.png')

im,d=canvas('Cuatro topologías de datos: ¿quién lee y quién es dueño?','Síntesis original de figuras 15-33 a 15-38; las flechas representan acceso o copia, no eventos de negocio')
for x,y,title in [(70,220,'1 · Base compartida'),(960,220,'2 · Base compartida en caché'),(70,630,'3 · Bases por dominio'),(960,630,'4 · Base por procesador')]:
 d.text((x,y),title,font=font(33,True),fill=INK)
 for off,t in [(0,'A'),(240,'B'),(480,'C')]:box(d,x+off,y+65,190,85,'Procesador '+t,BLUE,size=23)
 if title.startswith('1'):
  box(d,x+120,y+240,520,90,'Una base común',GREY)
  for off in [0,240,480]:arrow(d,(x+off+95,y+150),(x+380,y+240))
 elif title.startswith('2'):
  box(d,x+120,y+240,520,90,'Caché → base común',TEAL)
  for off in [0,240,480]:arrow(d,(x+off+95,y+150),(x+380,y+240))
 elif title.startswith('3'):
  box(d,x,y+240,400,90,'Base del dominio AB',GREY,size=26);box(d,x+480,y+240,200,90,'Base C',GREY,size=26)
  arrow(d,(x+95,y+150),(x+120,y+240));arrow(d,(x+335,y+150),(x+280,y+240));arrow(d,(x+575,y+150),(x+580,y+240))
 else:
  for off,t in [(0,'Base A'),(240,'Base B'),(480,'Base C')]:box(d,x+off,y+240,190,90,t,GREY,size=26);arrow(d,(x+off+95,y+150),(x+off+95,y+240))
footer(d,['Compartir datos simplifica acceso y coordina cambios. Separarlos limita acceso directo y obliga a diseñar contratos.','La caché reduce lecturas, pero introduce invalidación y datos potencialmente antiguos. No elimina toda dependencia.'])
save(im,'c15-12-datos.png')


im,d=canvas('Responder antes no equivale a terminar antes','Figura 15-6, PDF 10 / impresa 236; números didácticos del libro, con el segundo tramo explícito')
box(d,70,260,740,180,'Síncrono\n50 + 3000 + 50 = 3100 ms',BLUE)
box(d,1000,260,730,180,'Asíncrono\nAceptación: 25 ms',TEAL)
box(d,70,650,740,280,'El usuario espera el resultado\n\nEl trabajo ocupa 3000 ms\n+ latencia de ida y vuelta',GREY,size=30)
box(d,1000,650,730,280,'El usuario recibe aceptación\n\nEl trabajo sigue pendiente\n25 + 25 + 3000 = 3050 ms',GREY,size=30)
arrow(d,(440,440),(440,650));arrow(d,(1370,440),(1370,650))
footer(d,['La prosa cuenta 3025 ms; la figura dibuja dos tramos de 25 ms. Se muestran ambas convenciones en las notas.','El tiempo real añade cola, persistencia y reintentos; aceptar un mensaje no confirma el resultado del negocio.'])
save(im,'c15-13-asincronia.png')

print('13 PNG generados')
