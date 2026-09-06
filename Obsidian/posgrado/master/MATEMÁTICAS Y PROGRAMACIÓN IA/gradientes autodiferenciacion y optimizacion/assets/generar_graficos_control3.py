"""Genera los gráficos y GIFs de la nota 13 (verificación de gradientes con diferencias finitas).

Los valores coinciden con la lectura previa del Control 3 y con las tablas de la nota.
Ejecutar con:  uv run --with matplotlib --with numpy --with pillow python generar_graficos_control3.py
"""

from decimal import Decimal
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent

NAVY = "#0B153F"
PURPLE = "#6C43E0"
GREEN = "#0D8F78"
ORANGE = "#F07A26"
RED = "#D34B4B"
BLUE = "#3B72C4"
GRAY = "#667085"
LIGHT = "#F7F7FC"


def configure() -> None:
    plt.rcParams.update(
        {
            "figure.facecolor": LIGHT,
            "axes.facecolor": "white",
            "axes.edgecolor": NAVY,
            "axes.labelcolor": NAVY,
            "axes.titlecolor": NAVY,
            "xtick.color": GRAY,
            "ytick.color": GRAY,
            "font.family": "DejaVu Sans",
            "font.size": 12,
            "axes.titleweight": "bold",
        }
    )


def save(fig: plt.Figure, filename: str) -> None:
    fig.savefig(OUT / filename, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def card(ax, x, y, width, height, text, *, facecolor="white", edgecolor="#D5D8E3", textcolor=NAVY, fontsize=11, linewidth=1.5, family=None, ha="center"):
    patch = FancyBboxPatch(
        (x, y), width, height,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        transform=ax.transAxes, facecolor=facecolor, edgecolor=edgecolor, linewidth=linewidth,
    )
    ax.add_patch(patch)
    tx = x + width / 2 if ha == "center" else x + 0.02
    ax.text(tx, y + height / 2, text, transform=ax.transAxes, ha=ha, va="center",
            color=textcolor, fontsize=fontsize, linespacing=1.4, family=family)


def arrow(ax, start, end, *, color=GRAY, linewidth=2.2):
    ax.annotate("", xy=end, xytext=start, xycoords=ax.transAxes, textcoords=ax.transAxes,
                arrowprops=dict(arrowstyle="-|>", color=color, linewidth=linewidth, mutation_scale=16))


# ---------------------------------------------------------------------------
# Funciones de prueba
# ---------------------------------------------------------------------------

def central(f, w, h):
    return (f(w + h) - f(w - h)) / (2 * h)


def forward(f, w, h):
    return (f(w + h) - f(w)) / h


sq = lambda w: w * w          # noqa: E731  f(w)=w^2, f'(3)=6  (ejemplo del PDF)
cube = lambda w: w * w * w    # noqa: E731  f(w)=w^3, f'(1)=3  (error central = h^2)


# ---------------------------------------------------------------------------
# 18. La diferencia central es la pendiente de una secante simétrica
# ---------------------------------------------------------------------------

def plot_central_secant() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(15.5, 6.4))
    fig.suptitle("La diferencia central es la pendiente de la recta que une $f(w-h)$ y $f(w+h)$",
                 fontsize=19, fontweight="bold", color=NAVY, y=1.01)

    # Panel izquierdo: h = 1 para ver la geometría
    ax = axes[0]
    w0, h = 3.0, 1.0
    ws = np.linspace(1.4, 4.6, 400)
    ax.plot(ws, sq(ws), color=NAVY, linewidth=2.6, label=r"$f(w)=w^2$")
    wl, wr = w0 - h, w0 + h
    slope = central(sq, w0, h)
    # secante
    xs = np.array([wl - 0.35, wr + 0.35])
    ax.plot(xs, sq(wl) + slope * (xs - wl), color=GREEN, linewidth=3, label=f"secante centrada, pendiente {slope:.0f}")
    # tangente
    ax.plot(xs, sq(w0) + 6 * (xs - w0), color=ORANGE, linewidth=2.2, linestyle="--", label="tangente en $w=3$, pendiente 6")
    for x, c in ((wl, GREEN), (wr, GREEN)):
        ax.scatter([x], [sq(x)], s=120, color=c, edgecolor="white", zorder=6)
        ax.vlines(x, 0, sq(x), color=c, linestyle=":", linewidth=1.4)
    ax.scatter([w0], [sq(w0)], s=130, color=ORANGE, edgecolor="white", zorder=7)
    ax.vlines(w0, 0, sq(w0), color=ORANGE, linestyle=":", linewidth=1.4)
    ax.annotate("", xy=(wr, 1.0), xytext=(wl, 1.0), arrowprops=dict(arrowstyle="<->", color=PURPLE, linewidth=2))
    ax.text(w0, 1.7, r"$2h$ (distancia entre los dos puntos)", ha="center", color=PURPLE, fontsize=11.5, fontweight="bold")
    ax.text(wl, -1.1, r"$w-h$", ha="center", color=GREEN, fontsize=12)
    ax.text(w0, -1.1, r"$w$", ha="center", color=ORANGE, fontsize=12)
    ax.text(wr, -1.1, r"$w+h$", ha="center", color=GREEN, fontsize=12)
    ax.text(0.03, 0.96, r"$h=1$:  $g_{num}=\dfrac{16-4}{2}=6$" + "\n" + "en una parábola la secante centrada\nes paralela a la tangente para cualquier $h$",
            transform=ax.transAxes, ha="left", va="top", color=NAVY, fontsize=11.2,
            bbox=dict(facecolor="white", edgecolor=GREEN, boxstyle="round,pad=0.4"))
    ax.set_xlim(1.4, 4.6)
    ax.set_ylim(-2.2, 24)
    ax.set_xlabel("parámetro $w$")
    ax.set_ylabel("$f(w)$")
    ax.set_title("Geometría con $h$ grande para verla", fontsize=14, pad=10)
    ax.grid(alpha=0.14)
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.70), fontsize=10.2, framealpha=0.95)

    # Panel derecho: el ejemplo del PDF, h = 0.01
    ax = axes[1]
    w0, h = 3.0, 0.01
    ws = np.linspace(2.984, 3.016, 300)
    ax.plot(ws, sq(ws), color=NAVY, linewidth=2.6)
    wl, wr = w0 - h, w0 + h
    ax.scatter([wl, wr], [sq(wl), sq(wr)], s=130, color=GREEN, edgecolor="white", zorder=6)
    ax.scatter([w0], [sq(w0)], s=130, color=ORANGE, edgecolor="white", zorder=7)
    # triángulo de pendiente
    ax.plot([wl, wr], [sq(wl), sq(wl)], color=PURPLE, linewidth=2)
    ax.plot([wr, wr], [sq(wl), sq(wr)], color=PURPLE, linewidth=2)
    ax.text(w0, sq(wl) - 0.012, r"$3.01-2.99=0.02$", ha="center", va="top", color=PURPLE, fontsize=11.5, fontweight="bold")
    ax.text(wr + 0.0008, (sq(wl) + sq(wr)) / 2, r"$9.0601-8.9401$" + "\n" + r"$=0.12$", ha="left", va="center", color=PURPLE, fontsize=11.5, fontweight="bold")
    ax.annotate(r"$f(2.99)=8.9401$", xy=(wl, sq(wl)), xytext=(wl - 0.0045, sq(wl) - 0.035), ha="left", color=GREEN, fontsize=11.5,
                arrowprops=dict(arrowstyle="-", color=GREEN))
    ax.annotate(r"$f(3.01)=9.0601$", xy=(wr, sq(wr)), xytext=(wr - 0.004, sq(wr) + 0.03), ha="right", color=GREEN, fontsize=11.5,
                arrowprops=dict(arrowstyle="-", color=GREEN))
    ax.text(0.03, 0.96, r"$g_{num}(3)=\dfrac{0.12}{0.02}=6$" + "\n" + "tan cerca del punto, la curva casi\nse confunde con su recta tangente",
            transform=ax.transAxes, ha="left", va="top", color=NAVY, fontsize=11.2,
            bbox=dict(facecolor="white", edgecolor=ORANGE, boxstyle="round,pad=0.4"))
    ax.set_xlim(2.984, 3.018)
    ax.set_ylim(8.88, 9.13)
    ax.set_xlabel("parámetro $w$")
    ax.set_title("El ejemplo de la lectura: $h=0.01$", fontsize=14, pad=10)
    ax.grid(alpha=0.14)

    fig.text(0.5, 0.075, r"$g_{num}(w)=\dfrac{f(w+h)-f(w-h)}{2h}\approx f'(w)$      el denominador es $2h$ porque los dos puntos están a $h$ de cada lado de $w$",
             ha="center", va="center", color=NAVY, fontsize=12.2)
    fig.text(0.5, 0.012, "No se usa la fórmula de la derivada: solo dos evaluaciones de la función y una división.",
             ha="center", va="center", color=NAVY, fontsize=11.5, fontweight="bold")
    fig.tight_layout(rect=(0, 0.13, 1, 0.96))
    save(fig, "18-diferencia-central-secante.png")


