from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
P=Path(__file__).resolve().parent
F='/System/Library/Fonts/Supplemental/Arial.ttf'
B='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
INK='#17324d'; BLUE='#e5eff9'; GREEN='#e5f2e9'; GOLD='#fff0d1'; RED='#fbe3de'; GREY='#edf0f4'
def font(n=27,b=False):return ImageFont.truetype(B if b else F,n)
def canvas(title,sub,h=1000):
 global im,d,H
 H=h;im=Image.new('RGB',(1600,h),'#ffffff');d=ImageDraw.Draw(im)
 d.text((55,34),title,font=font(39,True),fill=INK)
 d.text((55,92),sub,font=font(24),fill='#53677a')
 d.line((55,135,1545,135),fill='#becbd6',width=2)
def txt(x,y,s,n=27,b=False,fill=INK):d.multiline_text((x,y),s,font=font(n,b),fill=fill,spacing=8)
def box(x,y,w,h,s,fill=BLUE,n=27):
 d.rounded_rectangle((x,y,x+w,y+h),radius=14,fill=fill,outline=INK,width=3)
 bb=d.multiline_textbbox((0,0),s,font=font(n),spacing=8,align='center')
 d.multiline_text((x+(w-bb[2])/2,y+(h-(bb[3]-bb[1]))/2-5),s,font=font(n),fill=INK,spacing=8,align='center')
def arrow(pts,color=INK,dash=False):
 for a,b in zip(pts,pts[1:]):
  if dash:
   dx=b[0]-a[0];dy=b[1]-a[1];L=math.hypot(dx,dy)
   for k in range(0,int(L),17):
    t=k/L;u=min((k+9)/L,1);d.line((a[0]+dx*t,a[1]+dy*t,a[0]+dx*u,a[1]+dy*u),fill=color,width=3)
  else:d.line((a,b),fill=color,width=4)
 a,b=pts[-2:];ang=math.atan2(b[1]-a[1],b[0]-a[0]);r=15
 d.polygon([b,(b[0]-r*math.cos(ang-.48),b[1]-r*math.sin(ang-.48)),(b[0]-r*math.cos(ang+.48),b[1]-r*math.sin(ang+.48))],fill=color)
def footer(s):txt(55,H-55,s,21,fill='#53677a')
def save(name):im.save(P/(name+'.png'))
def cyl(x,y,w,h,s):
 d.rectangle((x,y+22,x+w,y+h-22),fill=GREY,outline=INK,width=3)
 d.ellipse((x,y+h-44,x+w,y+h),fill=GREY,outline=INK,width=3)
 d.rectangle((x+3,y+23,x+w-3,y+h-23),fill=GREY)
 d.ellipse((x,y,x+w,y+44),fill='#d9e1e8',outline=INK,width=3)
 txt(x+18,y+50,s,23)
def bucket(x,y,s,filled=False):
 box(x,y,360,300,'',GREY)
 d.polygon([(x+90,y+70),(x+270,y+70),(x+247,y+215),(x+113,y+215)],fill='#a7b9c8',outline=INK,width=3)
 d.ellipse((x+90,y+45,x+270,y+95),fill='#cedbe5',outline=INK,width=3)
 if filled:
  for k in range(3):
   d.rectangle((x+112+k*38,y+25+k*8,x+153+k*38,y+113+k*8),fill='white',outline=INK,width=2)
   for v in range(4):d.line((x+119+k*38,y+41+k*8+v*13,x+145+k*38,y+41+k*8+v*13),fill=INK,width=2)
 txt(x+50,y+244,s,25,True)
