"""Genera el gráfico reproducible usado en la nota de elección de k."""

from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt


X = np.array(
    [
        [4.0, 5.0, 0.0, 0.0],
        [3.0, 4.0, 0.0, 0.0],
        [0.0, 1.0, 5.0, 4.0],
        [0.0, 1.0, 4.0, 3.0],
        [5.0, 6.0, 0.0, 0.0],
    ]
)

singular_values = np.linalg.svd(X, compute_uv=False)
k_values = np.arange(1, len(singular_values) + 1)
total_energy = np.sum(singular_values**2)
retained_energy = np.cumsum(singular_values**2) / total_energy * 100
relative_frobenius_error = np.sqrt(
    np.maximum(0.0, 1.0 - retained_energy / 100)
) * 100

plt.style.use("seaborn-v0_8-whitegrid")
figure, (spectrum_axis, criterion_axis) = plt.subplots(
    1, 2, figsize=(12, 4.8), constrained_layout=True
)

spectrum_axis.bar(k_values, singular_values, color="#6f5bd3")
spectrum_axis.set_yscale("log")
spectrum_axis.set_xticks(k_values)
spectrum_axis.set_xlabel("Componente singular i")
spectrum_axis.set_ylabel("Valor singular σᵢ (escala logarítmica)")
spectrum_axis.set_title(r"Espectro singular: el salto aparece después de $\sigma_2$")
for k, value in zip(k_values, singular_values, strict=True):
    spectrum_axis.annotate(
        f"{value:.4f}",
        (k, value),
        xytext=(0, 5),
        textcoords="offset points",
        ha="center",
        fontsize=9,
    )

criterion_axis.plot(
    k_values,
    retained_energy,
    marker="o",
    linewidth=2.5,
    color="#138a72",
    label="Energía algebraica retenida",
)
criterion_axis.plot(
    k_values,
    relative_frobenius_error,
    marker="s",
    linewidth=2.5,
    color="#d95f59",
    label="Error relativo de Frobenius",
)
criterion_axis.axvline(2, color="#444444", linestyle="--", linewidth=1.2)
criterion_axis.annotate(
    "k = 2\n99.962 % retenido\n1.941 % de error",
    xy=(2, retained_energy[1]),
    xytext=(2.25, 72),
    arrowprops={"arrowstyle": "->", "color": "#444444"},
    fontsize=9,
)
criterion_axis.set_xticks(k_values)
criterion_axis.set_ylim(-2, 105)
criterion_axis.set_xlabel("Cantidad de componentes conservadas k")
criterion_axis.set_ylabel("Porcentaje")
criterion_axis.set_title("Elegir k exige declarar qué cantidad se controla")
criterion_axis.legend(loc="center right", fontsize=9)

output_path = (
    Path(__file__).resolve().parents[1] / "assets" / "diagnostico-eleccion-k.png"
)
figure.savefig(output_path, dpi=220, facecolor="white")
plt.close(figure)

print(f"Gráfico guardado en: {output_path}")
for k, retained, error in zip(
    k_values, retained_energy, relative_frobenius_error, strict=True
):
    print(f"k={k}: retenido={retained:.6f} %, error_F={error:.6f} %")
