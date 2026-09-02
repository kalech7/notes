"""Genera los gráficos de la nota del experimento M06 con Iris.

El script reproduce la configuración del notebook original: dos clases y dos
variables, partición estratificada 70/30, semilla 42, Regresión Logística con
escalado y Random Forest con 300 árboles.
"""

from argparse import ArgumentParser
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.base import clone
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, log_loss, recall_score
from sklearn.model_selection import StratifiedKFold, train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


RANDOM_STATE = 42
TEST_SIZE = 0.30
FEATURES = ["sepalLength", "sepalWidth"]
NEGATIVE_CLASS = "versicolor"
POSITIVE_CLASS = "virginica"
MODEL_LR = "Regresión Logística"
MODEL_RF = "Random Forest"

PURPLE = "#6546c7"
GREEN = "#138a72"
ORANGE = "#d97706"
INK = "#1f2937"
GRAY = "#6b7280"
LIGHT_PURPLE = "#c4b5fd"

OUTPUT_DIR = Path(__file__).resolve().parents[1] / "assets"
DEFAULT_PROJECT_ROOT = Path("/Users/alech/Downloads/m06-experimento-logreg-rf")


def configure_style() -> None:
    """Aplica un estilo común para que los gráficos formen una sola serie."""
    plt.rcParams.update(
        {
            "figure.dpi": 160,
            "savefig.dpi": 200,
            "font.size": 10.5,
            "axes.titlesize": 14,
            "axes.labelsize": 10.5,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.grid": True,
            "grid.alpha": 0.18,
        }
    )


def log_loss_per_case(y_true, p_positive):
    """Calcula -log(probabilidad asignada a la clase verdadera) por fila."""
    y_array = np.asarray(y_true, dtype=float)
    p_array = np.asarray(p_positive, dtype=float)
    epsilon = np.finfo(float).eps
    p_array = np.clip(p_array, epsilon, 1.0 - epsilon)
    return -(
        y_array * np.log(p_array)
        + (1.0 - y_array) * np.log(1.0 - p_array)
    )


def positive_probability(model, X_evaluation):
    """Extrae P(y=1) sin asumir la posición de la clase en predict_proba."""
    positive_index = int(np.flatnonzero(model.classes_ == 1)[0])
    return model.predict_proba(X_evaluation)[:, positive_index]


def binary_metrics(y_true, probability):
    """Resume una probabilidad continua y su etiqueta al umbral 0.5."""
    prediction = (probability >= 0.5).astype(int)
    return {
        "log_loss": log_loss(y_true, probability, labels=[0, 1]),
        "accuracy": accuracy_score(y_true, prediction),
        "recall_virginica": recall_score(y_true, prediction, pos_label=1),
        "f1_virginica": f1_score(y_true, prediction, pos_label=1),
    }


def sign_flip_reference(
    differences,
    n_resamples=200_000,
    random_state=RANDOM_STATE,
    batch_size=20_000,
):
    """Aproxima la referencia bilateral conservando magnitudes y cambiando signos."""
    differences = np.asarray(differences, dtype=float)
    rng = np.random.default_rng(random_state)
    null_means = np.empty(n_resamples, dtype=float)

    start = 0
    while start < n_resamples:
        end = min(start + batch_size, n_resamples)
        signs = rng.choice([-1.0, 1.0], size=(end - start, differences.size))
        null_means[start:end] = (signs * differences).mean(axis=1)
        start = end

    observed = abs(differences.mean())
    extreme = np.abs(null_means) >= observed - 1e-15
    p_monte_carlo = (int(extreme.sum()) + 1) / (n_resamples + 1)
    return null_means, p_monte_carlo


