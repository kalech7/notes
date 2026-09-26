"""Diagramas originales para la guía; sin dependencias. Ejecutar desde cualquier ruta."""
from pathlib import Path
from html import escape

OUT = Path(__file__).resolve().parent
NAVY, TEAL, BLUE, GOLD, RED = '#16324f', '#007f83', '#2463a5', '#ae6a06', '#b84640'
S = []

def text(x,y,value,size=22,color=NAVY,weight=400,anchor='start'):
    S.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>')

def line(x1,y1,x2,y2,color=TEAL,width=3,arrow=False,dash=False):
    S.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(' marker-end="url(#arrow)"' if arrow else '')+(' stroke-dasharray="8 7"' if dash else '')+'/>')

def rect(x,y,w,h,fill='#ffffff',stroke='#ccd8df',radius=18):
    S.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')

def box(x,y,w,h,title,body=(),color=TEAL):
    rect(x,y,w,h,stroke=color)
    text(x+20,y+34,title,23,color,700)
    for i,t in enumerate(body):text(x+20,y+66+28*i,t,19)

def dot(x,y,label,color=TEAL,dx=15,dy=-10):
    S.append(f'<circle cx="{x}" cy="{y}" r="8" fill="{color}" stroke="white" stroke-width="2"/>')
    text(x+dx,y+dy,label,20,color,600)

def start(title,subtitle):
    S.clear()
    S.append('<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" viewBox="0 0 1200 760" role="img">')
    S.append(f'<title>{escape(title)}</title><desc>{escape(subtitle)}</desc>')
    S.append('<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#007f83" stroke-width="1.5"/></marker></defs>')
    S.append('<g font-family="Arial, Helvetica, sans-serif"><rect width="1200" height="760" fill="#f6f8f8"/>')
    text(48,57,title,32,NAVY,700)
    text(48,92,subtitle,19)
    line(48,117,1152,117,'#ccd8df',1)

def end(name,foot):
    line(48,700,1152,700,'#ccd8df',1)
    text(48,732,foot,17)
    S.append('</g></svg>')
    (OUT/name).write_text('\n'.join(S),encoding='utf-8')

start('La arquitectura une contexto y decisiones','Cuatro dimensiones relacionadas; el estilo se elige después de entender el problema.')
box(360,150,480,100,'CONTEXTO',('Negocio · presupuesto · equipo · restricciones',),NAVY)
box(70,310,465,135,'CARACTERÍSTICAS',('Qué capacidades hacen viable el sistema', 'Ejemplo: soportar el pico del almuerzo'),TEAL)
box(665,310,465,135,'COMPONENTES LÓGICOS',('Qué responsabilidades tiene el sistema','Ejemplo: pedidos, pagos y entregas'),BLUE)
line(480,250,300,310,arrow=True);line(720,250,900,310,arrow=True)
box(70,520,465,125,'ESTILO',('Organiza las piezas y sus relaciones','Ejemplo: monolito modular'),BLUE)
box(665,520,465,125,'DECISIONES',('Reglas, alternativas y razones','Ejemplo: cada módulo posee sus datos'),TEAL)
line(300,445,300,520,arrow=True);line(900,445,900,520,arrow=True)
line(535,580,665,580,arrow=True);line(650,373,550,373,arrow=True)
end('01-arquitectura-contexto.svg','Elaboración propia. Las flechas expresan influencia; el proceso real es iterativo.')

start('Compartir trabajo no es difundir un evento','Ejemplo conceptual: un mensaje de pedido y consumidores con responsabilidades distintas.')
text(65,158,'A. UNA COLA, DOS TRABAJADORES',22,NAVY,700)
box(70,205,210,90,'Productor',('Pedido 101',))
box(420,205,265,90,'Cola de trabajo',('101 · 102 · 103',))
box(905,170,230,82,'Trabajador A',('Recibe 101',),BLUE)
box(905,290,230,82,'Trabajador B',('Recibe 102',),BLUE)
line(280,250,420,250,arrow=True);line(685,250,905,212,arrow=True);line(685,250,905,332,arrow=True)
text(72,359,'Reparten las entregas. Los reintentos pueden repetir un procesamiento.',19)
line(48,395,1152,395,'#ccd8df',1)
text(65,435,'B. PUBLICACIÓN Y SUSCRIPCIÓN, UNA COLA POR SUSCRIPTOR',22,NAVY,700)
box(70,505,210,90,'Productor',('PedidoCreado',))
box(385,505,230,90,'Distribuidor',('Exchange / broker',))
box(730,463,195,80,'Cola cocina',('Copia del evento',),BLUE)
box(730,580,195,80,'Cola análisis',('Copia del evento',),GOLD)
text(970,504,'Cocina',21,BLUE,700);text(970,623,'Analítica',21,GOLD,700)
line(280,550,385,550,arrow=True);line(615,550,730,503,arrow=True);line(615,550,730,620,arrow=True)
line(925,503,959,503,arrow=True);line(925,620,959,620,arrow=True)
end('02-colas-y-publicacion.svg','Pub/sub puede usar colas por suscriptor: permisos, persistencia y reentrega requieren configuración.')

