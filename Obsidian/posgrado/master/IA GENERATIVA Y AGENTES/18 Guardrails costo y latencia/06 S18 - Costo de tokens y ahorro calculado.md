---
title: "06 S18 - Costo de tokens y ahorro calculado"
created: 2026-10-09
fecha: 2026-10-07
capitulo: 18
sesion: 18
tags:
  - maestria/ia-generativa
  - agentes/llmops
  - estudio
  - arquitectura/costos
---

# 06 S18 - Costo de tokens y ahorro calculado

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/00 Índice - S18 Guardrails costo y latencia|Índice de S18]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

## Primero las unidades y los supuestos

La sesión utiliza una tabla histórica con tarifas en **USD por un millón de tokens**. Para estudiar el ejercicio se mantienen sus números:

| Etiqueta del PDF | Identificador citado en la tabla | Entrada USD / 1 M | Salida USD / 1 M |
| --- | --- | ---: | ---: |
| Modelo grande | `claude-opus-4-8` | 5 | 25 |
| Modelo pequeño | `claude-haiku-4-5` | 1 | 5 |

Son datos reportados por el material como verificados el 10 de julio de 2026. Estas notas **no confirman la disponibilidad de esos identificadores ni presentan esas tarifas como actuales**. El ejercicio no usa precios de caché ni lote porque la tabla mostrada no los contiene.

La entrada suele incluir más que la pregunta: instrucciones de sistema, ejemplos, historial y documentos. La salida es lo generado. Para este ejercicio se cuentan exactamente los tokens especificados por el PDF; en una integración hay que utilizar el desglose de uso que devuelve el proveedor y sus condiciones de facturación.

$$C=\frac{T_{entrada}\,P_{entrada}+T_{salida}\,P_{salida}}{1\,000\,000}.$$

Si un proveedor reporta categorías adicionales, como lectura y escritura de caché o tokens de razonamiento, hay que incorporarlas según su política. Usar la fórmula de dos categorías en un servicio con cuatro puede producir una estimación incorrecta.

## Actividad de la página 24: costo por llamada y por mes

Los conteos de la actividad son inventados para practicar: prefijo estable de 2 000 tokens, pregunta de 100 y respuesta de 300. El **prefijo estable** es el texto inicial que se repite, por ejemplo instrucciones y ejemplos. Entrada total: `2 000 + 100 = 2 100`. Hay 1 000 llamadas diarias durante 30 días: `1 000 × 30 = 30 000 llamadas`.

**Modelo grande:**

1. Entrada: `2 100 × 5 / 1 000 000 = USD 0,0105`.
2. Salida: `300 × 25 / 1 000 000 = USD 0,0075`.
3. Llamada: `0,0105 + 0,0075 = USD 0,018`.
4. Mes: `30 000 × 0,018 = USD 540`.

**Modelo pequeño:**

1. Entrada: `2 100 × 1 / 1 000 000 = USD 0,0021`.
2. Salida: `300 × 5 / 1 000 000 = USD 0,0015`.
3. Llamada: `0,0021 + 0,0015 = USD 0,0036`.
4. Mes: `30 000 × 0,0036 = USD 108`.

Los dos componentes del grande valen exactamente cinco veces los del pequeño. Por eso `540/108 = 5`, para esta misma cantidad de tokens. El rango «5–25×» que la página 23 corrige no se deriva de estas dos filas: 25 es una tarifa de salida, no la razón entre costos totales.

## Cuánto del costo es el prefijo repetido

En el grande, el prefijo cuesta `2 000 × 5 / 1 000 000 = USD 0,01`. Su parte del total es `0,01 / 0,018 = 55,56 %`.

En el pequeño, cuesta `2 000 × 1 / 1 000 000 = USD 0,002`. Su parte es `0,002 / 0,0036 = 55,56 %`.

Que el prefijo represente el 55,56 % del costo **no demuestra** que el ahorro por caché será 55,56 %. Se necesita saber cuánto cuesta crear la caché, cuánto cuesta leerla, qué llamadas aciertan y cuánto dura. La página 25 compara también con `gpt-4o-mini` en su figura: allí el prefijo aparece como 60,6 %, la pregunta 2,8 % y la respuesta 36,4 %. Ese tercer modelo explica el rango 55,6–60,6 %. Sus tarifas no aparecen en la tabla de esta actividad, por lo que no se reconstruye su costo absoluto. Para Opus/Haiku, las dos filas del ejercicio dan 55,56 % en ambos modelos.

## Un router envía el 60 % al pequeño

Un **router** decide qué modelo atiende cada solicitud. Supongamos que conserva la calidad, que no añade llamadas pagadas y que ambos modelos generan la misma cantidad de tokens. Son supuestos del cálculo, no resultados medidos.

1. Grande: `40 % × 30 000 = 12 000 llamadas`; costo `12 000 × 0,018 = USD 216`.
2. Pequeño: `60 % × 30 000 = 18 000 llamadas`; costo `18 000 × 0,0036 = USD 64,80`.
3. Total: `216 + 64,80 = USD 280,80`.
4. Ahorro: `540 − 280,80 = USD 259,20`.
5. Porcentaje: `259,20 / 540 = 48 %`.

El router no reduce el total cinco veces porque el 40 % sigue en el grande. Si la razón grande/pequeño es `r` y se enruta fracción `f`, el ahorro ideal es `f(1 − 1/r)`. Con `f=0,6` y `r=5`, da `0,6 × 0,8 = 0,48`. Aunque el pequeño fuera gratis, con esa fracción el techo sería 60 %.

## Qué pasa si una parte de las solicitudes pequeñas termina en el grande

