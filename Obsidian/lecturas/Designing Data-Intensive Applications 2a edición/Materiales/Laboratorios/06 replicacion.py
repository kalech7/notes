"""Laboratorio del capítulo 6 de DDIA. Solo biblioteca estándar.
Simulación en memoria de UNA clave: sin red, disco, réplicas ni fallos."""


class Servidor:
    """Un único servidor con una clave, como en la figura 6-15."""

    def __init__(self):
        self.version = 0
        self.hermanos = {}  # versión -> frozenset con el contenido del carrito

    def leer(self):
        return self.version, [self.hermanos[v] for v in sorted(self.hermanos)]

    def escribir(self, valor, contexto=None):
        base = 0 if contexto is None else contexto
        self.version += 1
        # Lo que tenga versión <= base ya lo vio el cliente y lo fusionó.
        self.hermanos = {v: x for v, x in self.hermanos.items() if v > base}
        self.hermanos[self.version] = frozenset(valor)
        return self.leer()


class Cliente:
    def __init__(self, nombre, servidor):
        self.nombre = nombre
        self.servidor = servidor
        self.contexto = None  # última versión que devolvió el servidor
        self.visto = []       # siblings recibidos junto con esa versión

    def fusionar(self):
        carrito = set()
        for hermano in self.visto:
            carrito |= hermano
        return carrito

    def leer(self):
        self.contexto, self.visto = self.servidor.leer()

    def agregar(self, articulo, enviar_contexto=True):
        carrito = self.fusionar()
        carrito.add(articulo)
        enviado = self.contexto if enviar_contexto else None
        self.contexto, self.visto = self.servidor.escribir(carrito, enviado)
        return enviado

    def resolver(self):
        self.contexto, self.visto = self.servidor.escribir(self.fusionar(), self.contexto)


def texto(servidor):
    return "  ".join("v%d={%s}" % (v, ", ".join(sorted(servidor.hermanos[v])))
                     for v in sorted(servidor.hermanos))


def figura_6_15():
    s = Servidor()
    c1, c2 = Cliente("C1", s), Cliente("C2", s)
    pasos = [(c1, "leche"), (c2, "huevos"), (c1, "harina"),
             (c2, "jamón"), (c1, "tocino")]
    for n, (cliente, articulo) in enumerate(pasos, start=1):
        enviado = cliente.agregar(articulo)
        ctx = "-" if enviado is None else enviado
        print("%d %s +%-7s contexto=%s -> %s" % (n, cliente.nombre, articulo, ctx, texto(s)))
    assert sorted(s.hermanos) == [4, 5]
    assert s.hermanos[4] == {"huevos", "jamón", "leche"}
    assert s.hermanos[5] == {"harina", "huevos", "leche", "tocino"}

    c3 = Cliente("C3", s)
    c3.leer()
    c3.resolver()
    print("C3 fusiona ->", texto(s))
    assert list(s.hermanos) == [6]


def union_resucita():
    inicial = {"ana", "beto"}
    dispositivo_1 = inicial - {"beto"}   # quita a Beto
    dispositivo_2 = inicial | {"carla"}  # añade a Carla
    return dispositivo_1 | dispositivo_2


def con_lapidas():
    altas = {("ana", "a1"), ("beto", "a2")}             # cada alta, con etiqueta única
    d1_altas, d1_lapidas = set(altas), {"a2"}           # dispositivo 1 quita a Beto
    d2_altas, d2_lapidas = altas | {("carla", "b1")}, set()
    altas_f, lapidas_f = d1_altas | d2_altas, d1_lapidas | d2_lapidas
    return {nombre for nombre, etiqueta in altas_f if etiqueta not in lapidas_f}


def comparar(a, b):
    nodos = set(a) | set(b)
    a_le_b = all(a.get(n, 0) <= b.get(n, 0) for n in nodos)
    b_le_a = all(b.get(n, 0) <= a.get(n, 0) for n in nodos)
    if a_le_b and b_le_a:
        return "iguales"
    if a_le_b:
        return "a antes que b"
    if b_le_a:
        return "b antes que a"
    return "concurrentes"


def fusionar_contador(a, b):
    return {n: max(a.get(n, 0), b.get(n, 0)) for n in set(a) | set(b)}


if __name__ == "__main__":
    figura_6_15()

    print("Unión ingenua:", sorted(union_resucita()))
    print("Con lápidas:  ", sorted(con_lapidas()))
    assert union_resucita() == {"ana", "beto", "carla"}
    assert con_lapidas() == {"ana", "carla"}

    casos = [({"R1": 1}, {"R1": 1, "R2": 1}),
             ({"R1": 1, "R2": 1}, {"R3": 1}),
             ({"R1": 3, "R2": 0}, {"R1": 1, "R2": 2})]
    for a, b in casos:
        print(a, "vs", b, "->", comparar(a, b))
    assert [comparar(a, b) for a, b in casos] == [
        "a antes que b", "concurrentes", "concurrentes"]

    r1, r2 = {"R1": 3}, {"R2": 2}
    f = fusionar_contador(r1, r2)
    print("Contador:", dict(sorted(f.items())), "total", sum(f.values()))
    assert sum(f.values()) == 5
    assert max(sum(r1.values()), sum(r2.values())) == 3  # máximo de totales: pierde 2
    assert fusionar_contador(f, r2) == f                  # fusionar otra vez no cambia nada

    print("Todas las comprobaciones pasaron.")