def prepare_experiment(project_root: Path):
    """Carga Iris, divide los datos, ajusta los modelos y conserva cada par."""
    data_path = project_root / "data" / "iris.json"
    if not data_path.is_file():
        raise FileNotFoundError(f"No se encontró el dataset: {data_path}")

    iris = pd.read_json(data_path)
    data = iris.loc[
        iris["species"].isin([NEGATIVE_CLASS, POSITIVE_CLASS])
    ].copy()
    data["target"] = (data["species"] == POSITIVE_CLASS).astype(int)

    X = data[FEATURES]
    y = data["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        stratify=y,
        random_state=RANDOM_STATE,
    )

    models = {
        MODEL_LR: Pipeline(
            [
                ("scaler", StandardScaler()),
                ("model", LogisticRegression(max_iter=1000)),
            ]
        ),
        MODEL_RF: RandomForestClassifier(
            n_estimators=300,
            random_state=RANDOM_STATE,
        ),
    }
    fitted = {name: clone(model).fit(X_train, y_train) for name, model in models.items()}

    p_lr = positive_probability(fitted[MODEL_LR], X_test)
    p_rf = positive_probability(fitted[MODEL_RF], X_test)

    results = X_test.copy()
    results["species"] = data.loc[X_test.index, "species"]
    results["y_true"] = y_test
    results["p_lr"] = p_lr
    results["p_rf"] = p_rf
    results["pred_lr"] = (p_lr >= 0.5).astype(int)
    results["pred_rf"] = (p_rf >= 0.5).astype(int)
    results["loss_lr"] = log_loss_per_case(y_test, p_lr)
    results["loss_rf"] = log_loss_per_case(y_test, p_rf)
    results["d"] = results["loss_lr"] - results["loss_rf"]

    metrics = pd.DataFrame(
        {
            MODEL_LR: binary_metrics(y_test, p_lr),
            MODEL_RF: binary_metrics(y_test, p_rf),
        }
    ).T
    return data, X_train, y_train, X_test, y_test, models, results, metrics


def cross_validation_results(X_train, y_train, models):
    """Calcula cinco folds descriptivos y el solapamiento de sus entrenamientos."""
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
    splits = list(cv.split(X_train, y_train))
    rows = []
    training_sets = []

    for fold, (train_indices, validation_indices) in enumerate(splits, start=1):
        training_sets.append(set(train_indices.tolist()))
        X_fold_train = X_train.iloc[train_indices]
        y_fold_train = y_train.iloc[train_indices]
        X_validation = X_train.iloc[validation_indices]
        y_validation = y_train.iloc[validation_indices]

        for name, model in models.items():
            fitted = clone(model).fit(X_fold_train, y_fold_train)
            probability = positive_probability(fitted, X_validation)
            rows.append(
                {
                    "fold": fold,
                    "model": name,
                    **binary_metrics(y_validation, probability),
                }
            )

    shared_counts = []
    for index, first_train in enumerate(training_sets):
        for second_train in training_sets[index + 1 :]:
            shared_counts.append(len(first_train & second_train))

    return pd.DataFrame(rows), shared_counts


def plot_overlap(data, X_train, X_test) -> None:
    fig, ax = plt.subplots(figsize=(9.5, 5.6))
    class_colors = {NEGATIVE_CLASS: PURPLE, POSITIVE_CLASS: GREEN}
    train_ids = set(X_train.index)
    test_ids = set(X_test.index)

    for species, group in data.groupby("species"):
        train_group = group.loc[group.index.intersection(train_ids)]
        test_group = group.loc[group.index.intersection(test_ids)]
        ax.scatter(
            train_group[FEATURES[0]],
            train_group[FEATURES[1]],
            color=class_colors[species],
            alpha=0.55,
            s=54,
            label=f"{species} - entrenamiento",
        )
        ax.scatter(
            test_group[FEATURES[0]],
            test_group[FEATURES[1]],
            facecolors="white",
            edgecolors=class_colors[species],
            linewidths=1.8,
            s=82,
            label=f"{species} - test",
        )

    ax.set_title("Iris binario: las clases se solapan con solo dos variables")
    ax.set_xlabel("Longitud del sépalo")
    ax.set_ylabel("Anchura del sépalo")
    ax.legend(frameon=False, ncol=2, fontsize=9)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "iris-solapamiento-train-test.png", bbox_inches="tight")
    plt.close(fig)


