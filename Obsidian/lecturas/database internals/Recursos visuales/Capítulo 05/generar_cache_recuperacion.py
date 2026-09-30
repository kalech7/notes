#!/usr/bin/env python3
"""Diagramas de estudio del capítulo 5. Ejecutar: uv run --with pillow este_script.py.

01–03 adaptan las figuras 5-1, 5-2 y 5-3 (pp. 82, 87, 88) a español.
04–05 son elaboraciones didácticas propias sobre WAL y ARIES (pp. 88–93).
No representan estadísticas, ni tamaños o tiempos proporcionales.
"""
from pathlib import Path
from math import sin, cos, atan2, pi
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
W, H = 1800, 1120
BG = '#F8FAFC'
INK = '#17304A'
MUTED = '#53667A'
BLUE = '#2563A6'
BLUE_L = '#E4EFFC'
TEAL = '#087F8C'
TEAL_L = '#DCF4F0'
ORANGE = '#B96B18'
ORANGE_L = '#FFF0D9'
RED = '#AD4352'
RED_L = '#FCE8EC'
LINE = '#BCD0DE'
FONT_ROOT = Path('/System/Library/Fonts/Supplemental')

def font(size=30, bold=False):
    p = FONT_ROOT / ('Arial Bold.ttf' if bold else 'Arial.ttf')
    if not p.exists():
        p = Path('/usr/share/fonts/truetype/dejavu') / ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')
    return ImageFont.truetype(str(p), size)

def canvas(title, subtitle, footer):
    im = Image.new('RGB', (W,H), BG)
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((50,45,62,130), radius=5, fill=TEAL)
    d.text((85,48), title, font=font(48,True), fill=INK)
    d.text((85,111), subtitle, font=font(28), fill=MUTED)
    d.line((80,1033,1720,1033), fill=LINE,width=2)
    d.text((80,1055),footer,font=font(23),fill=MUTED)
    return im,d

def txt(d, xy, s, size=30, color=INK, bold=False, anchor=None, spacing=9):
    if anchor == 'mt':
        for i,line in enumerate(s.split('\n')):
            d.text((xy[0],xy[1]+i*(size+spacing)),line,font=font(size,bold),fill=color,anchor=anchor)
    else:
        d.multiline_text(xy,s,font=font(size,bold),fill=color,anchor=anchor,spacing=spacing,align='center' if anchor else 'left')

def box(d, bounds, s='', fill='white', outline=LINE, size=30, color=INK, bold=False):
    d.rounded_rectangle(bounds,radius=18,fill=fill,outline=outline,width=3)
    x1,y1,x2,y2=bounds
    if s:
        lines=s.split('\n'); total=len(lines)*(size+9)-9
        for i,line in enumerate(lines):
            d.text(((x1+x2)/2,(y1+y2-total)/2+i*(size+9)),line,font=font(size,bold),fill=color,anchor='mt')

def arrow(d, points, color=BLUE, width=4, head=15):
    d.line(points,fill=color,width=width,joint='curve')
    x,y=points[-1]; a=atan2(y-points[-2][1],x-points[-2][0])
    d.polygon([(x,y),(x-head*cos(a-pi/6),y-head*sin(a-pi/6)),(x-head*cos(a+pi/6),y-head*sin(a+pi/6))],fill=color)

def save(im,name):
    im.save(OUT/name, optimize=True)

