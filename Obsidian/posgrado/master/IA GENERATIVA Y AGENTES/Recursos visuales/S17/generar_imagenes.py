"""Esquemas didácticos S17/S18. Ejecutar con Python y Pillow.
No representa mediciones propias de modelos ni precios actuales.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

HERE = Path(__file__).resolve().parent
OUT18 = HERE.parent / 'S18'
OUT18.mkdir(exist_ok=True)
W,H = 1800,1120
INK='#172a44'; MUTED='#50647e'; BG='#f2f6fb'
BLUE='#2862be'; TEAL='#147d75'; ORANGE='#ab5b18'; RED='#ad3345'
FONTS = Path('/System/Library/Fonts/Supplemental')
def font(size=30,bold=False):
    candidates=[str(FONTS/('Arial Bold.ttf' if bold else 'Arial.ttf')),
                'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf',
                'C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf']
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate,size)
        except OSError:
            continue
    raise RuntimeError('Instala Arial o DejaVu Sans para regenerar las imágenes con texto legible.')
def canvas(title,subtitle):
    im=Image.new('RGB',(W,H),BG); d=ImageDraw.Draw(im)
    d.text((75,55),title,font=font(52,True),fill=INK)
    d.text((75,125),subtitle,font=font(29),fill=MUTED)
    return im,d
def wrap(d,text,width,size=29,bold=False):
    rows=[]
    for paragraph in text.split('\n'):
        line=''
        for word in paragraph.split():
            trial=f'{line} {word}'.strip()
            if d.textlength(trial,font=font(size,bold))>width and line:
                rows.append(line);line=word
            else: line=trial
        rows.append(line)
    return rows
def text(d,xy,s,width,size=29,color=INK,bold=False):
    x,y=xy
    for row in wrap(d,s,width,size,bold):
        d.text((x,y),row,font=font(size,bold),fill=color);y+=size+11
    return y
def card(d,box,title,body,color=BLUE,size=29):
    x,y,x2,y2=box
    d.rounded_rectangle(box,radius=20,fill='white',outline='#cfdaea',width=2)
    d.rounded_rectangle((x,y,x+9,y2),radius=4,fill=color)
    end=text(d,(x+30,y+18),title,x2-x-60,32,color,True)
    body_y=end+3
    while len(wrap(d,body,x2-x-60,size))*(size+11)>y2-body_y-10 and size>20:
        size-=1
    text(d,(x+30,body_y),body,x2-x-60,size)
def arrow(d,a,b,color=MUTED):
    d.line([a,b],fill=color,width=5)
    angle=math.atan2(b[1]-a[1],b[0]-a[0]);r=15
    pts=[b,(b[0]-r*math.cos(angle-.5),b[1]-r*math.sin(angle-.5)),(b[0]-r*math.cos(angle+.5),b[1]-r*math.sin(angle+.5))]
    d.polygon(pts,fill=color)
def footer(d,s):
    text(d,(75,1035),s,1650,24,MUTED)

def traza():
    im,d=canvas('Una traza explica una ejecución completa','Ejemplo secuencial del material S17 · cada span registra un paso')
    card(d,(75,205,630,400),'Traza T-001 · raíz','Inicio y fin de la ejecución\nVersión del prompt: v1\nResultado y errores',BLUE)
    labels=['Paso 1 · 45 ms','Paso 2 · 900 ms','Paso 3 · 120 ms','Paso 4 · 1 100 ms']
    colors=[TEAL,BLUE,ORANGE,BLUE]
    d.line((130,410,130,840),fill=MUTED,width=4)
    for i,(lab,c) in enumerate(zip(labels,colors)):
        y=435+105*i
        arrow(d,(130,y+28),(180,y+28))
        d.rounded_rectangle((190,y,620,y+76),radius=13,fill='white',outline=c,width=3)
        d.text((215,y+20),lab,font=font(31,True),fill=c)
    text(d,(745,210),'Línea de tiempo',900,35,INK,True)
    x0,x1=755,1685; total=2165
    d.line((x0,320,x1,320),fill=MUTED,width=3)
    for val in [0,500,1000,1500,2165]:
        x=x0+(x1-x0)*val/total
        d.line((x,307,x,335),fill=MUTED,width=2)
        d.text((x-25,345),str(val),font=font(24),fill=MUTED)
    start=0
    for i,(ms,c) in enumerate(zip([45,900,120,1100],colors)):
        y=435+105*i
        x=x0+(x1-x0)*start/total;end=x0+(x1-x0)*(start+ms)/total
        d.rounded_rectangle((x,y+10,max(x+7,end),y+60),radius=5,fill=c)
        start+=ms
    card(d,(740,880,1725,990),'Duración raíz = 2 165 ms','45 + 900 + 120 + 1 100. Con pasos solapados, la suma cambia.',TEAL,26)
    text(d,(75,875),'El costo requiere tokens, modelo y tarifas.\nLos milisegundos no bastan para calcularlo.',590,27,ORANGE)
    footer(d,'Recreación didáctica · PDF S17 pp. 5–7. Los nombres de pasos son genéricos; no son mediciones nuevas.')
    im.save(HERE/'01-traza-spans.png')

def versiones():
    im,d=canvas('Guardar versiones y elegir la activa son dos cosas','El registro conserva el texto; la etiqueta production decide qué versión se usa')
    card(d,(80,235,565,480),'v1 · conservada','Texto del prompt\nQué cambió y por qué\nIdentificador de versión',BLUE)
    card(d,(80,530,565,775),'v2 · candidata','Nuevo texto del prompt\nNuevo changelog\nEvaluación por versión',TEAL)
    card(d,(690,370,1110,680),'Evaluación común','Mismas preguntas\nCalidad y formato\nCosto y latencia\nCriterio de aceptación',ORANGE)
    arrow(d,(565,355),(685,455),BLUE);arrow(d,(565,650),(685,565),TEAL)
    card(d,(1240,235,1720,480),'Antes: production → v1','La aplicación obtiene v1.\nLas trazas registran v1.',BLUE)
    card(d,(1240,530,1720,775),'Después: production → v2','Se promueve si pasa la evaluación.\nLas trazas registran v2.',TEAL)
    arrow(d,(1110,545),(1235,650),TEAL)
    arrow(d,(1485,490),(1485,520),TEAL)
    card(d,(690,850,1720,990),'Rollback: production vuelve a v1','La v2 sigue guardada. Cachés o despliegues deben actualizar la versión que obtienen.',RED,26)
    text(d,(80,870),'Las versiones no se sobrescriben.\nLa etiqueta puede moverse.',525,30,INK,True)
    footer(d,'Esquema propio a partir de S17 pp. 20 y 30, y S18 pp. 28–29. Una etiqueta no demuestra una mejora.')
    im.save(HERE/'02-versionado-prompts.png')

def bordes():
    im,d=canvas('Los controles actúan en los bordes del sistema','El prompt orienta al modelo; el código decide si el flujo puede continuar')
    steps=[('1 · Entrada','Longitud y alcance\nPatrones de riesgo\nDatos personales',BLUE),('2 · Contexto','Documentos externos\nInstrucciones ocultas\nFuentes y permisos',TEAL),('Modelo','Genera una propuesta\nPuede equivocarse\nNo concede permisos',ORANGE),('3 · Salida','Esquema y contenido\nDatos y secretos\nRespuesta permitida',BLUE)]
    for i,(title,body,c) in enumerate(steps):
        x=75+i*440
        card(d,(x,250,x+365,570),title,body,c,28)
        if i<3:arrow(d,(x+370,410),(x+435,410))
    card(d,(575,640,1130,840),'Herramientas: otro borde','Autorizar la acción y sus argumentos antes de ejecutar. Leer datos no autoriza modificarlos.',RED,29)
    arrow(d,(1138,577),(855,635),ORANGE)
    card(d,(75,900,1725,995),'Trazas: proteger también lo que se registra','Sanitizar antes de guardar o exportar, incluso las entradas bloqueadas y los errores.',TEAL,28)
    text(d,(75,655),'Cada control puede:\n• dejar pasar\n• corregir\n• bloquear',435,32,INK)
    text(d,(1200,655),'Medir ambos errores:\nfalso positivo = frena algo válido\nfalso negativo = deja pasar un riesgo',500,29,INK)
    footer(d,'Elaboración didáctica · S18 pp. 2–5 y 15–17. Ningún detector de patrones cubre toda inyección.')
    im.save(OUT18/'01-bordes-guardrails.png')

def costos():
    im,d=canvas('Reducir costo y reducir espera requieren medidas distintas','Ejercicio S18 · 2 000 tokens de prefijo + 100 de pregunta + 300 de respuesta')
    card(d,(75,205,1015,360),'Base: 30 000 llamadas al mes','Tarifas del PDF: grande 5/25 y pequeño 1/5 USD por millón de tokens de entrada/salida.',BLUE,27)
    rows=[('Todo al grande','$0,018','$540,00','Referencia'),('Todo al pequeño','$0,0036','$108,00','80 % menos'),('60 % al pequeño','$0,00936','$280,80','48 % menos'),('Prefijo a la mitad · grande','$0,013','$390,00','27,78 % menos')]
    headers=['Estrategia','Por llamada','Por mes','Frente a base']
    xs=[100,510,690,865]
    for x,label in zip(xs,headers):d.text((x,395),label,font=font(25,True),fill=MUTED)
    for i,row in enumerate(rows):
        y=445+i*94
        d.rounded_rectangle((75,y,1015,y+78),radius=13,fill='white')
        for j,(x,label) in enumerate(zip(xs,row)):
            text(d,(x,y+17),label,[390,170,170,145][j],25,TEAL if i>0 and j>0 else INK,j>0)
    card(d,(1080,205,1725,460),'TTFT: primer token','Ejemplo propio, no medido:\nprimer token emitido a los 0,4 s;\nrespuesta completa a los 3,0 s.\nEse token puede no mostrarse.',TEAL,29)
    card(d,(1080,510,1725,795),'Tiempo total: respuesta terminada','Streaming permite empezar a mostrarla antes. Por sí solo no cambia los tokens facturados.',ORANGE,29)
    card(d,(75,870,1725,995),'Antes de decidir: verificar calidad, reintentos y caché','El router puede fallar. La caché tiene condiciones y tarifas propias. Estas cuentas no los incluyen.',RED,28)
    footer(d,'Cuentas del escenario S18 pp. 23–26 · tarifas históricas del material, sin impuestos ni infraestructura.')
    im.save(OUT18/'02-presupuesto-latencia.png')

if __name__=='__main__':
    traza();versiones();bordes();costos()
    print('4 imágenes creadas en',HERE,'y',OUT18)
