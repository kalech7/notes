from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
P=Path(__file__).resolve().parent
F='/System/Library/Fonts/Supplemental/Arial.ttf';B='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
COL={'ink':'#17324d','bg':'#f7f9fc','blue':'#dceaff','teal':'#d6f4ec','amber':'#ffe9bd','soft':'#edf1f7'}
def font(n,b=False):return ImageFont.truetype(B if b else F,n)
def label(d,xy,text,n=27,b=False,c=None):d.text(xy,text,font=font(n,b),fill=c or COL['ink'])
def center(d,xy,text,n=26):
 bb=d.multiline_textbbox((0,0),text,font=font(n),spacing=8,align='center');x=(xy[0]+xy[2]-(bb[2]-bb[0]))/2;y=(xy[1]+xy[3]-(bb[3]-bb[1]))/2;d.multiline_text((x,y),text,font=font(n),spacing=8,fill=COL['ink'],align='center')
def box(d,xy,text='',color='blue',n=26,width=3):
 d.rounded_rectangle(xy,16,fill=COL[color],outline=COL['ink'],width=width)
 if text:center(d,xy,text,n)
def arrow(d,a,b):
 d.line([a,b],fill=COL['ink'],width=4);x,y=b
 if x>a[0]:poly=[(x,y),(x-14,y-9),(x-14,y+9)]
 elif x<a[0]:poly=[(x,y),(x+14,y-9),(x+14,y+9)]
 elif y>a[1]:poly=[(x,y),(x-9,y-14),(x+9,y-14)]
 else:poly=[(x,y),(x-9,y+14),(x+9,y+14)]
 d.polygon(poly,fill=COL['ink'])
def page(title,sub):
 im=Image.new('RGB',(1800,1260),COL['bg']);d=ImageDraw.Draw(im);label(d,(65,40),title,42,True);label(d,(65,103),sub,27);return im,d
im,d=page('Cuatro estilos: cuatro maneras de separar el trabajo','Las cajas de borde grueso son unidades de despliegue en estas variantes típicas.')
for x,y,title in [(55,170,'11 · Monolito modular'),(925,170,'12 · Pipeline'),(55,710,'13 · Microkernel'),(925,710,'14 · Basada en servicios')]:
 d.rounded_rectangle((x,y,x+820,y+500),20,outline='#bac7d5',width=2);label(d,(x+30,y+25),title,33,True)
x,y=55,170
box(d,(x+35,y+100,x+785,y+325),'','soft',width=5)
for i,text in enumerate(['Pedidos','Pagos','Envíos']):box(d,(x+70+i*235,y+155,x+280+i*235,y+265),text,'blue')
label(d,(x+35,y+355),'Agrupa responsabilidades por área del negocio.',26)
label(d,(x+35,y+400),'Una entrega contiene todos los módulos.',26)
x,y=925,170
box(d,(x+35,y+100,x+785,y+325),'','soft',width=5)
for i,text in enumerate(['Leer','Validar','Calcular','Guardar']):
 z=x+65+i*185;box(d,(z,y+160,z+145,y+255),text,'blue',24)
 if i<3:arrow(d,(z+145,y+207),(z+185,y+207))
label(d,(x+35,y+355),'Agrupa tareas por etapas de procesamiento.',26)
label(d,(x+35,y+400),'Los datos avanzan por canales definidos.',26)
x,y=55,710
box(d,(x+35,y+100,x+785,y+335),'','soft',width=5)
box(d,(x+300,y+155,x+530,y+275),'Núcleo','teal',30)
box(d,(x+65,y+120,x+250,y+205),'Plugin A','amber');box(d,(x+65,y+235,x+250,y+315),'Plugin B','amber');box(d,(x+585,y+178,x+750,y+260),'Plugin C','amber')
arrow(d,(x+300,y+183),(x+250,y+183));arrow(d,(x+300,y+260),(x+250,y+260));arrow(d,(x+530,y+218),(x+585,y+218))
label(d,(x+35,y+365),'Un núcleo estable coordina extensiones.',26)
label(d,(x+35,y+410),'Los plugins aíslan variaciones específicas.',26)
x,y=925,710
box(d,(x+65,y+100,x+750,y+165),'Interfaz de usuario','soft',26,width=5)
for i,text in enumerate(['Pedidos','Pagos','Envíos']):
 z=x+65+i*245;box(d,(z,y+225,z+200,y+300),text,'blue',26,width=5);arrow(d,(z+100,y+165),(z+100,y+225));arrow(d,(z+100,y+300),(z+100,y+337))
d.line([(x+165,y+337),(x+655,y+337)],fill=COL['ink'],width=4);arrow(d,(x+410,y+337),(x+410,y+355));box(d,(x+260,y+355,x+560,y+410),'Base compartida','teal',25)
label(d,(x+35,y+440),'Servicios gruesos con despliegues separados.',26)
im.save(P/'comparacion-01-cuatro-estilos.png')
im,d=page('Independencia: código, publicación, datos y fallos','Separar componentes ayuda, pero cada frontera protege una dimensión diferente.')
rows=[('Código','Puedo cambiar el cálculo sin reescribir la captura.','Contratos y responsabilidades claras.'),('Publicación','Puedo desplegar Pedidos sin desplegar Pagos.','Artefactos y compatibilidad de versiones.'),('Datos','Puedo cambiar mi esquema sin romper otro servicio.','Propiedad de datos y accesos controlados.'),('Fallos','Un fallo grave en una pieza no derriba las demás.','Procesos, recursos y dependencias aislados.')]
for i,(dim,ex,condition) in enumerate(rows):
 y=190+i*225;box(d,(65,y,395,y+175),dim,'blue',34);box(d,(440,y,1720,y+175),'','soft');label(d,(475,y+30),ex,30,True);label(d,(475,y+98),'Requiere: '+condition,28)
label(d,(65,1150),'Un servicio separado que comparte esquema o dependencia crítica conserva acoplamiento.',29,True)
im.save(P/'comparacion-02-independencia.png')
