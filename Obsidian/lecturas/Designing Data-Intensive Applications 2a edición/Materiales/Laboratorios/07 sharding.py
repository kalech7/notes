"""Ejemplos deterministas de DDIA cap. 7: no conecta una base real."""
from collections import Counter


def modulo_cambia():
    claves = list(range(24))
    permanecen = [h for h in claves if h % 3 == h % 4]
    print("Módulo 3 -> 4: permanecen", permanecen)
    print("Se mueven", len(claves) - len(permanecen), "de", len(claves))
    assert permanecen == [0, 1, 2, 12, 13, 14]


def shards_fijos():
    # Figura 7-4: 20 shards en 4 nodos; cada nodo recibe una clase módulo 4.
    antes = {s: s % 4 for s in range(20)}
    despues = antes.copy()
    for s in [4, 9, 14, 19]:
        despues[s] = 4
    movidos = [s for s in antes if antes[s] != despues[s]]
    print("Shards fijos: movidos", movidos, "distribución", dict(Counter(despues.values())))
    assert movidos == [4, 9, 14, 19]
    assert sorted(Counter(despues.values()).values()) == [4, 4, 4, 4, 4]


def rangos_hash():
    # Hashes de la figura 7-5, ya calculados por el ejemplo del libro.
    hashes = [7372, 18805, 50537, 31579, 62253, 24510]
    shards = [h // 16384 for h in hashes]
    print("Hash -> shard:", list(zip(hashes, shards)))
    assert shards == [0, 1, 3, 1, 3, 1]
    assert 65535 // 16384 == 3


def rangos_virtuales():
    # Intervalos semiabiertos [inicio, fin) de figura 7-6.
    antes = [(0, 88, 1), (88, 128, 0), (128, 309, 2), (309, 398, 0),
             (398, 511, 2), (511, 672, 1), (672, 702, 2),
             (702, 930, 1), (930, 1024, 0)]
    despues = [(0, 60, 1), (60, 88, 3), (88, 128, 0),
               (128, 276, 2), (276, 309, 3), (309, 398, 0),
               (398, 511, 2), (511, 551, 1), (551, 672, 3),
               (672, 702, 2), (702, 930, 1), (930, 1024, 0)]
    def contar(rangos):
        resultado = Counter()
        for inicio, fin, nodo in rangos:
            resultado[nodo] += fin - inicio
        assert sum(resultado.values()) == 1024
        return dict(sorted(resultado.items()))
    print("Rangos antes:", contar(antes))
    print("Rangos después:", contar(despues))
    assert contar(antes) == {0: 223, 1: 477, 2: 324}
    assert contar(despues) == {0: 223, 1: 328, 2: 291, 3: 182}


def indices():
    locales = [{"rojo": {191, 306}, "negro": {214}},
               {"rojo": {768}, "plata": {515, 893}}]
    ids_locales = set().union(*(indice.get("rojo", set()) for indice in locales))
    global_rojo = {191, 306, 768}
    print("IDs rojos locales y global:", sorted(ids_locales))
    assert ids_locales == global_rojo
    # Un shard del índice entrega IDs; los registros pueden seguir en varios shards.
    shards_datos = {identificador // 500 for identificador in global_rojo}
    assert shards_datos == {0, 1}
    print("Recuperar registros completos requiere shards:", sorted(shards_datos))


if __name__ == "__main__":
    modulo_cambia()
    shards_fijos()
    rangos_hash()
    rangos_virtuales()
    indices()
    print("Todas las comprobaciones pasaron.")
