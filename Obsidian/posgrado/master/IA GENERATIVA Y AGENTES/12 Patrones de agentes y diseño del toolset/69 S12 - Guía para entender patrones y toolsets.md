---
title: "69 S12 - Guía para entender patrones y toolsets"
created: 2026-09-29
fecha: 2026-09-29
capitulo: 12
sesion: "12"
tags:
  - maestria/ia-generativa
  - agentes
  - estudio
---

# 69 S12 - Guía para entender patrones y toolsets

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

La sesión 11 explicó **quién decide y quién ejecuta**. La sesión 12 pregunta **cómo organizar las decisiones, cómo detectar fallas y qué contrato necesitan las herramientas**. Entender esto permite construir un sistema que avance con evidencia y que se detenga de forma explicable.

## Un ejemplo que une toda la sesión

Usaremos las ventas ficticias del notebook del lunes. La tarea es: «Compara abril con marzo y explica la variación». Marzo suma 2695 y abril 1670. El cálculo correcto es:

$$\frac{1670-2695}{2695}\times100\approx-38{,}03\%$$

El resultado indica una caída respecto de marzo. No demuestra por qué ocurrió: estas siete filas no contienen una explicación causal. El agente debe obtener las cantidades, comprobar que sean comparables, calcular y redactar con el alcance correcto.

La misma tarea permite entender tres organizaciones:

| Patrón | Dónde organiza las decisiones | Qué haría en el ejemplo |
| --- | --- | --- |
| ReAct | Dentro de un intento, según cada resultado | Pedir marzo, observar; pedir abril, observar; calcular |
| Plan-and-Execute | Un plan antes de ejecutar, con revisión si hace falta | Crear esos pasos y recorrerlos |
| Reflexion | Entre intentos, usando evaluación y lecciones | Reintentar si un verificador detecta una comparación incorrecta |

**ReAct y Reflexion pueden componerse.** El primero organiza una trayectoria; el segundo utiliza su evaluación para cambiar el siguiente intento. Un intento es una corrida para resolver la tarea; un paso es una unidad definida por el programa, que aquí suele ser una decisión del modelo.

## Ruta de estudio

1. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/11 Agentes y uso de herramientas/68 S11 - Notebook del lunes explicado y revisado|68 S11 - Notebook del lunes explicado y revisado]]: mecanismo y cifras del lunes.
2. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/70 S12 - ReAct pensamiento acción observación y evidencia|70 S12 - ReAct pensamiento acción observación y evidencia]]: qué cambia con ReAct y qué probaron sus autores.
3. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/71 S12 - Autopsia de trazas y detector de repetición|71 S12 - Autopsia de trazas y detector de repetición]]: localizar falta de progreso y fabricación.
4. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/72 S12 - Pasos presupuestos timeouts y condiciones de parada|72 S12 - Pasos presupuestos timeouts y condiciones de parada]]: controlar vueltas y consumo.
5. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/73 S12 - Reflexion entre intentos memoria y aprendizaje|73 S12 - Reflexion entre intentos memoria y aprendizaje]]: mejorar mediante retroalimentación.
6. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/74 S12 - Verificadores fiables y errores del notebook|74 S12 - Verificadores fiables y errores del notebook]]: separar salida válida de respuesta correcta.
7. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/75 S12 - Plan-and-Execute y elección de patrones|75 S12 - Plan-and-Execute y elección de patrones]]: planes, replanning y niveles conceptuales.
8. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/76 S12 - Toolsets validación errores y límites efectivos|76 S12 - Toolsets validación errores y límites efectivos]]: hacer que una acción sea ejecutable y controlable.
9. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/77 S12 - Laboratorio local y soluciones del martes|77 S12 - Laboratorio local y soluciones del martes]]: ejemplos ejecutables y resultados comprobados.
10. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/78 S12 - Ejercicios resueltos y repaso activo|78 S12 - Ejercicios resueltos y repaso activo]]: aplicar las ideas sin memorizar nombres.

La primera lectura puede seguir 70 → 71 → 72 → 73 → 74. Después estudia 75 y 76; usa 77 para relacionar las decisiones con código y 78 para comprobar comprensión.

## Preguntas que debes poder responder

- ¿Qué parte de una traza aporta evidencia externa y qué parte es texto producido por el modelo?
- ¿Cómo puede haber una respuesta final incorrecta y también una parada correcta sin resolver la tarea?
- ¿Por qué un detector de repetición no sustituye al máximo de pasos?
- ¿Cómo recibe el intento siguiente la crítica del anterior?
- ¿Qué comprueba exactamente el verificador y qué errores aún puede aceptar?
- ¿Quién impone el máximo de filas o una ruta de escritura permitida?

## Alcance y procedencia

Se revisaron las **25 páginas** de [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-12.pdf|sesion-12.pdf]], *Patrones de agentes y diseño del toolset*, Daniel Andrés Riofrío Almeida, martes 29 de septiembre de 2026; el texto completo y las figuras. La página PDF coincide con la numeración visible 1–25. Se leyeron las 18 celdas del notebook del lunes y las 20 del martes. Las celdas se citan desde 0 para encontrarlas en el archivo JSON.

Los originales están en `Materiales`. Las notas son explicaciones propias, con ocho figuras reproducibles en PNG y SVG, cálculos y respuestas razonadas. Los resultados históricos se comprobaron en apartados seleccionados de las copias locales de [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/fuentes/papers/s3-agentes/yao-2023-react.pdf|yao-2023-react.pdf]] y [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/fuentes/papers/s3-agentes/shinn-2023-reflexion.pdf|shinn-2023-reflexion.pdf]].

Se conservan dos niveles de certeza: los errores de los notebooks se reprodujeron con código aislado; los defectos del **Lab 03** se explican según el PDF, porque sus archivos no forman parte de los tres adjuntos. No se atribuye una inspección propia a las líneas de laboratorio citadas por el docente.

> [!info] Consignas académicas
> Las actividades en grupos, la entrega y el porcentaje de evaluación son contenido de clase. Según la página 25, el Taller 3 se anuncia para el sábado 3 de octubre de 2026 y como 25 % de la nota final; no se infieren pesos de cada criterio. Crear estas notas no entrega el taller ni modifica sus servicios.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/11 Agentes y uso de herramientas/68 S11 - Notebook del lunes explicado y revisado|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/70 S12 - ReAct pensamiento acción observación y evidencia|Siguiente]] →


## Revisión integral de estas dos sesiones

Revisión del 29 de septiembre de 2026: se contrastaron las 51 páginas de las dos sesiones, las 38 celdas de sus notebooks y las 20 notas 59–78. Se revisaron visualmente las 16 figuras 41–56. Se corrigieron contradicciones de alcance, se ampliaron operaciones del ReAct original y lectura de sus métricas, y se mantuvieron separados datos didácticos, resultados históricos y defectos del Lab 03 descritos por el docente. Se consultaron apartados pertinentes de los papers locales; no se afirma lectura íntegra de sus apéndices ni disponibilidad de las sesiones 13–14.
