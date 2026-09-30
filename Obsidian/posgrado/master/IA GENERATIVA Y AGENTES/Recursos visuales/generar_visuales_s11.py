"""Figuras originales S11. Ejecutar con Python y Pillow; salida junto al script."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math, html
ROOT=Path(__file__).parent
INK="#183247"; BLUE="#dcecf7"; GREEN="#dff2e9"; ORANGE="#fff0d6"; RED="#fbe2df"; MUTED="#526777"
class Figure:
 def __init__(self,title,sub):
  self.im=Image.new("RGB",(1400,850),"#fafcfe"); self.d=ImageDraw.Draw(self.im)
  self.svg=['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="850" viewBox="0 0 1400 850"><rect width="1400" height="850" fill="#fafcfe"/>']
  self.text(55,35,title,34,True); self.text(55,88,sub,21,color=MUTED)
 def text(self,x,y,s,size=24,bold=False,color=INK):
  font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial'+(' Bold' if bold else '')+'.ttf',size)
  for j,line in enumerate(s.split('\n')):
   yy=y+j*(size+9); self.d.text((x,yy),line,font=font,fill=color)
   self.svg.append(f'<text x="{x}" y="{yy+size}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{html.escape(line)}</text>')
 def rect(self,x,y,w,h,fill,stroke=INK):
  self.d.rounded_rectangle((x,y,x+w,y+h),radius=12,fill=fill,outline=stroke,width=2)
  self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
 def box(self,x,y,w,h,s,fill=BLUE):
  self.rect(x,y,w,h,fill); self.text(x+18,y+18,s,24)
 def line(self,pts,color=INK,width=3,arrow=False):
  self.d.line(pts,fill=color,width=width)
  self.svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in pts)+f'" fill="none" stroke="{color}" stroke-width="{width}"/>')
  if arrow:
   x,y=pts[-1]; a=math.atan2(y-pts[-2][1],x-pts[-2][0]); pp=[(x,y),(x-15*math.cos(a-.45),y-15*math.sin(a-.45)),(x-15*math.cos(a+.45),y-15*math.sin(a+.45))]
   self.d.polygon(pp,fill=color);self.svg.append('<polygon points="'+' '.join(f'{u},{v}' for u,v in pp)+f'" fill="{color}"/>')
 def save(self,name,foot):
  self.text(55,785,foot,18,color=MUTED);self.im.save(ROOT/(name+'.png')); (ROOT/(name+'.svg')).write_text(''.join(self.svg)+'</svg>')

f=Figure('41 · Quién decide el próximo paso','Tres arquitecturas: la diferencia está en el control del flujo.')
f.text(55,160,'CHATBOT',23,True); f.text(55,340,'PIPELINE RAG',23,True); f.text(55,530,'AGENTE',23,True)
for x,s in [(300,'Pregunta'),(650,'LLM'),(1000,'Texto')]: f.box(x,145,260,80,s)
for x in [560,910]: f.line([(x,185),(x+90,185)],arrow=True)
for x,s in [(300,'Recuperar'),(650,'Construir contexto'),(1000,'Generar')]: f.box(x,310,260,100,s)
for x in [560,910]: f.line([(x,360),(x+90,360)],arrow=True)
f.text(310,425,'Tu código fija la secuencia, incluso si hay varias llamadas al LLM.',21)
for x,s in [(300,'Decidir'),(650,'Ejecutar tool'),(1000,'Observar')]: f.box(x,515,260,90,s,ORANGE)
for x in [560,910]: f.line([(x,560),(x+90,560)],arrow=True)
f.line([(1130,605),(1130,675),(430,675),(430,605)],arrow=True)
f.text(550,688,'Otra decisión con la nueva evidencia',21)
f.line([(430,515),(430,480),(1130,480)],arrow=True); f.text(720,450,'Salida: respuesta final o límite',19)
f.save('41-s11-quien-decide','Esquema didáctico. Un agente puede finalizar sin usar herramientas si la tarea ya está resuelta.')

f=Figure('42 · PEAS aplicado a un asistente de ventas','Primero especifica qué cuenta como éxito; después diseña el sistema.')
f.box(55,160,1285,95,'P · Desempeño: resultado correcto, evidencia trazable y uso limitado de recursos',GREEN)
f.box(55,320,310,245,'E · Entorno\nBase de ventas\nReglas del negocio\nArchivos y usuario')
f.box(500,310,350,120,'S · Sensores\nPregunta y resultados',BLUE)
f.box(500,520,350,120,'A · Actuadores\nConsultas y respuesta',ORANGE)
f.box(1010,340,330,250,'SISTEMA AGENTE\nLLM: propone\nHarness: valida\ny ejecuta\nEstado: historial',GREEN)
f.line([(365,370),(500,370)],arrow=True);f.line([(850,370),(1010,370)],arrow=True)
f.line([(1010,570),(850,570)],arrow=True);f.line([(500,570),(210,570),(210,565)],arrow=True)
f.text(65,700,'El LLM recibe observaciones parciales; no ve toda la base de datos.',25,True)
f.save('42-s11-peas','Ejemplo propio. Las herramientas pueden percibir, actuar o hacer ambas cosas.')

f=Figure('43 · Una llamada recorre tres participantes','El identificador c1 permite emparejar la solicitud con su resultado.')
for x,s in [(100,'LLM'),(565,'Harness / código'),(1090,'Herramienta')]:
 f.box(x,145,230,75,s,GREEN);f.line([(x+115,230),(x+115,730)],color='#b4c3ce',width=2)
for y,a,b,s in [(300,215,680,'1. c1: total_ventas(mes)'),(400,680,1205,'2. Validar y ejecutar'),(500,1205,680,'3. Devuelve 15000 USD'),(600,680,215,'4. Resultado de c1 al contexto')]:
 f.line([(a,y),(b,y)],arrow=True); f.text(min(a,b)+10,y-42,s,22)
f.text(80,680,'5. Nueva decisión: otra llamada o respuesta final',24,True)
f.save('43-s11-llamada-y-resultado','Una llamada fallida también debe obtener un resultado: un error estructurado y asociado a su id.')

f=Figure('44 · La descripción orienta; el código controla','Son dos responsabilidades diferentes y ambas deben estar presentes.')
f.box(55,160,580,250,'LO QUE RECIBE EL MODELO\nNombre de la herramienta\nCuándo usarla y cuándo no\nParámetros y restricciones\nFormato del resultado',BLUE)
f.box(765,160,580,250,'LO QUE HACE EL HARNESS\nComprueba nombre permitido\nValida estructura y dominio\nAplica permisos y límites\nEjecuta y registra el resultado',GREEN)
f.line([(635,285),(765,285)],arrow=True)
f.box(55,490,580,180,'Ejemplo de selección\n"Dame el total de marzo"\ntotal_ventas(mes="2026-03")',ORANGE)
f.box(765,490,580,180,'Ejemplo de rechazo\nmes="2026-99"\nError: mes fuera del dominio',RED)
f.text(65,718,'Escribir "solo lectura" en un prompt no cambia los permisos de la base.',23,True)
f.save('44-s11-contrato-herramienta','Esquema conceptual de diseño, independiente de la API de un proveedor.')

f=Figure('45 · Cada vuelta añade contexto','Supuestos: 1000 tokens iniciales; cada llamada + resultado añade 500 tokens.')
x0,y0=130,670; sx=175; sy=.115
for value in range(0,4001,1000):
 y=y0-value*sy;f.line([(x0,y),(1250,y)],color='#d1dbe3',width=1);f.text(60,y-12,str(value),19)
f.line([(x0,150),(x0,y0),(1250,y0)],width=3)
pts=[]
for i in range(7):
 x=x0+i*sx;y=y0-(1000+500*i)*sy;pts.append((x,y));f.rect(x-5,y-5,10,10,'#137da3','#137da3');f.text(x-5,y0+15,str(i),21)
f.line(pts,color='#137da3',width=5)
y=y0-3500*sy; f.line([(x0,y),(1250,y)],color='#b46711',width=3);f.text(710,y-35,'Límite útil ilustrativo: 3500',21,color='#96570d')
f.text(440,730,'Llamadas de herramienta completadas',23)
f.text(145,140,'Tokens de entrada en la siguiente decisión',22)
f.save('45-s11-crecimiento-contexto','Datos calculados, no mediciones. Con 6 llamadas: 4000 > 3500. Costos de API y caché no modelados.')

f=Figure('46 · Toolformer: construir datos y ajustar pesos','La pérdida de predicción sirve para filtrar llamadas candidatas útiles.')
for x,s in [(55,'1. Texto original\n+ demostraciones'),(500,'2. Muestrear\nllamadas candidatas'),(945,'3. Ejecutar APIs\ny obtener resultados')]:f.box(x,180,395,125,s)
f.line([(450,245),(500,245)],arrow=True);f.line([(895,245),(945,245)],arrow=True)
f.box(945,460,395,145,'4. Filtrar\nConservar si la reducción\nde pérdida alcanza el umbral',ORANGE)
f.box(500,460,395,145,'5. Corpus aumentado\nTexto con llamadas\ny resultados',GREEN)
f.box(55,460,395,145,'6. Ajuste fino\nLos parámetros cambian\nθ → θ nuevo',GREEN)
f.line([(1140,305),(1140,460)],arrow=True);f.line([(945,530),(895,530)],arrow=True);f.line([(500,530),(450,530)],arrow=True)
f.text(65,680,'En la inferencia posterior: emitir llamada → ejecutar fuera del modelo → continuar texto.',22)
f.save('46-s11-toolformer-aprendizaje','Redibujo conceptual propio basado en Schick et al. (2023), sección 2. No es un entrenamiento ejecutado aquí.')

f=Figure('47 · Toolformer: el comparador cambia por tarea','Resultados históricos de 2023; cada panel tiene su propio protocolo de evaluación.')
rows=[('LAMA · T-REx',53.5,39.8,'GPT-3'),('Matemáticas · ASDiv',40.4,14.8,'Toolformer sin llamadas'),('QA · TriviaQA',48.8,65.9,'GPT-3'),('MLQA · árabe',3.7,8.2,'GPT-J sin ajustar')]
for i,(label,a,b,other) in enumerate(rows):
 y=150+i*148;f.text(55,y,label,23,True)
 for yy,val,col,lab in [(y+38,a,'#16866b','Toolformer'),(y+78,b,'#7a8da1',other)]:
  f.rect(430,yy,val*8,28,col,col);f.text(1080,yy,lab,19);f.text(440+val*8,yy,f'{val:.1f}',20)
for v in [0,20,40,60,80]:f.text(425+v*8,755,str(v),19)
f.text(1130,750,'Puntaje (%)',20)
f.save('47-s11-toolformer-resultados','Fuente: paper local, tablas 3–6, pp. PDF 6–7. No comparar directamente los puntajes entre tareas.')

f=Figure('48 · Parar también forma parte del diseño','Definición del ejemplo: un paso es una decisión del modelo, incluso si finaliza.')
f.box(55,160,350,100,'¿Quedan pasos?',ORANGE)
f.box(520,160,350,100,'Decisión del modelo',BLUE)
f.box(990,160,350,100,'¿Es respuesta final?',ORANGE)
f.line([(405,210),(520,210)],arrow=True);f.text(440,170,'Sí',20)
f.line([(870,210),(990,210)],arrow=True)
f.box(990,360,350,110,'Sí: terminar\nGuardar respuesta',GREEN)
f.line([(1165,260),(1165,360)],arrow=True)
f.box(520,520,350,115,'No: validar, ejecutar\ny añadir resultado',BLUE)
f.line([(990,240),(930,240),(930,575),(870,575)],arrow=True)
f.line([(520,575),(455,575),(455,290),(230,290),(230,260)],arrow=True);f.text(260,610,'Siguiente decisión',22)
f.box(55,335,350,115,'No: cierre incompleto\nExplicar qué falta',RED)
f.line([(100,260),(100,335)],arrow=True)
f.text(65,715,'El límite de pasos no reemplaza el timeout de cada operación.',25,True)
f.save('48-s11-parada','Esquema del simulador incluido. Otros programas pueden contar pasos de forma diferente.')
