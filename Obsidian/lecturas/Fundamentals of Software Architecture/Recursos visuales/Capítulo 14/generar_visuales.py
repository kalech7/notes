"""Recreaciones didácticas originales del capítulo 14. uv run --with pillow generar_visuales.py"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).resolve().parent
W,H=1600,1100
BG='#F5F7FB'; INK='#15283D'; BLUE='#DCEBFA'; GREEN='#DDF2E6'; GOLD='#FFF0C7'; RED='#FBE2DF'; GRAY='#E8EAF0'
FONT=Path('/System/Library/Fonts/Supplemental/Arial.ttf')
BOLD=Path('/System/Library/Fonts/Supplemental/Arial Bold.ttf')
def font(n=27,b=False): return ImageFont.truetype(str(BOLD if b else FONT),n)
def base(title,subtitle):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    d.text((60,35),title,font=font(42,True),fill=INK)
    d.text((60,100),subtitle,font=font(25),fill=INK)
    d.text((60,H-45),'Fundamentals of Software Architecture · Capítulo 14 · Elaboración didáctica',font=font(19),fill=INK)
    return im,d
def txt(d,xy,s,size=27,b=False): d.multiline_text(xy,s,font=font(size,b),fill=INK,spacing=9)
def box(d,rect,s,color=BLUE,size=27):
    d.rounded_rectangle(rect,radius=20,fill=color,outline=INK,width=2)
    lines=s.split('\n'); f=font(size,True); x0,y0,x1,y1=rect
    height=len(lines)*(size+10)-10
    y=y0+(y1-y0-height)/2
    for line in lines:
        bounds=d.textbbox((0,0),line,font=f); width=bounds[2]-bounds[0]
        if width>x1-x0-18: raise ValueError('Texto excede caja: '+line)
        d.text((x0+(x1-x0-width)/2,y),line,font=f,fill=INK); y+=size+10
def arrow(d,a,b,color=INK,dashed=False,width=4):
    if dashed:
        dx=b[0]-a[0];dy=b[1]-a[1];dist=math.hypot(dx,dy)
        for q in range(0,int(dist),18):
            z=min(q+10,dist);d.line((a[0]+dx*q/dist,a[1]+dy*q/dist,a[0]+dx*z/dist,a[1]+dy*z/dist),fill=color,width=width)
    else:d.line((a,b),fill=color,width=width)
    ang=math.atan2(b[1]-a[1],b[0]-a[0]); n=15
    p=[b,(b[0]-n*math.cos(ang-.5),b[1]-n*math.sin(ang-.5)),(b[0]-n*math.cos(ang+.5),b[1]-n*math.sin(ang+.5))]
    d.polygon(p,fill=color)
def save(im,n):im.save(OUT/n)

im,d=base('Servicios de dominio: autonomía con datos compartidos','Recreación de la figura 14-1 y ejemplo propio de comercio')
box(d,(70,180,1530,285),'Interfaz de usuario · despliegue propio',GOLD)
names=['Pedidos','Clientes','Envíos','Informes']
for j,n in enumerate(names):
    x=70+j*390
    box(d,(x,405,x+290,580),f'{n}\nAPI + negocio\n+ persistencia',BLUE)
    arrow(d,(x+145,285),(x+145,405))
    arrow(d,(x+145,580),(800,730))
box(d,(490,730,1110,865),'Base de datos compartida\nSQL, tablas y transacciones',GREEN)
txt(d,(65,930),'Cada servicio se publica por separado. La base común conserva una dependencia compartida.',26)
save(im,'c14-01-topologia.png')

im,d=base('El tamaño del servicio cambia el costo del cambio','Figura 14-2 + contraste propio: modularidad interna y despliegue son fronteras diferentes')
for x,title in [(60,'Diseño interno por capas'),(840,'Diseño interno por subdominios')]:
    txt(d,(x,175),title,30,True)
    d.rounded_rectangle((x,240,x+700,745),radius=25,outline=INK,width=3)
    box(d,(x+35,275,x+665,365),'Fachada API',GOLD)
box(d,(95,420,725,540),'Lógica de negocio',BLUE)
box(d,(95,595,725,705),'Persistencia',GREEN)
arrow(d,(410,365),(410,420));arrow(d,(410,540),(410,595))
for j,n in enumerate(['Pedido','Pago','Stock']):
    x=875+j*210;box(d,(x,440,x+190,690),f'{n}\nReglas\nDatos',BLUE,size=25)
    arrow(d,(x+95,365),(x+95,440))
box(d,(80,820,740,990),'Cambio de regla de pedido\nSe prueba y publica TODO el servicio',RED,25)
box(d,(860,820,1520,990),'Separar módulos ayuda a entender\nNo crea despliegues independientes',GOLD,25)
save(im,'c14-02-interior.png')

im,d=base('Rollback local y compensación distribuida','Pedido y pago rechazado: comparación conceptual, no una implementación de pagos reales')
txt(d,(70,180),'Una transacción de base de datos',31,True)
box(d,(70,260,500,390),'Pedido e inventario\nCambios sin confirmar',BLUE)
arrow(d,(500,325),(650,325));box(d,(650,260,1050,390),'Validación rechazada',RED)
arrow(d,(1050,325),(1190,325));box(d,(1190,260,1530,390),'ROLLBACK\nSin pedido confirmado',GREEN,25)
txt(d,(80,435),'Límite: solo operaciones participantes en esa misma transacción.',27)
txt(d,(70,560),'Dos servicios y dos transacciones locales',31,True)
box(d,(70,650,500,790),'Servicio de pedidos\nCOMMIT: pendiente',BLUE)
arrow(d,(500,720),(650,720));box(d,(650,650,1050,790),'Servicio de pagos\nRechazo de tarjeta',RED)
arrow(d,(1050,720),(1190,720));box(d,(1190,650,1530,790),'Compensar pedido\nCOMMIT: cancelado',GREEN,25)
arrow(d,(1340,790),(1340,830),dashed=True)
arrow(d,(1340,830),(285,830),dashed=True)
arrow(d,(285,830),(285,790),dashed=True)
txt(d,(80,895),'Hay un estado intermedio observable. Cancelar es una acción nueva, que también puede fallar.',26)
txt(d,(80,960),'Un cobro externo no se deshace con ROLLBACK de la base local.',27,True)
save(im,'c14-03-transacciones.png')

im,d=base('Interfaces y gateway: dos decisiones independientes','Recreación combinada de figuras 14-3 y 14-4')
rows=[(190,'Una interfaz', [('UI común',340,1250)]),(390,'Por grupos\nde dominio',[('UI clientes',340,770),('UI interna',850,1280)]),(590,'Por servicio',[('UI A',340,525),('UI B',590,775),('UI C',840,1025),('UI D',1090,1275)])]
for y,label,uis in rows:
    txt(d,(65,y+25),label,27,True)
    for t,x0,x1 in uis:box(d,(x0,y,x1,y+110),t,GOLD,25)
box(d,(340,795,1275,895),'Gateway opcional · rutas, acceso, métricas, balanceo',GREEN,25)
for x,n in [(340,'A'),(590,'B'),(840,'C'),(1090,'D')]:
    box(d,(x,940,x+185,1010),'Servicio '+n,BLUE,23);arrow(d,(x+92,895),(x+92,940))
txt(d,(70,810),'Capa común\nfrente a servicios',24)
save(im,'c14-04-interfaces-gateway.png')

im,d=base('Bases compartidas, agrupadas o privadas','Recreación de figura 14-5: menor dependencia de datos exige resolver otras dependencias')
for r,label in enumerate(['Una base común','Bases por grupos','Una base por servicio']):
    y=190+r*280;txt(d,(60,y+30),label,28,True)
    for j in range(4):box(d,(450+j*265,y,650+j*265,y+90),'Servicio '+chr(65+j),BLUE,25)
    if r==0:
        box(d,(700,y+150,1200,y+245),'Base compartida',GREEN)
        for j in range(4):arrow(d,(550+j*265,y+90),(950,y+150))
    elif r==1:
        box(d,(450,y+150,660,y+245),'Base A',GREEN);box(d,(820,y+150,1390,y+245),'Base B, C y D',GREEN)
        arrow(d,(550,y+90),(550,y+150))
        for j in range(1,4):arrow(d,(550+j*265,y+90),(1110,y+150))
    else:
        for j in range(4):
            box(d,(450+j*265,y+150,650+j*265,y+245),'Base '+chr(65+j),GREEN,25)
            arrow(d,(550+j*265,y+90),(550+j*265,y+150))
save(im,'c14-05-datos.png')

im,d=base('El radio de un cambio depende de quién comparte su contrato','Recreación conceptual de figuras 14-6 y 14-7. Se cambia una tabla de facturación.')
txt(d,(60,175),'Biblioteca única de entidades',31,True)
txt(d,(840,175),'Bibliotecas separadas por dominio',31,True)
box(d,(70,265,740,365),'Cambio: tabla Facturación',RED)
box(d,(850,265,1520,365),'Cambio: tabla Facturación',RED)
box(d,(70,440,740,570),'Biblioteca global\nClientes + Facturas + Pedidos + Seguimiento',GOLD,25)
box(d,(850,440,1520,570),'Biblioteca de Facturación',GREEN)
arrow(d,(405,365),(405,440));arrow(d,(1185,365),(1185,440))
for x,n in [(70,'Clientes'),(250,'Facturas'),(430,'Pedidos'),(610,'Rastreo')]:
    box(d,(x,710,x+150,815),n,RED,23);arrow(d,(405,570),(x+75,710))
for x,n in [(850,'Clientes'),(1030,'Facturas'),(1210,'Pedidos'),(1390,'Rastreo')]:
    box(d,(x,710,x+150,815),n,GREEN if n=='Facturas' else GRAY,23)
arrow(d,(1185,570),(1105,710))
txt(d,(70,900),'El contrato compilado se propaga a todos.\nVersionar reduce coordinación, no borra el acoplamiento.',25)
txt(d,(850,900),'Solo cambia quien usa esa biblioteca.\nUna biblioteca «común» aún puede afectar a todos.',25)
save(im,'c14-06-cambios.png')

im,d=base('Going Green: siete servicios, dos zonas y escala selectiva','Figuras 14-9 y 14-10: acceso interno hacia datos públicos, sin camino público hacia el interior')
d.rounded_rectangle((55,170,1545,560),radius=22,fill=BLUE,outline=INK,width=2)
txt(d,(80,190),'Zona interna · dos interfaces · dependencia común de base interna',27,True)
for j,n in enumerate(['Recepción','Evaluación','Reciclaje','Contabilidad','Informes']):
    x=90+j*295;box(d,(x,280,x+240,375),n,GOLD,25);arrow(d,(x+120,375),(795,440))
box(d,(510,440,1080,525),'Base interna',GREEN)
txt(d,(60,585),'Firewall / separación de red',26,True)
d.line((60,630,1540,630),fill=INK,width=4)
d.rounded_rectangle((55,670,1545,1010),radius=22,fill=GOLD,outline=INK,width=2)
txt(d,(80,690),'Zona pública · web y kiosco · servicios que necesitan más instancias',27,True)
box(d,(110,770,580,870),'Cotizaciones · varias instancias',BLUE,25)
box(d,(700,770,1180,870),'Estado · varias instancias',BLUE,25)
box(d,(510,915,1080,985),'Base pública',GREEN)
arrow(d,(345,870),(640,915));arrow(d,(940,870),(940,915))
arrow(d,(210,375),(210,400),dashed=True)
arrow(d,(210,400),(40,400),dashed=True)
arrow(d,(40,400),(40,950),dashed=True)
arrow(d,(40,950),(510,950),dashed=True)
txt(d,(80,885),'Recepción escribe\nel estado público',20)
arrow(d,(1080,480),(1500,480),color='#9E6413',dashed=True)
arrow(d,(1500,480),(1500,950),color='#9E6413',dashed=True)
arrow(d,(1500,950),(1080,950),color='#9E6413',dashed=True)
txt(d,(1210,725),'Alternativa:\nsincronización\nentre las bases',22)
save(im,'c14-07-going-green.png')

im,d=base('Valoraciones del libro: una tabla ordinal, no una medición','Figura 14-8. Estrellas: apoyo débil (1) a fuerte (5). No se promedian ni expresan porcentajes.')
items=[('Simplicidad',3),('Modularidad',3),('Mantenibilidad',4),('Facilidad de pruebas',4),('Facilidad de despliegue',4),('Evolución',4),('Capacidad de respuesta',3),('Escalabilidad',3),('Elasticidad',2),('Tolerancia a fallos',3)]
def star(cx,cy):
    pts=[]
    for k in range(10):
        a=-math.pi/2+k*math.pi/5;r=16 if k%2==0 else 7
        pts.append((cx+r*math.cos(a),cy+r*math.sin(a)))
    d.polygon(pts,fill='#D39223',outline=INK)
for i,(label,n) in enumerate(items):
    y=190+i*67
    d.rounded_rectangle((65,y,1030,y+59),radius=8,fill='white' if i%2==0 else GRAY)
    txt(d,(85,y+11),label,26)
    for k in range(n):star(710+k*52,y+30)
box(d,(1100,220,1530,430),'Costo: $$\nPartición: dominio\nQuanta: uno a varios',GOLD,25)
box(d,(1100,540,1530,815),'Errata de la prosa\nPDF 15 afirma 4\nen tolerancia a fallos.\nLa tabla muestra 3.',RED,24)
txt(d,(70,920),'Son orientaciones sobre la variante habitual. Réplicas, UI y bases alteran el resultado real.',26)
save(im,'c14-08-caracteristicas.png')
