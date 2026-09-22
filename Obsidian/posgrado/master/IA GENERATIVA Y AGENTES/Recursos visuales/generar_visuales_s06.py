"""Figuras didácticas de la sesión 06. Requiere NumPy y Matplotlib."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parent
BLUE = "#2563eb"
TEAL = "#0d9488"
ORANGE = "#ea580c"
INK = "#172554"
GRAY = "#64748b"
plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 11,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "svg.fonttype": "none",
    }
)


def save(fig, stem):
    fig.savefig(OUT / f"{stem}.png", dpi=190, bbox_inches="tight", facecolor="white")
    svg_path = OUT / f"{stem}.svg"
    fig.savefig(svg_path, bbox_inches="tight", facecolor="white")
    svg_path.write_text("\n".join(line.rstrip() for line in svg_path.read_text().splitlines()) + "\n")
    plt.close(fig)


# 16. El plano es una ilustración, no una proyección medida de un modelo.
fig, ax = plt.subplots(figsize=(10, 5.5), layout="constrained")
fig.suptitle("Embeddings: proximidad de significado", fontsize=17, fontweight="bold")
points = [
    (0.8, 2.8, "¿Cómo restablezco mi contraseña?", BLUE),
    (2.1, 2.35, "Olvidé mi clave de acceso", BLUE),
    (6.5, 3.5, "Receta de locro de papa", ORANGE),
    (7.6, 2.7, "Cómo cocinar una sopa", ORANGE),
    (4.6, 0.8, "La computadora calcula π", TEAL),
]
for x, y, label, color in points:
    ax.scatter(x, y, s=170, color=color, zorder=3)
    ax.annotate(label, (x, y), xytext=(7, 10), textcoords="offset points", fontsize=10)
ax.plot([0.8, 2.1], [2.8, 2.35], color=BLUE, lw=2, ls="--")
ax.plot([6.5, 7.6], [3.5, 2.7], color=ORANGE, lw=2, ls="--")
ax.set(xlim=(0, 10.8), ylim=(0, 4.7), xlabel="Dimensión ilustrativa 1", ylabel="Dimensión ilustrativa 2")
ax.grid(alpha=0.14)
fig.text(0.5, -0.01, "Esquema conceptual 2D: no son embeddings calculados ni preserva distancias reales.", ha="center", color=GRAY)
save(fig, "16-embeddings-vecindad")


# 17. Una ablación histórica reproducida a partir de las cifras citadas en las diapositivas.
labels = ["BERT CLS", "BERT promedio", "GloVe promedio", "SBERT-NLI base", "SBERT-NLI large"]
values = [29.19, 54.81, 61.32, 74.89, 76.55]
fig, ax = plt.subplots(figsize=(10, 5), layout="constrained")
fig.suptitle("Comparar por coseno requiere entrenar el espacio", fontsize=17, fontweight="bold")
bars = ax.barh(labels[::-1], values[::-1], color=[TEAL, BLUE, GRAY, GRAY, GRAY], height=0.63)
for bar, value in zip(bars, values[::-1]):
    ax.text(value + 0.9, bar.get_y() + bar.get_height() / 2, f"{value:.2f}", va="center")
ax.set(xlim=(0, 90), xlabel="Spearman × 100, promedio de siete tareas STS")
ax.grid(axis="x", alpha=0.15)
ax.set_axisbelow(True)
fig.text(0.5, -0.02, "Reimers y Gurevych (2019), Tabla 1; modelos y prueba de ese estudio, no ranking actual.", ha="center", color=GRAY)
save(fig, "17-sbert-sts-historico")


# 18. Contraejemplo exacto del material: producto punto sin normalizar invierte el ganador.
q = np.array([1.0, 0.0])
s1 = np.array([0.8, 0.6])
s2 = np.array([1.0, 2.0])
fig, axes = plt.subplots(1, 2, figsize=(11, 5.5), layout="constrained")
fig.suptitle("Sin normalizar, la longitud puede cambiar el primer resultado", fontsize=16, fontweight="bold")
ax = axes[0]
for v, name, color in [(q, "q=(1,0)", INK), (s1, "s₁=(0.8,0.6)", TEAL), (s2, "s₂=(1,2)", ORANGE)]:
    ax.arrow(0, 0, v[0], v[1], width=0.012, head_width=0.08, length_includes_head=True, color=color)
    ax.text(v[0] + 0.05, v[1] + 0.04, name, color=color)
ax.set(xlim=(-0.1, 1.9), ylim=(-0.1, 2.45), xlabel="Dimensión 1", ylabel="Dimensión 2")
ax.set_aspect("equal")
ax.grid(alpha=0.15)
ax = axes[1]
x = np.arange(2)
ax.bar(x - 0.18, [q @ s1, q @ s2], 0.34, color=ORANGE, label="Producto punto")
ax.bar(x + 0.18, [(q @ s1) / np.linalg.norm(s1), (q @ s2) / np.linalg.norm(s2)], 0.34, color=TEAL, label="Coseno")
ax.set(xticks=x, xticklabels=["s₁", "s₂"], ylim=(0, 1.15), ylabel="Puntaje")
ax.legend(loc="upper left", fontsize=9)
ax.grid(axis="y", alpha=0.15)
ax.set_axisbelow(True)
fig.text(0.5, -0.02, "Ejemplo matemático de la sesión 06, p. 14: dot elige s₂; coseno elige s₁.", ha="center", color=GRAY)
save(fig, "18-coseno-producto-punto")


# 19. Demostración de umbral entre consultas: mismo coseno, distinta norma de consulta.
fig, ax = plt.subplots(figsize=(9, 4.8), layout="constrained")
fig.suptitle("Normalizar solo documentos conserva el orden, pero cambia el puntaje", fontsize=15, fontweight="bold")
names = ["Consulta A\n||q|| = 1", "Consulta B\n||q|| = 2"]
cosines = [0.3, 0.3]
dots = [0.3, 0.6]
x = np.arange(2)
ax.bar(x - 0.17, cosines, 0.33, color=TEAL, label="Coseno")
ax.bar(x + 0.17, dots, 0.33, color=ORANGE, label="q · documento unitario")
ax.axhline(0.35, color=INK, ls="--", label="Umbral fijo 0.35")
ax.set(xticks=x, xticklabels=names, ylim=(0, 0.73), ylabel="Puntaje del mismo nivel de similitud angular")
ax.legend(loc="upper left", fontsize=9)
ax.grid(axis="y", alpha=0.15)
ax.set_axisbelow(True)
fig.text(0.5, -0.02, "Datos inventados para ilustrar q · ŝ = ||q|| cos(q,s); no son mediciones de un sistema.", ha="center", color=GRAY)
save(fig, "19-normalizacion-umbral")
