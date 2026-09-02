"""Genera los gráficos didácticos del módulo 08.

Los ejemplos coinciden con los valores usados en las notas y en module_08.pdf.
"""

from itertools import combinations
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


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


if __name__ == "__main__":
    configure()
    plot_learning_rate_regimes()
    plot_curvature_valley()
    plot_minibatch_variability()
