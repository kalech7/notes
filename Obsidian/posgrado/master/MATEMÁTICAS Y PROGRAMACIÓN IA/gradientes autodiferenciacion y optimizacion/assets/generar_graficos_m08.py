"""Genera los gráficos didácticos del módulo 08.

Los ejemplos coinciden con los valores usados en las notas y en module_08.pdf.
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch


OUT = Path(__file__).resolve().parent

NAVY = "#0B153F"
PURPLE = "#6C43E0"
GREEN = "#0D8F78"
ORANGE = "#F07A26"
RED = "#D34B4B"
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


def card(
    ax: plt.Axes,
    x: float,
    y: float,
    width: float,
    height: float,
    text: str,
    *,
    facecolor: str = "white",
    edgecolor: str = "#D5D8E3",
    textcolor: str = NAVY,
    fontsize: float = 11,
    linewidth: float = 1.5,
) -> None:
    """Dibuja una tarjeta en coordenadas normalizadas del eje."""
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        transform=ax.transAxes,
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=linewidth,
    )
    ax.add_patch(patch)
    ax.text(
        x + width / 2,
        y + height / 2,
        text,
        transform=ax.transAxes,
        ha="center",
        va="center",
        color=textcolor,
        fontsize=fontsize,
        linespacing=1.35,
    )


def arrow(
    ax: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    color: str = GRAY,
    linewidth: float = 2.2,
) -> None:
    """Conecta elementos de un diagrama en coordenadas normalizadas."""
    ax.annotate(
        "",
        xy=end,
        xytext=start,
        xycoords=ax.transAxes,
        textcoords=ax.transAxes,
        arrowprops=dict(arrowstyle="-|>", color=color, linewidth=linewidth, mutation_scale=16),
    )


def plot_learning_rate_regimes() -> None:
    a = 4.0
    etas = [0.10, 0.25, 0.40, 0.50, 0.60]
    labels = [
        "Monótona",
        "Llega en un paso",
        "Oscila y converge",
        "No contrae",
        "Diverge",
    ]
    colors = [GREEN, GREEN, PURPLE, ORANGE, RED]
    steps = np.arange(9)

    fig, axes = plt.subplots(1, 5, figsize=(17, 4.6), sharey=True)
    fig.suptitle(
        "La tasa de aprendizaje cambia la dinámica, no solo la velocidad",
        fontsize=20,
        fontweight="bold",
        color=NAVY,
        y=1.03,
    )

    for ax, eta, label, color in zip(axes, etas, labels, colors):
        rho = 1 - eta * a
        errors = rho**steps
        ax.axhline(0, color="#B8BDCC", linewidth=1)
        ax.plot(steps, errors, marker="o", color=color, linewidth=2.5)
        ax.set_title(f"{label}\n$\\eta={eta:.2f}$, $\\rho={rho:.1f}$", fontsize=12)
        ax.set_xlabel("iteración $t$")
        ax.grid(alpha=0.16)
        ax.set_xticks([0, 2, 4, 6, 8])

    axes[0].set_ylabel("error firmado $e_t$")
    axes[0].set_ylim(-4.4, 4.4)
    fig.text(
        0.5,
        -0.04,
        r"Caso $L(\theta)=\frac{4}{2}(\theta-\theta^*)^2$:  "
        r"$e_{t+1}=(1-4\eta)e_t$. Converge exactamente cuando $0<\eta<0.5$.",
        ha="center",
        color=NAVY,
        fontsize=12,
    )
    fig.tight_layout()
    save(fig, "01-regimenes-tasa-aprendizaje.png")


def plot_curvature_valley() -> None:
    hessian = np.diag([1.0, 6.0])
    eta = 0.28
    theta = np.array([-3.2, 1.8])
    trace = [theta.copy()]
    for _ in range(13):
        theta = theta - eta * (hessian @ theta)
        trace.append(theta.copy())
    trace = np.asarray(trace)

    x = np.linspace(-3.8, 3.8, 320)
    y = np.linspace(-2.2, 2.2, 280)
    xx, yy = np.meshgrid(x, y)
    loss = 0.5 * (xx**2 + 6 * yy**2)

    fig, ax = plt.subplots(figsize=(10.5, 6.4))
    levels = [0.15, 0.35, 0.7, 1.2, 2, 3.5, 5.5, 8, 12, 16]
    contours = ax.contour(xx, yy, loss, levels=levels, cmap="Purples", linewidths=1.7)
    ax.clabel(contours, inline=True, fontsize=8, fmt="%.1f")
    ax.plot(trace[:, 0], trace[:, 1], color=ORANGE, marker="o", linewidth=2.4, markersize=5)
    ax.scatter([0], [0], s=130, color=NAVY, zorder=5, label="mínimo")
    ax.scatter(trace[0, 0], trace[0, 1], s=90, color=ORANGE, zorder=5, label="inicio")
    for idx in [0, 1, 2, 3, 5, 8, 13]:
        ax.annotate(str(idx), trace[idx], xytext=(6, 6), textcoords="offset points", color=NAVY)

    ax.set_title("Una sola tasa, dos escalas de curvatura", fontsize=20, pad=16)
    ax.set_xlabel(r"dirección suave: $\lambda_1=1$, factor $1-\eta\lambda_1=0.72$")
    ax.set_ylabel(r"dirección curva: $\lambda_2=6$, factor $1-\eta\lambda_2=-0.68$")
    ax.legend(loc="upper right", frameon=False)
    ax.grid(alpha=0.10)
    ax.set_aspect("equal")
    fig.text(
        0.5,
        0.01,
        "El signo negativo en la dirección más curva produce el zigzag; su módulo menor que 1 todavía permite converger.",
        ha="center",
        color=NAVY,
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    save(fig, "02-valle-curvatura-gd.png")


def plot_minibatch_variability() -> None:
    individual = np.array([-2.0, -6.0, -12.0])
    full_gradient = individual.mean()
    rng = np.random.default_rng(8)

    fig, ax = plt.subplots(figsize=(10.5, 6.2))
    palette = {1: PURPLE, 2: ORANGE, 3: GREEN}

    for batch_size in (1, 2, 3):
        estimates = np.array(
            [individual[list(indices)].mean() for indices in combinations(range(3), batch_size)]
        )
        jitter = rng.uniform(-0.07, 0.07, size=len(estimates))
        ax.scatter(
            np.full_like(estimates, batch_size) + jitter,
            estimates,
            s=100,
            color=palette[batch_size],
            alpha=0.9,
            label=f"m={batch_size}",
        )
        ax.scatter(
            [batch_size],
            [estimates.mean()],
            marker="D",
            s=90,
            facecolor="white",
            edgecolor=NAVY,
            linewidth=2,
            zorder=4,
        )
        ax.vlines(
            batch_size,
            estimates.min(),
            estimates.max(),
            color=palette[batch_size],
            alpha=0.45,
            linewidth=6,
        )

    ax.axhline(
        full_gradient,
        color=NAVY,
        linestyle="--",
        linewidth=2,
        label=rf"gradiente completo $=-20/3\approx{full_gradient:.2f}$",
    )
    ax.set_title("Menor mini-batch: menor costo por paso y mayor variabilidad", fontsize=19, pad=16)
    ax.set_xlabel("tamaño del mini-batch $m$")
    ax.set_ylabel("gradiente estimado $g_S$")
    ax.set_xticks([1, 2, 3])
    ax.set_xlim(0.65, 3.35)
    ax.grid(axis="y", alpha=0.18)
    ax.legend(frameon=False, ncol=2, loc="lower right")
    fig.text(
        0.5,
        0.01,
        "Cada punto es un subconjunto posible. Los diamantes muestran la media: coincide con el gradiente completo.",
        ha="center",
        color=NAVY,
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    save(fig, "03-variabilidad-mini-batch.png")


def plot_derivative_as_slope() -> None:
    """Muestra que la derivada es la pendiente local de la pérdida."""
    w = np.linspace(0.2, 5.8, 400)
    loss = 0.5 * (w - 3.0) ** 2
    points = [1.0, 3.0, 5.0]
    colors = [PURPLE, GREEN, ORANGE]
    titles = [
        "Derivada negativa: $-2$",
        "Derivada cero: $0$",
        "Derivada positiva: $+2$",
    ]
    messages = [
        "Al mover $w$ a la derecha,\nla pérdida baja",
        "La tangente es horizontal:\nestamos en el mínimo",
        "Al mover $w$ a la derecha,\nla pérdida sube",
    ]

    fig, axes = plt.subplots(1, 3, figsize=(15.5, 5.4), sharex=True, sharey=True)
    fig.suptitle(
        "La derivada es la inclinación local de la pérdida",
        fontsize=20,
        fontweight="bold",
        color=NAVY,
        y=1.02,
    )

    for ax, w0, color, title, message in zip(axes, points, colors, titles, messages):
        l0 = 0.5 * (w0 - 3.0) ** 2
        derivative = w0 - 3.0
        local_w = np.linspace(w0 - 0.85, w0 + 0.85, 100)
        tangent = l0 + derivative * (local_w - w0)

        ax.plot(w, loss, color=NAVY, linewidth=2.6, label="pérdida $L(w)$")
        ax.plot(local_w, tangent, color=color, linewidth=3.0, label="recta tangente")
        ax.scatter([w0], [l0], color=color, s=120, zorder=5)
        ax.axvline(w0, color=GRAY, alpha=0.25, linewidth=1)
        ax.set_title(title, fontsize=14, pad=10)
        ax.set_xlabel("parámetro $w$")
        ax.set_xlim(0.2, 5.8)
        ax.set_ylim(-0.55, 4.4)
        ax.grid(alpha=0.14)
        ax.text(
            0.5,
            0.04,
            message,
            transform=ax.transAxes,
            ha="center",
            va="bottom",
            color=NAVY,
            fontsize=11,
        )

    axes[0].set_ylabel("pérdida $L(w)$")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, ncol=2, loc="lower center")
    fig.tight_layout(rect=(0, 0.10, 1, 0.98))
    save(fig, "04-derivada-como-pendiente.png")


def plot_subtract_derivative() -> None:
    """Explica visualmente por qué se resta la derivada."""
    w = np.linspace(0.2, 5.8, 400)
    loss = 0.5 * (w - 3.0) ** 2
    eta = 0.5
    starts = [1.0, 5.0]
    subtitles = [
        r"$L'(1)=-2$: restar un negativo mueve a la derecha",
        r"$L'(5)=+2$: restar un positivo mueve a la izquierda",
    ]

    fig, axes = plt.subplots(1, 2, figsize=(13.2, 5.6), sharex=True, sharey=True)
    fig.suptitle(
        "Restar la derivada mueve el parámetro hacia menor pérdida",
        fontsize=20,
        fontweight="bold",
        color=NAVY,
        y=1.02,
    )

    for ax, w0, subtitle in zip(axes, starts, subtitles):
        derivative = w0 - 3.0
        w1 = w0 - eta * derivative
        l0 = 0.5 * (w0 - 3.0) ** 2
        l1 = 0.5 * (w1 - 3.0) ** 2

        ax.plot(w, loss, color=NAVY, linewidth=2.7)
        ax.scatter([w0], [l0], color=ORANGE, s=130, zorder=5, label="antes")
        ax.scatter([w1], [l1], color=GREEN, s=130, zorder=5, label="después")
        ax.scatter([3], [0], marker="*", color=PURPLE, s=180, zorder=5, label="mínimo")
        ax.annotate(
            "",
            xy=(w1, l1),
            xytext=(w0, l0),
            arrowprops=dict(arrowstyle="-|>", color=GREEN, linewidth=3),
        )
        ax.axvline(w0, color=ORANGE, alpha=0.25, linewidth=1)
        ax.axvline(w1, color=GREEN, alpha=0.25, linewidth=1)
        ax.set_title(subtitle, fontsize=13, pad=10)
        ax.set_xlabel("parámetro $w$")
        ax.set_xlim(0.2, 5.8)
        ax.set_ylim(-0.3, 4.35)
        ax.grid(alpha=0.14)
        ax.text(
            0.5,
            0.93,
            rf"$w_{{nuevo}}={w0:.0f}-0.5({derivative:+.0f})={w1:.0f}$",
            transform=ax.transAxes,
            ha="center",
            va="top",
            color=NAVY,
            fontsize=12,
        )

    axes[0].set_ylabel("pérdida $L(w)$")
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, frameon=False, ncol=3, loc="lower center")
    fig.tight_layout(rect=(0, 0.09, 1, 0.98))
    save(fig, "05-restar-derivada.png")


def plot_gradient_direction() -> None:
    """Muestra el gradiente y un paso real sin superponer textos sobre el mapa."""
    w = np.linspace(-1.2, 3.6, 420)
    b = np.linspace(-0.5, 3.3, 360)
    ww, bb = np.meshgrid(w, b)
    loss = (ww - 2.0) ** 2 + 2.0 * (bb - 1.0) ** 2

    theta = np.array([0.0, 2.0])
    gradient = np.array([-4.0, 4.0])
    direction = gradient / np.linalg.norm(gradient)
    eta = 0.2
    theta_new = theta - eta * gradient

    fig = plt.figure(figsize=(15, 7.6))
    grid = fig.add_gridspec(1, 2, width_ratios=[1.65, 1.0], wspace=0.08)
    ax = fig.add_subplot(grid[0, 0])
    info = fig.add_subplot(grid[0, 1])

    levels = [0, 0.5, 1.5, 3, 6, 10, 15, 22]
    ax.contourf(ww, bb, loss, levels=levels, cmap="Purples", alpha=0.48, extend="max")
    contours = ax.contour(
        ww,
        bb,
        loss,
        levels=[0.5, 1.5, 3, 6, 10, 15],
        colors=NAVY,
        alpha=0.50,
        linewidths=1.3,
    )
    ax.clabel(contours, inline=True, fontsize=8.5, fmt=lambda value: f"L={value:g}")

    # Solo tres marcas en el mapa: estado, paso real y mínimo.
    ax.scatter([2], [1], marker="*", s=300, color=NAVY, zorder=8)
    ax.text(2.05, 0.78, "mínimo\n$(2,1)$", color=NAVY, fontsize=10.5, ha="left", va="top")

    ax.scatter(theta[0], theta[1], s=170, color=ORANGE, edgecolor="white", linewidth=1.6, zorder=9)
    ax.text(-0.05, 1.78, "estado actual\n$\\theta=(0,2)$", color=NAVY, fontsize=11, ha="right", va="top")

    # Rojo: solo orientación del gradiente, normalizada para caber.
    grad_tip = theta + 1.05 * direction
    ax.annotate(
        "",
        xy=grad_tip,
        xytext=theta,
        arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=4.2, mutation_scale=21),
        zorder=10,
    )
    ax.text(grad_tip[0] - 0.06, grad_tip[1] + 0.10, "subida\n$\\nabla L$", color=RED, fontsize=11, ha="right", va="bottom", fontweight="bold")

    # Verde: el paso aplicado tiene exactamente longitud eta por gradiente.
    ax.annotate(
        "",
        xy=theta_new,
        xytext=theta,
        arrowprops=dict(arrowstyle="-|>", color=GREEN, linewidth=4.5, mutation_scale=22),
        zorder=10,
    )
    ax.scatter(theta_new[0], theta_new[1], s=145, color=GREEN, edgecolor="white", linewidth=1.5, zorder=9)
    ax.text(theta_new[0] + 0.10, theta_new[1] + 0.08, "nuevo estado\n$(0.8,1.2)$", color=GREEN, fontsize=11, ha="left", va="bottom", fontweight="bold")

    ax.set_title("Mapa de la pérdida", fontsize=17, pad=12)
    ax.set_xlabel("parámetro $w$")
    ax.set_ylabel("parámetro $b$")
    ax.set_xlim(w.min(), w.max())
    ax.set_ylim(b.min(), b.max())
    ax.set_aspect("equal")
    ax.grid(alpha=0.10)

    # Panel separado para que los cálculos nunca tapen el mapa.
    info.axis("off")
    info.set_xlim(0, 1)
    info.set_ylim(0, 1)
    info.text(0.02, 0.95, "Cómo leer los valores", fontsize=18, fontweight="bold", color=NAVY, va="top")
    card(info, 0.02, 0.76, 0.96, 0.13, r"FUNCIÓN DE PÉRDIDA" + "\n" + r"$L(w,b)=(w-2)^2+2(b-1)^2$", facecolor="#F4F1FF", edgecolor=PURPLE, fontsize=11.5)
    card(info, 0.02, 0.59, 0.96, 0.13, r"PUNTO ACTUAL" + "\n" + r"$\theta=(0,2)$  y  $L=6$", facecolor="#FFF5EC", edgecolor=ORANGE, fontsize=11.5)
    card(info, 0.02, 0.38, 0.96, 0.17, r"GRADIENTE" + "\n" + r"$\nabla L=(-4,+4)$" + "\n" + r"$-4$: subir $w$ baja $L$  |  $+4$: subir $b$ sube $L$", facecolor="#FFF1F1", edgecolor=RED, fontsize=11.2)
    card(info, 0.02, 0.13, 0.96, 0.21, r"PASO CON $\eta=0.2$" + "\n" + r"$\Delta\theta=-\eta\nabla L=(+0.8,-0.8)$" + "\n" + r"$\theta_{nuevo}=(0.8,1.2)$" + "\n" + r"$L: 6\rightarrow1.52$  ↓", facecolor="#EDF9F5", edgecolor=GREEN, fontsize=11.2)
    info.text(0.50, 0.055, "Rojo = subida local\nVerde = paso aplicado hacia menor pérdida", ha="center", va="center", color=NAVY, fontsize=10.5)

    fig.suptitle("Gradiente: dirección, componentes y paso", fontsize=22, fontweight="bold", color=NAVY, y=0.995)
    fig.text(0.5, 0.012, "Las curvas unen puntos con igual pérdida. La flecha roja muestra la dirección del gradiente; la verde incluye la tasa de aprendizaje.", ha="center", color=NAVY, fontsize=11)
    fig.tight_layout(rect=(0, 0.04, 1, 0.96))
    save(fig, "06-gradiente-direcciones.png")


def plot_gradient_components() -> None:
    """Enseña a interpretar por separado los valores de un gradiente de dos componentes."""
    w = np.linspace(-1.0, 3.6, 420)
    b = np.linspace(-0.4, 3.2, 420)
    loss_w = (w - 2.0) ** 2 + 2.0  # b=2 permanece fijo
    loss_b = 4.0 + 2.0 * (b - 1.0) ** 2  # w=0 permanece fijo

    current_loss = 6.0
    delta = 0.25
    next_w_loss = (delta - 2.0) ** 2 + 2.0
    next_b_loss = 4.0 + 2.0 * (2.0 + delta - 1.0) ** 2

    fig, axes = plt.subplots(1, 2, figsize=(15, 6.3), sharey=True)
    fig.suptitle(
        "Cada componente del gradiente responde por un parámetro",
        fontsize=20,
        fontweight="bold",
        color=NAVY,
        y=1.02,
    )

    # Componente respecto de w: la pendiente negativa indica descenso al movernos a la derecha.
    ax = axes[0]
    local_w = np.linspace(-0.75, 0.85, 120)
    tangent_w = current_loss - 4.0 * local_w
    ax.plot(w, loss_w, color=NAVY, linewidth=2.8, label=r"pérdida con $b=2$")
    ax.plot(local_w, tangent_w, color=PURPLE, linewidth=2.5, linestyle="--", label="tangente local")
    ax.scatter([0], [current_loss], s=140, color=ORANGE, edgecolor="white", linewidth=1.4, zorder=6)
    ax.scatter([delta], [next_w_loss], s=115, color=GREEN, edgecolor="white", linewidth=1.2, zorder=6)
    ax.annotate(
        "",
        xy=(delta, next_w_loss),
        xytext=(0, current_loss),
        arrowprops=dict(arrowstyle="-|>", color=GREEN, linewidth=3, mutation_scale=18),
    )
    ax.set_title(r"$\frac{\partial L}{\partial w}=-4$  →  aumentar $w$ baja $L$", fontsize=14, pad=12)
    ax.text(
        0.04,
        0.95,
        r"Si $\Delta w=+0.01$:  $\Delta L\approx(-4)(0.01)=-0.04$",
        transform=ax.transAxes,
        va="top",
        color=NAVY,
        fontsize=11,
        bbox=dict(facecolor="white", edgecolor="#D5D8E3", alpha=0.92, boxstyle="round,pad=0.35"),
    )
    ax.annotate(
        r"$w: 0\to0.25$" + "\n" + r"$L: 6\to5.06$",
        (delta, next_w_loss),
        xytext=(45, -35),
        textcoords="offset points",
        color=GREEN,
        fontsize=11,
        fontweight="bold",
    )
    ax.set_xlabel("valor del parámetro $w$")
    ax.set_ylabel("pérdida $L$")
    ax.set_xlim(w.min(), w.max())

    # Componente respecto de b: la pendiente positiva indica aumento al movernos a la derecha.
    ax = axes[1]
    local_b = np.linspace(1.25, 2.75, 120)
    tangent_b = current_loss + 4.0 * (local_b - 2.0)
    ax.plot(b, loss_b, color=NAVY, linewidth=2.8, label=r"pérdida con $w=0$")
    ax.plot(local_b, tangent_b, color=PURPLE, linewidth=2.5, linestyle="--", label="tangente local")
    ax.scatter([2], [current_loss], s=140, color=ORANGE, edgecolor="white", linewidth=1.4, zorder=6)
    ax.scatter([2 + delta], [next_b_loss], s=115, color=RED, edgecolor="white", linewidth=1.2, zorder=6)
    ax.annotate(
        "",
        xy=(2 + delta, next_b_loss),
        xytext=(2, current_loss),
        arrowprops=dict(arrowstyle="-|>", color=RED, linewidth=3, mutation_scale=18),
    )
    ax.set_title(r"$\frac{\partial L}{\partial b}=+4$  →  aumentar $b$ sube $L$", fontsize=14, pad=12)
    ax.text(
        0.04,
        0.95,
        r"Si $\Delta b=+0.01$:  $\Delta L\approx(+4)(0.01)=+0.04$",
        transform=ax.transAxes,
        va="top",
        color=NAVY,
        fontsize=11,
        bbox=dict(facecolor="white", edgecolor="#D5D8E3", alpha=0.92, boxstyle="round,pad=0.35"),
    )
    ax.annotate(
        r"$b: 2\to2.25$" + "\n" + r"$L: 6\to7.13$",
        (2 + delta, next_b_loss),
        xytext=(45, 15),
        textcoords="offset points",
        color=RED,
        fontsize=11,
        fontweight="bold",
    )
    ax.set_xlabel("valor del parámetro $b$")
    ax.set_xlim(b.min(), b.max())

    for ax in axes:
        ax.set_ylim(0, 15)
        ax.grid(alpha=0.14)
        ax.axhline(current_loss, color=GRAY, linewidth=1, alpha=0.22)

    fig.text(
        0.5,
        0.022,
        "Curva azul: pérdida. Línea morada: tangente local. Para leer una componente, cambia solo ese parámetro y mantén el otro fijo.",
        ha="center",
        color=NAVY,
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0.09, 1, 0.98))
    save(fig, "07-interpretar-componentes-gradiente.png")


def plot_case_conductor() -> None:
    """Resume visualmente predicción, residuo, pérdida, gradiente y actualización."""
    fig, ax = plt.subplots(figsize=(15.5, 7.4))
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.suptitle("Del error al cambio de parámetros", fontsize=22, fontweight="bold", color=NAVY, y=0.98)

    xs = [0.03, 0.275, 0.52, 0.765]
    width = 0.205
    top = [
        "1  PARÁMETROS Y DATO\n$w=1$, $b=0$\n$x=2$, $y=5$",
        "2  PREDICCIÓN\n$\\hat y=wx+b$\n$\\hat y=2$",
        "3  RESIDUO\n$r=\\hat y-y$\n$r=-3$",
        "4  PÉRDIDA\n$L=\\frac{1}{2}r^2$\n$L=4.5$",
    ]
    colors = ["#F4F1FF", "#EEF4FF", "#FFF5EC", "#FFF1F1"]
    edges = [PURPLE, "#3B72C4", ORANGE, RED]
    for x, text_value, fc, ec in zip(xs, top, colors, edges):
        card(ax, x, 0.67, width, 0.17, text_value, facecolor=fc, edgecolor=ec, fontsize=11.5)
    for left, right in zip(xs[:-1], xs[1:]):
        arrow(ax, (left + width, 0.755), (right, 0.755), color=NAVY)

    card(
        ax,
        0.26,
        0.43,
        0.48,
        0.14,
        "5  GRADIENTES Y PASO\n$\\nabla L=(-6,-3)$   →   $-\\eta\\nabla L=(+0.6,+0.3)$ con $\\eta=0.1$\nRestar valores negativos aumenta $w$ y $b$",
        facecolor="#EDF9F5",
        edgecolor=GREEN,
        fontsize=11.5,
    )
    arrow(ax, (0.867, 0.67), (0.72, 0.57), color=RED)
    arrow(ax, (0.50, 0.43), (0.13, 0.34), color=GREEN)

    bottom = [
        "6  NUEVOS PARÁMETROS\n$w^+=1.6$\n$b^+=0.3$",
        "7  NUEVA PREDICCIÓN\n$\\hat y^+=1.6(2)+0.3$\n$\\hat y^+=3.5$",
        "8  NUEVO RESIDUO\n$r^+=3.5-5$\n$r^+=-1.5$",
        "9  NUEVA PÉRDIDA\n$L^+=1.125$\n$4.5\\rightarrow1.125$  ↓",
    ]
    for x, text_value, fc, ec in zip(xs, bottom, colors, edges):
        card(ax, x, 0.17, width, 0.17, text_value, facecolor=fc, edgecolor=ec, fontsize=11.3)
    for left, right in zip(xs[:-1], xs[1:]):
        arrow(ax, (left + width, 0.255), (right, 0.255), color=NAVY)

    ax.text(0.5, 0.075, "Interpretación: el residuo sigue siendo negativo, pero su magnitud bajó de 3 a 1.5; la pérdida cayó 75 % en este paso.", transform=ax.transAxes, ha="center", va="center", color=NAVY, fontsize=11.5)
    ax.text(0.5, 0.025, "Un paso exitoso no demuestra convergencia global: solo confirma que esta actualización concreta redujo el objetivo.", transform=ax.transAxes, ha="center", va="center", color=GRAY, fontsize=10.5)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    save(fig, "08-caso-conductor-entrenamiento.png")


def plot_backprop_visual() -> None:
    """Separa el carril forward del carril backward con valores observables."""
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.suptitle("Forward calcula valores; backward transporta sensibilidad", fontsize=22, fontweight="bold", color=NAVY, y=0.98)

    xs = [0.025, 0.19, 0.355, 0.52, 0.685, 0.85]
    width = 0.125
    forward = [
        "ENTRADAS\n$w=1$, $x=2$\n$b=0$, $y=5$",
        "MULTIPLICAR\n$u=wx$\n$u=2$",
        "SUMAR\n$\\hat y=u+b$\n$\\hat y=2$",
        "RESTAR\n$r=\\hat y-y$\n$r=-3$",
        "CUADRADO\n$q=r^2$\n$q=9$",
        "ESCALAR\n$L=q/2$\n$L=4.5$",
    ]
    for x, label in zip(xs, forward):
        card(ax, x, 0.66, width, 0.18, label, facecolor="#F4F1FF", edgecolor=PURPLE, fontsize=10.8)
    for left, right in zip(xs[:-1], xs[1:]):
        arrow(ax, (left + width, 0.75), (right, 0.75), color=PURPLE)
    ax.text(0.025, 0.88, "FORWARD  →", transform=ax.transAxes, color=PURPLE, fontsize=14, fontweight="bold")

    backward = [
        "$\\partial L/\\partial w=-6$\n$\\partial L/\\partial b=-3$",
        "$\\partial L/\\partial u=-3$\núltimo factor para $w$: $x=2$",
        "$\\partial L/\\partial\\hat y=-3$\nla suma transmite $\\times1$",
        "$\\partial L/\\partial r=-3$\n$\\frac{1}{2}(2r)=-3$",
        "$\\partial L/\\partial q=0.5$\nla división aporta $\\times\\frac{1}{2}$",
        "SEMILLA\n$\\partial L/\\partial L=1$",
    ]
    for x, label in zip(xs, backward):
        card(ax, x, 0.31, width, 0.19, label, facecolor="#EDF9F5", edgecolor=GREEN, fontsize=10.2)
    for right, left in zip(xs[:0:-1], xs[-2::-1]):
        arrow(ax, (right, 0.405), (left + width, 0.405), color=GREEN)
    ax.text(0.85, 0.54, "←  BACKWARD", transform=ax.transAxes, color=GREEN, fontsize=14, fontweight="bold")

    ax.text(0.5, 0.19, "Regla de lectura: multiplica derivadas locales a lo largo de una ruta; si varias rutas llegan al mismo nodo, suma sus contribuciones.", transform=ax.transAxes, ha="center", color=NAVY, fontsize=12, fontweight="bold")
    card(ax, 0.18, 0.055, 0.64, 0.085, "Ruta hacia $w$:  $1\\times\\frac{1}{2}\\times(2r)\\times1\\times1\\times x = 1\\times\\frac{1}{2}\\times(-6)\\times1\\times1\\times2=-6$", facecolor="white", edgecolor=NAVY, fontsize=11.5)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    save(fig, "09-forward-backward-valores.png")


def plot_autograd_lifecycle() -> None:
    """Representa el ciclo de vida de valores, historial, gradientes y parámetros."""
    fig, ax = plt.subplots(figsize=(16, 7.2))
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.suptitle("Qué cambia en cada etapa de autograd", fontsize=22, fontweight="bold", color=NAVY, y=0.98)

    xs = [0.02, 0.215, 0.41, 0.605, 0.80]
    labels = [
        "1  CREAR HOJAS\n$w$, $b$\n`requires_grad=True`\n`.grad = None`",
        "2  FORWARD\ncalcula `y_hat` y `loss`\nlos no-hoja tienen `grad_fn`\n`.grad` aún no cambia",
        "3  BACKWARD\nrecorre el DAG al revés\nllena o acumula\n`w.grad`, `b.grad`",
        "4  STEP\nconsume gradiente + estado\ncambia los parámetros\nno recalcula el gradiente",
        "5  ZERO_GRAD\nprepara el siguiente ciclo\n`set_to_none=True`\n`.grad = None`",
    ]
    faces = ["#F4F1FF", "#EEF4FF", "#EDF9F5", "#FFF5EC", "#FFF1F1"]
    edges = [PURPLE, "#3B72C4", GREEN, ORANGE, RED]
    for x, label, fc, ec in zip(xs, labels, faces, edges):
        card(ax, x, 0.43, 0.16, 0.31, label, facecolor=fc, edgecolor=ec, fontsize=10.7)
    for left, right in zip(xs[:-1], xs[1:]):
        arrow(ax, (left + 0.16, 0.585), (right, 0.585), color=NAVY)

    card(ax, 0.04, 0.18, 0.27, 0.12, "VALOR\nresultado numérico del forward", facecolor="white", edgecolor="#3B72C4", fontsize=11)
    card(ax, 0.365, 0.18, 0.27, 0.12, "HISTORIAL\n`grad_fn` conecta operaciones", facecolor="white", edgecolor=PURPLE, fontsize=11)
    card(ax, 0.69, 0.18, 0.27, 0.12, "GRADIENTE\n`.grad` vive en hojas entrenables", facecolor="white", edgecolor=GREEN, fontsize=11)
    ax.text(0.5, 0.08, "Clave: forward construye valores e historial; backward calcula sensibilidad; step cambia parámetros; zero_grad limpia el acumulador.", transform=ax.transAxes, ha="center", color=NAVY, fontsize=11.7, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    save(fig, "10-ciclo-autograd.png")


def plot_batch_shapes() -> None:
    """Contrasta las formas correctas del lote con un broadcasting silencioso."""
    fig = plt.figure(figsize=(15.5, 7.8))
    grid = fig.add_gridspec(1, 2, width_ratios=[1.15, 1.0], wspace=0.16)
    left = fig.add_subplot(grid[0, 0])
    right = fig.add_subplot(grid[0, 1])
    fig.suptitle("Formas correctas frente a broadcasting accidental", fontsize=22, fontweight="bold", color=NAVY, y=0.98)

    left.axis("off")
    left.set_xlim(0, 1)
    left.set_ylim(0, 1)
    left.set_title("Caso correcto: un residuo por ejemplo", fontsize=16, color=GREEN, pad=12)
    card(left, 0.03, 0.70, 0.25, 0.14, "$X:(B,d)$\n$(3,1)$", facecolor="#F4F1FF", edgecolor=PURPLE, fontsize=12)
    card(left, 0.03, 0.50, 0.25, 0.14, "$w:(d,)$ y $b:()$\n$(1,)$ y escalar", facecolor="#F4F1FF", edgecolor=PURPLE, fontsize=12)
    card(left, 0.38, 0.61, 0.25, 0.16, "$\\hat y=Xw+b$\nforma $(B,)=(3,)$", facecolor="#EEF4FF", edgecolor="#3B72C4", fontsize=12)
    card(left, 0.72, 0.61, 0.25, 0.16, "$r=\\hat y-y$\nforma $(B,)=(3,)$", facecolor="#FFF5EC", edgecolor=ORANGE, fontsize=12)
    arrow(left, (0.28, 0.77), (0.38, 0.70), color=NAVY)
    arrow(left, (0.28, 0.57), (0.38, 0.68), color=NAVY)
    arrow(left, (0.63, 0.69), (0.72, 0.69), color=NAVY)
    card(left, 0.38, 0.34, 0.25, 0.14, "reducir con `mean`\n$L$ tiene forma $()$", facecolor="#EDF9F5", edgecolor=GREEN, fontsize=12)
    arrow(left, (0.845, 0.61), (0.63, 0.48), color=GREEN)
    card(left, 0.11, 0.10, 0.78, 0.13, "$\\nabla_wL:(d,)$, igual que $w$   |   $\\partial L/\\partial b:()$, igual que $b$", facecolor="white", edgecolor=NAVY, fontsize=12)
    arrow(left, (0.505, 0.34), (0.505, 0.23), color=GREEN)

    prediction = np.array([1.0, 2.0, 3.0])
    target = np.array([1.0, 2.0, 3.0])[:, None]
    residual = prediction - target
    im = right.imshow(residual, cmap="RdBu_r", vmin=-2, vmax=2)
    right.set_title("Caso incorrecto: $(3,)-(3,1)\\rightarrow(3,3)$", fontsize=16, color=RED, pad=12)
    right.set_xlabel("predicción $\\hat y_j$ (forma $(3,)$)")
    right.set_ylabel("objetivo $y_i$ (forma $(3,1)$)")
    right.set_xticks(range(3), ["1", "2", "3"])
    right.set_yticks(range(3), ["1", "2", "3"])
    for i in range(3):
        for j in range(3):
            right.text(j, i, f"{residual[i, j]:+.0f}", ha="center", va="center", color="white" if abs(residual[i, j]) > 1 else NAVY, fontsize=15, fontweight="bold")
    right.text(1, 3.05, "Aparecen 9 diferencias $\\hat y_j-y_i$, no 3 residuos emparejados.", ha="center", va="top", color=RED, fontsize=11.5, fontweight="bold", clip_on=False)
    right.text(1, 3.42, "Defensa: `assert prediction.shape == target.shape` antes de restar.", ha="center", va="top", color=NAVY, fontsize=11, clip_on=False)
    cbar = fig.colorbar(im, ax=right, fraction=0.046, pad=0.04)
    cbar.set_label("residuo creado", color=NAVY)
    fig.tight_layout(rect=(0, 0.08, 1, 0.94))
    save(fig, "11-formas-y-broadcasting.png")


def plot_momentum_state() -> None:
    """Hace visible la diferencia entre gradiente, memoria, paso y parámetro."""
    gradients = np.array([-3.0, -1.0, 4.0])
    velocity = np.array([-3.0, -3.7, 0.67])
    changes = -0.1 * velocity
    parameters = np.array([0.0, 0.30, 0.67, 0.603])
    steps = np.arange(1, 4)

    fig, axes = plt.subplots(1, 3, figsize=(15.5, 6.2))
    fig.suptitle("Momentum recuerda: el paso no depende solo del gradiente actual", fontsize=21, fontweight="bold", color=NAVY, y=1.01)

    colors = [GREEN if value < 0 else RED for value in gradients]
    axes[0].bar(steps, gradients, color=colors, width=0.58)
    axes[0].axhline(0, color=NAVY, linewidth=1)
    axes[0].set_title("1. Gradiente observado $g_t$", fontsize=14)
    axes[0].set_xlabel("paso $t$")
    axes[0].set_ylabel("valor")
    for x, value in zip(steps, gradients):
        axes[0].text(x, value + (0.22 if value >= 0 else -0.38), f"{value:g}", ha="center", color=NAVY, fontsize=11, fontweight="bold")

    axes[1].plot(steps, velocity, color=PURPLE, marker="o", linewidth=3, markersize=9)
    axes[1].axhline(0, color=NAVY, linewidth=1)
    axes[1].set_title(r"2. Memoria $v_t=0.9v_{t-1}+g_t$", fontsize=14)
    axes[1].set_xlabel("paso $t$")
    for x, value in zip(steps, velocity):
        axes[1].annotate(f"{value:g}", (x, value), xytext=(0, 12), textcoords="offset points", ha="center", color=PURPLE, fontsize=11, fontweight="bold")

    axes[2].plot(np.arange(4), parameters, color=ORANGE, marker="o", linewidth=3, markersize=9)
    axes[2].set_title(r"3. Parámetro tras $\Delta\theta=-0.1v_t$", fontsize=14)
    axes[2].set_xlabel("estado")
    axes[2].set_xticks(range(4), [r"$\theta_0$", r"$\theta_1$", r"$\theta_2$", r"$\theta_3$"])
    for x, value in enumerate(parameters):
        axes[2].annotate(f"{value:.3f}".rstrip("0").rstrip("."), (x, value), xytext=(0, 12), textcoords="offset points", ha="center", color=ORANGE, fontsize=11, fontweight="bold")

    for ax in axes:
        ax.grid(alpha=0.16)
    axes[0].set_ylim(-4.7, 5.0)
    axes[1].set_ylim(-4.7, 2.0)
    axes[2].set_ylim(-0.05, 0.82)
    fig.text(0.5, 0.015, "En $t=2$, $|g_2|=1$ pero el paso vale $0.37$: la memoria acumulada $v_2=-3.7$ domina al gradiente actual.", ha="center", color=NAVY, fontsize=11.5)
    fig.tight_layout(rect=(0, 0.05, 1, 0.96))
    save(fig, "12-momentum-gradiente-memoria-paso.png")


def plot_mode_matrix() -> None:
    """Visualiza los dos ejes independientes: modo del módulo y registro de autograd."""
    fig, ax = plt.subplots(figsize=(14.5, 8))
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.suptitle("PyTorch tiene dos interruptores independientes", fontsize=22, fontweight="bold", color=NAVY, y=0.98)

    ax.text(0.50, 0.88, "REGISTRO DE AUTOGRAD", transform=ax.transAxes, ha="center", color=PURPLE, fontsize=14, fontweight="bold")
    ax.text(0.36, 0.82, "grad habilitado\nconstruye historial", transform=ax.transAxes, ha="center", color=NAVY, fontsize=12)
    ax.text(0.73, 0.82, "`torch.no_grad()`\nno construye historial", transform=ax.transAxes, ha="center", color=NAVY, fontsize=12)
    ax.text(0.08, 0.50, "MODO DEL\nMÓDULO", transform=ax.transAxes, ha="center", va="center", rotation=90, color=ORANGE, fontsize=14, fontweight="bold")

    card(ax, 0.20, 0.49, 0.32, 0.25, "`model.train()` + grad\n\nDropout: activo y aleatorio\nGrafo: SÍ\nUso típico: entrenamiento", facecolor="#F4F1FF", edgecolor=PURPLE, fontsize=11.5)
    card(ax, 0.57, 0.49, 0.32, 0.25, "`model.train()` + `no_grad()`\n\nDropout: activo y aleatorio\nGrafo: NO\nUso: diagnóstico sin derivar", facecolor="#FFF5EC", edgecolor=ORANGE, fontsize=11.5)
    card(ax, 0.20, 0.18, 0.32, 0.25, "`model.eval()` + grad\n\nDropout: desactivado\nGrafo: SÍ\nUso: saliencia o sensibilidad", facecolor="#EEF4FF", edgecolor="#3B72C4", fontsize=11.5)
    card(ax, 0.57, 0.18, 0.32, 0.25, "`model.eval()` + `no_grad()`\n\nDropout: desactivado\nGrafo: NO\nUso típico: inferencia", facecolor="#EDF9F5", edgecolor=GREEN, fontsize=11.5)
    ax.text(0.14, 0.615, "TRAIN", transform=ax.transAxes, ha="center", va="center", color=ORANGE, fontsize=13, fontweight="bold")
    ax.text(0.14, 0.305, "EVAL", transform=ax.transAxes, ha="center", va="center", color="#3B72C4", fontsize=13, fontweight="bold")
    ax.text(0.5, 0.075, "`eval()` no apaga autograd. `no_grad()` no desactiva Dropout. Cada interruptor responde una pregunta diferente.", transform=ax.transAxes, ha="center", color=NAVY, fontsize=12, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    save(fig, "13-matriz-train-eval-grad.png")


def plot_training_cycle_visual() -> None:
    """Resume el ciclo de entrenamiento y la evidencia observable de cada responsabilidad."""
    fig, ax = plt.subplots(figsize=(16, 8.2))
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.suptitle("Ciclo de entrenamiento: acción, resultado y evidencia", fontsize=22, fontweight="bold", color=NAVY, y=0.98)

    xs = [0.025, 0.215, 0.405, 0.595, 0.785]
    labels = [
        "1  `zero_grad()`\nprepara acumuladores\nEvidencia: `.grad=None`",
        "2  FORWARD\ncalcula predicciones\nEvidencia: forma correcta",
        "3  PÉRDIDA\nreduce a un escalar\nEvidencia: `loss.ndim==0`",
        "4  `backward()`\ncalcula sensibilidades\nEvidencia: `grad_norm`",
        "5  `step()`\ncambia parámetros\nEvidencia: `change_norm`",
    ]
    faces = ["#FFF1F1", "#EEF4FF", "#F4F1FF", "#EDF9F5", "#FFF5EC"]
    edges = [RED, "#3B72C4", PURPLE, GREEN, ORANGE]
    for x, label, fc, ec in zip(xs, labels, faces, edges):
        card(ax, x, 0.58, 0.16, 0.22, label, facecolor=fc, edgecolor=ec, fontsize=10.5)
    for left, right in zip(xs[:-1], xs[1:]):
        arrow(ax, (left + 0.16, 0.69), (right, 0.69), color=NAVY)
    arrow(ax, (0.865, 0.58), (0.865, 0.47), color=NAVY)
    arrow(ax, (0.785, 0.40), (0.18, 0.40), color=NAVY)
    arrow(ax, (0.105, 0.40), (0.105, 0.58), color=NAVY)
    ax.text(0.50, 0.43, "siguiente mini-batch / siguiente iteración", transform=ax.transAxes, ha="center", color=GRAY, fontsize=10.5)

    card(ax, 0.05, 0.17, 0.25, 0.14, "`loss`\n¿cuánto vale el objetivo?\nMenor no prueba todo", facecolor="white", edgecolor=PURPLE, fontsize=11)
    card(ax, 0.375, 0.17, 0.25, 0.14, "`grad_norm`\n¿llegó sensibilidad a las hojas?\nCero y `None` no son iguales", facecolor="white", edgecolor=GREEN, fontsize=11)
    card(ax, 0.70, 0.17, 0.25, 0.14, "`change_norm`\n¿los parámetros cambiaron?\nDebe medirse tras `step()`", facecolor="white", edgecolor=ORANGE, fontsize=11)
    ax.text(0.5, 0.075, "Diagnóstico causal: localiza primero la etapa cuya evidencia contradice lo esperado; no cambies la tasa para ocultar otro problema.", transform=ax.transAxes, ha="center", color=NAVY, fontsize=11.7, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    save(fig, "14-ciclo-entrenamiento-evidencia.png")


def plot_module_overview() -> None:
    """Mapa visual compacto para el índice y la nota de repaso."""
    fig, ax = plt.subplots(figsize=(16, 7.2))
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.suptitle("Mapa visual del entrenamiento verificable", fontsize=23, fontweight="bold", color=NAVY, y=0.98)

    xs = [0.02, 0.185, 0.35, 0.515, 0.68, 0.845]
    width = 0.135
    labels = [
        "1  OBJETIVO\n$\\hat y$ → $r$ → $L$\n¿qué reducimos?",
        "2  SENSIBILIDAD\n$\\nabla L$ y backward\n¿qué parámetro influye?",
        "3  DATOS\nlote y mini-batch\n¿exacto o estimado?",
        "4  DINÁMICA\n$\\eta$ + curvatura\n¿converge u oscila?",
        "5  OPTIMIZADOR\nGD, momentum, Adam\n¿cómo forma el paso?",
        "6  EJECUCIÓN\nmodo, grafo y evidencia\n¿ocurrió lo esperado?",
    ]
    faces = ["#FFF5EC", "#FFF1F1", "#EEF4FF", "#F4F1FF", "#EDF9F5", "white"]
    edges = [ORANGE, RED, "#3B72C4", PURPLE, GREEN, NAVY]
    for x, label, fc, ec in zip(xs, labels, faces, edges):
        card(ax, x, 0.46, width, 0.28, label, facecolor=fc, edgecolor=ec, fontsize=10.4)
    for left, right in zip(xs[:-1], xs[1:]):
        arrow(ax, (left + width, 0.60), (right, 0.60), color=NAVY)

    subtitles = [
        "Notas 01",
        "Notas 02–04",
        "Notas 05 y 07",
        "Nota 06",
        "Nota 08",
        "Notas 09–11",
    ]
    for x, subtitle, ec in zip(xs, subtitles, edges):
        ax.text(x + width / 2, 0.40, subtitle, transform=ax.transAxes, ha="center", color=ec, fontsize=10.5, fontweight="bold")

    card(ax, 0.10, 0.15, 0.80, 0.13, "SECUENCIA MENTAL:  predecir → calcular → observar → comparar → explicar límites", facecolor="white", edgecolor=NAVY, fontsize=13)
    ax.text(0.5, 0.065, "No confundas: pérdida ≠ gradiente ≠ paso ≠ estado del optimizador. Cada cantidad responde una pregunta distinta.", transform=ax.transAxes, ha="center", color=NAVY, fontsize=11.7, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    save(fig, "15-mapa-visual-modulo.png")


def plot_lab_protocol() -> None:
    """Convierte el protocolo del laboratorio en una plantilla visual reutilizable."""
    fig, ax = plt.subplots(figsize=(16, 7.3))
    ax.axis("off")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    fig.suptitle("Método del laboratorio: el código contrasta una predicción", fontsize=22, fontweight="bold", color=NAVY, y=0.98)

    xs = [0.025, 0.19, 0.355, 0.52, 0.685, 0.85]
    labels = [
        "1  FORMULAR\nfunción, formas\ny variables",
        "2  PREDECIR\nsigno, valor\no comportamiento",
        "3  EJECUTAR\nsemilla fija\ny asserts",
        "4  REGISTRAR\nloss, gradiente\ny cambio",
        "5  CONTRASTAR\n¿coincide con\nlo esperado?",
        "6  EXPLICAR\ncausa, evidencia\ny límites",
    ]
    faces = ["#F4F1FF", "#FFF5EC", "#EEF4FF", "#EDF9F5", "#FFF1F1", "white"]
    edges = [PURPLE, ORANGE, "#3B72C4", GREEN, RED, NAVY]
    for x, label, fc, ec in zip(xs, labels, faces, edges):
        card(ax, x, 0.58, 0.125, 0.21, label, facecolor=fc, edgecolor=ec, fontsize=10.6)
    for left, right in zip(xs[:-1], xs[1:]):
        arrow(ax, (left + 0.125, 0.685), (right, 0.685), color=NAVY)

    ax.text(0.50, 0.49, "Una salida inesperada no es el final: indica qué supuesto debes revisar.", transform=ax.transAxes, ha="center", color=NAVY, fontsize=12, fontweight="bold")
    card(ax, 0.05, 0.18, 0.20, 0.18, "PREDICCIÓN\n“Espero `w.grad < 0`\nporque $r<0$ y $x>0$”", facecolor="#FFF5EC", edgecolor=ORANGE, fontsize=11)
    card(ax, 0.29, 0.18, 0.20, 0.18, "OBSERVACIÓN\n`w.grad = -6`\n`loss = 4.5`", facecolor="#EDF9F5", edgecolor=GREEN, fontsize=11)
    card(ax, 0.53, 0.18, 0.20, 0.18, "CONCLUSIÓN\nEl signo coincide\ncon la ruta causal", facecolor="#EEF4FF", edgecolor="#3B72C4", fontsize=11)
    card(ax, 0.77, 0.18, 0.18, 0.18, "LÍMITE\nNo prueba que toda\ntasa converja", facecolor="#FFF1F1", edgecolor=RED, fontsize=11)
    for left, right, width_left in [(0.05, 0.29, 0.20), (0.29, 0.53, 0.20), (0.53, 0.77, 0.20)]:
        arrow(ax, (left + width_left, 0.27), (right, 0.27), color=NAVY)
    ax.text(0.5, 0.075, "Plantilla para cada experimento: qué espero → por qué → qué observé → qué prueba → qué no prueba.", transform=ax.transAxes, ha="center", color=NAVY, fontsize=11.7, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    save(fig, "16-protocolo-laboratorio.png")


def plot_learning_rate_intuition() -> None:
    """Compara tres tasas partiendo del mismo punto y del mismo gradiente."""
    w = np.linspace(0.2, 5.8, 500)
    loss = 0.5 * (w - 3.0) ** 2
    w0 = 1.0
    loss0 = 2.0
    gradient = -2.0
    etas = [0.1, 0.8, 2.2]
    labels = ["Pequeña: avanza poco", "Intermedia: avanza mucho", "Demasiado grande: se pasa"]
    colors = ["#3B72C4", GREEN, RED]

    fig, axes = plt.subplots(1, 3, figsize=(15.5, 6.2), sharex=True, sharey=True)
    fig.suptitle("La tasa de aprendizaje escala el gradiente para crear el paso", fontsize=21, fontweight="bold", color=NAVY, y=1.01)

    for ax, eta, label, color in zip(axes, etas, labels, colors):
        change = -eta * gradient
        w1 = w0 + change
        loss1 = 0.5 * (w1 - 3.0) ** 2

        ax.plot(w, loss, color=NAVY, linewidth=2.7)
        ax.scatter([3], [0], marker="*", s=190, color=PURPLE, zorder=7)
        ax.scatter([w0], [loss0], s=130, color=ORANGE, edgecolor="white", linewidth=1.3, zorder=8)
        ax.scatter([w1], [loss1], s=130, color=color, edgecolor="white", linewidth=1.3, zorder=8)
        ax.annotate("", xy=(w1, loss1), xytext=(w0, loss0), arrowprops=dict(arrowstyle="-|>", color=color, linewidth=3.3, mutation_scale=19))
        ax.set_title(label, fontsize=14, pad=10, color=color)
        ax.text(0.5, 0.93, rf"$\eta={eta}$" + "\n" + rf"$\Delta w=-\eta g={change:.1f}$" + "\n" + rf"$w:1\rightarrow{w1:.1f}$   $L:2\rightarrow{loss1:.2f}$", transform=ax.transAxes, ha="center", va="top", color=NAVY, fontsize=11.3, bbox=dict(facecolor="white", edgecolor=color, alpha=0.94, boxstyle="round,pad=0.35"))
        ax.set_xlabel("parámetro $w$")
        ax.set_xlim(0.2, 5.8)
        ax.set_ylim(-0.25, 4.2)
        ax.grid(alpha=0.14)

    axes[0].set_ylabel("pérdida $L(w)$")
    fig.text(0.5, 0.055, r"En los tres paneles: $L(w)=\frac{1}{2}(w-3)^2$, punto inicial $w=1$, gradiente $g=-2$ y mínimo $w^*=3$.", ha="center", color=NAVY, fontsize=11.2)
    fig.text(0.5, 0.018, "El gradiente decide el sentido; la tasa decide la distancia. La tasa adecuada depende de la escala y de la curvatura del problema.", ha="center", color=NAVY, fontsize=11.5, fontweight="bold")
    fig.tight_layout(rect=(0, 0.09, 1, 0.96))
    save(fig, "17-tasa-aprendizaje-intuicion.png")


if __name__ == "__main__":
    configure()
    plot_learning_rate_regimes()
    plot_curvature_valley()
    plot_minibatch_variability()
    plot_derivative_as_slope()
    plot_subtract_derivative()
    plot_gradient_direction()
    plot_gradient_components()
    plot_case_conductor()
    plot_backprop_visual()
    plot_autograd_lifecycle()
    plot_batch_shapes()
    plot_momentum_state()
    plot_mode_matrix()
    plot_training_cycle_visual()
    plot_module_overview()
    plot_lab_protocol()
    plot_learning_rate_intuition()
