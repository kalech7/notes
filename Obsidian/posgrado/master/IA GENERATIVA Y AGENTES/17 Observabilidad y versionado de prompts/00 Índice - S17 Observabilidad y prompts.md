---
title: "00 Índice - S17 Observabilidad y prompts"
created: 2026-10-09
capitulo: 17
sesion: 17
tags:
  - maestria/ia-generativa
  - agentes/observabilidad
  - estudio
---

# 00 Índice - S17 Observabilidad y prompts

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/00 Índice - S17 Observabilidad y prompts|Índice de S17]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Esta sesión responde una pregunta práctica: **si una respuesta salió mal, ¿cómo sabemos en qué paso ocurrió y con qué instrucciones?** Las notas explican el contenido de las 37 páginas del PDF con ejemplos propios, imágenes, diagramas y un laboratorio local resuelto.

No hace falta abrir el PDF para seguir las explicaciones. Las referencias por página sirven para contrastar. Los scripts, repositorios, claves y órdenes descritos por las diapositivas son material académico, no acciones realizadas al preparar estas notas.

## Ruta de lectura

1. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/01 S17 - Por qué una respuesta exitosa puede ser un fallo|Por qué una respuesta exitosa puede ser un fallo]]: HTTP 200, logs, observabilidad y evidencia.
2. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/02 S17 - Trazas spans y campos para reconstruir una corrida|Trazas, spans y campos]]: identidad, árbol reconstruido, intervalos, tiempo exclusivo y datos mínimos.
3. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/03 S17 - Tokens costos y atribución del gasto|Tokens y costo]]: fórmula explicada, llamadas con distintos modelos, reintentos y cuentas verificadas.
4. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/04 S17 - Latencia percentiles y diagnóstico de anomalías|Latencia y percentiles]]: media, p50, p95, máximos, paralelismo y camino crítico.
5. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/05 S17 - Instrumentar el bucle y conservar los errores|Instrumentación interna]]: registro de fallos, finally y limitaciones del andamiaje.
6. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/06 S17 - Langfuse y el mapa de sus objetos|Langfuse]]: objetos, instrumentación automática/manual y comparación de alternativas.
7. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/07 S17 - Configuración privacidad y exportación de trazas|Configuración y privacidad]]: servicios, credenciales, máscaras, sesión, flush y exportación.
8. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/08 S17 - Versiones etiquetas evaluación y rollback de prompts|Versionar prompts]]: plantillas, versiones, etiquetas, comparación por caso, fallback y rollback.
9. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/09 S17 - Laboratorio resuelto sin API ni servicios externos|Laboratorio propio resuelto]]: diez corridas ficticias que conservan bloqueos y errores.
10. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/10 S17 - Repaso activo y preguntas resueltas|Repaso activo]]: preguntas plegables y un caso integrado.

El hilo común es registrar para explicar, evaluar para decidir y versionar para reconstruir. Una traza no demuestra calidad por sí sola; una evaluación sin traza tampoco explica todas las causas.

## Material y alcance

- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S17 Observabilidad y versionado de prompts.pdf|PDF original de S17]], 37 páginas, clase del martes 6 de octubre de 2026.
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/99 Fuentes y cobertura S17|Cobertura por página, discrepancias y validaciones]].
- [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/Practica/s17_trazador_local.py|Script del laboratorio propio]], solo biblioteca estándar de Python.

Las cuentas del PDF usan tarifas históricas de su tabla semestral. Las notas distinguen cifras citadas de ejemplos propios y explican qué no puede recalcularse sin las trazas originales. Las versiones de servicios y cuotas mencionadas son las declaradas en el material; no se presentan como vigentes.

## Al terminar

Deberías poder abrir una corrida, explicar la diferencia entre su árbol y sus tiempos, calcular consumo bajo tarifas conocidas, distinguir fallo técnico de fallo de calidad, conservar errores sin silenciarlos y comparar dos prompts con evidencia.

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/01 S17 - Por qué una respuesta exitosa puede ser un fallo|Comenzar la lectura]] →
