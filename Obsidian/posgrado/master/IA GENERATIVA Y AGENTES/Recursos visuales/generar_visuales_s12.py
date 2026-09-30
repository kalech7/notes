"""Ocho figuras de estudio; Python + Pillow. PNG y SVG junto al script.

Los diagramas son propios. Cifras históricas: artículos locales ReAct, tabla 1,
y Reflexion, tabla 3. No representan mediciones de los notebooks del usuario.
"""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import html

ROOT = Path(__file__).parent
INK, BLUE, GREEN, ORANGE, RED = '#183247', '#dcecf7', '#dff2e9', '#fff0d6', '#fbe2df'


class Figura:
    def __init__(self, titulo, subtitulo):
        self.im = Image.new('RGB', (1400, 850), '#fafcfe')
        self.d = ImageDraw.Draw(self.im)
        self.svg = ['<svg xmlns="http://www.w3.org/2000/svg" width="1400" height="850" viewBox="0 0 1400 850"><rect width="1400" height="850" fill="#fafcfe"/>']
        self.texto(55, 35, titulo, 33, True)
        self.texto(55, 90, subtitulo, 21)

    def texto(self, x, y, texto, size=23, bold=False, color=INK):
        fuente = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial' + (' Bold' if bold else '') + '.ttf', size)
        for i, linea in enumerate(texto.split('\n')):
            yy = y + i * (size + 9)
            assert x + self.d.textlength(linea, font=fuente) < 1380, (linea, x)
            assert yy + size < 845, linea
            self.d.text((x, yy), linea, fill=color, font=fuente)
            self.svg.append(f'<text x="{x}" y="{yy+size}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{700 if bold else 400}" fill="{color}">{html.escape(linea)}</text>')

    def rect(self, x, y, w, h, fill):
        self.d.rounded_rectangle((x, y, x+w, y+h), 12, fill=fill, outline=INK, width=2)
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="{INK}" stroke-width="2"/>')

    def caja(self, x, y, w, h, texto, fill=BLUE, size=23):
        self.rect(x, y, w, h, fill)
        for linea in texto.split('\n'):
            font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf', size)
            assert self.d.textlength(linea, font=font) < w-30, linea
        assert len(texto.split('\n'))*(size+9) < h-15, texto
        self.texto(x+16, y+16, texto, size)

    def flecha(self, puntos, color=INK):
        self.d.line(puntos, fill=color, width=3)
        self.svg.append('<polyline points="'+' '.join(f'{x},{y}' for x,y in puntos)+f'" fill="none" stroke="{color}" stroke-width="3"/>')
        x,y=puntos[-1];a=math.atan2(y-puntos[-2][1],x-puntos[-2][0])
        tri=[(x,y),(x-14*math.cos(a-.45),y-14*math.sin(a-.45)),(x-14*math.cos(a+.45),y-14*math.sin(a+.45))]
        self.d.polygon(tri,fill=color)
        self.svg.append('<polygon points="'+' '.join(f'{u},{v}' for u,v in tri)+f'" fill="{color}"/>')

    def guardar(self, nombre, pie):
        self.texto(55, 790, pie, 18)
        self.im.save(ROOT/(nombre+'.png'))
        (ROOT/(nombre+'.svg')).write_text(''.join(self.svg)+'</svg>')


