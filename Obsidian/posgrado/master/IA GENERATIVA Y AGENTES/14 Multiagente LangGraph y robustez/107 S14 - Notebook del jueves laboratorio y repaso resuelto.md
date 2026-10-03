---
title: "107 S14 - Notebook del jueves laboratorio y repaso resuelto"
created: 2026-10-02
fecha: 2026-10-01
capitulo: 14
sesion: "14"
tags:
  - maestria/ia-generativa
  - agentes/robustez
  - estudio
---

# 107 S14 - Notebook del jueves laboratorio y repaso resuelto

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|Índice de S14]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

El notebook adjunto tiene **13 celdas**: siete Markdown y seis de código, sin salidas guardadas. Las celdas de ejercicios están vacías; las definiciones de tickets y simulador sí están presentes. Que se ejecute sin imprimir nada no demuestra que hayas completado los ejercicios.

Esta nota explica las tres partes y añade una práctica local propia con soluciones. El original se conserva sin cambios en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/s3-jue-estudiante.ipynb|Materiales/s3-jue-estudiante.ipynb]]. La copia didáctica está en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/Practica/s3-jue-resuelto.ipynb|s3-jue-resuelto.ipynb]] y utiliza [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/Practica/s14_robustez_local.py|s14_robustez_local.py]]. Ambos archivos deben permanecer juntos.

## 1. PresupuestoAgente

La consigna 1.1 pide acumular pasos, costo y ocurrencias de `(tool, entrada)`. La solución usa `Counter` para las ocurrencias, JSON ordenado para la clave y `Decimal` para el dinero, evitando errores binarios alrededor de un límite decimal.

```python
b = PresupuestoAgente(max_pasos=2, max_usd="0.02", max_repetidas=2)
primera = b.autorizar("buscar", {"q": "a"}, "0.01")
segunda = b.autorizar("buscar", {"q": "b"}, "0.01")
tercera = b.autorizar("buscar", {"q": "c"}, "0.01")
```

Las dos primeras se autorizan y reservan consumo. La tercera se bloquea; el total queda en dos pasos y 0,02 USD simulados. `autorizar` es una extensión propia para comprobar antes del efecto. La interfaz original `registrar`/`permitir` permanece y tiene un experimento que muestra su límite retrospectivo: puede registrar una tercera repetición antes de detenerse.

Si coinciden varios límites, la implementación devuelve el primero en este orden: pasos, gasto, repetición. La razón mostrada no implica que los otros límites se encuentren disponibles.

## 2. Decorador de confirmación

Un **decorador** envuelve una función para aplicar comportamiento antes o después de llamarla. `tool_protegida` construye una propuesta con nombre, riesgo y argumentos. La cola determinista devuelve decisiones en orden.

El caso `[False, True]` rechaza `r1` y permite `r2`. La lista de efectos contiene únicamente `r2`; `r3` se rechaza por falta de una respuesta. Aprobar solo un valor booleano `True` evita que una cadena como `"no"`, que Python considera verdadera por no estar vacía, se transforme en aprobación.

La demo nunca borra registros reales. Su función solo modifica una lista en memoria. En una aplicación real, el transporte de aprobación debe verificar identidad y mantener la propuesta aprobada hasta ejecutarla; el decorador local no implementa esa infraestructura.

## 3. A/B de privilegios

| Escenario verificado | Qué se ejecuta | Qué queda demostrado |
| --- | --- | --- |
| A: lectura y envío | Lectura y envío simulado, paso 2 | El simulador vulnerable pide una capacidad disponible |
| B: solo lectura | Lectura y respuesta textual | El simulador no pide envío con ese catálogo |
| B con petición de envío forzada | Lectura y rechazo `tool_not_allowed`, paso 2 | El registro permitido impide ejecutar una función ausente |

La consigna Markdown 3.1 pide comparar configuraciones de frenos y sus pérdidas, mientras que el comentario de la celda 9 concreta dos catálogos de tools. La práctica resuelve ambos aspectos: límites con casos de frontera y A/B de catálogo. No confunde retirar una capacidad con ajustar un detector de bucles.

A admite un envío legítimo si la tarea lo exigiera, pero también expone el canal al ataque simulado. B retira ese canal y pierde la posibilidad de enviar. Para un resumen, esa pérdida no bloquea el objetivo; para un agente de correo, harían falta permisos y aprobación apropiados.

## Ejecutar y contrastar