# ---------------------------------------------------------------------------
# 19. Diferencia hacia adelante frente a diferencia central
# ---------------------------------------------------------------------------

def plot_forward_vs_central() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(15.5, 6.4), gridspec_kw={"width_ratios": [1.25, 1]})
    fig.suptitle("Dos lados frente a un lado: por qué la central aproxima mejor con el mismo $h$",
                 fontsize=19, fontweight="bold", color=NAVY, y=1.01)

    ax = axes[0]
    w0, h = 1.0, 0.5
    ws = np.linspace(0.15, 1.85, 400)
    ax.plot(ws, cube(ws), color=NAVY, linewidth=2.6, label=r"$f(w)=w^3$,  $f'(1)=3$")
    wl, wr = w0 - h, w0 + h
    xs = np.array([0.25, 1.8])
    s_fwd = forward(cube, w0, h)
    s_cen = central(cube, w0, h)
    ax.plot(xs, cube(w0) + s_fwd * (xs - w0), color=ORANGE, linewidth=2.8, label=f"hacia adelante: $(f(w+h)-f(w))/h = {s_fwd:.2f}$")
    ax.plot(xs, cube(wl) + s_cen * (xs - wl), color=GREEN, linewidth=2.8, label=f"central: $(f(w+h)-f(w-h))/2h = {s_cen:.2f}$")
    ax.plot(xs, cube(w0) + 3 * (xs - w0), color=PURPLE, linewidth=2.2, linestyle="--", label="tangente exacta: pendiente 3")
    ax.scatter([wl, wr], [cube(wl), cube(wr)], s=120, color=GREEN, edgecolor="white", zorder=6)
    ax.scatter([w0], [cube(w0)], s=130, color=ORANGE, edgecolor="white", zorder=7)
    for x, lab, c in ((wl, "$w-h$", GREEN), (w0, "$w$", ORANGE), (wr, "$w+h$", GREEN)):
        ax.vlines(x, -1.2, cube(x), color=c, linestyle=":", linewidth=1.3)
        ax.text(x, -1.75, lab, ha="center", color=c, fontsize=12)
    ax.text(0.03, 0.96, "$h=0.5$\n" + f"error adelante $= {abs(s_fwd-3):.2f}$\n" + f"error central $= {abs(s_cen-3):.2f}$\n"
            "la central se apoya a ambos lados y\nlos errores de cada lado se compensan",
            transform=ax.transAxes, ha="left", va="top", color=NAVY, fontsize=11.2,
            bbox=dict(facecolor="white", edgecolor="#D5D8E3", boxstyle="round,pad=0.4"))
    ax.set_xlim(0.15, 1.85)
    ax.set_ylim(-2.3, 6.5)
    ax.set_xlabel("parámetro $w$")
    ax.set_ylabel("$f(w)$")
    ax.set_title("Misma $h$, dos secantes distintas", fontsize=14, pad=10)
    ax.grid(alpha=0.14)
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.69), fontsize=9.8, framealpha=0.95)

    ax = axes[1]
    hs = [0.5, 0.1, 0.01, 0.001]
    e_fwd = [abs(forward(cube, 1.0, h) - 3) for h in hs]
    e_cen = [abs(central(cube, 1.0, h) - 3) for h in hs]
    x = np.arange(len(hs))
    ax.bar(x - 0.19, e_fwd, width=0.36, color=ORANGE, label="hacia adelante")
    ax.bar(x + 0.19, e_cen, width=0.36, color=GREEN, label="central")
    for xi, ef, ec in zip(x, e_fwd, e_cen):
        ax.text(xi - 0.19, ef * 1.25, f"{ef:.3g}", ha="center", color=ORANGE, fontsize=9.5)
        ax.text(xi + 0.19, ec * 1.25, f"{ec:.3g}", ha="center", color=GREEN, fontsize=9.5)
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels([f"$h={h}$" for h in hs])
    ax.set_ylim(3e-7, 8)
    ax.set_ylabel(r"$|g_{num}-f'(w)|$  (escala logarítmica)")
    ax.set_title("El error de la central cae como $h^2$", fontsize=14, pad=10)
    ax.grid(alpha=0.14, axis="y")
    ax.legend(loc="upper right", fontsize=10.5, framealpha=0.95)
    ax.text(0.03, 0.05, "dividir $h$ entre 10:\nadelante $\\approx$ 10 veces menos error\ncentral $\\approx$ 100 veces menos error",
            transform=ax.transAxes, ha="left", va="bottom", color=NAVY, fontsize=11,
            bbox=dict(facecolor="white", edgecolor="#D5D8E3", boxstyle="round,pad=0.4"))

    fig.text(0.5, 0.02, "En $f(w)=w^3$ alrededor de $w=1$: $g_{adelante}=3+3h+h^2$ y $g_{central}=3+h^2$. Solo aritmética, sin series de Taylor.",
             ha="center", color=NAVY, fontsize=11.5, fontweight="bold")
    fig.tight_layout(rect=(0, 0.06, 1, 0.96))
    save(fig, "19-adelante-vs-central.png")


