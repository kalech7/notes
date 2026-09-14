"""Figuras originales para los apuntes. Requiere numpy, matplotlib y scipy."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse
from scipy.stats import beta
OUT=Path(__file__).resolve().parent
BLUE='#2563eb'; TEAL='#0d9488'; ORANGE='#ea580c'; INK='#172554'; GRAY='#64748b'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','axes.facecolor':'white','text.color':INK,'axes.labelcolor':INK,'svg.fonttype':'none'})
def save(fig,name):
 fig.savefig(OUT/(name+'.png'),dpi=180,bbox_inches='tight',facecolor='white')
 fig.savefig(OUT/(name+'.svg'),bbox_inches='tight',facecolor='white')
 plt.close(fig)
def canvas(title,subtitle='',size=(12,6)):
 fig,ax=plt.subplots(figsize=size);ax.set(xlim=(0,12),ylim=(0,6));ax.axis('off')
 fig.suptitle(title,fontsize=20,fontweight='bold',y=.99)
 if subtitle:fig.text(.5,.91,subtitle,ha='center',fontsize=11,color=GRAY)
 return fig,ax
def box(ax,x,y,w,h,text,c=BLUE):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.04,rounding_size=.14',facecolor=c+'12',edgecolor=c,lw=1.8))
 ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12,color=INK)
def arrow(ax,a,b,label=None,c=GRAY,rad=0):
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,lw=1.7,color=c,connectionstyle=f'arc3,rad={rad}'))
 if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.15,label,ha='center',fontsize=10,color=c)
# 1: Perceptron
fig,ax=canvas('Perceptrón: de las entradas a una decisión','Ejemplo AND: pesos 1 y 1; sesgo −1.5')
box(ax,.3,3.7,1.7,.8,'Entrada x₁');box(ax,.3,1.8,1.7,.8,'Entrada x₂')
box(ax,3.7,2.5,2.5,1.2,'Suma ponderada\na = x₁ + x₂ − 1.5')
arrow(ax,(2,4.1),(3.7,3.3),'× 1');arrow(ax,(2,2.2),(3.7,2.9),'× 1')
box(ax,7.2,2.5,2.2,1.2,'Umbral\n¿a ≥ 0?',TEAL);arrow(ax,(6.2,3.1),(7.2,3.1))
box(ax,10.2,2.5,1.5,1.2,'Salida\n0 o 1',ORANGE);arrow(ax,(9.4,3.1),(10.2,3.1))
ax.text(6,.9,'Con (1, 1): a = 0.5 → salida 1\nCon (1, 0): a = −0.5 → salida 0',ha='center',fontsize=14)
save(fig,'01-perceptron')
# 2 XOR
fig,axes=plt.subplots(1,2,figsize=(11,5),layout='constrained');fig.suptitle('AND se separa con una recta; XOR no',fontsize=20,fontweight='bold')
pts=np.array([[0,0],[0,1],[1,0],[1,1]])
for ax,lab,ys in zip(axes,['AND','XOR'],[[0,0,0,1],[0,1,1,0]]):
 for cls,c,m in [(0,BLUE,'o'),(1,ORANGE,'s')]:
  q=pts[np.array(ys)==cls];ax.scatter(q[:,0],q[:,1],s=180,c=c,marker=m,label=f'Salida {cls}',zorder=3)
 ax.set(xlim=(-.3,1.35),ylim=(-.3,1.35),xticks=[0,1],yticks=[0,1],xlabel='x₁',ylabel='x₂',title=lab);ax.set_aspect('equal');ax.grid(alpha=.2);ax.legend(loc='upper center',ncol=2,fontsize=10)
axes[0].plot([.2,1.3],[1.3,.2],'--',color=TEAL);axes[0].text(.43,.52,'x₁ + x₂ = 1.5',rotation=-45,color=TEAL,fontsize=10)
axes[1].text(.5,.5,'Clases en\ndiagonales opuestas',ha='center',va='center',fontsize=11)
save(fig,'02-and-xor')
# 3 Bayes tree
fig,ax=canvas('Bayes: cambiar el grupo sobre el que contamos','De 1 000 correos, seleccionamos los 200 que contienen «oferta».')
box(ax,.2,2.4,2,1.2,'1 000 correos')
box(ax,3.8,3.7,2.1,.9,'200 spam',ORANGE);box(ax,3.8,1.3,2.1,.9,'800 normales',BLUE)
arrow(ax,(2.2,3.1),(3.8,4.1),'20 %');arrow(ax,(2.2,2.8),(3.8,1.8),'80 %')
box(ax,8,3.7,3.4,.9,'120 con «oferta»',ORANGE);box(ax,8,1.3,3.4,.9,'80 con «oferta»',BLUE)
arrow(ax,(5.9,4.1),(8,4.1),'60 % de los spam');arrow(ax,(5.9,1.8),(8,1.8),'10 % de los normales')
ax.text(6,.35,'P(spam | oferta) = 120 / (120 + 80) = 60 %',ha='center',fontsize=16,fontweight='bold')
save(fig,'03-bayes-conteos')
# 4 GMM
rng=np.random.default_rng(6013);means=[[-2,0],[2,1]];covs=[[[.7,.3],[.3,.5]],[[.5,-.2],[-.2,.8]]]
fig,ax=plt.subplots(figsize=(10,5.6),layout='constrained');fig.suptitle('GMM: puntos observados y componentes que los explican',fontsize=18,fontweight='bold')
for mean,cov,c,label in zip(means,covs,[BLUE,ORANGE],['Componente 1','Componente 2']):
 x=rng.multivariate_normal(mean,cov,90);ax.scatter(x[:,0],x[:,1],c=GRAY,s=13,alpha=.45)
 vals,vecs=np.linalg.eigh(cov);angle=np.degrees(np.arctan2(vecs[1,1],vecs[0,1]))
 for scale,alpha in [(1,.16),(2,.06)]:
  ax.add_patch(Ellipse(mean,2*scale*np.sqrt(vals[1]),2*scale*np.sqrt(vals[0]),angle=angle,facecolor=c,alpha=alpha,edgecolor=c,lw=2))
 ax.scatter(*mean,c=c,marker='X',s=160,label=label,zorder=4)
ax.set(xlabel='Característica 1',ylabel='Característica 2');ax.legend();ax.text(.02,.98,'Datos sintéticos. Elipses: contornos de cada gaussiana.\nLas cruces son medias, no etiquetas observadas.',transform=ax.transAxes,va='top',fontsize=10)
save(fig,'04-gmm-componentes')
# 5 EM
fig,ax=canvas('EM: alternar inferencia y ajuste','Se repite el ciclo; no garantiza encontrar el máximo global.')
box(ax,.2,2.5,2,1.2,'Inicializar\nlos parámetros')
box(ax,3.5,2.5,3,1.2,'Paso E\nCalcular responsabilidades\ncon parámetros fijos',BLUE)
box(ax,8,2.5,3.5,1.2,'Paso M\nReestimar parámetros\ncon responsabilidades fijas',TEAL)
arrow(ax,(2.2,3.1),(3.5,3.1));arrow(ax,(6.5,3.1),(8,3.1))
arrow(ax,(9.5,2.45),(5,2.45),rad=-.55,c=ORANGE)
ax.text(7.3,1,'Repetir hasta el criterio de parada',ha='center',color=ORANGE)
ax.text(6,4.5,'E: ¿cuánto explica cada componente a cada dato?\nM: ¿qué parámetros encajan con esas responsabilidades?',ha='center',fontsize=13)
save(fig,'05-em-ciclo')
# 6 HMM
fig,ax=canvas('HMM: estados ocultos que evolucionan y emiten observaciones','Las flechas horizontales son transiciones; las verticales son emisiones.')
for x,t in [(1,'t − 1'),(4.9,'t'),(8.8,'t + 1')]:
 box(ax,x,3.6,2.1,.9,f'Estado z({t})',BLUE);box(ax,x,1.4,2.1,.9,f'Dato x({t})',TEAL)
 arrow(ax,(x+1.05,3.6),(x+1.05,2.3))
arrow(ax,(3.1,4.05),(4.9,4.05));arrow(ax,(7,4.05),(8.8,4.05))
ax.text(6,.3,'La creencia sobre z(t) incorpora el historial observado x(1), …, x(t).',ha='center',fontsize=13)
save(fig,'06-hmm')
# 7 VAE
fig,ax=canvas('VAE: reconstruir un dato y generar uno nuevo','El codificador aproxima una distribución latente; el decodificador modela los datos.',size=(13,6))
box(ax,.1,3.5,1.4,1,'Dato x');box(ax,2.1,3.5,2,1,'Codificador\nq(z | x)');arrow(ax,(1.5,4),(2.1,4))
box(ax,4.8,3.5,1.7,1,'μ y σ\npara z');arrow(ax,(4.1,4),(4.8,4))
box(ax,7.2,3.5,1.5,1,'Muestrear\nz',ORANGE);arrow(ax,(6.5,4),(7.2,4))
box(ax,9.5,3.5,2.3,1,'Decodificador\np(x | z)',TEAL);arrow(ax,(8.7,4),(9.5,4))
box(ax,2.1,1.3,2.6,.9,'Generación nueva\nz ~ N(0, I)',ORANGE)
arrow(ax,(4.7,1.75),(10.65,3.45),rad=.12,c=ORANGE)
ax.text(8,1.1,'Para generar desde el prior\nno hace falta un dato x inicial.',ha='center',fontsize=12)
ax.text(6,.1,'Entrenamiento: maximizar reconstrucción esperada − divergencia KL.',ha='center',fontsize=12)
save(fig,'07-vae')
# 8 LLM
fig,ax=canvas('LLM: del texto al siguiente token','Durante generación, el token elegido se añade al contexto y el ciclo continúa.')
for x,w,txt,c in [(.1,1.8,'Texto\ndel contexto',BLUE),(2.5,1.8,'Tokens\ne IDs',BLUE),(4.9,2,'Vectores y\ntransformer',TEAL),(7.5,1.9,'Probabilidades\ndel vocabulario',TEAL),(10,1.9,'Elegir\nun token',ORANGE)]:box(ax,x,3,w,1.2,txt,c)
for a,b in [(1.9,2.5),(4.3,4.9),(6.9,7.5),(9.4,10)]:arrow(ax,(a,3.6),(b,3.6))
arrow(ax,(10.9,2.95),(1,2.95),rad=-.25,c=ORANGE)
ax.text(6,1.1,'Añadir el token al texto: los pesos permanecen fijos en inferencia ordinaria.',ha='center',fontsize=12)
save(fig,'08-llm-ciclo')
# 9 beta
x=np.linspace(.001,.999,600);fig,ax=plt.subplots(figsize=(10,5.2),layout='constrained');fig.suptitle('Bayes: más datos concentran la incertidumbre sobre θ',fontsize=18,fontweight='bold')
for a,b,c,label in [(1,1,GRAY,'Prior Beta(1, 1)'),(8,4,BLUE,'7 caras / 3 cruces → Beta(8, 4)'),(71,31,ORANGE,'70 caras / 30 cruces → Beta(71, 31)')]:ax.plot(x,beta.pdf(x,a,b),c=c,lw=2.3,label=label)
ax.set(xlabel='θ: probabilidad desconocida de cara',ylabel='Densidad (no probabilidad de un punto)',xlim=(0,1));ax.legend(loc='upper left',fontsize=10);ax.grid(alpha=.15)
save(fig,'09-bayes-incertidumbre')
# 10 causal
fig,ax=canvas('Observar X e intervenir sobre X no son lo mismo','Ejemplo: calor, venta de helados y personas nadando.')
for offset,title in [(0,'Observación'),(6,'Intervención en X')]:
 ax.text(offset+3,5.1,title,ha='center',fontsize=16,fontweight='bold')
 box(ax,offset+2,3.8,2,.8,'Z: calor',ORANGE);box(ax,offset+.2,1.7,2.6,.9,'X: venta\nde helados',BLUE);box(ax,offset+3.2,1.7,2.6,.9,'Y: personas\nnadando',TEAL)
 arrow(ax,(offset+3.5,3.8),(offset+4.5,2.6))
 if offset==0:arrow(ax,(offset+2.5,3.8),(offset+1.5,2.6))
 else:ax.text(offset+1.2,3.15,'X se fija\nexternamente',ha='center',fontsize=10,color=BLUE)
ax.text(6,.4,'En este grafo, fijar las ventas no cambia el calor ni causa más natación.',ha='center',fontsize=12)
save(fig,'10-causalidad')
print('10 figuras generadas en PNG y SVG.')
