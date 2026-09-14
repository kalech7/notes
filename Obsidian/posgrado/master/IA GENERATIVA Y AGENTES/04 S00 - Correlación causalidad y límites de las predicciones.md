---
title: "04 S00 - Correlación causalidad y límites de las predicciones"
tags:
  - maestria/ia-generativa
  - estudio
---

# 04 S00 - Correlación causalidad y límites de las predicciones

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. Dos cosas pueden cambiar juntas sin causarse entre sí

Supón que los días con más ventas de helados también hay más personas nadando. Es tentador concluir que vender helados provoca que la gente nade.

Pero existe otra explicación: **el calor aumenta ambas cosas**. La venta de helados ayuda a predecir cuánta gente habrá nadando, aunque no sea la causa de esa actividad.

Cuando dos variables aportan información una sobre otra hablamos de asociación. Cuando preguntamos qué cambiaría al intervenir sobre una de ellas, estamos haciendo una pregunta causal.

## 2. Lee el diagrama como una hipótesis sobre el mundo

![Observar e intervenir](<Recursos visuales/10-causalidad.png>)

A la izquierda, el calor tiene una flecha hacia las ventas y otra hacia la natación. El diagrama dice que el calor influye en ambas. No tiene una flecha de ventas a natación.

A la derecha fijamos las ventas mediante una acción externa. Por ejemplo, hacemos una promoción que cambia cuántos helados se venden. Retiramos la flecha que normalmente determinaba esa variable, pero no cambiamos el calor. Según esta hipótesis, tampoco cambia la natación por esa ruta.

El dibujo no demuestra que el mundo funcione así. Expresa un supuesto causal que necesitaría justificarse.

## 3. Qué significan las dos probabilidades

$P(Y\mid X=x)$ significa: «entre los casos en los que observamos X con ese valor, ¿cómo se comporta Y?». Por ejemplo, mirar días con muchas ventas y contar nadadores.

$P(Y\mid\operatorname{do}(X=x))$ significa: «si fijamos X mediante una intervención, ¿cómo se comporta Y?». Por ejemplo, cambiar las ventas por una acción y estudiar su efecto.

La palabra **do** señala esa intervención. Observar un grupo de casos y cambiar el mecanismo que produce una variable no son el mismo procedimiento.

## 4. Qué otras explicaciones puede tener una asociación

Si X e Y cambian juntas, X podría influir en Y, Y podría influir en X o una tercera variable podría influir en ambas. Una correlación por sí sola no decide cuál explicación es correcta.

También puede existir retroalimentación a lo largo del tiempo. Los grafos dirigidos acíclicos excluyen ciclos por cómo están definidos; eso no significa que ningún sistema real pueda tener efectos recíprocos.

## 5. Qué implica para la IA

Un clasificador de spam puede aprender que cierta palabra es una pista útil. Si cambian los mensajes, esa pista puede dejar de servir. Aprender una asociación no explica automáticamente qué ocurrirá cuando alguien actúe para modificar la situación.

Del mismo modo, un modelo de lenguaje puede redactar una explicación convincente sin haber verificado la causa que describe. Debes separar lo plausible de lo demostrado con datos y supuestos apropiados.

## 6. Una palabra que puede confundirte después

En transformers encontrarás **atención causal**. Allí significa impedir que una posición consulte tokens futuros mientras predice. Por ejemplo, al predecir la palabra que sigue a «yo», el modelo no debe mirar esa respuesta más adelante en la frase.

Esa máscara controla qué partes del texto puede leer. No demuestra causas del mundo ni calcula por sí sola efectos de intervenciones. Recuerda esta diferencia cuando llegues a los modelos de lenguaje.

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-00.pdf#page=14|Sesión 00, páginas 14–15]]
- [[Build_a_Large_Language_Model_From_Scrat.pdf#page=97|Raschka, §3.5.1, p. impresa 75; PDF 97]]

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Por qué helados y natación pueden estar asociados sin causarse entre sí?
> Porque una causa común, como el calor, puede aumentar ambos. La asociación no identifica automáticamente una flecha causal directa.

> [!question]- ¿Cuál es la diferencia entre observar X y hacer do(X)?
> Observar selecciona casos donde X ocurre; intervenir fija X sustituyendo su mecanismo habitual. Las distribuciones resultantes pueden ser distintas.

> [!question]- ¿Una explicación causal bien redactada prueba una causa?
> No. La redacción puede ser plausible sin que exista evidencia suficiente. Deben examinarse los supuestos y el diseño que permiten identificar el efecto.

> [!question]- ¿Toda causalidad excluye retroalimentación?
> No. Puede haber efectos recíprocos a lo largo del tiempo. La ausencia de ciclos es una restricción de un tipo de representación, no una ley universal del mundo.


> [!question]- ¿Una máscara causal permite concluir que X causa Y en el mundo?
> No. Impide consultar posiciones futuras del texto; no identifica efectos de intervenciones.