# ---------------------------------------------------------------------------
# 20. Error frente a h: truncamiento a la derecha, redondeo a la izquierda
# ---------------------------------------------------------------------------

def sweep64(f, w, true, hs):
    return np.array([max(abs(central(f, w, h) - true), 1e-17) for h in hs])


def sweep32(hs):
    w = np.float32(3.0)
    out = []
    for h in hs:
        h32 = np.float32(h)
        a, b = w + h32, w - h32
        g = (a * a - b * b) / (np.float32(2) * h32)
        out.append(max(abs(float(g) - 6.0), 1e-17))
    return np.array(out)


def plot_error_vs_h() -> None:
    hs = np.logspace(-1, -17, 97)
    hs32 = np.logspace(-1, -8, 43)
    e_cube = sweep64(cube, 1.0, 3.0, hs)
    e_sq = sweep64(sq, 3.0, 6.0, hs)
    e_32 = sweep32(hs32)

    fig, ax = plt.subplots(figsize=(15.5, 7.2))
    fig.suptitle("Reducir $h$ mejora la estimación… hasta que la representación finita la destruye",
                 fontsize=19, fontweight="bold", color=NAVY, y=0.985)

    ax.axvspan(1e-18, 3e-9, color=RED, alpha=0.06)
    ax.axvspan(3e-9, 3e-4, color=GREEN, alpha=0.07)
    ax.axvspan(3e-4, 1, color=ORANGE, alpha=0.07)

    ax.plot(hs, e_cube, color=NAVY, linewidth=2.6, marker="o", markersize=3.5, label=r"float64, $f(w)=w^3$ en $w=1$ (derivada 3)")
    ax.plot(hs, e_sq, color=PURPLE, linewidth=2.2, marker="o", markersize=3.5, alpha=0.9, label=r"float64, $f(w)=w^2$ en $w=3$ (derivada 6, ejemplo de la lectura)")
    ax.plot(hs32, e_32, color=RED, linewidth=2.4, linestyle="--", marker="s", markersize=3.5, label=r"float32 (dtype por defecto de PyTorch), $f(w)=w^2$ en $w=3$")

    ref = np.logspace(-4, -1, 10)
    ax.plot(ref, 0.03 * ref**2, color=GRAY, linewidth=1.4, linestyle=":")
    ax.text(5e-2, 8e-7, "pendiente $h^2$\n(truncamiento)", color=GRAY, fontsize=10.5, ha="center", va="top")
    ref2 = np.logspace(-13, -9, 10)
    ax.plot(ref2, 3e-17 / ref2, color=GRAY, linewidth=1.4, linestyle=":")
    ax.text(3e-12, 5e-8, "pendiente $1/h$\n(redondeo)", color=GRAY, fontsize=10.5, ha="center", va="top")

    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.invert_xaxis()
    ax.set_xlim(1, 3e-18)
    ax.set_ylim(3e-16, 5e3)
    ax.set_xlabel("perturbación $h$   (hacia la derecha, $h$ más pequeño)")
    ax.set_ylabel(r"$|g_{num}-f'(w)|$")
    ax.grid(alpha=0.16, which="both")
    ax.legend(loc="lower right", fontsize=10.5, framealpha=0.96)

    ax.text(1.5e-2, 2.5e3, "$h$ grande:\nla secante representa mal\nel cambio local", ha="center", va="top", color=ORANGE, fontsize=11.5, fontweight="bold")
    ax.text(3e-6, 2.5e3, "zona útil (float64):\nel error queda cerca de $10^{-10}$", ha="center", va="top", color=GREEN, fontsize=11.5, fontweight="bold")
    ax.text(1e-13, 2.5e3, "$h$ diminuto: $f(w+h)$ y $f(w-h)$ comparten\ncasi todos sus dígitos; al restar\nquedan pocos dígitos útiles", ha="center", va="top", color=RED, fontsize=11.5, fontweight="bold")

    ax.annotate("float64, $h\\leq10^{-16}$:\n$w+h==w$, numerador $=0$,\n$g_{num}=0$ y el error salta a $|f'(w)|$",
                xy=(1e-16, 6.0), xytext=(1e-10, 8e-2), ha="center", color=NAVY, fontsize=10.8,
                bbox=dict(facecolor="white", edgecolor=NAVY, boxstyle="round,pad=0.35"),
                arrowprops=dict(arrowstyle="-|>", color=NAVY, linewidth=1.6))
    ax.annotate("float32, $h=10^{-7}$:\nya ocurre $w+h==w$",
                xy=(1e-7, 6.0), xytext=(3e-7, 3e-3), ha="center", color=RED, fontsize=10.8,
                bbox=dict(facecolor="white", edgecolor=RED, boxstyle="round,pad=0.35"),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.6))
    ax.annotate("float32: lo mejor que consigue\nes $\\approx 6\\cdot10^{-6}$ con $h\\approx10^{-2}$",
                xy=(1e-2, 5.7e-6), xytext=(3e-3, 3e-10), ha="center", color=RED, fontsize=10.8,
                bbox=dict(facecolor="white", edgecolor=RED, boxstyle="round,pad=0.35"),
                arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=1.6))

    fig.text(0.5, 0.015, "Un $h$ menor no siempre da una estimación mejor: dos fuentes de error compiten y la computadora almacena una cantidad finita de cifras.",
             ha="center", color=NAVY, fontsize=11.8, fontweight="bold")
    fig.tight_layout(rect=(0, 0.05, 1, 0.95))
    save(fig, "20-error-vs-h-curva.png")


