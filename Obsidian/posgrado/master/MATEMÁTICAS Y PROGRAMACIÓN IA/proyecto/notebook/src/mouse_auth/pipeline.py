"""Pipeline por usuario: enrolamiento, validación legítima y test final."""

from __future__ import annotations

import csv
from dataclasses import dataclass
import json
import math
from pathlib import Path
from typing import Iterable

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

from .features import FEATURE_NAMES, extract_session_features
from .metrics import classification_metrics, eer_operating_point


@dataclass(frozen=True)
class Config:
    validation_fraction: float = 0.25
    legitimate_rejection_quantile: float = 0.95
    random_state: int = 7
    n_estimators: int = 200


def quantile(values: list[float], q: float) -> float:
    if not values or not 0.0 <= q <= 1.0:
        raise ValueError("Valores o cuantil inválidos")
    ordered = sorted(values)
    position = q * (len(ordered) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    return ordered[lower] * (upper - position) + ordered[upper] * (position - lower)


def load_labels(path: Path) -> dict[str, int]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = csv.DictReader(handle)
        return {row["filename"]: int(row["is_illegal"]) for row in rows}


def select_labeled_paths(paths: Iterable[Path], labels: dict[str, int]) -> tuple[list[Path], int]:
    """Separa el subconjunto público etiquetado del test privado sin etiquetas."""
    all_paths = list(paths)
    labeled = [path for path in all_paths if path.name in labels]
    return labeled, len(all_paths) - len(labeled)


def _matrix(paths: Iterable[Path]) -> list[list[float]]:
    return [[features[name] for name in FEATURE_NAMES] for features in map(extract_session_features, paths)]


def _split_training(paths: list[Path], fraction: float) -> tuple[list[Path], list[Path]]:
    if len(paths) < 3:
        raise ValueError("Se necesitan al menos tres sesiones legítimas")
    validation_count = max(1, round(len(paths) * fraction))
    validation_count = min(validation_count, len(paths) - 2)
    return paths[:-validation_count], paths[-validation_count:]


def _rms_scores(matrix) -> list[float]:
    return [math.sqrt(sum(float(value) ** 2 for value in row) / len(row)) for row in matrix]


def evaluate_user(user: str, data_dir: Path, labels: dict[str, int], config: Config) -> tuple[list[dict[str, object]], dict[str, object]]:
    train_paths = sorted((data_dir / "training_files" / user).glob("session_*"))
    all_test_paths = sorted((data_dir / "test_files" / user).glob("session_*"))
    test_paths, unlabeled_test_count = select_labeled_paths(all_test_paths, labels)
    if not test_paths:
        raise ValueError(f"No hay sesiones de test con etiqueta pública para {user}")
    enrollment_paths, validation_paths = _split_training(train_paths, config.validation_fraction)
    assert set(enrollment_paths).isdisjoint(validation_paths)

    enrollment = _matrix(enrollment_paths)
    validation = _matrix(validation_paths)
    test = _matrix(test_paths)
    scaler = StandardScaler().fit(enrollment)
    enrollment_z = scaler.transform(enrollment)
    validation_z = scaler.transform(validation)
    test_z = scaler.transform(test)
    y_test = [labels[path.name] for path in test_paths]

    forest = IsolationForest(
        n_estimators=config.n_estimators,
        contamination="auto",
        random_state=config.random_state,
    ).fit(enrollment_z)

    model_scores = {
        "rms_z": (_rms_scores(validation_z), _rms_scores(test_z)),
        "isolation_forest": (
            [-float(value) for value in forest.score_samples(validation_z)],
            [-float(value) for value in forest.score_samples(test_z)],
        ),
    }
    predictions_rows: list[dict[str, object]] = []
    metrics_by_model: dict[str, object] = {}
    for model_name, (validation_scores, test_scores) in model_scores.items():
        threshold = quantile(validation_scores, config.legitimate_rejection_quantile)
        predictions = [int(score >= threshold) for score in test_scores]
        metrics = classification_metrics(y_test, predictions)
        metrics_by_model[model_name] = {
            **metrics,
            "threshold_validation": threshold,
            "eer_exploratory_on_test": eer_operating_point(y_test, test_scores),
        }
        for path, label, score, prediction in zip(test_paths, y_test, test_scores, predictions):
            predictions_rows.append({
                "user": user,
                "session": path.name,
                "model": model_name,
                "label_is_illegal": label,
                "score_anomaly": score,
                "threshold": threshold,
                "prediction_alarm": prediction,
            })
    summary = {
        "training_sessions": len(train_paths),
        "enrollment_sessions": len(enrollment_paths),
        "validation_sessions": len(validation_paths),
        "test_sessions_total": len(all_test_paths),
        "test_sessions_labeled": len(test_paths),
        "test_sessions_unlabeled": unlabeled_test_count,
        "models": metrics_by_model,
    }
    return predictions_rows, summary


def run(data_dir: Path, output_dir: Path, config: Config = Config()) -> dict[str, object]:
    labels = load_labels(data_dir / "public_labels.csv")
    users = sorted(path.name for path in (data_dir / "training_files").iterdir() if path.is_dir())
    all_predictions: list[dict[str, object]] = []
    per_user: dict[str, object] = {}
    for user in users:
        rows, summary = evaluate_user(user, data_dir, labels, config)
        all_predictions.extend(rows)
        per_user[user] = summary

    aggregate: dict[str, object] = {}
    for model_name in ("rms_z", "isolation_forest"):
        rows = [row for row in all_predictions if row["model"] == model_name]
        aggregate[model_name] = classification_metrics(
            [int(row["label_is_illegal"]) for row in rows],
            [int(row["prediction_alarm"]) for row in rows],
        )

    output_dir.mkdir(parents=True, exist_ok=True)
    predictions_path = output_dir / "baseline_predictions.csv"
    with predictions_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(all_predictions[0]))
        writer.writeheader()
        writer.writerows(all_predictions)
    report = {"config": config.__dict__, "users": per_user, "aggregate": aggregate}
    (output_dir / "baseline_metrics.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    return report
