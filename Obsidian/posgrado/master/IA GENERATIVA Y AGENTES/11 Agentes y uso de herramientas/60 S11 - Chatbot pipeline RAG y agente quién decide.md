---
title: "60 S11 - Chatbot pipeline RAG y agente quién decide"
sesion: "11"
fecha: 2026-09-28
tags:
  - maestria/ia-generativa
  - agentes
  - herramientas
fuente: "[[sesion-11.pdf]]"
---

# 60 S11 - Chatbot pipeline RAG y agente quién decide

[[59 S11 - Guía para entender agentes y herramientas|Guía de la sesión 11]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[59 S11 - Guía para entender agentes y herramientas]]

Siguiente: [[61 S11 - PEAS racionalidad y observación parcial]]

## 1. Empieza por observar quién controla el recorrido

**Chatbot simple:** recibe texto y produce texto. Puede explicar una fórmula o redactar una respuesta. No tiene, en este ejemplo, un ejecutor de herramientas.

**Pipeline o cadena:** tu código establece una secuencia, por ejemplo extraer una pregunta, buscar documentos y resumirlos. Cada etapa puede usar un modelo. El hecho de que sus salidas sean variables no cambia quién fijó el recorrido.

**Agente de esta sesión:** el modelo elige una acción a partir de lo observado; el sistema la ejecuta y vuelve a pedir una decisión. Tiene una meta y condiciones de salida.

| Caso | Quién decide el flujo | Clasificación útil |
| --- | --- | --- |
| Cinco prompts ejecutados siempre en el mismo orden | El programa | Pipeline. |
| RAG que siempre recupera y después genera | El programa | Pipeline RAG. |
| Menú de veinte funciones, pero solo se llama siempre a la primera | El programa | Tener herramientas no basta. |
| Modelo elige buscar, observa resultados, reformula o termina | El modelo dentro de límites del programa | Agente según el criterio operativo del curso. |
| Modelo selecciona una ruta una sola vez, sin retorno | Modelo para el enrutamiento; programa para el resto | Enrutador dinámico; todavía no muestra el bucle de la definición. |

## 2. Las cuatro condiciones de la definición del curso

El PDF, pp. 4–6, exige elegir **qué herramienta**, **cuándo**, **en bucle** y **hacia un objetivo**.

**Qué.** La elección debe tener alternativas relevantes. Ante una solicitud de ventas, el sistema podría consultar datos, buscar una definición o responder si ya tiene evidencia suficiente. No basta con imprimir un nombre de herramienta que el programa ignora.

**Cuándo.** La herramienta debe poder ser necesaria en una situación y prescindible en otra. Si cada consulta pasa obligatoriamente por el buscador, el modelo no decide si buscar.

**En bucle.** El resultado de la acción vuelve a alimentar una nueva decisión. Repetir una función cinco veces por un `for` fijo tampoco demuestra autonomía: lo relevante es que la nueva observación pueda cambiar la acción siguiente.

**Hacia un objetivo.** No se trata de producir actividad. El agente debe reconocer cuándo tiene suficiente información para completar la tarea, cuándo debe pedir un dato y cuándo debe parar sin éxito.

> [!important] Definición operativa, no ley universal
> En IA clásica, «agente» es más amplio: incluye sistemas reactivos sin LLM. Aquí usamos la definición del curso para distinguir arquitecturas de aplicaciones con LLM. Una herramienta única tampoco excluye toda decisión: se puede decidir si usarla, con qué argumentos, repetirla o terminar. La frase del PDF «una sola acción posible» describe una ausencia real de alternativas, no simplemente contar funciones.

## 3. El paso de RAG a herramienta

Antes:

```text
pregunta → recuperar siempre → construir contexto → generar
```

Después:

```text
pregunta → decidir
           ├─ buscar_documentos → resultado → decidir otra vez
           ├─ total_ventas      → resultado → decidir otra vez
           ├─ calcular          → resultado → decidir otra vez
           └─ responder o pedir información
```

En ambos sistemas, `buscar_documentos` puede usar exactamente el mismo índice, embeddings y reranker. Cambia **quién decide llamarlo** y **qué hace después con lo obtenido**.

La respuesta B de la pregunta de la p. 6 identifica el cambio decisivo: recuperar se vuelve opcional y seleccionable. Para que se cumpla además la definición completa de la p. 4, se necesita integrar esa elección en el bucle con objetivo y salida.

Una variante encapsula un RAG completo como `responder_con_documentos`. Otra devuelve únicamente fragmentos para que el agente sintetice. La primera oculta parte del trabajo y puede duplicar generación; la segunda hace visible la evidencia pero consume más contexto. En ambas conviene devolver referencias y límites de la búsqueda.

## 4. Arquitectura y ejecución concreta son dos cosas

Una arquitectura puede admitir iteraciones y, para una pregunta sencilla, terminar sin herramientas. No deja de admitir comportamiento de agente porque una ejecución particular haya sido corta.

A la inversa, una traza larga no demuestra autonomía. Un pipeline con treinta pasos fijos sigue teniendo el flujo predefinido. Para clasificarlo pregunta: **si cambia el resultado de una herramienta, ¿el modelo puede elegir una acción distinta?**

Ejemplo: el buscador devuelve cero fragmentos. Un agente puede ampliar términos, pedir un identificador o abstenerse. Un pipeline podría tener también esas ramas, pero gobernadas por reglas explícitas. Los sistemas híbridos combinan ambos: un flujo exterior fijo puede contener un paso con un bucle de agente.

## 5. Cuándo aporta algo esa decisión dinámica

Si todos los usuarios piden el mismo cálculo con los mismos campos, un procedimiento explícito puede resolverlo con menos variabilidad. La decisión dinámica aporta cuando el camino depende de información que se descubre durante la ejecución: qué documento existe, qué campo falta o qué prueba falla.

Esto no demuestra que un agente sea siempre más lento o que un pipeline sea siempre mejor. Da una hipótesis de diseño: comparar éxito, costo y fallos en tareas reales. La autonomía añade posibilidades y también más lugares donde equivocarse.

## 6. «Agentic AI» y las cuatro capas

La p. 25 plantea una taxonomía de divulgación, no una frontera técnica certificada. No existe en el material una línea de código que convierta automáticamente «agente» en «Agentic AI».

Una empresa puede usar esa etiqueta para sistemas con planificación larga, varias herramientas o coordinación. Sin una definición explícita no se puede deducir una arquitectura de la palabra. Describe lo observable: acciones disponibles, quién las selecciona, qué estado se conserva, cómo se evalúa y cuándo se detiene.

Un chatbot con un prompt largo no adquiere herramientas, memoria persistente o un bucle de ejecución por la longitud del texto. Debemos inspeccionar sus capacidades reales.

## Comprobación rápida

**¿Agregar una segunda herramienta convierte un RAG en agente?** No: puede seguir ejecutando ambas en orden fijo. **¿Un agente necesita mostrar un razonamiento largo?** No: necesita un mecanismo de decisión y ejecución; la longitud de la explicación no es el criterio.

**Fuente:** [[sesion-11.pdf#page=2|pp. 2–6 y 25–26]]. Precisión sobre arquitectura frente a corrida y sistemas híbridos: ampliación pedagógica. *Hands-On LLMs*, p. impresa 218 (PDF 240), compara acciones elegidas por el sistema con cadenas predefinidas.
