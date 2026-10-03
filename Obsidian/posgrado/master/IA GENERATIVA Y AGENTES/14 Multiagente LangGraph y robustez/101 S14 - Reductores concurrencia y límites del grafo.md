---
title: "101 S14 - Reductores concurrencia y límites del grafo"
created: 2026-10-02
fecha: 2026-10-01
capitulo: 14
sesion: "14"
tags:
  - maestria/ia-generativa
  - agentes/robustez
  - estudio
---

# 101 S14 - Reductores concurrencia y límites del grafo

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|Índice de S14]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Un **reductor** es la función que combina el valor guardado en una clave con la actualización que devuelve un nodo. Con listas, `operator.add` concatena; con números suma. Su significado depende de los valores y de la operación elegida.

```python
import operator
from typing import Annotated, TypedDict

class Estado(TypedDict):
    historial: Annotated[list, operator.add]
    pasos: int
```

Si el historial actual es `["pregunta"]` y el nodo devuelve `["resultado"]`, queda `["pregunta", "resultado"]`. El nodo debe devolver la parte nueva: devolver otra vez toda la lista anterior la duplicaría. La clave `pasos` no tiene reductor; el nodo que la actualiza debe calcular explícitamente el siguiente valor.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 14/03-reductores.png]]

En el panel izquierdo, A y B escriben la misma clave durante el mismo paso paralelo. Una clave ordinaria no puede aceptar ambos valores y se produce un conflicto. En el derecho, el reductor combina listas y conserva resultados identificados. Conservar ambos no resuelve una contradicción entre ellos; todavía hay que revisar sus fuentes y significado.

Un **superstep** agrupa nodos que pueden ejecutarse en paralelo. Nodos consecutivos pertenecen a supersteps distintos. Dos escrituras en pasos sucesivos reemplazan la clave sin ese conflicto de concurrencia. Para ramas paralelas, claves separadas o un reductor apropiado definen cómo reunir los datos. No asignes significado a la posición de una lista sin un contrato de orden explícito.

## El límite del agente y el del motor

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 14/02-bucle-con-salida.png]]

El control previo revisa el consumo y el router dirige una salida final o una herramienta. La herramienta produce una observación que vuelve al estado. La salida por límite explica lo pendiente y conserva el motivo. El límite del motor protege la ejecución por otra vía: si se alcanza, puede lanzar una excepción.

`recursion_limit` cuenta supersteps, **no** llamadas al LLM. Un ciclo modelo → herramienta contiene dos supersteps; en una bifurcación varios nodos pueden compartir uno. El total depende de la topología y de los nodos de cierre. Un valor 10 no significa exactamente diez llamadas al modelo.

La sesión reporta un conflicto entre la documentación —1 000 por defecto— y el código de la versión 1.2.12 —10 007—, junto con 5 004 llamadas observadas por el docente. Esos números pertenecen a esa prueba fechada, no a una ejecución nuestra. Conviene fijar un valor explícito y dimensionarlo sobre el grafo real.

Un router propio puede emitir `max_steps_reached`, respuesta parcial y traza antes de llegar a `GraphRecursionError`. Debes definir qué cuenta `pasos`: llamadas al modelo, herramientas o iteraciones. Revisa el límite antes de la operación correspondiente. Capturar la excepción es una recuperación adicional, no reemplaza el presupuesto.

> [!question]- ¿Un reductor de suma hace seguro un presupuesto paralelo?
> No. Sumar consumos después de dos llamadas no impide que ambas se autoricen sobre el mismo saldo. La reserva debe coordinarse antes de ejecutar.

Fuente: PDF 10–12 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-14.pdf#page=10|sesion-14.pdf]].

Precisión contrastada: [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api) define supersteps, reductores y el límite de recursión; la consulta mantiene 1 000 como valor documentado. No se inspeccionó el paquete 1.2.12 del docente.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/100 S14 - Estado nodos y aristas en LangGraph|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/102 S14 - Pausas aprobación humana y contrato de salida|Siguiente]] →
