"""Recreaciones didácticas DDIA 2e, capítulo 7, a partir de las figuras del PDF.
Ejecutar: uv run --with pillow generar_figuras.py. No usa conexión de red.
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math,json
OUT=Path(__file__).parent
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
if not Path(FONT).exists():
 FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
 BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
manifest=[]
class Canvas:
 def __init__(self,w,h,title,pdf,figure):
  self.w=w;self.h=h;self.im=Image.new('RGB',(w,h),'white');self.d=ImageDraw.Draw(self.im);self.pdf=pdf;self.figure=figure
  self.text((45,28),title,36,True)
  self.d.line((45,82,w-45,82),fill='black',width=2)
 def text(self,pos,txt,size=28,bold=False,anchor=None,fill='black'):
  f=ImageFont.truetype(BOLD if bold else FONT,size)
  self.d.multiline_text(pos,txt,font=f,fill=fill,anchor=anchor,spacing=8,align='center' if anchor=='mm' else 'left')
 def box(self,rect,txt='',size=28,bold=False,width=2):
  self.d.rectangle(rect,fill='white',outline='black',width=width)
  if txt:self.text(((rect[0]+rect[2])/2,(rect[1]+rect[3])/2),txt,size,bold,'mm')
 def line(self,pts,width=2,dash=False):
  if not dash:self.d.line(pts,fill='black',width=width);return
  for a,b in zip(pts,pts[1:]):
   dx=b[0]-a[0];dy=b[1]-a[1];n=math.hypot(dx,dy)
   for t in range(0,int(n),14):
    v=min(t+6,n);self.d.line((a[0]+dx*t/n,a[1]+dy*t/n,a[0]+dx*v/n,a[1]+dy*v/n),fill='black',width=width)
 def arrow(self,pts,width=3,dash=False):
  self.line(pts,width,dash);a,b=pts[-2:];theta=math.atan2(b[1]-a[1],b[0]-a[0]);sz=13
  self.d.polygon([b,(b[0]-sz*math.cos(theta-.45),b[1]-sz*math.sin(theta-.45)),(b[0]-sz*math.cos(theta+.45),b[1]-sz*math.sin(theta+.45))],fill='black')
 def curve(self,a,b,c,d,width=3,dash=False):
  pts=[]
  for i in range(61):
   t=i/60;s=1-t;pts.append((s**3*a[0]+3*s*s*t*b[0]+3*s*t*t*c[0]+t**3*d[0],s**3*a[1]+3*s*s*t*b[1]+3*s*t*t*c[1]+t**3*d[1]))
  self.arrow(pts,width,dash)
 def hatch(self,rect):
  x0,y0,x1,y1=rect;self.d.rectangle(rect,fill='white',outline='black',width=2)
  for x in range(int(x0)-int(y1-y0),int(x1),12):
   a=max(x,x0);b=min(x+y1-y0,x1)
   self.d.line((a,y1-(a-x),b,y1-(b-x)),fill='black',width=2)
 def cylinder(self,x,y,w=85,h=90,txt=''):
  self.d.line((x,y+15,x,y+h-15),fill='black',width=2)
  self.d.line((x+w,y+15,x+w,y+h-15),fill='black',width=2)
  self.d.arc((x,y+h-30,x+w,y+h),0,180,fill='black',width=2)
  self.d.ellipse((x,y,x+w,y+30),fill='white',outline='black',width=2)
  if txt:self.text((x+w/2,y+h*.58),txt,24,anchor='mm')
 def save(self,name,note,explanation):
  self.text((45,self.h-52),f'Adaptación didáctica · figura {self.figure} · DDIA 2.ª ed. · PDF {self.pdf} / impresa {250+self.pdf}',23)
  self.im.save(OUT/name)
  manifest.append(dict(file=name,figure=self.figure,pdf=self.pdf,printed=250+self.pdf,note_number=note,explanation=explanation))

# 7-1: cuatro nodos, tres réplicas de cada shard, líder único por shard.
c=Canvas(1600,1030,'Sharding + replicación: cada shard tiene su propio líder',2,'7-1')
nodes={1:(70,150,[(1,'Líder'),(2,'Seguidor'),(3,'Seguidor')]),2:(850,150,[(2,'Seguidor'),(3,'Líder'),(4,'Seguidor')]),3:(70,610,[(1,'Seguidor'),(2,'Líder'),(4,'Seguidor')]),4:(850,610,[(1,'Seguidor'),(3,'Seguidor'),(4,'Líder')])}
points={}
for n,(x,y,sh) in nodes.items():
 for i,(s,r) in enumerate(sh):points[n,s]=(x+95+i*210,y+100)
for n,(x,y,sh) in nodes.items():
 c.text((x,y-42),f'Nodo {n}',30,True);c.box((x,y,x+650,y+205))
 for i,(s,r) in enumerate(sh):c.box((x+15+i*210,y+35,x+205+i*210,y+165),f'Shard {s}\n{r}',27,r=='Líder',3 if r=='Líder' else 2)
for s in range(1,5):
 leader=[n for n,(_,_,sh) in nodes.items() if (s,'Líder') in sh][0]
 a=points[leader,s]
 for n,(_,_,sh) in nodes.items():
  if n!=leader and any(k==s for k,r in sh):
   end=points[n,s]
   start=(a[0],a[1]+65 if a[1]<400 else a[1]-65)
   finish=(end[0],end[1]+65 if end[1]<400 else end[1]-65)
   c.curve(start,(start[0],430),(finish[0],480),finish,2,False)
for n,(x,y,sh) in nodes.items():
 c.d.rectangle((x,y-48,x+165,y-8),fill='white')
 c.text((x,y-42),f'Nodo {n}',30,True)
c.box((1130,855,1430,925),'Cliente: escribe shard 4',24)
c.arrow([(1280,855),(1280,818),(1365,818),(1365,775)])
c.arrow([(75,875),(255,875)],2);c.text((275,859),'Flujo de replicación: líder → seguidores del mismo shard',26)
c.save('07-01-sharding-y-replicacion.png','01','Cada caja exterior es una máquina; las cajas interiores son las copias de shards que guarda. Un shard tiene un solo líder y dos seguidores, pero una máquina puede ser líder de un shard y seguidora de otros. Las flechas representan la replicación desde el líder hacia las otras copias del mismo shard. La escritura del shard 4 llega a su líder, en el nodo 4.')

# 7-2: lomos de una enciclopedia, con las fronteras originales.
c=Canvas(1600,1060,'Sharding por rangos: cada volumen cubre una parte del orden',6,'7-2')
ranges=['A-ak — Bayes','Bayeu — Ceanothus','Ceara — Deluc','Delusion — Frenssen','Freon — Holderlin','Holderness — Krasnoje','Krasnokamsk — Menadra','Menage — Ottawa','Otter — Rethimnon','Reti — Solovets','Solovyov — Truck','Trudeau — Zywiec']
for i,t in enumerate(ranges):
 x=90+i*118;y=220
 c.d.polygon([(x,y),(x+43,y-90),(x+140,y-90),(x+97,y)],fill='white',outline='black',width=2)
 c.box((x,y,x+97,805));c.text((x+48,858),str(i+1),30,True,'mm')
 layer=Image.new('RGB',(530,58),'white');dd=ImageDraw.Draw(layer);dd.text((8,8),t,font=ImageFont.truetype(FONT,27),fill='black')
 layer=layer.rotate(90,expand=True);c.im.paste(layer,(x+20,235))
c.line([(60,885),(1520,885)],3)
c.text((70,925),'Clave de partición = título de la entrada. Las fronteras se adaptan a los datos.',28)
c.save('07-02-rangos-enciclopedia.png','02','Los doce volúmenes reproducen los límites alfabéticos de la figura del libro. Cada entrada pertenece al volumen cuyo rango contiene su título: no hace falta mirar todos los volúmenes. Los rangos no abarcan la misma cantidad de letras; la distribución de títulos determina dónde conviene colocar sus fronteras.')

# 7-3: todos los hashes 0..23 y la operación módulo exacta.
c=Canvas(1600,1090,'Hash % N: al cambiar N, cambia el destino de muchas claves',9,'7-3')
for row,n,y in [(0,3,170),(1,4,605)]:
 c.text((55,y-50),f'{"Antes" if row==0 else "Después"}: {n} nodos',30,True)
 w=345 if n==4 else 455
 for j in range(n):
  x=55+j*(w+35);c.box((x,y,x+w,y+275));c.text((x+20,y+18),f'Nodo {j}',29,True);c.text((x+20,y+65),f'hash % {n} = {j}',26)
  vals=[v for v in range(24) if v%n==j]
  for k,v in enumerate(vals):c.text((x+55+(k%3)*(w-50)/3,y+140+(k//3)*55),str(v),31,anchor='mm')
c.arrow([(800,475),(800,550)]);c.text((850,488),'Se añade un nodo; N pasa de 3 a 4',29)
c.text((55,936),'Ejemplo: hash 3 → nodo 0 antes, nodo 3 después.',30)
c.text((55,988),'18 de los 24 hashes cambian de nodo (75 %).',30,True)
c.save('07-03-hash-modulo-rebalanceo.png','05','Las cajas agrupan los mismos hashes, del 0 al 23, antes y después de añadir el cuarto nodo. Con tres nodos se calcula hash % 3; con cuatro, hash % 4. La operación cambia el destino de 18 de los 24 valores de este ejemplo, aunque solo se haya añadido una máquina. Los números son hashes, no necesariamente las claves originales.')

# 7-4: se mueven cuatro shards de un total fijo de veinte.
c=Canvas(1750,1090,'Número fijo de shards: mover shards completos al nuevo nodo',10,'7-4')
before=[[0,4,8,12,16],[1,5,9,13,17],[2,6,10,14,18],[3,7,11,15,19]]
after=[[0,8,12,16],[1,5,13,17],[2,6,10,18],[3,7,11,15],[4,9,14,19]]
c.text((45,125),'Antes: 4 nodos, 5 shards por nodo',30,True)
p1={};p2={}
for n,sh in enumerate(before):
 x=55+n*425;c.text((x,185),f'Nodo {n}',28,True)
 for k,s in enumerate(sh):p1[s]=(x+k*75+37,310)
for n,sh in enumerate(after):
 x=55+n*338
 for k,s in enumerate(sh):p2[s]=(x+k*75+37,640)
for s in range(20):
 a=p1[s];b=p2[s]
 if s in [4,9,14,19]:c.curve(a,(a[0],470),(b[0],470),b,4)
 else:c.line([a,b],2,True)
for n,sh in enumerate(before):
 x=55+n*425
 for k,s in enumerate(sh):c.box((x+k*75,235,x+(k+1)*75,310),f's{s}',26)
for n,sh in enumerate(after):
 x=55+n*338
 for k,s in enumerate(sh):c.box((x+k*75,640,x+(k+1)*75,720),f's{s}',26)
 c.text((x,745),f'Nodo {n}'+(' (nuevo)' if n==4 else ''),28,True)
c.text((45,823),'Después: 5 nodos, 4 shards por nodo. Siguen existiendo los mismos 20 shards.',30,True)
c.line([(65,915),(230,915)],2,True);c.text((250,897),'El shard sigue en el mismo nodo.',27)
c.arrow([(65,975),(230,975)],4);c.text((250,957),'El shard migra al nodo 4: s4, s9, s14 y s19.',27)
c.save('07-04-shards-fijos-rebalanceo.png','05','Los veinte shards mantienen su identidad y las claves asignadas a cada uno. Para repartirlos entre cinco máquinas, los shards s4, s9, s14 y s19 migran al nuevo nodo 4; los otros dieciséis se quedan en sus nodos. Las flechas sólidas representan las cuatro transferencias y las líneas discontinuas muestran las asignaciones que no cambian.')

# 7-5: hashes exactos del libro; intervalos explícitos para evitar fronteras ambiguas.
c=Canvas(1750,1130,'Rangos de hash: claves cercanas pueden terminar en shards distintos',11,'7-5')
values=[7372,18805,50537,31579,62253,24510];dest=[0,1,3,1,3,1]
c.text((55,122),'Clave original',28,True);c.text((525,122),'Hash de 16 bits',28,True)
for i,(v,s) in enumerate(zip(values,dest)):
 y=205+i*82;c.text((55,y-18),f'2024-12-19 17:08:{10+i}',30);c.arrow([(425,y),(500,y)])
 c.text((525,y-18),f'{v:,}',30)
 tx=720+s*230+45+(i%3)*45
 c.arrow([(645,y),(tx,y),(tx,840)],2)
for s in range(4):
 x=700+s*235;c.box((x,840,x+235,930),f'Shard {s}',30,True)
 lo=s*16384;hi=(s+1)*16384-1;c.text((x+117,970),f'{lo:,}–{hi:,}',24,anchor='mm')
c.text((55,1040),'La continuidad se conserva en el espacio de hashes; se pierde en las claves originales.',28)
c.save('07-05-rangos-de-hash.png','03','Las seis marcas de tiempo son consecutivas, pero los hashes originales del libro se dispersan por el espacio de 16 bits: de 0 a 65.535. Cada flecha termina en el shard dueño del intervalo que contiene su hash. El shard 2 no recibe ninguna de estas seis claves: una distribución útil a gran escala no exige que cada muestra pequeña use todos los shards.')

# 7-6: fronteras y propiedad originales. Intervalos [a,b), excepto extremo final.
c=Canvas(1800,1320,'Varios rangos por nodo: se añaden límites y se transfieren subrangos',12,'7-6')
old=[(0,88,1),(88,128,0),(128,309,2),(309,398,0),(398,511,2),(511,672,1),(672,702,2),(702,930,1),(930,1024,0)]
new=[(0,60,1),(60,88,3),(88,128,0),(128,276,2),(276,309,3),(309,398,0),(398,511,2),(511,551,1),(551,672,3),(672,702,2),(702,930,1),(930,1024,0)]
def axis(intervals,y):
 x0=75;width=1650
 for a,b,n in intervals:
  x=x0+a/1024*width;z=x0+b/1024*width
  c.box((x,y,z,y+72),f'n{n}',23,n==3)
  if n==3:c.hatch((x,y+60,z,y+72))
  c.text((x,y-27),str(a),21,anchor='mm')
 c.text((x0+width,y-27),'1024',21,anchor='mm')
def nodeblocks(intervals,y,nodes):
 w=(1700-(nodes-1)*35)/nodes
 for n in range(nodes):
  x=50+n*(w+35);c.box((x,y,x+w,y+205));c.text((x+20,y+15),f'Nodo {n}',29,True)
  spans=[(a,b) for a,b,owner in intervals if owner==n]
  for i,(a,b) in enumerate(spans):c.box((x+20,y+63+i*43,x+w-20,y+103+i*43),f'{a}–{b}',25)
c.text((55,115),'Antes: tres nodos; tres rangos por nodo',30,True)
nodeblocks(old,165,3);axis(old,445)
c.text((55,583),'Después: se añade el nodo 3 con los límites 60, 276 y 551',30,True)
axis(new,685);nodeblocks(new,820,4)
c.text((55,1105),'Nodo 1 → nodo 3: 60–88 y 551–672. Nodo 2 → nodo 3: 276–309.',28)
c.text((55,1160),'Los demás intervalos conservan su nodo. Las bandas rayadas identifican los rangos nuevos.',27)
c.text((55,1215),'Las cifras son fronteras de intervalos; cada frontera pertenece a un único rango.',26)
c.save('07-06-rangos-virtuales-nodo-nuevo.png','05','Las barras reproducen los límites de hash y los propietarios de la figura original; n0 significa nodo 0 y así sucesivamente. El nodo 3 se incorpora tomando dos subrangos del nodo 1 y uno del nodo 2. Los rangos tienen tamaños distintos y cada máquina almacena varios rangos separados. Las cifras indican fronteras, no dos copias de la misma clave en rangos vecinos.')

# 7-7: tres alternativas; rayado = conocimiento del mapa.
c=Canvas(1800,1110,'Tres formas de encaminar una petición al nodo que posee el shard',16,'7-7')
for mode in range(3):
 x=45+mode*585;c.text((x,120),f'{mode+1}. '+['Un nodo reenvía','Capa de routing','Cliente conoce el mapa'][mode],30,True)
 c.box((x+180,205,x+385,275),'Cliente',29)
 if mode==2:c.hatch((x+180,275,x+385,292))
 for n in range(3):
  nx=x+n*180+20;c.box((nx,680,nx+135,765),f'Nodo {n}',27)
  if mode==0:c.hatch((nx,680,nx+135,697))
  c.line([(nx+68,765),(nx+68,815)])
  c.cylinder(nx+22,815,90,95,'foo' if n==2 else '')
 if mode==0:
  c.text((x+270,340),'GET foo\nNodo elegido\nal azar',25)
  c.arrow([(x+225,275),(x+88,680)])
  c.curve((x+88,680),(x+88,570),(x+450,570),(x+448,680))
  c.text((x+145,555),'foo está en nodo 2',24)
 elif mode==1:
  c.arrow([(x+282,275),(x+282,405)]);c.text((x+315,325),'GET foo',26)
  c.box((x+140,405,x+430,495),'Capa de routing',28);c.hatch((x+140,495,x+430,512))
  c.arrow([(x+285,512),(x+448,680)]);c.text((x+40,570),'foo está en nodo 2',24)
 else:
  c.arrow([(x+282,292),(x+448,680)]);c.text((x+65,405),'GET foo\nConexión directa\nal nodo 2',26)
c.hatch((55,960,205,985));c.text((235,955),'Conocimiento del mapa shard → nodo',29)
c.save('07-07-rutas-de-peticiones.png','06','Las tres alternativas buscan la misma clave foo, almacenada en el nodo 2. En la primera, un nodo elegido inicialmente reenvía la petición; en la segunda, una capa de routing elige el nodo; en la tercera, el cliente se conecta directamente. Las bandas rayadas muestran dónde debe estar el conocimiento de la asignación de shards a máquinas. Los cilindros representan el almacenamiento de datos.')

# 7-8: tabla autoritativa completa, con los rangos e IP originales.
c=Canvas(1800,1180,'ZooKeeper: un mapa autoritativo que mantiene informado al router',17,'7-8')
c.box((155,160,435,235),'Cliente',30);c.text((80,260),'GET «Danube»',27)
c.arrow([(295,235),(295,340)]);c.box((95,340,480,430),'Capa de routing',29);c.hatch((95,430,480,450))
c.cylinder(530,335,100,140,'');c.text((570,300),'ZooKeeper',28,True,'mm')
c.arrow([(530,395),(485,395)],3,True);c.text((65,475),'Mapa actualizado',24)
for n in range(3):
 x=60+n*220;c.box((x,700,x+170,790),f'Nodo {n}',27);c.cylinder(x+38,850,95,110)
 c.line([(x+85,790),(x+85,850)])
 c.arrow([(x+85,700),(x+85,570),(575,570),(575,475)],2,True)
c.arrow([(295,450),(295,585),(585,700)],4)
c.text((55,1008),'Los nodos se registran; el router consulta\ny recibe notificaciones de cambios.',27)
xcols=[730,1190,1350,1500];headers=['Rango de claves','Shard','Nodo','Dirección IP']
for x,h in zip(xcols,headers):c.text((x,148),h,26,True)
c.line([(725,195),(1750,195)])
for i,r in enumerate(ranges):
 y=223+i*65;vals=[r,f's{i}',f'n{i%3}',f'10.20.30.{100+i%3}']
 for x,v in zip(xcols,vals):c.text((x,y),v,25)
 if i==2:c.d.rectangle((725,y-9,1760,y+44),outline='black',width=3)
c.text((740,1050),'«Danube» está en Ceara–Deluc → s2 → n2.',27,True)
c.save('07-08-zookeeper-mapa-shards.png','06','ZooKeeper conserva la asignación autoritativa de los doce rangos a shards, nodos y direcciones IP. Danube está dentro de Ceara–Deluc, por lo que el router envía la petición al nodo 2. Las flechas discontinuas representan registro y actualización del mapa; la flecha sólida representa la petición de datos. ZooKeeper aporta metadatos de coordinación: la lectura del dato se ejecuta en el nodo propietario.')

# 7-9 y 7-10: mismas seis filas, términos ingleses para conservar el orden original.
records=[[(191,'red','Honda','Palo Alto'),(214,'black','Dodge','San Jose'),(306,'red','Ford','Sunnyvale')],[(515,'silver','Ford','Milpitas'),(768,'red','Volvo','Cupertino'),(893,'silver','Audi','Santa Clara')]]
local=[[('color:black','[214]'),('color:red','[191, 306]'),('color:yellow','[]'),('marca:Dodge','[214]'),('marca:Ford','[306]'),('marca:Honda','[191]')],[('color:black','[]'),('color:red','[768]'),('color:silver','[515, 893]'),('marca:Audi','[893]'),('marca:Ford','[515]'),('marca:Volvo','[768]')]]
globalidx=[[('color:black','[214]'),('color:red','[191, 306, 768]'),('marca:Audi','[893]'),('marca:Dodge','[214]'),('marca:Ford','[306, 515]')],[('color:silver','[515, 893]'),('color:yellow','[]'),('marca:Honda','[191]'),('marca:Volvo','[768]')]]
for glob in (False,True):
 fig='7-10' if glob else '7-9';pdf=20 if glob else 19
 c=Canvas(1900,1350,'Índices secundarios '+('globales: cada término tiene un shard dueño' if glob else 'locales: cada shard indexa sus propios registros'),pdf,fig)
 idx=globalidx if glob else local
 for n in range(2):
  x=50+n*930;c.text((x,123),f'Shard {n} · IDs '+('0–499' if n==0 else '500–999'),32,True)
  c.box((x,185,x+865,990));c.text((x+20,205),'DATOS / ÍNDICE POR CLAVE PRIMARIA',27,True)
  for xx,h in zip([x+25,x+130,x+280,x+495],['ID','Color','Marca','Ubicación']):c.text((xx,275),h,26,True)
  for i,r in enumerate(records[n]):
   y=338+i*58
   for xx,v in zip([x+25,x+130,x+280,x+495],r):c.text((xx,y),str(v),27)
  c.line([(x,532),(x+865,532)]);c.text((x+20,560),'ÍNDICE SECUNDARIO '+('GLOBAL' if glob else 'LOCAL'),27,True)
  if glob:
   text=('colores a–r · marcas a–f' if n==0 else 'colores s–z · marcas h–z');c.text((x+20,608),text,26)
  else:c.text((x+20,608),'Listas de IDs de este shard solamente',26)
  for i,(term,ids) in enumerate(idx[n]):
   y=674+i*48
   if term=='color:red':c.d.rectangle((x+15,y-6,x+835,y+36),outline='black',width=3)
   c.text((x+30,y),term,28,term=='color:red');c.text((x+350,y),'→ '+ids,28,term=='color:red')
 c.box((580,1085,1320,1165),'Cliente: «Busco un automóvil rojo»',29)
 if glob:
  # Mantenimiento entre shards: el registro rojo 768 y el Audi 893 alimentan índices del shard 0.
  c.arrow([(1790,410),(1870,410),(1870,510),(935,510),(935,730),(895,730)],2,True)
  c.arrow([(1790,470),(1845,470),(1845,526),(945,526),(945,778),(895,778)],2,True)
  c.text((1120,1183),'Discontinuas: actualizar el índice global',25)
  c.arrow([(825,1085),(825,1025),(730,1025),(730,740)],4)
  c.text((60,1014),'Una consulta de índice → [191, 306, 768]',28,True)
  c.text((1350,1020),'Para obtener los registros:\nleer sus shards de datos.',26)
 else:
  c.arrow([(690,1085),(690,1040),(730,1040),(730,738)],4)
  c.arrow([(1210,1085),(1210,1040),(1600,1040),(1600,738)],4)
  c.text((60,1183),'Consultar todos los shards y combinar: [191, 306] + [768]',27,True)
 c.text((55,1220),'Términos del libro: red = rojo · black = negro · silver = plateado · yellow = amarillo.',26)
 name='07-10-indice-global-autos.png' if glob else '07-09-indices-locales-autos.png'
 exp=('Los registros siguen distribuidos por ID, pero el índice global se reparte por el término indexado. La lista color:red del shard 0 reúne 191, 306 y 768, aunque 768 vive en el shard 1 de datos. Una consulta al índice obtiene todos esos IDs; recuperar los automóviles completos todavía requiere consultar sus shards de datos. Las flechas discontinuas muestran que los registros 768 y 893 del shard 1 alimentan entradas del índice global del shard 0. Los colores mantienen sus nombres originales en inglés para conservar los rangos a–r y s–z de la figura del libro.' if glob else 'Los datos se reparten por ID y cada índice local contiene únicamente los IDs del shard donde reside. color:red devuelve 191 y 306 en el shard 0, y 768 en el shard 1. La consulta por color necesita buscar en ambos y combinar los resultados porque no conoce los IDs de antemano. Las seis filas y las listas de IDs conservan el ejemplo del libro; los colores mantienen sus términos originales en inglés.')
 c.save(name,'04',exp)
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(f'{len(manifest)} figuras generadas en {OUT}')
