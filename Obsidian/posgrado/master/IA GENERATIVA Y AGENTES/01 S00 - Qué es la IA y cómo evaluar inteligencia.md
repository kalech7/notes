---
title: "01 S00 - Qué es la IA y cómo evaluar inteligencia"
tags:
  - maestria/ia-generativa
  - estudio
---

# 01 S00 - Qué es la IA y cómo evaluar inteligencia

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. Empecemos con una pregunta concreta

Imagina que te ofrecen una aplicación que «entiende tus apuntes». ¿Cómo comprobarías esa afirmación? Podrías darle una nota que nunca haya visto, hacerle preguntas y verificar si responde correctamente usando el contenido.

Este ejemplo muestra el primer problema de la inteligencia artificial: **decir que un sistema es inteligente no explica qué sabe hacer ni cómo vamos a evaluarlo**.

La inteligencia artificial, o IA, estudia cómo construir sistemas que realizan tareas como reconocer imágenes, utilizar lenguaje, aprender de ejemplos y resolver problemas. Para estudiar una capacidad concreta, debemos convertirla en una prueba.

## 2. Qué significa evaluar una capacidad

Una prueba necesita una tarea, unas condiciones y una forma de medir el resultado. Por ejemplo:

- **Tarea:** responder preguntas sobre un documento.
- **Condición:** el documento no formó parte de los ejemplos de evaluación usados al desarrollar el sistema.
- **Medida:** cuántas respuestas son correctas y están respaldadas por el documento.

A esta manera de convertir una idea en algo comprobable se le llama **definición operativa**. No tienes que memorizar el nombre: recuerda que pasamos de «parece que entiende» a «vamos a comprobar si puede hacer esto».

La medida también debe tener sentido. Si 990 de 1 000 correos son normales, un programa que siempre diga «normal» obtiene 99 % de aciertos. Sin embargo, no identifica ninguno de los 10 spam. El porcentaje es verdadero, pero no demuestra que el programa detecte spam.

## 3. Una máquina automática no necesariamente aprende

Un reloj puede funcionar sin intervención humana continua y no aprender nada. Ejecuta un mecanismo. Un sistema que aprende, en cambio, modifica alguna parte de su comportamiento a partir de datos o experiencia.

La sesión presenta ejemplos históricos para distinguir estas ideas. Talos representa la imaginación de una máquina autónoma, pero pertenece al mito. Antikythera era un dispositivo real para cálculos astronómicos. Los autómatas de Jaquet-Droz ejecutaban movimientos mediante un mecanismo. El Turco mecánico aparentaba jugar ajedrez automáticamente, pero ocultaba a una persona.

El punto de estos ejemplos es preguntar **qué produce el resultado**. Dos demostraciones parecidas pueden funcionar de maneras muy distintas. Después, las computadoras programables permitieron cambiar de tarea sin construir una máquina completamente nueva para cada problema.

## 4. Qué propuso Turing

En la versión de la prueba explicada en clase, una persona conversa por texto con interlocutores que no puede ver y trata de identificar cuál es una máquina.

La idea importante es que Turing propuso un procedimiento observable. En vez de resolver primero qué significa «pensar», planteó una situación que se podía probar.

Esa prueba evalúa cómo se comporta la máquina en una conversación bajo ciertas condiciones. No comprueba automáticamente que tenga conciencia, que diga la verdad o que pueda resolver cualquier tarea.

## 5. Por qué aparece Dartmouth en esta historia

En 1956, la reunión de Dartmouth ayudó a dar nombre y un programa de investigación a la IA. Se propuso estudiar cómo representar capacidades como aprendizaje, lenguaje y abstracción para implementarlas en máquinas.

Era una propuesta de investigación, no una demostración de que todos esos problemas estuvieran resueltos. Esa diferencia sigue siendo útil: resolver una tarea concreta no demuestra una capacidad ilimitada.

**Lo que debes poder explicar al terminar:** cómo distinguir una demostración convincente de una capacidad comprobada. La siguiente nota responde otra pregunta: [[02 S00 - Reglas modelos y aprendizaje desde datos|¿cómo construimos el conocimiento que usa el sistema?]]

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-00.pdf#page=4|Sesión 00, páginas 4–9]]
- [[bishop-2006-prml.pdf#page=65|Bishop, §1.5.4, p. impresa 45; PDF 65]]

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
