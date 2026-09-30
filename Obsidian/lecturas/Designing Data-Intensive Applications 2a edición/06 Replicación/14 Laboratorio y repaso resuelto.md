---
title: "DDIA — Replicación: laboratorio de contextos y siblings, y repaso resuelto"
created: 2026-09-29
capitulo: 6
tags:
  - lecturas/ddia
  - arquitectura/replicacion
cobertura: "Impresas 243–244 y práctica de 220–242"
---

# DDIA — Replicación: laboratorio de contextos y siblings, y repaso resuelto

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Índice de Replicación]]

## El capítulo en cinco ideas

El resumen del libro vuelve al principio: replicar es mantener copias del mismo dato en varias máquinas, y sirve para cinco cosas. **Alta disponibilidad**: seguir funcionando aunque caiga una máquina, una zona o una región entera. **Durabilidad**: no perder datos aunque una máquina, o una región, falle para siempre. **Operación desconectada**: seguir trabajando durante un corte de red. **Latencia**: tener los datos cerca de los usuarios. **Escalabilidad**: atender más lecturas de las que admite una sola máquina, leyendo de réplicas.

La idea es simple y el problema es endiabladamente difícil, porque obliga a pensar en concurrencia y en todo lo que puede fallar: como mínimo, nodos no disponibles y cortes de red, sin contar fallos más insidiosos como la corrupción silenciosa de datos.

| Enfoque | Quién acepta escrituras | Punto fuerte | Precio |
|---|---|---|---|
| Un líder | Solo el líder, que envía el flujo de cambios a los seguidores | Fácil de entender, consistencia fuerte | Lecturas de seguidores pueden ser viejas; dependes del líder |
| Multilíder | Cualquiera de varios líderes, que se envían cambios entre sí | Tolera nodos caídos, cortes y picos de latencia | Resolución de conflictos, garantías más débiles |
| Sin líder | Varias réplicas a la vez; se lee también de varias | Igual que multilíder, sin failover | Igual que multilíder |

La replicación **síncrona o asíncrona** cambia mucho qué pasa ante un fallo: la asíncrona es rápida mientras todo va bien, pero si promueves a líder un seguidor atrasado puedes perder datos ya confirmados. Frente al retraso de replicación el libro propone tres modelos: **leer tus propias escrituras**, **lecturas monótonas** (no ver el pasado después de haber visto el presente) y **prefijo consistente** (ver pregunta y respuesta en orden causal). Por último, multilíder y sin líder convergen **detectando qué escrituras son concurrentes** (vectores de versión o similares) y **fusionándolas** (CRDT, LWW o resolución manual). El capítulo supuso que cada réplica guarda todo el conjunto de datos; el siguiente reparte los datos entre máquinas.

## Laboratorio: el carrito de la figura 6-15 en Python

El programa reproduce el algoritmo de [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/13 Causalidad versiones y vectores|la nota 13]] con un servidor y una clave, y añade tres miniexperimentos: borrado con unión frente a lápidas, comparación de vectores de versión y fusión de contadores. Es una **simulación en memoria**: no hay red, disco, réplicas reales ni fallos, así que no pretende parecerse a una base de datos distribuida. Solo usa la biblioteca estándar. El archivo listo para ejecutar está en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/Laboratorios/06 replicacion.py|06 replicacion.py]]; ejecuta `python3 "06 replicacion.py"` desde su carpeta. También puedes copiar el código siguiente.

```python
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
```

La salida esperada de la parte del carrito es:

```text
1 C1 +leche   contexto=- -> v1={leche}
2 C2 +huevos  contexto=- -> v1={leche}  v2={huevos}
3 C1 +harina  contexto=1 -> v2={huevos}  v3={harina, leche}
4 C2 +jamón   contexto=2 -> v3={harina, leche}  v4={huevos, jamón, leche}
5 C1 +tocino  contexto=3 -> v4={huevos, jamón, leche}  v5={harina, huevos, leche, tocino}
C3 fusiona -> v6={harina, huevos, jamón, leche, tocino}
```

Cada línea coincide con una fila de la tabla de la nota 13. Los carritos se imprimen ordenados alfabéticamente porque son conjuntos; en el libro aparecen en el orden en que se añadieron. `Servidor.escribir` es la regla 4 del algoritmo en una línea: conserva solo las versiones mayores que el contexto. `Cliente.agregar` es la regla 3: fusiona todo lo visto antes de añadir. El cliente C3 demuestra cómo se cierra el conflicto: lee con contexto 5, fusiona los dos siblings y su escritura los sobrescribe a ambos.

