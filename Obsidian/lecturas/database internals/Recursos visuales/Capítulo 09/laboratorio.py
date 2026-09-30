"""Ejemplos didácticos del capítulo 9; Python 3, solo biblioteca estándar."""
import math

def phi_normal(espera_ms, media_ms, desviacion_ms):
    if desviacion_ms <= 0:
        raise ValueError('La dispersión debe ser positiva')
    z = (espera_ms - media_ms) / desviacion_ms
    cola = .5 * math.erfc(z / math.sqrt(2))
    return -math.log10(max(cola, 1e-300))

def mezcla(contador, ultimo_avance, recibido, instante):
    # Una sola generación del miembro: no se simulan reinicios.
    return (recibido, instante) if recibido > contador else (contador, ultimo_avance)

def fuse_simplificado(caido, dependencias):
    # Rondas ideales: cada miembro induce silencio si vigila a uno silencioso.
    # No simula timers, transporte ni las reglas completas de FUSE.
    silenciosos = {caido}
    etapas = [set(silenciosos)]
    while True:
        nuevos = silenciosos | {p for p, otros in dependencias.items()
                                 if otros & silenciosos}
        if nuevos == silenciosos:
            return etapas
        silenciosos = nuevos
        etapas.append(set(silenciosos))

def main():
    print('Phi, umbral didáctico = 3')
    for espera, media, desviacion in [(100,100,20), (140,100,20),
                                      (160,100,20), (180,100,20), (160,150,50)]:
        valor = phi_normal(espera, media, desviacion)
        print(f'{espera:3d} ms, media={media}, sd={desviacion}: phi={valor:.3f}; sospecha={valor>=3}')
    contador, avance = 41, 0
    print('\nGossip: contador y último instante de avance')
    for instante, recibido in [(2,42), (4,42), (6,40)]:
        contador, avance = mezcla(contador, avance, recibido, instante)
        print(f't={instante}s recibe {recibido}: contador={contador}, avance={avance}s')
    print(f't=7.1s: silencio={7.1-avance:.1f}s; sospecha={7.1-avance>5}')
    print('\nFUSE simplificado: miembros silenciosos por etapa')
    for i, etapa in enumerate(fuse_simplificado('B', {'A':{'D'}, 'B':set(), 'C':{'D'}, 'D':{'B'}})):
        print(i, ', '.join(sorted(etapa)))

if __name__ == '__main__':
    main()
