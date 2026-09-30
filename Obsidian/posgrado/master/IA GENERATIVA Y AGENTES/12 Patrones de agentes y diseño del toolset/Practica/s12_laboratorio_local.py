"""Ejemplos didácticos verificados; biblioteca estándar, sin API ni credenciales.

Lee solo asignaciones y definiciones seleccionadas mediante AST de los originales.
No ejecuta sus celdas de configuración, red, lectura de .env o hacer_llm().
Ejecutar: python3 s12_laboratorio_local.py
"""
import ast
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def extraer(nombre, celda, nombres, entorno):
    nb = json.loads((ROOT / 'Materiales' / nombre).read_text())
    arbol = ast.parse(''.join(nb['cells'][celda]['source']))
    elegidos = []
    for nodo in arbol.body:
        nombre_nodo = getattr(nodo, 'name', None)
        if isinstance(nodo, ast.Assign) and isinstance(nodo.targets[0], ast.Name):
            nombre_nodo = nodo.targets[0].id
        if nombre_nodo in nombres:
            elegidos.append(nodo)
    assert len(elegidos) == len(nombres), (nombre, nombres)
    exec(compile(ast.Module(body=elegidos, type_ignores=[]), nombre, 'exec'), entorno)


def normalizar(texto):
    """Heurística del ejercicio: conserva palabras repetidas; pierde el orden."""
    return tuple(sorted(re.findall(r'\w+', texto.casefold())))


def detectar_loop(traza, ventana=6):
    """Ventana de EVENTOS, no de acciones. Repetir no prueba falta de progreso."""
    if type(ventana) is not int or ventana <= 0:
        raise ValueError('ventana debe ser un entero positivo')
    vistos = set()
    for evento in traza[-ventana:]:
        if evento['tipo'] == 'action':
            clave = (evento['tool'], normalizar(evento['input']))
            if clave in vistos:
                return True
            vistos.add(clave)
    return False


def verificador(respuesta):
    """Contrato docente: objeto, dos claves, categoría permitida, entero real.

    No impone un rango a urgencia: el original no lo especifica.
    """
    try:
        datos = json.loads(respuesta)
    except (json.JSONDecodeError, TypeError):
        return False, 'Entrega solo JSON válido, sin texto adicional'
    if not isinstance(datos, dict):
        return False, 'La raíz debe ser un objeto JSON'
    if set(datos) != {'categoria', 'urgencia'}:
        return False, 'Usa exactamente las claves categoria y urgencia'
    if not isinstance(datos['categoria'], str) or datos['categoria'] not in {'tecnico', 'ventas'}:
        return False, 'categoria debe ser tecnico o ventas, sin tilde'
    if type(datos['urgencia']) is not int:
        return False, 'urgencia debe ser un entero, no un booleano ni decimal'
    return True, 'OK'


def mini_reflexion(generar, max_intentos=3):
    if type(max_intentos) is not int or max_intentos <= 0:
        raise ValueError('max_intentos debe ser un entero positivo')
    criticas, traza = [], []
    for intento in range(1, max_intentos + 1):
        respuesta = generar(list(criticas))
        ok, critica = verificador(respuesta)
        traza.append({'intento': intento, 'respuesta': respuesta,
                      'criticas_recibidas': list(criticas), 'ok': ok, 'critica': critica})
        if ok:
            return {'estado': 'verificado', 'respuesta': respuesta, 'traza': traza}
        criticas.append(critica)
    return {'estado': 'intentos_agotados', 'respuesta': None, 'traza': traza}


def validar_entrada(nombre, entrada):
    if not isinstance(entrada, dict):
        return 'input debe ser un objeto'
    campos = {'estadisticas_ventas': {'mes'}, 'consultar_ventas': {'mes', 'region'},
              'listar_productos': set()}
    if nombre not in campos:
        return 'herramienta no registrada'
    if set(entrada) - campos[nombre]:
        return 'hay argumentos inesperados'
    if nombre != 'listar_productos':
        mes = entrada.get('mes')
        if not isinstance(mes, str) or re.fullmatch(r'\d{4}-(0[1-9]|1[0-2])', mes) is None:
            return 'mes debe usar YYYY-MM con mes entre 01 y 12'
    region = entrada.get('region')
    if region is not None and (not isinstance(region, str) or region not in {'sierra', 'costa', 'oriente'}):
        return 'region debe ser sierra, costa u oriente'
    return None


