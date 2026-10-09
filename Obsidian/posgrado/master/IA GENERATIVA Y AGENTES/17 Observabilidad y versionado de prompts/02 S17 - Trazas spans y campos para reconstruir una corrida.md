---
title: "02 S17 - Trazas spans y campos para reconstruir una corrida"
created: 2026-10-09
capitulo: 17
sesion: 17
tags:
  - maestria/ia-generativa
  - agentes/observabilidad
  - estudio
---

# 02 S17 - Trazas spans y campos para reconstruir una corrida

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/00 Índice - S17 Observabilidad y prompts|Índice de S17]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Una **corrida** es una ejecución completa para resolver una consulta. Una **traza** es su registro organizado. Un **span** es el registro de una operación dentro de esa corrida. En lugar de decir «el agente trabajó», podemos distinguir «validó la entrada», «llamó al modelo», «consultó una herramienta» y «produjo la respuesta».

Una analogía útil es una compra a domicilio: el pedido completo corresponde a la traza; preparar, empacar y transportar corresponden a spans. La analogía es propia. La traza reúne todos los pasos de un mismo pedido y cada paso guarda su información particular.

## Identidad y relaciones

`trace_id` identifica la corrida. `span_id` identifica un paso. `padre` señala el span que contiene ese paso. Un **identificador** es un valor usado para distinguir un registro de los demás; no describe necesariamente su contenido.

El padre expresa **anidación**, es decir, que una operación ocurrió dentro del contexto de otra. Una llamada al modelo puede estar dentro de un paso «responder». Dos pasos pueden ser hermanos porque tienen el mismo padre. Esto no significa que se ejecuten simultáneamente: la relación padre-hijo y el orden temporal son datos distintos.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/S17/01-traza-spans.png]]

El árbol muestra qué operaciones pertenecen a la misma corrida. Las barras muestran cuándo comienza y termina cada paso. En el ejemplo secuencial del PDF, 45, 900, 120 y 1 100 milisegundos suman 2 165 milisegundos. Un span largo orienta el diagnóstico de tiempo. El dibujo por sí solo no determina el costo: también hacen falta el modelo y las tarifas de cada llamada.

## Reconstruir un árbol a partir de cinco registros

Este ejemplo es **elaboración propia** y no corresponde a la figura de cuatro spans del PDF. Los cinco registros comparten `trace_id = calendario-001`. El tiempo se expresa como milisegundos desde que se abrió el padre, para que las cuentas sean visibles.

| span_id | Nombre | Padre | Inicio relativo | Final relativo | Duración |
| --- | --- | --- | --- | --- | --- |
| a1 | agente | Ninguno | 0 ms | 1 000 ms | 1 000 ms |
| g1 | validar_entrada | a1 | 10 ms | 60 ms | 50 ms |
| d1 | decidir | a1 | 60 ms | 360 ms | 300 ms |
| t1 | consultar_calendario | a1 | 380 ms | 580 ms | 200 ms |
| r1 | redactar | a1 | 580 ms | 980 ms | 400 ms |

El registro `a1` es el padre porque todos los demás lo nombran en `padre`. `g1`, `d1`, `t1` y `r1` son hermanos, aunque se ejecutan consecutivamente. Si el archivo guarda primero `t1` y al final `a1`, la relación sigue siendo la misma. La jerarquía sale de los identificadores; el tiempo sale de los intervalos.

```text
traza calendario-001
└─ a1 agente                       0 a 1000 ms
   ├─ g1 validar_entrada          10 a   60 ms
   ├─ d1 decidir                  60 a  360 ms
   ├─ t1 consultar_calendario    380 a  580 ms
   └─ r1 redactar               580 a  980 ms
```

La sangría representa pertenencia, no duración. Los intervalos de la derecha muestran que el padre abarca todos los hijos y también pequeños espacios entre ellos. El padre no es una quinta tarea de 1 000 ms que deba añadirse al resto.

La suma de hijos es `50 + 300 + 200 + 400 = 950 ms`. Los 50 ms restantes corresponden a `0–10`, `360–380` y `980–1 000`: trabajo o espera dentro del padre que este ejemplo no separó en otros spans. El **tiempo inclusivo** del padre es sus 1 000 ms completos; su **tiempo exclusivo**, bajo estos intervalos secuenciales y sin otros hijos, es `1 000 − 950 = 50 ms`. No sabemos qué tarea causó esos 50 ms hasta instrumentarla o relacionarla con otra evidencia.

