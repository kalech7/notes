"""Laboratorio didáctico S11: simulador local; no usa LLM, red ni credenciales.
Ejecutar: python3 s11_laboratorio_bucle.py
El JSON de salida contiene verificaciones y trazas. Un paso = una decisión.
"""
import json
import math
import re
from copy import deepcopy
from time import perf_counter

VENTAS = {'2026-02': 12000, '2026-03': 15000}


def total_ventas(mes):
    if not isinstance(mes, str) or not re.fullmatch(r'[0-9]{4}-(0[1-9]|1[0-2])', mes):
        raise ValueError('mes_invalido: se espera YYYY-MM')
    if mes not in VENTAS:
        raise ValueError('mes_no_disponible')
    return {'mes': mes, 'total': VENTAS[mes], 'moneda': 'USD',
            'definicion': 'ventas netas sin impuestos', 'fuente': 'ventas_demo_v1'}


def variacion_porcentual(base, actual):
    for v in (base, actual):
        if type(v) not in (int, float) or not math.isfinite(v):
            raise ValueError('se_esperan_numeros_finitos')
    if base == 0:
        raise ValueError('porcentaje_indefinido: base cero')
    return {'porcentaje': (actual - base) / base * 100}


REGISTRO = {'total_ventas': (total_ventas, {'mes'}),
            'variacion_porcentual': (variacion_porcentual, {'base', 'actual'})}


def ejecutar(llamada):
    """Contrato propio; valida un repertorio cerrado y convierte fallos en datos."""
    resultado = {'kind': 'result', 'call_id': llamada['id']}
    try:
        nombre, argumentos = llamada['name'], llamada['args']
        if nombre not in REGISTRO:
            raise ValueError('herramienta_desconocida')
        funcion, campos = REGISTRO[nombre]
        if not isinstance(argumentos, dict) or set(argumentos) != campos:
            raise ValueError('parametros_invalidos')
        resultado.update(ok=True, data=funcion(**argumentos))
    except Exception as error:
        resultado.update(ok=False, error=str(error))
    return resultado


def modelo_simulado(historial, escenario):
    """Política por reglas que enseña el protocolo; no mide inteligencia de un LLM."""
    resultados = [m for m in historial if m['kind'] == 'result']
    n = len(resultados)
    ident = f'c{n + 1}'
    def call(nombre, args):
        return {'kind': 'call', 'id': ident, 'name': nombre, 'args': args}
    if escenario == 'malformado':
        return {'kind': 'call', 'id': ident}  # falta contrato de llamada
    if escenario == 'id_repetido':
        mensaje = call('total_ventas', {'mes': '2026-02'})
        mensaje['id'] = 'c1'
        return mensaje
    if escenario == 'repeticion':
        return call('total_ventas', {'mes': '2026-02'})
    if resultados and not resultados[-1]['ok']:
        return {'kind': 'final', 'complete': False,
                'text': 'No se pudo completar: ' + resultados[-1]['error']}
    if n == 0:
        especiales = {
            'desconocida': ('borrar_datos', {}),
            'mes_invalido': ('total_ventas', {'mes': '2026-99'}),
            'sin_datos': ('total_ventas', {'mes': '2026-01'}),
            'base_cero': ('variacion_porcentual', {'base': 0, 'actual': 15000}),
        }
        nombre, args = especiales.get(escenario, ('total_ventas', {'mes': '2026-02'}))
        return call(nombre, args)
    if n == 1:
        return call('total_ventas', {'mes': '2026-03'})
    if n == 2:
        return call('variacion_porcentual', {
            'base': resultados[0]['data']['total'],
            'actual': resultados[1]['data']['total']})
    g = resultados[-1]['data']['porcentaje']
    return {'kind': 'final', 'complete': True,
            'text': f'Las ventas pasaron de 12000 a 15000 USD: crecimiento de {g:g} %. Fuente: ventas_demo_v1.'}


