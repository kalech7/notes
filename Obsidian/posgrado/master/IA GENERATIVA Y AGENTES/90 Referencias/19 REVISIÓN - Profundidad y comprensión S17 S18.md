---
title: "Revisión de profundidad y comprensión - S17 y S18"
created: 2026-10-09
capitulo: 18
sesion: "17 y 18"
tags:
  - maestria/ia-generativa
  - referencias
  - estudio
---

# Qué se revisó para que las notas expliquen y permitan aplicar

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/01 Guía - Entender las sesiones 17 y 18|Guía conjunta]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

La segunda revisión del 9 de octubre se realizó con tres subagentes: uno revisó y profundizó S17, otro S18 y un tercero contrastó de forma independiente la claridad, los cálculos y la coherencia. El criterio fue un lector que no abrió los PDF: la explicación debe permitir entender qué es cada cosa, por qué hace falta, cómo funciona y qué resultado produce.

La revisión inicial encontró definiciones y explicaciones correctas en las 16 notas temáticas. La mejora necesaria estaba en algunos **ejemplos de mecanismo**: había descripciones correctas de operaciones sin suficientes estados intermedios para verlas actuar. Se añadieron transformaciones, registros, cuentas y decisiones concretas. No se evaluó la profundidad por longitud del texto.

## Criterios aplicados

| Criterio | Qué se comprobó |
| --- | --- |
| Definición | El término se explica al introducirlo y se conecta con algo concreto |
| Motivo | Se explica qué problema resuelve y qué pasa si falta |
| Mecanismo | Se presentan operaciones, orden y decisiones, no solo el nombre de una herramienta |
| Ejemplo resuelto | Se conocen entrada, pasos, resultado y cómo interpretar ese resultado |
| Alcance | Un caso inventado no se presenta como una medición y un formato válido no se confunde con verdad |
| Autoevaluación | Hay preguntas con soluciones razonadas para comprobar comprensión |

## Qué se profundizó

| Tema | Qué estaba explicado | Qué permite ver ahora |
| --- | --- | --- |
| Trazas y jerarquía | Campos, padres y spans | Reconstrucción del árbol desde filas y diferencia entre tiempo total, exclusivo y solapado |
| Costo de una ejecución | Fórmula de entrada y salida | Varias llamadas, modelos diferentes y reintentos pagados, con unidades explícitas |
| Instrumentación | Decoradores, `with` y excepciones | Apertura, paso interno, cierre y registro concreto del error que se propaga |
| Privacidad | Máscara recursiva y ramas | Diccionario, lista y tupla antes/después; registros protegidos de caminos bloqueados |
| Prompts | Versión, etiqueta y rollback | Plantilla, valores insertados, texto compilado y tabla v1/v2 que conduce a una decisión |
| Controles en RAG | Permisos, evidencia y salida | Consulta concreta que puede detenerse en cada borde y distinción entre cita existente y apoyo real |
| Normalización | Minúsculas, Unicode y espacios | Representaciones intermedias y qué cambia en cada transformación |
| Medición | Matriz y denominadores | Relación entre política, etiqueta y falso positivo; separación de bloqueo y redacción |
| Router | Ahorro ideal del 48 % | Escalamiento posterior al grande: la primera llamada se paga y el ahorro puede bajar al 42 % en el ejemplo |
| Presupuesto | Revisar antes de llamar | Reservar, conciliar y rechazar también un reintento por saldo insuficiente |
| Caché | Prefijo frente a respuesta | Primera escritura, lecturas posteriores y punto de equilibrio con tarifas inventadas explícitas |
| Streaming | Primer token frente a respuesta completa | Conflicto entre liberar texto pronto y validarlo antes de publicarlo |

La [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/99 Fuentes y cobertura S17|revisión S17]] y la [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/18 Guardrails costo y latencia/99 Fuentes y cobertura S18|revisión S18]] documentan sus cambios específicos. El [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/02 Caso resuelto - Diagnosticar y mejorar un asistente de ventas|caso conjunto de ventas]] conecta las piezas con una consulta que falla, su diagnóstico, una política nueva y una ejecución explicada con tiempos y costo.

## Qué demuestran las prácticas

S17 conserva una ejecución exitosa, una bloqueada y una fallida; registra sus pasos, propagación de excepción y saneamiento antes de exportar. Sus tokens son ficticios y sus intervalos son los medidos al ejecutar operaciones locales pequeñas.

S18 comprueba las tildes, los errores de redacción, las matrices de casos sintéticos, el texto que llega al simulador, los reintentos, el registro protegido y la selección de una versión activa. La ampliación integra reserva y conciliación de presupuesto antes y después de cada llamada simulada: si no se autoriza la siguiente reserva, esa llamada no ocurre. También registra una estimación insuficiente sin esconder el gasto real.

Las comprobaciones validan esos mecanismos programados. No son resultados del agente del curso ni un experimento de calidad con un modelo real. El caso narrativo usa cifras fijadas para enseñar y no declara una tercera ejecución de software.

## Cómo comprobar comprensión al estudiar

El primer recorrido puede ser la guía y el caso conjunto. Después, cada sesión desarrolla sus mecanismos y termina con práctica y repaso. Una respuesta entendida debe poder justificar tres cosas: **qué dato cambió, qué operación produjo el cambio y qué evidencia permite comprobarlo**.

Por ejemplo, «el control es seguro» resulta demasiado general. «El control sustituyó una lista de tiendas porque su regex admite espacios entre dígitos; la traza muestra una sustitución y cero tiendas recuperadas» identifica un mecanismo y una consecuencia. La solución debe comprobar que conserva los números autorizados y que no abre un camino indebido para los demás datos.

Las preguntas resueltas sirven para comprobar esa distinción. Las referencias del PDF permiten contrastar la procedencia, pero no son necesarias para llenar pasos omitidos: la explicación de los mecanismos y los ejemplos queda en las notas.

## Resultado final de la revisión

Las ampliaciones fueron contrastadas de forma independiente. La revisión no dejó errores conceptuales o aritméticos pendientes en los ejemplos añadidos. La comprobación estructural y el renderizado final están registrados en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/18 FUENTES - Sesiones 17 y 18 integración|fuentes y validación del conjunto]] y [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/Validación S17 S18/resultado.json|el resultado del validador]].

Las huellas de los PDF, las imágenes, los scripts y la guía de reproducción se conservan con las notas. El validador usa las copias dentro del repositorio y puede comprobar los originales opcionalmente; ya no depende de que el lector tenga la carpeta Descargas del autor.

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/02 Caso resuelto - Diagnosticar y mejorar un asistente de ventas|Anterior: caso resuelto]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/01 Guía - Entender las sesiones 17 y 18|Siguiente: guía conjunta]] →