# ---------------------------------------------------------------------------
# 21. Representación finita: la recta numérica tiene huecos
# ---------------------------------------------------------------------------

def plot_finite_representation() -> None:
    fig = plt.figure(figsize=(15.5, 8.6))
    gs = fig.add_gridspec(2, 1, height_ratios=[1.15, 1], hspace=0.32)
    fig.suptitle("Cerca de $w=3$ los números almacenables forman una rejilla; una $h$ menor que medio hueco desaparece",
                 fontsize=18, fontweight="bold", color=NAVY, y=0.985)

    ax = fig.add_subplot(gs[0])
    ax.set_xlim(-5.2, 5.2)
    ax.set_ylim(-0.45, 4.4)
    ax.axis("off")

    def number_line(y, ulp_label, arrows, title, color_line):
        ax.plot([-4.9, 4.9], [y, y], color=color_line, linewidth=2.4)
        for k in range(-4, 5):
            ax.plot([k, k], [y - 0.08, y + 0.08], color=color_line, linewidth=2)
            lab = "3" if k == 0 else (f"3+{k}·ulp" if k > 0 else f"3−{-k}·ulp")
            ax.text(k, y - 0.22, lab, ha="center", va="top", color=GRAY if k else NAVY, fontsize=9.5, fontweight="bold" if k == 0 else "normal")
        ax.annotate("", xy=(0, y + 0.16), xytext=(-1, y + 0.16), arrowprops=dict(arrowstyle="<->", color=PURPLE, linewidth=1.6))
        ax.text(-0.5, y + 0.2, ulp_label, ha="center", va="bottom", color=PURPLE, fontsize=10)
        ax.text(-5.1, y + 0.75, title, ha="left", va="center", color=NAVY, fontsize=12.5, fontweight="bold")
        for (dx, text, ok), yy in zip(arrows, (y + 1.40, y + 0.80)):
            c = GREEN if ok else RED
            ax.annotate("", xy=(dx, yy), xytext=(0, yy), arrowprops=dict(arrowstyle="-|>", color=c, linewidth=2.4, mutation_scale=15))
            ax.scatter([dx], [yy], s=60, color=c, zorder=5)
            landing = round(dx)
            ax.annotate("", xy=(landing, y + 0.11), xytext=(dx, yy - 0.05), arrowprops=dict(arrowstyle="-|>", color=c, linewidth=1.2, linestyle="--", mutation_scale=10))
            ax.text(0.0, yy + 0.07, text, ha="left", va="bottom", color=c, fontsize=10.2, fontweight="bold")

    number_line(
        2.35, "ulp = 4.44·10⁻¹⁶",
        [(1e-15 / 4.44e-16, "h = 10⁻¹⁵ ≈ 2.25 ulp → se guarda como 3+2·ulp (no como 3.000000000000001)", True),
         (1e-16 / 4.44e-16, "h = 10⁻¹⁶ ≈ 0.23 ulp → se redondea a 3: (w+h)==w es True", False)],
        "float64 (Python, NumPy por defecto)", NAVY,
    )
    number_line(
        0.0, "ulp = 2.38·10⁻⁷",
        [(1e-6 / 2.38e-7, "h = 10⁻⁶ ≈ 4.2 ulp → sobrevive, pero con solo 4 huecos de resolución", True),
         (1e-7 / 2.38e-7, "h = 10⁻⁷ ≈ 0.42 ulp → se redondea a 3: (w+h)==w es True", False)],
        "float32 (dtype por defecto de PyTorch)", RED,
    )

    ax2 = fig.add_subplot(gs[1])
    ax2.axis("off")
    rows = [
        ("3 + 1e-3", repr(3 + 1e-3), str(Decimal(3 + 1e-3))[:28] + "…", "False", GREEN),
        ("3 + 1e-15", repr(3 + 1e-15), str(Decimal(3 + 1e-15))[:28] + "…", "False", GREEN),
        ("3 + 1e-16", repr(3 + 1e-16), str(Decimal(3 + 1e-16)), "True", RED),
    ]
    header = ("expresión", "repr() (lo que imprime Python)", "valor exacto guardado", "(w+h) == w")
    xs = [0.02, 0.19, 0.50, 0.86]
    ax2.text(0.02, 0.95, "Lo que realmente queda en memoria (float64)", transform=ax2.transAxes, color=NAVY, fontsize=13, fontweight="bold", va="top")
    for x, htxt in zip(xs, header):
        ax2.text(x, 0.78, htxt, transform=ax2.transAxes, color=GRAY, fontsize=10.5, va="center", fontweight="bold")
    for i, (a, b, c, d, col) in enumerate(rows):
        y = 0.62 - i * 0.16
        ax2.add_patch(FancyBboxPatch((0.01, y - 0.065), 0.98, 0.13, boxstyle="round,pad=0.005,rounding_size=0.01", transform=ax2.transAxes, facecolor="white", edgecolor="#D5D8E3"))
        ax2.text(xs[0], y, a, transform=ax2.transAxes, family="monospace", fontsize=11.5, va="center", color=NAVY)
        ax2.text(xs[1], y, b, transform=ax2.transAxes, family="monospace", fontsize=11.5, va="center", color=NAVY)
        ax2.text(xs[2], y, c, transform=ax2.transAxes, family="monospace", fontsize=10.5, va="center", color=NAVY)
        ax2.text(xs[3], y, d, transform=ax2.transAxes, family="monospace", fontsize=12, va="center", color=col, fontweight="bold")
    ax2.text(0.02, 0.06, "print(f\"{3+1e-15:.6f}\")  →  3.000000     y también     print(f\"{3:.6f}\")  →  3.000000     pero  (3+1e-15) == 3  →  False",
             transform=ax2.transAxes, family="monospace", fontsize=10.8, va="center", color=NAVY,
             bbox=dict(facecolor="#FFF4E8", edgecolor=ORANGE, boxstyle="round,pad=0.4"))
    ax2.text(0.02, -0.08, "Dos números impresos con pocos decimales pueden verse iguales sin serlo; y dos que parecen distintos en papel pueden ser el mismo valor en memoria.",
             transform=ax2.transAxes, fontsize=11.2, va="center", color=NAVY, fontweight="bold")
    save(fig, "21-representacion-finita-flotante.png")


