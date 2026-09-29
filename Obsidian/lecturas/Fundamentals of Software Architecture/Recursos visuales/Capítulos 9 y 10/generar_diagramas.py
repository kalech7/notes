"""Diagramas didácticos originales. Ejecutar con Python y Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).resolve().parent
INK = '#17324d'
BLUE = '#e3effb'
GREEN = '#e4f2e9'
GOLD = '#fff0d1'
RED = '#fbe3df'
GREY = '#edf0f4'
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'

def font(n=28, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, n)

def canvas(title, subtitle, h=1000):
    global im, d, H
    H=h
    im=Image.new('RGB',(1600,h),'white')
    d=ImageDraw.Draw(im)
    text(60,40,title,42,True)
    text(60,104,subtitle,25,False,'#526b80')
    d.line((60,153,1540,153),fill='#bccddb',width=2)

def text(x,y,s,n=28,b=False,c=INK):
    d.multiline_text((x,y),s,font=font(n,b),fill=c,spacing=10)

def box(x,y,w,h,s,color=BLUE,n=28):
    d.rounded_rectangle((x,y,x+w,y+h),radius=16,fill=color,outline=INK,width=2)
    bb=d.multiline_textbbox((0,0),s,font=font(n),spacing=9,align='center')
    assert bb[2] <= w-20, (s,bb,w)
    assert bb[3]-bb[1] <= h-15, (s,bb,h)
    d.multiline_text((x+(w-bb[2])/2,y+(h-(bb[3]-bb[1]))/2-bb[1]),s,font=font(n),fill=INK,spacing=9,align='center')

def arrow(points,c=INK,dashed=False):
    for a,b in zip(points,points[1:]):
        length=math.dist(a,b)
        if dashed:
            for k in range(0,int(length),18):
                u=k/length; v=min((k+9)/length,1)
                d.line((a[0]+(b[0]-a[0])*u,a[1]+(b[1]-a[1])*u,a[0]+(b[0]-a[0])*v,a[1]+(b[1]-a[1])*v),fill=c,width=4)
        else:d.line((a,b),fill=c,width=4)
    a,b=points[-2:];theta=math.atan2(b[1]-a[1],b[0]-a[0])
    d.polygon([b,(b[0]-16*math.cos(theta-.5),b[1]-16*math.sin(theta-.5)),(b[0]-16*math.cos(theta+.5),b[1]-16*math.sin(theta+.5))],fill=c)

def save(name,foot):
    text(60,H-55,foot,22,False,'#526b80')
    im.save(OUT/(name+'.png'))

canvas('¿Qué organizas primero: técnica o negocio?','Capítulo 9 · Elaboración propia sobre la partición de nivel superior',1050)
text(85,190,'PARTICIÓN TÉCNICA',30,True)
text(865,190,'PARTICIÓN POR DOMINIO',30,True)
for y,label in [(260,'Presentación'),(395,'Negocio'),(530,'Persistencia')]:
    box(80,y,640,105,'',BLUE)
    text(105,y+34,label,28,True)
    box(450,y+20,245,65,'Cambio de pedido',GOLD,23)
box(870,260,280,420,'Pedidos\n\nPresentación\nNegocio\nPersistencia',GREEN,28)
box(1190,260,330,195,'Inventario\nSus capas internas',BLUE)
box(1190,485,330,195,'Entregas\nSus capas internas',BLUE)
arrow([(575,365),(575,395)],'#a46800');arrow([(575,500),(575,530)],'#a46800')
box(80,755,640,165,'Una función cruza categorías técnicas.\nUn cambio puede tocar varias capas.\nLos contratos limitan su propagación.',GOLD,27)
box(870,755,650,165,'La función se agrupa en su dominio.\nPuede contener capas internas.\nLos cambios entre dominios aún coordinan.',GREEN,27)
save('c09-01-particion','Color dorado = cambio de negocio. Ambos diseños pueden vivir en un único despliegue.')

canvas('Un timeout no demuestra que el cobro falló','Capítulo 9 · Escenario inventado para explicar incertidumbre y reintentos',1100)
box(95,195,375,90,'Servicio de pedidos',BLUE)
box(1050,195,430,90,'Servicio de pagos',GREEN)
for x in (280,1265): d.line((x,300,x,810),fill='#96aabc',width=3)
text(90,335,'1',27,True);arrow([(280,360),(1265,360)]);text(490,311,'Cobrar: clave pedido-42',28)
box(1060,395,440,105,'2. Cobro confirmado\nResultado guardado',GREEN,27)
arrow([(1265,545),(785,545)],'#b04936',True);text(460,502,'3. Respuesta perdida',27,True,'#a44336')
text(780,525,'×',45,True,'#a44336')
box(65,590,480,100,'4. Timeout: resultado desconocido',RED,25)
arrow([(280,735),(1265,735)]);text(500,697,'5. Reintentar con la misma clave',27)
box(1020,775,485,95,'6. Devolver el resultado registrado',GREEN,25)
box(65,900,1440,92,'La idempotencia exige diseño y persistencia: no surge por añadir una clave al mensaje.',GOLD,27)
save('c09-02-respuesta-perdida','Flechas = mensajes en el tiempo. Ejemplo de mitigación; no garantiza entrega ni éxito de toda la operación.')

canvas('Distribuir añade tiempo y tráfico','Capítulo 9 · Aritmética explicada; cifras de ejemplo, no mediciones de producción',1050)
text(70,190,'LATENCIA: 10 LLAMADAS SECUENCIALES',30,True)
for i in range(10):
    box(75+i*145,270,125,80,'100 ms',BLUE,25)
    if i<9:arrow([(200+i*145,310),(220+i*145,310)])
text(80,393,'10 × 100 ms = 1.000 ms de comunicación',34,True)
text(80,447,'Faltan procesamiento, colas y otros accesos. No sumes percentiles p95 como si fueran medias.',25)
text(70,530,'DATOS: 2.000 RESPUESTAS POR SEGUNDO',30,True)
box(75,600,670,240,'Contrato amplio: 500 kB\n500.000 B × 2.000/s\n1.000.000.000 B/s = 1 GB/s\n8 Gbit/s',RED,30)
box(825,600,700,240,'Solo lo necesario: 200 B\n200 B × 2.000/s\n400.000 B/s = 400 kB/s\n3,2 Mbit/s',GREEN,30)
text(250,885,'2.500 veces menos carga útil transferida; cabeceras y reintentos se suman aparte.',27,True)
save('c09-03-latencia-datos','Unidades decimales: B = byte, bit = bit, 1 B = 8 bits. La escala de las cajas no representa volumen.')

canvas('Cuatro tipos de equipo, cuatro responsabilidades','Capítulo 9 · Síntesis didáctica de Team Topologies',1050)
box(470,390,660,195,'Equipo alineado con el flujo\nEntrega una capacidad de negocio\nEjemplo: completar un pedido',GREEN,31)
box(70,205,550,115,'Equipo habilitador\nEnseña una capacidad que falta',BLUE,28)
box(985,205,545,115,'Equipo de subsistema complicado\nEncapsula conocimiento especializado',GOLD,26)
box(460,740,680,115,'Equipo de plataforma\nOfrece servicios internos como producto',BLUE,29)
arrow([(345,320),(345,450),(470,450)]);arrow([(1260,320),(1260,450),(1130,450)]);arrow([(800,740),(800,585)])
text(65,640,'Apoyo: aprender a medir latencia',24)
text(1115,640,'Especialidad: optimización\nde rutas de entrega',24)
text(530,885,'La meta es reducir fricción y carga cognitiva.',29,True)
save('c09-04-equipos','Flechas = apoyo al flujo de valor, no llamadas de software. No hace falta crear cuatro equipos nuevos.')

canvas('Una capa lógica no es necesariamente un servidor','Capítulo 10 · Separación de responsabilidad y despliegue',1050)
text(90,190,'QUÉ RESPONSABILIDAD TIENE',30,True)
for y,label,color in [(260,'Presentación: entrada y salida',BLUE),(405,'Negocio: reglas del pedido',GREEN),(550,'Persistencia: acceso a datos',GOLD),(695,'Base de datos: guardar y consultar',GREY)]:
    box(85,y,650,100,label,color,29)
    if y<695:arrow([(410,y+100),(410,y+145)])
text(890,190,'DÓNDE SE EJECUTA · EJEMPLO',30,True)
d.rounded_rectangle((870,250,1510,640),radius=18,outline=INK,width=3)
text(900,275,'Un despliegue de aplicación',30,True)
for y,label in [(340,'Presentación'),(425,'Negocio'),(510,'Persistencia')]:box(920,y,540,65,label,BLUE,28)
box(920,730,540,100,'Servidor de base de datos',GREY,29)
arrow([(1190,640),(1190,730)]);text(1240,663,'Red',25)
text(90,880,'Cambiar de máquina es otra decisión: añade comunicación remota y operación.',28,True)
save('c10-01-capas-despliegue','Las flechas de la izquierda siguen una solicitud. El ejemplo no prescribe una única topología física.')

canvas('Abrir una capa no elimina las otras restricciones','Capítulo 10 · Negocio permanece cerrada; Servicios compartidos es abierta',1100)
for y,label,color in [(215,'Presentación',BLUE),(395,'Negocio · CERRADA',GREEN),(575,'Servicios compartidos · ABIERTA',GOLD),(795,'Persistencia · CERRADA',GREY)]:
    box(400,y,780,110,label,color,30)
arrow([(660,325),(660,395)]);arrow([(660,505),(660,575)]);arrow([(660,685),(660,795)])
arrow([(1180,450),(1510,450),(1510,850),(1180,850)],'#327858')
text(1210,610,'Permitido:\nNegocio puede\nsaltar Servicios',25,True,'#327858')
arrow([(400,270),(230,270),(230,630),(400,630)],'#ac4939',True)
text(62,365,'PROHIBIDO:\nPresentación\nsalta Negocio',24,True,'#ac4939')
text(215,465,'×',52,True,'#ac4939')
box(130,960,1340,70,'ABIERTA = se puede omitir esa capa en una ruta permitida. No significa acceso público.',GOLD,26)
save('c10-02-abiertas-cerradas','Flechas continuas = rutas permitidas; roja discontinua = violación de la capa cerrada.')

canvas('Sumidero arquitectónico: capas que solo reenvían','Capítulo 10 · Comparación de dos recorridos didácticos',1070)
text(80,190,'CONSULTA SIMPLE',30,True);text(855,190,'CONFIRMACIÓN DE PEDIDO',30,True)
left=['Presentación: pide nombre','Negocio: solo delega','Reglas: solo delega','Persistencia: consulta']
right=['Presentación: recibe pedido','Negocio: comprueba disponibilidad','Reglas: calcula descuento','Persistencia: guarda resultado']
for i in range(4):
    y=265+i*145
    box(75,y,675,100,left[i],RED if i in (1,2) else BLUE,27)
    box(855,y,675,100,right[i],GREEN if i in (1,2) else BLUE,27)
    if i<3:
        arrow([(410,y+100),(410,y+145)])
        arrow([(1190,y+100),(1190,y+145)])
box(75,865,675,120,'Medir frecuencia y coste real.\nUn paso corto puede proteger un contrato.',GOLD,26)
box(855,865,675,120,'Cada paso tiene una responsabilidad.\nEso no prueba que el flujo sea eficiente.',GREEN,26)
save('c10-03-sumidero','El criterio 80/20 del libro es heurístico. No es un umbral universal ni permiso automático para saltar capas.')

canvas('Replicar un monolito cambia el alcance de un fallo','Capítulo 10 · Ampliación didáctica: aislamiento interno, redundancia y datos',1080)
box(490,205,630,90,'Balanceador con comprobación de salud',BLUE,28)
for x,label,color in [(75,'Réplica A\nMemoria agotada\nFuera de servicio',RED),(600,'Réplica B\nTodas las capas\nSigue atendiendo',GREEN),(1125,'Réplica C\nTodas las capas\nSigue atendiendo',GREEN)]:
    box(x,405,400,190,label,color,29)
arrow([(650,295),(650,345),(275,345),(275,405)],'#ac4939',True)
arrow([(800,295),(800,405)],'#327858')
arrow([(950,295),(950,345),(1325,345),(1325,405)],'#327858')
box(440,735,720,120,'Base de datos compartida\nCapacidad y disponibilidad deben diseñarse',GOLD,29)
arrow([(800,595),(800,735)]);arrow([(1325,595),(1325,795),(1160,795)])
text(70,895,'Replicar aumenta capacidad total y puede mantener servicio ante la caída de una instancia.',27)
text(70,941,'No permite escalar solo Pagos ni evita fallos correlacionados, estado local o saturación de datos.',26)
save('c10-04-fallos-escala','Hipótesis: réplicas intercambiables, balanceo sano y dependencias disponibles. No es garantía de alta disponibilidad.')
