---
title: "91 S13 - Agentes analistas de código y de investigación"
created: 2026-09-30
fecha: 2026-09-30
capitulo: 13
sesion: "13"
tags:
  - maestria/ia-generativa
  - agentes/mcp
  - estudio
---

# 91 S13 - Agentes analistas de código y de investigación

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|Índice de la sesión 13]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

## El mismo bucle, distintas evidencias

La sesión distingue agentes analistas, de código y de investigación. En los tres casos hay una tarea, selección de herramienta, resultado y decisión posterior. Cambian las operaciones disponibles y el criterio que permite aceptar una respuesta.

Un **verificador** es un procedimiento que comprueba una condición concreta. Puede ser una cuenta, un test o una revisión de evidencia. Su fuerza depende de qué comprueba, no de que se llame verificador.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 13/06-verificadores.png]]

Cada fila une un tipo de trabajo con su evidencia principal. El analista necesita cuentas sobre datos correctos; el agente de código necesita casos que representen el contrato; el de investigación necesita fragmentos que sostengan sus afirmaciones. Ninguna fila garantiza por sí sola que toda la tarea esté resuelta.

## Analista: recalcular sobre datos adecuados

La tarea es «compara abril con marzo». Usamos los totales didácticos ya empleados en las sesiones anteriores: marzo 2695, abril 1670. El agente debe consultar ambos meses, verificar qué representan y calcular:

$$\Delta=1670-2695=-1025.$$

$$\Delta\%=\frac{-1025}{2695}\times100\approx-38{,}03\%.$$

Marzo es el denominador porque se pregunta cómo cambió abril respecto de marzo. La conclusión es una caída de 38,03 % en los totales registrados. Si los períodos tienen cobertura distinta o faltan ventas, debe expresarse esa limitación.

Un SQL que devuelve un número no asegura haber filtrado el mes correcto. El verificador puede contrastar filtros, totales, unidad monetaria y denominador. El gráfico debe utilizar los mismos datos. La caída no demuestra una causa: no hay información sobre campañas, competencia o inventario.

| Paso | Evidencia que debería quedar en la traza |
| --- | --- |
| Consultar marzo | Período y total 2695 |
| Consultar abril | Período y total 1670 |
| Calcular variación | Fórmula con marzo como referencia |
| Generar gráfico | Valores y unidades coherentes |
| Responder | Comparación con límites del conjunto de datos |

## Código: tests que comprueban un contrato

Un agente escribe una función `variacion(actual, base)`. El contrato puede exigir devolver una fracción, no el porcentaje ya multiplicado por cien. Para `actual=80` y `base=100`, la salida esperada es `-0.2`.

```python
def variacion(actual, base):
    if base == 0:
        raise ValueError("La referencia no puede ser cero")
    return (actual - base) / base

assert variacion(80, 100) == -0.2
assert variacion(100, 100) == 0
assert variacion(150, 100) == 0.5
```

La igualdad se aplica aquí a valores simples; en cálculos más generales conviene comparar con una tolerancia numérica. También se debe comprobar la referencia cero y acordar cómo manejarla. Un único test de descenso no cubre igualdad, aumento o errores.

**Determinista** significa que la misma entrada y condiciones producen el mismo resultado. Un test determinista puede estar mal diseñado o no cubrir el defecto. `run_python_code` es una capacidad de ejecución; el permiso para archivos, red o procesos requiere otros controles.

## Investigación: una cita que realmente sostenga la frase

La tarea es «explica qué cambió en esta revisión de MCP». El agente recupera documentos, identifica pasajes relevantes y redacta. La evidencia debe conectar cada afirmación material con una fuente y una revisión concreta.

Una cita válida exige más que un enlace existente. Si el informe afirma que desapareció `initialize`, el fragmento debe describir ese cambio. Si afirma adopción universal, una especificación no sirve para probarla. Un recurso recuperado puede ser anterior a la revisión; su fecha y alcance importan.

| Afirmación | Evidencia apropiada | Evidencia insuficiente |
| --- | --- | --- |
| Cambió el saludo inicial | Changelog de la revisión pertinente | Tutorial sin fecha |
| El total cayó 38,03 % | Datos y cuenta con denominador correcto | Un gráfico sin valores |
| La implementación cumple su contrato | Tests y criterios de aceptación | Código que solo ejecuta sin excepción |

## Reflexion depende de feedback útil

**Reflexion** incorpora evaluación y lecciones entre intentos. Un fallo verificable permite una crítica concreta: «usaste abril como denominador; utiliza marzo». Un «parece incorrecto» aporta menos información y puede conducir a cambios inútiles.

La diapositiva 23 afirma que el caso con verificador determinista es el único donde Reflexion «rinde de verdad». Esa frase es demasiado general: la sesión 12 ya mostró resultados que dependen de la tarea y del evaluador. Se conserva la conclusión sustentable: **feedback fiable facilita mejoras; el beneficio debe comprobarse en la tarea**. También pueden existir verificadores deterministas para cálculos del analista o para integridad de citas, y tests incompletos para código.

> [!question]- ¿MCP decide si un agente de investigación utilizó una cita que apoya su conclusión?
> No. Comunica operaciones y resultados. La comprobación del vínculo entre afirmación y evidencia pertenece al evaluador o a la aplicación.

Fuente de clase: PDF 23 · numeración visible igual a la página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-13.pdf#page=23|Sesión 13]].

La cuenta, el código, las tablas y los ejemplos de verificación son propios. Los totales de ventas se reutilizan como datos didácticos de las notas de sesiones 11–12; no se presentan como una medición nueva de S13.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/90 S13 - Confianza permisos costo y límites|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/92 S13 - Laboratorio local de descubrimiento y extensión B|Siguiente]] →
