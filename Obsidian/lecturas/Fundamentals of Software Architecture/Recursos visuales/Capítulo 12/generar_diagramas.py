from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
P=Path(__file__).resolve().parent;P.mkdir(parents=True,exist_ok=True)
F='/System/Library/Fonts/Supplemental/Arial.ttf';B='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def canvas(title,subtitle):
 im=Image.new('RGB',(1600,900),'#f5f7fa');d=ImageDraw.Draw(im)
 d.text((65,40),title,font=ImageFont.truetype(B,38),fill='#172b4d');d.text((65,100),subtitle,font=ImageFont.truetype(F,25),fill='#344563');return im,d
def box(d,xy,lines,fill='#deebff'):
 d.rounded_rectangle(xy,20,fill=fill,outline='#172b4d',width=3)
 text='\n'.join(lines);font=ImageFont.truetype(F,25);bb=d.multiline_textbbox((0,0),text,font=font,spacing=8,align='center');x=(xy[0]+xy[2]-(bb[2]-bb[0]))/2;y=(xy[1]+xy[3]-(bb[3]-bb[1]))/2
 d.multiline_text((x,y),text,font=font,fill='#172b4d',spacing=8,align='center')
def arrow(d,a,b,label=None):
 d.line([a,b],fill='#172b4d',width=4)
 x,y=b
 if b[0]>a[0]:pts=[(x,y),(x-15,y-9),(x-15,y+9)]
 elif b[1]>a[1]:pts=[(x,y),(x-9,y-15),(x+9,y-15)]
 else:pts=[(x,y),(x-9,y+15),(x+9,y+15)]
 d.polygon(pts,fill='#172b4d')
 if label:d.text(((a[0]+b[0])/2-40,(a[1]+b[1])/2-38),label,font=ImageFont.truetype(F,21),fill='#344563')
im,d=canvas('Un flujo lógico, dos formas de desplegarlo','El papel de cada filtro se conserva; cambia la frontera de ejecución.')
d.rounded_rectangle((55,175,1545,460),20,outline='#536878',width=3);d.text((80,195),'UN SOLO DESPLIEGUE',font=ImageFont.truetype(B,24),fill='#172b4d')
for i,(a,b) in enumerate([('Leer','Productor'),('Validar','Tester'),('Calcular','Transformador'),('Guardar','Consumidor')]):
 x=90+i*365;box(d,(x,275,x+295,410),[a,b]);
 if i<3:arrow(d,(x+295,342),(x+365,342))
d.text((65,500),'CUATRO DESPLIEGUES: cada enlace cruza la red',font=ImageFont.truetype(B,25),fill='#172b4d')
for i,(a,b) in enumerate([('Leer','Servicio 1'),('Validar','Servicio 2'),('Calcular','Servicio 3'),('Guardar','Servicio 4')]):
 x=90+i*365;box(d,(x,575,x+295,735),[a,b],fill='#ffedcc')
 if i<3:arrow(d,(x+295,655),(x+365,655),'canal')
d.text((65,800),'Separar filtros facilita cambios. Separar despliegues añade transporte, fallos parciales y operación.',font=ImageFont.truetype(F,25),fill='#344563');im.save(P/'c12-01-topologia.png')
im,d=canvas('Una función de aptitud puede ser un pipeline','Recreación conceptual de la figura 12-2: datos → selección → análisis → informe.')
labels=[['Capturar datos','Productor'],['Seleccionar período','Transformador'],['Analizar tendencia','Transformador'],['Generar informe','Consumidor']]
for i,lines in enumerate(labels):
 x=65+i*385;box(d,(x,350,x+310,505),lines)
 if i<3:arrow(d,(x+310,427),(x+385,427))
box(d,(65,175,375,280),['Datos brutos'],'#e3fcef');arrow(d,(220,280),(220,350))
box(d,(450,620,760,730),['Reglas de selección'],'#e3fcef');arrow(d,(605,620),(605,505))
box(d,(835,620,1145,730),['Resultados analíticos'],'#e3fcef');arrow(d,(990,505),(990,620))
box(d,(1220,620,1530,730),['Informe final'],'#ffedcc');arrow(d,(1375,505),(1375,620))
d.text((65,800),'Los almacenes apoyan a cada etapa; no sustituyen los canales que conectan el procesamiento.',font=ImageFont.truetype(F,25),fill='#344563');im.save(P/'c12-02-datos.png')
im,d=canvas('Clasificar telemetría antes de calcular','Recreación conceptual de la figura 12-4. Cada dato recorre la ruta de su tipo.')
box(d,(50,220,310,355),['Capturar de Kafka','Productor']);box(d,(450,220,720,355),['¿Es duración?','Tester']);box(d,(900,220,1170,355),['¿Es uptime?','Tester']);box(d,(1310,220,1550,355),['Fin sin guardar'],'#ffedcc')
arrow(d,(310,288),(450,288));arrow(d,(720,288),(900,288),'no');arrow(d,(1170,288),(1310,288),'no')
box(d,(450,480,720,615),['Calcular duración','Transformador']);box(d,(900,480,1170,615),['Calcular uptime','Transformador'])
arrow(d,(585,355),(585,480),'sí');arrow(d,(1035,355),(1035,480),'sí')
box(d,(700,710,1050,845),['Guardar en MongoDB','Consumidor'],'#e3fcef')
d.line([(585,615),(585,778),(700,778)],fill='#172b4d',width=4);arrow(d,(585,778),(700,778))
d.line([(1035,615),(1120,615),(1120,778)],fill='#172b4d',width=4);d.line([(1120,778),(1050,778)],fill='#172b4d',width=4);d.polygon([(1050,778),(1065,769),(1065,787)],fill='#172b4d')
im.save(P/'c12-03-telemetria.png')
