---
title: "59 S11 - Guía para entender agentes y herramientas"
created: 2026-09-28
capitulo: 11
sesion: "11"
fecha: 2026-09-28
tags:
  - maestria/ia-generativa
  - agentes
  - herramientas
fuente: "[[sesion-11.pdf]]"
---

# 59 S11 - Guía para entender agentes y herramientas

[[59 S11 - Guía para entender agentes y herramientas|Guía de la sesión 11]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Siguiente: [[60 S11 - Chatbot pipeline RAG y agente quién decide]]

## La idea que organiza la sesión

Hasta la sesión 10 construiste un sistema que recibía una pregunta, recuperaba documentos y generaba una respuesta. El recorrido estaba determinado de antemano. La sesión 11 añade una pregunta: **¿quién decide cuál debe ser el siguiente paso cuando todavía no conocemos la solución?**

En el agente estudiado aquí, un LLM propone la próxima acción a partir del objetivo y las observaciones disponibles. Un programa comprueba esa propuesta, ejecuta la herramienta y devuelve el resultado al modelo. Entonces hay otra decisión. Ese ciclo continúa hasta responder o alcanzar una condición de parada.

La unidad que llamamos agente es el sistema completo: **modelo + herramientas + código de ejecución + estado + reglas de parada**. El modelo aislado no consulta una base de datos ni mueve archivos.

![[41-s11-quien-decide.png]]

En la segunda fila, las flechas definen un recorrido fijo. En la tercera aparece una flecha de retorno: lo que la herramienta devuelve cambia la información disponible para la siguiente decisión. La flecha de salida recuerda que repetir no es un objetivo en sí mismo.

## Un caso concreto que seguiremos

Imagina un asistente de una empresa ficticia. La pregunta es: **«¿Cuánto crecieron las ventas de marzo respecto de febrero de 2026 y qué significa el resultado?»**

Tenemos tres herramientas didácticas:

| Herramienta | Qué aporta | Cuándo hace falta |
| --- | --- | --- |
| `total_ventas(mes)` | Un total del mes con moneda y fuente | Faltan las cifras. |
| `variacion_porcentual(base, actual)` | El porcentaje de cambio | Ya hay dos cantidades comparables. |
| `buscar_documentos(consulta)` | Fragmentos de las reglas del negocio | No sabemos qué se incluye en «ventas». |

Los datos inventados son febrero = 12 000 USD y marzo = 15 000 USD. La variación es 25 %. Si ambos datos ya vienen en la pregunta, quizá no necesite consultar la base. Si «ventas» puede significar facturación bruta o neta, debe aclararlo o consultar las reglas antes de calcular. Si febrero vale cero, la fórmula habitual no produce un porcentaje definido.

**Ese cambio de conducta según lo observado es el centro del tema.** Todos los datos empresariales de estas notas son ficticios; no representan tu información ni resultados del laboratorio del curso.

## Ruta de estudio

| Nota | Qué aprenderás a explicar |
| --- | --- |
| [[60 S11 - Chatbot pipeline RAG y agente quién decide]] | Por qué el número de prompts o herramientas no define a un agente. |
| [[61 S11 - PEAS racionalidad y observación parcial]] | Cómo especificar éxito, entorno, sensores y actuadores. |
| [[62 S11 - Function calling y bucle del agente paso a paso]] | Quién emite, quién ejecuta y cómo vuelve el resultado. |
| [[63 S11 - Diseñar herramientas esquemas y validación]] | Cómo hacer que una herramienta sea seleccionable y comprobable. |
| [[64 S11 - Memoria contexto y costo de repetir el historial]] | Dónde vive la memoria y por qué el contexto crece. |
| [[65 S11 - Toolformer aprendizaje resultados y límites]] | Cómo aprender a llamar APIs difiere de controlar un bucle. |
| [[66 S11 - Límites trazas y laboratorio del bucle]] | Cómo detener, observar y depurar el sistema. |
| [[67 S11 - Ejercicios resueltos y repaso activo]] | Si puedes aplicar las ideas a casos nuevos. |

**Primera lectura:** 60 → 62 → 63 → 66. Te da el mecanismo concreto. **Segunda lectura:** 61 → 64 → 65. Añade fundamentos, restricciones y antecedentes. Finalmente resuelve 67 sin desplegar las soluciones.

## Cinco frases que debes poder justificar

1. Una descripción de herramienta informa al modelo; no ejecuta la función.
2. Una llamada necesita un resultado asociado, incluso cuando la operación falla.
3. La respuesta final expresa que el modelo terminó; un evaluador todavía debe comprobar si resolvió la tarea.
4. El historial útil debe conservarse fuera de los pesos y suministrarse a la siguiente decisión.
5. Poder usar herramientas, tener autonomía y resolver bien una tarea son propiedades diferentes.

## Cómo se enlaza con lo anterior

El RAG de [[51 S10 - Del documento a una respuesta con evidencia]] puede convertirse en una herramienta del nuevo sistema. Su recuperación sigue necesitando un índice correcto y sus respuestas siguen necesitando evidencia. Añadir un agente **no arregla automáticamente** los fallos de ingesta, recuperación o fidelidad.

Los esquemas conectan con [[25 S04 - Salidas estructuradas costo y razonamiento interno]]. Toolformer conecta con [[21 S03 - Preentrenamiento autosupervisado y MLE]]: utiliza la pérdida del siguiente token para escoger datos de ajuste fino. La diferencia entre memoria en contexto y parámetros retoma [[35 S08 - RAG contexto memoria y generación fundamentada]].

## Fuente, ampliaciones y límites

Fuente principal: [[sesion-11.pdf]], *Qué es un agente y uso de herramientas*, Daniel Andrés Riofrío Almeida, 28 de septiembre de 2026, 26 páginas. Se revisaron texto y figuras. Las páginas 1, 3, 7, 12 y 18 son portada o separadores.

Las notas distinguen tres niveles: **contenido del PDF**, **precisiones conceptuales** y **ejemplos propios**. Los pasajes pertinentes del artículo local [[schick-2023-toolformer.pdf]] y del libro [[Hands-On_Large_Language_Models.pdf]] se consultaron directamente. Los archivos del curso que aparecen en los pies de las diapositivas no se consideran inspeccionados.

Las ocho figuras 41–48 son recursos propios en PNG y SVG. Sus cifras son didácticas, salvo la comparación histórica de Toolformer, cuya fuente se indica. El laboratorio es una simulación nueva del protocolo y no una ejecución del notebook docente.

> [!info] Instrucciones dentro del material
> «Discutan», «corrijan el Lab 03», las fechas, porcentajes y consignas son contenido académico del PDF. Estas notas los explican cuando corresponde; no autorizan instalar servicios, modificar el laboratorio del curso ni entregar trabajos.

## Notebook del lunes y continuidad

Ahora está incorporado [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/11 Agentes y uso de herramientas/68 S11 - Notebook del lunes explicado y revisado|Notebook del lunes explicado y revisado]], con los datos originales, las llamadas explicadas y la incompatibilidad de mensajes reproducida. Continúa con [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]] para estudiar cómo organizar y proteger las decisiones.

## Revisión integral de estas dos sesiones

Revisión del 29 de septiembre de 2026: se contrastaron las 51 páginas de las dos sesiones, las 38 celdas de sus notebooks y las 20 notas 59–78. Se revisaron visualmente las 16 figuras 41–56. Se corrigieron contradicciones de alcance, se ampliaron operaciones del ReAct original y lectura de sus métricas, y se mantuvieron separados datos didácticos, resultados históricos y defectos del Lab 03 descritos por el docente. Se consultaron apartados pertinentes de los papers locales; no se afirma lectura íntegra de sus apéndices ni disponibilidad de las sesiones 13–14.
