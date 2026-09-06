"""Laboratorio reproducible de probabilidad sin dependencias externas."""

from __future__ import annotations

import math
import random
import statistics


def bayes_from_counts(tp: int, fn: int, fp: int, tn: int) -> dict[str, float]:
    if min(tp, fn, fp, tn) < 0:
        raise ValueError("Los conteos no pueden ser negativos")
    return {
        "recall": tp / (tp + fn),
        "precision": tp / (tp + fp),
        "false_positive_rate": fp / (fp + tn),
        "prevalence": (tp + fn) / (tp + fn + fp + tn),
    }


def bernoulli_mean(p: float, n: int, rng: random.Random) -> float:
    return sum(rng.random() < p for _ in range(n)) / n


def sampling_sd(p: float, n: int, repetitions: int, seed: int) -> float:
    rng = random.Random(seed)
    means = [bernoulli_mean(p, n, rng) for _ in range(repetitions)]
    return statistics.stdev(means)


def binary_log_loss(y: int, p: float) -> float:
    if y not in (0, 1) or not 0.0 < p < 1.0:
        raise ValueError("y debe ser 0/1 y p debe estar en (0,1)")
    return -(y * math.log(p) + (1 - y) * math.log(1 - p))


def stable_softmax(logits: list[float]) -> list[float]:
    maximum = max(logits)
    exps = [math.exp(z - maximum) for z in logits]
    total = sum(exps)
    return [value / total for value in exps]


def main() -> None:
    rates = bayes_from_counts(tp=90, fn=10, fp=495, tn=9405)
    assert math.isclose(rates["recall"], 0.9)
    assert rates["precision"] < 0.16

    observed = []
    for n in (10, 100, 1000):
        sd = sampling_sd(p=0.3, n=n, repetitions=3000, seed=7)
        theory = math.sqrt(0.3 * 0.7 / n)
        observed.append(sd)
        assert abs(sd - theory) / theory < 0.08
        print(f"n={n:4d}  SD simulada={sd:.4f}  SE teórico={theory:.4f}")
    assert observed[0] > observed[1] > observed[2]

    losses = [binary_log_loss(1, p) for p in (0.99, 0.8, 0.5, 0.2, 0.01)]
    assert all(a < b for a, b in zip(losses, losses[1:]))

    probabilities = stable_softmax([1000.0, 999.0, 998.0])
    assert math.isclose(sum(probabilities), 1.0, rel_tol=1e-12)
    assert probabilities[0] > probabilities[1] > probabilities[2]

    print("Bayes:", {key: round(value, 4) for key, value in rates.items()})
    print("Log-loss:", [round(value, 4) for value in losses])
    print("Softmax estable:", [round(value, 4) for value in probabilities])
    print("OK: conteos, CLT, log-loss y estabilidad verificados.")


if __name__ == "__main__":
    main()

