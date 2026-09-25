---
title: "46 S09 - Evaluar respuestas fidelidad y citas"
sesion: "09"
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-09.pdf]]"
---

# 46 S09 - Evaluar respuestas fidelidad y citas

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[42 S09 - Guía para evaluar un RAG|Guía de la sesión 09]]

## 1. Recuperación correcta no garantiza generación correcta

Fuente base: [[sesion-09.pdf#page=20|PDF, p. 20]]. Imagina que el contexto dice: «Se requieren 60 créditos. El plazo de solicitud se anunciará posteriormente». El modelo responde: «Necesitas 60 créditos y debes solicitarlo antes del 30 de junio».

La primera afirmación está respaldada y la segunda es inventada respecto al contexto. El sistema pudo recuperar el documento perfecto y aun así producir una respuesta defectuosa. La unidad de análisis cambia: ya no miramos solo documentos recuperados, sino **afirmaciones, evidencia y relación con la pregunta**.

## 2. Qué significa juzgar la respuesta

| Eje | Pregunta que hace el evaluador | Posible error |
| --- | --- | --- |
| Fluidez | ¿Se entiende y está bien redactada? | Texto claro con información falsa. |
| Utilidad percibida | ¿Ayuda al usuario con su necesidad? | Información correcta pero irrelevante o incompleta. |
| Recall de citas | ¿Las afirmaciones que necesitan soporte tienen citas que lo aporten? | Muchas afirmaciones sin respaldo identificable. |
| Precisión de citas | ¿Las citas incluidas sostienen lo que se les atribuye? | Citar un documento relacionado que no prueba la afirmación. |

La denominación «recall de citas» necesita una rúbrica: aquí tomamos como unidad las afirmaciones verificables que requieren respaldo. No es Recall@k, cuyo denominador son unidades relevantes anotadas para recuperar.

## 3. Fidelidad: descomponer antes de contar

Una operacionalización didáctica del concepto de la diapositiva es:

$$Faithfulness=\frac{\text{afirmaciones sustentadas por el contexto}}{\text{afirmaciones evaluadas}}$$

En nuestro ejemplo hay dos afirmaciones y solo una sustentada: 1/2 = 0,5. Para hacer reproducible el juicio debes indicar cómo separas afirmaciones y cómo tratas inferencias, ambigüedades y contradicciones.

![[31-s09-afirmaciones-y-citas.png]]

### Cómo leer el diagrama

El bloque izquierdo muestra la evidencia disponible. Los dos bloques del centro separan las afirmaciones de una única respuesta. La línea verde indica soporte: los 60 créditos aparecen en el contexto. La línea roja indica falta de soporte: el 30 de junio no está establecido.

El bloque derecho resume el conteo: una de dos afirmaciones respaldada. Los colores representan un juicio explícito sobre este ejemplo, no una probabilidad producida por el modelo. Una cita al mismo documento junto a toda la respuesta no transforma la línea roja en verde.

**Fidelidad al contexto no equivale a verdad universal.** Si el documento está desactualizado, una respuesta puede repetirlo fielmente y seguir siendo incorrecta para la situación actual. Por eso importa mantener y fechar el corpus.

## 4. Relevancia de respuesta y relevancia de contexto

Según la formulación histórica de RAGAS que explica el PDF, para estimar relevancia de respuesta se generan preguntas a partir de la respuesta y se compara su similitud con la pregunta original. Intuición: si la respuesta parece contestar otra pregunta, la similitud debería disminuir. Es una aproximación dependiente de modelos; no prueba que la respuesta sea correcta.

La relevancia de contexto se presenta como proporción de oraciones cruciales respecto de las oraciones suministradas. Mide **foco**: cuánto del contexto resulta útil. Si entregas una frase muy pertinente pero omites una segunda condición necesaria, puedes tener contexto enfocado y cobertura insuficiente.

Ejemplo: hacen falta dos reglas; entregas una frase con una de ellas y nada más. Todo el contexto puede ser pertinente, pero solo cubres una de dos evidencias. No sustituyas Recall@k por una medida de foco.

Estas son las definiciones tratadas en la p. 20; no se presentan como documentación de la API actual de una biblioteca ni como una lista de sus capacidades vigentes.

## 5. Citas: dos denominadores distintos

Supón que hay cuatro afirmaciones que necesitan respaldo. Solo dos tienen citas, y una de esas citas realmente sostiene la afirmación a la que está asociada.

Con una rúbrica basada en relaciones afirmación-cita:

- Precisión de citas: una relación válida de dos incluidas = 1/2.
- Cobertura o recall de citas: una afirmación correctamente respaldada de cuatro que lo necesitaban = 1/4.

Tener muchas citas no garantiza precisión. Tener una sola cita perfecta no garantiza cobertura. Si varias afirmaciones comparten una cita, el protocolo debe decidir cómo evaluar cada relación; no basta contar enlaces.

## 6. Qué aporta un LLM juez y qué no resuelve

Un modelo juez puede automatizar parte de la revisión, pero sus salidas dependen del prompt, del contexto disponible y del modelo elegido. La diapositiva menciona sesgos de posición, verbosidad y autopreferencia: por ejemplo, una respuesta más larga puede parecerle mejor aunque añada afirmaciones sin soporte.

Como ampliación metodológica, una evaluación cuidada fija la rúbrica, registra las versiones, presenta la evidencia necesaria y contrasta una muestra de juicios con revisión humana. «Sin referencia» suele significar sin una respuesta ideal previamente redactada; todavía necesitas la pregunta y el contexto para juzgar soporte y relevancia.

Las métricas automáticas sirven para localizar casos a revisar y comparar bajo un protocolo estable. No convierten un juicio semántico en una verdad infalible.

> [!abstract] Para recordar
> Recuperar la fuente, usarla fielmente y citarla correctamente son tres logros relacionados, pero distintos.
