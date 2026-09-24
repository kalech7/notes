"""Figuras originales S08: esquemas conceptuales y cálculos, no experimentos.
Requiere matplotlib y numpy. Ejecutar este archivo para regenerar PNG y SVG.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
OUT=Path(__file__).resolve().parent
BLUE='#2563eb'; TEAL='#0f766e'; ORANGE='#c2410c'; INK='#172554'; GRAY='#475569'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'figure.facecolor':'white','axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none'})
def save(fig,name):
    for ext in ['png','svg']: fig.savefig(OUT/f'{name}.{ext}',dpi=180,bbox_inches='tight',facecolor='white')
    plt.close(fig)
def base(title,sub,h=6):
    fig,ax=plt.subplots(figsize=(13,h)); ax.set(xlim=(0,13),ylim=(0,h));ax.axis('off')
    fig.suptitle(title,fontsize=20,fontweight='bold',color=INK,y=1.03)
    ax.text(0,h-.1,sub,color=GRAY,fontsize=12,va='top')
    return fig,ax
def box(ax,x,y,w,h,text,color=BLUE):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.06,rounding_size=0.12',facecolor=color+'12',edgecolor=color,lw=1.8))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',color=INK,fontsize=12,linespacing=1.5)
def arrow(ax,a,b,color=GRAY): ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'-|>','color':color,'lw':1.7,'mutation_scale':15})
fig,ax=base('RAG: preparar documentos y consultar evidencia','Dos tiempos: la ingesta se reutiliza; la consulta depende de cada pregunta.',6.5)
ax.text(.1,5.45,'1  PREPARACIÓN · al incorporar o actualizar fuentes',weight='bold',color=BLUE)
xs=[.1,3.4,6.7,10]
for x,t in zip(xs,['Documentos\ncon procedencia','Extraer y limpiar\nConservar relaciones','Dividir con sentido\nContar tokens','Representar y guardar\nTexto + índices']):box(ax,x,3.8,2.8,1.05,t)
for i in range(3):arrow(ax,(xs[i]+2.9,4.32),(xs[i+1]-.1,4.32))
ax.text(.1,2.95,'2  CONSULTA · por cada pregunta',weight='bold',color=TEAL)
for x,t in zip(xs,['Pregunta\nFormar la búsqueda','Recuperar\nCandidatos pertinentes','Seleccionar contexto\nOrden y procedencia','Generar y comprobar\nRespuesta con sustento']):box(ax,x,1.3,2.8,1.05,t,TEAL)
for i in range(3):arrow(ax,(xs[i]+2.9,1.82),(xs[i+1]-.1,1.82),TEAL)
ax.plot([11.4,11.4,4.8,4.8],[3.72,3.35,3.35,2.43],color=GRAY,lw=1.5)
arrow(ax,(4.8,2.65),(4.8,2.4))
ax.text(.1,.45,'Dependencia central: la consulta solo puede aprovechar la evidencia que el sistema conserva y hace accesible.',color=GRAY,fontsize=12)
save(fig,'20-s08-mapa-rag')
fig,ax=plt.subplots(figsize=(12,5.1),layout='constrained')
ax.barh([1], [900],height=.42,color='#cbd5e1',label='Texto disponible en el payload')
ax.barh([0], [128],height=.42,color=BLUE,label='Entrada conservada por el codificador')
ax.barh([0], [772],left=[128],height=.42,color='#fed7aa',label='No participa en ese embedding')
ax.text(450,1,'900 tokens guardados',ha='center',va='center',color=INK)
ax.text(64,0,'128',ha='center',va='center',color='white',weight='bold')
ax.text(514,0,'772 tokens omitidos en el cálculo del vector',ha='center',va='center',color=INK)
ax.set(yticks=[0,1],yticklabels=['Texto representado','Texto almacenado'],xlabel='Tokens del fragmento (supuesto didáctico)',xlim=(0,930),ylim=(-.55,1.55))
ax.set_title('Guardar todo no significa representarlo todo',loc='left',fontsize=19,weight='bold',pad=25)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.2),ncol=1,frameon=False)
fig.text(.5,-.13,'128 / 900 = 14,2 % de tokens retenidos. No es una medida de significado ni de exactitud.\nSe supone un presupuesto útil de 128; el límite real debe descontar prefijos y tokens especiales.',ha='center',color=GRAY,fontsize=11)
save(fig,'21-s08-truncamiento')
fig,(ax,bx)=plt.subplots(1,2,figsize=(13,5),gridspec_kw={'width_ratios':[1,1.2]},layout='constrained')
for y,start in zip([3,2,1],[0,8,16]):
    ax.broken_barh([(start,10)],(y-.25,.5),facecolors=BLUE if y%2 else TEAL)
    ax.text(start+5,y,f'Ventana {4-y}',ha='center',va='center',color='white')
ax.set(xlim=(0,27),ylim=(.3,3.7),yticks=[],xlabel='Posición en una secuencia ilustrativa')
ax.set_title('Tamaño 10 · solapamiento 2\nCada ventana avanza 8 unidades',fontsize=13,pad=15)
r=np.linspace(0,.75,200);bx.plot(r*100,1/(1-r),color=BLUE,lw=3)
for p in [.125,.2,80/300,.5]:
    y=1/(1-p);bx.scatter(p*100,y,color=ORANGE,zorder=3)
    bx.annotate(f'{p*100:.1f} % → ×{y:.2f}',(p*100,y),xytext=(7,{.125:48,.2:28,80/300:8,.5:8}[p]),textcoords='offset points',fontsize=10)
bx.set(xlabel='Solapamiento / tamaño (%)',ylabel='Multiplicador aproximado de ventanas',xlim=(0,76),ylim=(.95,4.25));bx.grid(alpha=.15)
bx.set_title('F ≈ 1 / (1 − proporción de solapamiento)',fontsize=13,pad=15)
fig.suptitle('Solapar protege fronteras, pero repite trabajo',fontsize=20,weight='bold',color=INK)
fig.text(.5,-.07,'Cálculo para textos largos y ventanas regulares. Los bordes alteran la razón exacta; no mide bytes ni latencia.',ha='center',fontsize=11,color=GRAY)
save(fig,'22-s08-solapamiento')
fig,ax=plt.subplots(figsize=(12,5),layout='constrained')
a=np.array([1/62,1/61]);b=np.array([1/62,0]);pos=np.array([1,0])
ax.barh(pos,a,color=BLUE,height=.42,label='Aporte BM25');ax.barh(pos,b,left=a,color=TEAL,height=.42,label='Aporte denso')
for y,v in zip(pos,a+b):ax.text(v+.0004,y,f'{v:.5f}',va='center',weight='bold',color=INK)
ax.set(yticks=pos,yticklabels=['A · puesto 2 en ambas listas','B · puesto 1 solo en BM25'],xlim=(0,.038),ylim=(-.6,1.6),xlabel='Puntaje RRF · suma de 1 / (60 + posición)')
ax.legend(loc='lower right',frameon=False);ax.grid(axis='x',alpha=.13)
ax.set_title('RRF: el acuerdo entre listas puede superar un primer puesto aislado',fontsize=17,weight='bold',loc='left',pad=20)
fig.text(.5,-.04,'Cálculo didáctico: A = 2/62; B = 1/61. El puntaje fusionado no es una probabilidad de verdad.',ha='center',color=GRAY,fontsize=11)
save(fig,'23-s08-rrf')
fig,ax=base('Dos etapas: buscar ampliamente y examinar una lista corta','Esquema del PDF: 20 candidatos y 5 fragmentos finales; no son valores óptimos universales.',5.5)
for x,w,t,c in [(0.1,2.2,'Corpus\nFragmentos\nindexados',BLUE),(3.2,2.2,'Recuperación\n20 candidatos',BLUE),(6.3,2.5,'Cross-encoder\n20 pares\ncon pregunta',TEAL),(9.8,3,'Contexto del LLM\n5 fragmentos elegidos',TEAL)]:box(ax,x,2.25,w,1.25,t,c)
for a,b in [((2.4,2.9),(3.05,2.9)),((5.5,2.9),(6.15,2.9)),((8.95,2.9),(9.65,2.9))]:arrow(ax,a,b)
box(ax,3.2,.4,5.6,.85,'Si la evidencia no está entre los candidatos,\nel reordenador no puede evaluarla.',ORANGE)
arrow(ax,(4.3,2.15),(4.3,1.4),ORANGE)
ax.text(10,1.3,'Después: generar\ny comprobar citas',ha='left',color=GRAY,linespacing=1.6)
save(fig,'24-s08-dos-etapas')
fig,ax=base('Diagnosticar: seguir el recorrido de la evidencia','Revisa en orden. El primer fallo observado orienta qué componente investigar.',8)
steps=[('¿La fuente contiene la respuesta?','No → revisar cobertura y vigencia'),('¿La extracción conserva su sentido?','No → revisar lectura, OCR y tablas'),('¿El fragmento es suficiente y está representado?','No → revisar cortes y truncamiento'),('¿La evidencia llega a los candidatos?','No → revisar búsqueda y filtros'),('¿La evidencia llega al contexto final?','No → revisar reranking y selección'),('¿La respuesta utiliza bien esa evidencia?','No → revisar generación y sustento')]
for i,(q,t) in enumerate(steps):
    y=6.45-i*1.05
    box(ax,.1,y,7.35,.72,q,BLUE if i<3 else TEAL)
    ax.text(8,y+.36,t,va='center',fontsize=12,color=ORANGE)
    arrow(ax,(7.58,y+.36),(7.9,y+.36),ORANGE)
    if i<5:arrow(ax,(3.75,y-.08),(3.75,y-.26));ax.text(4,y-.22,'Sí',fontsize=10,color=GRAY)
ax.text(.1,.15,'Conservar trazas permite separar causas: una respuesta final incorrecta, por sí sola, no identifica la etapa.',color=GRAY,fontsize=12)
save(fig,'25-s08-diagnostico')
print('6 figuras PNG + SVG generadas')

# 26. Se separa la representación para búsqueda del texto que lee el generador.
fig,ax=base('Del texto al vector, y del resultado de búsqueda al texto','RAG textual básico: el embedding localiza; el generador recibe los pasajes originales.',7.3)
box(ax,.1,3.15,2.1,1.2,'Fragmento\nTexto original',BLUE)
box(ax,3.35,4.6,2.2,1.05,'Codificador\nCalcula el vector',BLUE)
box(ax,6.6,4.6,2.2,1.05,'Índice\nVector + ID',BLUE)
box(ax,9.9,4.6,2.9,1.05,'Búsqueda\nDevuelve IDs',BLUE)
arrow(ax,(2.32,4.0),(3.22,5.1));arrow(ax,(5.68,5.12),(6.47,5.12));arrow(ax,(8.93,5.12),(9.77,5.12))
ax.text(11.35,6.42,'Pregunta vectorizada',ha='center',color=BLUE,fontsize=12)
arrow(ax,(11.35,6.14),(11.35,5.78),BLUE)
box(ax,3.35,1.85,2.2,1.05,'Registro\nID → texto y origen',TEAL)
box(ax,6.6,1.85,2.2,1.05,'Leer el texto\nDe los IDs elegidos',TEAL)
box(ax,9.9,1.85,2.9,1.05,'Prompt del generador\nPregunta + pasajes',TEAL)
arrow(ax,(2.32,3.45),(3.22,2.4),TEAL);arrow(ax,(5.68,2.37),(6.47,2.37),TEAL);arrow(ax,(8.93,2.37),(9.77,2.37),TEAL)
ax.plot([11.35,11.35,7.7],[4.47,3.7,3.7],color=GRAY,lw=1.7)
arrow(ax,(7.7,3.7),(7.7,3.02));ax.text(8.2,3.87,'Referencias al contenido',fontsize=11,color=GRAY)
ax.text(.1,.75,'El identificador une las dos rutas. No se invierte el vector para reconstruir el documento.',fontsize=13,color=INK,weight='bold')
ax.text(.1,.25,'Esquema conceptual: índice y registro pueden estar en el mismo sistema o en almacenes distintos.',fontsize=11,color=GRAY)
save(fig,'26-s08-texto-vector-texto')
print('Figura 26: separación entre búsqueda vectorial y contenido del prompt')
