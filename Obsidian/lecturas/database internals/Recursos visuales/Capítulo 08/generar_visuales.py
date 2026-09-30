"""Genera un contraste didáctico propio de efecto duplicado y deduplicación."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import textwrap
OUT=Path(__file__).resolve().parent
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
FONTB='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
font=ImageFont.truetype(FONT,27)
small=ImageFont.truetype(FONT,23)
head=ImageFont.truetype(FONTB,34)
im=Image.new('RGB',(1600,1060),'#f8fafc');d=ImageDraw.Draw(im)
d.text((65,40),'Se perdió el ACK: ¿qué ocurre al reintentar?',font=head,fill='#0f172a')
d.text((65,95),'Mismo síntoma para el cliente. Distinta garantía sobre el efecto.',font=font,fill='#334155')

def txt(x,y,text,width,ft=font,fill='#0f172a'):
    wrapped=textwrap.fill(text,width=width)
    box=d.multiline_textbbox((x,y),wrapped,font=ft,spacing=10)
    assert box[2]<1570
    d.multiline_text((x,y),wrapped,font=ft,fill=fill,spacing=10)
    return box[3]

def rect(x,y,w,h,text,color):
    d.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=color,outline='#cbd5e1',width=2)
    b=txt(x+22,y+22,text,21)
    assert b<y+h-10

def arrow(x,y,x2,color):
    d.line((x,y,x2,y),fill=color,width=5)
    d.polygon([(x2,y),(x2-14,y-9),(x2-14,y+9)],fill=color)

for row,(title,c,first,last,total) in enumerate([
 ('Sin identificación estable','#b91c1c','Solicitud: cobrar 20','Nuevo intento: cobrar 20','Total: 40'),
 ('Con ID y registro durable atómico','#0369a1','ID 42: cobrar 20','Mismo ID 42: devolver resultado','Total: 20')]):
    y=170+row*420
    d.text((65,y),title,font=head,fill=c)
    rect(65,y+70,365,140,first,'#ffffff')
    rect(610,y+70,365,140,'Efecto aplicado: cobro de 20','#ffffff')
    arrow(442,y+140,594,c)
    txt(465,y+90,'Envío',10,small)
    d.line((970,y+245,250,y+245),fill='#64748b',width=4)
    d.line((490,y+229,523,y+262),fill='#b91c1c',width=6)
    d.line((490,y+262,523,y+229),fill='#b91c1c',width=6)
    d.text((580,y+260),'Confirmación perdida',font=small,fill='#b91c1c')
    rect(1090,y+70,440,140,last,'#ffffff')
    arrow(990,y+140,1075,c)
    d.text((1115,y+235),total,font=head,fill=c)
    if row==1:
        txt(65,y+305,'Efecto + ID se comprometen juntos. El ID también sobrevive al reinicio.',80,small)
    else:
        txt(65,y+305,'El cliente no vio respuesta, pero el primer cobro ya ocurrió.',80,small)

d.text((65,1015),'El ACK perdido no demuestra que el efecto haya fallado. Modelo de aplicación, no de TCP.',font=small,fill='#475569')
im.save(OUT/'ack_perdido.png')
print(OUT/'ack_perdido.png')