def main():
    f=Figura('49 · Del pedido al dato: el lunes completo', 'Datos del notebook: marzo tiene 4 ventas; total 2695; promedio 673,75.')
    for y,t,fill in [(160,'Usuario: ¿cuánto vendimos en marzo?',BLUE),
                     (280,'Decisión 1: pedir estadisticas_ventas(mes="2026-03"), id=c1',ORANGE),
                     (400,'Tu código: validar, ejecutar y guardar resultado de c1',GREEN),
                     (520,'Observación: {n: 4, total: 2695, promedio: 673.75}',BLUE),
                     (640,'Decisión 2: responder con las cifras recibidas',GREEN)]:
        f.caja(100,y,1200,90,t,fill)
    for y in [250,370,490,610]:f.flecha([(700,y),(700,y+30)])
    f.guardar('49-s11-notebook-traza','Una llamada de herramienta y dos decisiones del modelo. El modelo pide; el programa ejecuta.')

    f=Figura('50 · Pensar cambia contexto; actuar trae evidencia', 'ReAct intercalado: una propuesta del modelo tiene que contrastarse con el entorno.')
    f.caja(55,170,520,150,'THOUGHT\nOrganizar lo que se sabe.\nIdentificar el dato que falta.',ORANGE)
    f.caja(795,170,550,150,'ACTION\nestadisticas_ventas("2026-04")\nEl programa ejecuta la consulta.',BLUE)
    f.flecha([(575,245),(795,245)])
    f.caja(795,470,550,145,'OBSERVATION\nTotal: 1670; 3 ventas.\nDato devuelto por la herramienta.',GREEN)
    f.flecha([(1070,320),(1070,470)])
    f.caja(55,470,520,145,'SIGUIENTE DECISIÓN\nComparar 1670 con 2695.\nResponder o pedir otro dato.',ORANGE)
    f.flecha([(795,540),(575,540)])
    f.flecha([(310,470),(310,320)])
    f.texto(65,700,'Un Thought no comprueba su propia afirmación. Una Observation tampoco es infalible.',23,True)
    f.guardar('50-s12-react-contexto','Ejemplo propio con datos del notebook. No representa razonamiento privado ni una corrida de LLM.')

    f=Figura('51 · ReAct: el resultado cambia con la tarea', 'PaLM-540B, prompting del paper de 2023. Escala común de 0 a 70 en ambos paneles.')
    valores=[('HotpotQA · exact match (%)',[28.7,29.4,25.7,27.4]),('FEVER · accuracy (%)',[57.1,56.3,58.9,60.9])]
    for j,(titulo,vals) in enumerate(valores):
        y=165+j*280;f.texto(55,y,titulo,25,True)
        for i,(nombre,v) in enumerate(zip(['Standard','CoT','Act','ReAct'],vals)):
            yy=y+45+i*45;f.texto(70,yy,nombre,22);f.rect(280,yy,v*12,28,'#9fcce0' if nombre!='ReAct' else '#82b7a0');f.texto(300+v*12,yy,f'{v:.1f}',21)
        for tick in [0,10,20,30,40,50,60,70]:f.texto(275+tick*12,y+230,str(tick),18)
    f.guardar('51-s12-react-resultados','Fuente: ReAct, tabla 1, PDF 5. No comparar EM y accuracy como si midieran la misma tarea.')

    f=Figura('52 · Tres cortes complementarios', 'El control vive en el programa y se aplica antes de repetir la operación.')
    for x,t,b,fill in [(55,'TOPE DE PASOS','Como máximo 5\ndecisiones del modelo.\nAcota las vueltas.',BLUE),
                        (500,'REPETICIÓN','Misma tool + entrada,\nsin progreso relevante.\nIdentifica estancamiento.',ORANGE),
                        (945,'PRESUPUESTO','Tokens, llamadas,\ntiempo y dinero.\nAcota los recursos.',GREEN)]:
        f.texto(x,170,t,25,True);f.caja(x,235,395,230,b,fill)
    f.caja(120,580,1160,120,'Se detiene con una razón explícita y se conserva lo ocurrido.\nUna respuesta final aún necesita verificación.',RED)
    f.guardar('52-s12-tres-cortes','Un tope de iteraciones no evita que una operación se bloquee: también hacen falta timeouts.')

    f=Figura('53 · ReAct dentro; Reflexion entre intentos', 'La crítica cambia el contexto del intento siguiente; los pesos pueden permanecer fijos.')
    f.rect(55,160,1290,550,ORANGE);f.texto(80,185,'BUCLE EXTERNO · Reflexion',25,True)
    for x,txt in [(100,'Intento 1\nReAct o generación\nProducir trayectoria'),(550,'Evaluador\nComprobar contrato\nAprobado / rechazado'),(1000,'Reflexión\nExplicar el fallo\nGuardar lección')]:
        f.caja(x,280,295,175,txt,BLUE,21)
    f.flecha([(395,365),(550,365)]);f.flecha([(845,365),(1000,365)])
    f.texto(865,335,'si falla',18)
    f.flecha([(1145,455),(1145,600),(250,600),(250,455)])
    f.texto(340,620,'Nuevo intento con la crítica anterior',23,True)
    f.flecha([(695,280),(695,240),(1260,240)])
    f.texto(835,205,'Si aprueba: termina',20,True)
    f.guardar('53-s12-reflexion-anidada','El dibujo omite el máximo de intentos para claridad: el laboratorio sí lo comprueba en código.')

    f=Figura('54 · Reflexionar sin tests puede empeorar', 'GPT-4, HumanEval Rust: 50 problemas más difíciles, tabla 3 de Reflexion (2023).')
    filas=[('Modelo base',60,GREEN),('Solo tests',60,BLUE),('Solo auto-reflexión',52,RED),('Tests + auto-reflexión',68,GREEN)]
    for i,(txt,v,col) in enumerate(filas):
        y=185+i*115;f.texto(55,y,txt,24,True);f.rect(460,y,v*10,45,col);f.texto(480+v*10,y+7,f'{v} %',24)
    for v in [0,20,40,60,80]:f.texto(455+v*10,675,str(v),20)
    f.texto(450,725,'pass@1 (%) del procedimiento evaluado',23)
    f.guardar('54-s12-reflexion-ablacion','52 - 60 = -8 puntos porcentuales. No es una garantía sobre otros modelos o tareas.')

    f=Figura('55 · Planificar primero exige manejar cambios', 'Ejemplo de ventas: el plan depende de que existan datos comparables de marzo y abril.')
    f.caja(55,175,370,370,'PLANIFICADOR\n1. Consultar marzo\n2. Consultar abril\n3. Calcular variación\n4. Redactar con evidencia',ORANGE)
    f.caja(560,175,360,160,'EJECUTOR\nCumplir un paso\nRegistrar el resultado',BLUE)
    f.flecha([(425,255),(560,255)])
    f.caja(560,450,360,145,'¿PLAN AÚN VÁLIDO?\nNo hay datos de abril.\nEl cálculo no puede seguir.',RED)
    f.flecha([(740,335),(740,450)])
    f.caja(1030,450,310,145,'REPLANIFICAR\nPedir otro período\no declarar el límite',GREEN,22)
    f.flecha([(920,520),(1030,520)])
    f.flecha([(1185,595),(1185,690),(240,690),(240,545)])
    f.texto(455,710,'Máximo de replanes + presupuesto global',23,True)
    f.guardar('55-s12-plan-y-cambio','El esquema explica el mecanismo. No afirma una mejora medida de Plan-and-Execute.')

    f=Figura('56 · Contrato completo antes de ejecutar', 'La descripción ayuda a elegir; las restricciones efectivas las impone el programa.')
    cajas=[(55,160,600,155,'1. Descubrir lo permitido\nNombre, descripción y esquema de datos.',BLUE),
           (745,160,600,155,'2. Validar propuesta\nCampos, tipos, dominio y permisos.',ORANGE),
           (745,430,600,155,'3. Ejecutar con límites\nFilas máximas, tiempo y ruta autorizada.',GREEN),
           (55,430,600,155,'4. Devolver y registrar\nResultado o error útil; id y latencia.',BLUE)]
    for x,y,w,h,t,c in cajas:f.caja(x,y,w,h,t,c,22)
    f.flecha([(655,235),(745,235)]);f.flecha([(1045,315),(1045,430)]);f.flecha([(745,505),(655,505)])
    f.texto(65,665,'SQL: el esquema informa qué existe; permisos y validación limitan qué puede hacerse.',23,True)
    f.texto(65,715,'Un error útil: tabla desconocida. Tablas disponibles: sales, products, customers.',23)
    f.guardar('56-s12-contrato-completo','Nombres de tablas ilustrativos. No se inspeccionó el Lab 03 citado por las diapositivas.')


if __name__ == '__main__':
    main()
