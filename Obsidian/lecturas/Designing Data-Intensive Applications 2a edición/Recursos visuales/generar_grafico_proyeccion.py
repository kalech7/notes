"""Genera PNG + SVG didácticos. Requiere Python 3 y matplotlib.
Ejecutar: python generar_grafico_proyeccion.py
Todos los volúmenes son decimales y sintéticos; no son mediciones.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent
ROWS, TOTAL_COLUMNS, BYTES_PER_VALUE = 1_000_000, 20, 8
columns = [20, 2, 5, 10]
volumes_mb = [ROWS * n * BYTES_PER_VALUE / 1_000_000 for n in columns]
labels = ['Filas completas · 20 columnas', 'Proyección · 2 columnas',
          'Proyección · 5 columnas', 'Proyección · 10 columnas']
colors = ['#8793A8', '#087F8C', '#328FA3', '#63ADB9']
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 13,
                     'svg.fonttype': 'none', 'axes.unicode_minus': False})
fig = plt.figure(figsize=(13, 8), facecolor='#F6F8FC')
ax = fig.add_axes([.32, .25, .60, .43], facecolor='#F6F8FC')
fig.text(.07, .91, 'Leer menos columnas reduce el volumen', fontsize=25,
         fontweight='bold', color='#17243B')
fig.text(.07, .855, 'Modelo sintético: 1 millón de filas × 20 columnas × 8 bytes por valor',
         fontsize=15, color='#41506A')
fig.text(.07, .795, '2 de 20 columnas = 10 % del contenido de valores',
         fontsize=17, fontweight='bold', color='#087F8C')
ys = list(range(len(columns)))
ax.barh(ys, volumes_mb, height=.53, color=colors, zorder=3)
ax.set_yticks(ys, labels, color='#24344C')
ax.invert_yaxis()
ax.set_xlim(0, 183)
ax.set_xticks([0, 40, 80, 120, 160])
ax.set_xlabel('MB decimales de valores (1 MB = 1 000 000 bytes)',
              labelpad=15, fontsize=12, color='#41506A')
ax.grid(axis='x', color='#DDE3EC', linewidth=1, zorder=0)
ax.tick_params(axis='both', length=0, pad=10, labelsize=12)
for spine in ax.spines.values():
    spine.set_visible(False)
for y, value in zip(ys, volumes_mb):
    ax.text(value + 3, y, f'{value:.0f} MB', va='center', color='#17243B',
            fontsize=16, fontweight='bold')
fig.text(.07, .12, '160 MB frente a 16 MB: 90 % menos contenido de valores en este modelo.',
         fontsize=15, color='#17243B', fontweight='bold')
fig.text(.07, .068, 'Antes de compresión y metadatos. Supone lectura de filas completas frente a proyección ideal.\n'
         'No es un benchmark ni una predicción de tiempo, E/S física o consumo de memoria.',
         fontsize=11, color='#52617A', linespacing=1.55)
for ext in ('png', 'svg'):
    fig.savefig(OUT / f'03-proyeccion-columnas.{ext}', dpi=160,
                facecolor=fig.get_facecolor())
plt.close(fig)
print('Generados: 03-proyeccion-columnas.png y 03-proyeccion-columnas.svg')