# 1
canvas('8 · Los componentes son funciones con límites','Recreación didáctica de las figuras 8-1, 8-2 y 8-3 · pp. 108–109',1050)
txt(65,170,'CASA: habitaciones con propósito',28,True)
box(70,230,270,175,'Baño',GREY);box(345,230,385,175,'Sala / cocina',GOLD)
box(70,410,270,260,'Dormitorio 1',BLUE);box(345,410,125,260,'Paso',GREY);box(475,410,255,260,'Dormitorio 2',GREEN)
txt(850,170,'SISTEMA: funciones con propósito',28,True)
box(840,230,220,130,'Registrar\npedido');box(1070,230,210,130,'Validar\npedido');box(1290,230,240,130,'Preparar\npedido')
box(840,375,330,130,'Historial de pedidos');box(1185,375,345,130,'Gestionar inventario')
box(840,520,220,130,'Notificar',GREEN);box(1070,520,210,130,'Cobrar',GREEN);box(1290,520,240,130,'Enviar pedido',GREEN)
arrow([(755,440),(812,440)])
txt(80,735,'EN EL CÓDIGO',27,True);txt(80,780,'order_entry/\n    ordering/\n        payment/\n        validation/',29)
arrow([(460,878),(700,878)])
box(720,788,760,160,'payment/ agrupa el código de pagos.\nEl componente incluye clases colaboradoras;\nno equivale a una clase ni a un servidor.',GOLD,28)
footer('Analogía estructural: las cajas muestran responsabilidad; no son servicios ni bases de datos.');save('c08-01-componentes')
# 2
canvas('Arquitectura lógica y arquitectura física','Recreación de las figuras 8-4 y 8-5 · pp. 110–111',1150)
txt(75,168,'VISTA LÓGICA · ¿qué hace y con quién colabora?',27,True)
box(360,220,180,65,'Actor',GOLD)
box(110,330,230,85,'Componente A');box(110,490,230,85,'Componente B');box(450,490,230,85,'Componente C');box(450,665,230,85,'Componente D');box(840,665,230,85,'Componente E')
box(800,490,260,85,'Repositorio 1',GREY);box(100,665,250,85,'Repositorio 2',GREY);box(840,820,250,85,'Repositorio 3',GREY)
arrow([(360,251),(225,251),(225,330)]);arrow([(450,285),(565,285),(565,490)]);arrow([(225,415),(225,490)]);arrow([(225,575),(225,665)]);arrow([(680,532),(800,532)]);arrow([(565,575),(565,665)]);arrow([(450,707),(350,707)]);arrow([(680,707),(840,707)]);arrow([(955,750),(955,820)])
txt(1160,250,'Los repositorios\nson abstracciones.\nNo eligen motor\nni despliegue.',25)
txt(1160,460,'Flecha = relación\nfuncional.\nNo prescribe HTTP,\ncolas ni procesos.',25)
box(65,955,1470,100,'VISTA FÍSICA: interfaz → servicios / procesos → bases de datos y mensajería.\nUn componente lógico puede estar dentro de un monolito o implementarse mediante servicios.',GREEN,27)
footer('El mismo problema se describe con dos vistas complementarias; no existe equivalencia 1 componente = 1 servicio.');save('c08-02-logica-fisica')
# physical standalone
canvas('La vista física muestra decisiones de ejecución','Recreación simplificada de la figura 8-5 · p. 111',930)
box(565,175,330,95,'Interfaz de usuario',GOLD)
box(180,370,230,120,'Servicio A');box(520,370,230,120,'Servicio B');box(875,370,230,120,'Servicio C');box(1200,640,230,120,'Servicio D')
arrow([(660,270),(660,370)]);arrow([(800,270),(990,270),(990,370)]);arrow([(520,430),(410,430)])
cyl(520,650,230,150,'Base de datos 1');cyl(1200,805,230,65,'')
arrow([(295,490),(295,705),(520,705)]);arrow([(635,490),(635,650)]);arrow([(990,490),(990,705),(750,705)])
box(1190,395,240,80,'Mensajería',GREY);arrow([(1105,430),(1190,430)]);arrow([(1310,475),(1310,640)]);arrow([(1315,760),(1315,805)])
footer('Cilindro = base de datos concreta; cajas = unidades de ejecución. El diagrama no especifica una tecnología.');save('c08-03-fisica')
#4
canvas('Diseñar componentes es un ciclo de aprendizaje','Recreación de la figura 8-6 · p. 112',880)
box(70,350,265,130,'1. Identificar\ncandidatos',GOLD);box(420,350,265,130,'2. Asignar\nhistorias');box(810,190,280,140,'3. Revisar roles\ny responsabilidades');box(1210,350,300,140,'4. Analizar\ncaracterísticas');box(810,600,280,140,'5. Reestructurar\no añadir',GREEN)
arrow([(335,415),(420,415)]);arrow([(555,350),(555,260),(810,260)]);arrow([(1090,260),(1360,260),(1360,350)]);arrow([(1360,490),(1360,670),(1090,670)]);arrow([(810,670),(555,670),(555,480)])
txt(85,185,'Entrada: funciones principales\ny prioridades conocidas.',26)
txt(85,640,'También al agregar\no cambiar una función.',26)
footer('Volver al paso 2 permite comprobar que cada cambio conserva cobertura y mejora los límites.');save('c08-04-ciclo')
#5
canvas('De candidatos vacíos a responsabilidades concretas','Recreación de las figuras 8-7 y 8-9 · pp. 113 y 117',1050)
for x,s in [(100,'Registrar pedido'),(620,'Preparar pedido'),(1140,'Enviar pedido')]:bucket(x,190,s,False)
arrow([(280,510),(280,620)]);arrow([(800,510),(800,620)]);arrow([(1320,510),(1320,620)])
txt(425,530,'Historias de usuario + requisitos',30,True)
for x,s in [(100,'Registrar pedido'),(620,'Preparar pedido'),(1140,'Enviar pedido')]:bucket(x,650,s,True)
footer('Los documentos representan requisitos asignados. Revisar su coherencia puede crear, fusionar o dividir componentes.');save('c08-05-cubos')
#6
canvas('La trampa de las entidades: un nombre oculta demasiadas tareas','Recreación de la figura 8-8 y contraste didáctico · p. 116',950)
for x,s,t in [(70,'Gestor de clientes','Registrar\nCrear perfil\nIniciar sesión\nCambiar avatar'),(570,'Gestor de artículos','Añadir artículo\nActualizar datos\nCargar imagen\nCambiar precio'),(1070,'Gestor de pedidos','Registrar\nDevolver\nPreparar\nEnviar')]:
 box(x,190,420,95,s,RED);arrow([(x+210,285),(x+210,340)]);txt(x+50,365,t,30)