# ---------------------------------------------------------------------------
# 22. Qué compara la verificación
# ---------------------------------------------------------------------------

def plot_what_is_compared() -> None:
    fig, ax = plt.subplots(figsize=(15.5, 8.2))
    ax.axis("off")
    fig.suptitle("Qué compara una verificación numérica del gradiente", fontsize=20, fontweight="bold", color=NAVY, y=0.985)

    card(ax, 0.03, 0.75, 0.34, 0.21,
         "Gradiente candidato  $g_{cand}$\n\nderivación a mano:  $f'(w)=2w$\no autodiferenciación:\nloss.backward()  →  w.grad",
         facecolor="#EEF1FF", edgecolor=PURPLE, fontsize=11.5)
    card(ax, 0.63, 0.75, 0.34, 0.21,
         "Gradiente numérico  $g_{num}$\n\nperturbar:  $w+h$  y  $w-h$\nevaluar la función dos veces\ndividir entre $2h$",
         facecolor="#E9F7F3", edgecolor=GREEN, fontsize=11.5)
    card(ax, 0.35, 0.52, 0.30, 0.13, "diferencia absoluta\n$|g_{num}-g_{cand}|$", facecolor="white", edgecolor=NAVY, fontsize=13)
    arrow(ax, (0.20, 0.75), (0.42, 0.66), color=PURPLE)
    arrow(ax, (0.80, 0.75), (0.58, 0.66), color=GREEN)

    card(ax, 0.04, 0.22, 0.42, 0.20,
         "pequeña  →  compatibles localmente\n\nla derivada candidata describe bien la tasa\nde cambio en ESTE punto y con ESTE $h$\n(no se exige igualdad exacta)",
         facecolor="#E9F7F3", edgecolor=GREEN, fontsize=11.3)
    card(ax, 0.54, 0.22, 0.42, 0.20,
         "grande  →  algo no encaja\n\nrevisar la derivada a mano, el forward,\nel valor de $h$ o la precisión numérica\n(el fallo puede estar en $g_{num}$, no en $g_{cand}$)",
         facecolor="#FCEBEB", edgecolor=RED, fontsize=11.3)
    arrow(ax, (0.44, 0.52), (0.28, 0.43), color=GREEN)
    arrow(ax, (0.56, 0.52), (0.72, 0.43), color=RED)
    ax.text(0.50, 0.465, "umbral fijado para este ejercicio;\nno es una tolerancia universal", transform=ax.transAxes, ha="center", va="center", color=GRAY, fontsize=10.2, style="italic")

    strip = [
        ("$h$ no es la tasa de aprendizaje", "$h$ sirve para comprobar;\n$\\eta$ sirve para actualizar", PURPLE),
        ("un punto no certifica\ntoda la implementación", "probar otros puntos y otros $h$", ORANGE),
        ("con varios parámetros", "perturbar uno, congelar los demás\ny los datos: una componente cada vez", BLUE),
    ]
    for i, (t, s, c) in enumerate(strip):
        x = 0.03 + i * 0.325
        card(ax, x, 0.02, 0.30, 0.14, f"{t}\n{s}", facecolor="white", edgecolor=c, fontsize=10.6)
    save(fig, "22-que-compara-la-verificacion.png")


