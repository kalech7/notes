"""Figuras didácticas de sesión 09. Ejecutar con Python y Matplotlib.
La figura 33 transcribe la diapositiva 23; las demás son esquemas o cálculos propios.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'none'})
BLUE='#2466a2'; GREEN='#25805d'; RED='#ba4545'; ORANGE='#bf761b'; INK='#19334b'; GRAY='#e7edf2'
def canvas(title,sub='',h=6):
 f,a=plt.subplots(figsize=(12,h)); f.patch.set_facecolor('white'); a.set(xlim=(0,12),ylim=(0,6)); a.axis('off')
 f.suptitle(title,x=.05,ha='left',fontsize=20,fontweight='bold',color=INK,y=.97)
 if sub:f.text(.05,.88,sub,fontsize=11,color='#536577')
 f.subplots_adjust(top=.82,bottom=.08,left=.04,right=.96)
 return f,a
def box(a,x,y,w,h,text,color=BLUE,fill='#f1f6fb',fs=12):
 a.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.04,rounding_size=0.10',facecolor=fill,edgecolor=color,linewidth=1.6))
 a.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,color=INK,linespacing=1.45)
def arrow(a,x1,y1,x2,y2,color=BLUE):
 a.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='->',color=color,lw=2,shrinkA=5,shrinkB=5))
def save(f,name):
 f.savefig(OUT/(name+'.png'),dpi=180,facecolor='white'); f.savefig(OUT/(name+'.svg'),facecolor='white'); plt.close(f)
f,a=canvas('Tres evaluaciones, tres referencias','Diagrama conceptual · Una etapa correcta no garantiza que la siguiente lo sea')
for x,title,desc in [(0.2,'1. ÍNDICE','¿Reproduce los vecinos\nde la búsqueda exacta?'),(4.2,'2. RECUPERACIÓN','¿Llega la evidencia\nque necesita la pregunta?'),(8.2,'3. GENERACIÓN','¿La respuesta usa\nbien esa evidencia?')]:
 box(a,x,3.1,3.5,2,title+'\n\n'+desc)
for x,t in [(.2,'Referencia:\nkNN exacto'),(4.2,'Referencia:\nrelevancia anotada'),(8.2,'Referencia:\ncontexto + rúbrica')]:
 box(a,x,.6,3.5,1.5,t,color=GREEN,fill='#eef7f2');arrow(a,x+1.75,3.1,x+1.75,2.1,GREEN)
arrow(a,3.7,4.1,4.2,4.1);arrow(a,7.7,4.1,8.2,4.1)
save(f,'27-s09-tres-evaluaciones')
f,axs=plt.subplots(1,2,figsize=(12,5.4),gridspec_kw={'width_ratios':[1.2,1]},layout='constrained')
f.suptitle('Presencia, cobertura y posición miden cosas diferentes',fontsize=18,fontweight='bold',color=INK)
a=axs[0];a.set(xlim=(.2,5.8),ylim=(0,4));a.axis('off');a.text(.3,3.6,'Ejemplo propio · Relevantes: A y B',fontsize=13)
for i,label in enumerate(['X','A','Y','B','Z'],1):
 box(a,i-.38,2.05,.76,.8,label,color=GREEN if label in 'AB' else '#96a4b0',fill='#dcefe4' if label in 'AB' else GRAY,fs=15)
 a.text(i,1.65,f'{i}',ha='center',color=INK)
a.axvline(3.5,ymin=.36,ymax=.76,color=ORANGE,ls='--',lw=2);a.text(3.55,3,'corte k = 3',color=ORANGE,fontsize=10)
a.text(.3,.65,'Top-3:  Hit = 1  ·  Recall = ½  ·  RR = ½\nTop-5:  Hit = 1  ·  Recall = 1  ·  RR = ½',linespacing=1.8,fontsize=12)
a=axs[1];x=np.arange(1,6);a.plot(x,1/x,'o-',color=BLUE,lw=2,ms=8);a.set(xticks=x,ylim=(0,1.14),xlabel='Puesto del primer relevante',ylabel='RR = 1 / puesto');a.grid(alpha=.2)
for i,v in zip(x,1/x):a.annotate(f'{v:.2f}',(i,v),xytext=(0,10),textcoords='offset points',ha='center',fontsize=10)
save(f,'28-s09-metricas-y-posicion')
f,a=canvas('La evidencia debe sobrevivir al cambio de fragmentación','Ejemplo esquemático · El mismo identificador puede acabar señalando otro texto')
a.text(.3,5.3,'Antes',fontweight='bold');a.text(.3,3.65,'Después',fontweight='bold')
for x,id_,t,green in [(2,'doc-01','Introducción',False),(5.2,'doc-02','60 créditos',True),(8.4,'doc-03','Trámites',False)]:box(a,x,4.55,2.8,1.05,id_+'\n'+t,color=GREEN if green else BLUE,fill='#dcefe4' if green else '#f1f6fb')
for x,id_,t,green in [(2,'doc-01','Introducción A',False),(5.2,'doc-02','Introducción B',False),(8.4,'doc-03','60 créditos',True)]:box(a,x,2.9,2.8,1.05,id_+'\n'+t,color=GREEN if green else RED,fill='#dcefe4' if green else '#f1f6fb')
arrow(a,6.6,4.55,6.6,3.95,RED)
box(a,2,.3,9.2,1.3,'Ancla: documento fuente + «Se requieren 60 créditos»\nRevisar que la frase siga existiendo y quepa completa en un fragmento',GREEN,'#eef7f2')
arrow(a,9.8,2.9,9.8,1.6,GREEN)
save(f,'29-s09-anotacion-estable')
f,a=plt.subplots(figsize=(10,6),layout='constrained');f.suptitle('Abstención: queremos avanzar a la derecha y bajar',fontsize=18,fontweight='bold',color=INK)
a.set(xlim=(-.08,1.1),ylim=(-.1,1.15),xlabel='Abstención correcta en negativas (más alto es mejor)',ylabel='Abstención indebida en respondibles (más bajo es mejor)',xticks=[0,.25,.5,.75,1],yticks=[0,.25,.5,.75,1]);a.grid(alpha=.2)
a.add_patch(Rectangle((.8,0),.2,.2,facecolor='#e2f2e8',edgecolor='none'))
for x,y,t,col,offset in [(0,0,'Siempre responde',RED,(15,15)),(1,1,'Siempre se abstiene',RED,(-175,12)),(.75,.125,'Ejemplo: 3/4 y 1/8',BLUE,(-135,22)),(1,0,'Ideal',GREEN,(-42,14))]:
 a.scatter([x],[y],s=100,color=col,zorder=3);a.annotate(t,(x,y),xytext=offset,textcoords='offset points',color=col,fontsize=12)
save(f,'30-s09-abstencion')
f,a=canvas('Una cita no convierte una invención en evidencia','Ejemplo ficticio · Evaluación de dos afirmaciones, no de la fluidez del texto')
box(a,.2,1.6,3.5,3,'CONTEXTO\n\nSe requieren 60 créditos.\nEl plazo se anunciará\nposteriormente.')
box(a,4.6,3.5,3.3,1.3,'Afirmación 1\n«Se exigen 60 créditos»',GREEN,'#eef7f2')
box(a,4.6,1.2,3.3,1.3,'Afirmación 2\n«Hasta el 30 de junio»',RED,'#fcf0f0')
arrow(a,3.7,3.6,4.6,4.15,GREEN);arrow(a,3.7,2.5,4.6,1.85,RED)
box(a,8.8,2,2.9,2.3,'SOPORTE\n\n1 de 2 afirmaciones\nFidelidad = 0,5',ORANGE,'#fff7e9')
arrow(a,7.9,4.15,8.8,3.7,GREEN);arrow(a,7.9,1.85,8.8,2.6,RED)
save(f,'31-s09-afirmaciones-y-citas')
f,a=canvas('GraphRAG global: preparar resúmenes y luego combinarlos','Patrón descrito en la sesión 09 · Diagrama conceptual',h=6.6)
a.text(.2,5.55,'PREPARACIÓN DEL CORPUS',color=BLUE,fontweight='bold')
for x,t in [(.2,'Textos y\nfragmentos'),(3.2,'Entidades, relaciones\ny grafo'),(6.2,'Comunidades\njerárquicas'),(9.2,'Resúmenes de\ncomunidades')]:box(a,x,3.85,2.5,1.35,t,fs=11)
for x in (2.7,5.7,8.7):arrow(a,x,4.5,x+.5,4.5)
a.text(.2,2.9,'CUANDO LLEGA UNA PREGUNTA',color=GREEN,fontweight='bold')
box(a,.2,.8,2.5,1.35,'Pregunta global',GREEN,'#eef7f2')
box(a,3.2,.5,5,1.95,'MAP\nRespuestas parciales desde los resúmenes\n+ valoración de utilidad',GREEN,'#eef7f2')
box(a,9.2,.8,2.5,1.35,'REDUCE\nSíntesis global',GREEN,'#eef7f2')
arrow(a,2.7,1.5,3.2,1.5,GREEN);arrow(a,8.2,1.5,9.2,1.5,GREEN);arrow(a,10.45,3.85,7.4,2.45,ORANGE)
save(f,'32-s09-graphrag')
f,a=plt.subplots(figsize=(10,6),layout='constrained');f.suptitle('El ganador cambia cuando miras el segmento',fontsize=18,fontweight='bold',color=INK)
x=np.arange(2);w=.32
for shift,vals,label,col in [(-w/2,[61,63.4],'Exactitud global',BLUE),(w/2,[60.5,46],'Exactitud en incontestables',ORANGE)]:
 b=a.bar(x+shift,vals,w,label=label,color=col);a.bar_label(b,labels=[str(v).replace('.',',') for v in vals],padding=6,fontsize=12)
a.set(xticks=x,xticklabels=['MM-GraphRAG','RAG-Anything'],ylim=(0,100),ylabel='Exactitud (%)');a.legend(loc='upper left',frameon=False);a.grid(axis='y',alpha=.15);a.set_axisbelow(True)
f.supxlabel('Fuente: sesión-09.pdf, p. 23 · Cifras históricas atribuidas allí a DocBench',fontsize=10,color='#536577')
save(f,'33-s09-promedio-y-segmentos')
f,a=plt.subplots(figsize=(10,5.8),layout='constrained');f.suptitle('Ocho respondibles: cada acierto vale 12,5 puntos',fontsize=18,fontweight='bold',color=INK)
x=np.arange(9);a.plot(x,x/8,'o-',color=BLUE,lw=2);a.set(xticks=x,yticks=np.arange(9)/8,xlabel='Número de preguntas con algún acierto',ylabel='Hit Rate = aciertos / 8',ylim=(-.04,1.08));a.grid(alpha=.2)
a.annotate('6/8 = 0,75',(6,.75),xytext=(3.5,.86),arrowprops=dict(arrowstyle='->',color=ORANGE),color=ORANGE)
a.annotate('7/8 = 0,875',(7,.875),xytext=(5.2,.52),arrowprops=dict(arrowstyle='->',color=GREEN),color=GREEN)
f.supxlabel('Cálculo exacto para una muestra didáctica · No representa incertidumbre estadística',fontsize=10,color='#536577')
save(f,'34-s09-resolucion-hit-rate')
print('8 figuras exportadas en PNG y SVG')
