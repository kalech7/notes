#!/usr/bin/env python3
"""Regenera las ilustraciones didácticas 06–10. Requiere Pillow.

Uso: uv run --with pillow generar_concurrencia.py
Fuente: Database Internals, capítulo 5, PDF CamScanner 30/09/2026.
Diseños originales en español. No se usan recortes ni calcos del PDF.
06 adapta fig 5-4 (PDF 17 / p95);08 adapta fig 5-6 (PDF 23 / p101);
09 adapta fig 5-9 (PDF 28 / p106), con contraste propio de página insegura;
07 y10 son ejemplos propios de prosa PDF 19 / p97 y PDF 29–30 / p107–108.
"""
from pathlib import Path
import itertools
import math
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
W = 1800
BG = '#f4f7fb'
INK = '#19314b'
MUTED = '#56687c'
BLUE = '#2865b0'
TEAL = '#087f80'
ORANGE = '#ba650a'
RED = '#b6394b'
LIGHT_BLUE = '#e4effb'
LIGHT_TEAL = '#dff4ed'
LIGHT_RED = '#fbe6e9'
GRAY = '#d8e1ea'
FONT_DIR = Path('/System/Library/Fonts/Supplemental')

def font(size=29, bold=False):
    name = 'Arial Bold.ttf' if bold else 'Arial.ttf'
    path = FONT_DIR / name
    if not path.exists():
        candidates = ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf']
        path = next((Path(p) for p in candidates if Path(p).exists()), name)
    return ImageFont.truetype(str(path), size)

def wrapped(draw, text, width, f):
    lines=[]
    for paragraph in text.split('\n'):
        words=paragraph.split(); line=''
        for word in words:
            trial=(line+' '+word).strip()
            if line and draw.textlength(trial, font=f)>width:
                lines.append(line); line=word
            else: line=trial
        lines.append(line)
    return lines

def txt(draw, xy, text, size=29, color=INK, bold=False, width=None, spacing=10, center=False):
    f=font(size,bold); x,y=xy
    lines=wrapped(draw,text,width,f) if width else text.split('\n')
    for line in lines:
        xx=x-draw.textlength(line,font=f)/2 if center else x
        draw.text((xx,y),line,font=f,fill=color)
        y+=size+spacing
    return y

def box(draw, rect, fill='white', border=GRAY, radius=20, width=3):
    draw.rounded_rectangle(rect,radius=radius,fill=fill,outline=border,width=width)

def arrow(draw, a,b,color=BLUE,width=5,dash=False):
    x1,y1=a;x2,y2=b
    if dash:
        length=math.hypot(x2-x1,y2-y1)
        for dist in range(0,int(length),22):
            t1=dist/length;t2=min((dist+12)/length,1)
            draw.line((x1+(x2-x1)*t1,y1+(y2-y1)*t1,x1+(x2-x1)*t2,y1+(y2-y1)*t2),fill=color,width=width)
    else: draw.line((a,b),fill=color,width=width)
    angle=math.atan2(y2-y1,x2-x1)
    pts=[b,(x2-20*math.cos(angle-.5),y2-20*math.sin(angle-.5)),(x2-20*math.cos(angle+.5),y2-20*math.sin(angle+.5))]
    draw.polygon(pts,fill=color)

def base(height, title, subtitle, source):
    im=Image.new('RGB',(W,height),BG);d=ImageDraw.Draw(im)
    txt(d,(64,42),title,48,bold=True)
    txt(d,(64,112),subtitle,28,color=MUTED,width=W-128)
    d.line((64,height-92,W-64,height-92),fill=GRAY,width=2)
    txt(d,(64,height-70),source,23,color=MUTED,width=W-128)
    return im,d

def save(im,name): im.save(OUT/name,optimize=True)

