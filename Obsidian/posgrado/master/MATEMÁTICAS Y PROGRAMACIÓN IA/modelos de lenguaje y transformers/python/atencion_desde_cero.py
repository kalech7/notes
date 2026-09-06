"""Atención causal mínima usando solo la biblioteca estándar de Python.

El propósito es hacer visibles las operaciones; no busca rendimiento.
"""

from math import exp, sqrt


def transpose(matrix):
    return [list(col) for col in zip(*matrix)]


def matmul(a, b):
    b_t = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in b_t] for row in a]


def softmax_stable(row):
    maximum = max(row)
    shifted = [exp(value - maximum) for value in row]
    denominator = sum(shifted)
    return [value / denominator for value in shifted]


def causal_attention(q, k, v):
    """Calcula softmax(QK^T/sqrt(H))V con máscara causal."""

    head_dim = len(q[0])
    scores = matmul(q, transpose(k))
    scale = sqrt(head_dim)

    for i, row in enumerate(scores):
        for j in range(len(row)):
            row[j] = row[j] / scale if j <= i else float("-inf")

    weights = [softmax_stable(row) for row in scores]
    output = matmul(weights, v)
    return scores, weights, output


if __name__ == "__main__":
    q = [[1.0, 0.0], [0.8, 0.2], [0.2, 1.0]]
    k = [[1.0, 0.0], [0.6, 0.4], [0.0, 1.0]]
    v = [[10.0, 0.0], [0.0, 20.0], [5.0, 5.0]]

    scores, weights, output = causal_attention(q, k, v)

    for i, row in enumerate(weights):
        assert abs(sum(row) - 1.0) < 1e-12
        assert all(abs(row[j]) < 1e-12 for j in range(i + 1, len(row)))

    print("Pesos de atención:")
    for row in weights:
        print([round(value, 4) for value in row])

    print("\nSalida ponderada:")
    for row in output:
        print([round(value, 4) for value in row])

    print("\nComprobaciones superadas: filas suman 1 y el futuro recibe peso 0.")
