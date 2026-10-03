"""Esquemas conceptuales propios. Regenerar: uv run --with pillow python generar_diagramas.py."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).resolve().parent
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
INK = '#18334a'
COLORS = {'blue':('#e6f1ff','#2463a5'), 'green':('#e2f4ec','#247653'),
          'amber':('#fff0d2','#9c6500'), 'red':('#ffe9e8','#b23c3c'),
          'gray':('#edf1f5','#516777')}

def font(n=29,bold=False): return ImageFont.truetype(BOLD if bold else FONT,n)
def start(title,subtitle):
    global im,d
    im=Image.new('RGB',(1600,1000),'#fafcfe'); d=ImageDraw.Draw(im)
    d.text((65,40),title,fill=INK,font=font(44,True))
    d.text((65,104),subtitle,fill='#516777',font=font(27))
def wrapped(text,width,f):
    lines=[]
    for para in text.split('\n'):
        line=''
        for word in para.split():
            trial=(line+' '+word).strip()
            if d.textbbox((0,0),trial,font=f)[2]>width and line: lines.append(line);line=word
            else: line=trial
        lines.append(line)
    return lines
def box(x,y,w,h,title,body='',color='blue'):
    bg,fg=COLORS[color];d.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=bg,outline=fg,width=3)
    for size in range(29,20,-1):
        rows=sum(len(wrapped(t,w-36,font(size,b))) for t,b in [(title,True),(body,False)] if t)
        if 28+rows*(size+5)+(8 if body else 0)<=h:break
    else: raise ValueError('Texto fuera de caja: '+title)
    yy=y+14
    for text,bold in [(title,True),(body,False)]:
        if not text: continue
        f=font(size,bold)
        for line in wrapped(text,w-36,f):
            d.text((x+18,yy),line,fill=INK,font=f);yy+=size+5
        yy+=8
def arrow(a,b,color='#516777'):
    d.line([a,b],fill=color,width=4);ang=math.atan2(b[1]-a[1],b[0]-a[0])
    pts=[b,(b[0]-16*math.cos(ang-.5),b[1]-16*math.sin(ang-.5)),(b[0]-16*math.cos(ang+.5),b[1]-16*math.sin(ang+.5))]
    d.polygon(pts,fill=color)
def label(x,y,t):d.text((x,y),t,fill='#516777',font=font(26))
def save(name):
    d.line((65,924,1535,924),fill='#d4dde5',width=2)
    d.text((65,945),'S14 · Esquema didáctico propio · Cajas: funciones o datos; flechas: flujo',fill='#516777',font=font(23))
    im.save(OUT/name)

start('Tres formas de coordinar agentes','La topología cambia quién recibe el trabajo y quién conserva el control.')
for x,title in [(65,'Supervisor'),(575,'Traspaso'),(1085,'Paralelismo')]:label(x,177,title)
box(65,230,445,130,'Supervisor','Elige, entrega contexto y consolida','amber')
box(65,450,205,150,'Datos','Devuelve evidencia')
box(305,450,205,150,'Análisis','Devuelve conclusiones')
arrow((165,360),(165,450));arrow((405,360),(405,450))
arrow((165,600),(165,685));arrow((405,600),(405,685))
box(65,690,445,120,'Control central','La respuesta vuelve al supervisor','green')
box(575,230,445,120,'Agente A','Produce un resultado parcial')
arrow((798,350),(798,435))
box(575,440,445,165,'Contrato','Resultado + objetivo siguiente + restricciones','amber')
arrow((798,605),(798,690))
box(575,695,445,120,'Agente B','Continúa con el control','green')
box(1085,230,445,120,'Repartir','Ramas independientes','amber')
box(1085,450,205,150,'Rama A','Produce un resultado')
box(1325,450,205,150,'Rama B','Produce un resultado')
arrow((1185,350),(1185,450));arrow((1425,350),(1425,450))
arrow((1185,600),(1185,685));arrow((1425,600),(1425,685))
box(1085,690,445,155,'Consolidar','Presupuesto compartido e identidad por resultado','green')
save('01-topologias.png')

start('El agente como grafo con una salida explícita','El programa revisa límites antes de autorizar otra llamada.')
box(65,220,300,135,'Control previo','Pasos, gasto y permisos','amber')
box(475,220,300,135,'Modelo','Propone acción o final')
box(885,220,300,135,'Router','Decide el siguiente nodo','amber')
arrow((365,288),(475,288));arrow((775,288),(885,288))
box(885,490,300,140,'Herramienta','El programa la ejecuta')
arrow((1035,355),(1035,490));label(1050,403,'acción válida')
d.line([(885,560),(625,560),(625,410),(215,410),(215,355)],fill='#516777',width=4)
arrow((215,410),(215,355));label(405,586,'resultado al estado y nueva revisión')
box(1250,490,285,140,'Respuesta','Completa o parcial','green')
arrow((1185,288),(1392,490));label(1240,355,'final')
box(65,715,670,145,'Salida por límite','Explica el trabajo pendiente y registra el motivo','green')
arrow((215,355),(65,715))
label(830,754,'recursion_limit: otra capa de protección')
label(830,799,'Si se alcanza, hay una excepción.')
save('02-bucle-con-salida.png')

start('Un reductor define cómo juntar actualizaciones','Actualizar una clave y concatenar una lista son operaciones diferentes.')
box(65,205,700,110,'Sin reductor','resultado: str','gray')
box(65,400,320,125,'Nodo A','resultado = "A"')
box(445,400,320,125,'Nodo B','resultado = "B"')
arrow((225,525),(415,650));arrow((605,525),(415,650))
box(65,655,700,165,'Conflicto en el mismo superstep','Dos escrituras para una clave: InvalidUpdateError','red')
box(835,205,700,110,'Con reductor','resultados: lista + operator.add','gray')
box(835,400,320,125,'Nodo A','Añade [{id: "A"}]')
box(1215,400,320,125,'Nodo B','Añade [{id: "B"}]')
arrow((995,525),(1185,650));arrow((1375,525),(1185,650))
box(835,655,700,165,'Se conservan ambos resultados','La identidad permite ordenarlos y revisar contradicciones','green')
save('03-reductores.png')

start('Confirmar una acción exige detener su ejecución','La aprobación se aplica a una propuesta concreta y a sus argumentos.')
box(65,235,350,155,'Propuesta','Acción, destino, contenido y riesgo')
box(625,235,350,155,'interrupt','Pausa antes del efecto','amber')
box(1185,235,350,155,'Checkpoint','Estado guardado + thread_id','gray')
arrow((415,312),(625,312));arrow((975,312),(1185,312))
box(625,505,350,155,'Decisión humana','Command(resume=...)','amber')
arrow((800,390),(800,505))
box(65,745,550,120,'Rechazo','La función sensible no se ejecuta','red')
box(985,745,550,120,'Aprobación','Ejecuta la propuesta aprobada','green')
arrow((720,660),(340,745));arrow((880,660),(1260,745))
label(70,550,'El nodo puede reiniciarse al reanudar.')
label(70,597,'Los efectos quedan después de aprobar.')
save('04-pausa-y-aprobacion.png')

start('Tres frenos observan tres problemas diferentes','Una sola regla deja fuera otros modos de falla.')
box(65,230,450,295,'Pasos','Cuenta iteraciones o llamadas.\nAcota una tarea que no termina.\nNo mide el precio de cada llamada.','blue')
box(575,230,450,295,'Presupuesto','Suma gasto o consumo.\nAcota operaciones costosas.\nNo detecta progreso semántico.','amber')
box(1085,230,450,295,'Repetición','Cuenta herramienta + entrada.\nDetecta duplicados exactos.\nNo identifica paráfrasis.','red')
arrow((290,525),(800,685));arrow((800,525),(800,685));arrow((1310,525),(800,685))
box(300,690,1000,165,'Una autorización antes de actuar','Si falla cualquier freno: detener, explicar y guardar la traza.','green')
save('05-tres-frenos.png')

start('Reenviar el historial repite el trabajo de entrada','S es el contexto inicial. A, B y C son pares nuevos de mensajes.')
rows=[('Llamada 1',['S']),('Llamada 2',['S','A']),('Llamada 3',['S','A','B']),('Llamada 4',['S','A','B','C'])]
for i,(title,blocks) in enumerate(rows):
 y=230+i*145;label(65,y+32,title)
 for j,b in enumerate(blocks):box(290+j*230,y,200,100,b,'inicial' if i==0 else ('nuevo' if j==len(blocks)-1 and j>0 else 'reenviado'),'blue' if b=='S' else 'amber')
box(290,825,1100,70,'Cada mensaje previo vuelve a entrar en llamadas posteriores.','','green')
save('06-historial-reenviado.png')

start('Una herramienta ausente limita el daño posible','El ticket es un dato no confiable. No concede permisos al agente.')
box(405,195,790,110,'Ticket malicioso','Pretende convertir un resumen en envío de información','red')
box(65,415,680,160,'A: catálogo permisivo','leer_tickets + enviar_email','amber')
box(855,415,680,160,'B: catálogo mínimo','leer_tickets','green')
arrow((630,305),(405,415));arrow((970,305),(1195,415))
box(65,680,680,165,'Simulador original A','Pide envío. La función registra ENVIADO de forma local.','red')
box(855,680,680,165,'Simulador original B','No pide envío y devuelve un resumen. No prueba resistencia general.','green')
arrow((405,575),(405,680));arrow((1195,575),(1195,680))
save('07-inyeccion-y-capacidades.png')

start('LangChain, LangGraph y LangSmith en la misma tarea','Una pregunta recorre funciones, estado y observaciones.')
box(65,235,460,430,'LangChain','Interfaz del modelo.\nCatálogo de herramientas.\nEsquemas de salida.\nRecuperador como herramienta.','blue')
box(570,235,460,430,'LangGraph','Nodos y aristas.\nEstado y reductores.\nPausa y reanudación.\ncreate_agent utiliza este motor.','amber')
box(1075,235,460,430,'LangSmith','Registra la ejecución.\nRelaciona sus pasos.\nDatasets y evaluación.\nTambién puedes guardar JSON local.','green')
arrow((525,450),(570,450));arrow((1030,450),(1075,450))
box(220,770,1160,110,'Responsabilidad del diseño','Contratos, permisos, presupuesto y verificación de respuestas.','gray')
save('08-tres-bibliotecas.png')

start('La traza permite explicar una acción','Registrar lo ocurrido hace posible revisar límites y resultados.')
box(65,230,450,250,'Petición','Pregunta original.\nIdentidad de la tarea.\nLímites y herramientas permitidas.','blue')
box(575,230,450,250,'Decisión y ejecución','Propuesta y argumentos.\nAutorización o rechazo.\nResultado y costo.','amber')
box(1085,230,450,250,'Cierre','Respuesta completa o parcial.\nMotivo de parada.\nReferencias a la evidencia.','green')
arrow((515,355),(575,355));arrow((1025,355),(1085,355))
box(170,660,1260,180,'Evaluación posterior','¿Respondió bien? ¿Respetó los límites? ¿Hubo una acción rechazada?\nUn registro completo ayuda a comprobarlo; no demuestra por sí solo corrección.','gray')
save('09-traza-y-evaluacion.png')
print('9 PNG generados')