# ---------------------------------------------------------------------------
# 23. Con varios parámetros: una componente cada vez
# ---------------------------------------------------------------------------

def plot_one_component_at_a_time() -> None:
    L = lambda w, b: (w - 2) ** 2 + 2 * (b - 1) ** 2  # noqa: E731
    fig, axes = plt.subplots(1, 2, figsize=(15.5, 6.6), gridspec_kw={"width_ratios": [1.1, 1]})
    fig.suptitle("Con varios parámetros se perturba una coordenada y se congela el resto", fontsize=19, fontweight="bold", color=NAVY, y=1.0)

    ax = axes[0]
    W, B = np.meshgrid(np.linspace(-1.5, 2.2, 300), np.linspace(0.3, 3.4, 300))
    cs = ax.contour(W, B, L(W, B), levels=[0.5, 1.5, 3, 4.5, 6, 8, 10, 13], colors=[GRAY], linewidths=1.1, alpha=0.7)
    ax.clabel(cs, fontsize=8.5, fmt="%.1f", colors=GRAY)
    w0, b0, h = 0.0, 2.0, 0.4
    ax.scatter([w0], [b0], s=170, color=NAVY, edgecolor="white", zorder=8)
    ax.text(w0 + 0.08, b0 + 0.12, r"$\theta=(w,b)=(0,2)$", color=NAVY, fontsize=11.5, fontweight="bold")
    # perturbación en w
    ax.plot([w0 - h, w0 + h], [b0, b0], color=ORANGE, linewidth=2.5, zorder=6)
    ax.scatter([w0 - h, w0 + h], [b0, b0], s=110, color=ORANGE, edgecolor="white", zorder=7)
    ax.text(w0 - h - 0.06, b0 - 0.2, r"$(w-h,\,b)$", ha="right", color=ORANGE, fontsize=11)
    ax.text(w0 + h + 0.06, b0 - 0.2, r"$(w+h,\,b)$", ha="left", color=ORANGE, fontsize=11)
    # perturbación en b
    ax.plot([w0, w0], [b0 - h, b0 + h], color=BLUE, linewidth=2.5, zorder=6)
    ax.scatter([w0, w0], [b0 - h, b0 + h], s=110, color=BLUE, edgecolor="white", zorder=7)
    ax.text(w0 - 0.1, b0 + h + 0.08, r"$(w,\,b+h)$", ha="right", color=BLUE, fontsize=11)
    ax.text(w0 - 0.1, b0 - h - 0.2, r"$(w,\,b-h)$", ha="right", color=BLUE, fontsize=11)
    ax.set_xlabel("parámetro $w$")
    ax.set_ylabel("parámetro $b$")
    ax.set_title(r"$L(w,b)=(w-2)^2+2(b-1)^2$, gradiente exacto $(-4,\,4)$", fontsize=13, pad=10)
    ax.set_xlim(-1.5, 2.2)
    ax.set_ylim(0.3, 3.4)
    ax.grid(alpha=0.12)

    ax = axes[1]
    ax.axis("off")
    lw_p, lw_m = L(w0 + h, b0), L(w0 - h, b0)
    lb_p, lb_m = L(w0, b0 + h), L(w0, b0 - h)
    card(ax, 0.02, 0.62, 0.96, 0.32,
         r"componente $w$ (naranja): $b$ y los datos quedan fijos" + "\n\n"
         + rf"$\dfrac{{L(w+h,b)-L(w-h,b)}}{{2h}}=\dfrac{{{lw_p:.2f}-{lw_m:.2f}}}{{{2*h:.1f}}}={(lw_p-lw_m)/(2*h):.0f}$",
         facecolor="#FFF4E8", edgecolor=ORANGE, fontsize=12)
    card(ax, 0.02, 0.24, 0.96, 0.32,
         r"componente $b$ (azul): $w$ y los datos quedan fijos" + "\n\n"
         + rf"$\dfrac{{L(w,b+h)-L(w,b-h)}}{{2h}}=\dfrac{{{lb_p:.2f}-{lb_m:.2f}}}{{{2*h:.1f}}}={(lb_p-lb_m)/(2*h):.0f}$",
         facecolor="#EAF1FB", edgecolor=BLUE, fontsize=12)
    card(ax, 0.02, 0.0, 0.96, 0.18,
         "cada componente del gradiente exige 2 evaluaciones de la pérdida;\n$p$ parámetros  →  $2p$ evaluaciones completas del forward.\nPor eso sirve para verificar, no para entrenar.",
         facecolor="white", edgecolor="#D5D8E3", fontsize=10.6)
    fig.text(0.5, 0.01, "En $h=0.4$ los valores coinciden con $(-4,4)$ porque la pérdida es cuadrática; en general habrá una diferencia pequeña.",
             ha="center", color=NAVY, fontsize=11.2, fontweight="bold")
    fig.tight_layout(rect=(0, 0.04, 1, 0.95))
    save(fig, "23-una-componente-a-la-vez.png")