Extensión didáctica propia. Partimos del router de 60 % y suponemos que el 10 % de esas solicitudes pequeñas requiere después una llamada al grande. La primera llamada al pequeño ya se pagó: no se recupera ese importe por escalar.

1. Solicitudes enviadas al pequeño: 18 000.
2. Escalamientos: `10 % × 18 000 = 1 800` llamadas adicionales al grande.
3. Costo extra: `1 800 × 0,018 = USD 32,40`.
4. Total mensual: `280,80 + 32,40 = USD 313,20`.
5. Ahorro frente a USD 540: `(540 − 313,20)/540 = 42 %`.

La reducción ideal era 48 %; con ese escalamiento es 42 %. Si el segundo intento incluye el historial fallido o genera una respuesta más larga, puede costar más de USD 0,018. Si un clasificador de router consume una API, su costo se añade a todas las solicitudes que lo usen.

También hay que comparar tareas terminadas correctamente: un router que parece barato porque responde mal a muchos casos no conserva la misma utilidad. Se puede estudiar costo por solicitud y costo por tarea resuelta, pero se declara cuál es el denominador y cómo se comprobó la solución.

## Acortar el prefijo a la mitad

Se conserva la pregunta de 100 y la salida de 300. Entrada nueva: `1 000 + 100 = 1 100` tokens.

| Escenario | Grande: USD por llamada | Grande: USD al mes | Pequeño: USD al mes |
| --- | ---: | ---: | ---: |
| Prefijo de 2 000 | 0,018 | 540 | 108 |
| Prefijo de 1 000 | `0,0055 + 0,0075 = 0,013` | 390 | 78 |

Ahorro del grande: `540 − 390 = USD 150`, equivalente a `150/540 = 27,78 %`. Ahorro del pequeño: `108 − 78 = USD 30`, también 27,78 %. Se redujo la mitad del prefijo, no la mitad del costo: la pregunta y la salida siguen pagándose.

Acortar un prompt debe evaluarse: si desaparecen ejemplos necesarios y aumentan los reintentos, el ahorro previsto puede perderse. Comparar dinero sin calidad equivale a comparar tareas distintas.

## Un presupuesto tiene que mirar la próxima llamada

Un **presupuesto** es un límite de recursos permitido por tarea o período. Revisar después de llamar sirve para conocer el gasto, pero ya no impide que esa llamada lo exceda. Una autorización previa estima o reserva la operación siguiente, limita tokens y reintentos, y después concilia con el consumo real. Si la estimación es demasiado baja, el límite monetario no es duro.

Ejemplo propio con presupuesto de USD 0,05 y gasto ya confirmado de USD 0,035. Quedan `0,05 − 0,035 = USD 0,015`. La próxima llamada puede costar como máximo estimado USD 0,018. Comparar solo `0,035 < 0,05` la dejaría pasar; comparar `0,035 + 0,018 ≤ 0,05` la rechaza antes de generar. Registrar después revelaría un total de USD 0,053 cuando el gasto ya ocurrió.

**Reservar** significa apartar temporalmente el importe autorizado para que no lo utilice otra operación pendiente. Con USD 0,05 disponibles, una llamada reserva USD 0,018: quedan USD 0,032 disponibles aunque todavía no se haya cobrado. Si termina gastando USD 0,016, **conciliar** reemplaza la reserva por el consumo real: quedan `0,05 − 0,016 = USD 0,034`.

| Momento | Gasto confirmado | Reserva pendiente | Disponible |
| --- | ---: | ---: | ---: |
| Inicio | 0 | 0 | 0,050 |
| Autorizar una llamada | 0 | 0,018 | 0,032 |
| Conciliar uso real | 0,016 | 0 | 0,034 |

La regla general es `disponible = límite − confirmado − reservas`. Cada intento necesita su reserva. La práctica añade una clase local que hace estas operaciones de forma **serial**: una después de otra. En un sistema con solicitudes simultáneas, consultar el saldo y reservar debe ser una operación indivisible, para que dos llamadas no gasten el mismo saldo.

La estimación debe cubrir el uso posible según límites de entrada, salida y categorías facturadas. Si se reserva USD 0,018 y la factura real llega a USD 0,022, se registra USD 0,022 y se señala la diferencia; esconderla mantendría un saldo falso. Una reserva de una estimación insuficiente protege la contabilidad previa, pero no garantiza el límite real. Para una operación sin consumo confirmado no se libera dinero por un simple timeout si aún puede haber cobro: primero hay que conocer qué ocurrió.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/S18/02-presupuesto-latencia.png]]

La imagen compara los costos de mantener el modelo grande, usar el pequeño, enrutar una parte del tráfico y reducir el prefijo. El panel de tiempo distingue la espera hasta el primer token emitido de la duración total. El primer contenido visible y útil es otra medida, explicada en la nota 07. El gasto y el tiempo necesitan métricas propias: un modelo más barato puede tardar más y mostrar contenido pronto no implica terminar pronto.

> [!question]- ¿Cuánto costaría combinar el router del 60 % con el prefijo reducido?
> Es una extensión propia, no el escenario «en vez de eso» del PDF. Grande: `12 000 × 0,013 = 156`. Pequeño: `18 000 × 0,0026 = 46,80`. Total: USD 202,80; ahorro frente a USD 540: USD 337,20, o 62,44 %. Supone la misma calidad, longitud de salida y ausencia de costo de router.

Fuente: PDF 22–25 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S18 Guardrails costo y latencia.pdf#page=22|Sesión 18, p. 22]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/05 S18 - Medir guardrails y equilibrar seguridad y utilidad|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/07 S18 - Cachés streaming batching y latencia|Siguiente]] →
