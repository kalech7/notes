"""Modelos didácticos sin hilos, disco ni servicios externos. Python 3."""
from itertools import permutations
from dataclasses import dataclass, field
from copy import deepcopy

def carreras():
    resultados = []
    for orden in permutations(('R+', 'W+', 'R*', 'W*')):
        if orden.index('R+') > orden.index('W+') or orden.index('R*') > orden.index('W*'):
            continue
        x, local = 1, {}
        for paso in orden:
            quien = paso[1]
            if paso[0] == 'R':
                local[quien] = x
            else:
                x = local[quien] + 2 if quien == '+' else local[quien] * 2
        resultados.append((orden, x))
    assert len(resultados) == 6
    assert {x for _, x in resultados} == {2, 3, 4, 6}
    return resultados

def cola():
    pendientes = (160 - 100) * 3
    vaciado = pendientes / (100 - 70)
    assert pendientes == 180 and vaciado == 6
    return pendientes, vaciado

def fifo(entrada):
    ultimo, buffer, salida, historia = 0, set(), [], []
    for n in entrada:
        nueva = []
        if n > ultimo:
            buffer.add(n)
        while ultimo + 1 in buffer:
            ultimo += 1
            buffer.remove(ultimo)
            salida.append(ultimo)
            nueva.append(ultimo)
        historia.append((n, nueva, sorted(buffer), ultimo))
    assert salida == [1, 2, 3, 4, 5]
    assert not buffer
    return historia

@dataclass
class Estado:
    total: int = 0
    registro: dict = field(default_factory=dict)

class Cobros:
    def __init__(self, durable=None):
        self.estado = deepcopy(durable) if durable is not None else Estado()

    def cobrar(self, identificador, importe):
        if identificador in self.estado.registro:
            guardado = self.estado.registro[identificador]
            if guardado['importe'] != importe:
                raise ValueError('El ID ya representa otro contenido')
            return guardado['resultado']
        # Publicar snapshot completo modela un commit atómico.
        # No implementa durabilidad física ni una caída entre instrucciones.
        siguiente = deepcopy(self.estado)
        siguiente.total += importe
        siguiente.registro[identificador] = {'importe': importe, 'resultado': siguiente.total}
        self.estado = siguiente
        return siguiente.total

    def snapshot(self):
        return deepcopy(self.estado)

def ack_perdido():
    sin_dedup = 20 + 20
    s = Cobros()
    respuesta_perdida = s.cobrar('pedido-42', 20)
    assert respuesta_perdida == 20
    assert s.cobrar('pedido-42', 20) == 20
    assert s.estado.total == 20
    recuperado = Cobros(s.snapshot())
    assert recuperado.cobrar('pedido-42', 20) == 20
    assert recuperado.estado.total == 20
    olvidado = Cobros(Estado(total=20))
    assert olvidado.cobrar('pedido-42', 20) == 40
    try:
        recuperado.cobrar('pedido-42', 30)
    except ValueError:
        pass
    else:
        raise AssertionError('No se rechazó reutilización incompatible del ID')
    assert sin_dedup == 40
    return sin_dedup, recuperado.estado.total, olvidado.estado.total

if __name__ == '__main__':
    print('Carreras:', carreras())
    print('Cola: pendientes y segundos de vaciado:', cola())
    print('FIFO: entrada, entrega, buffer, procesado:', fifo([1, 3, 2, 3, 5, 4]))
    print('Cobro: sin dedup, durable, ID olvidado:', ack_perdido())
    print('Todas las aserciones pasaron. Modelo didáctico, sin fallos reales de disco.')