# ---------------------------------------------------------------------------
# GIF 18: al reducir h la secante centrada se acerca a la tangente
# ---------------------------------------------------------------------------

def gif_secant_to_tangent() -> None:
    hs = np.concatenate([np.geomspace(1.4, 0.04, 44), np.full(12, 0.04)])
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.8), dpi=100)
    fig.suptitle("Al reducir $h$, la secante centrada se acerca a la tangente", fontsize=16, fontweight="bold", color=NAVY, y=0.99)

    specs = [
        (axes[0], sq, 3.0, 6.0, (1.0, 5.0), (-1, 27), r"$f(w)=w^2$ en $w=3$  (derivada exacta 6)"),
        (axes[1], cube, 1.0, 3.0, (-0.6, 2.6), (-2, 15), r"$f(w)=w^3$ en $w=1$  (derivada exacta 3)"),
    ]
    artists = []
    for ax, f, w0, true, xl, yl, title in specs:
        ws = np.linspace(*xl, 400)
        ax.plot(ws, f(ws), color=NAVY, linewidth=2.4)
        xs = np.array(xl)
        ax.plot(xs, f(w0) + true * (xs - w0), color=ORANGE, linewidth=2, linestyle="--", label="tangente (derivada exacta)")
        ax.scatter([w0], [f(w0)], s=110, color=ORANGE, edgecolor="white", zorder=7)
        (sec,) = ax.plot([], [], color=GREEN, linewidth=3, label="secante centrada")
        pts = ax.scatter([], [], s=100, color=GREEN, edgecolor="white", zorder=8)
        vl = ax.vlines([], 0, 0)
        txt = ax.text(0.03, 0.96, "", transform=ax.transAxes, ha="left", va="top", color=NAVY, fontsize=11,
                      bbox=dict(facecolor="white", edgecolor=GREEN, boxstyle="round,pad=0.4"))
        ax.set_xlim(*xl)
        ax.set_ylim(*yl)
        ax.set_title(title, fontsize=12.5, pad=8)
        ax.set_xlabel("parámetro $w$")
        ax.grid(alpha=0.14)
        ax.legend(loc="lower right", fontsize=9.5, framealpha=0.95)
        artists.append((ax, f, w0, true, xl, sec, pts, txt))

    def update(i):
        h = hs[i]
        out = []
        for ax, f, w0, true, xl, sec, pts, txt in artists:
            wl, wr = w0 - h, w0 + h
            g = central(f, w0, h)
            xs = np.array(xl)
            sec.set_data(xs, f(wl) + g * (xs - wl))
            pts.set_offsets(np.c_[[wl, wr], [f(wl), f(wr)]])
            err = abs(g - true)
            note = "siempre 6: parábola" if f is sq else f"error $= h^2 = {err:.4f}$"
            txt.set_text(f"$h = {h:.3f}$\n$g_{{num}} = {g:.4f}$\n{note}")
            out += [sec, pts, txt]
        return out

    anim = FuncAnimation(fig, update, frames=len(hs), blit=False)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    anim.save(OUT / "18-secante-a-tangente-animado.gif", writer=PillowWriter(fps=8), dpi=100)
    plt.close(fig)


