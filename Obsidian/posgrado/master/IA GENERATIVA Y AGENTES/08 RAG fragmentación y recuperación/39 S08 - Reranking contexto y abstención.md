---
title: "39 S08 - Reranking contexto y abstención"
sesion: "08"
tags:
  - maestria/ia-generativa
  - rag
  - estudio
fuente: "[[sesion-08.pdf]]"
---

# 39 S08 - Reranking contexto y abstención

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[34 S08 - Guía para entender fragmentación y recuperación|Guía de la sesión 08]]

## 1. El problema después de encontrar candidatos

Un buscador debe explorar un corpus potencialmente grande. Necesita ser eficiente, por lo que utiliza representaciones y estructuras que permiten seleccionar candidatos sin leer cada pareja pregunta-fragmento con un modelo complejo.

Pero encontrar candidatos plausibles y determinar cuáles responden mejor no son exactamente el mismo trabajo. La recuperación en dos etapas separa esas tareas: una etapa amplia y rápida, seguida de un examen más detallado de una lista corta.

## 2. Qué es reranking y cómo funciona

El **reranking** asigna nuevos puntajes a candidatos ya recuperados y cambia su orden. Un **cross-encoder** puede realizar ese trabajo al procesar conjuntamente la pregunta y cada fragmento. Eso permite representar interacciones entre ambos textos dentro del modelo.

En un **bi-encoder**, cada fragmento obtiene su representación independientemente de la pregunta concreta; después se comparan los vectores. En un cross-encoder, el resultado depende de la pareja y debe calcularse cuando se conoce la consulta. Esa dependencia explica tanto su posible ventaja como su costo.

La frase «la primera etapa no lee la pregunta» de la página 23 simplifica demasiado: el recuperador sí usa la pregunta. Lo que no hace el bi-encoder es volver a codificar cada fragmento junto con ella.

![Recuperación amplia y selección detallada](<../Recursos visuales/24-s08-dos-etapas.png>)

El gráfico es un esquema del flujo propuesto en el PDF: recuperar 20 candidatos, puntuar 20 parejas y seleccionar 5 fragmentos. Esos números ilustran la arquitectura; no son parámetros óptimos demostrados para cualquier corpus.

### Por qué leer juntos pregunta y pasaje cambia la representación

En un bi-encoder, el vector del fragmento debe servir para muchas preguntas futuras. En el cross-encoder típico basado en un transformer bidireccional, los tokens de la pregunta y del pasaje se procesan en una entrada conjunta. La atención puede relacionar tokens de ambos: la representación que se usa para puntuar el pasaje depende de la pregunta que lo acompaña.

El entrenamiento enseña a producir una señal de relevancia para la pareja. El sistema usa ese puntaje para ordenar; no necesita que el modelo redacte una explicación o una respuesta. Esa diferencia funcional evita confundir un reordenador con el LLM generador.

La interacción conjunta puede ayudar a distinguir detalles que una comparación de dos resúmenes vectoriales pierde. Pero la arquitectura por sí sola no garantiza mejorar: también importan el objetivo de entrenamiento, el idioma, el dominio y la entrada que realmente procesa.

El reranker tiene además su **propio límite de entrada**. La pregunta, los separadores y el pasaje deben caber juntos. Si el fragmento cabía en el modelo de embeddings pero se recorta en el reordenador, reaparece el problema de evidencia no observada. Tener tres modelos en el flujo puede implicar tres tokenizadores y presupuestos distintos.

## 3. Por qué el reranker tiene un techo

El reordenador solo evalúa los candidatos que recibe. Si la evidencia correcta no está entre los 20, no puede inventar un puesto para ella. Por eso, antes de culpar al reranker, debemos inspeccionar la lista inicial.

A tamaño de lista y longitudes comparables, se evalúan 20 pares tanto si el corpus tiene miles como millones de fragmentos. Eso no significa que el costo total de búsqueda sea independiente del corpus. Tampoco significa necesariamente 20 llamadas de red: los pares pueden procesarse por lotes.

El puntaje del cross-encoder depende de su entrenamiento y de cómo se transforme su salida. Algunos modelos devuelven valores entre 0 y 1; otros logits o escalas distintas. Incluso un valor entre 0 y 1 no es automáticamente una probabilidad calibrada de que el fragmento contenga una respuesta correcta.

## 4. Por qué más contexto puede perjudicar

Aumentar el número de fragmentos eleva la posibilidad de incluir evidencia, pero también puede añadir redundancia, ruido, documentos desactualizados y afirmaciones en conflicto. El modelo debe resolver esas relaciones dentro de un presupuesto limitado.

**Lost in the middle** describe una dificultad observada en ciertos escenarios: la información relevante ubicada en medio de contextos largos puede utilizarse peor que la situada cerca de los extremos. No significa que todo modelo ignore siempre el centro. La consecuencia práctica es considerar selección y orden, además de longitud.

Conviene distinguir tres cantidades: candidatos recuperados, candidatos examinados por el reordenador y fragmentos enviados al generador. Pueden tener valores diferentes. Subir la primera cantidad no obliga a enviar todo al prompt.

