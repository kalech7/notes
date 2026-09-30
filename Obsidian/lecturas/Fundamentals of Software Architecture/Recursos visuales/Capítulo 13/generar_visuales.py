"""Diagramas didácticos originales. Ejecutar con Python y Pillow; sin datos medidos."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math
OUT=Path(__file__).resolve().parent
FONT='/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
INK='#17344b'; BLUE='#e2eef9'; GREEN='#dff3e9'; GOLD='#fff0ca'; RED='#fae2e1'; GREY='#edf0f3'
def font(n=30,b=False): return ImageFont.truetype(BOLD if b else FONT,n)
def base(title, subtitle):
 im=Image.new('RGB',(1600,1000),'#f7f9fc'); d=ImageDraw.Draw(im)
 d.text((60,38),title,font=font(46,True),fill=INK); d.text((60,105),subtitle,font=font(26),fill=INK)
 d.text((60,950),'Capítulo 13 · Elaboración didáctica original · Las cajas no fijan una tecnología',font=font(22),fill=INK)
 return im,d
def text(d,xy,s,size=28,b=False): d.multiline_text(xy,s,font=font(size,b),fill=INK,spacing=10)
def box(d,xy,s,fill=BLUE,size=30):
 d.rounded_rectangle(xy,22,fill=fill,outline=INK,width=3)
 x0,y0,x1,y1=xy; lines=s.split('\n'); h=len(lines)*(size+10)-10
 for i,l in enumerate(lines):
  w=d.textlength(l,font=font(size)); d.text(((x0+x1-w)/2,(y0+y1-h)/2+i*(size+10)),l,font=font(size),fill=INK)
def arrow(d,a,b,label=None,color=INK):
 d.line((a,b),fill=color,width=5); ang=math.atan2(b[1]-a[1],b[0]-a[0]); q=20
 pts=[b,(b[0]-q*math.cos(ang-.5),b[1]-q*math.sin(ang-.5)),(b[0]-q*math.cos(ang+.5),b[1]-q*math.sin(ang+.5))];d.polygon(pts,fill=color)
 if label: text(d,((a[0]+b[0])/2+8,(a[1]+b[1])/2-35),label,23)
def save(im,name): im.save(OUT/name)
# 1 topología
im,d=base('Un flujo estable, muchas reglas variables','El núcleo coordina; cada plugin encapsula una variante del negocio.')
d.rounded_rectangle((65,170,1535,875),25,outline='#a7b6c4',width=4);text(d,(90,190),'Una entrega monolítica habitual',25,True)
box(d,(580,320,1010,610),'NÚCLEO\nRecibir dispositivo\nElegir evaluación\nGuardar y comunicar',BLUE)
box(d,(120,280,420,450),'Plugin teléfono\nReglas del modelo',GREEN,27)
box(d,(120,560,420,730),'Plugin tableta\nReglas del modelo',GREEN,27)
box(d,(1170,410,1470,580),'Plugin portátil\nReglas del modelo',GREEN,27)
arrow(d,(580,380),(420,380));arrow(d,(580,580),(420,630));arrow(d,(1010,490),(1170,490))
text(d,(525,760),'Los plugins comparten contrato.\nNo se llaman entre sí.',32,True);save(im,'c13-01-nucleo-plugins.png')
# 2 espectro
im,d=base('Cuánto hace el núcleo sin extensiones','Dos extremos explican el espectro del libro; no es una puntuación de calidad.')
box(d,(90,220,735,610),'Núcleo mínimo\nAnaliza código y produce AST\nSin reglas: aporta poco\nPlugins: detectan problemas',BLUE,31)
box(d,(865,220,1510,610),'Producto funcional\nNavega y muestra páginas\nSin extensiones: sigue sirviendo\nPlugins: capacidades adicionales',GREEN,31)
arrow(d,(220,715),(1380,715));text(d,(95,760),'Menos funcionalidad autónoma',29);text(d,(980,760),'Más funcionalidad autónoma',29)
text(d,(180,840),'La pregunta decisiva: ¿el núcleo conserva un flujo estable o acumula variantes?',30,True);save(im,'c13-02-espectro.png')
# 3 registro
im,d=base('Descubrir, elegir, invocar y devolver','El registro es el mapa; el contrato es la promesa de comportamiento.')
box(d,(65,240,370,405),'Solicitud\nTipo: teléfono',GREY,29)
box(d,(505,240,865,405),'Núcleo\nBusca por tipo',BLUE,29)
box(d,(1070,240,1500,405),'Registro\nteléfono → Evaluador A\ncontrato → evaluación v1',GOLD,27)
arrow(d,(370,320),(505,320));arrow(d,(865,320),(1070,320))
box(d,(505,565,865,735),'Contrato estable\nevaluar(entrada)\n→ resultado',BLUE,29)
box(d,(1070,565,1500,735),'Plugin A\nAplica reglas\nDevuelve informe',GREEN,29)
arrow(d,(685,405),(685,565));arrow(d,(865,650),(1070,650));arrow(d,(1070,705),(865,705))
text(d,(80,835),'Nombre o dirección incorrectos: fallo al localizar.\nSignificado o versión incorrectos: fallo de contrato.',31);save(im,'c13-03-registro-contrato.png')
# 4 local remoto
im,d=base('Una extensión local y una extensión remota','La separación del código y la separación de procesos producen garantías distintas.')
text(d,(90,180),'Dentro del proceso',34,True);text(d,(870,180),'A través de la red',34,True)
d.rounded_rectangle((65,240,735,655),20,outline=INK,width=3)
box(d,(100,290,350,460),'Núcleo',BLUE);box(d,(450,290,700,460),'Plugin',GREEN);arrow(d,(350,370),(450,370))
text(d,(105,500),'Llamada de función\nMemoria y recursos compartidos\nUn fallo grave puede afectar a ambos',25)
box(d,(870,285,1140,460),'Núcleo\nProceso A',BLUE);box(d,(1270,285,1540,460),'Plugin\nProceso B',GREEN);arrow(d,(1140,370),(1270,370))
text(d,(870,500),'Serialización, latencia y timeout\nPuede fallar una parte del sistema\nRequiere versiones y observabilidad',25)
box(d,(180,745,1420,865),'Elegir remoto por necesidades concretas:\naislamiento, carga, despliegue o especialización',GOLD,30);save(im,'c13-04-local-remoto.png')
# 5 datos
im,d=base('Quién conoce qué datos','El núcleo posee los datos comunes; un plugin puede poseer reglas privadas.')
box(d,(620,230,1000,435),'Núcleo\nExpediente común\nEntrada del contrato',BLUE)
box(d,(90,525,490,740),'BD común\nDispositivo y estado\nResultados guardados',GREY)
box(d,(1110,230,1510,435),'Plugin evaluación\nCalcula resultado',GREEN)
box(d,(1110,610,1510,815),'Almacén privado\nReglas del modelo\nSolo accede el plugin',GOLD)
arrow(d,(710,435),(430,525));arrow(d,(1000,315),(1110,315));arrow(d,(1310,435),(1310,610))
text(d,(540,620),'El plugin recibe datos\npor contrato, sin conocer\nlas tablas del núcleo.',31)
text(d,(80,830),'Cambiar el esquema común se absorbe en el núcleo si el contrato conserva su significado.',29,True);save(im,'c13-05-propiedad-datos.png')
# 6 riesgos
im,d=base('Dos formas de perder la ventaja del microkernel','La frontera debe contener cambios sin convertir cada ampliación en una coordinación global.')
box(d,(80,230,740,550),'Riesgo 1: núcleo volátil\nNueva jurisdicción → nuevo if\nNuevo modelo → nueva condición\nCada variante modifica el centro',RED,29)
box(d,(860,230,1520,550),'Riesgo 2: plugins entrelazados\nA depende de B; B depende de C\nA necesita librería v1\nC necesita la misma librería v2',RED,29)
box(d,(80,650,740,865),'Gobierno: revisar cambios\n¿La regla pertenece al plugin?\n¿Cambió el contrato público?\n¿La modificación era necesaria?',GREEN,29)
box(d,(860,650,1520,865),'Gobierno: revisar dependencias\nProhibir importaciones laterales\nProbar versiones compatibles\nExplicitar excepciones justificadas',GREEN,29)
arrow(d,(410,550),(410,650));arrow(d,(1190,550),(1190,650));save(im,'c13-06-riesgos-gobierno.png')