# ---------------------------------------------------------------------------
# GIF 20: la curva de error se dibuja mientras h se reduce
# ---------------------------------------------------------------------------

def gif_error_sweep() -> None:
    hs = np.logspace(-1, -17, 33)
    w0, true = 1.0, 3.0
    errs = sweep64(cube, w0, true, hs)
    hold = 14
    frames = list(range(len(hs))) + [len(hs) - 1] * hold

    fig, (ax, axc) = plt.subplots(1, 2, figsize=(13.5, 5.9), dpi=100, gridspec_kw={"width_ratios": [1.25, 1]})
    fig.suptitle("Barrido de $h$ en float64 para $f(w)=w^3$ en $w=1$: dos regímenes y un colapso", fontsize=15, fontweight="bold", color=NAVY, y=0.99)

    ax.axvspan(1e-18, 3e-9, color=RED, alpha=0.06)
    ax.axvspan(3e-9, 3e-4, color=GREEN, alpha=0.07)
    ax.axvspan(3e-4, 1, color=ORANGE, alpha=0.07)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.invert_xaxis()
    ax.set_xlim(1, 3e-18)
    ax.set_ylim(3e-13, 30)
    ax.set_xlabel("perturbación $h$   (hacia la derecha, $h$ más pequeño)")
    ax.set_ylabel(r"$|g_{num}-3|$")
    ax.grid(alpha=0.16, which="both")
    ax.text(1.5e-2, 8, "truncamiento", ha="center", va="top", color=ORANGE, fontsize=11, fontweight="bold")
    ax.text(3e-6, 8, "zona útil", ha="center", va="top", color=GREEN, fontsize=11, fontweight="bold")
    ax.text(1e-13, 8, "redondeo y cancelación", ha="center", va="top", color=RED, fontsize=11, fontweight="bold")
    (line,) = ax.plot([], [], color=NAVY, linewidth=2.2, marker="o", markersize=3.5)
    cur = ax.scatter([], [], s=160, color=PURPLE, edgecolor="white", zorder=9)

    axc.axis("off")
    axc.add_patch(FancyBboxPatch((0.0, 0.0), 1.0, 1.0, boxstyle="round,pad=0.01,rounding_size=0.02", transform=axc.transAxes, facecolor="#1E2433", edgecolor="#1E2433"))
    console = axc.text(0.04, 0.95, "", transform=axc.transAxes, family="monospace", fontsize=10.6, va="top", ha="left", color="#E6E9F2", linespacing=1.55)
    status = axc.text(0.5, 0.06, "", transform=axc.transAxes, ha="center", va="center", fontsize=11.5, fontweight="bold", color="white",
                      bbox=dict(facecolor=GREEN, edgecolor="none", boxstyle="round,pad=0.45"))

    def regime(h, err):
        if h <= 1e-16:
            return "w+h == w  →  numerador 0, g_num = 0", RED
        if h < 3e-9:
            return "h diminuto: se pierden dígitos útiles al restar", RED
        if h < 3e-4:
            return "zona útil: el error ronda 1e-10", GREEN
        return "h grande: error de truncamiento ≈ h²", ORANGE

    def update(i):
        k = frames[i]
        h = float(hs[k])
        a, b = w0 + h, w0 - h
        num = cube(a) - cube(b)
        g = num / (2 * h)
        line.set_data(hs[: k + 1], errs[: k + 1])
        cur.set_offsets([[h, errs[k]]])
        console.set_text(
            f"w = 1.0      f(w) = w**3      f'(w) = 3\n"
            f"h              = {h:.1e}\n"
            f"w + h          = {a!r}\n"
            f"w - h          = {b!r}\n"
            f"(w + h) == w   = {a == w0}\n"
            f"f(w+h)-f(w-h)  = {num!r}\n"
            f"g_num          = {g!r}\n"
            f"abs(g_num - 3) = {abs(g - true):.3e}"
        )
        s, c = regime(h, errs[k])
        status.set_text(s)
        status.get_bbox_patch().set_facecolor(c)
        return line, cur, console, status

    anim = FuncAnimation(fig, update, frames=len(frames), blit=False)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    anim.save(OUT / "20-error-vs-h-animado.gif", writer=PillowWriter(fps=3), dpi=100)
    plt.close(fig)


if __name__ == "__main__":
    configure()
    plot_central_secant()
    plot_forward_vs_central()
    plot_error_vs_h()
    plot_finite_representation()
    plot_what_is_compared()
    plot_one_component_at_a_time()
    gif_secant_to_tangent()
    gif_error_sweep()
    print("listo:", sorted(p.name for p in OUT.glob("1[89]-*")) + sorted(p.name for p in OUT.glob("2[0-3]-*")))
