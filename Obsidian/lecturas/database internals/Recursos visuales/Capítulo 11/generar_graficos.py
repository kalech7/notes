"""Diagramas conceptuales propios. Regenerar: uv run --with pillow generar_graficos.py."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
OUT=Path(__file__).parent
W,H=1600,900
BG='#f5f7fc'; INK='#172a41'; BLUE='#2166ac'; ORANGE='#b64a0a'; GREEN='#25734c'; MUTED='#526579'
F='/System/Library/Fonts/Supplemental/Arial.ttf'
def font(n):return ImageFont.truetype(F,n)
def canvas(title,sub):
 im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
 d.text((65,35),title,font=font(43),fill=INK);d.text((65,103),sub,font=font(25),fill=MUTED)
 d.text((65,845),'Database Internals · capítulo 11 · esquema propio, sin mediciones',font=font(21),fill=MUTED)
 return im,d
def txt(d,x,y,s,size=28,color=INK):
 d.multiline_text((x,y),s,font=font(size),fill=color,spacing=12)
def box(d,xy,s,col=BLUE,size=28):
 d.rounded_rectangle(xy,radius=18,fill='white',outline=col,width=4)
 b=d.multiline_textbbox((0,0),s,font=font(size),spacing=10)
 d.multiline_text(((xy[0]+xy[2]-b[2])/2,(xy[1]+xy[3]-b[3])/2),s,font=font(size),fill=INK,spacing=10,align='center')
def arrow(d,a,b,col=BLUE):
 d.line((a,b),fill=col,width=5); ang=math.atan2(b[1]-a[1],b[0]-a[0]);p=[b,(b[0]-20*math.cos(ang-.45),b[1]-20*math.sin(ang-.45)),(b[0]-20*math.cos(ang+.45),b[1]-20*math.sin(ang+.45))];d.polygon(p,fill=col)
def save(im,n):im.save(OUT/n)
im,d=canvas('CAP y PACELC: dos situaciones','La partición es una condición de la red; la política determina qué responde el sistema.')
box(d,(70,210,450,385),'¿La red impide\ncomunicar réplicas?')
arrow(d,(450,265),(640,265));txt(d,485,215,'Sí',25)
box(d,(650,185,1490,390),'Consistencia: bloquear o rechazar sin autoridad\nDisponibilidad: responder con vista local',ORANGE)
arrow(d,(450,355),(640,600));txt(d,455,490,'No',25)
box(d,(650,485,1490,715),'Menor latencia: confirmar sin esperar todas\nMayor coordinación: esperar visibilidad acordada',GREEN)
text='Ejemplo: A acepta x=1 y B aislado aún tiene x=0.\nUna lectura iniciada tras confirmar 1 debe ver 1, si no hay otra escritura.';txt(d,75,740,text,24)
save(im,'01 CAP y PACELC.png')
im,d=canvas('Una operación ocupa un intervalo','Invocación y respuesta delimitan cuándo puede ubicarse su efecto lógico.')
for row,label,ranges in [(230,'Separadas',[(300,600),(780,1100)]),(440,'Solapadas',[(300,860),(640,1150)]),(650,'Contenidas',[(300,1250),(620,850)])]:
 txt(d,70,row-25,label,29)
 for j,(a,b) in enumerate(ranges):
  y=row+j*58;d.line((280,y,1480,y),fill='#c5cedc',width=2);d.line((a,y,b,y),fill=[BLUE,ORANGE][j],width=14)
  d.ellipse((a-9,y-9,a+9,y+9),fill=INK);d.ellipse((b-9,y-9,b+9,y+9),fill=INK)
 txt(d,1320,row-20,'P1\nP2',23)
txt(d,480,780,'Sólo las separadas imponen precedencia de tiempo real.',28)
save(im,'02 Intervalos y concurrencia.png')
im,d=canvas('Linealizabilidad: un punto dentro del intervalo','Ejemplo propio: x empieza en 0 y una escritura lo cambia a 1.')
d.line((220,330,1400,330),fill='#c5cedc',width=3);d.line((460,330,1040,330),fill=BLUE,width=13)
txt(d,440,260,'Invocación',26);txt(d,1010,260,'Respuesta',26)
d.line((760,220,760,640),fill=ORANGE,width=5);txt(d,620,175,'Punto de efecto',29,ORANGE)
box(d,(120,455,690,620),'Lectura antes: x = 0',BLUE)
box(d,(830,455,1490,620),'Lectura después: x = 1',GREEN)
txt(d,100,705,'Una lectura que se solapa puede ubicarse a cualquiera de los lados.\nUna lectura iniciada tras la respuesta debe respetar la nueva versión.',29)
save(im,'03 Punto de linealización.png')
im,d=canvas('Secuencial y causal: qué orden comparten','Las letras representan escrituras. Estos ejemplos ilustran garantías, no tiempos medidos.')
box(d,(70,185,765,450),'Secuencial: un orden total común\nLector 1: A → B → C\nLector 2: A → B → C',BLUE,30)
box(d,(835,185,1530,450),'Causal: A causa B; C independiente\nLector 1: A → B → C\nLector 2: C → A → B',GREEN,30)
box(d,(70,520,765,745),'Preserva orden de cada cliente\nPuede alterar precedencia real\nentre clientes distintos',BLUE,28)
box(d,(835,520,1530,745),'Ambos lectores ponen A antes de B\nC puede ocupar otro lugar\nNo equivale a un único orden global',GREEN,28)
save(im,'04 Orden secuencial y causal.png')
im,d=canvas('Historia común, ramas concurrentes','Recreación conceptual de la figura 11-9: 1 → 5 y después dos ramas.')
box(d,(65,365,275,505),'x = 1');box(d,(425,365,635,505),'x = 5');arrow(d,(275,435),(425,435))
box(d,(835,230,1055,365),'x = 7',GREEN);box(d,(1280,230,1500,365),'x = 8',GREEN)
box(d,(835,535,1055,670),'x = 3',ORANGE)
arrow(d,(635,420),(835,300),GREEN);arrow(d,(635,465),(835,600),ORANGE);arrow(d,(1055,300),(1280,300),GREEN)
txt(d,700,720,'7 y 3 comparten la versión 5, pero ninguna causó la otra.\nEl vector detecta concurrencia; la aplicación decide cómo fusionar.',28)
save(im,'05 Ramas causales.png')
im,d=canvas('Quórums: intersección y una escritura incompleta','N = 3 y R = W = 2. El solapamiento no elimina todos los problemas.')
for x,s,c in [(80,'A: versión 1',GREEN),(580,'B: versión 0',BLUE),(1080,'C: versión 0',BLUE)]:box(d,(x,230,x+430,400),s,c)
box(d,(80,475,760,650),'Lectura 1: {A, B}\nElige versión 1',GREEN)
box(d,(840,475,1520,650),'Lectura 2: {B, C}\nElige versión 0',ORANGE)
txt(d,100,730,'La escritura sólo llegó a A y no completó W = 2.\nAmbas lecturas cumplen R = 2, pero la segunda retrocede sin reparación.',29)
save(im,'06 Quórum y escritura incompleta.png')
im,d=canvas('Un testigo necesita el dato durante la falla','Ejemplo del libro: dos réplicas completas y un testigo, con mayoría de dos.')
for y,label,vals in [(230,'Normal',['1c: dato','2c: dato','3w: registro']),(420,'2c falla',['1c: dato nuevo','2c: no responde','3w: dato temporal']),(610,'Reparación',['1c: dato nuevo','2c: dato nuevo','3w: registro'])]:
 txt(d,65,y+40,label,25)
 for x,v,col in zip([330,750,1170],vals,[BLUE,BLUE,ORANGE]):box(d,(x,y,x+340,y+145),v,col,25)
txt(d,330,785,'Eliminar el dato temporal sólo tras conservar copias válidas suficientes.',25)
save(im,'07 Réplicas testigo.png')
im,d=canvas('G-counter: fusionar máximos, leer la suma','Cada nodo aumenta únicamente su casilla. Se pueden repetir estados sin duplicar incrementos.')
box(d,(80,240,690,420),'Nodo A: [1, 0, 0]',BLUE,36);box(d,(910,240,1520,420),'Nodo C: [0, 0, 1]',ORANGE,36)
arrow(d,(690,365),(790,560));arrow(d,(910,365),(810,560),ORANGE)
box(d,(410,565,1190,735),'máximo por casilla = [1, 0, 1]\nvalor = 1 + 0 + 1 = 2',GREEN,33)
save(im,'08 G-counter.png')
print('8 diagramas regenerados')
