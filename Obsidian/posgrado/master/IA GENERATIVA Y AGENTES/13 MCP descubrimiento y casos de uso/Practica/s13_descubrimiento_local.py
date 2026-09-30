"""Simulador educativo de descubrimiento; sin LLM, red ni transporte MCP real.

Ejecutar con Python 3. Genera s13_resultados_verificados.json junto al script.
El agente recibe catálogo y dispatcher: no contiene nombres específicos de tools.
La validación solo implementa el subconjunto de JSON Schema utilizado aquí.
"""
from copy import deepcopy
from pathlib import Path
import hashlib
import inspect
import json


class ServidorSimulado:
    def __init__(self):
        self.catalogo = {}
        self.funciones = {}

    def publicar(self, nombre, descripcion, esquema, funcion):
        if nombre in self.catalogo:
            raise ValueError('Nombre duplicado en servidor')
        self.catalogo[nombre] = {
            'name': nombre, 'description': descripcion, 'inputSchema': esquema}
        self.funciones[nombre] = funcion

    def listar(self):
        return deepcopy([self.catalogo[n] for n in sorted(self.catalogo)])

    def invocar(self, nombre, argumentos):
        if nombre not in self.catalogo:
            return {'isError': True, 'error': 'Herramienta desconocida'}
        try:
            validar(self.catalogo[nombre]['inputSchema'], argumentos)
            valor = self.funciones[nombre](**argumentos)
            return {'isError': False, 'resultado': valor}
        except (ValueError, TypeError, KeyError) as e:
            return {'isError': True, 'error': str(e)}


def validar(esquema, args):
    if not isinstance(args, dict):
        raise ValueError('La entrada debe ser un objeto')
    propiedades = esquema['properties']
    for campo in esquema.get('required', []):
        if campo not in args:
            raise ValueError('Falta campo: ' + campo)
    if esquema.get('additionalProperties') is False and set(args) - set(propiedades):
        raise ValueError('Hay campos no permitidos')
    for campo, valor in args.items():
        contrato = propiedades.get(campo)
        if contrato is None:
            continue
        tipo = contrato.get('type')
        valido = (tipo == 'string' and isinstance(valor, str)) or (
            tipo == 'number' and isinstance(valor, (int, float))
            and not isinstance(valor, bool))
        if not valido:
            raise ValueError('Tipo incorrecto: ' + campo)
        if 'enum' in contrato and valor not in contrato['enum']:
            raise ValueError('Valor no permitido: ' + campo)


class ClienteMultiSimulado:
    def __init__(self, proveedores):
        self.proveedores = proveedores
        self.rutas = {}

    def descubrir(self):
        self.rutas = {}
        herramientas = []
        for identificador, servidor in sorted(self.proveedores.items()):
            for tool in servidor.listar():
                nombre_original = tool['name']
                nombre_publico = identificador + '__' + nombre_original
                if nombre_publico in self.rutas:
                    raise ValueError('Colisión de nombres públicos')
                tool['name'] = nombre_publico
                herramientas.append(tool)
                self.rutas[nombre_publico] = (servidor, nombre_original)
        return herramientas

    def despachar(self, nombre, argumentos):
        ruta = self.rutas.get(nombre)
        if ruta is None:
            return {'isError': True, 'error': 'Nombre fuera del catálogo descubierto'}
        servidor, original = ruta
        return servidor.invocar(original, argumentos)


def agente(catalogo, despachar, politica):
    """Una política guionizada sustituye al LLM; el catálogo sí llega en ejecución."""
    propuesta = politica(deepcopy(catalogo))
    nombres = {t['name'] for t in catalogo}
    if propuesta['name'] not in nombres:
        return {'isError': True, 'error': 'Propuesta no ofrecida al agente'}
    return despachar(propuesta['name'], propuesta['arguments'])


def politica_para(nombre, argumentos):
    def politica(catalogo):
        if nombre not in {t['name'] for t in catalogo}:
            raise ValueError('La política solicitó una capacidad ausente')
        return {'name': nombre, 'arguments': argumentos}
    return politica


