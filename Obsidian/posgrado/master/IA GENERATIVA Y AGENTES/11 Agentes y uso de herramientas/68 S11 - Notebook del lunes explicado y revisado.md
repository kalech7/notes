---
title: "68 S11 - Notebook del lunes explicado y revisado"
created: 2026-09-29
fecha: 2026-09-29
capitulo: 11
sesion: "11"
tags:
  - maestria/ia-generativa
  - agentes
  - estudio
---

# 68 S11 - Notebook del lunes explicado y revisado

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/11 Agentes y uso de herramientas/59 S11 - Guía para entender agentes y herramientas|Guía de la sesión 11]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

El notebook [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/s3-lun-estudiante.ipynb|s3-lun-estudiante.ipynb]] enseña la maquinaria que permite a un modelo pedir herramientas. Está asociado a la semana 3, lunes, y a la sesión 11. Esta nota completa la teoría con sus **datos reales de ejemplo**, aunque la empresa es ficticia. Los importes no son datos personales ni resultados de un LLM.

La copia ejecutable con todos los ejercicios resueltos y explicaciones junto a sus celdas está ahora en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/Practica lunes/s3-lun-resuelto.ipynb|Talleres y práctica: lunes resuelto]]. Sigue el código paso a paso en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/95 PRÁCTICA - Notebook del lunes resuelto y explicado|la guía de la práctica del lunes]]. Esa copia corrige directamente el filtro del simulador; el adaptador descrito más abajo corresponde al laboratorio complementario anterior.

## 1. Qué piezas construyes y para qué

Un modelo puede escribir «consulta marzo», pero esa frase no consulta nada. El **harness**, o programa que rodea al modelo, interpreta la solicitud, valida sus argumentos, llama una función y añade el resultado al historial. El historial es la lista de mensajes que permite a la próxima decisión saber qué ocurrió.

| Pieza del notebook | Responsabilidad | Lo que no demuestra |
| --- | --- | --- |
| `VENTAS` | Siete filas ficticias en memoria | Conexión a una base real |
| Funciones Python | Consultar filas, agregados o productos | Elegir la siguiente acción |
| `ESQUEMAS` | Describir nombres y parámetros al modelo | Que el programa valide esos parámetros |
| `LLMSimulado` | Elegir con reglas de palabras clave | Comprensión general o autonomía de un LLM |
| `LLMReal` | Adaptar mensajes a un servicio compatible | Que todo servidor acepte idénticas opciones |
| Bucle que debes completar | Decidir, ejecutar, observar y detener | Corrección automática de la respuesta |
| Traza | Registrar decisiones y resultados | Acceso al razonamiento privado del modelo |

La arquitectura del bucle puede mantenerse al cambiar el simulador por un servicio real. **El comportamiento y las fallas posibles cambian**: red, JSON incorrecto, varias llamadas simultáneas, errores de herramientas y límites de salida.

## 2. Los números del ejemplo, paso a paso

En marzo hay importes 1200, 300, 1150 y 45. En abril hay 1300, 320 y 50.

$$\text{Total marzo}=1200+300+1150+45=2695$$
$$\text{Promedio marzo}=2695/4=673{,}75$$
$$\text{Total abril}=1300+320+50=1670$$
$$\text{Promedio abril}=1670/3\approx556{,}67$$

El promedio es **por fila de venta**, no por producto, cliente ni día. `round(..., 2)` redondea la salida a dos decimales; no cambia la definición del promedio.

Para marzo en sierra, `consultar_ventas` devuelve únicamente laptop = 1200 y teclado = 45. Esas dos filas suman 1245, pero la herramienta devuelve el **detalle**: no calcula ese agregado. `listar_productos()` devuelve `['laptop', 'monitor', 'teclado']` ordenados alfabéticamente y sin duplicados.

La información completa del ejemplo permite comprobar los filtros sin adivinar qué fila entró:

