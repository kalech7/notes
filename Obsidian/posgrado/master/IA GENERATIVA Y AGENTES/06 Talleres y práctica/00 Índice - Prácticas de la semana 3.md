---
title: "Prácticas de la semana 3 - IA generativa y agentes"
created: 2026-09-30
tags:
  - maestria/ia-generativa
  - agentes
  - practica
---

# Prácticas de la semana 3: empieza por el lunes

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Estas cuatro prácticas construyen un recorrido: **ejecutar herramientas → controlar errores y reintentos → coordinar tareas y publicar herramientas → controlar consumo, aprobación y privilegios**. Cada una tiene una explicación del código y un notebook resuelto con salidas guardadas de una ejecución local.

| Día | Qué aprendes | Guía | Notebook ejecutable |
| --- | --- | --- | --- |
| Lunes | Definir herramientas, recibir una petición, ejecutar la función y devolver su resultado al simulador. | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/95 PRÁCTICA - Notebook del lunes resuelto y explicado\|Lunes explicado]] | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/Practica lunes/s3-lun-resuelto.ipynb\|s3-lun-resuelto.ipynb]] |
| Martes | Diagnosticar trazas, detectar repeticiones, limitar pasos y costo y corregir salidas con feedback. | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/96 PRÁCTICA - Notebook del martes resuelto y explicado\|Martes explicado]] | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/Practica martes/s3-mar-resuelto.ipynb\|s3-mar-resuelto.ipynb]] |
| Miércoles | Implementar un grafo de estados, pausar y restaurar una ejecución y descubrir herramientas mediante un MCP simulado. | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/94 PRÁCTICA - Notebook del miércoles grafos checkpoints y MCP\|Miércoles explicado]] | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/Practica miercoles/s3-mie-resuelto.ipynb\|s3-mie-resuelto.ipynb]] |
| Jueves | Limitar pasos, costo y repetición; confirmar efectos; comparar catálogos y rechazar una tool ausente. | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/107 S14 - Notebook del jueves laboratorio y repaso resuelto\|Jueves explicado]] | [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/Practica/s3-jue-resuelto.ipynb\|s3-jue-resuelto.ipynb]] |

## Cómo trabajar cada notebook

1. Abre la guía del día para reconocer qué piezas construirás.
2. Abre el notebook resuelto en Jupyter o VS Code con soporte para notebooks.
3. Lee el comentario explicativo anterior a cada celda de código. Predice su resultado y luego ejecútala.
4. Ejecuta las celdas en orden: las últimas dependen de funciones y variables de las primeras.
5. Revisa la traza y las comprobaciones finales. Cambia una pregunta o un límite para observar qué parte del resultado cambia.

Los notebooks usan la biblioteca estándar de Python y simuladores locales. La conexión real del lunes y la traducción opcional del miércoles a LangGraph se conservan como lectura. Las salidas demuestran comportamiento del código didáctico; no evalúan un modelo remoto ni un servidor MCP real.

Usa un kernel de **Python 3.10 o posterior** para ejecutar las cuatro prácticas: las anotaciones del lunes incluyen la sintaxis `str | None`. Reinicia el kernel antes de una ejecución completa si habías cambiado variables o funciones durante los experimentos.

## Originales y resultados

Los originales del lunes y martes están junto a sus soluciones:

- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/Practica lunes/s3-lun-estudiante.ipynb|Original del lunes]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/Practica lunes/s3-lun-resultados-verificados.json|Resultados del lunes]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/Practica martes/s3-mar-estudiante.ipynb|Original del martes]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/Practica martes/s3-mar-resultados-verificados.json|Resultados del martes]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/s3-mie-estudiante.ipynb|Original del miércoles]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/Practica miercoles/s3-mie-resultados-verificados.json|Resultados del miércoles]].

Las copias originales conservan los huecos de los ejercicios. Las soluciones están en archivos separados, con las correcciones explicadas: reconocimiento de resultados del simulador del lunes; verificación de tipos y feedback del martes; distinción entre decisión pendiente y rechazo del miércoles.

El jueves utiliza el script [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/Practica/s14_robustez_local.py|s14_robustez_local.py]] junto al notebook. El original está en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/s3-jue-estudiante.ipynb|Materiales]] y los resultados en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/Practica/s14_resultados_verificados.json|resultados del jueves]]. Sus acciones sensibles son simulaciones locales.