def plot_metrics(metrics) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.6), constrained_layout=True)
    colors = [PURPLE, GREEN]

    values = metrics["log_loss"].to_numpy()
    bars = axes[0].bar(metrics.index, values, color=colors)
    axes[0].set_title("Log-loss: menor es mejor")
    axes[0].set_ylabel("Log-loss media")
    axes[0].set_ylim(0, max(values) * 1.25)
    axes[0].tick_params(axis="x", rotation=10)
    for bar, value in zip(bars, values):
        axes[0].text(bar.get_x() + bar.get_width() / 2, value + 0.025, f"{value:.3f}", ha="center")

    secondary = metrics[["accuracy", "recall_virginica", "f1_virginica"]].T
    x = np.arange(len(secondary.index))
    width = 0.36
    for offset, (model, color) in enumerate(zip(metrics.index, colors)):
        model_values = secondary[model].to_numpy()
        bars = axes[1].bar(x + (offset - 0.5) * width, model_values, width, label=model, color=color)
        for bar, value in zip(bars, model_values):
            axes[1].text(bar.get_x() + bar.get_width() / 2, value + 0.018, f"{value:.2f}", ha="center", fontsize=9)
    axes[1].set_title("Métricas tras aplicar el umbral 0.5")
    axes[1].set_ylabel("Proporción")
    axes[1].set_xticks(x, ["Accuracy", "Recall", "F1"])
    axes[1].set_ylim(0, 0.85)
    axes[1].legend(frameon=False, fontsize=9)

    fig.savefig(OUTPUT_DIR / "experimento-iris-metricas.png", bbox_inches="tight")
    plt.close(fig)


def plot_differences(results) -> None:
    ordered = results.sort_values("d").copy()
    values = ordered["d"].to_numpy()
    colors = np.where(values < 0, PURPLE, GREEN)
    positions = np.arange(1, len(values) + 1)
    mean = float(values.mean())
    median = float(np.median(values))

    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.bar(positions, values, color=colors, width=0.82)
    ax.axhline(0, color=INK, linewidth=1.2)
    ax.axhline(mean, color=ORANGE, linewidth=1.9, linestyle="--", label=f"Media = {mean:.3f}")
    ax.axhline(median, color=GRAY, linewidth=1.6, linestyle=":", label=f"Mediana = {median:.3f}")
    ax.set_title("Diferencia pareada por flor: loss_LR - loss_RF")
    ax.set_xlabel("Flores de test ordenadas por diferencia")
    ax.set_ylabel("Diferencia de log-loss")
    ax.text(0.01, 0.94, "Negativo: favorece a Regresión Logística", transform=ax.transAxes, color=PURPLE)
    ax.text(0.64, 0.94, "Positivo: favorece a Random Forest", transform=ax.transAxes, color=GREEN)
    ax.legend(frameon=False, loc="lower right")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "experimento-iris-diferencias.png", bbox_inches="tight")
    plt.close(fig)


def plot_effect_interval(results) -> None:
    differences = results["d"].to_numpy()
    n = differences.size
    mean = float(differences.mean())
    se = float(differences.std(ddof=1) / np.sqrt(n))
    critical = stats.t.ppf(0.975, df=n - 1)
    low, high = mean - critical * se, mean + critical * se

    fig, ax = plt.subplots(figsize=(10, 3.3))
    ax.axvline(0, color=ORANGE, linewidth=2, label="Referencia nula: 0")
    ax.hlines(0, low, high, color=PURPLE, linewidth=7)
    ax.scatter([low, high], [0, 0], s=110, facecolors="white", edgecolors=PURPLE, linewidths=2.5, zorder=3)
    ax.scatter([mean], [0], s=160, color=GREEN, zorder=4, label=f"Media = {mean:.3f}")
    ax.text(low, 0.08, f"{low:.3f}", ha="center")
    ax.text(mean, -0.11, f"{mean:.3f}", ha="center")
    ax.text(high, 0.08, f"{high:.3f}", ha="center")
    ax.set_title("IC t del 95 % para la diferencia media")
    ax.set_xlabel("Negativo favorece a Regresión Logística; positivo favorece a Random Forest")
    ax.set_yticks([])
    ax.set_ylim(-0.25, 0.25)
    ax.set_xlim(low - 0.09, 0.1)
    ax.legend(frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "experimento-iris-intervalo.png", bbox_inches="tight")
    plt.close(fig)