## Ejercicios resueltos

> [!question]- 1. En el paso 4, C2 escribe **sin** contexto (`c2.agregar("jamón", enviar_contexto=False)`). ¿Qué siblings quedan y cómo termina el paso 5?
> Tras el paso 4 quedan tres: v2 {huevos}, v3 {harina, leche} y v4 {huevos, jamón, leche}. El servidor no puede saber que {huevos} está incluido en v4, porque no interpreta valores. En el paso 5, C1 envía contexto 3 y borra todo lo ≤ 3, incluido v2, que C1 sí había visto: el final vuelve a ser v4 y v5, como en el libro.

> [!question]- 2. ¿Por qué el laboratorio no sirve como base de datos distribuida?
> Usa un único contador por clave en un único servidor. Con varias réplicas aceptando escrituras, dos podrían asignar el mismo número a escrituras distintas: harían falta vectores de versión. Además no simula red, fallos, durabilidad ni reparación.

> [!question]- 3. n = 5. Para cada par (w, r) = (3, 3), (4, 2), (2, 3), di si hay intersección garantizada y cuántas réplicas caídas toleran escritura y lectura.
> (3, 3): 6 > 5, sí; toleran 2 y 2. (4, 2): 6 > 5, sí; toleran 1 y 3. (2, 3): 5 no es mayor que 5, no; toleran 3 y 2, pero una lectura puede no ver la última escritura.

> [!question]- 4. Dos regiones con tres réplicas cada una. Escribes con cuórum local en Europa y lees con cuórum local en EE. UU. ¿Ves tu escritura?
> No está garantizado: los dos grupos de réplicas no comparten ningún nodo. La escritura llegará a EE. UU. de forma asíncrona.

> [!question]- 5. Fusiona los contadores {R1: 4, R2: 1} y {R1: 2, R2: 3, R3: 1}. ¿Cuál es el total? ¿Qué daría el máximo de totales?
> Máximo por componente: {R1: 4, R2: 3, R3: 1}, total 8. Los totales eran 5 y 6; su máximo, 6, perdería incrementos.

> [!question]- 6. Texto `dato`. A hace `insert(0, "[")`; B, concurrentemente, `insert(4, "]")`. ¿Qué operación aplica A tras transformar la de B?
> `insert(5, "]")`, porque la inserción de A en una posición anterior desplaza todo una posición. Ambos terminan en `[dato]`.

> [!question]- 7. Un saldo de 50 € es un contador CRDT. Dos réplicas aprueban a la vez sendas retiradas de 30 €. ¿Qué pasa?
> Ambas convergen a −10 €. El CRDT no perdió operaciones, pero no puede proteger «saldo ≥ 0»: esa regla exige coordinar antes de aprobar.

> [!question]- 8. Una clave de configuración se lee una vez al mes y su réplica estuvo caída durante una escritura. ¿Qué mecanismo la reparará antes?
> Read repair no, porque casi no hay lecturas. Hinted handoff, si otra réplica guardó la pista; si no, la antientropía de fondo.

> [!question]- 9. Una app de notas personales debe funcionar sin red y el usuario usa móvil y portátil. ¿Qué enfoque y qué resolución de conflictos?
> Multilíder con un sync engine: cada dispositivo es un líder. Para el texto, un CRDT u OT que conserve las ediciones de ambos dispositivos; LWW perdería párrafos.

> [!question]- 10. ¿w + r > n convierte una base tipo Dynamo en linealizable?
> No. Garantiza que los grupos de nodos se solapen, pero las lecturas concurrentes con una escritura, las escrituras fallidas a medias, el LWW con relojes, las restauraciones y los rebalanceos pueden devolver valores viejos o inesperados.

## Referencias

PDF 47–48 · impresas 243–244 (resumen del capítulo). Enlaces: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=47|PDF 47 · impresa 243]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=48|PDF 48 · impresa 244]]. El laboratorio adapta la figura 6-15 ([[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=44|PDF 44 · impresa 240]]); los demás experimentos y todos los ejercicios son propios.

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/13 Causalidad versiones y vectores|Causalidad, versiones y vectores]] · **Índice:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Replicación]] · **Siguiente capítulo:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/07 Sharding y particionado/00 Índice|Sharding y particionado]]