box(75,620,1450,220,'Pregunta de diagnóstico: ¿qué responsabilidad concreta expresa el nombre?\n\nCandidatos más claros: Validar pedido · Preparar pedido · Enviar pedido.\nCompartir una entidad no demuestra compartir una sola responsabilidad.',GREEN,28)
footer('La señal es la acumulación de comportamientos heterogéneos; un sufijo como “Manager” es una pista, no una prueba.');save('c08-06-entidades')
#7
canvas('Una historia transversal descubre un nuevo componente','Recreación de la figura 8-10 · p. 118',960)
box(80,220,300,115,'Gestionar\ninventario');box(535,220,300,115,'Registrar\npedido');box(535,465,300,115,'Preparar\npedido');box(535,710,300,115,'Enviar\npedido');box(1160,465,340,115,'Notificar\nal cliente',GREEN)
arrow([(535,277),(380,277)]);arrow([(685,335),(685,465)]);arrow([(685,580),(685,710)]);arrow([(835,277),(1320,277),(1320,465)]);arrow([(835,522),(1160,522)]);arrow([(835,767),(1320,767),(1320,580)])
txt(1000,165,'Nuevo: enviar correo\ncuando cambia el estado.',26)
txt(70,470,'Una responsabilidad\ncompartida se implementa\nen un lugar coherente.',28)
footer('Las flechas hacia Notificar indican colaboración. No determinan que el envío de correo deba ser sincrónico.');save('c08-07-notificaciones')
#8
canvas('Acoplamiento: mirar entradas, salidas y dependencias ocultas','Recreación de las figuras 8-11, 8-12 y 8-13 · pp. 121–122',1110)
txt(65,175,'AFERENTE (Ca): otros componentes dependen del objetivo',29,True)
box(110,245,310,90,'Registrar pedido');box(110,385,310,90,'Enviar pedido');box(1000,305,340,110,'Notificar al cliente',GREEN)
arrow([(420,290),(780,290),(780,342),(1000,342)]);arrow([(420,430),(830,430),(830,378),(1000,378)]);txt(1050,455,'Ca = 2',31,True)
txt(65,535,'EFERENTE (Ce): el objetivo depende de otros componentes',29,True)
box(200,605,350,100,'Registrar pedido',GOLD);box(1020,605,350,100,'Preparar pedido');arrow([(550,655),(1020,655)]);txt(265,735,'Ce = 1',31,True)
box(70,830,1450,170,'DEPENDENCIA TEMPORAL: registrar debe ocurrir antes de enviar.\nDEPENDENCIA DE CAMBIO: un formato compartido puede obligar a modificar ambos.\nLa ausencia de una llamada directa no demuestra ausencia de acoplamiento.',GREY,28)
footer('Se cuentan dependencias entre componentes distintos, no llamadas por segundo. Cada panel es un ejemplo independiente.');save('c08-08-acoplamiento')
#9
canvas('Ley de Demeter: trasladar conocimiento al lugar adecuado','Recreación de las figuras 8-14 y 8-15 · pp. 123–125',1180)
txt(60,170,'ANTES · Registrar conoce stock, reposición, precios y correo',28,True)
box(95,245,290,95,'Registrar pedido',RED);box(740,245,315,95,'Inventario');box(95,450,290,90,'Notificar');box(740,450,315,90,'Precios');box(1150,450,315,90,'Reponer stock')
arrow([(385,292),(740,292)]);arrow([(240,340),(240,450)]);arrow([(320,340),(320,395),(880,395),(880,450)]);arrow([(350,340),(350,370),(1305,370),(1305,450)]);txt(1120,252,'Ce(Registrar) = 4',28,True)
txt(60,620,'DESPUÉS · Inventario conoce qué hacer cuando hay poco stock',28,True)
box(95,700,290,95,'Registrar pedido',GREEN);box(740,700,315,95,'Inventario',GREEN);box(95,940,290,90,'Notificar');box(740,940,315,90,'Precios');box(1150,940,315,90,'Reponer stock')
arrow([(385,747),(740,747)]);arrow([(240,795),(240,940)]);arrow([(895,795),(895,940)]);arrow([(1000,795),(1000,865),(1305,865),(1305,940)]);txt(1120,707,'Ce(Registrar) = 2\nCe(Inventario) = 2',27,True)
footer('En este ejemplo se mantienen 4 relaciones. Cambia su distribución y el conocimiento que concentra cada componente.');save('c08-09-demeter')
#10/11
for revised in (False,True):
 canvas('Going, Going, Gone · '+('componentes revisados' if revised else 'componentes iniciales'),'Recreación didáctica de la figura '+('8-17 · p. 128' if revised else '8-16 · p. 126'),1330)
 txt(65,172,'ACTOR',28,True);txt(300,172,'ACCIÓN',28,True);txt(810,172,'COMPONENTE',28,True)
 box(60,245,210,235,'Postor',GOLD);txt(300,252,'Ver vídeo\nVer pujas\nRealizar puja',26)
 box(60,575,210,255,'Subastador',GOLD);txt(300,589,'Ingresar puja local\nRecibir pujas web\nMarcar vendido',26)
 box(60,920,210,220,'Sistema',GREY);txt(300,932,'Iniciar subasta\nCobrar ganador\nSeguir actividad',26)
 box(800,235,340,80,'Transmitir vídeo');box(800,355,340,80,'Transmitir pujas');box(800,485,340,100,'Capturar pujas\n'+('del postor' if revised else '(ambos actores)'))
 box(800,790,340,90,'Sesión de subasta');box(800,950,340,90,'Pago externo');box(1200,1050,330,100,'Registrar pujas\n(fuente oficial)',GREEN)
 if revised:box(800,635,340,100,'Capturar pujas\ndel subastador',GREEN)
 arrow([(510,269),(650,269),(650,275),(800,275)]);arrow([(510,308),(685,308),(685,395),(800,395)]);arrow([(510,347),(610,347),(610,518),(800,518)])
 arrow([(585,606),(690,606),(690,665 if revised else 550),(800,665 if revised else 550)])
 arrow([(585,645),(655,645),(655,555),(800,555)])
 arrow([(585,684),(620,684),(620,820),(800,820)])
 arrow([(555,949),(700,949),(700,850),(800,850)]);arrow([(555,988),(800,988)]);arrow([(555,1027),(620,1027),(620,1210),(1365,1210),(1365,1150)])
 arrow([(1140,535),(1175,535),(1175,395),(1140,395)],dash=True);arrow([(1140,555),(1400,555),(1400,1050)],dash=True)
 if revised:
  arrow([(1140,670),(1210,670),(1210,415),(1140,415)],dash=True);arrow([(1140,695),(1450,695),(1450,1050)],dash=True)
 arrow([(970,880),(970,950)],dash=True);arrow([(1140,835),(1310,835),(1310,1050)],dash=True)
 footer('Continua: acción asignada. Discontinua: colaboración lógica; no implica mensajería asíncrona ni orden transaccional.');save('c08-11-ggg-revisado' if revised else 'c08-10-ggg-inicial')
