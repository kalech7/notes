"""Diagramas propios del capítulo 6. Regenerar: uv run --with pillow python generar_visuales.py."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).resolve().parent
BG = '#F7F9FC'
INK = '#172B45'
BLUE = '#DCEBFF'
GREEN = '#D5F2E4'
ORANGE = '#FFE6C7'
PURPLE = '#EAE1FA'
RED = '#F9DCDD'
GRAY = '#E7ECF2'
LINE = '#64758B'
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'

def font(size=25, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)

def canvas(title, subtitle, h=1000):
    global im, d
    im = Image.new('RGB', (1600, h), BG)
    d = ImageDraw.Draw(im)
    text(55, 32, title, 39, True)
    text(55, 92, subtitle, 25)
    d.line((55, 137, 1545, 137), fill=LINE, width=2)

def text(x,y,s,size=25,bold=False,fill=INK):
    d.multiline_text((x,y),str(s),font=font(size,bold),fill=fill,spacing=9)

def box(x,y,w,h,s,fill=BLUE,size=25,bold=False):
    f=font(size,bold)
    bounds=d.multiline_textbbox((0,0),s,font=f,spacing=9)
    tw,th=bounds[2]-bounds[0],bounds[3]-bounds[1]
    assert tw <= w-20 and th <= h-18,(s,tw,th,w,h)
    assert x>=0 and y>=0 and x+w<=im.width and y+h<=im.height,(s,x,y)
    d.rounded_rectangle((x,y,x+w,y+h),radius=15,fill=fill,outline=LINE,width=2)
    d.multiline_text((x+(w-tw)/2,y+(h-th)/2-bounds[1]),s,font=f,spacing=9,fill=INK,align='center')

def arrow(points, color=LINE, width=4):
    d.line(points, fill=color,width=width)
    (x0,y0),(x1,y1)=points[-2:]
    a=math.atan2(y1-y0,x1-x0)
    d.polygon([(x1,y1),(x1-14*math.cos(a-.45),y1-14*math.sin(a-.45)),(x1-14*math.cos(a+.45),y1-14*math.sin(a+.45))],fill=color)

def cells(x,y,values,w=75,colors=None,size=27):
    for i,v in enumerate(values):
        fill=(colors or {}).get(i,BLUE if v is not None else BG)
        box(x+i*w,y,w-5,65,'·' if v is None else str(v),fill,size)

def save(name,caption):
    text(55,im.height-82,caption,22)
    text(55,im.height-43,'Database Internals · Capítulo 6 · Diagramas de estudio en español',18,fill=LINE)
    im.save(OUT/name)

canvas('Copy-on-write: cambia el camino, comparte el resto',
       'Adaptación conceptual de la figura 6-1 · Ejemplo: actualizar la clave 70',1050)
arrow([(440,340),(440,435),(260,435),(260,505)])
arrow([(440,340),(440,435),(750,435),(750,505)])
arrow([(1160,340),(1160,420),(260,420),(260,505)],'#3C769D')
arrow([(1160,340),(1160,450),(1260,450),(1260,505)],'#21805B')
arrow([(750,590),(750,650),(520,650),(520,735)])
arrow([(750,590),(750,650),(860,650),(860,735)])
arrow([(1260,590),(1260,675),(520,675),(520,735)],'#3C769D')
arrow([(1260,590),(1260,675),(1310,675),(1310,735)],'#21805B')
box(240,245,400,95,'R0 · raíz anterior',ORANGE,29,True)
box(960,245,400,95,'R1 · raíz nueva',GREEN,29,True)
box(100,505,320,85,'Subárbol intacto',BLUE)
box(580,505,340,85,'I0 · rama anterior',ORANGE)
box(1090,505,340,85,'I1 · rama copiada',GREEN)
box(340,735,360,95,'Hoja compartida\nclaves 50 y 60',BLUE)
box(735,735,250,95,'L0 · 70 = 10',ORANGE)
box(1160,735,300,95,'L1 · 70 = 12',GREEN)
text(235,180,'Lector anterior conserva R0',27,True)
text(920,180,'Nuevos lectores reciben R1',27,True)
text(70,885,'3 páginas nuevas: L1, I1 y R1. Las páginas azules se reutilizan sin copiarse.',28)
save('01-copy-on-write.png','Publicar R1 exige completar y persistir sus páginas antes de hacer durable la nueva raíz.')

canvas('Un nodo puede tener tres representaciones en memoria',
       'El formato físico y el objeto usado por el programa cumplen funciones diferentes',980)
for x,title in [(55,'Acceso directo'),(570,'Objeto materializado'),(1085,'Wrapper del buffer')]:
    text(x,185,title,28,True)
box(55,260,450,110,'Punteros / estructuras\ninterpretan bytes',BLUE)
box(55,480,450,110,'Buffer de bytes\nheader + claves + offsets',GRAY)
arrow([(280,370),(280,480)])
text(65,650,'Una representación principal.\nEl código respeta el formato\ny protege los cambios.',25)
box(570,260,450,110,'Objeto del lenguaje\nlistas, claves y valores',GREEN)
box(570,480,450,110,'Buffer de bytes\nimagen de la página',GRAY)
arrow([(795,370),(795,480)])
text(825,405,'reconciliar',22)
text(580,650,'Dos representaciones.\nCambios flexibles en el objeto;\nla serialización cuesta memoria.',25)
box(1085,260,450,110,'Wrapper\nget / set / insert',PURPLE)
box(1085,480,450,110,'Buffer de bytes\nmodificado por el wrapper',GRAY)
arrow([(1310,370),(1310,480)])
text(1095,650,'Interfaz de objetos.\nCada operación transforma\nel buffer que está detrás.',25)
save('02-representaciones.png','Separar representación, visibilidad y persistencia permite optimizarlas con reglas diferentes.')

canvas('WiredTiger: imagen base + actualizaciones pendientes',
       'Figuras 6-2 y 6-3 explicadas con claves concretas · Se omiten detalles de MVCC',1120)
text(70,185,'Página limpia',30,True)
text(810,185,'Página modificada en memoria',30,True)
box(70,245,650,110,'Índice en RAM: 10, 20, 30\nsin actualizaciones pendientes',BLUE)
box(810,245,650,110,'Índice en RAM: 10, 20, 30\n+ estructura de actualizaciones',GREEN)
box(810,405,650,120,'Cambios: PUT(20, B2)\nDELETE(30) · PUT(40, D)',ORANGE)
box(70,570,650,100,'Base en disco\n10:A · 20:B · 30:C',GRAY)
box(810,570,650,100,'Base en disco\n10:A · 20:B · 30:C',GRAY)
arrow([(395,355),(395,570)])
arrow([(1135,355),(1135,405)])
arrow([(810,465),(740,465),(740,735),(810,735)])
arrow([(1135,670),(1135,695)])
box(810,695,650,105,'Lectura visible: 10:A · 20:B2 · 40:D\n30 está borrada aunque exista en la base',PURPLE,25)
arrow([(1135,800),(1135,855)])
box(70,855,1390,100,'Reconciliación: construir una nueva imagen de disco con los cambios aplicables\nSi supera el tamaño permitido, puede producir varias páginas',GREEN,25)
save('03-wiredtiger.png','Una lectura que ignora los cambios pendientes puede devolver datos viejos o resucitar un borrado.')

canvas('LA-Tree: buffers por subárbol y propagación por lotes',
       'Adaptación de la figura 6-4 · Las operaciones bajan según su rango de claves',1100)
box(380,190,840,110,'Buffer superior\nPUT(12,a) · PUT(18,b) · DELETE(70) · PUT(80,c)',ORANGE,26)
arrow([(650,300),(650,375),(400,375),(400,435)])
arrow([(960,300),(960,375),(1200,375),(1200,435)])
text(700,335,'separador 50',24)
box(85,435,630,110,'Subárbol: claves < 50\nBuffer: PUT(12,a) · PUT(18,b)',GREEN,27)
box(885,435,630,110,'Subárbol: claves ≥ 50\nBuffer: DELETE(70) · PUT(80,c)',PURPLE,27)
arrow([(400,545),(400,650)])
arrow([(1200,545),(1200,650)])
box(85,650,630,100,'Hojas izquierdas\naplicar juntas las operaciones del lote',BLUE,25)
box(885,650,630,100,'Hojas derechas\nborrar 70 e insertar 80 en el lote',BLUE,25)
box(85,820,1430,110,'Leer 80 antes de llegar a la hoja: consultar también los buffers de su ruta\nLos splits y merges necesarios se agrupan al materializar el lote',GRAY,28)
save('04-la-tree.png','La actualización lógica puede existir arriba mientras la hoja física aún conserva el estado anterior.')

canvas('FD-Tree: un B-Tree pequeño delante de runs inmutables',
       'Adaptación de la figura 6-6 · Capacidades didácticas con factor k = 4',1150)
box(70,185,730,120,'Head tree mutable\nB-Tree pequeño · hasta 4 registros',ORANGE,29)
box(1000,185,500,120,'Escrituras nuevas\nse acumulan aquí',GRAY,26)
arrow([(1000,245),(800,245)])
arrow([(435,305),(435,365)])
box(70,365,730,100,'L1 · run ordenado\numbral ilustrativo: 4 registros',GREEN,28)
box(1000,365,500,100,'Al llenarse la cabeza:\nfusionar con L1',GRAY,25)
arrow([(435,465),(435,540)])
box(70,540,730,100,'L2 · run ordenado\numbral ilustrativo: 16 registros',BLUE,28)
box(1000,540,500,100,'Si L1 excede su umbral:\nfusionar hacia L2',GRAY,25)
arrow([(435,640),(435,715)])
box(70,715,730,100,'L3 · run ordenado\numbral ilustrativo: 64 registros',PURPLE,28)
text(1000,715,'Los fences enlazan páginas\ny reducen la búsqueda\nrepetida entre niveles.',25)
box(70,895,1430,120,'DELETE(70) crea un tombstone que oculta las versiones antiguas de 70\nSe elimina cuando ya no quedan registros inferiores que deba ocultar',RED,28)
save('05-fd-tree.png','Una fusión escribe un run nuevo y sustituye la versión anterior; no modifica el run existente.')

canvas('Fractional cascading: buscar una vez y reutilizar la posición',
       'Ejemplo del libro reconstruido de abajo arriba · Naranja: muestras añadidas',1170)
text(60,182,'Catálogo C1',27,True)
cells(60,235,[12,22,24,26,30,32,34,39],80,{1:ORANGE,3:ORANGE,4:ORANGE})
text(660,447,'C2',27,True)
cells(60,500,[16,22,25,26,28,30,35],80,{0:ORANGE,3:ORANGE})
text(500,752,'C3 = A3',27,True)
cells(60,805,[11,16,24,26,30],80)
for up,low in [(1,1),(3,3),(4,5)]:
    x=60+up*80+35; z=60+low*80+35
    arrow([(x,300),(x,350+up*18),(z,350+up*18),(z,500)])
for up,low in [(0,1),(3,3)]:
    x=60+up*80+35;z=60+low*80+35
    arrow([(x,565),(x,640+up*12),(z,640+up*12),(z,805)])
box(835,235,700,160,'Consulta: primer elemento ≥ 27\nC1: búsqueda binaria → 30\npuente hacia el 30 de C2',BLUE,27)
box(835,490,700,160,'C2: revisión local → 28\nEl puente inferior cercano es 26\nNo se busca todo C2 otra vez',GREEN,27)
box(835,795,700,120,'C3: desde 26, el siguiente es 30\nResultado en A1, A2, A3: 32, 28, 30',PURPLE,25)
text(60,965,'Los catálogos tienen copias auxiliares: encontrar 30 en C1 no significa que 30 exista en A1.',27)
save('06-fractional-cascading.png','Los enlaces dibujados son los puentes de muestra; un catálogo completo añade metadatos de posición.')

canvas('Bw-Tree: un nodo lógico es una base más una cadena de deltas',
       'Adaptación de la figura 6-7 · El delta más nuevo está al inicio',1100)
box(70,185,500,95,'Padre: hijo con ID lógico N7',PURPLE,27)
arrow([(320,280),(320,355)])
box(70,355,500,95,'Tabla de mapeo\nN7 → cabeza física H3',GREEN,28)
arrow([(570,400),(680,400)])
box(680,355,770,95,'H3 · PUT(C,7) → H2',ORANGE,29)
arrow([(1065,450),(1065,505)])
box(680,505,770,95,'H2 · DELETE(B) → H1',ORANGE,29)
arrow([(1065,600),(1065,655)])
box(680,655,770,95,'H1 · PUT(A,12) → base',ORANGE,29)
arrow([(1065,750),(1065,805)])
box(680,805,770,95,'Base · A=10, B=20',BLUE,29)
box(70,600,500,190,'Estado reconstruido\nA=12 · C=7\nB está borrada',GREEN,29)
save('07-bw-cadenas.png','El padre sigue usando N7 aunque cambie la dirección física de la cabeza de su cadena.')

canvas('CAS: dos escritores compiten por publicar una cabeza',
       'Compare-and-swap cambia el puntero solo si conserva el valor esperado',1120)
text(65,185,'Momento',27,True)
text(315,185,'Escritor T1',27,True)
text(870,185,'Escritor T2',27,True)
rows=[('1', 'Lee cabeza H', 'Lee cabeza H'),
      ('2', 'Prepara D1 → H', 'Prepara D2 → H'),
      ('3', 'CAS(H, D1) tiene éxito', 'CAS(H, D2) falla: ahora es D1'),
      ('4', 'El cambio de T1 está publicado', 'Relee y prepara D2\' → D1'),
      ('5', 'Se conserva el efecto de T1', 'CAS(D1, D2\') tiene éxito')]
for i,(moment,a,b) in enumerate(rows):
    y=245+i*125
    box(65,y,130,85,moment,GRAY,30)
    box(255,y,530,85,a,GREEN,25)
    box(840,y,695,85,b,RED if i==2 else BLUE,25)
box(255,905,1280,95,"Resultado: D2' → D1 → H. La publicación fallida no sobrescribe a T1.",PURPLE,28)
save('08-cas.png','Este ejemplo ilustra publicación atómica; CAS por sí solo no garantiza durabilidad ni aislamiento SQL.')

canvas('Bw-Tree: split y merge conservan rutas válidas por etapas',
       'Las modificaciones estructurales se anuncian con deltas antes de terminar el padre',1170)
text(65,185,'SPLIT · separador 50',30,True)
box(65,245,445,140,'1 · Crear derecha R\ncon claves ≥ 50\nconsolidar estado',BLUE,26)
box(575,245,445,140,'2 · Publicar split delta\nN: si clave ≥ 50\nredirigir a R',ORANGE,26)
box(1085,245,445,140,'3 · Actualizar padre\nN y R quedan\naccesibles directamente',GREEN,26)
arrow([(510,315),(575,315)])
arrow([(1020,315),(1085,315)])
box(65,435,1465,100,'Antes del paso 3: buscar 70 llega a N y después a R mediante el split delta',PURPLE,28)
text(65,600,'MERGE · unir derecha R a izquierda L',30,True)
box(65,665,445,140,'1 · Remove delta en R\nmarca el comienzo\nde la fusión',ORANGE,26)
box(575,665,445,140,'2 · Merge delta en L\nincorpora lógicamente\nel contenido de R',BLUE,26)
box(1085,665,445,140,'3 · Actualizar padre\nretirar el enlace\ndirecto a R',GREEN,26)
arrow([(510,735),(575,735)])
arrow([(1020,735),(1085,735)])
box(65,875,1465,140,'Los hilos pueden ayudar a terminar una operación estructural incompleta\nAbort deltas coordinan SMO que entrarían en conflicto\nRetirar un enlace no autoriza todavía a liberar la memoria',GRAY,26)
save('09-bw-split-merge.png','Los dibujos representan el orden lógico descrito por el capítulo, no pseudocódigo concurrente completo.')

canvas('Consolidar no significa poder liberar inmediatamente',
       'Reclamación por épocas: conservar lo retirado hasta que los lectores antiguos terminen',1080)
text(65,185,'Tiempo →',28,True)
for x,label in [(300,'Época 7'),(800,'Retirar cadena'),(1250,'Época 8')]:
    text(x,240,label,25,True)
arrow([(280,320),(1490,320)])
box(65,390,310,95,'Lector antiguo',ORANGE,26)
box(420,390,1080,95,'Usa la cadena vieja hasta terminar en este punto',ORANGE,27)
box(65,530,310,95,'Publicación',GREEN,26)
box(420,530,370,95,'Tabla → cadena vieja',BLUE,25)
box(865,530,635,95,'Tabla → nueva base consolidada',GREEN,25)
arrow([(790,575),(865,575)])
box(65,685,310,95,'Lector nuevo',PURPLE,26)
box(865,685,635,95,'Solo puede alcanzar la nueva base',PURPLE,25)
box(65,840,1435,105,'La cadena vieja deja de ser visible para lectores nuevos, pero sigue viva\nSe libera tras salir todos los participantes que podían haberla alcanzado',GRAY,28)
save('10-reclamacion-epocas.png','El seguimiento por épocas necesita un protocolo de entrada y salida, aunque la lectura no use latches.')

canvas('Layout van Emde Boas: subárboles juntos a varias escalas',
       'Adaptación de la figura 6-8 · Árbol binario de 4 niveles · Los números son IDs',1210)
coords={1:(800,225),2:(430,365),3:(1170,365),4:(245,535),5:(615,535),6:(985,535),7:(1355,535),
        8:(140,685),9:(315,685),10:(520,685),11:(695,685),12:(900,685),13:(1075,685),14:(1260,685),15:(1435,685)}
groups={1:BLUE,2:BLUE,3:BLUE,4:GREEN,8:GREEN,9:GREEN,5:ORANGE,10:ORANGE,11:ORANGE,6:PURPLE,12:PURPLE,13:PURPLE,7:RED,14:RED,15:RED}
for n in range(1,8):
    for c in (2*n,2*n+1):arrow([coords[n],coords[c]],width=3)
for n,(x,y) in coords.items():box(x-44,y-35,88,70,str(n),groups[n],28,True)
d.line((60,450,1540,450),fill=LINE,width=3)
text(60,760,'Corte por altura: parte superior de 2 niveles + 4 subárboles de 2 niveles',24)
text(60,820,'Orden físico vEB',28,True)
order=[1,2,3,4,8,9,5,10,11,6,12,13,7,14,15]
cells(60,875,order,98,{i:groups[n] for i,n in enumerate(order)},27)
text(60,995,'[1,2,3]  |  [4,8,9]  |  [5,10,11]  |  [6,12,13]  |  [7,14,15]',28,True)
text(60,1050,'Cada grupo se vuelve a ordenar con la misma regla. No hay un tamaño de bloque B en la receta.',25)
save('11-layout-veb.png','La contigüidad recursiva mejora localidad para distintos bloques; no elimina cachés ni transferencias.')

canvas('Packed array: mantener el orden dejando huecos distribuidos',
       'Adaptación de la figura 6-9 · Ejemplo propio con un array de 8 posiciones',1170)
rows=[('Estado inicial · 4/8 = 50 %',[2,None,8,None,12,None,18,None],{}),
      ('Insertar 10 · ocupa un hueco local',[2,None,8,10,12,None,18,None],{3:GREEN}),
      ('Insertar 11 · mover 12 para abrir espacio',[2,None,8,10,11,12,18,None],{4:GREEN,5:ORANGE}),
      ('Redistribuir una ventana mayor',[2,None,8,10,None,11,12,18],{4:BG,5:GREEN,6:ORANGE,7:ORANGE})]
for i,(label,values,colors) in enumerate(rows):
    y=185+215*i
    text(65,y,label,28,True)
    cells(65,y+65,values,130,colors,30)
    if i<3:arrow([(1220,y+90),(1330,y+90),(1330,y+235),(1220,y+235)])
text(65,1050,'El índice debe ajustar las referencias a los elementos reubicados; los huecos consumen capacidad.',25)
save('12-packed-array.png','Los umbrales de densidad se aplican por ventanas; estas filas ilustran movimientos, no una política completa.')

print('12 diagramas PNG generados; texto de todas las cajas validado contra sus dimensiones.')