def main():
    esquema_mes = {'type': 'object', 'properties': {
        'mes': {'type': 'string', 'enum': ['2026-03', '2026-04']}},
        'required': ['mes'], 'additionalProperties': False}
    ventas = ServidorSimulado()
    ventas.publicar('consultar_ventas', 'Total didáctico por mes', esquema_mes,
                    lambda mes: {'mes': mes, 'total': {'2026-03': 2695, '2026-04': 1670}[mes]})
    cliente = ClienteMultiSimulado({'ventas': ventas})
    fuente_antes = hashlib.sha256(inspect.getsource(agente).encode()).hexdigest()
    catalogo1 = cliente.descubrir()
    antes = agente(catalogo1, cliente.despachar,
                   politica_para('ventas__consultar_ventas', {'mes': '2026-03'}))
    assert antes['resultado']['total'] == 2695

    cambio = ServidorSimulado()
    cambio.publicar('convertir_moneda', 'Multiplica por una tasa ficticia fija de 2',
        {'type': 'object', 'properties': {'monto': {'type': 'number'}},
         'required': ['monto'], 'additionalProperties': False}, lambda monto: monto * 2)
    cliente.proveedores['cambio'] = cambio  # Configuración; el agente no se edita.
    catalogo2 = cliente.descubrir()
    despues = agente(catalogo2, cliente.despachar,
                     politica_para('cambio__convertir_moneda', {'monto': 100}))
    assert despues['resultado'] == 200
    fuente_despues = hashlib.sha256(inspect.getsource(agente).encode()).hexdigest()
    assert fuente_antes == fuente_despues
    casos = {}
    for titulo, nombre, entrada in [
        ('mes_fuera_de_dominio', 'ventas__consultar_ventas', {'mes': '2026-05'}),
        ('campo_faltante', 'ventas__consultar_ventas', {}),
        ('campo_extra', 'ventas__consultar_ventas', {'mes': '2026-03', 'borrar': True}),
        ('tipo_incorrecto', 'cambio__convertir_moneda', {'monto': '100'}),
        ('bool_no_es_monto', 'cambio__convertir_moneda', {'monto': True}),
        ('nombre_desconocido', 'otro__buscar', {})]:
        resultado = cliente.despachar(nombre, entrada)
        assert resultado['isError'] is True
        casos[titulo] = resultado

    # Mismo nombre local en distintos servidores; ambas rutas siguen accesibles.
    cambio.publicar('consultar_ventas', 'Respuesta distinta para probar enrutamiento',
                    esquema_mes, lambda mes: {'origen': 'cambio', 'mes': mes})
    catalogo3 = cliente.descubrir()
    assert len({t['name'] for t in catalogo3}) == 3
    assert cliente.despachar('cambio__consultar_ventas', {'mes': '2026-03'})['resultado']['origen'] == 'cambio'
    assert cliente.despachar('ventas__consultar_ventas', {'mes': '2026-03'})['resultado']['total'] == 2695
    report = {'tipo': 'simulador educativo; no prueba conformidad MCP ni selección de LLM',
        'catalogo_antes': [t['name'] for t in catalogo1],
        'catalogo_despues': [t['name'] for t in catalogo2],
        'catalogo_colision_local': [t['name'] for t in catalogo3],
        'ventas': antes, 'conversion_tasa_ficticia': despues,
        'fuente_agente_igual': fuente_antes == fuente_despues,
        'sha256_fuente_agente': fuente_despues,
        'rechazos_verificados': casos, 'rutas_distinguidas': True,
        'cuentas': [{'M': m, 'N': n, 'integraciones': m*n, 'piezas': m+n,
                     'producto_mayor': (m-1)*(n-1)>1}
                    for m,n in [(1,3), (1,10), (2,2), (2,3), (3,4), (5,5)]]}
    for fila in report['cuentas']:
        assert (fila['integraciones'] > fila['piezas']) == fila['producto_mayor']
    Path(__file__).with_name('s13_resultados_verificados.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print('OK: catálogo, nueva capacidad, fuente igual, 6 rechazos y rutas separadas')


if __name__ == '__main__':
    main()
