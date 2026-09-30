"""Gráficos conceptuales propios del capítulo 9. Requiere Pillow, sin datos reales."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
OUT=Path(__file__).resolve().parent
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
COL={'blue':'#2563eb','green':'#15803d','red':'#b91c1c','amber':'#b45309','ink':'#17283b','muted':'#52677d','line':'#becbd8','bg':'#f5f8fc'}
def font(n=26,bold=False): return ImageFont.truetype(BOLD if bold else FONT,n)
def canvas(title,subtitle,h=780):
 im=Image.new('RGB',(1400,h),COL['bg']); d=ImageDraw.Draw(im); d.text((55,35),title,font=font(37,True),fill=COL['ink']); d.text((55,91),subtitle,font=font(23),fill=COL['muted']); return im,d
def text(d,xy,s,n=25,color='ink',bold=False): d.multiline_text(xy,s,font=font(n,bold),fill=COL.get(color,color),spacing=9)
def box(d,rect,label,color='blue',n=25):
 d.rounded_rectangle(rect,radius=17,fill='white',outline=COL[color],width=3)
 x,y,x2,y2=rect; b=d.multiline_textbbox((0,0),label,font=font(n,True),spacing=8); w=b[2]-b[0]; h=b[3]-b[1]; text(d,((x+x2-w)/2,(y+y2-h)/2-4),label,n,color,True)
def arrow(d,a,b,color='blue',width=4):
 d.line([a,b],fill=COL[color],width=width); ang=math.atan2(b[1]-a[1],b[0]-a[0]); size=15
 pts=[b,(b[0]-size*math.cos(ang-.45),b[1]-size*math.sin(ang-.45)),(b[0]-size*math.cos(ang+.45),b[1]-size*math.sin(ang+.45))]; d.polygon(pts,fill=COL[color])
def save(im,name): im.save(OUT/name)
im,d=canvas('Un plazo vencido describe la espera de A','Ejemplo propio · tiempo relativo en milisegundos · B sigue ejecutándose')
for y,l in [(230,'A'),(440,'B')]:
 text(d,(60,y-18),l,30,bold=True); arrow(d,(150,y),(1320,y),'muted',2)
arrow(d,(250,230),(410,440)); text(d,(190,320),'ping',24,'blue')
arrow(d,(490,440),(1030,230),'green'); text(d,(725,375),'ACK retrasado',24,'green')
d.line([(710,175),(710,525)],fill=COL['red'],width=3); text(d,(585,140),'vence a 200 ms',23,'red')
text(d,(237,535),'0 ms\nenvío',23); text(d,(657,535),'200 ms\nsospecha',23,'red'); text(d,(1000,535),'320 ms\nACK recibido',23,'green')
box(d,(135,650,1265,730),'La sospecha falsa dura 120 ms; el retraso no prueba una caída.','amber',25)
save(im,'01-plazo-y-ack.png')
im,d=canvas('Comprobar una ruta alternativa','Ejemplo propio · la conexión A → B pierde el ACK; C puede contactar a B')
box(d,(75,220,350,330),'A\nobservador'); box(d,(1025,220,1300,330),'B\nresponde','green'); box(d,(550,460,850,570),'C\nintermediario')
d.line([(350,275),(1025,275)],fill=COL['red'],width=4); text(d,(480,212),'ACK directo perdido',26,'red'); text(d,(672,251),'×',38,'red',True)
arrow(d,(320,330),(570,460)); text(d,(70,405),'1. Consulta por B',24,'blue')
arrow(d,(840,460),(1050,330),'green'); text(d,(1110,390),'2. Sondeo',24,'green')
arrow(d,(1030,310),(825,510),'green'); text(d,(986,497),'3. ACK',24,'green')
arrow(d,(550,510),(270,330),'green'); text(d,(200,520),'4. C confirma a A',24,'green')
box(d,(135,650,1265,730),'B es alcanzable mediante C; el fallo observado pertenece a una ruta.','amber',25)
save(im,'02-sondeo-indirecto.png')
im,d=canvas('Phi: evidencia, criterio y consecuencia','Ejemplo conceptual propio · las probabilidades describen intervalos del modelo')
labels=[('Medir\nintervalos',70,390,'blue'),('Calcular φ\ncon la ventana',520,890,'blue'),('Aplicar umbral\ny actuar',1020,1340,'amber')]
for label,x,x2,c in labels: box(d,(x,190,x2,315),label,c)
arrow(d,(390,253),(520,253)); arrow(d,(890,253),(1020,253),'amber')
text(d,(100,355),'Últimos latidos\nMedia y dispersión',25); text(d,(545,355),'q = P(intervalo > espera)\nφ = −log10(q)',25); text(d,(1030,355),'φ ≥ umbral\nproduce sospecha',25)
for x,phi,q in [(80,'1','0,1'),(520,'2','0,01'),(960,'3','0,001')]:
 box(d,(x,505,x+360,620),f'φ = {phi}\ncola del modelo = {q}','green',25)
text(d,(95,677),'Una cola de 0,001 no significa «99,9 % de probabilidad de estar muerto».',27,'red',True)
save(im,'03-phi-arquitectura.png')
im,d=canvas('Gossip conserva evidencia reciente','Ejemplo propio · el contador de C avanza y B transmite esa novedad a A')
box(d,(75,220,345,340),'A\nC = 41'); box(d,(570,220,840,340),'B\nC = 42'); box(d,(1050,220,1320,340),'C\ncontador = 42','green')
arrow(d,(1050,280),(840,280),'green'); text(d,(877,215),'novedad',22,'green')
arrow(d,(570,280),(345,280)); text(d,(370,215),'difusión',22,'blue')
box(d,(130,445,650,590),'A recibe 42\nactualiza contador y tiempo','green')
box(d,(750,445,1270,590),'A recibe otra vez 42\nconserva tiempo de avance','amber')
text(d,(145,660),'Una copia vieja no debe rejuvenecer la evidencia de C.',30,'red',True)
save(im,'04-gossip-frescura.png')
im,d=canvas('FUSE propaga una falla mediante el silencio','Ejemplo propio · cuatro miembros forman un grupo indivisible para esta tarea')
steps=[('B cae','red'),('D no oye B\ny deja de responder','amber'),('A y C no oyen D\ny dejan de responder','amber'),('Grupo\nno disponible','red')]
xs=[60,400,740,1080]
for j,((s,c),x) in enumerate(zip(steps,xs)):
 box(d,(x,240,x+270,425),s,c,24)
 if j<3: arrow(d,(x+270,332),(xs[j+1],332),'red')
text(d,(100,500),'Causa inicial: caída física de B.',28,'red',True)
text(d,(100,555),'Consecuencia protocolaria: los demás suspenden sus respuestas.',28)
text(d,(100,610),'El silencio inducido transmite que el grupo ya no puede operar como unidad.',26)
text(d,(100,680),'Los otros procesos no tienen por qué haberse apagado físicamente.',27,'green',True)
save(im,'05-fuse-silencio.png')
