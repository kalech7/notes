"""Regresión, gradientes y umbrales sin bibliotecas de ML."""

from __future__ import annotations

import math


def linear_loss_and_grad(xs: list[float], ys: list[float], w: float, b: float) -> tuple[float, float, float]:
    n = len(xs)
    residuals = [w * x + b - y for x, y in zip(xs, ys)]
    loss = sum(r * r for r in residuals) / (2.0 * n)
    grad_w = sum(r * x for r, x in zip(residuals, xs)) / n
    grad_b = sum(residuals) / n
    return loss, grad_w, grad_b


def fit_linear(xs: list[float], ys: list[float], lr: float = 0.05, steps: int = 2000) -> tuple[float, float, list[float]]:
    w = b = 0.0
    history = []
    for step in range(steps):
        loss, grad_w, grad_b = linear_loss_and_grad(xs, ys, w, b)
        if step in (0, steps - 1):
            history.append(loss)
        w -= lr * grad_w
        b -= lr * grad_b
    return w, b, history


def sigmoid(z: float) -> float:
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    exp_z = math.exp(z)
    return exp_z / (1.0 + exp_z)


def bce_from_logit(z: float, y: int) -> float:
    return max(z, 0.0) - z * y + math.log1p(math.exp(-abs(z)))


def finite_logit_grad(z: float, y: int, h: float = 1e-5) -> float:
    return (bce_from_logit(z + h, y) - bce_from_logit(z - h, y)) / (2.0 * h)


def confusion(labels: list[int], scores: list[float], threshold: float) -> dict[str, int | float]:
    predictions = [int(score >= threshold) for score in scores]
    tp = sum(y == 1 and p == 1 for y, p in zip(labels, predictions))
    fp = sum(y == 0 and p == 1 for y, p in zip(labels, predictions))
    fn = sum(y == 1 and p == 0 for y, p in zip(labels, predictions))
    tn = sum(y == 0 and p == 0 for y, p in zip(labels, predictions))
    precision = tp / (tp + fp) if tp + fp else 0.0
    recall = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn, "precision": precision, "recall": recall, "f1": f1}


def main() -> None:
    xs = [-2.0, -1.0, 0.0, 1.0, 2.0]
    ys = [-3.0, -1.0, 1.0, 3.0, 5.0]
    w, b, history = fit_linear(xs, ys)
    assert history[-1] < history[0] * 1e-6
    assert math.isclose(w, 2.0, abs_tol=1e-4)
    assert math.isclose(b, 1.0, abs_tol=1e-4)

    for z, y in [(-2.0, 0), (-0.2, 1), (1.5, 0), (3.0, 1)]:
        analytic = sigmoid(z) - y
        numeric = finite_logit_grad(z, y)
        assert math.isclose(analytic, numeric, rel_tol=1e-8, abs_tol=1e-8)

    labels = [0, 0, 0, 1, 1, 1]
    scores = [0.1, 0.35, 0.55, 0.45, 0.7, 0.95]
    low = confusion(labels, scores, 0.4)
    high = confusion(labels, scores, 0.8)
    assert low["recall"] > high["recall"]
    assert low["fp"] > high["fp"]

    print("Regresión: w=", round(w, 4), "b=", round(b, 4), "loss", [round(x, 6) for x in history])
    print("Umbral 0.4:", low)
    print("Umbral 0.8:", high)
    print("OK: regresión, gradiente logístico y compromiso de umbral verificados.")


if __name__ == "__main__":
    main()

