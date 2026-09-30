"""Figuras conceptuales de S13. Ejecutar con Python y Pillow. PNG y SVG junto al script."""
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
    f=Figura('01 · Producto de conexiones, suma de componentes', 'Ejemplo conceptual: 3 aplicaciones y 4 sistemas. No es una medición de tiempo o costo.')
    f.texto(55,160,'CONEXIONES PROPIAS: 3 × 4 = 12',25,True)
    f.texto(755,160,'COMPONENTES REUTILIZABLES: 3 + 4 = 7',25,True)
    for i in range(3):
        y=240+i*145
        f.caja(55,y,190,85,['Agente','IDE','Soporte'][i],BLUE,23)
    for j in range(4):
        y=220+j*115
        f.caja(440,y,200,75,['Ventas','RAG','Calendario','Incidencias'][j],GREEN,22)
    for i in range(3):
        for j in range(4): f.flecha([(245,282+i*145),(440,257+j*115)])
    for i in range(3):
        y=240+i*145;f.caja(755,y,210,85,['Agente + cliente','IDE + cliente','Soporte + cliente'][i],BLUE,21)
        f.flecha([(965,y+42),(1080,y+42)])
    f.rect(1080,210,50,435,ORANGE)
    f.texto(1040,680,'Mismo protocolo',20,True)
    for j in range(4):
        y=220+j*115;f.caja(1170,y,175,75,['S. ventas','S. RAG','S. agenda','S. incidencias'][j],GREEN,21)
        f.flecha([(1130,y+37),(1170,y+37)])
    f.texto(55,715,'Se cuentan aristas a la izquierda y componentes a la derecha: son unidades diferentes.',23,True)
    f.guardar('01-integraciones-y-piezas','Supuesto didáctico: cada aplicación usa cada sistema; se cuenta un proveedor por sistema.')

    f=Figura('02 · Añadir la herramienta siguiente', 'M=1 y N=3: 3 integraciones frente a 4 piezas. La ventaja buscada es cambiar menos código.')
    f.texto(55,175,'REGISTRO FIJO',25,True)
    f.caja(55,240,370,205,'Aparece convertir_moneda\nEditar registro\nAñadir contrato al modelo\nRevisar despacho del agente',RED,22)
    f.flecha([(425,340),(555,340)])
    f.caja(555,260,790,150,'El conocimiento de las tools está en el agente.\nLa nueva capacidad obliga a revisar esa dependencia.',ORANGE,24)
    f.texto(55,505,'DESCUBRIMIENTO',25,True)
    f.caja(55,565,370,145,'Publicar nueva capacidad\nConfigurar el servidor\nVolver a descubrir catálogo',GREEN,22)
    f.flecha([(425,635),(555,635)])
    f.caja(555,565,790,145,'El cliente recibe el contrato y sabe a dónde enviarlo.\nEl mismo agente consume el catálogo actualizado.',BLUE,24)
    f.guardar('02-herramienta-siguiente','Cambiar configuración y probar el sistema sigue siendo necesario. El código del agente puede conservarse.')

    f=Figura('03 · Un host, dos clientes y dos servidores', 'Un servidor puede publicar varias tools. El cliente MCP de cada servidor mantiene su frontera.')
    f.rect(55,160,730,540,BLUE);f.texto(85,180,'HOST · aplicación que coordina',26,True)
    f.caja(85,255,300,220,'Modelo\nRecibe herramientas\nPropone nombre\ny argumentos',ORANGE,24)
    f.caja(470,245,265,145,'Cliente A\nDescubre y adapta\nEnruta hacia ventas',GREEN,22)
    f.caja(470,485,265,145,'Cliente B\nDescubre y adapta\nEnruta hacia cambio',GREEN,22)
    f.flecha([(385,315),(470,315)]);f.flecha([(385,435),(425,435),(425,555),(470,555)])
    f.caja(970,245,375,160,'Servidor A · ventas\nconsultar_ventas\nestadisticas_ventas',BLUE,24)
    f.caja(970,485,375,160,'Servidor B · cambio\nconvertir_moneda\nAquí se ejecuta la función',BLUE,24)
    f.flecha([(735,315),(970,315)]);f.flecha([(735,555),(970,555)])
    f.texto(70,720,'La propuesta sale del modelo; la ejecución ocurre en código local o remoto.',24,True)
    f.guardar('03-host-clientes-servidores','M cuenta aplicaciones. N debe definirse consistentemente como proveedores o sistemas de integración.')

    f=Figura('04 · Dos contratos y un adaptador', 'El contrato publicado debe convertirse al formato que espera la llamada al modelo.')
    f.caja(55,180,360,220,'SERVIDOR\nname\ndescription\ninputSchema',GREEN,26)
    f.flecha([(415,290),(525,290)])
    f.caja(525,180,340,220,'CLIENTE / ADAPTADOR\nValidar catálogo\nTraducir formato\nGuardar ruta de ejecución',ORANGE,23)
    f.flecha([(865,290),(975,290)])
    f.caja(975,180,370,220,'API DEL MODELO\nRecibe contratos\nDevuelve propuesta\nNo ejecuta la función',BLUE,24)
    f.caja(55,520,600,145,'FUNCTION CALLING\nModelo → aplicación\nCómo se expresa la petición',BLUE,24)
    f.caja(745,520,600,145,'MCP\nCliente → servidor\nCómo se publica, descubre e invoca',GREEN,24)
    f.texto(55,720,'El catálogo llega al ejecutar. Un nombre descubierto necesita también una ruta de despacho.',23,True)
    f.guardar('04-contratos-y-adaptador','La ubicación del adaptador es una decisión arquitectónica del ejemplo, no una obligación de MCP.')

    f=Figura('05 · Acciones, datos y plantillas', 'Las tres primitivas tienen funciones diferentes dentro de la aplicación.')
    for x,title,txt,col in [(55,'TOOLS','consultar_ventas(mes)\nUna operación invocable\nDevuelve resultado\nPuede tener efectos',BLUE),
                             (500,'RESOURCES','reporte://ventas/marzo\nContenido identificable\nSe incorpora al contexto\nNo es una orden',GREEN),
                             (945,'PROMPTS','comparar_periodos\nPlantilla reutilizable\nOrganiza mensajes\nNo prueba una respuesta',ORANGE)]:
        f.texto(x,190,title,27,True);f.caja(x,265,395,300,txt,col,23)
    f.caja(140,635,1120,95,'El host decide qué capacidades usar y qué información llega al modelo.',BLUE,25)
    f.guardar('05-tres-primitivas','Ejemplos propios. Un servidor puede ofrecer una o varias de estas categorías.')

    f=Figura('06 · Tres agentes, tres criterios de comprobación', 'El mismo bucle puede trabajar con herramientas y evidencias diferentes.')
    rows=[('ANALISTA','Consulta → cálculo → gráfico','Recalcular sobre datos correctos',BLUE),
          ('CÓDIGO','Archivos → ejecución → tests','Comprobar casos y contrato',GREEN),
          ('INVESTIGACIÓN','Búsqueda → fragmentos → informe','Vincular afirmación y evidencia',ORANGE)]
    for i,(title,flow,check,col) in enumerate(rows):
        y=185+i*175;f.texto(55,y,title,25,True)
        f.caja(300,y-5,510,125,flow,col,23);f.flecha([(810,y+55),(875,y+55)])
        f.caja(875,y-5,470,125,check,col,22)
    f.caja(120,720,1160,55,'Una respuesta coherente puede fallar la comprobación.',RED,24)
    f.guardar('06-verificadores','Tests deterministas no equivalen a cobertura completa; una cita tampoco demuestra causalidad.')

    f=Figura('07 · Del catálogo a una acción permitida', 'Descubrir una capacidad inicia una decisión; no concede autorización sobre los datos.')
    steps=[('1. Descubrir catálogo','Identificar nombre, entrada y proveedor',BLUE),
           ('2. Seleccionar contrato','Ofrecer solo capacidades pertinentes',ORANGE),
           ('3. Validar petición','Comprobar argumentos, alcance y permiso',GREEN),
           ('4. Ejecutar y registrar','Aplicar límites y guardar la evidencia',BLUE)]
    for i,(title,txt,col) in enumerate(steps):
        y=175+i*135;f.caja(100,y,1200,95,title+'\n'+txt,col,23)
        if i<3:f.flecha([(700,y+95),(700,y+135)])
    f.texto(100,745,'La descripción externa informa sobre la tool; no cambia las reglas del host.',24,True)
    f.guardar('07-descubrimiento-y-confianza','Ejemplo propio de responsabilidades. La política efectiva vive en controles de la aplicación y del servicio.')

if __name__ == '__main__':
    main()