Una línea de tiempo permite ver ese hueco. Un árbol solo permite ver pertenencia. Mantener ambos evita atribuir al modelo un intervalo que pudo ser preparación, transporte o espera entre operaciones.

## Los ocho requisitos y los once campos

El material enumera ocho requisitos conceptuales. Identidad y tiempo necesitan varios campos, por lo que su lista termina en once campos concretos.

| Familia | Campo | Explicación sencilla |
| --- | --- | --- |
| Identidad | `trace_id` | Qué corrida contiene el paso |
| Identidad | `span_id` | Cuál es este paso |
| Identidad | `padre` | Dentro de qué operación se abrió |
| Tiempo | `inicio` | Momento en que comenzó |
| Tiempo | `duración` | Cuánto tardó |
| Economía | `modelo` | Modelo usado en la llamada |
| Economía | `tokens_in` | Tokens enviados al modelo |
| Economía | `tokens_out` | Tokens generados por el modelo |
| Economía | `costo_estimado` | Consumo multiplicado por las tarifas aplicables |
| Cambio | `prompt_version` | Instrucciones exactas usadas |
| Resultado | `error` | Fallo técnico observado o ausencia de él |

Entradas, salidas y nombre del paso también ayudan a reconstruir el proceso; no desaparecen porque no estén en este recuento de once. La lista sirve como mínimo del ejercicio, no como definición universal de una traza.

**SQL** es un lenguaje para consultar bases de datos organizadas en tablas. Una herramienta que consulta SQL puede no usar modelo ni tokens. En ese caso los campos económicos del LLM son «no aplicables», no un consumo inventado. La herramienta puede tener otros costos, como la infraestructura, que este ejercicio no contabiliza.

## Un ejemplo de registro explicado

El siguiente JSON es **un ejemplo didáctico propio**, con costo hipotético calculado en la nota siguiente. No reproduce las trazas originales del curso.

```json
{
  "trace_id": "consulta-001",
  "span_id": "llm-001",
  "padre": "agente-001",
  "nombre": "redactar_respuesta",
  "inicio": "2026-10-09T15:00:00Z",
  "duracion_ms": 900,
  "modelo": "modelo-ejemplo",
  "tokens_in": 1200,
  "tokens_out": 100,
  "costo_estimado_usd": 0.0017,
  "prompt_version": "v2",
  "error": null
}
```

`Z` indica tiempo **UTC**, una referencia horaria común para comparar eventos de sistemas que pueden estar en lugares diferentes. `null` indica ausencia de valor en JSON; aquí expresa que no se registró un error técnico. La duración es 900 milisegundos, es decir, 0,9 segundos. El paso pertenece al agente y ambos pertenecen a la consulta 001. Un nombre claro explica el propósito del span; el identificador permite relacionarlo sin depender del nombre.

El PDF muestra `prompt_version` una vez por traza en la simulación, pero señala que el taller la solicita por span. Ambas organizaciones pueden ser coherentes si la versión se hereda sin perderse al exportar. Cuando una corrida usa varios prompts —por ejemplo, uno para decidir y otro para redactar— se debe conservar la versión correspondiente a cada llamada. Un solo «v2» global no describe necesariamente todas las instrucciones.

## Tiempo total y suma de pasos

Si cuatro spans son secuenciales, no se solapan y cubren toda la corrida, sus duraciones pueden sumar la duración total. Si dos operaciones se ejecutan en paralelo durante 500 ms cada una, ambas pueden terminar en unos 500 ms de tiempo transcurrido; sumar sus spans daría 1 000 ms. Si un padre dura 1 000 ms y contiene un hijo de 800 ms, sumarlos da 1 800 ms y cuenta parte del tiempo dos veces.

Por eso la **latencia de extremo a extremo** se mide desde el inicio hasta el final de la corrida. La suma de spans sirve para otros análisis, pero requiere conocer la estructura y el solapamiento.

> [!question]- ¿Por qué `step = 3` no reemplaza a `span_id`?
> Porque muchas corridas pueden tener un tercer paso. `step` expresa orden; un identificador distingue un registro específico y permite vincular sus hijos, errores y métricas. La identidad debe ser única dentro del alcance del sistema.

Fuente: PDF 4–6 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S17 Observabilidad y versionado de prompts.pdf#page=5|Sesión 17, página 5]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/01 S17 - Por qué una respuesta exitosa puede ser un fallo|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/03 S17 - Tokens costos y atribución del gasto|Siguiente]] →