def serializacion():
    im,d=base(1260,'Serializabilidad: equivalencia con un orden completo',
        'Tres transacciones pueden solaparse. Sus efectos deben equivaler a alguna ejecución una detrás de otra.',
        'Adaptación didáctica de figura 5-4 · PDF 17 · impresa 95. Ejemplos y aclaración propios.')
    box(d,(64,198,704,885));box(d,(744,198,1736,885))
    txt(d,(94,228),'Ejecución concurrente',35,bold=True)
    txt(d,(94,290),'El tiempo avanza →',25,color=MUTED)
    colors=[BLUE,TEAL,ORANGE]
    intervals=[(130,540),(280,610),(200,430)]
    for i,((a,b),c) in enumerate(zip(intervals,colors)):
        y=410+i*124
        txt(d,(94,y-65),f'T{i+1}',32,color=c,bold=True)
        box(d,(a,y,b,y+44),fill=c,border=c,radius=12)
        d.ellipse((a-7,y+14,a+7,y+28),fill='white');d.ellipse((b-21,y+14,b-7,y+28),fill='white')
    txt(d,(94,793),'Solapamiento ≠ garantía de equivalencia.',27,color=MUTED,width=570)
    txt(d,(778,228),'Los 6 órdenes seriales candidatos',35,bold=True)
    for i,order in enumerate(itertools.permutations([1,2,3])):
        y=317+i*84
        txt(d,(778,y+12),f'{i+1}',27,color=MUTED)
        for j,n in enumerate(order):
            x=841+j*280
            box(d,(x,y,x+225,y+58),fill=colors[n-1],border=colors[n-1],radius=12)
            txt(d,(x+112,y+11),f'T{n}',29,color='white',bold=True,center=True)
            if j<2: arrow(d,(x+234,y+29),(x+267,y+29),MUTED,3)
    box(d,(64,926,1736,1133),fill=LIGHT_BLUE,border='#bcd2ed')
    txt(d,(94,955),'La condición que importa',33,bold=True,color=BLUE)
    txt(d,(94,1013),'Los conflictos y los valores leídos deben admitir un mismo orden serial equivalente. No cualquier intercalado lo permite, ni los 6 candidatos son válidos para toda ejecución.',31,width=1600)
    save(im,'06-serializacion.png')

def write_skew():
    im,d=base(1390,'Write skew: decisiones válidas por separado, fallo conjunto',
        'Ejemplo propio de aislamiento por instantánea: dos médicos deciden dejar la guardia al mismo tiempo.',
        'Elaboración propia basada en prosa PDF 19 · impresa 97 (la figura 5-5 es la tabla de aislamiento).')
    box(d,(64,200,1736,356),fill=LIGHT_BLUE,border='#bcd2ed')
    txt(d,(94,226),'Estado inicial: Ana = disponible · Bruno = disponible',34,bold=True)
    txt(d,(94,287),'Regla del servicio: siempre debe quedar al menos 1 médico disponible.',30)
    for left,name,other,c in [(64,'Ana','Bruno',BLUE),(928,'Bruno','Ana',TEAL)]:
        right=left+808
        box(d,(left,397,right,979))
        txt(d,(left+32,425),f'Transacción de {name}',36,bold=True,color=c)
        steps=[('1 · Lee su instantánea','Ana = sí; Bruno = sí. La instantánea se mantiene estable.'),
               ('2 · Decide sobre su propia fila',f'{other} sigue disponible según esa lectura; {name} cambia su fila a «no».'),
               ('3 · Confirma (COMMIT)',f'Solo escribe la fila de {name}. No colisiona con la fila que escribe la otra transacción.')]
        for j,(head,body) in enumerate(steps):
            y=510+j*148
            txt(d,(left+32,y),head,30,bold=True,color=c)
            txt(d,(left+32,y+47),body,28,width=740)
    box(d,(64,1018,1736,1264),fill=LIGHT_RED,border='#e4acb7')
    txt(d,(94,1049),'Estado final: Ana = no · Bruno = no · disponibles = 0',35,bold=True,color=RED)
    txt(d,(94,1110),'Las escrituras afectan filas distintas: bajo aislamiento por instantánea ambas pueden confirmar. Pero comparten una condición leída, y juntas rompen la regla global.',30,width=1590)
    txt(d,(94,1200),'En un orden serial, el segundo médico vería al primero fuera de guardia y tendría que quedarse.',28,color=RED,width=1580)
    save(im,'07-write-skew.png')

