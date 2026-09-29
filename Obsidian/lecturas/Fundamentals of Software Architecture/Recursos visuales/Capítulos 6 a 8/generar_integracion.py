"""Gráfico didáctico original. Ejecutar con Python y Pillow; no requiere red."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).resolve().parent
im = Image.new('RGB', (1600, 1080), '#f8fafc')
d = ImageDraw.Draw(im)
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
NAVY, BLUE, TEAL, GRAY = '#16324f', '#2463a5', '#007f83', '#576575'

def text(x, y, s, size=24, color=NAVY, bold=False):
    d.text((x,y), s, font=ImageFont.truetype(BOLD if bold else FONT,size), fill=color)

def box(x,y,w,h,lines,color=BLUE):
    d.rounded_rectangle((x,y,x+w,y+h),radius=9,fill='white',outline=color,width=3)
    for i,s in enumerate(lines):
        text(x+18,y+17+i*31,s,24,color if i==0 else NAVY,i==0)

def arrow(x1,y1,x2,y2,label=None):
    d.line((x1,y1,x2,y2),fill=TEAL,width=4)
    a=math.atan2(y2-y1,x2-x1)
    pts=[(x2,y2)]+[(x2-15*math.cos(a+t),y2-15*math.sin(a+t)) for t in [-.5,.5]]
    d.polygon(pts,fill=TEAL)
    if label: text((x1+x2)/2-50,(y1+y2)/2-32,label,19,TEAL)

def database(x,y,label):
    d.rectangle((x,y+15,x+220,y+66),fill='#e7f4f4',outline=TEAL,width=3)
    d.ellipse((x,y+50,x+220,y+82),fill='#e7f4f4',outline=TEAL,width=3)
    d.rectangle((x+3,y+45,x+217,y+65),fill='#e7f4f4')
    d.ellipse((x,y,x+220,y+32),fill='white',outline=TEAL,width=3)
    text(x+20,y+38,label,23)

text(50,30,'De responsabilidades a límites verificables',42,bold=True)
text(50,90,'Ejemplo propio: PedidoClaro. Los capítulos 8, 7 y 6 se aplican juntos.',25,GRAY)

for x,title,subtitle in [(50,'1. COMPONENTES · cap. 8','Qué responsabilidad tiene cada parte'),
                          (570,'2. QUANTUM · cap. 7','Qué necesita para funcionar'),
                          (1090,'3. GOBIERNO · cap. 6','Qué evidencia protege la decisión')]:
    text(x,163,title,26,bold=True)
    text(x,203,subtitle,22,GRAY)

box(70,276,360,91,['Capturar pedido','Valida y registra la intención'])
box(70,426,360,91,['Reservar existencias','Acepta o rechaza la reserva'])
box(70,576,360,91,['Notificar estado','Informa el resultado'])
arrow(245,367,245,426)
arrow(245,517,245,576)
text(70,697,'Flechas: colaboración lógica.',22,GRAY)
text(70,730,'Aún no dicen HTTP, cola o proceso.',22,GRAY)

d.rounded_rectangle((570,260,1025,768),radius=15,outline=TEAL,width=4)
text(595,280,'UN QUANTUM EN ESTE EJEMPLO',22,TEAL,True)
box(605,340,385,138,['Un desplegable','Capturar + reservar + notificar','Contratos entre módulos'])
arrow(795,478,795,539)
database(685,540,'BD de pedidos')
text(595,653,'La BD es una dependencia necesaria.',22,GRAY)
text(595,690,'Separar módulos no crea por sí solo',22,GRAY)
text(595,724,'varios quanta ni varios servicios.',22,GRAY)
arrow(450,471,553,471)

box(1100,276,440,100,['Regla estructural','Sin ciclos entre módulos'])
box(1100,431,440,130,['Escenario operacional','p95 de aceptación ≤ 300 ms','con 40 solicitudes/s'])
box(1100,616,440,122,['Decisión al observar evidencia','Verde: continuar bajo ese ensayo','Rojo: investigar y corregir'])
arrow(1320,376,1320,431)
arrow(1320,561,1320,616)
arrow(1040,471,1083,471)

d.line((50,815,1550,815),fill='#cbd5e1',width=2)
text(50,845,'Lectura: responsabilidad → dependencia necesaria → prueba de la propiedad',29,bold=True)
text(50,900,'Un límite se justifica por el dominio y por capacidades necesarias; después se comprueba con evidencia.',25)
text(50,945,'Si falla el ensayo, hay que distinguir código, base de datos, infraestructura y condiciones de carga.',25)
text(50,1010,'Supuestos didácticos. El gráfico no prescribe monolitos ni distribuye servicios automáticamente.',22,GRAY)
im.save(OUT/'c678-integracion.png')