| Fecha | Producto | Región | Importe |
| --- | --- | --- | ---: |
| 2026-03-02 | laptop | sierra | 1200 |
| 2026-03-05 | monitor | costa | 300 |
| 2026-03-11 | laptop | costa | 1150 |
| 2026-03-15 | teclado | sierra | 45 |
| 2026-04-01 | laptop | oriente | 1300 |
| 2026-04-03 | monitor | sierra | 320 |
| 2026-04-18 | teclado | costa | 50 |

El dataset no declara una moneda en un campo propio. El simulador imprime `$`, pero eso no establece por sí solo una moneda inequívoca para un sistema general. Una versión empresarial debería devolver el código de moneda. Además, `listar_productos` enumera productos **observados en estas ventas**; no consulta un catálogo de inventario ni demuestra disponibilidad actual.

## 3. Una corrida completa

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/49-s11-notebook-traza.png|49-s11-notebook-traza.png]]

La primera decisión pide `estadisticas_ventas` con `mes="2026-03"`. El programa ejecuta la función y devuelve las tres cifras. La segunda decisión ya puede redactar la respuesta. Por eso hay **una llamada de herramienta y dos decisiones del modelo**. Las flechas muestran transferencia de información; el modelo nunca ejecuta la suma mediante la emisión de la llamada.

El historial debe guardar la solicitud y el resultado asociados a `c1`. Ese identificador permite saber a qué petición responde una observación. Un resultado de error también debe corresponder a su llamada; emparejar mensajes no demuestra que una operación con efectos ocurriera exactamente una vez.

```python
mensajes.append({
    "role": "assistant_tool_use", "id": "c1",
    "name": "estadisticas_ventas", "input": {"mes": "2026-03"}
})
mensajes.append({
    "role": "tool_result", "id": "c1", "name": "estadisticas_ventas",
    "content": '{"n": 4, "total": 2695, "promedio": 673.75}'
})
```

Estos nombres son del **protocolo interno didáctico**, no roles universales que todos los proveedores entiendan. El adaptador traduce ese historial al formato requerido por el servicio.

## 4. Hallazgos comprobados en el original

**Incompatibilidad del historial.** La celda 7 detecta herramientas ya utilizadas mediante `role == "tool_result_meta"`. La consigna de la celda 8 pide guardar la solicitud y su `tool_result`, pero no explica ese tercer metadato. Si completas el bucle con los dos mensajes naturales de la consigna, el simulador no reconoce que ya recibió el dato y vuelve a pedirlo. Lo reprodujimos localmente.

Hay dos soluciones coherentes: adaptar el simulador para reconocer `assistant_tool_use`, o construir explícitamente el metadato esperado. La práctica adjunta usa un **adaptador** que inserta ese metadato en una copia del historial suministrada al simulador; mantiene el par solicitud–resultado en el historial principal. No altera el original docente.

**Ubicación del repositorio.** La celda 1 busca un ancestro que contenga `curso/actividades`. En esta bóveda esa estructura no existe. Abrir el notebook archivado aquí no garantiza que su configuración funcione: debes ejecutarlo dentro del repositorio docente, o adaptar la configuración en una copia. Colocarlo en `Materiales` conserva y organiza la fuente; no crea su entorno de ejecución.

**Ejercicios vacíos y variable `traza`.** La implementación está intencionalmente en blanco. La celda 11 usa `traza`, que no queda definida por las celdas anteriores suministradas. Ejecutar «todo» sin completar los ejercicios puede fallar. Es un cuaderno de estudiante, no una solución terminada.

**El simulador no cubre todas las herramientas de forma general.** Si la pregunta no contiene «marzo», el código elige abril, aunque pidas otro período. Solo reconoce sierra como filtro regional. No sabe manejar cualquier consulta ni tiene un comportamiento fiable ante cualquier resultado de error. Sus reglas son útiles para estudiar el protocolo, no para responder consultas reales.

**Varias llamadas y consumo.** `LLMReal` toma `tool_calls[0]` e ignora las demás. La práctica implementa una llamada por decisión; un servicio que devuelva varias requiere manejar el conjunto o configurar y verificar esa restricción. Imprimir `usage` permite ver consumo, pero no lo convierte en un presupuesto acumulado.