def ejecutar_agente(modelo, tools, pregunta, max_pasos=5):
    """Un paso = una decisión del modelo. Detecta duplicados antes de ejecutar.

    Política conservadora didáctica: misma herramienta y argumentos se detiene.
    En sistemas reales debe considerar cambio de estado y reintentos legítimos.
    """
    if type(max_pasos) is not int or max_pasos <= 0:
        raise ValueError('max_pasos debe ser un entero positivo')
    mensajes = [{'role': 'user', 'content': pregunta}]
    traza, vistos = [], set()
    for paso in range(1, max_pasos + 1):
        respuesta = modelo.responder(mensajes)
        if respuesta.get('tipo') == 'texto':
            traza.append({'paso': paso, 'tipo': 'final', 'texto': respuesta['texto']})
            return {'estado': 'respuesta_final', 'traza': traza, 'mensajes': mensajes}
        nombre, entrada = respuesta['name'], respuesta['input']
        clave = (nombre, json.dumps(entrada, sort_keys=True, ensure_ascii=False))
        if clave in vistos:
            traza.append({'paso': paso, 'tipo': 'parada', 'motivo': 'repeticion'})
            return {'estado': 'repeticion', 'traza': traza, 'mensajes': mensajes}
        vistos.add(clave)
        llamada_id = f'c{paso}'
        error = validar_entrada(nombre, entrada)
        if error:
            resultado = json.dumps({'error': error}, ensure_ascii=False)
        else:
            try:
                resultado = tools[nombre](**entrada)
                error = 'error' in json.loads(resultado) if resultado.startswith('{') else False
            except Exception as exc:
                resultado = json.dumps({'error': type(exc).__name__})
                error = True
        mensajes.append({'role': 'assistant_tool_use', 'id': llamada_id,
                         'name': nombre, 'input': entrada})
        mensajes.append({'role': 'tool_result', 'id': llamada_id,
                         'name': nombre, 'content': resultado})
        traza.append({'paso': paso, 'tipo': 'tool', 'id': llamada_id,
                      'name': nombre, 'input': entrada, 'resultado': resultado, 'error': bool(error)})
    traza.append({'tipo': 'parada', 'motivo': 'max_pasos'})
    return {'estado': 'max_pasos', 'traza': traza, 'mensajes': mensajes}


class ModeloCorregido:
    """Adaptación didáctica: agrega al simulador original el metadato que espera.

    El harness guarda assistant_tool_use y tool_result. Este adaptador agrega
    tool_result_meta SOLO en una copia para el simulador, no en el protocolo.
    """
    def __init__(self, original):
        self.original = original

    def responder(self, mensajes):
        copia = []
        for m in mensajes:
            if m['role'] == 'tool_result':
                copia.append({'role': 'tool_result_meta', 'name': m['name']})
            copia.append(m)
        return self.original.responder(copia)


def presupuesto_local(deseados=12, max_pasos=5, presupuesto=7, coste_paso=2):
    """Unidades ficticias, no tokens reales. Se reserva antes de actuar."""
    gastado, traza = 0, []
    for paso in range(1, deseados + 1):
        if paso > max_pasos:
            return {'estado': 'max_pasos', 'gastado': gastado, 'traza': traza}
        if gastado + coste_paso > presupuesto:
            return {'estado': 'presupuesto', 'gastado': gastado, 'traza': traza}
        gastado += coste_paso
        traza.append({'paso': paso, 'gasto_acumulado': gastado})
    return {'estado': 'completado', 'gastado': gastado, 'traza': traza}


