"""Gradiente, Taylor, VJP y condicionamiento con Python estándar."""

from __future__ import annotations

import math


def f(point: tuple[float, float]) -> float:
    x, y = point
    return x * x + 3.0 * x * y + y * y


def grad_f(point: tuple[float, float]) -> tuple[float, float]:
    x, y = point
    return 2.0 * x + 3.0 * y, 3.0 * x + 2.0 * y


def finite_difference(point: tuple[float, ...], function, h: float = 1e-5) -> list[float]:
    result = []
    for j in range(len(point)):
        plus = list(point)
        minus = list(point)
        plus[j] += h
        minus[j] -= h
        result.append((function(tuple(plus)) - function(tuple(minus))) / (2.0 * h))
    return result


def dot(a: tuple[float, ...] | list[float], b: tuple[float, ...] | list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("Vectores incompatibles")
    return sum(x * y for x, y in zip(a, b))


def transpose_matvec(matrix: list[list[float]], vector: list[float]) -> list[float]:
    if len(matrix) != len(vector):
        raise ValueError("El vector debe tener una entrada por fila")
    return [sum(matrix[i][j] * vector[i] for i in range(len(matrix))) for j in range(len(matrix[0]))]


def quadratic_descent(curvature_y: float, learning_rate: float, steps: int = 60) -> float:
    x, y = 2.0, 2.0
    for _ in range(steps):
        x -= learning_rate * x
        y -= learning_rate * curvature_y * y
    return 0.5 * (x * x + curvature_y * y * y)


def main() -> None:
    point = (1.0, 2.0)
    analytic = grad_f(point)
    numeric = finite_difference(point, f)
    assert all(math.isclose(a, n, rel_tol=1e-9, abs_tol=1e-9) for a, n in zip(analytic, numeric))

    direction = (0.01, -0.02)
    predicted = dot(analytic, direction)
    actual = f((point[0] + direction[0], point[1] + direction[1])) - f(point)
    assert abs(actual - predicted) < 0.002

    half = (direction[0] / 2.0, direction[1] / 2.0)
    err_full = abs(actual - predicted)
    actual_half = f((point[0] + half[0], point[1] + half[1])) - f(point)
    err_half = abs(actual_half - dot(analytic, half))
    assert err_half < err_full / 3.5

    matrix = [[2.0, 1.0], [0.0, 3.0], [-1.0, 4.0]]
    upstream = [0.5, -2.0, 1.0]
    vjp = transpose_matvec(matrix, upstream)
    assert vjp == [-0.0, -1.5]

    assert quadratic_descent(1.0, 0.1) < 1e-4
    assert not math.isfinite(quadratic_descent(100.0, 0.1)) or quadratic_descent(100.0, 0.1) > 1e20

    print("Gradiente analítico:", analytic)
    print("Gradiente numérico:", [round(x, 8) for x in numeric])
    print("Cambio predicho/real:", round(predicted, 6), round(actual, 6))
    print("VJP A^T·v:", vjp)
    print("OK: Taylor, gradient check, VJP y condicionamiento verificados.")


if __name__ == "__main__":
    main()

