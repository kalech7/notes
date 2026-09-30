---
title: "64 S11 - Memoria contexto y costo de repetir el historial"
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

# 64 S11 - Memoria contexto y costo de repetir el historial

[[59 S11 - Guía para entender agentes y herramientas|Guía de la sesión 11]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[63 S11 - Diseñar herramientas esquemas y validación]]

Siguiente: [[65 S11 - Toolformer aprendizaje resultados y límites]]

## 1. Qué quiere decir que el modelo «no recuerda»

En la interacción básica, una nueva llamada al modelo no recupera por sí sola la conversación anterior. El sistema debe facilitar el historial o un estado derivado de él. Que la aplicación mantenga una conversación no implica que los pesos estén aprendiendo cada mensaje.

Hay que separar tres cosas:

| Concepto | Dónde está | Qué conserva |
| --- | --- | --- |
| Parámetros del modelo | Pesos entrenados | Patrones aprendidos durante entrenamiento o ajuste. |
| Contexto de esta decisión | Entrada disponible al inferir | Pregunta, instrucciones, herramientas y observaciones incluidas. |
| Estado de la aplicación | Programa, almacenamiento o servicio | Historial, resultados, identificadores y datos que podrán recuperarse. |

Un servicio puede gestionar parte del historial por ti. La responsabilidad lógica sigue existiendo aunque el cliente no reenvíe manualmente cada mensaje. Por eso «cada iteración reenvía todo» describe la implementación sencilla del curso, no todas las implementaciones posibles.

## 2. Ejemplo: perder el dato que acabas de obtener

En el paso 1 consultaste febrero: 12 000 USD. En el paso 2 consultaste marzo: 15 000 USD. Si el paso 3 recibe solo «¿cuánto crecieron?», no tiene por qué conocer esos números. Si recibe únicamente el resultado de marzo, todavía le falta la base.

Una representación mínima del estado podría ser:

```json
{
  "objetivo": "comparar marzo con febrero de 2026",
  "base": {"mes": "2026-02", "total": 12000, "moneda": "USD"},
  "actual": {"mes": "2026-03", "total": 15000, "moneda": "USD"},
  "pendiente": "calcular variacion",
  "fuentes": ["demo_febrero", "demo_marzo"]
}
```

Este estado es más pequeño que una conversación extensa, pero debe preservar correctamente significado, unidades y referencias. Si resume «febrero 12, marzo 15» puede perder miles, moneda o período.

## 3. Crecimiento de contexto: una cuenta concreta

![[45-s11-crecimiento-contexto.png]]

El eje horizontal cuenta llamadas de herramienta completadas; el vertical indica los tokens que tendría la entrada de la siguiente decisión. Cada vuelta añade 500 tokens en este ejemplo. La línea horizontal es un presupuesto ficticio de entrada, no la capacidad de un modelo comercial.

Supuestos propios:

- $B=1000$ tokens iniciales entre instrucciones, pregunta y catálogo.
- Cada llamada y resultado añaden $d=500$ tokens.
- No hay resúmenes, recortes ni otros mensajes.

Después de $n$ llamadas:

$$C_n=B+nd.$$

| Llamadas completadas $n$ | Contexto para decidir después |
| --- | --- |
| 0 | 1000 |
| 1 | 1500 |
| 2 | 2000 |
| 3 | 2500 |
| 4 | 3000 |
| 5 | 3500 |
| 6 | 4000 |

Con un presupuesto útil de 3500, después de cinco llamadas todavía cabe esa entrada; después de seis ya no. Además debe existir espacio para la salida según el contrato del modelo. En un diseño real se cuentan los tokens reales de cada mensaje y la reserva de salida; no se supone que todas las herramientas devuelvan lo mismo.

## 4. Por qué el total procesado puede crecer más deprisa

Una entrada crece linealmente bajo esos supuestos. Pero si envías el historial completo en cada una de $N$ decisiones, vuelves a incluir los tokens antiguos:

$$T_N=\sum_{i=0}^{N-1}(B+id)=NB+d\frac{N(N-1)}{2}.$$

Para siete decisiones, precedidas por cero a seis resultados:

$$T_7=7(1000)+500\frac{7(6)}{2}=17\,500.$$

La última entrada tiene 4000 tokens; el total de entradas suma 17 500. Son cantidades diferentes. Esta cuenta no incluye tokens de salida, caché, llamadas adicionales para resumir ni precios. Describe volumen lógico de contexto, no una factura ni una predicción exacta de tiempo de cómputo. Con el presupuesto ficticio de 3500, esa séptima decisión requeriría reducir contexto o ampliar el presupuesto; el total calculado ilustra el caso sin ese corte.

## 5. Cuatro estrategias y lo que arriesgan

| Estrategia | Qué conserva | Riesgo que debes revisar |
| --- | --- | --- |
| Historial completo | Mensajes anteriores mientras quepan | Crecimiento y contenido irrelevante. |
| Ventana de mensajes recientes | Últimos intercambios | Perder una restricción o dato antiguo. |
| Resumen | Síntesis del recorrido | Omitir, distorsionar o mezclar información. |
| Estado estructurado y recuperación | Campos críticos y documentos pertinentes | Recuperación incompleta o estado mal actualizado. |

No existe una compresión gratuita. Si eliminas la única referencia que identifica la moneda, no puedes recuperarla razonando mejor. Un patrón útil es conservar explícitamente objetivo, restricciones, hechos verificados, fuentes, pendientes y errores relevantes.

Al recortar mensajes del protocolo, no dejes una llamada sin su resultado. Puedes retirar pares ya cerrados y conservar un resumen externo, pero debes respetar el formato que espera el ejecutor. También debes distinguir hechos observados de hipótesis del modelo.

## 6. Memoria no equivale a verdad

Guardar un resultado falso hace que el error persista. Guardar un dato antiguo no lo actualiza. Un sistema necesita conservar procedencia e instante o versión cuando el dominio cambia.

Ejemplo: «marzo = 15 000» fue correcto antes de registrar una devolución. La memoria ayuda a recordar qué se obtuvo; no prueba que siga vigente. Consultar otra vez puede ser razonable si la pregunta exige el estado actual.

Tampoco se debe confundir una base documental de RAG con historial conversacional: la primera conserva conocimiento externo; el segundo conserva lo que pasó en la interacción. Ambas fuentes pueden incorporarse al contexto con funciones diferentes.

## 7. Pesos fijos, comportamiento diferente

Es posible escribir la idea como:

$$a_t\sim\pi_\theta(\cdot\mid c_t).$$

$\theta$ representa los parámetros; $c_t$, el contexto de la decisión; $a_t$, la acción propuesta. Cambiar $c_t$ puede cambiar la acción sin modificar $\theta$. Añadir un resultado de herramienta es precisamente un cambio de contexto. Ajustar fino, como Toolformer, sí modifica los parámetros mediante entrenamiento.

> [!abstract] Qué recordar
> La aplicación conserva y selecciona información; el modelo usa la que recibe. Contexto más largo no garantiza mejor memoria útil, y memoria útil no garantiza información verdadera.

**Fuentes:** [[sesion-11.pdf#page=10|pp. 10 y 14]]; [[Hands-On_Large_Language_Models.pdf#page=231|cap. 7, pp. impresas 209–210, 212 y 217; PDF 231–232, 234 y 239]]. Fórmulas y cifras: ampliación propia.