Cambiar top-k normalmente no exige reconstruir el índice ni entrenar. Sin embargo, puede aumentar el trabajo de búsqueda, transferencia, reranking y generación. La expresión del PDF «gratis para el índice» debe entenderse como ausencia de reindexación, no como ausencia total de costo.

## 5. Qué debe hacer el contexto

El contexto debe conservar el contenido que sustenta la respuesta y permitir identificar su procedencia. Antes de enviarlo, conviene eliminar duplicación innecesaria y mantener juntos encabezados o condiciones que determinan el significado. El orden puede reflejar relevancia, estructura documental o vigencia, según la tarea.

No basta con agregar muchos fragmentos. Debemos poder responder: ¿qué aporta cada uno?, ¿de qué documento y versión viene?, ¿qué afirmación podría respaldar? Esto conecta la preparación de documentos con la calidad final de la respuesta.

### Construir el contexto es seleccionar información bajo un presupuesto

Supongamos que $W$ es el presupuesto conjunto disponible en una configuración del generador. Si $I$ corresponde a instrucciones, $Q$ a pregunta, $H$ a historial, $D$ a documentos y $O$ a salida reservada, una comprobación simplificada es:

$$I+Q+H+D+O\leq W.$$

Todas esas cantidades deben medirse con el tokenizador del generador e incluir los delimitadores o metadatos pertinentes. Si la API distingue límites de entrada y salida, se deben respetar además por separado; esta desigualdad sirve como explicación del reparto, no como especificación universal de una API.

Un top-5 de fragmentos cortos y un top-5 de secciones largas no cuestan lo mismo. Por eso, elegir el número de fragmentos no sustituye calcular el volumen real. Tampoco basta con rellenar hasta el límite: puede ser preferible un contexto menor que conserve todas las condiciones necesarias.

La selección no siempre consiste en tomar los mejores pasajes individualmente. Una pregunta puede requerir información complementaria de varias secciones. Cinco pasajes muy parecidos pueden ser menos suficientes que tres que cubran partes diferentes de la respuesta. Aquí la pregunta central pasa de «¿qué fragmento puntúa más?» a «¿qué conjunto de fragmentos permite sostener una respuesta completa?».

### Citar exige mantener la relación entre afirmación y evidencia

El identificador `[3]` en una respuesta solo es útil si podemos resolverlo al tercer pasaje suministrado y después a su documento, ubicación y versión. Esa cadena permite revisar la afirmación sin buscar otra vez a ciegas.

Una cita que menciona el mismo tema puede no respaldar la conclusión. Para verificarla hay que comprobar que el pasaje mantiene el sujeto, alcance, condiciones y vigencia de lo afirmado. Si la respuesta combina varias fuentes, debe quedar claro qué sostiene cada una y qué parte es una inferencia.

## 6. El prompt: instrucciones, evidencia y abstención

La página 27 propone delimitar el contexto, pedir una respuesta basada en él, citar fragmentos y permitir la abstención. Estas decisiones cumplen funciones distintas:

| Elemento | Por qué está ahí |
| --- | --- |
| Contexto delimitado | Distingue la fuente consultada de las instrucciones de la tarea |
| Regla de fundamentación | Pide que las afirmaciones dependan de evidencia disponible |
| Referencias a fragmentos | Permite revisar el sustento de cada afirmación |
| Abstención explícita | Hace válida la respuesta cuando falta evidencia suficiente |

Las etiquetas ayudan a expresar la separación, pero no son una garantía técnica de obediencia. Del mismo modo, escribir «solo con el contexto» no obliga matemáticamente al modelo a cumplir. La respuesta debe comprobarse contra las fuentes.

La frase del curso es: **«El corpus no contiene informacion suficiente.»** Se conserva aquí como contenido docente. Una limitación lógica es que fallar al recuperar no demuestra que el corpus entero carezca de la información. Fuera de ese formato de evaluación, decir «No tengo evidencia suficiente en los fragmentos recuperados» describe con más precisión lo observado.

Abstenerse no debe equivaler a rendirse siempre: es reconocer una insuficiencia de evidencia concreta. Si la respuesta existe pero no llegó al contexto, la abstención puede ser prudente para el generador y, al mismo tiempo, revelar un fallo del recuperador.

> [!abstract] Para recordar
> **Recuperar encuentra candidatos; reordenar prioriza; construir contexto decide qué ve el modelo; generar redacta.** Cada paso resuelve un problema distinto.

> [!question] Comprueba que lo entendiste
> ¿Puede un generador actuar correctamente y aun así fallar el sistema?
>
> Sí. Puede abstenerse correctamente al no recibir evidencia, aunque esa evidencia exista en un documento que el recuperador no encontró.

**Lectura complementaria consultada:** [[Hands-On_Large_Language_Models.pdf#page=266|cap. 8, p. impresa 244 (PDF 266)]], sobre procesamiento conjunto; y [[Hands-On_Large_Language_Models.pdf#page=274|p. impresa 252 (PDF 274)]], sobre fuentes asociadas a afirmaciones. La explicación de presupuestos es una ampliación propia.

**Fuente:** [[sesion-08.pdf#page=23|páginas 23–24 y 26–27]]. Continúa con [[40 S08 - Diagnóstico de fallos y decisiones del taller]].
