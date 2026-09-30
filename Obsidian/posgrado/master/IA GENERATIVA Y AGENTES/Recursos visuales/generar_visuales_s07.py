"""Figuras conceptuales y cálculos S07. Requiere Pillow y el helper local S12.
No son tiempos medidos ni embeddings reales. Ejecutar con Python y Pillow.
"""
from pathlib import Path
import importlib.util
spec=importlib.util.spec_from_file_location('helper_s12',Path(__file__).with_name('generar_visuales_s12.py'))
h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
F=h.Figura;BLUE=h.BLUE;GREEN=h.GREEN;RED=h.RED;ORANGE=h.ORANGE

f=F('57 · IVF puede perder el vecino al otro lado','Ejemplo 1D: dos centroides; la consulta elige primero la celda derecha.')
f.caja(55,170,600,260,'CELDA IZQUIERDA\nCentroide: -1\nVecino A: -0,05\nDistancia a consulta: 0,15',BLUE)
f.caja(745,170,600,260,'CELDA DERECHA\nCentroide: +1\nConsulta: +0,10; vecino B: +0,50\nDistancia a B: 0,40',ORANGE)
f.caja(55,520,600,155,'nprobe = 1\nSolo se busca en la celda derecha.\nDevuelve B y pierde A.',RED)
f.caja(745,520,600,155,'nprobe = 2\nSe buscan ambas celdas.\nDevuelve A, el más cercano.',GREEN)
f.flecha([(655,590),(745,590)])
f.guardar('57-s07-ivf-frontera','Distancias euclídeas en 1D. La cercanía al centroide no garantiza la cercanía a cada punto.')

f=F('58 · Abrir más celdas aumenta el trabajo','N = 100000; nlist = 64; celdas equilibradas; comparaciones, no milisegundos.')
for i,(label,val) in enumerate([(str(n),64+100000/64*n) for n in [1,2,4,8,16]]+[('Exacto',100000)]):
 y=165+i*85;f.texto(55,y,'nprobe '+label if label!='Exacto' else label,23,True)
 f.rect(290,y,val/100000*820,36,BLUE if label!='Exacto' else ORANGE);f.texto(320+val/100000*820,y+3,(f'{val:,.1f}' if val%1 else f'{val:,.0f}').replace(',',' ').replace('.' , ','),22)
for v in [0,25000,50000,75000,100000]:f.texto(285+v/100000*820,705,str(v),18)
f.guardar('58-s07-ivf-comparaciones','Cálculo: nlist + (N/nlist) × nprobe. El tiempo también depende de memoria, paralelismo y acceso.')

f=F('59 · HNSW reduce candidatos mediante un grafo','Esquema simplificado: nodos superiores son también nodos de la capa base.')
for y,label,positions in [(210,'Capa superior',[220,680,1180]),(410,'Capa intermedia',[220,450,680,930,1180]),(610,'Capa base',[220,335,450,565,680,805,930,1055,1180])]:
 f.texto(55,y-45,label,23,True)
 for j,x in enumerate(positions):
  f.rect(x,y,60,55,BLUE)
  if j: f.flecha([(positions[j-1]+60,y+27),(x,y+27)])
f.flecha([(710,265),(710,410)],color='#b46711');f.flecha([(960,465),(960,610)],color='#b46711')
f.texto(60,730,'Arriba orienta el recorrido; abajo mantiene y explora un conjunto de candidatos.',22,True)
f.guardar('59-s07-hnsw-capas','No es un grafo real ni una garantía de encontrar siempre el vecino. ef_search controla la exploración.')

f=F('60 · Tres evaluaciones, tres preguntas','Buscar casi como el exacto no demuestra recuperar evidencia útil ni responder fielmente.')
for x,t,c in [(55,'ÍNDICE ANN\nReferencia: kNN exacto\n¿Coinciden los vecinos?\nEjemplo: recall = 0,98',BLUE),
              (500,'RECUPERACIÓN\nReferencia: evidencia\n¿Llegó el dato necesario?\nEjemplo: Hit Rate = 0,55',ORANGE),
              (945,'RESPUESTA\nReferencia: contexto\n¿Está respaldada?\nNo se deduce de 0,98.',GREEN)]:f.caja(x,210,395,270,t,c,21)
f.flecha([(450,340),(500,340)]);f.flecha([(895,340),(945,340)])
f.caja(115,595,1170,115,'Un índice puede reproducir perfectamente un ranking que no sirve para la pregunta.\nLa causa puede estar en texto, embeddings, filtros, contexto o generación.',RED,22)
f.guardar('60-s07-tres-evaluaciones','Números del escenario didáctico del PDF; no son mediciones propias del laboratorio.')

f=F('61 · La dimensión se paga en memoria','Un millón de vectores float32; 4 bytes por coordenada; GB decimales.')
for i,d in enumerate([384,1024,1536,3072]):
 gb=1_000_000*d*4/1e9;y=190+i*120;f.texto(55,y,f'd = {d}',26,True)
 f.rect(320,y,gb/13*780,48,BLUE);f.texto(345+gb/13*780,y+8,f'{gb:.3f} GB',23)
for v in [0,3,6,9,12]:f.texto(315+v/13*780,705,str(v),20)
f.guardar('61-s07-dimension-memoria','Solo vectores: faltan grafo/listas, IDs, payload, metadatos y sobrecarga. 3072/384 = 8.')

f=F('62 · El punto conecta vector y documento','Colección: declara dimensión y métrica. Cada punto añade identificador y payload.')
f.caja(55,170,580,210,'PUNTO\nid: faq-17\nvector: [0,2; -0,1; ...]\npayload: texto, tema, fuente',BLUE,24)
f.caja(770,170,570,210,'CONSULTA\nvector de la pregunta\nfiltro: tema = pagos\nlímite de resultados: 2',ORANGE,24)
f.flecha([(345,380),(345,525)])
f.caja(55,525,580,150,'SELECCIÓN\nEl filtro define el subconjunto.\nLa similitud ordena candidatos.',GREEN,24)
f.caja(770,525,570,150,'RESULTADO\nid + puntaje + payload permitido\nDespués se construye el contexto.',BLUE,23)
f.flecha([(1055,380),(1055,450),(345,450),(345,525)]);f.flecha([(635,600),(770,600)])
f.guardar('62-s07-vector-payload-filtro','Esquema propio. IDs y metadatos pueden apuntar a texto externo; el payload no crea significado.')
