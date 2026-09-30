---
title: "63 S11 - Diseñar herramientas esquemas y validación"
created: 2026-09-28
capitulo: 11
sesion: "11"
fecha: 2026-09-28
tags:
  - maestria/ia-generativa
  - agentes
  - herramientas
fuente: "[[sesion-11.pdf]]"
---

# 63 S11 - Diseñar herramientas esquemas y validación

[[59 S11 - Guía para entender agentes y herramientas|Guía de la sesión 11]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[62 S11 - Function calling y bucle del agente paso a paso]]

Siguiente: [[64 S11 - Memoria contexto y costo de repetir el historial]]

## 1. Una herramienta tiene dos caras

Para el modelo, una herramienta es una posibilidad descrita: qué hace, cuándo conviene y qué argumentos acepta. Para el programa, es una implementación ejecutable. Tener una función en Python no significa que el modelo sepa que existe. Tener una descripción tampoco significa que exista una función conectada.

![[44-s11-contrato-herramienta.png]]

La columna izquierda mejora la selección; la derecha hace cumplir el contrato. El dato `2026-99` puede parecer una cadena de mes, pero el ejecutor debe rechazarlo porque 99 no es un mes válido.

## 2. Diseñar desde la intención del usuario

Compara dos herramientas:

| Descripción | Qué problema causa o resuelve |
| --- | --- |
| «Consulta datos». Parámetro `q: string`. | No especifica qué datos, qué devuelve ni cómo preguntar. |
| «Devuelve filas individuales de ventas de un mes. Úsala para inspeccionar transacciones; no calcula totales». | Permite distinguir detalle de agregado. |
| «Devuelve el total mensual de ventas netas sin impuestos en USD. Úsala para cifras agregadas; no devuelve transacciones». | Alinea la herramienta con preguntas sobre totales. |

Si el usuario pide «total de marzo», devolver miles de transacciones hace que el modelo tenga que sumar y use más contexto. Una herramienta agregada reduce ambas cargas. Si el usuario pide revisar una transacción concreta, un total no contiene suficiente detalle.

La separación debe reflejar necesidades reales, no multiplicar funciones innecesarias. Dos nombres muy parecidos con descripciones idénticas dificultan la selección.

## 3. Contrato conceptual completo

El siguiente JSON es una ficha didáctica. `input_schema` conserva la convención del PDF, pero no se presenta como formato universal de API:

```json
{
  "name": "total_ventas",
  "description": "Devuelve total, moneda y fuente de las ventas netas sin impuestos de un mes. Usar para agregados mensuales; no devuelve el detalle de transacciones.",
  "input_schema": {
    "type": "object",
    "properties": {
      "mes": {
        "type": "string",
        "pattern": "^[0-9]{4}-(0[1-9]|1[0-2])$",
        "description": "Mes calendario YYYY-MM; por ejemplo 2026-03."
      }
    },
    "required": ["mes"],
    "additionalProperties": false
  }
}
```

En JSON Schema, `properties` define las propiedades conocidas; `required` exige su presencia; `additionalProperties: false` impide campos extra. El patrón exige un año de cuatro cifras y un mes entre 01 y 12. No comprueba por sí solo que existan datos para ese período. [Referencia oficial de objetos de JSON Schema](https://json-schema.org/understanding-json-schema/reference/object).

**Lee el patrón por partes:** `^` comienza la cadena; `[0-9]{4}` acepta cuatro dígitos; `-` exige el separador; `0[1-9]` permite 01–09; `1[0-2]` permite 10–12; `$` termina la cadena. Por eso `2026-3`, `2026-99` y `marzo` quedan fuera.

Para dominios pequeños puede convenir `enum`, por ejemplo `"moneda": {"type":"string", "enum":["USD","EUR"]}`. Eso limita los valores aceptados; no realiza una conversión de moneda ni garantiza una tasa correcta.

## 4. Cuatro niveles que no conviene confundir

1. **Sintaxis:** ¿la respuesta se puede leer como JSON?
2. **Estructura:** ¿contiene nombre y parámetros con los tipos requeridos?
3. **Dominio:** ¿el mes, moneda o identificador tiene sentido y está disponible?
4. **Autorización:** ¿esta operación está permitida para este usuario y recurso?

`{"mes":"2026-99"}` es JSON válido y el valor es de tipo cadena. Aun así viola el dominio. `{"mes":"2026-03"}` puede pasar ese control y fallar porque el usuario no tiene acceso al conjunto de datos. Validar tipos no sustituye el resto.

Las descripciones son instrucciones que ayudan al modelo. No reemplazan restricciones del programa ni permisos reales. Una herramienta debe usar credenciales con las capacidades adecuadas y validar antes de ejecutar. En nuestro laboratorio todas las herramientas trabajan sobre datos ficticios en memoria.

## 5. El resultado también necesita un diseño

Un resultado útil explica qué obtuvo y de dónde:

```json
{
  "ok": true,
  "mes": "2026-03",
  "total": 15000,
  "moneda": "USD",
  "definicion": "ventas netas sin impuestos",
  "fuente": "ventas_demo_v1"
}
```

Si la herramienta busca documentos, conviene incluir identificador, fragmento y referencia. Si limita filas, debe indicar que hay truncamiento. Si no encuentra datos, debe distinguir ausencia de una falla.

No conviene devolver «15» sin unidad, «consulta exitosa» sin datos o un error mezclado con un campo de éxito. El modelo decide a partir de esos resultados: cuanto más ambiguos sean, más difícil será inferir la acción adecuada.

Para un RAG convertido en herramienta, devuelve evidencia y no solo una frase fluida. Así se puede inspeccionar qué documentos respaldan la respuesta, como estudiaste en [[46 S09 - Evaluar respuestas fidelidad y citas]].

## 6. Registro local y catálogo del modelo

```python
# Relaciona un nombre permitido con código real.
REGISTRO = {
    "total_ventas": total_ventas,
    "variacion_porcentual": variacion_porcentual,
}
```

El registro permite ejecutar. El catálogo con descripciones y esquemas permite elegir. Deben ser coherentes: si el catálogo anuncia `ventas_totales` pero el registro solo contiene `total_ventas`, la llamada fallará aunque la intención sea correcta.

El PDF p. 17 señala un problema de descubrimiento de herramientas en el Lab 03. Lo tratamos como una observación de la presentación; estas notas no afirman haber inspeccionado o corregido ese archivo.

## 7. Cómo investigar una selección equivocada

Supón que pide filas cuando necesitaba un total. Revisa primero si el modelo recibió el catálogo y si las descripciones distinguen ambos casos. Después inspecciona si el contexto de la conversación vuelve ambigua la petición, si el esquema está bien formado y si el nombre propuesto coincide con el registro.

Solo entonces tiene sentido atribuir el error a la capacidad del modelo. Cambiar de modelo puede ayudar, pero no arregla un catálogo que nunca se envía.

> [!tip] Recordatorio
> Una buena herramienta reduce la ambigüedad antes de ejecutar y devuelve evidencia comprensible después de ejecutar.

**Fuente:** [[sesion-11.pdf#page=16|pp. 16–17]]. Esquema ampliado y validaciones: elaboración pedagógica; referencia oficial de JSON Schema consultada el 28 de septiembre de 2026, hora local. No se usa una firma específica de proveedor.
