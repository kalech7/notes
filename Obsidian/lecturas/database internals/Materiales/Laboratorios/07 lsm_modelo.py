"""Modelo didáctico de versiones LSM. No modela I/O durable ni concurrencia real.

Ejecutar: python3 'Obsidian/lecturas/database internals/Materiales/Laboratorios/07 lsm_modelo.py'
"""
from dataclasses import dataclass
from heapq import heappush, heappop
from itertools import groupby
from math import exp

@dataclass(frozen=True)
class Record:
    key: int
    version: int
    value: str | None  # None significa tombstone

def merge(sources):
    """Una cabeza por fuente; admite varias versiones de una clave por fuente."""
    streams=[iter(sorted(s,key=lambda r:(r.key,-r.version))) for s in sources]
    heap=[]
    def refill(index):
        record=next(streams[index],None)
        if record is not None:
            heappush(heap,(record.key,-record.version,index,record))
    for i in range(len(streams)):
        refill(i)
    while heap:
        _,_,index,record=heappop(heap)
        yield record
        refill(index)

def lookup(sources,key,snapshot=float('inf')):
    eligible=[r for source in sources for r in source
              if r.key==key and r.version<=snapshot]
    return max(eligible,key=lambda r:r.version).value if eligible else None

def scan(sources,snapshot=float('inf')):
    result={}
    for key,group in groupby(merge(sources),key=lambda r:r.key):
        versions=[r for r in group if r.version<=snapshot]
        if versions:
            latest=max(versions,key=lambda r:r.version)
            if latest.value is not None:
                result[key]=latest.value
    return result

def compact(inputs,*,covers_all_sources=False,active_snapshots=()):
    """Retención conservadora: con snapshots se conservan todas las versiones.

    Purga tombstones solo si se cubren todas las fuentes y no hay snapshots.
    No representa seguridad de eliminación en un sistema replicado.
    """
    if active_snapshots:
        return list(merge(inputs))
    output=[]
    for _,group in groupby(merge(inputs),key=lambda r:r.key):
        latest=max(group,key=lambda r:r.version)
        if latest.value is not None or not covers_all_sources:
            output.append(latest)
    return output

old=[Record(10,1,'rojo'),Record(20,1,'naranja'),Record(30,1,'azul')]
new=[Record(10,2,'verde'),Record(20,3,None),Record(40,2,'gris')]
expected={10:'verde',30:'azul',40:'gris'}
assert lookup([old,new],10)=='verde'
assert lookup([old,new],20) is None
assert lookup([old,new],10,snapshot=1)=='rojo'
assert lookup([old,new],20,snapshot=2)=='naranja'
assert scan([old,new])==expected
# Compactación parcial conserva el tombstone que protege frente a fuentes ajenas.
partial=compact([new])
assert Record(20,3,None) in partial
assert scan([old,partial])==expected
# Quitar incorrectamente la marca resucita el valor antiguo.
wrong=[r for r in partial if r.value is not None]
assert lookup([old,wrong],20)=='naranja'
# Con cobertura completa y sin snapshots, la marca y el valor viejo se purgan.
complete=compact([old,new],covers_all_sources=True)
assert all(r.key!=20 for r in complete)
assert scan([complete])==expected
# Retener versiones mantiene snapshots y mezcla versiones de una misma fuente.
retained=compact([old,new],covers_all_sources=True,active_snapshots=(1,2))
assert lookup([retained],10,snapshot=1)=='rojo'
assert lookup([retained],20,snapshot=2)=='naranja'
assert scan([retained])==expected
# Un archivo recién creado no hace más nueva su versión lógica.
assert lookup([[Record(10,8,'vigente')],[Record(10,2,'antiguo')]],10)=='vigente'
# Ejemplo Bloom del libro: posiciones explícitas, no hashes implementados.
bits=[0]*16
for indices in ((3,5,10),(5,8,14)):
    for i in indices:
        bits[i]=1
assert all(bits[i] for i in (3,10,14)) # Falso positivo: key3 no fue insertada.
assert not all(bits[i] for i in (5,9,15))
p7=(1-exp(-7/10))**7
p20=(1-exp(-20/10))**20
assert .008<p7<.009
assert p20>p7
assert 150+150+220==520
assert (100+100+400)/100==6
assert 6*1.5==9
print('OK: consulta actual, snapshots, heap con versiones, compactación parcial y purga completa.')
print('OK: resurrección detectada, retención histórica y orden lógico independientes del archivo.')
print(f'OK: Bloom; p7={p7:.5%}, p20={p20:.5%}; espacio temporal=520 MB; amplificación=6.')