start('Abstracción e inestabilidad: leer la secuencia principal','Cada punto es un módulo hipotético; la distancia es una señal para investigar, no una nota de calidad.')
x0,y0,L=120,625,450
rect(120,175,450,450,'#ffffff',radius=0)
S.append('<path d="M120,625 L120,490 L255,625 Z" fill="#f9ded9"/>')
S.append('<path d="M570,175 L435,175 L570,310 Z" fill="#fff0d6"/>')
for v in [0,.2,.4,.6,.8,1]:
    xx=x0+v*L;yy=y0-v*L
    line(xx,175,xx,625,'#dce4e8',1);line(120,yy,570,yy,'#dce4e8',1)
    text(xx,653,f'{v:g}',17,anchor='middle');text(99,yy+6,f'{v:g}',17,anchor='end')
line(120,625,590,625,NAVY,2);line(120,625,120,157,NAVY,2)
line(120,175,570,625,TEAL,4)
text(70,153,'A',23,NAVY,700);text(602,645,'I',23,NAVY,700)
text(280,685,'I = Ce / (Ca + Ce)',20)
dot(210,580,'P',RED);dot(210,265,'B',TEAL);dot(502.5,220,'U',GOLD)
box(655,175,485,117,'P · rígido y concreto',('I = 0,20; A = 0,10; D = 0,70','Zona de dolor: investigar rigidez'),RED)
box(655,322,485,117,'B · sobre la secuencia',('I = 0,20; A = 0,80; D = 0,00','A + I = 1; no demuestra buen dominio'),TEAL)
box(655,469,485,117,'U · abstracto y poco dependido',('I = 0,85; A = 0,90; D = 0,75','Zona de inutilidad: revisar abstracciones'),GOLD)
text(655,630,'D = |A + I − 1|  (distancia normalizada)',22,NAVY,700)
text(655,663,'Distancia perpendicular geométrica = D / √2',19)
end('04-secuencia-principal.svg','A = Na / (Na + Nc). Se cuentan tipos abstractos y concretos; no se cuentan líneas de código.')

start('LCOM: seguir qué métodos comparten estado','Clase hipotética con cuatro métodos, dos campos y seis pares distintos de métodos.')
rect(60,155,550,430,stroke=BLUE)
text(85,196,'Una clase, dos grupos de estado',24,BLUE,700)
for y,name in [(255,'m1'),(325,'m2'),(445,'m3'),(515,'m4')]:box(92,y-32,125,58,name,color=BLUE)
box(425,260,130,60,'a',color=TEAL);box(425,450,130,60,'b',color=TEAL)
line(217,252,425,290,arrow=True);line(217,322,425,290,arrow=True)
line(217,442,425,480,arrow=True);line(217,512,425,480,arrow=True)
box(655,155,485,126,'Q = 2 pares con estado compartido',('(m1, m2) comparten a','(m3, m4) comparten b'),TEAL)
box(655,314,485,126,'P = 4 pares sin estado compartido',('(m1, m3), (m1, m4),','(m2, m3), (m2, m4)'),RED)
box(655,473,485,113,'LCOM1 = max(P − Q, 0)',('max(4 − 2, 0) = 2',),NAVY)
text(80,635,'Separar puede ayudar si también hay dos responsabilidades distintas.',23,NAVY,700)
text(80,673,'Los dos grupos conexos coinciden aquí con 2, pero LCOM1 no cuenta grupos.',20)
end('05-lcom.svg','Ejemplo propio. No confundir LCOM1 con otras variantes; compartir campos no prueba cohesión semántica.')

start('Escalabilidad y elasticidad responden preguntas diferentes','Datos sintéticos para aprender a leer capacidad y demanda; no son mediciones de un sistema real.')
text(65,166,'ESCALABILIDAD',24,BLUE,700);text(650,166,'ELASTICIDAD',24,TEAL,700)
text(65,199,'¿Cuánto trabajo admito al añadir recursos?',19)
text(650,199,'¿Cómo adapto los recursos al cambiar la carga?',19)
line(100,565,545,565,NAVY,2);line(100,565,100,250,NAVY,2)
line(670,565,1118,565,NAVY,2);line(670,565,670,250,NAVY,2)
for i,(n,cap) in enumerate([(1,100),(2,180),(4,300)]):
    x=165+i*155;h=cap*.9
    rect(x-36,565-h,72,h,'#d4e8f5',BLUE,5)
    text(x,547-h,str(cap),20,BLUE,700,'middle');text(x,598,str(n),20,anchor='middle')