Desde la carpeta `Practica`, ejecuta `python s14_robustez_local.py` con Python 3.10 o posterior, o abre el notebook con un kernel que tenga acceso al script. Usa biblioteca estándar; no necesita credenciales. La ejecución guarda [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/Practica/s14_resultados_verificados.json|s14_resultados_verificados.json]] con 17 comprobaciones y las tres trazas.

Los resultados verifican el código local, no un LLM real. La función denominada envío en el original también solo produce JSON; su campo `bytes` utiliza `len(contenido)`, que cuenta caracteres de Python, no bytes UTF-8. La solución propia lo llama `caracteres`.

## Repaso activo

> [!question]- 1. ¿Un especialista adicional garantiza mejor respuesta?
> No. Debe corregir una limitación identificada y mostrar mejora en una comparación controlada.

> [!question]- 2. ¿Cuáles son los tres trabajos del supervisor?
> Seleccionar al destinatario, entregar contexto y consolidar resultados. Cada uno puede fallar por razones diferentes.

> [!question]- 3. ¿Qué debe viajar en un handoff?
> Resultado parcial, objetivo siguiente y restricciones, con evidencia y formatos suficientes para interpretarlos.

> [!question]- 4. Dos ramas tienen 0,70 USD y el total de la tarea es 1 USD. ¿Estás protegido?
> No con límites independientes: podrían consumir 1,40. Necesitas reserva compartida antes de cada llamada.

> [!question]- 5. ¿Un nodo con SQL es necesariamente un agente?
> No. Puede ser una función determinista dentro del grafo de un solo agente.

> [!question]- 6. ¿Qué hace un reductor de listas?
> Combina el valor previo con la actualización. La concatenación conserva ambas listas, pero no valida su verdad ni elimina duplicados automáticamente.

> [!question]- 7. ¿Qué sucede si devuelves todo el historial con operator.add?
> Lo anterior se concatena otra vez. El nodo debe devolver solo la parte nueva.

> [!question]- 8. ¿Qué cuenta recursion_limit?
> Supersteps. Su excepción no equivale al cierre del agente con respuesta parcial y estado.

> [!question]- 9. ¿Dónde debe ir un efecto que requiere aprobación?
> Después de obtener y validar la aprobación. Los efectos previos a un interrupt pueden repetirse al reanudar el nodo.

> [!question]- 10. ¿Qué demuestra realmente B en el notebook original?
> Que el simulador toma la rama textual cuando no conoce enviar_email. El experimento forzado adicional comprueba el despachador.

> [!question]- 11. ¿Corta la tercera paráfrasis con max_repetidas=2?
> No por ese detector si sus entradas son distintas. Sí podría cortarla un límite global de pasos o de gasto.

> [!question]- 12. ¿Registrar después impide una llamada demasiado cara?
> No, el gasto ya ocurrió. Necesitas comprobar o reservar antes y conciliar después con consumo real.

> [!question]- 13. ¿Duplicar N de 8 a 16 multiplica todo el costo por 4,3?
> No. Multiplica el término triangular 28T a 120T. El término NS, las salidas y las tarifas también cuentan.

> [!question]- 14. ¿Una salida sql válida en el esquema puede ser incorrecta?
> Sí. Cumplir el tipo o enum valida forma; la clasificación requiere evaluar significado.

> [!question]- 15. ¿Qué le agrega LangSmith a un bucle correcto?
> Registros relacionados, datasets y evaluación. Una traza local también puede permitir inspección; ninguno diseña por ti la política de permisos.

> [!question]- 16. ¿Cuál es la mitigación estructural de ticket malicioso + envío?
> Eliminar envío si no es necesario, o limitar destinatarios, alcance y aprobación dentro del ejecutor. El contenido del ticket no autoriza la acción.

> [!question]- 17. ¿Qué cambia al migrar internamente a un grafo?
> El motor del flujo. La interfaz externa run(question) y sus campos deben conservarse si otras piezas dependen de ellos.

> [!question]- 18. ¿Por qué 69 menos 54 son puntos porcentuales?
> Ambas cifras son porcentajes de éxito. Su diferencia es 15 puntos; la mejora relativa usa 15/54 y es aproximadamente 27,8 %.

Fuente: notebook completo, celdas 0–12 en numeración desde cero; Fuente: PDF 22–31 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-14.pdf#page=22|sesion-14.pdf]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/106 S14 - LangSmith trazas evaluación y elección de herramientas|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/14 Multiagente LangGraph y robustez/00 Índice - S14 Multiagente LangGraph y robustez|Siguiente]] →
