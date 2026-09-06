"""Ejemplos de estabilidad y condicionamiento con Python estándar."""

from __future__ import annotations

import math


def stable_softmax(values: list[float]) -> list[float]:
    maximum = max(values)
    exps = [math.exp(value - maximum) for value in values]
    total = sum(exps)
    return [value / total for value in exps]


def solve_2x2(a: float, b: float, c: float, d: float, y1: float, y2: float) -> tuple[float, float]:
    determinant = a * d - b * c
    if abs(determinant) < 1e-18:
        raise ValueError("Sistema singular o demasiado cercano a singular")
    return (y1 * d - b * y2) / determinant, (a * y2 - y1 * c) / determinant


def residual(matrix: tuple[tuple[float, float], tuple[float, float]], x: tuple[float, float], b: tuple[float, float]) -> float:
    r0 = matrix[0][0] * x[0] + matrix[0][1] * x[1] - b[0]
    r1 = matrix[1][0] * x[0] + matrix[1][1] * x[1] - b[1]
    return math.hypot(r0, r1)


def main() -> None:
    x = 1e-12
    direct = math.sqrt(1.0 + x) - 1.0
    stable = x / (math.sqrt(1.0 + x) + 1.0)
    expected = 0.5e-12
    assert abs(stable - expected) < abs(direct - expected)

    probabilities = stable_softmax([1000.0, 999.0, 998.0])
    assert math.isclose(sum(probabilities), 1.0, rel_tol=1e-15)

    matrix = ((1.0, 1.0), (1.0, 1.000001))
    b = (2.0, 2.000001)
    solution = solve_2x2(1.0, 1.0, 1.0, 1.000001, *b)
    perturbed = solve_2x2(1.0, 1.0, 1.0, 1.000001, 2.0, 2.00000101)
    amplification = math.hypot(perturbed[0] - solution[0], perturbed[1] - solution[1]) / 1e-8
    assert amplification > 100_000
    assert residual(matrix, solution, b) < 1e-12

    print("Cancelación directa/estable:", direct, stable)
    print("Softmax estable:", [round(p, 6) for p in probabilities])
    print("Solución:", solution, "solución perturbada:", perturbed)
    print("Amplificación aproximada:", round(amplification))
    print("OK: cancelación, overflow evitado y sensibilidad verificados.")


if __name__ == "__main__":
    main()

