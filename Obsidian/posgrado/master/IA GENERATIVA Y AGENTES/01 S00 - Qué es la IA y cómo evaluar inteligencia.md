---
title: "01 S00 - Qué es la IA y cómo evaluar inteligencia"
tags:
  - maestria/ia-generativa
  - estudio
---

# 01 S00 - Qué es la IA y cómo evaluar inteligencia

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-00.pdf#page=4|Sesión 00, páginas 4–9]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción.

## Qué debes comprender

La pregunta «¿una máquina es inteligente?» necesita un criterio de evaluación. Una definición abstracta puede orientar la conversación, pero para experimentar debemos decidir qué tarea hará el sistema, bajo qué condiciones y cómo mediremos su desempeño.

**Inteligencia artificial (IA)** es el campo que estudia y construye sistemas capaces de realizar tareas asociadas con capacidades inteligentes: reconocer patrones, utilizar lenguaje, planificar o resolver problemas. Esa descripción no establece por sí sola una prueba universal de inteligencia.

### De una palabra amplia a una prueba concreta

Imagina que alguien afirma: «Mi sistema entiende documentos». Para evaluarlo, convierte esa frase en preguntas observables: ¿identifica la idea principal?, ¿responde con información del documento?, ¿reconoce que falta una respuesta?, ¿funciona con documentos que no vio durante el entrenamiento?

Un ejemplo de criterio sería evaluar 50 preguntas nuevas con una rúbrica de exactitud y respaldo documental. Ese número es un ejemplo de diseño, no una exigencia del curso. La idea es medir algo definido, en lugar de aceptar una demostración convincente como prueba suficiente.

## Antes de la disciplina: mito, mecanismo y apariencia

La sesión usa a Talos como ejemplo de una idea antigua de autonomía. Es un personaje mítico; sirve para mostrar una aspiración humana, no como evidencia de tecnología real. El mecanismo de Antikythera representa otro caso: un dispositivo físico que realizaba cálculos astronómicos. Automatizar un cálculo no implica aprender de ejemplos.

El contraste entre el **Turco mecánico**, que ocultaba a una persona, y los autómatas de **Jaquet-Droz**, cuyo mecanismo ejecutaba movimientos, deja una pregunta vigente: ¿qué produce realmente la respuesta que vemos?

Hay tres niveles que conviene separar:

| Nivel | Pregunta | Ejemplo |
| --- | --- | --- |
| Comportamiento | ¿Qué resultado produce? | Escribe una frase |
| Mecanismo | ¿Cómo se obtiene? | Levas, programa o red neuronal |
| Aprendizaje | ¿Qué cambia gracias a los datos? | Se ajustan los pesos |

Una máquina puede funcionar automáticamente sin aprender. Y un resultado que parece automático puede tener intervención humana. Para comprender un sistema debemos examinar tanto sus resultados como su funcionamiento.

## La importancia de poder programar

La transición hacia computadoras programables hizo posible expresar una tarea de una forma separable de la máquina que la ejecuta. Esto permite reutilizar un mismo equipo para problemas diferentes, aunque la facilidad de reprogramación varió mucho entre las primeras computadoras.

Piensa en una calculadora especializada frente a una computadora en la que ejecutas hoy un editor y mañana un clasificador. Lo decisivo para este tema es la flexibilidad de la tarea, no memorizar el peso o la superficie de máquinas históricas.

## Turing: hacer comprobable una pregunta

En 1950, Turing propuso el juego de imitación. En la versión simplificada presentada en clase, una persona conversa por texto con interlocutores ocultos y debe distinguir a una máquina de una persona.

La aportación es **operacionalizar**: sustituir una pregunta difícil de delimitar por un procedimiento observable. Se controla el canal de comunicación para que la apariencia física no determine el juicio.

La prueba estudia la capacidad de imitar una conversación humana bajo determinadas condiciones. No demuestra por sí sola conciencia, veracidad, comprensión de todos los dominios o capacidad de actuar competentemente en el mundo. También depende de quién evalúa, cuánto dura la conversación y qué preguntas se permiten.

## Dartmouth: un programa de investigación

La reunión de Dartmouth de 1956 dio nombre y un programa de trabajo a la IA. La propuesta vinculaba lenguaje, aprendizaje, abstracción, redes neuronales y creatividad con la posibilidad de construir máquinas.

Una **conjetura** es una idea que orienta la investigación; no es un resultado demostrado. Que una máquina resuelva una tarea concreta no demuestra automáticamente que todos los aspectos de la inteligencia sean simulables de la misma manera.

### Conexión con la IA generativa

Un texto fluido puede impresionar igual que una demostración de un autómata. Para estudiarlo bien, pregunta qué aprende el modelo, cómo genera y cómo se verifica lo que afirma. Esas preguntas llevan a [[02 S00 - Reglas modelos y aprendizaje desde datos]].

## Complemento del libro: una métrica puede engañarte

Bishop explica que la proporción de clases afecta a la evaluación. Adaptemos la idea a correos: si 990 de 1 000 son normales, un sistema que siempre diga «normal» logra 99 % de aciertos, pero detecta cero de los 10 spam. El cálculo es correcto; la conclusión «detecta bien spam» sería incorrecta.

Para tu criterio operativo, especifica qué error quieres detectar. **Exactitud global** pregunta qué proporción de decisiones acertó. **Sensibilidad de spam** pregunta cuántos spam reales encontró. Una prueba útil compara además el sistema con una alternativa simple, como predecir siempre la clase mayoritaria.

La lección conecta con Turing: elegir un procedimiento observable es necesario, pero también hay que justificar que ese procedimiento mide la capacidad que nos importa. Un número alto sin contexto no lo demuestra.

**Fuente del complemento:** [[bishop-2006-prml.pdf#page=65|Bishop, §1.5.4, p. impresa 45; PDF 65]]. Ejemplo de correos elaborado para estas notas.

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Qué significa convertir una definición en un criterio operativo?
> Definir un procedimiento observable de evaluación: tarea, condiciones y medidas. «Entiende» es ambiguo; responder preguntas nuevas con exactitud verificable es evaluable.

> [!question]- ¿Un mecanismo automático aprende necesariamente?
> No. Puede ejecutar un programa fijo sin modificar nada a partir de ejemplos. Aprender exige algún ajuste basado en datos o experiencia.

> [!question]- ¿Qué enseña el contraste entre el Turco y Jaquet-Droz?
> Que resultados parecidos pueden proceder de mecanismos distintos. Hay que distinguir la apariencia de automatización de cómo se produce realmente el resultado.

> [!question]- ¿Superar una conversación tipo Turing demuestra que todo lo dicho es verdadero?
> No. Evalúa indistinguibilidad conversacional bajo unas condiciones; no constituye una garantía de verdad ni de competencia universal.


> [!question]- ¿Puede un 99 % de aciertos ocultar que no se detecta ningún spam?
> Sí. Si el 99 % de los correos es normal, predecir siempre normal obtiene esa exactitud y sensibilidad de spam igual a cero.