print('Generados',len(list(P.glob('c08-*.png'))),'PNG')
# Diagrama adicional de decisión: elaboración didáctica de la nota 07.
canvas('¿Conservar o separar un componente?','Elaboración didáctica basada en el análisis de características · p. 120',1160)
box(510,175,580,90,'Una función aparentemente común',GOLD)
box(510,335,580,100,'Comparar demanda y\nconsecuencias de fallo')
arrow([(800,265),(800,335)])
box(510,505,580,115,'¿Las necesidades diferentes\njustifican un límite?',GOLD)
arrow([(800,435),(800,505)])
box(100,730,580,110,'Separar responsabilidades o entradas',GREEN)
box(920,730,580,110,'Conservar el componente',BLUE)
arrow([(510,562),(390,562),(390,730)]);arrow([(1090,562),(1210,562),(1210,730)])
txt(325,625,'Sí',29,True);txt(1240,625,'No',29,True)
box(100,900,580,90,'Diseñar contratos y comprobar coste',GREEN)
arrow([(390,840),(390,900)])
box(920,995,580,90,'Validar cobertura de historias',GREY)
arrow([(680,945),(800,945),(800,1040),(920,1040)]);arrow([(1210,840),(1210,995)])
footer('Las flechas muestran razonamiento arquitectónico. No implican que separar sea siempre la mejor respuesta.');save('c08-12-decision-granularidad')