def plot_normality_diagnostic(results) -> tuple[float, float]:
    """Muestra la forma de las diferencias y su gráfico Q-Q normal."""
    differences = results["d"].to_numpy()
    shapiro_result = stats.shapiro(differences)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.8), constrained_layout=True)

    axes[0].hist(
        differences,
        bins=10,
        color=LIGHT_PURPLE,
        edgecolor="white",
        linewidth=1,
    )
    axes[0].axvline(
        differences.mean(),
        color=ORANGE,
        linewidth=2,
        linestyle="--",
        label=f"Media = {differences.mean():.3f}",
    )
    axes[0].axvline(
        np.median(differences),
        color=GREEN,
        linewidth=2,
        linestyle=":",
        label=f"Mediana = {np.median(differences):.3f}",
    )
    axes[0].set_title("Forma de las diferencias pareadas")
    axes[0].set_xlabel("d = loss_LR - loss_RF")
    axes[0].set_ylabel("Cantidad de flores")
    axes[0].legend(frameon=False)

    theoretical, ordered = stats.probplot(differences, dist="norm", fit=False)
    slope, intercept, _ = stats.probplot(differences, dist="norm", fit=True)[1]
    theoretical = np.asarray(theoretical)
    ordered = np.asarray(ordered)
    axes[1].scatter(theoretical, ordered, color=PURPLE, s=48, alpha=0.9)
    reference_x = np.array([theoretical.min(), theoretical.max()])
    axes[1].plot(
        reference_x,
        intercept + slope * reference_x,
        color=ORANGE,
        linewidth=2,
        label="Referencia normal ajustada",
    )
    axes[1].set_title("Gráfico Q-Q normal de d")
    axes[1].set_xlabel("Cuantiles teóricos normales")
    axes[1].set_ylabel("Diferencias observadas ordenadas")
    axes[1].legend(frameon=False, loc="upper left")
    axes[1].text(
        0.98,
        0.05,
        f"Shapiro-Wilk\nW = {shapiro_result.statistic:.4f}\np = {shapiro_result.pvalue:.2e}",
        transform=axes[1].transAxes,
        ha="right",
        va="bottom",
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9},
    )

    fig.suptitle(
        "Diagnóstico conjunto: la prueba no reemplaza la inspección visual",
        fontsize=14,
    )
    fig.savefig(
        OUTPUT_DIR / "experimento-iris-shapiro-wilk.png",
        bbox_inches="tight",
    )
    plt.close(fig)
    return float(shapiro_result.statistic), float(shapiro_result.pvalue)


def plot_sign_flip(results) -> float:
    differences = results["d"].to_numpy()
    observed = abs(float(differences.mean()))
    null_means, p_value = sign_flip_reference(differences)
    counts, edges = np.histogram(null_means, bins=80)
    centers = (edges[:-1] + edges[1:]) / 2
    colors = np.where(np.abs(centers) >= observed, ORANGE, LIGHT_PURPLE)

    fig, ax = plt.subplots(figsize=(10, 5.2))
    ax.bar(centers, counts, width=np.diff(edges), color=colors, edgecolor="white", linewidth=0.25)
    ax.axvline(-observed, color=PURPLE, linewidth=2, linestyle="--")
    ax.axvline(observed, color=PURPLE, linewidth=2, linestyle="--")
    ax.text(
        0.02,
        0.94,
        f"200 000 cambios de signo; p Monte Carlo = {p_value:.4f}",
        transform=ax.transAxes,
        va="top",
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9},
    )
    ax.set_title("Referencia Monte Carlo condicionada a cambios de signo")
    ax.set_xlabel("Media después de invertir signos aleatoriamente")
    ax.set_ylabel("Frecuencia")
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "experimento-iris-signos-monte-carlo.png", bbox_inches="tight")
    plt.close(fig)
    return p_value