def cache():
    im,d=canvas('Caché de páginas: identidad y copia en memoria','La estructura del árbol, la posición en disco y el frame de RAM son cosas distintas.','Adaptación didáctica de la figura 5-1 · PDF 4 · impresa 82. Identificadores y distribución: ejemplo propio.')
    txt(d,(95,198),'Árbol lógico',36,bold=True)
    nodes={'P1':(365,305),'P2':(220,455),'P3':(510,455),'P4':(95,620),'P5':(265,620),'P6':(455,620),'P7':(625,620)}
    for parent,child in [('P1','P2'),('P1','P3'),('P2','P4'),('P2','P5'),('P3','P6'),('P3','P7')]:
        x,y=nodes[parent]; xx,yy=nodes[child]; arrow(d,[(x,y+40),(xx,yy-40)],LINE)
    for key,(x,y) in nodes.items():
        box(d,(x-64,y-40,x+64,y+40),key,ORANGE_L if key=='P6' else TEAL_L if key in ['P1','P3'] else 'white',ORANGE if key=='P6' else TEAL if key in ['P1','P3'] else LINE,32,bold=True)
    txt(d,(105,722),'Una página puede contener varias claves.\nLas flechas del árbol son referencias lógicas.',26,color=MUTED)
    txt(d,(825,198),'Tabla de páginas',36,bold=True)
    txt(d,(1280,198),'Buffer pool · RAM',36,bold=True)
    txt(d,(827,261),'ID de página  →  frame',26,color=MUTED)
    rows=[('P1','F2','limpia',BLUE_L),('P3','F0','limpia',BLUE_L),('P6','F1','sucia',ORANGE_L)]
    for i,(p,f,status,fill) in enumerate(rows):
        y=320+i*125
        box(d,(820,y,1130,y+92),f'{p}  →  {f}',fill,TEAL if status=='limpia' else ORANGE,32,bold=True)
        arrow(d,[(1130,y+46),(1260,y+46)],TEAL if status=='limpia' else ORANGE)
        box(d,(1260,y,1685,y+92),f'{f} · copia de {p} · {status}',fill,TEAL if status=='limpia' else ORANGE,30)
    box(d,(820,735,1685,820),'Sucia = la copia en RAM tiene cambios\nque todavía no están en su página de disco.',ORANGE_L,ORANGE,29)
    txt(d,(90,865),'Archivo de páginas · disco persistente',32,bold=True)
    for i,p in enumerate(['P5','P1','P7','P3','P6','P2','P4']):
        x=90+i*222;box(d,(x,920,x+192,994),p,BLUE_L,BLUE,31,bold=True)
    save(im,'01-cache-paginas.png')

def clock():
    im,d=canvas('CLOCK: segunda oportunidad al recorrer un anillo','El bit de acceso estima uso reciente. El pin indica si la página está en uso ahora.','Adaptación didáctica de la figura 5-2 · PDF 9 · impresa 87. Pin y reglas añadidos para aclarar conceptos.')
    cx,cy,r=485,550,255
    bits=[1,0,1,0,0,1,0,1]
    d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=LINE,width=4)
    positions=[]
    for i,bit in enumerate(bits):
        angle=-pi/2+i*pi/4;x=cx+r*cos(angle);y=cy+r*sin(angle);positions.append((x,y))
        box(d,(x-84,y-53,x+84,y+53),f'P{i+1}\nbit = {bit}',BLUE_L if bit else 'white',BLUE if bit else LINE,26,bold=True)
    x,y=positions[1];arrow(d,[(cx,cy),(x-48,y+45)],TEAL,6,22)
    d.ellipse((cx-10,cy-10,cx+10,cy+10),fill=TEAL)
    txt(d,(cx,cy+55),'aguja',28,color=TEAL,anchor='mt',bold=True)
    txt(d,(280,872),'P2: bit 0 y pin 0 → candidata',28,color=TEAL,bold=True)
    box(d,(95,935,820,995),'P4: bit 0, pero pin 1 → se omite',ORANGE_L,ORANGE,29)
    for i,(head,desc,fill,col) in enumerate([
        ('1 · Comprobar pin','Si pin > 0, la página está en uso.\nLa aguja avanza sin desalojarla.',ORANGE_L,ORANGE),
        ('2 · Si bit = 1','Bajar el bit a 0 y avanzar.\nLa página recibe otra oportunidad.',BLUE_L,BLUE),
        ('3 · Si bit = 0 y pin = 0','Puede elegirse como víctima.\nSi está sucia, requiere flush seguro.',TEAL_L,TEAL)]):
        y=240+i*230
        box(d,(935,y,1710,y+205),fill=fill,outline=col)
        txt(d,(965,y+28),head,33,bold=True,color=col)
        txt(d,(965,y+91),desc,29)
    txt(d,(945,952),'Cada acceso vuelve a poner el bit en 1.',29,color=MUTED)
    save(im,'02-clock.png')

