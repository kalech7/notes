#!/usr/bin/env python3
"""Recreaciones explicativas de DDIA, capítulo 6.

Regenerar: uv run --with pillow python generar_figuras.py
Diagramas propios en español contrastados con los escaneos; no recortes del libro.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math, json

OUT = Path(__file__).resolve().parent
W = 1800
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def font(n=27, bold=False):
    try: return ImageFont.truetype(BOLD if bold else FONT,n)
    except OSError: return ImageFont.load_default(size=n)
PAGES = [3,4,14,17,18,20,22,23,27,30,31,34,36,42,44,46]
manifest=[]

class Fig:
    def __init__(self,n,title,h=850,sub=''):
        self.n,self.h=n,h
        self.im=Image.new('RGB',(W,h),'white'); self.d=ImageDraw.Draw(self.im)
        self.text((55,30),f'6-{n} · {title}',size=38,bold=True)
        if sub:self.text((55,84),sub,size=25)
        self.d.rectangle((40,130,W-40,h-92),outline='#777777',width=2)
        p=PAGES[n-1]
        self.text((55,h-64),f'Adaptación didáctica de figura 6-{n} · DDIA 2.ª ed. · PDF {p} / impresa {p+196}',size=23)
    def text(self,xy,text,size=27,bold=False,anchor='la',white=False,fill='#111111'):
        f=font(size,bold)
        bbox=self.d.multiline_textbbox(xy,text,font=f,anchor=anchor,spacing=8)
        if bbox[0]<0 or bbox[2]>W or bbox[1]<0 or bbox[3]>self.h:raise ValueError((self.n,text,bbox))
        if white:self.d.rectangle((bbox[0]-7,bbox[1]-5,bbox[2]+7,bbox[3]+5),fill='white')
        self.d.multiline_text(xy,text,font=f,fill=fill,anchor=anchor,spacing=8)
    def arrow(self,a,b,dash=False,width=3,fill='#111111'):
        x1,y1=a;x2,y2=b
        if dash:
            length=math.hypot(x2-x1,y2-y1)
            for t in range(0,int(length),16):
                end=min(t+6,length)
                self.d.line((x1+(x2-x1)*t/length,y1+(y2-y1)*t/length,x1+(x2-x1)*end/length,y1+(y2-y1)*end/length),fill=fill,width=2)
        else:self.d.line((a,b),fill=fill,width=width)
        angle=math.atan2(y2-y1,x2-x1); size=13
        self.d.polygon([b,(x2-size*math.cos(angle-.45),y2-size*math.sin(angle-.45)),(x2-size*math.cos(angle+.45),y2-size*math.sin(angle+.45))],fill=fill)
    def box(self,x,y,w,h,label,size=27,shade=False):
        self.d.rectangle((x,y,x+w,y+h),outline='#111111',fill='#eeeeee' if shade else 'white',width=2)
        self.text((x+w/2,y+h/2),label,size=size,anchor='mm')
    def curve(self,p0,p1,p2,p3):
        points=[]
        for i in range(101):
            t=i/100;u=1-t
            points.append(tuple(u*u*u*p0[k]+3*u*u*t*p1[k]+3*u*t*t*p2[k]+t*t*t*p3[k] for k in [0,1]))
        self.d.line(points,fill='#111111',width=3)
        self.arrow(points[-3],points[-1])
    def db(self,x,y,label='',w=110,h=95,size=27):
        self.d.rectangle((x-w/2,y-h/2+12,x+w/2,y+h/2-12),fill='white')
        self.d.arc((x-w/2,y+h/2-24,x+w/2,y+h/2),0,180,fill='#111111',width=2)
        self.d.line((x-w/2,y-h/2+12,x-w/2,y+h/2-12),fill='#111111',width=2)
        self.d.line((x+w/2,y-h/2+12,x+w/2,y+h/2-12),fill='#111111',width=2)
        self.d.ellipse((x-w/2,y-h/2,x+w/2,y-h/2+24),fill='white',outline='#111111',width=2)
        if label:self.text((x,y+h/2+15),label,size=size,anchor='ma')
    def person(self,x,y):
        self.d.ellipse((x-15,y-34,x+15,y-4),outline='#111111',fill='#dddddd',width=2)
        self.d.polygon([(x-22,y+28),(x-20,y+5),(x-10,y-2),(x+10,y-2),(x+20,y+5),(x+22,y+28)],fill='#dddddd',outline='#111111')
    def lanes(self,labels,step=135,y=205):
        ys=[]
        for i,name in enumerate(labels):
            yy=y+i*step;ys.append(yy)
            shown=name.replace(' · ','\n').replace('Base de datos','Base de\ndatos')
            self.text((235,yy),shown,size=25,anchor='rm')
            if any(s in name.lower() for s in ['líder','réplica','seguidor','base','nodo','copia']):self.db(270,yy,w=48,h=54)
            else:self.person(270,yy)
            self.arrow((320,yy),(1700,yy),dash=True,fill='#999999')
        self.text((1690,y-48),'Tiempo',size=25,anchor='ra')
        return ys
    def bar(self,x1,x2,y):self.d.line((x1,y,x2,y),fill='#111111',width=5)
    def save(self,explanation,note):
        file=f'figura-6-{self.n:02}.png';self.im.save(OUT/file)
        final_notes=[1,2,5,6,6,7,7,7,9,9,10,11,11,13,13,13]
        manifest.append(dict(file=file,figure=f'6-{self.n}',pdf=PAGES[self.n-1],printed=PAGES[self.n-1]+196,note_number=final_notes[self.n-1],explanation=explanation))

# 6-1: arquitectura, escritura y lecturas.
f=Fig(1,'Un líder recibe las escrituras y propaga los cambios',830)
f.person(170,405);f.text((170,475),'Usuario 1234\nactualiza su foto',anchor='ma')
f.db(600,405,'Líder',w=145,h=140)
f.db(1240,275,'Seguidor 1',w=130,h=120)
f.db(1240,525,'Seguidor 2',w=130,h=120)
f.person(1620,525);f.text((1620,590),'Usuario 2345\nconsulta el perfil',anchor='ma')
f.arrow((215,405),(520,405));f.text((360,320),'Escritura\nnueva.jpg',anchor='ma')
f.arrow((675,390),(1175,280));f.arrow((675,420),(1175,525))
f.text((910,355),'Flujo de replicación',anchor='ma',white=True)
f.text((905,525),'Cambio del registro 1234:\nfoto: vieja.jpg → nueva.jpg',anchor='ma')
f.arrow((1575,525),(1310,525));f.text((1450,445),'Lectura',anchor='ma')
f.save('El usuario que modifica la foto envía la escritura al líder. El líder guarda el cambio y lo transmite a sus seguidores, dibujados como cilindros. Otra persona puede consultar un seguidor: recibe la copia que este haya alcanzado a aplicar. Las flechas de replicación transportan cambios de datos; la aplicación no escribe directamente en los seguidores.',1)

# 6-2: seguidores síncrono y asíncrono.
f=Fig(2,'Cuándo puede confirmarse una escritura',920,'El tiempo avanza a la derecha; las flechas inclinadas son mensajes.')
u,l,s1,s2=f.lanes(['Usuario 1234','Líder','Seguidor 1','Seguidor 2'])
f.text((400,u-60),'Actualizar foto',size=25);f.arrow((420,u),(560,l))
f.arrow((620,l),(795,s1));f.arrow((835,s1),(1035,l));f.bar(560,1060,l)
f.arrow((1060,l),(1200,u));f.text((1110,265),'OK al usuario',white=True,size=25)
f.arrow((620,l),(1410,s2));f.arrow((1470,s2),(1630,l))
f.text((820,l-52),'Espera el OK del seguidor 1',size=25,anchor='ma',white=True)
f.text((830,s1+42),'Síncrono: confirma antes del OK al usuario',size=25,anchor='ma')
f.text((1320,s2+42),'Asíncrono: puede terminar después',size=25,anchor='ma')
f.save('El líder espera la confirmación del seguidor 1 antes de responder al usuario: ese seguidor participa de forma síncrona. La flecha hacia el seguidor 2 tarda más y su confirmación llega después del éxito comunicado al usuario. Esa segunda réplica es asíncrona. Una escritura confirmada, por tanto, no implica que todas las copias estén actualizadas.',2)

# 6-3: no leer la propia escritura.
f=Fig(3,'El comentario está guardado, pero todavía no se ve',920)
u,l,s1,s2=f.lanes(['Usuario 1234','Líder','Seguidor 1','Seguidor 2'])
f.text((390,u-60),'Publicar comentario',size=25);f.arrow((420,u),(560,l));f.arrow((610,l),(755,u))
f.arrow((610,l),(810,s1));f.arrow((610,l),(1600,s2));f.text((760,u-53),'OK',size=25)
f.arrow((980,u),(1120,s2));f.bar(1120,1190,s2);f.arrow((1190,s2),(1370,u))
f.text((1040,u-58),'Consultar comentarios',size=25)
f.text((1470,u-53),'«No hay resultados»',size=27,anchor='ma')
f.text((1590,s2+40),'El comentario\nllega más tarde',size=25,anchor='ra')
f.save('El comentario llega al líder y recibe un OK. La consulta posterior se dirige al seguidor 2 cuando la replicación todavía está en camino, por lo que devuelve una lista vacía. El dato no desapareció: el usuario leyó una copia atrasada. Leer las propias escrituras exige dirigir esa lectura a una réplica que ya haya aplicado el cambio.',5)

# 6-4: lectura monótona.
f=Fig(4,'Cambiar de réplica puede hacer que el tiempo parezca retroceder',1050)
u,l,s1,s2,v=f.lanes(['Usuario 1234','Líder','Seguidor 1','Seguidor 2','Usuario 2345'])
f.arrow((410,u),(540,l));f.arrow((590,l),(730,u));f.arrow((590,l),(790,s1));f.arrow((590,l),(1590,s2))
f.text((410,u-60),'Publicar comentario',size=25)
f.arrow((860,v),(950,s1));f.bar(950,1015,s1);f.arrow((1015,s1),(1130,v))
f.arrow((1250,v),(1340,s2));f.bar(1340,1410,s2);f.arrow((1410,s2),(1500,v))
f.text((1000,v+36),'Primera consulta:\n1 comentario',size=25,anchor='ma')
f.text((1430,v+36),'Segunda consulta:\n0 comentarios',size=25,anchor='ma')
f.text((1640,s2-65),'Replicación pendiente',size=24,anchor='ra',white=True)
f.save('La primera consulta del usuario 2345 llega al seguidor 1 y encuentra el comentario. La segunda consulta llega al seguidor 2, que sigue atrasado, y el comentario deja de verse. Las lecturas monótonas impiden este retroceso para una misma persona: una lectura posterior no debe devolver un estado más antiguo que el ya observado.',5)

# 6-5: causalidad entre shards.
f=Fig(5,'Una respuesta puede verse antes que su pregunta',1210,'P = pregunta; R = respuesta. La respuesta depende de haber recibido la pregunta.')
ys=f.lanes(['Sr. Poons','Shard 1 · líder','Shard 1 · copia','Sra. Cake','Shard 2 · líder','Shard 2 · copia','Observador'],step=125,y=205)
a,l1,s1,b,l2,s2,o=ys
f.arrow((420,a),(520,l1));f.arrow((550,l1),(690,b));f.arrow((550,l1),(1410,s1));f.arrow((1450,s1),(1590,o))
f.arrow((835,b),(935,l2));f.arrow((960,l2),(1100,s2));f.arrow((960,l2),(1140,a));f.arrow((1140,s2),(1260,o))
f.text((420,a-62),'P: ¿Cuánto futuro puedes ver?',size=25)
f.text((815,b-64),'R: unos 10 segundos',size=25,white=True)
f.text((1250,o+40),'1.º llega R',size=27,anchor='ma');f.text((1570,o+40),'2.º llega P',size=27,anchor='ma')
f.save('Poons escribe la pregunta en el shard 1 y Cake la conoce antes de contestar en el shard 2. La copia del shard 1 tarda más en ponerse al día, mientras la del shard 2 entrega pronto la respuesta al observador. Así, el observador recibe el efecto antes que su causa. Un prefijo consistente o un mecanismo que preserve las dependencias causales evita esa historia incompleta.',5)

# 6-6: dos regiones.
f=Fig(6,'Cada región puede aceptar escrituras localmente',900)
f.d.rectangle((85,230,780,650),outline='#777777',width=2);f.d.rectangle((1020,230,1715,650),outline='#777777',width=2)
f.text((110,250),'Región 1',bold=True);f.text((1040,250),'Región 2',bold=True)
f.box(195,325,230,80,'Resolver\nconflictos',size=25);f.box(1385,325,230,80,'Resolver\nconflictos',size=25)
f.db(310,500,w=150,h=120);f.db(625,500,w=150,h=120)
f.db(1175,500,w=150,h=120);f.db(1500,500,w=150,h=120)
for x,t in [(310,'Líder\nzona 1A'),(625,'Copia\nzona 1B'),(1175,'Copia\nzona 2B'),(1500,'Líder\nzona 2A')]:f.text((x,507),t,size=24,anchor='mm')
f.arrow((385,500),(560,500));f.arrow((1425,500),(1240,500));f.arrow((310,438),(310,405));f.arrow((1500,438),(1500,405))
f.curve((385,500),(600,1000),(850,170),(1500,325))
f.curve((1425,500),(1210,1000),(950,170),(310,325))
f.text((900,420),'Replicación\nentre regiones',anchor='mm',white=True,size=25)
f.person(310,725);f.person(1500,725);f.arrow((310,682),(310,566));f.arrow((1500,682),(1500,566))
f.text((580,704),'Lecturas y escrituras locales',anchor='ma');f.text((1240,704),'Lecturas y escrituras locales',anchor='ma')
f.save('Cada región tiene un líder que atiende las escrituras de sus usuarios y transmite cambios a una copia local. Las flechas entre regiones conectan los líderes de forma asíncrona. Esa independencia permite seguir trabajando durante una desconexión entre regiones, pero también hace posible que dos líderes cambien el mismo dato antes de conocer el cambio ajeno; por eso aparecen los bloques de resolución de conflictos.',6)

# 6-7: topologías.
f=Fig(7,'Tres maneras de conectar los líderes',820)
for mode,cx in enumerate([330,900,1470]):
    pts=[(cx,270),(cx+150,450),(cx,620),(cx-150,450)]
    if mode==0:edges=[(0,1),(1,2),(2,3),(3,0)]
    elif mode==1:edges=[(0,1),(1,0),(0,2),(2,0),(0,3),(3,0)]
    else:edges=[(a,b) for a in range(4) for b in range(4) if a!=b]
    for a,b in edges:
        x1,y1=pts[a];x2,y2=pts[b];dx=x2-x1;dy=y2-y1;length=math.hypot(dx,dy)
        shift=9 if mode>0 else 0
        f.arrow((x1+dx/length*55-dy/length*shift,y1+dy/length*55+dx/length*shift),(x2-dx/length*55-dy/length*shift,y2-dy/length*55+dx/length*shift),width=2)
    for i,(x,y) in enumerate(pts):f.db(x,y,w=75,h=80)
    f.text((cx,695),['(a) Circular','(b) Estrella','(c) Todos con todos'][mode],anchor='ma',bold=True)
f.save('Los cilindros representan líderes y las flechas indican qué nodos transmiten escrituras directamente a cuáles. En el anillo, un cambio pasa de nodo en nodo. En la estrella, un nodo central redistribuye los cambios. En todos con todos, cada líder envía cambios a los demás; hay rutas alternativas, aunque los distintos retrasos de red todavía pueden alterar el orden de llegada.',6)

# 6-8: update antes de insert.
f=Fig(8,'Un cambio dependiente llega antes de crear su fila',1050,'A crea x = 1; B conoce esa fila y después incrementa x a 2.')
a,l1,l2,l3,b=f.lanes(['Cliente A','Líder 1','Líder 2','Líder 3','Cliente B'])
f.arrow((400,a),(520,l1));f.arrow((560,l1),(680,a));f.arrow((560,l1),(840,l3));f.arrow((560,l1),(1570,l2))
f.arrow((880,b),(990,l3));f.arrow((1040,l3),(1170,b));f.arrow((1040,l3),(1230,l2));f.arrow((1040,l3),(1240,l1))
f.text((400,a-62),'INSERT x = 1',size=25);f.text((900,b+36),'UPDATE x = x + 1',size=25)
f.text((1250,l2-58),'1.º UPDATE x = 2',size=25,anchor='ma',white=True)
f.text((1575,l2+37),'2.º INSERT x = 1',size=25,anchor='ra')
f.save('La inserción de A llega pronto al líder 3, por lo que B puede incrementar la fila ya creada. Sin embargo, el mensaje original hacia el líder 2 viaja despacio y la actualización lo adelanta. El líder 2 intenta modificar una fila que aún no existe. No son escrituras concurrentes: el UPDATE depende del INSERT, y esa dependencia debe respetarse al aplicar la replicación.',6)

# 6-9: conflicto títulos.
f=Fig(9,'Dos títulos válidos localmente entran en conflicto',920,'Estado inicial en ambos líderes: título A. Ninguna escritura conoce la otra.')
u,l1,l2,v=f.lanes(['Usuario 1','Líder 1','Líder 2','Usuario 2'],step=160)
f.arrow((430,u),(550,l1));f.arrow((600,l1),(730,u));f.arrow((430,v),(550,l2));f.arrow((600,l2),(730,v))
f.arrow((650,l1),(1390,l2));f.arrow((650,l2),(1390,l1))
f.text((440,u-58),'Cambiar A → B',size=27);f.text((440,v+35),'Cambiar A → C',size=27)
f.text((1360,l1-76),'Aquí ya hay B:\nrecibo A → C',size=27,anchor='ma',white=True)
f.text((1360,l2+38),'Aquí ya hay C:\nrecibo A → B',size=27,anchor='ma')
f.save('Ambos líderes parten del título A. Uno acepta B y el otro acepta C, y cada usuario recibe confirmación antes de que los líderes intercambien cambios. Al replicar, cada líder descubre una modificación incompatible con la suya. La concurrencia significa que ninguna modificación se basó en la otra, aunque sus relojes indiquen horas diferentes.',7)

# 6-10: union cart resurrect.
f=Fig(10,'Unir los carritos puede resucitar elementos eliminados',940,'Ambos dispositivos parten de {DVD, libro}. La unión conserva presencia, pero olvida borrados.')
a,l1,l2,b=f.lanes(['Dispositivo 1','Líder 1','Líder 2','Dispositivo 2'],step=160)
f.arrow((490,a),(620,l1));f.arrow((670,l1),(800,a));f.arrow((490,b),(620,l2));f.arrow((670,l2),(800,b))
f.arrow((780,l1),(1370,l2));f.arrow((780,l2),(1370,l1))
f.text((400,a-62),'Quitar libro; añadir jabón',size=27)
f.text((420,b+40),'Quitar DVD',size=27)
f.text((810,l1-55),'{DVD, jabón}',size=27,anchor='ma',white=True)
f.text((810,l2+36),'{libro}',size=27,anchor='ma')
f.text((1400,l1-50),'Unión: {DVD, libro, jabón}',size=27,anchor='ma',white=True)
f.text((1400,l2+40),'Unión: {DVD, libro, jabón}',size=27,anchor='ma')
f.save('El dispositivo 1 elimina el libro y añade jabón; el dispositivo 2 elimina el DVD. Si el servidor fusiona únicamente mediante la unión de los conjuntos que recibe, conserva el DVD de una rama y el libro de la otra: reaparecen ambos artículos borrados. Registrar también las operaciones de eliminación permite conservar su intención y obtener únicamente {jabón} en este ejemplo.',7)

# 6-11: diamonds OT vs CRDT.
f=Fig(11,'OT transforma posiciones; un CRDT conserva identidades',1120,'Ejemplo del libro: ambas ramas parten de ice y terminan en nice!. Etiquetas de código conservadas.')
f.d.line((900,150,900,960),fill='#aaaaaa',width=2)
def textnode(x,y,text,ids):
    n=len(text); width=n*49
    for i,ch in enumerate(text):
        f.box(x-width/2+i*49,y,49,60,ch,size=34)
    f.text((x,y+76),'   '.join(ids),size=23,anchor='ma',fill='#666666')
for off,title in [(0,'Transformación operacional (OT)'),(880,'CRDT para texto')]:
    f.text((off+440,170),title,bold=True,size=29,anchor='ma')
    textnode(off+170,495,'ice',['0','1','2'] if off==0 else ['1A','2A','3A'])
    textnode(off+465,310,'nice',['0','1','2','3'] if off==0 else ['4A','1A','2A','3A'])
    textnode(off+465,740,'ice!',['0','1','2','3'] if off==0 else ['1A','2A','3A','4B'])
    textnode(off+740,495,'nice!',['0','1','2','3','4'] if off==0 else ['4A','1A','2A','3A','4B'])
    f.arrow((off+235,480),(off+365,370));f.arrow((off+245,570),(off+365,740));f.arrow((off+560,370),(off+618,515));f.arrow((off+560,740),(off+618,540))
    if off==0:
        f.text((off+160,245),'Usuario 1:\ninsert(0, "n")',size=25)
        f.text((off+110,850),'Usuario 2: insert(3, "!")',size=25)
        f.text((off+560,255),'Se transforma a:\ninsert(4, "!")',size=25)
        f.text((off+555,855),'insert(0, "n")\nno cambia',size=25)
    else:
        f.text((off+120,245),'Usuario 1:\ninsert(nil, 4A, "n")',size=25)
        f.text((off+110,850),'Usuario 2:\ninsert(3A, 4B, "!")',size=25)
        f.text((off+545,255),'insert(3A, 4B, "!")\nno cambia',size=24)
        f.text((off+550,855),'insert(nil, 4A, "n")\nno cambia',size=24)
f.save('Los dos rombos muestran las mismas ediciones: una persona añade n al inicio de ice y otra añade ! al final. En OT, insertar n desplaza las posiciones, por lo que la inserción de ! debe transformarse de índice 3 a índice 4. En el CRDT ilustrado, cada carácter tiene una identidad estable: ! se inserta después de 3A y no hay que cambiar esa referencia cuando aparece n. Ambos mecanismos hacen que las dos ramas converjan en nice!, aunque internamente representan y combinan las operaciones de maneras diferentes.',7)

# 6-12: reparación de lectura, simplificación tiempos.
f=Fig(12,'Leer varias copias permite detectar y reparar una atrasada',1070,'Secuencia simplificada: n = 3, w = 2, r = 2. La versión 7 reemplaza a la versión 6.')
a,r1,r2,r3,b=f.lanes(['Usuario 1234','Réplica 1','Réplica 2','Réplica 3','Usuario 2345'],step=145)
f.arrow((400,a),(560,r1));f.arrow((400,a),(570,r2));f.arrow((400,a),(510,r3))
f.text((510,r3-45),'× desconectada',size=25,white=True)
f.arrow((610,r1),(780,a));f.arrow((620,r2),(810,a));f.text((420,a-60),'Escribir foto · v7',size=25)
f.arrow((960,b),(1080,r1));f.arrow((960,b),(1090,r3));f.arrow((1150,r1),(1340,b));f.arrow((1150,r3),(1240,b))
f.text((1180,r1-47),'v7 · nueva.jpg',size=25,white=True)
f.text((1160,r3+39),'v6 · vieja.jpg',size=25,white=True)
f.arrow((1410,b),(1540,r3));f.arrow((1580,r3),(1660,b));f.text((1470,b+45),'Reparar réplica 3 con v7',size=25,anchor='ma')
f.save('La escritura de la nueva foto se confirma en las réplicas 1 y 2 aunque la réplica 3 esté desconectada. Después, la lectura de dos copias recibe tanto la versión 7 como la versión 6, detecta cuál quedó atrasada y devuelve la nueva foto. La flecha final transmite la versión 7 a la réplica 3: es reparación en lectura. El dibujo simplifica el número de solicitudes para destacar el quórum y la reparación.',8)

# 6-13: quorum sets.
f=Fig(13,'Dos mayorías de cinco réplicas siempre comparten alguna',950,'n = 5 · w = 3 · r = 3 · intersección mínima = w + r − n = 1')
f.person(220,230);f.text((275,220),'Escritura',size=29)
f.person(1580,735);f.text((1530,770),'Lectura',size=29,anchor='ra')
xs=[380,640,900,1160,1420]
f.d.rectangle((300,340,985,585),outline='#888888',width=3)
f.d.rectangle((815,380,1505,625),outline='#888888',width=3)
for i,x in enumerate(xs):
    f.arrow((250,250),(x,408),width=2,fill='#111111' if i<3 else '#bbbbbb')
    f.arrow((1560,710),(x,520),width=2,fill='#111111' if i>=2 else '#bbbbbb')
    f.db(x,465,f'Réplica {i+1}',w=120,h=110)
    if i>=3:f.text((x-45,375),'×',size=31,white=True)
    if i<2:f.text((x+30,600),'×',size=31,white=True)
f.text((390,320),'W = {1, 2, 3}',size=28)
f.text((1090,650),'R = {3, 4, 5}',size=28)
f.text((900,730),'La réplica 3 pertenece a ambos conjuntos',size=29,anchor='ma',bold=True)
f.save('Los tres nodos que confirman la escritura forman W y los tres que responden a la lectura forman R. Aunque se elijan los grupos con el menor solapamiento posible, ambos incluyen a la réplica 3: 3 + 3 − 5 = 1. Las flechas grises y las cruces indican solicitudes que no contribuyen al quórum. Esta intersección asegura acceso a una copia de una escritura confirmada bajo los supuestos habituales, pero por sí sola no resuelve escrituras concurrentes ni garantiza linealizabilidad.',8)

# 6-14: concurrent different arrivals.
f=Fig(14,'El orden de llegada cambia entre réplicas',1060,'A y B escriben sin conocer la operación del otro; no existe una relación causal entre ellas.')
a,n1,n2,n3,b=f.lanes(['Cliente A','Nodo 1','Nodo 2','Nodo 3','Cliente B'],step=145)
f.arrow((420,a),(560,n1));f.arrow((420,a),(675,n2));f.arrow((420,a),(930,n3))
f.arrow((420,b),(560,n3));f.arrow((420,b),(740,n2));f.arrow((420,b),(820,n1))
f.text((400,a-58),'X = A',size=29);f.text((395,b+39),'X = B',size=29)
f.text((830,n1+35),'× no responde a B',size=25,white=True)
f.arrow((1110,b),(1270,n1));f.arrow((1160,b),(1300,n2));f.arrow((1210,b),(1330,n3))
f.arrow((1410,n1),(1610,b));f.arrow((1450,n2),(1560,b));f.arrow((1460,n3),(1510,b))
f.text((1430,n1-45),'Devuelve A',size=25,white=True)
f.text((1410,n2-45),'Devuelve B',size=25,white=True)
f.text((1420,n3-45),'Devuelve A',size=25,white=True)
f.text((1200,b+42),'Consulta posterior de X',size=25,anchor='ma')
f.save('A envía X = A y B envía X = B sin haber observado la escritura ajena. El nodo 2 recibe B después de A, pero el nodo 3 recibe A después de B; el nodo 1 no acepta la solicitud de B. Una consulta posterior puede obtener A, B y A de las tres copias. El orden de llegada local no identifica una última escritura común: hace falta detectar la concurrencia y aplicar una política explícita de resolución.',9)

# 6-15: cinco escrituras y contextos; tiempo horizontal + tabla.
f=Fig(15,'El contexto enviado revela qué versiones conocía cada cliente',1390,'Recreación simplificada de la secuencia y sus respuestas: una base de datos, dos clientes, cinco escrituras.')
c1,db,c2=f.lanes(['Cliente 1','Base de datos','Cliente 2'],step=155,y=200)
ops=[(1,c1,450,0),(2,c2,650,0),(3,c1,850,1),(4,c2,1050,2),(5,c1,1250,3)]
for n,yy,x,ctx in ops:
    f.arrow((x,yy),(x+55,db));f.bar(x+55,x+80,db);f.arrow((x+80,db),(x+125,yy))
    f.text((x+75,db+22),str(n),size=27,bold=True,anchor='ma',white=True)
    f.text((x+45,yy-62 if yy==c1 else yy+35),f'Escritura {n}\ncontexto {ctx or "ninguno"}',size=24,anchor='ma')
f.text((80,650),'El servidor numera el orden de recepción; el contexto del cliente expresa conocimiento previo.',size=26,bold=True)
columns=[75,190,380,945]
rows=[
['1','ninguno','[leche]','v1: [leche]'],
['2','ninguno','[huevos]','v1: [leche] + v2: [huevos]'],
['3','1','[leche, harina]','v3: [leche, harina] + v2: [huevos]'],
['4','2','[huevos, leche, jamón]','v3: [leche, harina] + v4: [huevos, leche, jamón]'],
['5','3','[leche, harina, huevos, tocino]','v5: [leche, harina, huevos, tocino]\n+ v4: [huevos, leche, jamón]']]
f.d.rectangle((65,710,1735,1195),outline='#777777',width=2)
for x in [175,355,920]:f.d.line((x,710,x,1195),fill='#bbbbbb',width=2)
for x,t in zip(columns,['Paso','Contexto','Valor que envía el cliente','Valores que quedan en el servidor']):f.text((x,725),t,size=24,bold=True)
f.d.line((65,775,1735,775),fill='#777777',width=2)
for i,row in enumerate(rows):
    y=790+i*76
    for x,t in zip(columns,row):f.text((x,y),t,size=24)
    if i<4:f.d.line((65,y+60,1735,y+60),fill='#dddddd',width=1)
f.text((85,1220),'«+» separa valores hermanos: no significa que el servidor ya los haya fusionado.',size=25)
f.save('Las cinco escrituras llegan en el orden numerado de la línea central, pero cada cliente solo conoce la respuesta de su operación anterior. El contexto 1 del paso 3 permite reemplazar [leche], pero no [huevos], que apareció concurrentemente. El contexto 2 del paso 4 y el contexto 3 del paso 5 dejan también una versión hermana que su cliente aún no había visto. La tabla distingue el nuevo valor enviado de todos los valores que conserva el servidor; al final quedan dos ramas, y una fusión posterior puede reunir sus artículos.',9)

# 6-16: DAG.
f=Fig(16,'Las flechas expresan conocimiento, no horas del reloj',820,'DAG causal de las cinco escrituras: una flecha A → B significa que B conoce o depende de A.')
f.text((110,420),'Vacío',size=29)
boxes=[(350,260,'1 · + leche'),(550,510,'2 · + huevos'),(830,260,'3 · + harina'),(1040,510,'4 · + jamón'),(1320,260,'5 · + tocino')]
f.arrow((205,435),(350,300));f.arrow((205,435),(550,550))
f.arrow((570,300),(830,300));f.arrow((770,550),(1040,550));f.arrow((1050,300),(1320,300))
f.arrow((570,325),(1040,535));f.arrow((770,530),(1320,325))
for x,y,label in boxes:f.box(x,y,220,80,label,size=28)
f.text((700,245),'[leche]',size=25,anchor='ma')
f.text((1170,245),'[leche, harina]',size=25,anchor='ma')
f.text((900,590),'[huevos]',size=25,anchor='ma')
f.arrow((1540,300),(1690,300));f.arrow((1260,550),(1690,550))
f.text((1500,375),'[leche, harina,\nhuevos, tocino]',size=25,anchor='ma')
f.text((1490,605),'[huevos, leche, jamón]',size=25,anchor='ma')
f.text((900,675),'3 y 4 son concurrentes · 4 y 5 también son concurrentes',size=29,bold=True,anchor='ma')
f.save('El grafo conecta una edición con las anteriores que su cliente ya conocía. Añadir harina depende de la leche; añadir jamón depende tanto de los huevos como de la leche; añadir tocino depende de harina y huevos. No existe un camino causal entre harina y jamón, ni entre jamón y tocino: esas parejas son concurrentes. Las dos salidas muestran las versiones hermanas que quedaron al final de la figura anterior.',9)

(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print(f'{len(manifest)} figuras guardadas en {OUT}')
