"""Diagramas originales para capítulo 7. Requiere Pillow: uv run --with pillow python generar_visuales.py."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap
out=Path(__file__).resolve().parent
font_path='/System/Library/Fonts/Supplemental/Arial.ttf'
bold_path='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
font=lambda size,bold=False: ImageFont.truetype(bold_path if bold else font_path,size)
W,H=1500,900
bg='#f5f7fb'; ink='#182e46'; blue='#dbeafe'; green='#d8f0e2'; yellow='#fff0c9'; gray='#e3e7ee'; red='#fbdeda'
def base(title,subtitle):
 im=Image.new('RGB',(W,H),bg);d=ImageDraw.Draw(im)
 d.text((55,35),title,font=font(38,True),fill=ink)
 d.text((55,95),subtitle,font=font(23),fill=ink)
 return im,d
def box(d,xy,title,lines,color):
 x,y,x2,y2=xy;d.rounded_rectangle(xy,18,fill=color,outline='#7d92aa',width=2)
 d.text((x+22,y+19),title,font=font(26,True),fill=ink)
 yy=y+63
 for line in lines:
  assert d.textbbox((0,0),line,font=font(23))[2]<x2-x-36,line
  d.text((x+22,yy),line,font=font(23),fill=ink);yy+=34
 assert yy<y2+10

def arrow(d,start,end,label=None):
 d.line([start,end],fill=ink,width=4)
 x,y=end;d.polygon([(x,y),(x-13,y-9),(x-13,y+9)],fill=ink)
 if label:d.text((start[0]+18,start[1]-35),label,font=font(20),fill=ink)

im,d=base('Publicar un flush sin dejar huecos','El archivo incompleto aún no forma parte de la vista de lectura.')
d.text((55,160),'ANTES DE PUBLICAR',font=font(26,True),fill=ink)
box(d,(55,215,470,400),'Memtable activa M2',['Nuevas escrituras','Lecturas permitidas'],blue)
box(d,(535,215,950,400),'Memtable congelada M1',['Solo lecturas','Se escribe su contenido'],green)
box(d,(1015,215,1445,400),'Salida incompleta',['No sirve lecturas','Archivo en construcción'],yellow)
arrow(d,(950,340),(1010,340))
d.text((55,475),'DESPUÉS DE PUBLICAR LA NUEVA VISTA',font=font(26,True),fill=ink)
box(d,(55,535,470,720),'Memtable activa M2',['Nuevas escrituras','Lecturas permitidas'],blue)
box(d,(535,535,950,720),'M1 retirada de la vista',['Lectores previos terminan','Luego se libera memoria'],gray)
box(d,(1015,535,1445,720),'SSTable publicada',['Completa y recuperable','Lecturas permitidas'],green)
d.text((55,795),'El WAL se retira solo cuando sus operaciones ya están protegidas por datos durables.',font=font(24),fill=ink)
im.save(out/'01 ciclo_flush.png')

im,d=base('Borrar una copia no borra la clave','Una marca de borrado debe dominar las versiones anteriores.')
box(d,(55,185,720,330),'Estado inicial de ambos casos',['Disco: k = azul, versión 1','RAM: k = verde, versión 2'],blue)
box(d,(805,185,1445,330),'Lectura inicial',['La versión 2 domina a la 1','Resultado: verde'],green)
box(d,(55,405,720,675),'Solo quitar la entrada de RAM',['Disco: azul @1','RAM: sin entrada para k','','Resultado: azul reaparece'],red)
box(d,(805,405,1445,675),'Escribir un tombstone',['Disco: azul @1, verde @2','RAM: BORRADO @3','','Resultado actual: ausente'],green)
d.text((55,765),'La compactación conserva la marca si quedan versiones antiguas fuera de sus entradas.',font=font(24),fill=ink)
d.text((55,812),'Los snapshots pueden requerir versiones históricas que la lectura actual ya no devuelve.',font=font(24),fill=ink)
im.save(out/'02 borrado_y_resurreccion.png')

im,d=base('Separar claves ordenadas y valores','Comparación conceptual: LSM con registros completos y diseño WiscKey.')
box(d,(55,185,660,400),'LSM con claves y valores',['Tabla ordenada:','10 → valor grande A','20 → valor grande B','30 → valor grande C'],blue)
box(d,(805,185,1445,400),'La compactación copia',['Claves + valores','Orden conservado en la salida','Más bytes si los valores son grandes'],yellow)
arrow(d,(665,285),(800,285))
box(d,(55,475,660,735),'Índice de claves de WiscKey',['Tabla ordenada de referencias:','10 → offset 200','20 → offset 0','30 → offset 400'],blue)
box(d,(805,475,1445,735),'Log de valores',['Offset 0: valor B','Offset 200: valor A','Offset 400: valor C','Recolección separada del índice'],green)
arrow(d,(665,590),(800,590),'Consulta')
d.text((55,807),'El rango 10–30 conserva orden lógico, pero sus valores no están en ese orden físico.',font=font(24),fill=ink)
im.save(out/'03 claves_y_valores.png')
print('3 PNG generated')
