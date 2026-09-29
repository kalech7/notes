"""Seis figuras didácticas propias. Requiere Pillow; salida PNG y SVG."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import html, math
OUT=Path(__file__).resolve().parent
FONT=next((p for p in [Path('/System/Library/Fonts/Supplemental/Arial.ttf'),Path('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')] if p.exists()),None)
BOLD=next((p for p in [Path('/System/Library/Fonts/Supplemental/Arial Bold.ttf'),Path('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')] if p.exists()),FONT)
INK='#193249';BLUE='#2563A5';TEAL='#147D73';RED='#A63E45';MUTED='#506479';BG='#F4F7FB'
class Figure:
 def __init__(self,title,subtitle):
  self.im=Image.new('RGB',(1600,1000),BG);self.d=ImageDraw.Draw(self.im)
  self.svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="1000" viewBox="0 0 1600 1000">',f'<rect width="1600" height="1000" fill="{BG}"/>']
  self.text(65,45,title,40,True);self.text(65,108,subtitle,24,color=MUTED)
 def text(self,x,y,t,size=25,bold=False,color=INK):
  font=ImageFont.truetype(str(BOLD if bold else FONT),size) if FONT else ImageFont.load_default()
  self.d.text((x,y),t,font=font,fill=color,anchor='lt')
  self.svg.append(f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}" dominant-baseline="text-before-edge">{html.escape(str(t))}</text>')
 def rect(self,x,y,w,h,fill='white',stroke='#CBD6E2',radius=18):
  self.d.rounded_rectangle((x,y,x+w,y+h),radius,fill=fill,outline=stroke,width=2)
  self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
 def line(self,x1,y1,x2,y2,color=MUTED,width=4):
  self.d.line((x1,y1,x2,y2),fill=color,width=width)
  self.svg.append(f'<path d="M{x1},{y1} L{x2},{y2}" stroke="{color}" stroke-width="{width}" fill="none"/>')
 def arrow(self,x1,y1,x2,y2,color=BLUE):
  self.line(x1,y1,x2,y2,color);a=math.atan2(y2-y1,x2-x1)
  for s in [-1,1]: self.line(x2,y2,x2-15*math.cos(a+s*.5),y2-15*math.sin(a+s*.5),color)
 def box(self,x,y,w,h,title,lines,fill='white',accent=BLUE):
  self.rect(x,y,w,h,fill);self.text(x+22,y+22,title,27,True,accent)
  for n,t in enumerate(lines): self.text(x+22,y+67+35*n,t,23)
 def footer(self,t):
  self.line(65,935,1535,935,'#CBD6E2',2);self.text(65,955,t,20,color=MUTED)
 def save(self,name):
  self.im.save(OUT/(name+'.png'));(OUT/(name+'.svg')).write_text('\n'.join(self.svg+['</svg>']))

f=Figure('RAG: conservar la evidencia en cada etapa','Preparación del corpus arriba; recorrido de cada pregunta abajo.')
xs=[65,455,845,1235];ws=[320,320,320,300]
for i,(title,lines) in enumerate([
 ('1. Documentos',['Archivos originales','y versiones']),('2. Texto y fragmentos',['Extracción legible','Cortes en tokens']),('3. Embeddings',['Representación de','la entrada efectiva']),('4. Colección',['Vectores + IDs','Texto y fuentes'])]):
 f.box(xs[i],190,ws[i],160,title,lines)
 if i<3:f.arrow(xs[i]+ws[i]+8,270,xs[i+1]-12,270)
f.line(1385,350,1385,410,BLUE)
f.line(1385,410,615,410,BLUE)
f.arrow(615,410,615,475,BLUE)
for i,(title,lines) in enumerate([
 ('Pregunta',['Qué necesita saber','la persona']),('Recuperación',['Ranking de candidatos','¿Llegó la evidencia?']),('Contexto',['Texto seleccionado','para el prompt']),('Respuesta',['Usar y citar evidencia','o abstenerse'])]):
 f.box(xs[i],490,ws[i],175,title,lines,fill='#EAF2FC')
 if i<3:f.arrow(xs[i]+ws[i]+8,575,xs[i+1]-12,575)
f.text(880,430,'El buscador consulta la colección',23,True,BLUE)
for x,title,lines in [(65,'Antes de consultar',['¿Qué se leyó y qué se rechazó?','¿Qué tokens entraron al encoder?']),(575,'Al recuperar',['Hit Rate: presencia de relevantes.','MRR: posición del primer relevante.']),(1085,'Al responder',['¿Se conserva lo que dice la fuente?','¿La abstención es adecuada?'])]:
 f.box(x,735,450,155,title,lines,accent=TEAL)
f.footer('Esquema conceptual propio · Los vectores sirven para buscar; el generador recibe texto.')
f.save('35-s10-cadena-evidencia')

f=Figure('Truncamiento: guardar no equivale a representar','Ejemplo didáctico: 900 tokens de contenido; límite total de 128; 2 tokens especiales.')
f.text(65,185,'FRAGMENTO GUARDADO: 900 TOKENS',26,True)
f.rect(65,240,1470,115,'#FBECEE',RED)
f.rect(65,240,206,115,'#CDEEE6',TEAL)
f.text(85,278,'126 tokens',27,True,TEAL);f.text(585,278,'774 tokens fuera de la entrada del encoder',28,True,RED)
f.text(65,381,'14 % del contenido entra',25,True,TEAL)
f.text(640,381,'86 % no contribuye directamente a este embedding',25,True,RED)
f.arrow(168,430,168,525,TEAL)
f.box(65,545,470,160,'Embedding',['El vector se calcula a partir','del prefijo efectivo.'],fill='#E2F3EE',accent=TEAL)
f.arrow(1100,430,1100,525,BLUE)
f.box(670,545,865,160,'Texto para el generador',['Si el registro se recupera, el prompt puede recibir','los 900 tokens almacenados, incluido el sufijo.'],fill='#EAF2FC')
f.box(65,770,1470,125,'Qué demuestra la comparación',['Si texto largo y prefijo producen la misma entrada, sus embeddings coinciden.'],fill='white')
f.footer('126 / 900 = 0,14 · El límite y los tokens especiales son supuestos del ejemplo, no valores universales.')
f.save('36-s10-truncamiento')

f=Figure('¿Dónde está disponible la respuesta?','Una misma pregunta puede ser respondible en los originales y carecer de evidencia en el prompt.')
rows=[(185,'1. Corpus original','Reglamento + instructivo escaneado + guías',1470,'#DFEBFB'),(375,'2. Contenido indexado','El escaneo no aportó texto al índice',1160,'#DCEFEA'),(565,'3. Contexto de la consulta','Solo los fragmentos seleccionados para el prompt',850,'#FFF0D9')]
for y,title,detail,w,color in rows:
 f.box(65,y,w,145,title,[detail],fill=color)
 if y<565:f.arrow(95,y+153,95,y+180)
f.text(1250,405,'Pérdida de ingesta',25,True,RED)
f.text(990,597,'Pérdida de selección',25,True,RED)
f.box(65,770,1470,125,'Dos evaluaciones compatibles',['Medir prudencia ante evidencia ausente y, por separado, la cobertura perdida por el sistema.'])
f.footer('Tamaños esquemáticos, sin porcentajes · Declara respecto de qué corpus defines las preguntas negativas.')
f.save('37-s10-corpus-y-contexto')

f=Figure('Hit Rate y MRR: ver los aportes de cada pregunta','Ocho preguntas respondibles. Verde = primer relevante; gris = candidato no relevante.')
f.text(75,185,'Pregunta',24,True)
for j in range(5): f.text(335+j*128,185,str(j+1),26,True)
f.text(1050,185,'H@5',26,True);f.text(1260,185,'RR@5',26,True)
ranks=[1,2,4,5,None,1,3,None]
for i,r in enumerate(ranks):
 y=233+i*69;f.text(95,y+13,f'q{i+1}',25,True)
 for j in range(1,6):
  green=j==r;f.rect(292+(j-1)*128,y,105,48,'#CDEEE6' if green else '#E0E6EE',TEAL if green else '#CCD5E0',9)
  if green:f.text(321+(j-1)*128,y+10,'R',25,True,TEAL)
 f.text(1072,y+12,'1' if r else '0',25,True)
 f.text(1268,y+12,('1' if r==1 else f'1/{r}') if r else '0',25,True)
f.box(65,817,650,88,'A k = 3: H = 0,50 | MRR = 0,3542',[],fill='#EAF2FC')
f.box(765,817,770,88,'A k = 5: H = 0,75 | MRR = 0,4104',[],fill='#E2F3EE',accent=TEAL)
f.footer('Datos inventados para aprender · Mismo corte y población: 0 ≤ MRR@k ≤ Hit Rate@k ≤ 1.')
f.save('38-s10-metricas-por-pregunta')

f=Figure('Abstención: dos decisiones, dos denominadores','Responder requiere además comprobar corrección, fidelidad y completitud.')
f.text(440,190,'EL SISTEMA RESPONDE',27,True)
f.text(1030,190,'EL SISTEMA SE ABSTIENE',27,True)
f.text(65,322,'RESPONDIBLE',26,True);f.text(65,365,'Hay evidencia',23)
f.text(65,610,'NEGATIVA',26,True);f.text(65,653,'No hay evidencia',23)
f.box(395,265,535,230,'Decisión potencialmente útil',['Aún hay que revisar la respuesta.','En el ejemplo: 6 de 8 casos.'],fill='#E2F3EE',accent=TEAL)
f.box(975,265,560,230,'Abstención indebida',['Se pierde una respuesta posible.','2 / 8 = 25 % de respondibles.'],fill='#FBECEE',accent=RED)
f.box(395,545,535,230,'Respuesta sin soporte suficiente',['Puede inventar información.','En el ejemplo: 1 de 2 casos.'],fill='#FBECEE',accent=RED)
f.box(975,545,560,230,'Abstención correcta',['Reconoce falta de evidencia.','1 / 2 = 50 % de negativas.'],fill='#E2F3EE',accent=TEAL)
f.text(65,840,'Siempre abstenerse: 100 % correcta sobre negativas Y 100 % indebida sobre respondibles.',27,True)
f.footer('Ejemplo inventado: 8 respondibles + 2 negativas · Las etiquetas dependen del corpus de referencia declarado.')
f.save('39-s10-matriz-abstencion')

f=Figure('La extensión se elige después del diagnóstico','Los promedios orientan; inspeccionar casos permite formular una hipótesis.')
for x,t in [(65,'SÍNTOMA'),(465,'VERIFICA'),(885,'PRUEBA'),(1215,'OBSERVA')]:f.text(x,185,t,24,True,BLUE)
rows=[
 ('Evidencia perdida',['Texto extraído, cortes','y límite del encoder'],'A · Fragmentación',['Cobertura de evidencia','y recuperación']),
 ('Falla en códigos',['Código correcto en','texto y candidatos'],'B · Híbrida',['Aciertos en consultas','con términos exactos']),
 ('Relevante llega tarde',['Posición dentro de','la lista de candidatos'],'C · Reranking',['MRR y cruces del','corte final']),
 ('Recuperación sólida',['Afirmaciones, citas','y condiciones omitidas'],'D · Evaluación',['Fidelidad y pertinencia','con revisión de casos'])]
for i,(sym,ver,act,obs) in enumerate(rows):
 y=245+156*i;f.rect(65,y,1470,126,'white')
 f.text(85,y+42,sym,26,True)
 for n,t in enumerate(ver):f.text(465,y+28+34*n,t,23)
 f.text(885,y+42,act,25,True,TEAL)
 for n,t in enumerate(obs):f.text(1215,y+28+34*n,t,23)
f.text(65,894,'Conserva corpus, referencia y condiciones comparables. Mide también costo y latencia.',26,True)
f.footer('No es una receta automática · Un reranker no añade candidatos ausentes; medir no mejora por sí solo.')
f.save('40-s10-diagnostico-extensiones')
print('6 PNG y 6 SVG generados en',OUT)
