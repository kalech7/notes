#!/usr/bin/env python3
"""Modelo didáctico propio: conjuntos de quórum, escritura incompleta y G-counter.
No modela red, caídas, persistencia ni todo un protocolo distribuido.
Ejecutar con Python 3 desde cualquier directorio.
"""
from itertools import combinations, permutations
from functools import reduce


def merge(a, b):
    if len(a) != len(b):
        raise ValueError('Vectores de distinta longitud')
    return tuple(max(x, y) for x, y in zip(a, b))


def read_version(state, participants):
    """Las versiones escalares ya tienen un orden comparable en este modelo."""
    return max(state[node] for node in participants)


def main():
    nodes = ('A', 'B', 'C')
    quorums = list(combinations(nodes, 2))
    overlaps = [set(r) & set(w) for r in quorums for w in quorums]
    assert len(overlaps) == 9 and all(overlaps)
    print(f'Quórums: {len(overlaps)} cruces, todos con intersección')
    # Contraste: igualdad R+W=N no obliga a intersectar.
    assert not (set(('A', 'B')) & set(('C', 'D')))

    state = {'A': 1, 'B': 0, 'C': 0}
    first = read_version(state, ('A', 'B'))
    second = read_version(state, ('B', 'C'))
    assert (first, second) == (1, 0)
    print(f'Regresión por escritura incompleta: {first} → {second}')
    # Propagar a B antes de completar la primera lectura bloqueante.
    state['B'] = first
    repaired = read_version(state, ('B', 'C'))
    assert (first, repaired) == (1, 1)
    print(f'Con reparación previa: {first} → {repaired}')

    initial = ((1, 0, 0), (0, 0, 0), (0, 0, 1))
    target = (1, 0, 1)
    results = [reduce(merge, order) for order in permutations(initial)]
    assert all(result == target for result in results)
    for a in initial:
        assert merge(a, a) == a
        for b in initial:
            assert merge(a, b) == merge(b, a)
            for c in initial:
                assert merge(merge(a, b), c) == merge(a, merge(b, c))
    # Repetir estados intercalados no duplica el incremento.
    repeated = (initial[0], initial[2], initial[0], initial[1], initial[2])
    assert reduce(merge, repeated) == target
    print(f'G-counter: {list(target)}, valor = {sum(target)}')
    print('6 órdenes y duplicados convergen; propiedades verificadas en estos estados')
    print('Este modelo ilustra reglas y contraejemplos; no prueba una base real')


if __name__ == '__main__':
    main()