def plot_cross_validation(cv_results, shared_counts) -> None:
    metrics = [
        ("log_loss", "Log-loss"),
        ("accuracy", "Accuracy"),
        ("recall_virginica", "Recall virginica"),
        ("f1_virginica", "F1 virginica"),
    ]
    model_colors = {MODEL_LR: PURPLE, MODEL_RF: GREEN}
    fig, axes = plt.subplots(2, 2, figsize=(11, 8), constrained_layout=True)

    for ax, (metric, title) in zip(axes.ravel(), metrics):
        for model, group in cv_results.groupby("model"):
            ax.plot(
                group["fold"],
                group[metric],
                marker="o",
                linewidth=2,
                color=model_colors[model],
                label=model,
            )
        ax.set_title(title)
        ax.set_xlabel("Fold")
        ax.set_xticks(range(1, 6))

    overlap = shared_counts[0] / 56
    axes[0, 0].legend(frameon=False, fontsize=9)
    fig.suptitle(
        f"Validación cruzada descriptiva: cada par de entrenamientos comparte {shared_counts[0]}/56 = {overlap:.0%}",
        fontsize=14,
    )
    fig.savefig(OUTPUT_DIR / "experimento-iris-cv-folds.png", bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument(
        "--project-root",
        type=Path,
        default=DEFAULT_PROJECT_ROOT,
        help="Carpeta del paquete m06-experimento-logreg-rf",
    )
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    configure_style()
    data, X_train, y_train, X_test, _, models, results, metrics = prepare_experiment(
        args.project_root.resolve()
    )
    cv_results, shared_counts = cross_validation_results(X_train, y_train, models)

    plot_overlap(data, X_train, X_test)
    plot_metrics(metrics)
    plot_differences(results)
    plot_effect_interval(results)
    shapiro_w, shapiro_p = plot_normality_diagnostic(results)
    p_signs = plot_sign_flip(results)
    plot_cross_validation(cv_results, shared_counts)

    differences = results["d"].to_numpy()
    t_result = stats.ttest_1samp(differences, popmean=0.0)
    se = differences.std(ddof=1) / np.sqrt(differences.size)
    critical = stats.t.ppf(0.975, df=differences.size - 1)
    low = differences.mean() - critical * se
    high = differences.mean() + critical * se

    assert np.isclose(metrics.loc[MODEL_LR, "log_loss"], 0.6361, atol=5e-5)
    assert np.isclose(metrics.loc[MODEL_RF, "log_loss"], 0.9348, atol=5e-5)
    assert np.isclose(differences.mean(), -0.298645, atol=5e-7)
    assert np.isclose(t_result.pvalue, 0.018849, atol=5e-7)
    assert np.isclose(shapiro_w, 0.748575, atol=5e-7)
    assert np.isclose(shapiro_p, 0.00000864, atol=5e-9)
    assert np.isclose(p_signs, 0.0145, atol=5e-5)
    assert min(shared_counts) == max(shared_counts) == 42

    print(f"Gráficos guardados en: {OUTPUT_DIR}")
    print(f"n={differences.size}; media(d)={differences.mean():.6f}")
    print(f"IC t 95 %=[{low:.6f}, {high:.6f}]")
    print(f"t({differences.size - 1})={t_result.statistic:.6f}; p={t_result.pvalue:.6f}")
    print(f"Shapiro-Wilk W={shapiro_w:.6f}; p={shapiro_p:.8f}")
    print(f"p por cambios de signo Monte Carlo={p_signs:.6f}")


if __name__ == "__main__":
    main()
