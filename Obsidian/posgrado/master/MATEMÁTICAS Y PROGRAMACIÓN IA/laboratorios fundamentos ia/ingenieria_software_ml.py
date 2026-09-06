"""Contratos, configuración y evaluación reproducible sin escribir artefactos."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
import math
from typing import Protocol, Sequence


@dataclass(frozen=True)
class Config:
    seed: int = 7
    threshold: float = 0.5
    positive_label: int = 1

    def __post_init__(self) -> None:
        if not 0.0 <= self.threshold <= 1.0:
            raise ValueError("threshold debe estar en [0,1]")


class Scorer(Protocol):
    def score(self, rows: Sequence[Sequence[float]]) -> list[float]: ...


class FirstFeatureScorer:
    def score(self, rows: Sequence[Sequence[float]]) -> list[float]:
        return [float(row[0]) for row in rows]


def canonical_hash(value: object) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def evaluate(labels: Sequence[int], scores: Sequence[float], threshold: float) -> dict[str, float | int]:
    if len(labels) != len(scores):
        raise ValueError("labels y scores deben tener igual longitud")
    if not all(math.isfinite(score) for score in scores):
        raise ValueError("Todos los scores deben ser finitos")
    predictions = [int(score >= threshold) for score in scores]
    tp = sum(y == 1 and p == 1 for y, p in zip(labels, predictions))
    fp = sum(y == 0 and p == 1 for y, p in zip(labels, predictions))
    fn = sum(y == 1 and p == 0 for y, p in zip(labels, predictions))
    tn = sum(y == 0 and p == 0 for y, p in zip(labels, predictions))
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn, "accuracy": (tp + tn) / len(labels)}


@dataclass
class Experiment:
    config: Config
    scorer: Scorer

    def run(self, rows: Sequence[Sequence[float]], labels: Sequence[int]) -> dict[str, object]:
        scores = self.scorer.score(rows)
        metrics = evaluate(labels, scores, self.config.threshold)
        return {
            "run_id": canonical_hash(asdict(self.config))[:12],
            "config": asdict(self.config),
            "metrics": metrics,
            "predictions_hash": canonical_hash(scores),
        }


def main() -> None:
    config = Config(threshold=0.5)
    experiment = Experiment(config, FirstFeatureScorer())
    rows = [[0.1], [0.8], [0.7], [0.2]]
    labels = [0, 1, 0, 0]
    first = experiment.run(rows, labels)
    second = experiment.run(rows, labels)
    assert first == second
    assert first["metrics"] == {"tp": 1, "fp": 1, "fn": 0, "tn": 2, "accuracy": 0.75}
    assert canonical_hash({"a": 1, "b": 2}) == canonical_hash({"b": 2, "a": 1})
    try:
        Config(threshold=1.2)
    except ValueError:
        pass
    else:
        raise AssertionError("La configuración inválida debía fallar")
    print(json.dumps(first, indent=2, ensure_ascii=False))
    print("OK: configuración, contrato, validación y hashes verificados.")


if __name__ == "__main__":
    main()