def main():
    env = {'json': json}
    extraer('s3-lun-estudiante.ipynb', 1, {'VENTAS'}, env)
    extraer('s3-lun-estudiante.ipynb', 3,
            {'consultar_ventas', 'estadisticas_ventas', 'listar_productos', 'ESQUEMAS', 'TOOLS'}, env)
    extraer('s3-lun-estudiante.ipynb', 7, {'LLMSimulado'}, env)
    extraer('s3-mar-estudiante.ipynb', 3, {'TRAZA_SANA', 'TRAZA_LOOP', 'TRAZA_FABRICA'}, env)
    original = {'json': json}
    extraer('s3-mar-estudiante.ipynb', 12, {'verificador', 'INTENTOS_SIMULADOS'}, original)
    fallos_original = {}
    for respuesta in ['[]', 'null', '{"categoria": [], "urgencia": 4}',
                      '{"categoria": "tecnico", "urgencia": true}']:
        try:
            fallos_original[respuesta] = original['verificador'](respuesta)
        except Exception as exc:
            fallos_original[respuesta] = type(exc).__name__
    assert fallos_original['[]'] == 'AttributeError'
    assert fallos_original['null'] == 'AttributeError'
    assert fallos_original['{"categoria": [], "urgencia": 4}'] == 'TypeError'
    assert fallos_original['{"categoria": "tecnico", "urgencia": true}'][0]
    casos = {r: verificador(r) for r in [*fallos_original,
             '{"categoria": "tecnico", "urgencia": 4}',
             '{"categoria": "ventas", "urgencia": 4.0}',
             '{"categoria": "técnico", "urgencia": 4}', 'no es JSON']}
    assert all(not ok for r, (ok, _) in casos.items() if r != '{"categoria": "tecnico", "urgencia": 4}')
    sin_adaptar = ejecutar_agente(env['LLMSimulado'](), env['TOOLS'], '¿Cuánto vendimos en marzo?')
    assert sin_adaptar['estado'] == 'repeticion'
    modelo = ModeloCorregido(env['LLMSimulado']())
    corridas = {p: ejecutar_agente(modelo, env['TOOLS'], p) for p in [
        '¿Cuánto vendimos en marzo?', '¿Qué productos vendemos?',
        'Dame el detalle de ventas de marzo en sierra', '¿Cuál es el sentido de la vida?']}
    assert all(c['estado'] == 'respuesta_final' for c in corridas.values())
    assert len(corridas['¿Cuánto vendimos en marzo?']['traza']) == 2
    assert json.loads(env['estadisticas_ventas']('2026-03')) == {'n': 4, 'total': 2695, 'promedio': 673.75}
    assert json.loads(env['estadisticas_ventas']('2026-04')) == {'n': 3, 'total': 1670, 'promedio': 556.67}
    for corrida in corridas.values():
        llamadas = [m['id'] for m in corrida['mensajes'] if m['role'] == 'assistant_tool_use']
        resultados = [m['id'] for m in corrida['mensajes'] if m['role'] == 'tool_result']
        assert llamadas == resultados
    loops = {k: detectar_loop(env[k]) for k in ['TRAZA_SANA', 'TRAZA_LOOP', 'TRAZA_FABRICA']}
    assert loops == {'TRAZA_SANA': False, 'TRAZA_LOOP': True, 'TRAZA_FABRICA': False}
    assert normalizar('Ana paga a Luis') == normalizar('Luis paga a Ana')
    def generar(criticas):
        if not criticas:
            return original['INTENTOS_SIMULADOS'][0]
        if 'solo JSON' in criticas[-1]:
            return original['INTENTOS_SIMULADOS'][1]
        if 'sin tilde' in criticas[-1]:
            return original['INTENTOS_SIMULADOS'][2]
        return original['INTENTOS_SIMULADOS'][0]
    reflexion = mini_reflexion(generar)
    assert reflexion['estado'] == 'verificado' and len(reflexion['traza']) == 3
    agotados = mini_reflexion(generar, 2)
    assert agotados['estado'] == 'intentos_agotados'
    por_coste = presupuesto_local()
    por_pasos = presupuesto_local(presupuesto=100)
    assert por_coste['gastado'] == 6 and por_coste['estado'] == 'presupuesto'
    assert len(por_pasos['traza']) == 5 and por_pasos['estado'] == 'max_pasos'
    resumen = {'tipo': 'simulacion local determinista; no mide LLM',
               'fallos_verificador_original': fallos_original, 'verificador_corregido': casos,
               'loop_sin_adaptar': sin_adaptar, 'corridas_adaptadas': corridas,
               'detector': loops, 'reflexion': reflexion, 'reflexion_agotada': agotados,
               'presupuesto_coste': por_coste, 'presupuesto_pasos': por_pasos,
               'crecimiento_porcentual': round((1670-2695)/2695*100, 4)}
    destino = Path(__file__).with_name('s12_resultados_verificados.json')
    destino.write_text(json.dumps(resumen, ensure_ascii=False, indent=2) + '\n')
    print('Verificación local correcta. Resultados:', destino)


if __name__ == '__main__':
    main()
