from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

DIFFERENCES = np.array(
    [0.04, 0.01, 0.03, -0.02, 0.05, 0.00, 0.02, 0.06, 0.01, -0.01]
)
MEAN = float(DIFFERENCES.mean())
SD = float(DIFFERENCES.std(ddof=1))
SE = SD / np.sqrt(DIFFERENCES.size)
T_CRITICAL_95_DF9 = 2.2621571627409915
CI_LOW = MEAN - T_CRITICAL_95_DF9 * SE
CI_HIGH = MEAN + T_CRITICAL_95_DF9 * SE


def configure_style() -> None:
    plt.rcParams.update(
        {
            "figure.dpi": 160,
            "savefig.dpi": 200,
            "font.size": 11,
            "axes.titlesize": 15,
            "axes.labelsize": 11,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.18,
        }
    )


def plot_differences() -> None:
    cases = np.arange(1, len(DIFFERENCES) + 1)
    colors = np.where(
        DIFFERENCES > 0,
        "#138a72",
        np.where(DIFFERENCES < 0, "#6546c7", "#6b7280"),
    )

    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.axhline(0, color="#1f2937", linewidth=1.2)
    ax.axhline(
        MEAN,
        color="#d97706",
        linewidth=1.8,
        linestyle="--",
        label=f"Media observada = {MEAN:.3f}",
    )
    ax.vlines(cases, 0, DIFFERENCES, color=colors, linewidth=2.4, alpha=0.85)
    ax.scatter(cases, DIFFERENCES, c=colors, s=70, zorder=3)

    for x, value in zip(cases, DIFFERENCES):
        offset = 0.004 if value >= 0 else -0.006
        ax.text(x, value + offset, f"{value:+.2f}", ha="center", va="center")

    ax.set_title("Diferencia de log-loss por caso: A - B")
    ax.set_xlabel("Caso de prueba")
    ax.set_ylabel("Diferencia de log-loss")
    ax.set_xticks(cases)
    ax.set_ylim(-0.033, 0.074)
    ax.legend(frameon=False, loc="upper left")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "diferencias-por-caso.png", bbox_inches="tight")
    plt.close(fig)


def plot_confidence_interval() -> None:
    fig, ax = plt.subplots(figsize=(10, 3.1))
    ax.axvline(0, color="#d97706", linewidth=2, label="Referencia nula: 0")
    ax.hlines(0, CI_LOW, CI_HIGH, color="#138a72", linewidth=7)
    ax.scatter([CI_LOW, CI_HIGH], [0, 0], s=110, facecolors="white", edgecolors="#138a72", linewidths=2.5, zorder=3)
    ax.scatter([MEAN], [0], s=150, color="#6546c7", zorder=4, label=f"Efecto observado = {MEAN:.3f}")
    ax.text(CI_LOW, 0.08, f"{CI_LOW:.4f}", ha="center")
    ax.text(MEAN, -0.10, f"{MEAN:.3f}", ha="center")
    ax.text(CI_HIGH, 0.08, f"{CI_HIGH:.4f}", ha="center")
    ax.set_title("Intervalo de confianza del 95 % para la diferencia media")
    ax.set_xlabel("Puntos de log-loss; valores positivos favorecen a B")
    ax.set_yticks([])
    ax.set_ylim(-0.24, 0.24)
    ax.set_xlim(-0.006, 0.043)
    ax.legend(frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "intervalo-efecto.png", bbox_inches="tight")
    plt.close(fig)


def plot_sign_flip_null() -> None:
    signs = np.array(list(product((-1.0, 1.0), repeat=len(DIFFERENCES))))
    null_means = (signs * DIFFERENCES).mean(axis=1)
    threshold = abs(MEAN)
    extreme = np.abs(null_means) >= threshold - 1e-15
    count = int(extreme.sum())

    values, counts = np.unique(np.round(null_means, 12), return_counts=True)
    bar_colors = np.where(np.abs(values) >= threshold - 1e-15, "#d97706", "#138a72")

    fig, ax = plt.subplots(figsize=(10, 4.8))
    width = np.min(np.diff(values)) * 0.82
    ax.bar(values, counts, width=width, color=bar_colors, alpha=0.9)
    ax.axvline(-threshold, color="#6546c7", linewidth=2, linestyle="--")
    ax.axvline(threshold, color="#6546c7", linewidth=2, linestyle="--")
    ax.text(
        0,
        counts.max() * 0.92,
        f"Extremas: {count}/1024 = {count/1024:.8f}",
        ha="center",
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.86},
    )
    ax.set_title("Distribución nula exacta por cambios de signo")
    ax.set_xlabel("Media de las diferencias después de cambiar signos")
    ax.set_ylabel("Número de configuraciones")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "distribucion-nula-signos.png", bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    assert np.isclose(MEAN, 0.019)
    assert np.isclose(SD, 0.0260128174)
    assert np.isclose(SE, 0.0082259751)
    assert np.isclose(CI_LOW, 0.00039155, atol=5e-9)
    assert np.isclose(CI_HIGH, 0.03760845, atol=5e-9)
    configure_style()
    plot_differences()
    plot_confidence_interval()
    plot_sign_flip_null()
    print(f"Gráficos guardados en: {OUTPUT_DIR}")