**Descripción no equivale a validación.** `mes` se describe como `YYYY-MM`, pero `startswith(mes)` no impone ese formato: un prefijo como `2026` podría seleccionar ambos meses. La versión didáctica verifica año–mes antes de llamar a la función. Un esquema declarado también necesita un validador o controles efectivos del programa.

**JSON inválido convertido en texto final.** `LLMReal` captura `JSONDecodeError` y devuelve `tipo="texto"` con un diagnóstico. El bucle del ejercicio termina ante cualquier texto, por lo que esa salida significa que se detuvo por error de representación, no que resolvió la pregunta. Conviene distinguir `error_protocolo` de `respuesta_final` en una implementación ampliada. Además, JSON válido puede devolver una lista o `null`; antes de expandir `**input` debe comprobarse que sea un objeto.

**Elección del backend y prueba previa.** `hacer_llm()` prueba primero el servicio configurado con clave; después intenta el servicio universitario y solo al fallar ambos utiliza el simulador. Por eso «sin clave» no significa que el código original evite toda red: aún intenta el servidor universitario. Una comparación necesita registrar qué backend terminó usando y si hubo una sustitución. En nuestra práctica local solo se extrae la clase simulada; no se ejecuta esa selección.

**Adaptar el formato no completa la integración.** Las celdas 4–5 enseñan que nombre, descripción y esquema pueden envolverse de dos maneras. La traducción conserva esa información, pero los mensajes, identificadores, opciones de salida y manejo de fallos aún pertenecen al contrato del adaptador. El puente que menciona MCP se desarrolla en la sesión siguiente; esta demostración no verifica toda la compatibilidad de un proveedor ni elimina la validación del harness.

## 5. Respuestas razonadas a los ejercicios

| Pregunta | Conducta del simulador adaptado | Decisiones / herramientas |
| --- | --- | --- |
| ¿Cuánto vendimos en marzo? | Pide estadísticas y responde 2695 | 2 / 1 |
| ¿Qué productos vendemos? | Pide lista y devuelve tres productos | 2 / 1 |
| Dame el detalle de marzo en sierra | Pide dos filas filtradas | 2 / 1 |
| ¿Cuál es el sentido de la vida? | Explica su alcance y pide reformular | 1 / 0 |

La última salida es razonable para **este asistente de ventas**: evita fingir una capacidad que sus reglas no tienen. Una respuesta final no significa que haya satisfecho cualquier pregunta.

Antes de incorporar una herramienta que escriba datos, hacen falta permisos específicos, validación de la operación y una política de confirmación apropiada al efecto. Además, conviene una clave de idempotencia para que un reintento no duplique una modificación, límites y traza. Esto explica el ejercicio; no ejecuta ninguna escritura.

En la taxonomía empresarial del notebook, llamar «capa 3» o «capa 4» al mismo bucle depende del alcance y la orquestación que se quiera describir. **No existe una línea mágica que cambie la categoría.** La clasificación es de divulgación; en el criterio operativo del curso importan las decisiones y la realimentación. No hay que elevarla a definición universal de agente.

> [!question]- ¿Por qué bajar `max_pasos` no arregla la incompatibilidad del simulador?
> Acorta la repetición, pero el simulador continúa sin reconocer el resultado. Hay que corregir el contrato del historial; el límite solo contiene la falla.

Fuentes: notebook del lunes, 18 celdas, numeradas aquí desde 0. Se leyeron completas; no tiene salidas guardadas. La práctica [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/Practica/s12_laboratorio_local.py|s12_laboratorio_local.py]] extrae solo datos y definiciones seleccionadas y conserva [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/Practica/s12_resultados_verificados.json|s12_resultados_verificados.json]]. No ejecuta configuración ni conexiones del notebook.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/11 Agentes y uso de herramientas/67 S11 - Ejercicios resueltos y repaso activo|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Siguiente]] →
