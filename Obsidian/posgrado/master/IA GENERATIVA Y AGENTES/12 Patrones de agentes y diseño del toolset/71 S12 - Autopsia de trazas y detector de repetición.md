---
title: "71 S12 - Autopsia de trazas y detector de repetición"
created: 2026-09-29
fecha: 2026-09-29
capitulo: 12
sesion: "12"
tags:
  - maestria/ia-generativa
  - agentes
  - estudio
---

# 71 S12 - Autopsia de trazas y detector de repetición

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Una **traza** es una secuencia registrada de decisiones, llamadas, resultados y terminación. Sirve para ubicar el primer paso donde el sistema deja de avanzar o afirma algo sin evidencia. Leer solo la respuesta final oculta esa diferencia.

## 1. Las tres trazas del martes

El notebook [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/s3-mar-estudiante.ipynb|s3-mar-estudiante.ipynb]], celda 3, trae listas prefabricadas. No son salidas obtenidas al ejecutar un LLM.

| Traza | Primer punto problemático | Intervención que sí corresponde |
| --- | --- | --- |
| `TRAZA_SANA` | No hay falla evidente en la secuencia | Verificar fuentes y el alcance temporal de la respuesta |
| `TRAZA_LOOP` | Segunda búsqueda equivalente a la primera, después de «sin resultados» | Revisar falta de progreso y cortar antes de otra ejecución inútil |
| `TRAZA_FABRICA` | Segundo Thought introduce ingresos de 45 millones | Verificar respaldo de afirmaciones; abstenerse sin datos |

La traza sana obtiene dos años y responde con un intervalo de edad, 30–31. El intervalo evita fingir precisión cuando no se cuenta con una fecha exacta del evento. Aquí estudiamos la lógica de esa traza: no se realizó una nueva búsqueda histórica sobre su contenido.

En la traza de bucle hay cuatro llamadas a `buscar` y ninguna respuesta final. La segunda cambia el orden de las palabras, pero no aporta una estrategia nueva frente al primer resultado vacío. En una política estricta de este ejercicio se puede detectar desde esa segunda acción, antes de ejecutarla.

La fabricación ocurre **antes de la respuesta final**: la observación solo dice que NimbusSoft es una empresa de software fundada en 2019. No contiene ingresos ni moneda. El Thought afirma 45 millones y luego la respuesta lo presenta como hecho. La empresa se usa como ejemplo ficticio. Un detector de repetición no detecta este error porque solo hubo una búsqueda.

## 2. Detectar equivalencia mediante palabras

La consigna propone bajar a minúsculas y ordenar palabras. Una implementación propia añade tokenización para separar palabras de signos de puntuación:

```python
import re

def normalizar(texto):
    return tuple(sorted(re.findall(r"\w+", texto.casefold())))

def detectar_loop(traza, ventana=6):
    if type(ventana) is not int or ventana <= 0:
        raise ValueError("ventana debe ser un entero positivo")
    vistos = set()
    for e in traza[-ventana:]:
        if e["tipo"] == "action":
            clave = (e["tool"], normalizar(e["input"]))
            if clave in vistos:
                return True
            vistos.add(clave)
    return False
```

`casefold()` normaliza mayúsculas de forma adecuada para comparación de texto. La tupla guarda las palabras ordenadas; un conjunto `vistos` permite identificar una clave ya encontrada. La clave incorpora la herramienta para distinguir dos operaciones diferentes con igual texto.

Se conservan palabras repetidas: no usamos un conjunto de palabras porque borraría sus cantidades. La función exige el formato de eventos del ejercicio, cuya entrada es texto; no es un validador universal de trazas.

## 3. Qué significa «ventana de seis»

Esta versión usa los **últimos seis eventos** de la traza. Incluye thoughts y observations, aunque solo compara actions. Otra implementación podría tomar las últimas seis acciones. Ambas unidades son posibles, pero no equivalen: en el formato de tres eventos por ciclo, seis eventos suelen contener solo dos acciones.

Con los datos suministrados, devuelve `False` para sana, `True` para bucle y `False` para fabricación. Este resultado no significa «dos trazas correctas»: significa «una traza con acciones repetidas según esta heurística».

## 4. Dos tipos de errores del detector

Un **falso negativo** ocurre cuando hay estancamiento, pero no se marca. «Cotización de NimbusSoft» no tiene las mismas palabras que «precio acción NimbusSoft», aunque busque esencialmente lo mismo.

Un **falso positivo** ocurre cuando se marca una repetición que no demuestra un bucle inútil. «Ana paga a Luis» y «Luis paga a Ana» producen la misma tupla ordenada, aunque sus significados sean opuestos. Además, repetir una consulta puede ser legítimo si cambió el estado, se espera una tarea asíncrona o se recupera un fallo temporal.

La equivalencia de entrada no equivale por sí sola a ausencia de progreso. En una aplicación se puede considerar herramienta, argumentos estructurados, resultado, versión del estado y motivo del reintento. Un máximo de reintentos sigue haciendo falta.

Para entradas JSON, conviene serializar con claves ordenadas o comparar los campos relevantes. Ordenar las palabras de una consulta SQL o de una ruta destruiría parte de su significado.

## 5. Detectar antes de actuar

Analizar una traza completa sirve para autopsia. Para protección **durante** la ejecución, se evalúa la acción propuesta contra las anteriores antes de llamar a la herramienta. Si se agrega después de actuar, el detector todavía puede detener la próxima vuelta, pero ya gastó esa llamada o produjo su efecto.

La salida de parada debe explicar el motivo y conservar evidencia: «dos búsquedas equivalentes sin resultados», con los eventos asociados. No debe presentar «sin resultados» como prueba de que la entidad no existe en el mundo.

> [!question]- ¿Agregar embeddings elimina todos los errores de equivalencia?
> No. La similitud semántica también requiere umbrales y puede confundir operaciones distintas. Puede complementar la señal, junto con estado, resultados y límites; no demuestra progreso por sí sola.

Fuentes: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-12.pdf#page=9|PDF 9–10]] y notebook del martes, celdas 3–9. La implementación y los contraejemplos son propios; sus resultados están en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/Practica/s12_resultados_verificados.json|s12_resultados_verificados.json]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/70 S12 - ReAct pensamiento acción observación y evidencia|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/72 S12 - Pasos presupuestos timeouts y condiciones de parada|Siguiente]] →

