---
title: "04 S00 - Correlación causalidad y límites de las predicciones"
tags:
  - maestria/ia-generativa
  - estudio
---

# 04 S00 - Correlación causalidad y límites de las predicciones

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-00.pdf#page=14|Sesión 00, páginas 14–15]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción.

## Predecir una asociación no equivale a explicar una causa

Supón que en tus datos los días con más helados vendidos también tienen más personas nadando. ¿Vender helados hace que la gente nade? Puede existir una tercera variable: el calor aumenta ambas cosas.

Una asociación indica que observar una variable aporta información sobre otra. La causalidad pregunta qué cambiaría si modificáramos una variable mediante una intervención.

## Tres explicaciones compatibles con una asociación

Si $X$ y $Y$ están asociados, podrían existir estructuras como:

- $X\rightarrow Y$: X influye en Y.
- $Y\rightarrow X$: la dirección es inversa.
- $X\leftarrow Z\rightarrow Y$: una causa común influye en ambas.

La correlación por sí sola no elige entre estas explicaciones. Se necesitan supuestos, conocimiento del problema o diseños de estudio capaces de identificar el efecto.

> [!note] Matiz respecto de la diapositiva
> La frase «A causa B o B causa A, y no las dos a la vez» no es una definición general de causalidad. Puede existir retroalimentación a lo largo del tiempo. Los grafos dirigidos acíclicos excluyen ciclos por su estructura; eso no significa que todo sistema real carezca de retroalimentación.

## Observar y actuar son preguntas diferentes

$P(Y\mid X=x)$ pregunta por Y entre los casos donde observamos X con valor x.

$P(Y\mid\operatorname{do}(X=x))$ pregunta por Y al fijar X mediante una intervención. En un grafo causal, esa intervención sustituye el mecanismo que normalmente determina X y elimina sus flechas entrantes.

En el ejemplo del calor, aumentar artificialmente las ventas de helados no aumenta necesariamente la temperatura ni la cantidad de personas que nadan. La asociación observada no basta para predecir el efecto de esa acción.

## Qué significa esto para un modelo predictivo

Un modelo podría aprender que cierta palabra identifica spam porque aparece mucho en los datos. Si los remitentes cambian de vocabulario, ese patrón puede dejar de servir. Se llama cambio de distribución cuando cambian las condiciones estadísticas relevantes entre entrenamiento y uso.

Tampoco hay garantía de acierto aunque no haya un cambio: puede haber ruido, datos insuficientes o errores del modelo. Lo correcto es decir que las asociaciones aprendidas pueden perder utilidad cuando cambian las condiciones, no que un mundo estable garantice aciertos.

## Qué significa para un modelo de lenguaje

Un modelo puede redactar una explicación causal plausible porque aprendió patrones de lenguaje y conocimiento descrito en textos. Esa capacidad no verifica el efecto causal específico de una intervención real.

Si un sistema propone «haz X para mejorar Y», conviene distinguir entre una hipótesis razonable, evidencia observacional y evidencia de intervención. La calidad de la redacción no reemplaza esa evaluación.

## Una forma de recordar la sesión 00

El recorrido comienza con mecanismos y pruebas de comportamiento, pasa a modelos escritos o aprendidos y termina con una limitación: calcular una predicción útil no resuelve automáticamente la pregunta por las causas. Para entender cómo se calculan las predicciones de la sesión 01, sigue con [[05 S01 - Probabilidad y teorema de Bayes paso a paso]].

## Complemento del libro: atención causal no significa inferencia causal

Cuando estudies transformers aparecerá otra vez la palabra **causal**, pero con una función distinta. Raschka llama atención causal al mecanismo que impide que una posición consulte tokens futuros mientras predice el siguiente token.

Con la entrada «yo estudio Bayes», la posición de «yo» no puede consultar «estudio» para predecirlo. La máscara evita revelar la respuesta durante el entrenamiento. Restringe el flujo de información de la secuencia.

Esto no calcula $P(Y\mid\operatorname{do}(X))$ ni identifica qué intervención produce un efecto. El nombre compartido no convierte una red con máscara en un modelo causal del mundo. Puedes recordar la diferencia como **restricción temporal de lectura** frente a **pregunta sobre el efecto de actuar**.

**Fuente de la máscara:** [[Build_a_Large_Language_Model_From_Scrat.pdf#page=97|Raschka, §3.5.1, p. impresa 75; PDF 97]]. La comparación con la causalidad de la sesión 00 es una conexión didáctica.

## Gráficos y diagramas para entender el tema

### Comparar observación e intervención

![Comparar observación e intervención](<Recursos visuales/10-causalidad.png>)

**Cómo leerlo:** A la izquierda el calor influye en ventas y natación. A la derecha fijamos las ventas externamente y retiramos su flecha entrante. En este ejemplo no hay una flecha de ventas a natación: la asociación se explica por el calor. El dibujo representa un supuesto causal explícito, no una estructura descubierta solo por correlación.

*Figuras originales elaboradas para estos apuntes. Los números y supuestos se explican en el texto; no son imágenes copiadas de los libros.*

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
