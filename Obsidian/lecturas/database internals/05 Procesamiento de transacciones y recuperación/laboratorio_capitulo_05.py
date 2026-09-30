"""Experimentos didácticos, no implementación de un motor de bases de datos.
Ejecutar con Python 3. Solo utiliza la biblioteca estándar.
"""
from collections import deque

SECUENCIA = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

def cache_trace(capacidad, politica):
    cola = deque()
    misses = 0
    filas = []
    for pagina in SECUENCIA:
        hit = pagina in cola
        if hit and politica == 'LRU':
            cola.remove(pagina)
            cola.append(pagina)
        if not hit:
            misses += 1
            if len(cola) == capacidad:
                cola.popleft()
            cola.append(pagina)
        filas.append((pagina, 'hit' if hit else 'miss', tuple(cola), misses))
    return filas

def tiene_ciclo(aristas):
    nodos = {n for par in aristas for n in par}
    adyacencia = {n: set() for n in nodos}
    for origen, destino in aristas:
        adyacencia[origen].add(destino)
    estado = {}
    def visitar(nodo):
        if estado.get(nodo) == 1:
            return True
        if estado.get(nodo) == 2:
            return False
        estado[nodo] = 1
        if any(visitar(siguiente) for siguiente in adyacencia[nodo]):
            return True
        estado[nodo] = 2
        return False
    return any(visitar(nodo) for nodo in sorted(nodos))

def grafo_conflictos(historia):
    """R/W sobre registros exactos; no modela rangos, versiones ni view equivalence."""
    aristas = set()
    for i, (tx1, op1, item1) in enumerate(historia):
        for tx2, op2, item2 in historia[i + 1:]:
            if tx1 != tx2 and item1 == item2 and 'W' in (op1, op2):
                aristas.add((tx1, tx2))
    return aristas

if __name__ == '__main__':
    print('SECUENCIA:', SECUENCIA)
    for politica in ('FIFO', 'LRU'):
        for capacidad in (3, 4):
            traza = cache_trace(capacidad, politica)
            print(f'{politica}, {capacidad} frames: {traza[-1][-1]} misses')
    print('\nTRAZA FIFO (colas: antigua -> nueva)')
    for a, b in zip(cache_trace(3, 'FIFO'), cache_trace(4, 'FIFO')):
        print(f'{a[0]}: 3 frames {a[1]:4} {a[2]} | 4 frames {b[1]:4} {b[2]}')
    historia = [
        ('T1', 'R', 'A'), ('T1', 'R', 'B'),
        ('T2', 'R', 'A'), ('T2', 'R', 'B'),
        ('T1', 'W', 'A'), ('T2', 'W', 'B'),
    ]
    conflictos = grafo_conflictos(historia)
    print('\nWRITE SKEW: aristas', sorted(conflictos), 'ciclo', tiene_ciclo(conflictos))
    print('DEADLOCK: T1 espera T2 y T2 espera T1:', tiene_ciclo({('T1', 'T2'), ('T2', 'T1')}))
    print('ESPERA SIN CICLO: T1 espera T2:', tiene_ciclo({('T1', 'T2')}))
