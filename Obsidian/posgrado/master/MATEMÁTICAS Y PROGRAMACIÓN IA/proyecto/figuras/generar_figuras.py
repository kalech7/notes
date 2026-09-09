"""Genera las figuras reproducibles utilizadas en proyecto.tex."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter


OUTPUT_DIR = Path(__file__).resolve().parent

BLUE = "#256A9E"
ORANGE = "#C46A2B"
GREEN = "#3A8467"
DARK = "#27323A"
GRAY = "#68727D"
GRID = "#D8DDE3"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 9,
        "axes.titlesize": 10,
        "axes.labelsize": 9,
        "axes.edgecolor": GRAY,
        "axes.labelcolor": DARK,
        "xtick.color": DARK,
        "ytick.color": DARK,
        "text.color": DARK,
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


def finish_axis(axis: plt.Axes, grid_axis: str) -> None:
    """Aplica un estilo sobrio y apto para impresión."""
    axis.spines["top"].set_visible(False)
    axis.spines["right"].set_visible(False)
    axis.grid(axis=grid_axis, color=GRID, linewidth=0.7, alpha=0.9)
    axis.set_axisbelow(True)


def plot_window_metrics() -> None:
    events = np.array([25, 50, 75, 100, 125, 150])
    auc = np.array([0.632, 0.652, 0.651, 0.692, 0.665, 0.673])
    far = np.array([81.6, 75.5, 71.4, 69.4, 67.3, 75.5])
    frr = np.array([7.1, 5.4, 8.9, 3.6, 7.1, 5.4])

    figure, axes = plt.subplots(1, 2, figsize=(8.2, 3.45), constrained_layout=True)

    auc_axis = axes[0]
    auc_axis.plot(events, auc, color=BLUE, marker="o", linewidth=2, markersize=5)
    auc_axis.axhline(0.80, color=GRAY, linestyle="--", linewidth=1.2, label="Criterio: 0.80")
    auc_axis.scatter([100], [0.692], color=ORANGE, marker="D", s=34, zorder=3)
    auc_axis.annotate(
        "Máximo: 0.692\n100 eventos = 23.1 s",
        xy=(100, 0.692),
        xytext=(106, 0.715),
        arrowprops={"arrowstyle": "-", "color": GRAY, "linewidth": 0.9},
        fontsize=8,
    )
    auc_axis.set_title("(a) Separación entre clases")
    auc_axis.set_xlabel("Eventos observados")
    auc_axis.set_ylabel("AUC")
    auc_axis.set_xticks(events)
    auc_axis.set_ylim(0.58, 0.83)
    auc_axis.legend(frameon=False, loc="lower right", fontsize=8)
    finish_axis(auc_axis, "y")

    error_axis = axes[1]
    error_axis.plot(events, far, color=ORANGE, marker="s", linewidth=2, markersize=5, label="FAR")
    error_axis.plot(events, frr, color=GREEN, marker="o", linewidth=2, markersize=5, label="FRR")
    error_axis.axhline(10, color=GRAY, linestyle="--", linewidth=1.2, label="Límite: 10 %")
    error_axis.scatter([100, 100], [69.4, 3.6], color=[ORANGE, GREEN], s=32, zorder=3)
    error_axis.annotate("69.4 %", xy=(100, 69.4), xytext=(105, 64), fontsize=8)
    error_axis.annotate(
        "3.6 %",
        xy=(100, 3.6),
        xytext=(106, 15),
        arrowprops={"arrowstyle": "-", "color": GRAY, "linewidth": 0.9},
        fontsize=8,
    )
    error_axis.set_title("(b) Errores de decisión")
    error_axis.set_xlabel("Eventos observados")
    error_axis.set_ylabel("Tasa")
    error_axis.set_xticks(events)
    error_axis.set_ylim(0, 90)
    error_axis.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:.0f} %"))
    error_axis.legend(frameon=False, loc="center right", fontsize=8)
    finish_axis(error_axis, "y")

    figure.savefig(OUTPUT_DIR / "metricas_por_eventos.png", dpi=300, bbox_inches="tight")
    plt.close(figure)


def plot_feature_auc() -> None:
    features = [
        "Variación de aceleración",
        "Aceleración media absoluta",
        "Velocidad máxima",
        "Variación de velocidad",
        "Fracción de movimientos",
    ]
    auc_values = np.array([0.769, 0.743, 0.665, 0.657, 0.626])
    positions = np.arange(len(features))

    figure, axis = plt.subplots(figsize=(7.7, 3.35), constrained_layout=True)
    bars = axis.barh(positions, auc_values - 0.5, left=0.5, color=BLUE, height=0.62)
    bars[0].set_color(ORANGE)

    for position, value in zip(positions, auc_values, strict=True):
        axis.text(value + 0.005, position, f"{value:.3f}", va="center", fontsize=8)

    axis.set_yticks(positions, features)
    axis.invert_yaxis()
    axis.set_xlim(0.5, 0.80)
    axis.set_xlabel("AUC individual orientado")
    axis.set_title("Capacidad discriminante de las principales características (100 eventos)")
    finish_axis(axis, "x")

    figure.savefig(OUTPUT_DIR / "caracteristicas_discriminantes.png", dpi=300, bbox_inches="tight")
    plt.close(figure)


def plot_session_stability() -> None:
    sessions = [
        "2144641057",
        "5265929106",
        "5815391283",
        "7409188284",
        "8872593360",
        "9031593624",
        "9838420452",
    ]
    roles = ["Enrolamiento"] * 5 + ["Validación"] * 2
    alarm_rates = np.array([9.0, 12.3, 6.3, 18.0, 8.3, 7.3, 12.5])
    positions = np.arange(len(sessions))
    colors = [BLUE if role == "Enrolamiento" else ORANGE for role in roles]

    figure, axis = plt.subplots(figsize=(7.7, 3.7), constrained_layout=True)
    bars = axis.barh(positions, alarm_rates, color=colors, height=0.62)
    for bar, role in zip(bars, roles, strict=True):
        if role == "Validación":
            bar.set_hatch("///")

    for position, value in zip(positions, alarm_rates, strict=True):
        axis.text(value + 0.35, position, f"{value:.1f} %", va="center", fontsize=8)

    axis.axvline(10, color=GRAY, linestyle="--", linewidth=1.2)
    axis.set_yticks(positions, sessions)
    axis.invert_yaxis()
    axis.set_xlim(0, 20.5)
    axis.set_xlabel("Ventanas legítimas enviadas a alarma")
    axis.set_ylabel("Sesión")
    axis.set_title("Variación de la tasa de alarma entre sesiones legítimas")
    axis.xaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:.0f} %"))
    axis.legend(
        handles=[
            Patch(facecolor=BLUE, label="Enrolamiento"),
            Patch(facecolor=ORANGE, hatch="///", label="Validación"),
            Line2D([0], [0], color=GRAY, linestyle="--", linewidth=1.2, label="Límite: 10 %"),
        ],
        frameon=False,
        loc="lower right",
        fontsize=8,
    )
    finish_axis(axis, "x")

    figure.savefig(OUTPUT_DIR / "estabilidad_sesiones.png", dpi=300, bbox_inches="tight")
    plt.close(figure)


def plot_multiuser_performance() -> None:
    """Compara separabilidad y errores de Isolation Forest entre las diez cuentas."""
    users = ["user7", "user9", "user12", "user15", "user16", "user20", "user21", "user23", "user29", "user35"]
    auc = np.array([0.861486, 0.754803, 0.551931, 0.678254, 0.497291,
                    0.650000, 0.611179, 0.420654, 0.576163, 0.506849])
    far = 100 * np.array([0.000000, 0.000000, 0.040816, 0.057143, 0.263158,
                          0.950000, 1.000000, 0.212121, 0.900000, 0.000000])
    frr = 100 * np.array([0.638889, 1.000000, 0.928571, 0.888889, 0.735294,
                          0.000000, 0.000000, 0.842105, 0.069767, 1.000000])
    positions = np.arange(len(users))

    figure, axes = plt.subplots(2, 1, figsize=(8.2, 5.8), sharex=True, constrained_layout=True)

    auc_axis = axes[0]
    colors = [ORANGE if value >= 0.80 else BLUE for value in auc]
    auc_axis.bar(positions, auc, color=colors, width=0.68)
    auc_axis.axhline(0.50, color=GRAY, linestyle=":", linewidth=1.1, label="Azar: 0.50")
    auc_axis.axhline(0.80, color=GRAY, linestyle="--", linewidth=1.1, label="Referencia: 0.80")
    auc_axis.set_ylim(0.35, 0.92)
    auc_axis.set_ylabel("AUC")
    auc_axis.set_title("(a) Separabilidad de Isolation Forest por usuario")
    auc_axis.legend(frameon=False, loc="upper right", fontsize=8, ncol=2)
    finish_axis(auc_axis, "y")

    error_axis = axes[1]
    width = 0.36
    error_axis.bar(positions - width / 2, far, width=width, color=ORANGE, label="FAR")
    error_axis.bar(positions + width / 2, frr, width=width, color=GREEN, label="FRR")
    error_axis.axhline(10, color=GRAY, linestyle="--", linewidth=1.1, label="Referencia: 10 %")
    error_axis.set_ylim(0, 108)
    error_axis.set_ylabel("Tasa")
    error_axis.set_xlabel("Cuenta evaluada")
    error_axis.set_title("(b) Errores con el umbral legítimo propio de cada usuario")
    error_axis.set_xticks(positions, users, rotation=35, ha="right")
    error_axis.yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"{value:.0f} %"))
    error_axis.legend(frameon=False, loc="upper center", fontsize=8, ncol=3)
    finish_axis(error_axis, "y")

    figure.savefig(OUTPUT_DIR / "desempeno_por_usuario.png", dpi=300, bbox_inches="tight")
    plt.close(figure)


def main() -> None:
    plot_window_metrics()
    plot_feature_auc()
    plot_session_stability()
    plot_multiuser_performance()


if __name__ == "__main__":
    main()
