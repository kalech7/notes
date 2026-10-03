---
title: "97 S14 - Cuándo dividir un agente y usar un supervisor"
created: 2026-10-02
fecha: 2026-10-01
capitulo: 14
sesion: "14"
tags:
  - maestria/ia-generativa
  - agentes/robustez
  - estudio
---

# 97 S14 - Cuándo dividir un agente y usar un supervisor

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|Índice de S14]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Un sistema multiagente coordina varios agentes para resolver una tarea. Cada agente puede tener un objetivo, contexto y herramientas propios. **La topología** es la forma de conectar esas piezas: quién recibe una petición, quién devuelve resultados y quién decide qué sigue.

Un nodo que ejecuta SQL no es automáticamente otro agente. Para hablar de agente tiene que existir alguna decisión sobre acciones o pasos; una función determinista puede ser simplemente una herramienta. En ambos casos, el modelo propone y el programa decide qué ejecutar.

## Un caso concreto: informe de ventas

El usuario pide «explica las ventas de marzo y las restricciones de devolución». Un único agente puede consultar ventas, recuperar políticas y redactar. Dividirlo tiene sentido si has observado un problema concreto: el contexto se vuelve demasiado grande, la clasificación de políticas necesita instrucciones distintas o dos consultas independientes tardan mucho.

Un **supervisor** mantiene el control central y delega subproblemas. Por ejemplo, pide al agente de datos un total, al de políticas una regla con citas y después combina ambos. Tiene tres trabajos diferentes:

| Trabajo | Error posible | Comprobación útil |
| --- | --- | --- |
| Seleccionar al especialista | Envía una pregunta de políticas al analista SQL | Evaluar ejemplos de enrutamiento |
| Preparar el contexto | Omite que la pregunta se refiere a marzo de 2026 | Contrato con período, alcance y fuentes |
| Consolidar | Suma cifras de monedas distintas o elige una respuesta sin evidencia | Verificador de unidades y contraste de fuentes |

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 14/01-topologias.png]]

La columna izquierda conserva el control en el supervisor. En el centro, A entrega a B un contrato y B continúa. A la derecha, dos ramas reciben trabajo independiente y una función posterior reúne sus resultados. Las cajas ámbar concentran decisiones de coordinación; las verdes representan el punto donde el trabajo puede cerrarse. Una jerarquía, un traspaso y una bifurcación pueden usar especialistas parecidos y tener comportamientos diferentes.

## Contexto y profundidad

La ventana de contexto es la cantidad de tokens que el modelo puede procesar en una llamada. La memoria del sistema puede contener más información, pero solo una selección entra en esa ventana. Un supervisor que filtra contexto intenta entregar lo pertinente; difundir todo a todos reduce el riesgo de omitir un dato, pero repite información y puede saturar cada llamada.

No existe una comparación experimental de ambas estrategias en estos materiales. El costo de difundir puede ser mayor **si** manda más tokens a llamadas comparables; el costo total también depende de reintentos, longitud de respuestas y trabajo duplicado.

Un límite de profundidad acota delegaciones anidadas: supervisor → especialista → subespecialista. Un límite de pasos acota la ejecución de cada bucle. Tener profundidad máxima 2 no impide que un especialista se repita 100 veces; ambos controles son distintos. Cada llamada a una herramienta debe recibir un resultado identificable, incluso cuando el resultado sea un rechazo o un error controlado.

> [!question]- ¿Cuándo agregar otro agente?
> Cuando puedes nombrar el fallo que intentas corregir y comparar la nueva arquitectura con el agente único sobre las mismas tareas. «Tiene más roles» no es una medida de calidad.

Fuente: PDF 2–5 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-14.pdf#page=2|sesion-14.pdf]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/98 S14 - Contratos de traspaso y paralelismo|Siguiente]] →
