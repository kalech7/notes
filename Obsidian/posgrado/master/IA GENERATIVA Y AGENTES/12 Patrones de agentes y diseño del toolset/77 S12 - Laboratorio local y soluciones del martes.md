---
title: "77 S12 - Laboratorio local y soluciones del martes"
created: 2026-09-29
fecha: 2026-09-29
capitulo: 12
sesion: "12"
tags:
  - maestria/ia-generativa
  - agentes
  - estudio
---

# 77 S12 - Laboratorio local y soluciones del martes

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

La práctica [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/Practica/s12_laboratorio_local.py|s12_laboratorio_local.py]] conecta los dos notebooks con las explicaciones. Usa biblioteca estándar de Python, datos ficticios y un modelo por reglas. Sus resultados se conservan en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/Practica/s12_resultados_verificados.json|s12_resultados_verificados.json]]. **Comprueba mecánica y contratos; no mide desempeño de un LLM.**

## 1. Cómo ejecutar y qué lee

Desde la carpeta `Practica`:

```bash
python3 s12_laboratorio_local.py
```

El programa localiza los originales en `Materiales`, analiza algunas celdas con `ast`, extrae únicamente asignaciones y definiciones seleccionadas y ejecuta esas piezas. No ejecuta la celda de configuración del lunes ni su fábrica de conexiones. No lee `.env` ni llama a los servicios nombrados en el original.

El archivo JSON de resultados se regenera junto al script. Es importante mantener intactos los originales: las mejoras están en el archivo complementario y se pueden contrastar con las fuentes.

## 2. Solución del detector

`detectar_loop` toma los últimos seis eventos y compara herramienta más palabras normalizadas. Los resultados comprobados son:

| Entrada | Resultado | Lo que demuestra |
| --- | --- | --- |
| `TRAZA_SANA` | `False` | No hay acciones repetidas bajo esta regla |
| `TRAZA_LOOP` | `True` | Se reconoce el cambio de orden de palabras |
| `TRAZA_FABRICA` | `False` | La fabricación requiere otro control |

La función está desarrollada en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/71 S12 - Autopsia de trazas y detector de repetición|71 S12 - Autopsia de trazas y detector de repetición]]. El script comprueba también el contraejemplo «Ana paga a Luis» frente a «Luis paga a Ana»: la normalización pierde la dirección de la relación.

## 3. Solución del presupuesto

`presupuesto_local` simula un agente que quiere dar 12 pasos. Con máximo de cinco y presupuesto de siete unidades, coste fijo dos por paso, corta por presupuesto después del tercer paso: gasto seis. Con presupuesto 100, corta por máximo después de cinco pasos: gasto diez.

Se comprueba el costo de la próxima acción **antes** de acumularlo. No se presenta ese contador como consumo real de tokens; su propósito es entender la reserva. La función y el bucle de herramientas son ejemplos separados: no se afirma que este script implemente contabilidad de una API.

## 4. Mini-Reflexion con crítica efectivamente recibida

El generador de la simulación utiliza el contenido de la última crítica para elegir la salida. Esto permite comprobar la transferencia de información:

| Intento | Salida | Verificación | Contexto nuevo |
| --- | --- | --- | --- |
| 1 | Texto seguido del objeto JSON | Falla parseo | Entrega solo JSON válido |
| 2 | Objeto con `"técnico"` | Categoría fuera del dominio | Usa `tecnico`, sin tilde |
| 3 | Objeto con `"tecnico"` y urgencia 4 | Pasa contrato | Termina |

El controlador es:

```python
criticas = []
for intento in range(1, max_intentos + 1):
    respuesta = generar(list(criticas))
    ok, critica = verificador(respuesta)
    # La traza guarda candidato, feedback recibido y evaluación.
    if ok:
        return respuesta
    criticas.append(critica)
# Finalizar con intentos_agotados.
```

El script completo registra todos esos campos y un estado explícito; este fragmento omite la traza para mostrar la lógica. Si `max_intentos=2`, termina sin solución aceptada. No afirma éxito simplemente por haber realizado dos correcciones.

El generador es una regla escrita por nosotros, no un LLM que descubrió cómo corregirse. A diferencia de iterar sin leer críticas por una lista fija, permite inspeccionar que el texto de feedback participa en la decisión. Sigue siendo una demostración limitada del patrón.

## 5. El lunes integrado

La ejecución extrae las funciones y las siete ventas del original. Con el simulador sin adaptar, se reproduce una nueva solicitud de la misma herramienta porque no reconoce los mensajes guardados. La política conservadora del harness corta por repetición en la segunda decisión, después de una única ejecución.

El adaptador agrega el metadato esperado solo a la copia que lee el simulador. Entonces las cuatro preguntas de [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/11 Agentes y uso de herramientas/68 S11 - Notebook del lunes explicado y revisado|68 S11 - Notebook del lunes explicado y revisado]] finalizan con las cantidades correctas y los pares solicitud–resultado correspondientes. La pregunta fuera del dominio finaliza sin herramientas.

No se añadieron respuestas a las celdas del cuaderno docente ni se crearon resultados de una conexión real. La síntesis resuelta sirve para estudiar y comparar.

## 6. Qué se verificó y qué falta en un sistema real

Se reprodujeron los fallos de `[]`, `null`, categoría lista y booleano; se comprobó el rechazo de esos casos en la variante didáctica y la aceptación del objeto esperado. Se comprobaron totales, promedios, emparejamiento de identificadores, repetición, máximo de pasos, presupuesto y reintentos.

El simulador todavía elige abril cuando no reconoce marzo y no interpreta regiones de manera general, igual que la pieza docente reutilizada. Tampoco es un agente listo para producción: faltan, según el uso, persistencia durable, red, contabilidad real, cancelación, concurrencia, políticas específicas e idempotencia de efectos. Estas limitaciones definen qué evidencia aporta la ejecución.

La práctica no inventa un rango para urgencia y no certifica que una categoría corresponda a un ticket real. Sus resultados de «verificado» se refieren al contrato explícito de formato y dominio.

Las salidas simuladas son útiles para pruebas reproducibles, pero no cubren todas las propuestas que un LLM podría devolver. El harness de este laboratorio presupone que `responder` entrega el formato interno descrito y asigna sus propios IDs; no es un adaptador completo para las respuestas crudas de una API. Para reutilizarlo con otro generador, faltaría validar mensajes mal formados, preservar sus identificadores cuando el protocolo lo exija y clasificar excepciones del generador como fallos explícitos. El laboratorio 66 sí incluye casos de mensajes e IDs rechazados, con un contrato didáctico diferente.

## 7. Respuestas de reflexión final

Para un asistente con herramientas cuyo próximo paso depende de resultados, un bucle simple con observaciones es una base razonable de estudio. Hay que justificarlo con la tarea y evaluarlo; usar un nombre de patrón no sustituye la comparación experimental.

Una señal verificable para reflexión puede ser un error de esquema, un cálculo contra una referencia o una prueba funcional. «La respuesta suena mejor» no basta. En un análisis de ventas, el verificador puede comprobar base temporal, dos cantidades comparables y operación correcta antes de aceptar.

Fuentes: ambos notebooks completos; implementación complementaria propia. La revisión no sustituye la rúbrica ni representa una entrega del Taller 3.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/76 S12 - Toolsets validación errores y límites efectivos|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/78 S12 - Ejercicios resueltos y repaso activo|Siguiente]] →