def tinylfu():
    im,d=canvas('W-TinyLFU: admisión por frecuencia y colas de recencia','TinyLFU aporta el filtro; la ventana y las colas organizan la permanencia.','Adaptación didáctica de la figura 5-3 · PDF 10 · impresa 88. Ejemplo de decisión y precisión W-TinyLFU: propios.')
    centers=[240,665,1130,1575]
    specs=[(80,390,'Admisión','Ventana de\nnuevas páginas',BLUE_L,BLUE),(510,820,'Filtro de\nfrecuencia','Compara candidato\ny posible víctima',ORANGE_L,ORANGE),(975,1285,'Prueba','Probation:\npáginas vulnerables',TEAL_L,TEAL),(1420,1730,'Protegida','Páginas que han\nmostrado reutilización',TEAL_L,TEAL)]
    for x1,x2,head,body,fill,col in specs:
        box(d,(x1,295,x2,600),fill=fill,outline=col)
        txt(d,((x1+x2)/2,325),head,33,bold=True,color=col,anchor='mt')
        txt(d,((x1+x2)/2,463),body,27,anchor='mt')
    arrow(d,[(390,430),(510,430)],BLUE)
    txt(d,(453,354),'sale de\nla ventana',23,color=MUTED,anchor='mt')
    arrow(d,[(820,430),(975,430)],TEAL)
    txt(d,(897,354),'admitida',23,color=TEAL,anchor='mt')
    arrow(d,[(1285,390),(1420,390)],TEAL)
    txt(d,(1354,310),'nuevo\nacceso',23,color=TEAL,anchor='mt')
    arrow(d,[(1420,545),(1285,545)],ORANGE)
    txt(d,(1353,570),'baja si\nno hay sitio',23,color=ORANGE,anchor='mt')
    arrow(d,[(665,600),(665,675)],RED)
    box(d,(460,680,870,780),'Candidato rechazado\nsi no supera a la víctima',RED_L,RED,27)
    arrow(d,[(1130,600),(1130,675)],RED)
    box(d,(945,680,1340,780),'Desalojo de la víctima\nsi el candidato gana',RED_L,RED,27)
    box(d,(80,850,1730,989),fill='white')
    txt(d,(115,875),'Ejemplo propio',28,color=BLUE,bold=True)
    txt(d,(115,925),'frecuencia estimada: candidato = 8 · víctima = 2 → admitir candidato y desalojar víctima',28)
    save(im,'03-tinylfu.png')

def wal():
    im,d=canvas('WAL: persistir el registro antes de persistir la página','Un commit puede ser durable aunque sus páginas de datos sigan sucias en RAM.','Elaboración propia basada en Log Semantics · PDF 11–14 · impresas 89–92. Esquema no proporcional al tiempo.')
    xs=[340,750,1160,1570]
    heads=['Modificar','Forzar WAL','Confirmar','Flush de datos']
    for i,x in enumerate(xs):
        txt(d,(x,205),f'{i+1} · {heads[i]}',32,bold=True,anchor='mt')
    for y in [405,640,872]:arrow(d,[(190,y),(1710,y)],LINE,3,14)
    txt(d,(85,315),'RAM',29,color=BLUE,bold=True)
    txt(d,(85,550),'WAL\ndurable',29,color=TEAL,bold=True)
    txt(d,(85,785),'Páginas\nen disco',29,color=ORANGE,bold=True)
    box(d,(190,335,495,475),'Página sucia\n+ registro en buffer',BLUE_L,BLUE,28)
    box(d,(600,568,910,710),'Cambios y COMMIT\npersistidos en orden',TEAL_L,TEAL,27)
    box(d,(1005,335,1315,475),'Cliente recibe\ncommit exitoso',BLUE_L,BLUE,29)
    box(d,(1415,800,1725,942),'Nueva página\npersistida',ORANGE_L,ORANGE,29)
    arrow(d,[(495,405),(550,405),(550,640),(600,640)],TEAL)
    arrow(d,[(910,640),(955,640),(955,405),(1005,405)],TEAL)
    arrow(d,[(910,695),(950,695),(950,757),(1570,757),(1570,800)],ORANGE)
    txt(d,(1220,718),'WAL durable → ya se puede escribir la página',26,color=ORANGE,anchor='mt')
    box(d,(85,960,1320,1015),'Regla: flushedLSN ≥ pageLSN antes del flush de esa página.',TEAL_L,TEAL,28)
    txt(d,(985,497),'Este ejemplo usa un flush posterior al commit.',25,color=MUTED)
    txt(d,(985,536),'STEAL permite flush antes, con WAL durable.',25,color=MUTED)
    save(im,'04-wal-y-flush.png')

