"""Recreaciones didácticas de las figuras 10-1 a 10-5. Ejecutar con Pillow.
No son mediciones: muestran mensajes y estados del ejemplo del libro.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).parent
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
BG, INK, BLUE, GREEN, RED = '#f4f7fb', '#14283e', '#175ca6', '#147b59', '#b93645'

def canvas(title, subtitle):
    im = Image.new('RGB', (1800, 1100), BG)
    d = ImageDraw.Draw(im)
    d.text((60, 35), title, font=ImageFont.truetype(BOLD, 48), fill=INK)
    d.text((60, 105), subtitle, font=ImageFont.truetype(FONT, 28), fill=INK)
    d.text((60, 1040), 'Database Internals · Capítulo 10 · Recreación didáctica en español',
           font=ImageFont.truetype(FONT, 24), fill=INK)
    return im, d

def text(d, xy, lines, size=30, color=INK, bold=False, spacing=15):
    d.multiline_text(xy, '\n'.join(lines), font=ImageFont.truetype(BOLD if bold else FONT, size),
                     fill=color, spacing=spacing)

def box(d, rect, title, lines, color=BLUE):
    x,y,x2,y2=rect
    d.rounded_rectangle(rect, radius=22, fill='white', outline=color, width=4)
    text(d,(x+25,y+20),[title],34,color,True)
    text(d,(x+25,y+83),lines,27 if x2-x < 600 else 30)

def arrow(d, a, b, color=BLUE, width=6):
    d.line((a,b),fill=color,width=width)
    theta=math.atan2(b[1]-a[1],b[0]-a[0])
    p=[b,(b[0]-24*math.cos(theta-.5),b[1]-24*math.sin(theta-.5)),
       (b[0]-24*math.cos(theta+.5),b[1]-24*math.sin(theta+.5))]
    d.polygon(p,fill=color)

def save(im,name):
    im.save(OUT/name)

im,d=canvas('Bully modificado: gana el mayor rango accesible', 'Figura 10-1 · 6 falla, 3 inicia y 5 resulta elegido')
box(d,(60,180,850,520),'1 · Preguntar',['3 → 4: ELECCIÓN','3 → 5: ELECCIÓN','3 → 6: ELECCIÓN (sin respuesta)'])
box(d,(950,180,1740,520),'2 · Recibir respuestas',['4 → 3: ESTOY VIVO','5 → 3: ESTOY VIVO','3 compara los rangos: máx(4, 5) = 5'])
box(d,(60,620,850,970),'3 · Delegar el liderazgo',['3 → 5: procede como líder','Se usa el mayor que respondió.','El silencio de 6 es una sospecha.'])
box(d,(950,620,1740,970),'4 · Difundir el resultado',['5 → {1, 2, 3, 4}: ELEGIDO','Los participantes conocen al líder.','Esto no prueba unicidad global.'],GREEN)
arrow(d,(860,350),(935,350));arrow(d,(1300,530),(1300,575));arrow(d,(930,570),(460,570));arrow(d,(460,580),(460,610));arrow(d,(860,795),(935,795))
save(im,'01-bully.png')

im,d=canvas('Sucesores preparados: evitar una elección completa','Figura 10-2 · El líder 6 había publicado la lista ordenada [5, 4]')
box(d,(60,190,580,660),'1 · Detectar y contactar',['6 deja de responder.','3 consulta la lista.','3 → 5: ¿sigues disponible?','No consulta primero a 4.'])
box(d,(640,190,1160,660),'2 · Responder',['5 → 3: ESTOY VIVO','3 deja de buscar alternativas.','Si 5 no responde,','el siguiente es 4.'])
box(d,(1220,190,1740,660),'3 · Anunciar',['5 → {1, 2, 3, 4}:','SOY EL NUEVO LÍDER','5 puede publicar','la nueva lista [4, 3].'],GREEN)
arrow(d,(590,410),(630,410));arrow(d,(1170,410),(1210,410))
box(d,(60,760,1740,975),'Condición de la mejora',['La ruta rápida funciona si algún sucesor preseleccionado sigue accesible.','Una lista de reemplazos reduce mensajes, pero no evita dos líderes en una partición.'],RED)
save(im,'02-sucesores.png')

im,d=canvas('Candidatos y ordinarios: iniciar no significa ganar','Figura 10-3 · Solo los candidatos {1, 2, 6} pueden convertirse en líderes')
box(d,(60,180,850,430),'Candidatos',['1: disponible    2: disponible    6: caído','El mayor candidato que responde es 2.'])
box(d,(950,180,1740,430),'Ordinarios',['3, 4 y 5 pueden coordinar la elección.','4 inicia; 5 no gana por tener mayor ID.'],GREEN)
box(d,(60,510,580,825),'1 · Consultar',['4 → {1, 2}: ELECCIÓN','6 se considera no disponible.','Se consulta al grupo candidato.'])
box(d,(640,510,1160,825),'2 · Seleccionar',['{1, 2} → 4: ESTOY VIVO','4 calcula máx(1, 2) = 2.','El iniciador permanece ordinario.'])
box(d,(1220,510,1740,825),'3 · Comunicar',['4 anuncia: LÍDER = 2','Lo reciben 1, 2, 3 y 5.','2 toma el papel de coordinador.'],GREEN)
arrow(d,(590,665),(630,665));arrow(d,(1170,665),(1210,665))
text(d,(65,910),['Retardo δ: más prioridad → menor espera antes de iniciar.',
                    'El escalonamiento reduce carreras bajo los supuestos de latencia; no crea un quórum.'],32)
save(im,'03-candidatos.png')

im,d=canvas('Invitación: fusionar grupos sin reiniciar todo','Figura 10-4 · El número de líderes depende del número de grupos')
box(d,(60,180,580,665),'1 · Cuatro grupos',['{1}, líder 1','{2}, líder 2','{3}, líder 3','{4}, líder 4','1 invita a 2; 3 invita a 4.'])
box(d,(640,180,1160,665),'2 · Dos grupos',['{1, 2}, líder 1','{3, 4}, líder 3','','1 contacta a 3.','Los líderes negocian la fusión.'])
box(d,(1220,180,1740,665),'3 · Un grupo',['{1, 2, 3, 4}, líder 1','','3 y 4 actualizan su líder.','2 ya conoce al líder 1.','El ID mayor no es la regla.'],GREEN)
arrow(d,(590,425),(630,425));arrow(d,(1170,425),(1210,425))
box(d,(60,765,1740,980),'Elegir al líder del grupo mayor ahorra actualizaciones',['Ejemplo propio: grupo A de 7 nodos + grupo B de 2 nodos.','Conservar al líder A cambia la referencia de 2 nodos, frente a 7 si se conserva B.'],BLUE)
save(im,'04-invitacion.png')

im,d=canvas('Anillo: recolectar primero, anunciar después','Figura 10-5 · Recorrido vivo 3 → 4 → 5 → 1 → 2 → 3, saltando al nodo 6')
box(d,(60,180,850,890),'Primera vuelta: descubrir',['3 → 4: {3}','4 → 5: {3, 4}','5 → 6: no responde; se intenta con 1','5 → 1: {3, 4, 5}','1 → 2: {3, 4, 5, 1}','2 → 3: {3, 4, 5, 1, 2}','','3 calcula: líder = 5'])
box(d,(950,180,1740,890),'Segunda vuelta: informar',['3 → 4: LÍDER = 5','4 → 5: LÍDER = 5','5 → 1: LÍDER = 5','1 → 2: LÍDER = 5','2 → 3: LÍDER = 5','','Variante: llevar solo el máximo.','máx(3, 4, 5, 1, 2) = 5'],GREEN)
arrow(d,(865,530),(935,530))
text(d,(60,940),['Dos vueltas = 10 entregas exitosas en este ejemplo, más intentos fallidos y sus esperas.'],30)
save(im,'05-anillo.png')