def deadlock():
    im,d=base(1160,'Deadlock: cada transacción retiene lo que la otra necesita',
        'Un ciclo de espera impide avanzar a las dos. Los bloqueos transaccionales protegen objetos lógicos.',
        'Adaptación didáctica de figura 5-6 · PDF 23 · impresa 101. Objetos A y B: ejemplo propio.')
    for x,n,res,c in [(85,'T1','A',BLUE),(1085,'T2','B',TEAL)]:
        box(d,(x,235,x+630,570),border=c,fill='white')
        txt(d,(x+315,263),n,48,bold=True,color=c,center=True)
        box(d,(x+65,348,x+565,453),fill=LIGHT_BLUE if n=='T1' else LIGHT_TEAL,border=c)
        txt(d,(x+315,378),f'POSEE bloqueo de {res}',33,color=c,bold=True,center=True)
        txt(d,(x+315,492),f'ESPERA bloqueo de {"B" if res=="A" else "A"}',29,color=RED,bold=True,center=True)
    arrow(d,(721,342),(1076,342),RED,7,dash=True)
    txt(d,(899,280),'T1 espera a T2',29,color=RED,center=True)
    arrow(d,(1076,497),(721,497),RED,7,dash=True)
    txt(d,(899,530),'T2 espera a T1',29,color=RED,center=True)
    box(d,(64,629,1736,828),fill=LIGHT_RED,border='#e4acb7')
    txt(d,(94,662),'Grafo de espera: T1 → T2 → T1',36,bold=True,color=RED)
    txt(d,(94,724),'Una flecha sale de quien espera y apunta a quien posee el bloqueo requerido. El ciclo muestra que ninguna puede terminar y liberar su bloqueo.',30,width=1590)
    box(d,(64,869,1736,1038),fill=LIGHT_TEAL,border='#a9d8c9')
    txt(d,(94,899),'Romper el ciclo',34,bold=True,color=TEAL)
    txt(d,(94,955),'El gestor puede abortar una transacción, deshacer sus cambios y liberar sus bloqueos; la otra continúa. La abortada se puede reintentar.',29,width=1580)
    save(im,'08-deadlock.png')

def node(d,rect,label,held=True,small=False):
    color=BLUE if held else MUTED
    box(d,rect,fill=LIGHT_BLUE if held else '#edf1f5',border=color)
    x1,y1,x2,y2=rect
    txt(d,((x1+x2)/2,y1+13),label,25 if small else 29,bold=True,color=color,center=True)
    txt(d,((x1+x2)/2,y1+54),'latch retenido' if held else 'latch libre',22,color=color,center=True)

def crabbing():
    im,d=base(1740,'Latch crabbing: asegurar el hijo antes de soltar el padre',
        'Inserción en un B-tree: los latches protegen páginas y enlaces mientras cambia la estructura física.',
        'Adaptación de figura 5-9 · PDF 27–28 · impresas 105–106. Contraste seguro/inseguro: elaboración propia.')
    cards=[(64,'1 · Proteger la raíz','Raíz',True,'Hijo',False,'Se adquiere el latch de la raíz antes de elegir el siguiente nodo.'),
           (634,'2 · Asegurar el hijo','Raíz',True,'Hijo',True,'Durante el traspaso están retenidos ambos latches. Se evalúa si el hijo es seguro.'),
           (1204,'3 · Hijo seguro: soltar la raíz','Raíz',False,'Hijo',True,'Si el hijo no propagará un cambio hasta la raíz, se libera la raíz y se desciende.')]
    for x,head,parent,ph,child,ch,body in cards:
        box(d,(x,212,x+532,749))
        txt(d,(x+25,239),head,28,bold=True,width=485)
        node(d,(x+146,338,x+386,440),parent,ph)
        arrow(d,(x+266,449),(x+266,489),MUTED,4)
        node(d,(x+146,503,x+386,605),child,ch)
        txt(d,(x+25,626),body,27,width=480)
    for x,head,color,bg,full in [(64,'Hoja segura: queda espacio',TEAL,LIGHT_TEAL,False),(928,'Hoja llena: puede propagar',RED,LIGHT_RED,True)]:
        box(d,(x,790,x+808,1333),fill=bg,border=color)
        txt(d,(x+28,821),head,33,bold=True,color=color)
        node(d,(x+270,888,x+540,990),'Padre',full)
        arrow(d,(x+405,998),(x+405,1034),color,4)
        node(d,(x+270,1048,x+540,1150),'Hoja',True)
        if full:
            arrow(d,(x+566,1104),(x+566,960),RED,4,dash=True)
            txt(d,(x+601,988),'split\npuede\nsubir',24,color=RED)
            text='Caso conservador: retener el padre si el split puede afectarlo. Retener más ancestros cuando también puedan dividirse.'
        else:
            txt(d,(x+37,935),'padre\nliberado',24,color=TEAL)
            text='La inserción cabe en la hoja: no divide el nodo ni cambia el padre. El latch del padre puede liberarse tras asegurar la hoja.'
        txt(d,(x+28,1190),text,28,width=750)
    box(d,(64,1374,1736,1608),fill='white')
    txt(d,(94,1404),'«Seguro» depende de la operación',33,bold=True)
    txt(d,(94,1462),'Lectura: hijo localizado y protegido. Inserción: no causará split que afecte al ancestro. Borrado: no causará fusión o rebalanceo que lo afecte. Soltar pronto reduce contención.',29,width=1580)
    txt(d,(94,1550),'Los latches tienen vida corta; no sustituyen el aislamiento ni los bloqueos de una transacción.',27,color=MUTED,width=1580)
    save(im,'09-latches-crabbing.png')

