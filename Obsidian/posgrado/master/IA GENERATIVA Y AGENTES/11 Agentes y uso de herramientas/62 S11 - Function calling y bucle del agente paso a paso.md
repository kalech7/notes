---
title: "62 S11 - Function calling y bucle del agente paso a paso"
sesion: "11"
fecha: 2026-09-28
tags:
  - maestria/ia-generativa
  - agentes
  - herramientas
fuente: "[[sesion-11.pdf]]"
---

# 62 S11 - Function calling y bucle del agente paso a paso

[[59 S11 - Guía para entender agentes y herramientas|Guía de la sesión 11]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[61 S11 - PEAS racionalidad y observación parcial]]

Siguiente: [[63 S11 - Diseñar herramientas esquemas y validación]]

## 1. Una llamada es una propuesta de operación

Si el modelo emite `total_ventas(mes="2026-03")`, todavía no existe una consulta ejecutada. Ha producido una representación de una acción. El programa debe reconocerla, validar los argumentos, encontrar la función y ejecutarla.

La expresión *function calling* se refiere a esta interacción estructurada. En una API puede aparecer como un bloque tipado, no como texto libre visible en la conversación. La idea de la diapositiva «solo texto» distingue generación de representación frente a ejecución: los tokens o la estructura devuelta no poseen por sí mismos acceso a una base de datos.

![[43-s11-llamada-y-resultado.png]]

**Cómo leerlo:** sigue las flechas de arriba hacia abajo. La propuesta sale del modelo, pasa por el harness y llega a la herramienta. El dato hace el camino inverso. Solo después el modelo dispone del resultado para decidir otra vez.

## 2. Los seis pasos de la sesión

1. **Declarar herramientas.** El modelo recibe nombres, descripciones y contratos de argumentos. El programa mantiene aparte un registro que relaciona nombres con funciones reales.
2. **Recibir la pregunta.** Se incorpora el objetivo y la información disponible.
3. **Obtener una decisión.** El modelo devuelve una llamada o una respuesta final.
4. **Validar y ejecutar.** El harness comprueba que la acción está permitida y ejecuta la función correspondiente.
5. **Añadir el resultado.** La observación, o el error, entra en el historial asociada a la llamada.
6. **Volver a decidir.** El modelo puede pedir otra herramienta, usar el dato o terminar.

**Harness** es el programa que organiza ese recorrido. No es un modelo adicional obligatorio ni una librería concreta. Incluso unas pocas funciones de Python pueden desempeñar ese papel.

## 3. El ejemplo completo con números

Petición: «¿Cuánto crecieron las ventas de marzo respecto a febrero de 2026?»

| Decisión | Propuesta | Observación que incorpora el sistema |
| --- | --- | --- |
| 1 | `total_ventas("2026-02")` | 12 000 USD; ventas netas sin impuestos. |
| 2 | `total_ventas("2026-03")` | 15 000 USD; misma definición. |
| 3 | `variacion_porcentual(12000,15000)` | 25 %. |
| 4 | Respuesta final | El sistema presenta el resultado con las dos cifras. |

La fórmula es:

$$g=\frac{V_{\text{actual}}-V_{\text{base}}}{V_{\text{base}}}\times100.$$

Primero restamos $15\,000-12\,000=3\,000$. Después dividimos por la base, $3\,000/12\,000=0.25$. Finalmente expresamos la proporción en porcentaje: $0.25\times100=25\%$.

La respuesta distingue **aumento absoluto**, 3 000 USD, de **aumento relativo**, 25 %. Si se divide por 15 000 se obtiene 20 %, que responde otra relación y no el crecimiento respecto de febrero. Si la base es cero, debe explicar que esta tasa no está definida; no sustituirla por cero.

## 4. Los mensajes y su identidad

Usaremos un formato didáctico, no una firma de proveedor:

```json
{
  "kind": "call",
  "id": "c1",
  "name": "total_ventas",
  "args": {"mes": "2026-02"}
}
```

Su resultado:

```json
{
  "kind": "result",
  "call_id": "c1",
  "ok": true,
  "data": {"total": 12000, "moneda": "USD", "fuente": "demo_febrero"}
}
```

`id` identifica una solicitud concreta. `name` identifica la función. Dos llamadas a `total_ventas` necesitan IDs distintos, aunque compartan nombre, para no intercambiar febrero y marzo.

Si la herramienta falla:

```json
{
  "kind": "result",
  "call_id": "c1",
  "ok": false,
  "error": "mes_no_disponible"
}
```

Un error también informa: el modelo puede corregir argumentos o explicar que faltan datos. Una lista vacía como resultado válido debe distinguirse de una falla de conexión; provocan decisiones diferentes.

## 5. Las dos invariantes y su alcance

**Separación entre emitir y ejecutar.** El modelo propone; el ejecutor produce los efectos. Esto permite imponer permisos y límites antes de tocar el entorno.

**Correspondencia entre llamada y resultado.** En el protocolo de la sesión, cada llamada registrada tiene un resultado lógico asociado. Si una respuesta del modelo trae varias llamadas, deben resolverse y asociarse todas antes de continuar según el protocolo elegido. El laboratorio de estas notas admite una por decisión para concentrarse en el mecanismo.

Esta correspondencia no garantiza «ejecución exactamente una vez». Si una operación modifica algo, el servidor puede completar el cambio y perderse la respuesta. Reintentar sin un mecanismo de idempotencia podría repetir el efecto. Idempotencia significa que repetir una operación identificada no duplica su consecuencia. Es una ampliación de diseño distinta de emparejar mensajes.

## 6. Pseudocódigo que muestra el control

```text
historial ← pregunta + instrucciones
repetir hasta max_decisiones:
    decision ← modelo(historial, herramientas)
    si decision es final:
        registrar final y terminar
    registrar llamada
    resultado ← validar_y_ejecutar(decision)
    registrar resultado asociado a la llamada
    añadir llamada y resultado al historial
registrar límite y cerrar como incompleto
```

La validación y la ejecución producen también resultados de error. El límite se controla fuera del modelo: no dependemos únicamente de que obedezca «no repitas».

## 7. Qué significa «terminó»

Hay una diferencia entre **terminación del protocolo** y **éxito de la tarea**. Una salida final puede contener un cálculo falso. Una parada por límite puede conservar datos útiles sin completar el objetivo. El estado de cierre debe hacer visible esa distinción.

En la nota 66 encontrarás un programa ejecutable y casos de fallo. Antes de ejecutarlo, intenta predecir: ¿con un máximo de tres decisiones alcanzará a emitir la respuesta final del ejemplo? No: las tres decisiones se consumen consultando dos meses y calculando; se necesita la cuarta para devolver la respuesta.

**Fuente:** [[sesion-11.pdf#page=13|pp. 13–15 y 23–24]]. Identificadores, errores estructurados, idempotencia y ejemplo numérico: ampliaciones didácticas, sin dependencia de una API comercial.