def correr(escenario='exito', max_decisiones=4):
    if type(max_decisiones) is not int or max_decisiones < 1:
        raise ValueError('max_decisiones debe ser entero positivo')
    historial = [{'kind': 'user', 'text': 'Compara marzo con febrero de 2026.'}]
    traza = [{'evento': 'inicio', 'pregunta': historial[0]['text'],
              'escenario': escenario, 'max_decisiones': max_decisiones}]
    usados = set()
    def cerrar(estado, texto, completo=False):
        traza.append({'evento': estado, 'texto': texto, 'complete': completo})
        return {'escenario': escenario, 'estado': estado, 'complete': completo,
                'respuesta': texto, 'historial': historial, 'traza': traza}
    for paso in range(1, max_decisiones + 1):
        decision = modelo_simulado(deepcopy(historial), escenario)
        if decision.get('kind') == 'final':
            return cerrar('respuesta_final', decision['text'], decision['complete'])
        campos = {'kind', 'id', 'name', 'args'}
        valido = (set(decision) == campos and decision['kind'] == 'call'
                  and isinstance(decision.get('id'), str) and bool(decision['id'])
                  and isinstance(decision.get('name'), str)
                  and isinstance(decision.get('args'), dict))
        if not valido or decision['id'] in usados:
            traza.append({'paso': paso, 'evento': 'propuesta_rechazada', 'propuesta': decision})
            return cerrar('error_protocolo', 'Mensaje mal formado o identificador repetido.')
        usados.add(decision['id'])
        historial.append(decision)
        traza.append({'paso': paso, 'evento': 'llamada', 'id': decision['id'],
                      'tool': decision['name'], 'input': decision['args']})
        inicio = perf_counter()
        resultado = ejecutar(decision)
        ms = (perf_counter() - inicio) * 1000
        historial.append(resultado)
        traza.append({'paso': paso, 'evento': 'resultado', 'tool': decision['name'],
                      'ms': round(ms, 4), **resultado})
    return cerrar('max_pasos_alcanzado',
                  'Se agotó el límite. Hay resultados registrados, pero no se emitió una respuesta final.')


def verificar():
    casos = [('exito', 4), ('exito', 3), ('repeticion', 3), ('desconocida', 4),
             ('mes_invalido', 4), ('sin_datos', 4), ('base_cero', 4),
             ('id_repetido', 4), ('malformado', 4)]
    corridas = [correr(c, n) for c, n in casos]
    esperado = ['respuesta_final', 'max_pasos_alcanzado', 'max_pasos_alcanzado',
                'respuesta_final', 'respuesta_final', 'respuesta_final',
                'respuesta_final', 'error_protocolo', 'error_protocolo']
    assert [r['estado'] for r in corridas] == esperado
    assert corridas[0]['complete'] and '25 %' in corridas[0]['respuesta']
    assert all(not r['complete'] for r in corridas[1:])
    # Invariante de las llamadas aceptadas: un resultado asociado, también en fallos.
    for corrida in corridas:
        h = corrida['historial']
        llamadas = [m['id'] for m in h if m['kind'] == 'call']
        resultados = [m['call_id'] for m in h if m['kind'] == 'result']
        assert llamadas == resultados and len(llamadas) == len(set(llamadas))
    for r, fragmento in zip(corridas[3:7], ['herramienta_desconocida', 'mes_invalido',
                                          'mes_no_disponible', 'base cero']):
        assert fragmento in r['respuesta']
    assert len([m for m in corridas[7]['historial'] if m['kind'] == 'call']) == 1
    assert not any(m['kind'] == 'call' for m in corridas[8]['historial'])
    # Cuentas de las notas y gráficos.
    contextos = [1000 + 500 * i for i in range(7)]
    assert contextos[-1] == 4000 and sum(contextos) == 17500
    assert math.isclose(variacion_porcentual(12000, 15000)['porcentaje'], 25)
    assert min(2.0, 1.8) - 0.9 >= 0.5
    assert min(2.0, 1.8) - 1.4 < 0.5
    return {'verificacion': '9 escenarios y cuentas correctos',
            'advertencia': 'Simulación por reglas, sin LLM ni API; datos ficticios.',
            'contextos_tokens': contextos, 'total_entradas_tokens': sum(contextos),
            'corridas': corridas}


if __name__ == '__main__':
    print(json.dumps(verificar(), ensure_ascii=False, indent=2))
