"""Diagramas didácticos originales del capítulo 11. Ejecutar con Python y Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

OUT = Path(__file__).resolve().parent
INK = '#17324d'
MUTED = '#526b80'
BLUE = '#e3effb'
GREEN = '#e4f2e9'
GOLD = '#fff0d1'
RED = '#fbe3df'
GREY = '#edf0f4'
ALERT = '#a44336'
# Series del gráfico de estrellas: paleta categórica validada (azul y naranja).
S_CAPAS = '#2a78d6'
S_MODULAR = '#eb6834'
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
BOLD = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
MONO = '/System/Library/Fonts/Menlo.ttc'


def font(n=28, bold=False, mono=False):
    if mono:
        return ImageFont.truetype(MONO, n)
    return ImageFont.truetype(BOLD if bold else FONT, n)


def canvas(title, subtitle, h=1000):
    global im, d, H
    H = h
    im = Image.new('RGB', (1600, h), 'white')
    d = ImageDraw.Draw(im)
    text(60, 40, title, 42, True)
    text(60, 104, subtitle, 25, False, MUTED)
    d.line((60, 153, 1540, 153), fill='#bccddb', width=2)


def text(x, y, s, n=28, b=False, c=INK, mono=False):
    d.multiline_text((x, y), s, font=font(n, b, mono), fill=c, spacing=10)


def box(x, y, w, h, s, color=BLUE, n=28, dashed=False, bold=False, mono=False, outline=INK):
    if dashed:
        d.rounded_rectangle((x, y, x + w, y + h), radius=16, fill=color)
        dashed_rect(x, y, w, h, outline)
    else:
        d.rounded_rectangle((x, y, x + w, y + h), radius=16, fill=color, outline=outline, width=2)
    if not s:
        return
    f = font(n, bold, mono)
    bb = d.multiline_textbbox((0, 0), s, font=f, spacing=9, align='center')
    assert bb[2] <= w - 20, (s, bb, w)
    assert bb[3] - bb[1] <= h - 15, (s, bb, h)
    d.multiline_text((x + (w - bb[2]) / 2, y + (h - (bb[3] - bb[1])) / 2 - bb[1]), s, font=f,
                     fill=INK, spacing=9, align='center')


def dashed_rect(x, y, w, h, c=INK):
    for (a, b) in [((x, y), (x + w, y)), ((x + w, y), (x + w, y + h)),
                   ((x + w, y + h), (x, y + h)), ((x, y + h), (x, y))]:
        dashed_line(a, b, c, 3)


def dashed_line(a, b, c=INK, width=4):
    length = math.dist(a, b)
    for k in range(0, int(length), 18):
        u = k / length
        v = min((k + 9) / length, 1)
        d.line((a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u,
                a[0] + (b[0] - a[0]) * v, a[1] + (b[1] - a[1]) * v), fill=c, width=width)


def arrow(points, c=INK, dashed=False, both=False):
    for a, b in zip(points, points[1:]):
        if dashed:
            dashed_line(a, b, c)
        else:
            d.line((a, b), fill=c, width=4)
    head(points[-2], points[-1], c)
    if both:
        head(points[1], points[0], c)


def head(a, b, c):
    theta = math.atan2(b[1] - a[1], b[0] - a[0])
    d.polygon([b, (b[0] - 18 * math.cos(theta - .5), b[1] - 18 * math.sin(theta - .5)),
               (b[0] - 18 * math.cos(theta + .5), b[1] - 18 * math.sin(theta + .5))], fill=c)


def cylinder(x, y, w, h, label, color=GREY):
    e = 26
    d.rectangle((x, y + e / 2, x + w, y + h - e / 2), fill=color)
    d.ellipse((x, y + h - e, x + w, y + h), fill=color, outline=INK, width=2)
    d.rectangle((x + 2, y + e / 2, x + w - 2, y + h - e / 2), fill=color)
    d.line((x, y + e / 2, x, y + h - e / 2), fill=INK, width=2)
    d.line((x + w, y + e / 2, x + w, y + h - e / 2), fill=INK, width=2)
    d.ellipse((x, y, x + w, y + e), fill=color, outline=INK, width=2)
    f = font(23)
    bb = d.textbbox((0, 0), label, font=f)
    d.text((x + (w - bb[2]) / 2, y + h / 2 - 6), label, font=f, fill=INK)


def save(name, foot):
    text(60, H - 55, foot, 22, False, MUTED)
    im.save(OUT / (name + '.png'))


# 1 · Namespaces: el tercer nodo decide el criterio de agrupación
canvas('El tercer nodo del namespace revela el criterio',
       'Capítulo 11 · Elaboración propia sobre las páginas impresas 165–166', 1000)
text(80, 190, 'ARQUITECTURA POR CAPAS', 30, True)
text(860, 190, 'MONOLITO MODULAR', 30, True)
for x, parts, colors in [
    (80, ['com', 'app', 'presentation', 'customer', 'profile'], [GREY, GREY, GOLD, GREEN, GREEN]),
    (860, ['com', 'app', 'customer', 'profile'], [GREY, GREY, GOLD, GREEN]),
]:
    cx = x
    for p, col in zip(parts, colors):
        w = int(d.textbbox((0, 0), p, font=font(24, mono=True))[2]) + 30
        box(cx, 250, w, 62, p, col, 24, mono=True)
        cx += w + 8
text(80, 335, 'Tercer nodo = preocupación técnica (la capa).', 25, False, INK)
text(860, 335, 'Tercer nodo = dominio (cliente).', 25, False, INK)
box(80, 400, 640, 400, '', BLUE)
text(105, 420, 'Primero la técnica, después el negocio', 26, True)
for i, (layer, y) in enumerate([('presentation', 480), ('business', 590), ('persistence', 700)]):
    box(110, y, 580, 90, '', GREY)
    text(130, y + 12, layer + '/', 24, True, INK, True)
    text(130, y + 50, 'customer · order · payment · …', 22, False, MUTED)
box(860, 400, 660, 400, '', GREEN)
text(885, 420, 'Primero el negocio, dentro la técnica', 26, True)
box(890, 480, 290, 300, '', 'white')
text(910, 495, 'customer/', 24, True, INK, True)
text(910, 545, 'profile/', 22, False, INK, True)
text(940, 590, 'presentation', 21, False, MUTED, True)
text(940, 630, 'business', 21, False, MUTED, True)
text(910, 680, 'address/', 22, False, INK, True)
box(1200, 480, 290, 140, '', 'white')
text(1220, 495, 'order/', 24, True, INK, True)
text(1220, 545, 'placement/ …', 22, False, MUTED, True)
box(1200, 640, 290, 140, '', 'white')
text(1220, 655, 'payment/', 24, True, INK, True)
text(1220, 705, 'card/ · paypal/', 22, False, MUTED, True)
box(80, 830, 1440, 90, 'Mismo código, distinto primer criterio: dónde busca quien cambia «perfil del cliente».', GOLD, 27)
save('c11-01-namespaces', 'Dorado = nodo que fija el criterio de partición. Verde = dominio. Las capas internas por dominio son opcionales.')


# 2 · Estructura monolítica frente a modular
canvas('Dos formas de construir el mismo monolito modular',
       'Capítulo 11 · Elaboración propia sobre las figuras 11-2 y 11-3', 1080)
text(80, 185, 'ESTRUCTURA MONOLÍTICA', 30, True)
text(860, 185, 'ESTRUCTURA MODULAR', 30, True)
box(80, 240, 660, 330, '', BLUE)
text(105, 255, 'Un repositorio', 26, True)
mods = ['pedidos/', 'inventario/', 'pagos/', 'notificación/', 'cumplimiento/', 'envíos/']
for i, m in enumerate(mods):
    box(110 + (i % 2) * 310, 310 + (i // 2) * 82, 290, 66, m, 'white', 23, mono=True)
for i, m in enumerate(['pedidos.jar', 'pagos.jar', 'envíos.jar']):
    box(860 + i * 225, 240, 205, 180, '', GREEN)
    text(875 + i * 225, 255, 'Repositorio', 21, True)
    box(875 + i * 225, 320, 175, 70, m, 'white', 20, mono=True)
text(860, 445, 'Cada módulo compila por separado y produce', 24)
text(860, 480, 'un artefacto propio (JAR, DLL…).', 24)
arrow([(410, 575), (410, 650)])
arrow([(1195, 525), (1195, 650)])
box(80, 655, 660, 80, 'Compilación única del código completo', GREY, 25)
box(860, 655, 670, 80, 'Ensamblado de los artefactos al desplegar', GREY, 25)
arrow([(410, 740), (720, 800)])
arrow([(1195, 740), (880, 800)])
box(560, 805, 480, 95, 'Una única unidad de despliegue\n(WAR, EAR, ejecutable .NET…)', GOLD, 25, bold=True)
text(80, 930, 'Sencillo, pero la frontera depende de disciplina y gobierno.', 24, False, ALERT)
text(860, 930, 'Fronteras más fuertes; comunicar exige contratos.', 24, False, ALERT)
save('c11-02-estructuras', 'Ambas opciones terminan en un solo despliegue: la diferencia está en cómo se escribe y compila el código.')


# 3 · Tres maneras de comunicar módulos
canvas('Cómo se hablan los módulos y dónde queda el acoplamiento',
       'Capítulo 11 · Elaboración propia sobre las figuras 11-4 y 11-5 y el texto de la página 169', 1050)
panels = [(60, 'A · Punto a punto'), (560, 'B · Interfaz compartida'), (1060, 'C · Mediador')]
for x, t in panels:
    box(x, 190, 480, 620, '', GREY)
    text(x + 20, 205, t, 27, True)
# A
box(90, 330, 190, 90, 'Pedidos', BLUE, 25)
box(330, 270, 180, 90, 'Inventario', GREEN, 25)
box(330, 420, 180, 90, 'Pagos', GREEN, 25)
arrow([(280, 355), (330, 315)])
arrow([(280, 395), (330, 465)])
text(90, 560, 'Pedidos crea clases de los\notros módulos y llama a sus\nmétodos. Muy cómodo: nada\nimpide importar cualquier\nclase interna.', 23)
# B
box(590, 280, 190, 90, 'Pedidos', BLUE, 25)
box(820, 280, 190, 90, 'Inventario', GREEN, 25)
box(660, 440, 280, 90, 'contratos.jar\n(interfaces)', GOLD, 23)
arrow([(685, 370), (740, 440)])
arrow([(915, 370), (860, 440)])
text(590, 560, 'Cada módulo compila solo\ncontra la interfaz. Con muchos\ncontratos y versiones aparece\nel «JAR/DLL Hell».', 23)
# C
box(1175, 260, 250, 85, 'Mediador', GOLD, 26, bold=True)
for i, m in enumerate(['Pedidos', 'Pagos', 'Inventario']):
    box(1080 + i * 150, 430, 140, 85, m, GREEN, 22)
    arrow([(1300, 345), (1150 + i * 150, 430)])
text(1085, 560, 'Los módulos no se conocen\nentre sí, pero todos dependen\ndel mediador, que necesita\nla API de cada uno.', 23)
box(60, 840, 1480, 110, 'Ninguna opción elimina el acoplamiento: A lo reparte entre pares, B lo concentra en contratos\ny C lo concentra en el mediador. Pocas comunicaciones es el objetivo en cualquier caso.', GOLD, 26)
save('c11-03-comunicacion', 'Flecha = «depende de / invoca a». Todas las cajas viven dentro del mismo despliegue.')


# 4 · Topologías de datos
canvas('Un despliegue no obliga a una sola base de datos',
       'Capítulo 11 · Elaboración propia sobre la figura 11-6 (página 170)', 1000)
text(80, 185, 'BASE DE DATOS MONOLÍTICA', 30, True)
text(860, 185, 'BASES POR MÓDULO', 30, True)
box(80, 240, 640, 330, '', BLUE)
names = ['Pedidos', 'Pagos', 'Envíos', 'Recetas', 'Inventario', 'Clientes']
for i, n in enumerate(names):
    box(110 + (i % 3) * 200, 280 + (i // 3) * 130, 180, 100, n, 'white', 23)
arrow([(400, 575), (400, 640)])
cylinder(290, 645, 220, 130, 'Base común')
box(860, 240, 660, 330, '', BLUE)
for i, n in enumerate(['Pedidos', 'Pagos', 'Envíos', 'Clientes', 'Recetas', 'Inventario']):
    col = GREEN if n in ('Recetas', 'Inventario') else 'white'
    box(890 + (i % 3) * 205, 280 + (i // 3) * 130, 185, 100, n, col, 23)
arrow([(1040, 575), (1040, 640)])
cylinder(930, 645, 220, 130, 'Base común')
arrow([(1195, 575), (1260, 640)])
cylinder(1200, 645, 150, 130, 'Recetas')
arrow([(1400, 575), (1430, 640)])
cylinder(1370, 645, 150, 130, 'Invent.')
text(80, 810, '+ menos comunicación: los datos se comparten\n− el esquema común acopla a los módulos', 24)
text(860, 810, '+ datos propios para módulos independientes\n− consultas cruzadas pasan por el módulo dueño', 24)
save('c11-04-datos', 'Rectángulo azul = la única unidad de despliegue. Verde = módulos con datos propios. Cilindro = base de datos.')


# 5 · Contar puntos de acoplamiento
canvas('Contar dependencias entre módulos con un límite de 5',
       'Capítulo 11 · Ejemplo propio para comprender el ejemplo 11-3 (página 173)', 1100)
pos = {
    'Pedidos': (560, 380), 'Inventario': (160, 230), 'Pagos': (160, 560),
    'Notificación': (560, 690), 'Cumplimiento': (960, 230), 'Envíos': (960, 560),
}
W, Hh = 230, 80
edges = [('Pedidos', 'Inventario'), ('Pedidos', 'Pagos'), ('Pedidos', 'Notificación'),
         ('Pedidos', 'Cumplimiento'), ('Pedidos', 'Envíos'), ('Cumplimiento', 'Inventario'),
         ('Cumplimiento', 'Envíos'), ('Envíos', 'Notificación'), ('Pagos', 'Notificación'),
         ('Notificación', 'Pedidos')]


def edge_point(a, b):
    (ax, ay), (bx, by) = pos[a], pos[b]
    ax, ay, bx, by = ax + W / 2, ay + Hh / 2, bx + W / 2, by + Hh / 2
    dx, dy = bx - ax, by - ay
    t = min((W / 2 + 6) / abs(dx) if dx else 9e9, (Hh / 2 + 6) / abs(dy) if dy else 9e9)
    return (ax + dx * t, ay + dy * t), (bx - dx * t, by - dy * t)


for a, b in edges:
    p, q = edge_point(a, b)
    if (a, b) == ('Notificación', 'Pedidos'):
        p, q = (p[0] + 40, p[1]), (q[0] + 40, q[1])
        arrow([p, q], ALERT)
    elif (a, b) == ('Pedidos', 'Notificación'):
        p, q = (p[0] - 40, p[1]), (q[0] - 40, q[1])
        arrow([p, q])
    else:
        arrow([p, q])
for n, (x, y) in pos.items():
    box(x, y, W, Hh, n, RED if n == 'Pedidos' else GREEN, 25)
tx = 1250
text(tx, 190, 'Módulo', 23, True)
text(tx + 170, 190, 'E  S  Total', 23, True)
rows = [('Pedidos', 1, 5), ('Inventario', 2, 0), ('Pagos', 1, 1), ('Notificación', 3, 1),
        ('Cumplimiento', 1, 2), ('Envíos', 2, 1)]
for i, (n, e, s) in enumerate(rows):
    y = 240 + i * 52
    c = ALERT if e + s > 5 else INK
    text(tx, y, n, 22, e + s > 5, c)
    text(tx + 175, y, f'{e}  {s}   {e + s}', 22, e + s > 5, c, True)
text(tx, 570, 'E = entrantes\nS = salientes\nSuma de totales = 20\n= 2 × 10 flechas', 21, False, MUTED)
box(60, 850, 1480, 150, 'Pedidos suma 6 > 5: la regla lanza una alerta. La flecha roja (Notificación → Pedidos)\ncierra además un ciclo. La alerta no dice qué cambiar: obliga a revisar si Pedidos\nconcentra demasiadas responsabilidades o si faltan fronteras mejores.', GOLD, 25)
save('c11-05-conteo', 'Cada flecha cuenta una vez como saliente en su origen y otra como entrante en su destino. Datos inventados.')


# 6 · Estrellas: capas frente a monolito modular
canvas('Qué cambia al pasar de capas a monolito modular',
       'Capítulo 11 · Valoraciones de las figuras 10-6 y 11-7 del libro (1 = débil, 5 = fortaleza)', 1150)
chars = ['Simplicidad', 'Modularidad', 'Mantenibilidad', 'Testabilidad', 'Desplegabilidad',
         'Evolución', 'Capacidad de respuesta', 'Escalabilidad', 'Elasticidad', 'Tolerancia a fallos']
capas = [5, 1, 1, 2, 1, 1, 3, 1, 1, 1]
modular = [5, 2, 2, 2, 2, 2, 3, 1, 1, 1]
x0, unit, bar = 470, 180, 22
# leyenda
d.rounded_rectangle((470, 180, 500, 200), radius=4, fill=S_CAPAS)
text(512, 176, 'Por capas (figura 10-6)', 23)
d.rounded_rectangle((850, 180, 880, 200), radius=4, fill=S_MODULAR)
text(892, 176, 'Monolito modular (figura 11-7)', 23)
for k in range(1, 6):
    gx = x0 + k * unit
    d.line((gx, 225, gx, 225 + len(chars) * 78), fill='#e1e7ee', width=1)
    text(gx - 7, 225 + len(chars) * 78 + 8, str(k), 21, False, MUTED)
d.line((x0, 225, x0, 225 + len(chars) * 78), fill='#9fb0c0', width=2)
for i, (cname, a, b) in enumerate(zip(chars, capas, modular)):
    y = 240 + i * 78
    bb = d.textbbox((0, 0), cname, font=font(24))
    changed = a != b
    text(x0 - 20 - bb[2], y + 10, cname, 24, changed)
    d.rounded_rectangle((x0, y, x0 + a * unit, y + bar), radius=4, fill=S_CAPAS)
    d.rounded_rectangle((x0, y + bar + 2, x0 + b * unit, y + 2 * bar + 2), radius=4, fill=S_MODULAR)
    if changed:
        text(x0 + b * unit + 14, y + 12, '+1', 24, True, INK)
text(1440, 255, 'En negrita:\nlas cuatro\nque suben', 21, False, MUTED)
save('c11-06-estrellas', 'Costo ($), quanta (1) y valoraciones operativas coinciden. Cambian la partición (técnica → dominio) y cuatro valoraciones.')


# 7 · EasyMeals, figura 11-8 en español
canvas('EasyMeals: un restaurante pequeño como monolito modular',
       'Capítulo 11 · Recreación didáctica de la figura 11-8 (página 178)', 1080)
box(195, 190, 330, 100, 'Cliente HTTP\n(clientes)', GREY, 25)
box(640, 190, 400, 100, 'Cliente HTTP\n(personal del restaurante)', GREY, 25)
box(120, 350, 1360, 440, '', BLUE)
text(1180, 362, 'Una unidad de despliegue', 22, True, MUTED)
box(170, 410, 380, 350, '', 'white', dashed=True)
text(190, 728, 'Atención al cliente', 21, True, MUTED)
box(230, 460, 260, 95, 'Realizar pedido', GREEN, 25)
box(230, 630, 260, 95, 'Procesar pago', GREEN, 25)
box(640, 410, 800, 350, '', 'white', dashed=True)
text(660, 728, 'Operación del restaurante', 21, True, MUTED)
box(690, 460, 300, 95, 'Preparar pedido', GREEN, 25)
box(1060, 460, 330, 95, 'Recetas', GREEN, 25)
box(690, 630, 300, 95, 'Entrega', GREEN, 25)
box(1060, 630, 330, 95, 'Inventario de\ningredientes', GREEN, 24)
arrow([(360, 290), (360, 460)])
arrow([(840, 290), (840, 460)])
arrow([(360, 555), (360, 630)])
arrow([(490, 507), (690, 507)])
arrow([(840, 555), (840, 630)])
arrow([(800, 790), (800, 850)])
cylinder(700, 855, 200, 120, 'Base de datos')
save('c11-07-easymeals', 'Recuadros punteados = agrupación por público. Flechas = colaboración principal. Una base de datos para todo el sistema.')


# 8 · Un módulo contiene componentes
canvas('Un módulo contiene varios componentes: EasyMeals',
       'Capítulo 11 · Elaboración propia con los namespaces de las páginas 178–180', 1120)
cards = [
    ('placeorder', ['menu', 'shoppingcart', 'customerdata', 'paymentdata', 'checkout']),
    ('payment', ['creditcard', 'debitcard', 'paypal']),
    ('prepareorder', ['displayorder', 'ready']),
    ('delivery', ['assign', 'issues', 'complete']),
    ('recipes', ['view', 'maintenance']),
    ('inventory', ['maintenance', 'forecasting', 'ordering', 'suppliers', 'invoices']),
]
for i, (m, comps) in enumerate(cards):
    x = 60 + (i % 3) * 500
    y = 190 + (i // 3) * 400
    box(x, y, 470, 370, '', BLUE)
    text(x + 20, y + 18, 'com.easymeals.', 21, False, MUTED, True)
    text(x + 20, y + 50, m, 27, True, INK, True)
    for j, c in enumerate(comps):
        col = GOLD if (m == 'inventory' and c == 'forecasting') else 'white'
        box(x + 35, y + 100 + j * 52, 400, 44, '.' + c, col, 21, mono=True)
box(60, 990, 1480, 60, 'Dorado: componente de IA que pronostica ventas para comprar ingredientes cada semana.', GOLD, 24)
save('c11-08-componentes', 'Cada tarjeta es un módulo (dominio); cada fila, un componente dentro de ese módulo.')

print('Diagramas generados en', OUT)
