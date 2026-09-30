"""Modelos didácticos del capítulo 6; no implementan persistencia ni concurrencia real."""
from dataclasses import dataclass, replace
from bisect import bisect_left


@dataclass(frozen=True)
class Page:
    records: tuple = ()
    left: object = None
    right: object = None


def copy_path(page, path, key, value):
    if not path:
        records = dict(page.records)
        records[key] = value
        return replace(page, records=tuple(sorted(records.items())))
    direction, *remaining = path
    updated = copy_path(getattr(page, direction), remaining, key, value)
    return replace(page, **{direction: updated})


def apply_changes(base, changes):
    state = dict(base)
    for op, key, value in changes:
        if op == 'PUT':
            state[key] = value
        elif op == 'DELETE':
            state.pop(key, None)
        else:
            raise ValueError(op)
    return state


# None representa un tombstone en este modelo, no un valor admitido.
def read_levels(key, levels):
    for level in levels:  # reciente -> antiguo
        if key in level:
            return level[key]
    return None


@dataclass(frozen=True)
class Piece:
    name: str
    change: tuple = None
    previous: object = None
    base: tuple = ()


class Mapping:
    def __init__(self, head):
        self.head = head

    def cas(self, expected, replacement):
        # Simulación secuencial del contrato CAS. No es una primitiva atómica real.
        if self.head is expected:
            self.head = replacement
            return True
        return False


def reconstruct(head):
    changes = []
    current = head
    while current.change is not None:
        changes.append(current.change)
        current = current.previous
    return apply_changes(dict(current.base), reversed(changes))


def veb_order(root, height):
    if height == 1:
        return [root]
    bottom = 1 << ((height - 1).bit_length() - 1)
    top = height - bottom
    roots = [root]
    for _ in range(top):
        roots = [child for parent in roots for child in (2 * parent, 2 * parent + 1)]
    return veb_order(root, top) + [
        node for child_root in roots for node in veb_order(child_root, bottom)
    ]


def main():
    intact = Page(records=((10, 'A'), (20, 'B')))
    shared_leaf = Page(records=((50, 'E'), (60, 'F')))
    leaf = Page(records=((70, 10),))
    old_root = Page(left=intact, right=Page(left=shared_leaf, right=leaf))
    new_root = copy_path(old_root, ['right', 'right'], 70, 12)
    assert dict(old_root.right.right.records)[70] == 10
    assert dict(new_root.right.right.records)[70] == 12
    assert old_root.left is new_root.left
    assert old_root.right.left is new_root.right.left
    assert old_root.right is not new_root.right
    print('CoW: raíz antigua=10; nueva=12; dos regiones intactas siguen compartidas.')

    changes = [('PUT', 20, 'B2'), ('DELETE', 30, None), ('PUT', 40, 'D')]
    visible = apply_changes({10: 'A', 20: 'B', 30: 'C'}, changes)
    assert visible == {10: 'A', 20: 'B2', 40: 'D'}
    assert apply_changes(visible, []) == visible  # después de materializar el estado
    print('Base + buffer:', sorted(visible.items()))

    levels = [{70: None}, {}, {70: 'viejo'}]
    assert read_levels(70, levels) is None
    assert read_levels(70, levels[1:]) == 'viejo'  # eliminación prematura, a propósito
    merged = apply_changes({70: 'viejo'}, [('DELETE', 70, None)])
    assert 70 not in merged
    assert read_levels(70, [merged]) is None
    print('FD: el tombstone evita resurrección; solo se retira al limpiar la versión vieja.')

    base = Piece('H', base=(('A', 10), ('B', 20)))
    table = Mapping(base)
    expected_t1 = table.head
    expected_t2 = table.head
    d1 = Piece('D1', ('PUT', 'A', 12), expected_t1)
    d2 = Piece('D2', ('PUT', 'C', 7), expected_t2)
    assert table.cas(expected_t1, d1)
    assert not table.cas(expected_t2, d2)
    assert reconstruct(table.head) == {'A': 12, 'B': 20}
    retry_expected = table.head
    d2_retry = Piece("D2'", ('PUT', 'C', 7), retry_expected)
    assert table.cas(retry_expected, d2_retry)
    assert reconstruct(table.head) == {'A': 12, 'B': 20, 'C': 7}
    print("CAS: éxito de T1, fallo inicial de T2, reintento D2' -> D1 -> H.")

    head = Piece('delete', ('DELETE', 'B', None), table.head)
    before = reconstruct(head)
    consolidated = Piece('nueva base', base=tuple(sorted(before.items())))
    assert before == reconstruct(consolidated) == {'A': 12, 'C': 7}
    # Conservar head ilustra que un lector antiguo todavía podría tener esta referencia.
    assert reconstruct(head) == before
    print('Bw consolidado:', sorted(before.items()), '; representación antigua aún válida.')

    order = veb_order(1, 4)
    assert order == [1, 2, 3, 4, 8, 9, 5, 10, 11, 6, 12, 13, 7, 14, 15]
    assert sorted(order) == list(range(1, 16))
    route = [1, 3, 7, 15]
    veb_blocks = {order.index(node) // 4 for node in route}
    bfs_blocks = {(node - 1) // 4 for node in route}
    assert veb_blocks == {0, 3} and bfs_blocks == {0, 1, 3}
    print('vEB:', order, '; bloques de la ruta:', sorted(veb_blocks))

    originals = [[12, 24, 32, 34, 39], [22, 25, 28, 30, 35], [11, 16, 24, 26, 30]]
    c3 = originals[2]
    c2 = sorted(set(originals[1] + c3[1::2]))
    c1 = sorted(set(originals[0] + c2[1::2]))
    assert c2 == [16, 22, 25, 26, 28, 30, 35]
    assert c1 == [12, 22, 24, 26, 30, 32, 34, 39]
    results = [a[bisect_left(a, 27)] for a in originals]
    assert results == [32, 28, 30]
    print('Catálogos coherentes:', c1, c2, c3, '; lower bounds originales:', results)
    print('Todas las comprobaciones didácticas pasaron.')


if __name__ == '__main__':
    main()
