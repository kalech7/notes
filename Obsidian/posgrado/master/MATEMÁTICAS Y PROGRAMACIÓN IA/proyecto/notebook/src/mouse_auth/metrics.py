"""Métricas de clasificación y biometría con convenciones explícitas."""

from __future__ import annotations

import math
from typing import Sequence


def classification_metrics(labels: Sequence[int], predictions: Sequence[int]) -> dict[str, float | int]:
    if len(labels) != len(predictions) or not labels:
        raise ValueError("labels y predictions deben tener igual longitud no vacía")
    if set(labels) - {0, 1} or set(predictions) - {0, 1}:
        raise ValueError("Solo se admiten etiquetas binarias 0/1")
    tp = sum(y == 1 and p == 1 for y, p in zip(labels, predictions))
    fp = sum(y == 0 and p == 1 for y, p in zip(labels, predictions))
    fn = sum(y == 1 and p == 0 for y, p in zip(labels, predictions))
    tn = sum(y == 0 and p == 0 for y, p in zip(labels, predictions))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2.0 * precision * recall / (precision + recall) if precision + recall else 0.0
    far = fn / (tp + fn) if tp + fn else 0.0
    frr = fp / (tn + fp) if tn + fp else 0.0
    return {
        "tp": tp, "fp": fp, "fn": fn, "tn": tn,
        "precision_impostor": precision,
        "recall_impostor": recall,
        "f1_impostor": f1,
        "far": far,
        "frr": frr,
        "accuracy": (tp + tn) / len(labels),
    }


def eer_operating_point(labels: Sequence[int], scores: Sequence[float]) -> dict[str, float]:
    if len(labels) != len(scores) or not labels:
        raise ValueError("labels y scores incompatibles")
    thresholds = [-math.inf, *sorted(set(float(score) for score in scores)), math.inf]
    best: dict[str, float] | None = None
    for threshold in thresholds:
        predictions = [int(score >= threshold) for score in scores]
        metrics = classification_metrics(labels, predictions)
        candidate = {
            "threshold": threshold,
            "far": float(metrics["far"]),
            "frr": float(metrics["frr"]),
            "eer": (float(metrics["far"]) + float(metrics["frr"])) / 2.0,
            "gap": abs(float(metrics["far"]) - float(metrics["frr"])),
        }
        if best is None or (candidate["gap"], candidate["eer"]) < (best["gap"], best["eer"]):
            best = candidate
    assert best is not None
    return best