text(115,237,'Capacidad (solicitudes/s)',18);text(265,633,'Instancias',20)
text(85,670,'Añadir 4× recursos no garantiza 4× capacidad.',19)
times=[8,10,12,14,16,18];demand=[10,20,100,40,20,10];capacity=[20,30,110,110,30,20]
def points(vals):return ' '.join(f'{685+i*83},{565-v*2.5}' for i,v in enumerate(vals))
S.append(f'<polyline points="{points(capacity)}" fill="none" stroke="{BLUE}" stroke-width="4" stroke-dasharray="9 5"/>')
S.append(f'<polyline points="{points(demand)}" fill="none" stroke="{TEAL}" stroke-width="4"/>')
for i,t in enumerate(times):text(685+i*83,598,f'{t} h',17,anchor='middle')
for v in [0,50,100]:text(656,570-v*2.5,str(v),16,anchor='end')
text(700,237,'Solicitudes/s equivalentes',18)
line(680,632,720,632,TEAL,4);text(732,639,'Demanda',18)
line(875,632,915,632,BLUE,4,dash=True);text(927,639,'Capacidad',18)
text(650,670,'Importan el tiempo de reacción y el costo ocioso.',19)
end('06-escalabilidad-elasticidad.svg','Escalar preserva objetivos bajo más carga; elasticidad ajusta recursos hacia arriba y hacia abajo.')

start('Recuperación: cuánto tiempo y cuántos datos','Incidente hipotético. Los resultados observados se comparan después con los objetivos RTO y RPO.')
line(140,385,1080,385,NAVY,4,arrow=True)
for x,time,label,color in [(185,'10:00','Último punto recuperable',BLUE),(425,'10:05','Fallo',RED),(1030,'10:20','Servicio recuperado',TEAL)]:
    line(x,355,x,415,color,3);dot(x,385,'',color)
    text(x,454,time,25,color,700,'middle')
    text(x,492,label,19,color,600,'middle')
line(185,290,425,290,BLUE,4);line(185,278,185,302,BLUE,3);line(425,278,425,302,BLUE,3)
text(305,251,'5 min',28,BLUE,700,'middle');text(305,212,'Ventana de datos en riesgo',20,BLUE,600,'middle')
line(425,330,1030,330,TEAL,4);line(425,318,425,342,TEAL,3);line(1030,318,1030,342,TEAL,3)
text(750,290,'15 min de interrupción',26,TEAL,700,'middle')
box(80,550,490,114,'RPO · objetivo de punto de recuperación',('¿Qué pérdida temporal de datos es aceptable?','El ejemplo expone hasta 5 minutos.'),BLUE)
box(620,550,490,114,'RTO · objetivo de tiempo de recuperación',('¿En cuánto tiempo debemos restaurar servicio?','El ejemplo tarda 15 minutos.'),TEAL)
end('07-recuperacion.svg','Un backup existente no prueba recuperación: hay que restaurarlo y comprobar integridad y operación.')

start('De una frase del negocio a una decisión verificable','Ejemplo propio de PedidoClaro. Los números son hipótesis para negociar y validar.')
stages=[
('1 · NECESIDAD','Durante el almuerzo no podemos perder pedidos.',BLUE),
('2 · ESCENARIO','Llegan 100 solicitudes/s durante 15 minutos.',TEAL),
('3 · CAPACIDADES','Disponibilidad · elasticidad · integridad de pedidos',BLUE),
('4 · DECISIÓN','Registrar antes de confirmar; aislar el fallo de mapas.',TEAL),
('5 · EVIDENCIA','Prueba de pico + caída de mapas + conciliación de pedidos',BLUE)]
for i,(title,body,color) in enumerate(stages):
    y=145+i*106;box(95,y,1005,85,title,(body,),color)
    if i<4:line(600,y+85,600,y+104,arrow=True)
text(96,690,'Registrar también alternativas, costos, responsables y condición para revisar la decisión.',19)
end('08-requisitos-decisiones.svg','La trazabilidad permite comprobar el porqué; elegir una tecnología por nombre no completa este recorrido.')

print('Generados 7 SVG originales en',OUT)
