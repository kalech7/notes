"""MLP 2-4-1 para XOR con forward/backward explícitos."""

from __future__ import annotations

import math
import random


X = [[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
Y = [0.0, 1.0, 1.0, 0.0]


def sigmoid(z: float) -> float:
    return 1.0 / (1.0 + math.exp(-z))


def train(seed: int = 7, steps: int = 12_000, lr: float = 0.1):
    rng = random.Random(seed)
    w1 = [[rng.uniform(-0.8, 0.8) for _ in range(4)] for _ in range(2)]
    b1 = [0.0] * 4
    w2 = [rng.uniform(-0.8, 0.8) for _ in range(4)]
    b2 = 0.0
    losses = []

    for step in range(steps):
        gw1 = [[0.0] * 4 for _ in range(2)]
        gb1 = [0.0] * 4
        gw2 = [0.0] * 4
        gb2 = 0.0
        loss = 0.0

        for x, y in zip(X, Y):
            hidden = [math.tanh(sum(x[i] * w1[i][j] for i in range(2)) + b1[j]) for j in range(4)]
            logit = sum(hidden[j] * w2[j] for j in range(4)) + b2
            probability = sigmoid(logit)
            loss += -(y * math.log(probability + 1e-12) + (1.0 - y) * math.log(1.0 - probability + 1e-12))

            delta2 = probability - y
            for j in range(4):
                gw2[j] += delta2 * hidden[j]
                delta1 = delta2 * w2[j] * (1.0 - hidden[j] ** 2)
                gb1[j] += delta1
                for i in range(2):
                    gw1[i][j] += delta1 * x[i]
            gb2 += delta2

        scale = 1.0 / len(X)
        if step in (0, steps - 1):
            losses.append(loss * scale)
        for i in range(2):
            for j in range(4):
                w1[i][j] -= lr * gw1[i][j] * scale
        for j in range(4):
            b1[j] -= lr * gb1[j] * scale
            w2[j] -= lr * gw2[j] * scale
        b2 -= lr * gb2 * scale

    predictions = []
    for x in X:
        hidden = [math.tanh(sum(x[i] * w1[i][j] for i in range(2)) + b1[j]) for j in range(4)]
        probability = sigmoid(sum(hidden[j] * w2[j] for j in range(4)) + b2)
        predictions.append(probability)
    return predictions, losses


def main() -> None:
    predictions, losses = train()
    classes = [int(p >= 0.5) for p in predictions]
    assert classes == [0, 1, 1, 0]
    assert losses[-1] < 0.03
    again, _ = train()
    assert predictions == again
    print("Probabilidades XOR:", [round(p, 4) for p in predictions])
    print("Loss inicial/final:", [round(value, 6) for value in losses])
    print("OK: MLP no lineal, backward y reproducibilidad verificados.")


if __name__ == "__main__":
    main()

