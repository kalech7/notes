---
title: "00 Índice - S14 Multiagente LangGraph y robustez"
created: 2026-10-02
capitulo: 14
sesion: "14"
tags:
  - maestria/ia-generativa
  - agentes/robustez
  - estudio
---

# S14: multiagente, LangGraph y robustez

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

La sesión 14 une dos preguntas: **¿cómo coordinar agentes y cómo limitar las acciones que pueden ejecutar?** Un grafo organiza el flujo; un presupuesto acota su consumo; los permisos y la aprobación deciden qué efectos están autorizados. La explicación conserva el agente único como punto de comparación.

Esta ampliación desarrolla los dos PDF y el notebook del jueves. Incluye nueve esquemas explicados, ejemplos propios, tablas de evidencia histórica, una práctica local resuelta y 18 preguntas con respuesta. Las cifras del docente, el artículo histórico y los resultados locales se distinguen en las notas.

## Ruta de lectura

- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/97 S14 - Cuándo dividir un agente y usar un supervisor|97 S14 - Cuándo dividir un agente y usar un supervisor]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/98 S14 - Contratos de traspaso y paralelismo|98 S14 - Contratos de traspaso y paralelismo]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/99 S14 - Evidencia histórica y cómo comparar varios agentes|99 S14 - Evidencia histórica y cómo comparar varios agentes]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/100 S14 - Estado nodos y aristas en LangGraph|100 S14 - Estado nodos y aristas en LangGraph]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/101 S14 - Reductores concurrencia y límites del grafo|101 S14 - Reductores concurrencia y límites del grafo]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/102 S14 - Pausas aprobación humana y contrato de salida|102 S14 - Pausas aprobación humana y contrato de salida]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/103 S14 - Presupuestos repetición y costo del historial|103 S14 - Presupuestos repetición y costo del historial]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/104 S14 - Inyección indirecta mínimo privilegio y responsabilidad|104 S14 - Inyección indirecta mínimo privilegio y responsabilidad]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/105 S14 - LangChain modelos herramientas RAG y salidas estructuradas|105 S14 - LangChain modelos herramientas RAG y salidas estructuradas]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/106 S14 - LangSmith trazas evaluación y elección de herramientas|106 S14 - LangSmith trazas evaluación y elección de herramientas]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/107 S14 - Notebook del jueves laboratorio y repaso resuelto|107 S14 - Notebook del jueves laboratorio y repaso resuelto]].

Para comprender primero el mecanismo: 97–98 muestran coordinación, 100–102 el grafo y sus pausas, 103–104 los controles. La nota 99 enseña a evaluar afirmaciones de mejora. Las notas 105–106 conectan bibliotecas, RAG, observabilidad y costos. La 107 cierra con código local y repaso.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 14/08-tres-bibliotecas.png]]

Las tres cajas separan conexión con capacidades, coordinación de estados y registro de la ejecución. La banda inferior contiene decisiones que ninguna biblioteca toma por ti: permisos, presupuesto y criterios para verificar una respuesta. Puedes aplicar esas decisiones también a un bucle escrito directamente en Python.

## Puente con lo que ya estudiaste

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|La sesión 12]] desarrolla ReAct, Reflexion y planificación. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|La sesión 13]] explica cómo descubrir herramientas. Descubrir una capacidad no concede permiso para usarla: S14 pone controles en la ejecución y estudia la coordinación.

El motor del miércoles está en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/94 PRÁCTICA - Notebook del miércoles grafos checkpoints y MCP|la práctica del miércoles]]. El jueves añade presupuesto, confirmación y un A/B de privilegios. La copia resuelta se abre desde [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/107 S14 - Notebook del jueves laboratorio y repaso resuelto|la guía 107]].

## Fuentes y alcance

Se leyeron las 31 páginas de `sesion-14.pdf`, las 15 de `tutorial-langgraph.pdf` y las 13 celdas del notebook. Las páginas visibles coinciden con la posición PDF. Los originales están en `Materiales`, sin cambios. El mapa de cobertura, las precisiones y la validación están en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/17 FUENTES - Sesión 14 tutorial y robustez|fuentes y revisión de S14]].

Los programas que el docente cita como verificados, los Lab 03/04 y los datos del tutorial no fueron adjuntados. Sus resultados se explican como declaraciones del material. El complemento local utiliza biblioteca estándar y acciones simuladas; su ejecución no reproduce la H200 ni mide un modelo real.

> [!info] Contexto del curso
> El PDF anuncia Taller 3 para el sábado 3 de octubre de 2026, con un peso del 25 %, un agente único y tres herramientas como baseline. Multiagente y LangGraph son extensiones. Los ejercicios, instrucciones de conexión y requisitos de entrega de los adjuntos se trataron como contenido académico.

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/93 S13 - Ejercicios resueltos y repaso activo|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/97 S14 - Cuándo dividir un agente y usar un supervisor|Siguiente]] →