def aries():
    im,d=canvas('ARIES: reconstruir la historia y retirar lo incompleto','ST EAL / NO-FORCE exige poder rehacer cambios y deshacer transacciones sin commit.'.replace('ST EAL','STEAL'),'Elaboración propia basada en ARIES · PDF 14–15 · impresas 92–93. Ejemplo simplificado de dos transacciones.')
    boxes=[(85,235,585,495),(650,235,1150,495),(1215,235,1715,495)]
    desc=[('1 · Análisis','¿Quién seguía activo?\n¿Qué páginas estaban sucias?\nDetermina dónde iniciar redo.',BLUE_L,BLUE),('2 · Redo','Repite la historia necesaria.\nIncluye cambios de ganadoras\ny de perdedoras.',TEAL_L,TEAL),('3 · Undo','Recorre hacia atrás los cambios\nde transacciones perdedoras.\nRegistra la compensación: CLR.',ORANGE_L,ORANGE)]
    for bounds,(head,body,fill,col) in zip(boxes,desc):
        box(d,bounds,fill=fill,outline=col)
        txt(d,(bounds[0]+25,265),head,34,color=col,bold=True)
        txt(d,(bounds[0]+25,340),body,27)
    arrow(d,[(585,365),(650,365)],BLUE)
    arrow(d,[(1150,365),(1215,365)],TEAL)
    txt(d,(90,550),'Ejemplo: saldo inicial A = 100; saldo inicial B = 200',31,bold=True)
    rows=[('T1 · ganadora','A: 100 → 80 + COMMIT','Redo deja A = 80','No se deshace',TEAL_L,TEAL),('T2 · perdedora','B: 200 → 250 sin COMMIT','Redo puede dejar B = 250','Undo devuelve B = 200',ORANGE_L,ORANGE)]
    for i,(head,before,red,undo,fill,col) in enumerate(rows):
        y=630+i*145
        box(d,(85,y,390,y+112),head,fill,col,29,bold=True)
        box(d,(420,y,880,y+112),before,fill,col,28)
        arrow(d,[(880,y+56),(935,y+56)],col)
        box(d,(935,y,1285,y+112),red,fill,col,27)
        arrow(d,[(1285,y+56),(1340,y+56)],col)
        box(d,(1340,y,1720,y+112),undo,fill,col,27)
    txt(d,(430,598),'Antes del fallo',25,color=MUTED)
    txt(d,(945,598),'Después de redo',25,color=MUTED)
    txt(d,(1350,598),'Estado final',25,color=MUTED)
    box(d,(85,944,1720,1010),'CLR: registra un undo ya realizado; puede rehacerse tras otro fallo y no vuelve a deshacerse.',BLUE_L,BLUE,28)
    save(im,'05-aries.png')

if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    for fn in [cache,clock,tinylfu,wal,aries]:fn()
    print('Generados 01-cache-paginas.png a 05-aries.png')