def blink():
    im,d=base(1370,'B-link tree: encontrar una clave durante un half-split',
        'El hijo ya se dividió y publicó su enlace lateral. El padre aún conserva la ruta anterior.',
        'Elaboración propia basada en PDF 29–30 · impresas 107–108. Convención: high key inclusiva, intervalos (abiertos,cerrados].')
    box(d,(64,207,1736,817))
    box(d,(460,248,1340,408),fill=LIGHT_BLUE,border=BLUE)
    txt(d,(900,278),'Padre: puntero antiguo para el rango (0,100]',35,bold=True,color=BLUE,center=True)
    txt(d,(900,343),'Todavía no tiene un puntero directo a la hoja nueva.',28,center=True)
    arrow(d,(683,420),(471,502),BLUE,6)
    txt(d,(940,442),'1 · Búsqueda de 75',27,color=BLUE,center=True)
    for rect,head,body,high,c in [((154,524,784,740),'Hoja izquierda original','Claves: 20 · 40','high key = 40',BLUE),((1038,524,1668,740),'Hoja derecha nueva','Claves: 60 · 75 · 90','high key = 100',TEAL)]:
        box(d,rect,fill=LIGHT_BLUE if c==BLUE else LIGHT_TEAL,border=c)
        x1,y1,x2,y2=rect;cx=(x1+x2)/2
        txt(d,(cx,y1+28),head,31,bold=True,color=c,center=True)
        txt(d,(cx,y1+85),body,32,bold=True,center=True)
        txt(d,(cx,y1+143),high,29,color=c,center=True)
    arrow(d,(796,636),(1020,636),TEAL,6)
    txt(d,(900,553),'2 · 75 > 40',27,bold=True,color=TEAL,center=True)
    txt(d,(900,672),'enlace lateral\na la derecha',25,color=TEAL,center=True)
    txt(d,(471,763),'Rango actual: (0,40]',25,color=BLUE,center=True)
    txt(d,(1353,763),'Rango actual: (40,100]',25,color=TEAL,center=True)
    box(d,(64,859,1736,1104),fill=LIGHT_TEAL,border='#a9d8c9')
    txt(d,(94,890),'3 · 75 pertenece al rango derecho y está en esa hoja',35,bold=True,color=TEAL)
    txt(d,(94,955),'La high key avisa que la ruta antigua quedó corta. El enlace lateral hace accesible el nodo nuevo aunque el padre todavía no lo referencie. Después, el padre incorporará el nuevo separador.',30,width=1575)
    box(d,(64,1145,1736,1237),fill='white')
    txt(d,(94,1173),'Los latches coordinan la publicación de límites y enlaces: un lector no debe ver un split a medio escribir.',27,color=MUTED,width=1590)
    save(im,'10-blink-split.png')

if __name__=='__main__':
    OUT.mkdir(parents=True,exist_ok=True)
    for make in [serializacion,write_skew,deadlock,crabbing,blink]:
        make()
    print('Generadas 06-serializacion.png a 10-blink-split.png')
