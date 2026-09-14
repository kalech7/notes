---
title: "06 S01 - Modelos discriminativos y generativos"
tags:
  - maestria/ia-generativa
  - estudio
---

# 06 S01 - Modelos discriminativos y generativos

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-01.pdf#page=3|Sesión 01, páginas 3–7]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción.

## Dos preguntas diferentes sobre los mismos datos

Supón que quieres trabajar con correos. Un enfoque **discriminativo** aprende a decidir la clase del correo. Un enfoque **generativo** modela cómo podrían distribuirse los datos, eventualmente junto con una clase.

En clasificación generativa:

$$P(X,Y)=P(Y)P(X\mid Y).$$

Después se aplica Bayes para obtener $P(Y\mid X)$. Por eso un modelo generativo también puede clasificar. «Generativo» no significa que su única utilidad sea producir texto o imágenes.

En clasificación discriminativa probabilística se aprende directamente $P(Y\mid X)$. Esto evita modelar toda la distribución de las entradas si la tarea consiste únicamente en decidir una etiqueta.

## Las tres posibilidades de Bishop

| Enfoque | Qué aprende | Ejemplo |
| --- | --- | --- |
| Generativo | Conjunta o distribución de entradas | Naive Bayes, GMM |
| Discriminativo probabilístico | Posterior de la clase | Regresión logística |
| Función discriminante | Puntaje o etiqueta sin probabilidades obligatorias | SVM |

Una SVM estándar entrega una función de decisión; no debe interpretarse automáticamente su puntaje como probabilidad. En clase, las dos últimas filas se agrupan bajo «discriminativo».

El nombre «regresión logística» puede confundir: se usa para clasificación probabilística. En el caso binario, transforma un puntaje mediante la función logística para producir un valor entre 0 y 1.

## Cómo genera un modelo de clasificación generativo

Primero puede sortear una clase con $P(Y)$. Después sortea una entrada usando $P(X\mid Y)$. Si eliges tú la clase, realizas generación condicionada.

Que el modelo permita muestrear no implica que las muestras sean realistas. Un Naive Bayes de palabras puede producir una bolsa de términos típicos del spam y no una frase gramatical. La calidad depende de los supuestos y de lo que se aprendió.

También existen modelos generativos condicionales que producen datos dada una entrada. Por tanto, ver una expresión $P(Y\mid X)$ aislada no basta para clasificar cualquier sistema: hay que preguntar qué representa Y. En las diapositivas de clasificación, Y es una etiqueta; en otros problemas podría ser un texto completo.

## ¿BERT para sentimiento es discriminativo?

El BERT afinado para clasificar sentimiento descrito en la sesión se usa para estimar etiquetas a partir de texto. Esa tarea es discriminativa. Compartir la familia transformer con GPT no cambia el objetivo del sistema.

Esto no significa que todas las posibles aplicaciones de una arquitectura sean iguales. Debemos distinguir arquitectura, objetivo de entrenamiento y tarea de uso.

## Pocos datos y muchos datos: una comparación con condiciones

El artículo de Ng y Jordan incluido en las fuentes compara Naive Bayes y su contraparte discriminativa, regresión logística, bajo condiciones específicas. Muestra que un modelo generativo puede acercarse rápidamente a su error límite, mientras el discriminativo puede necesitar más datos y alcanzar un límite mejor.

La intuición es una compensación: supuestos fuertes simplifican la estimación, pero pueden imponer un sesgo que persiste aun con muchos datos. Una familia menos restrictiva puede requerir más evidencia para ajustarse bien.

> [!note] Cómo interpretar la diapositiva 7
> Las tasas de crecimiento logarítmico y lineal se refieren al análisis y supuestos de ese trabajo. No constituyen una regla universal de que «con pocos datos siempre gana cualquier generativo» o «con muchos siempre gana cualquier discriminativo». El cruce puede ocurrir; hay que evaluar el problema concreto.

## De características manuales a representaciones aprendidas

La sesión recorre reglas simbólicas, aprendizaje estadístico, redes profundas, atención y transformers. El cambio central es que se aprende cada vez más de la representación útil para la tarea.

Las RNN procesan secuencias manteniendo un estado que depende del anterior. La atención permite consultar distintas posiciones; los transformers eliminan la recurrencia de su arquitectura básica y facilitan procesar posiciones en paralelo durante entrenamiento. La generación autorregresiva sigue produciendo nuevos tokens en pasos sucesivos.

Un **modelo fundacional** es un modelo preentrenado a escala que sirve de base para distintas tareas. Es una categoría de alcance y reutilización; no todos los modelos fundacionales se definen exclusivamente por ser generativos autorregresivos.

**Lectura de apoyo consultada:** [[ng-jordan-2001-discriminative-vs-generative.pdf|Ng y Jordan, introducción y planteamiento de la comparación]].

## Complemento del libro: predecir una probabilidad y decidir una acción

Bishop separa **inferencia** y **decisión**. Primero estimas una probabilidad; después eliges una acción teniendo en cuenta el costo de equivocarte.

Ejemplo propio: el modelo asigna 0.7 a spam. Supón que enviar un correo normal a spam cuesta 10 unidades y dejar un spam en la bandeja cuesta 1. Si lo envías a spam, el costo esperado es $0.3\times10=3$. Si lo dejas, es $0.7\times1=0.7$. Con estos costos y probabilidades, conviene dejarlo aunque spam sea la clase más probable.

Elegir siempre la clase más probable corresponde al caso particular de errores con igual costo y aciertos sin costo. Si cambian los costos, puedes cambiar la decisión sin volver a entrenar un modelo que ya proporciona probabilidades adecuadas.

También puedes reservar una acción «revisar» para casos inciertos, si el costo de revisión y el objetivo de uso lo justifican. Un puntaje de clasificación sin interpretación probabilística no permite hacer estos cálculos directamente.

**Fuente:** [[bishop-2006-prml.pdf#page=64|Bishop, §1.5.4, pp. impresas 44–45; PDF 64–65]]. Valores y escenario creados para explicar la separación.

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- Si un modelo clasifica spam, ¿necesariamente es discriminativo?
> No. Naive Bayes aprende una distribución generativa y obtiene la posterior de clase mediante Bayes. Hay que mirar qué modela y cómo se ajusta.

> [!question]- ¿Por qué el BERT de sentimiento del ejemplo es discriminativo?
> Porque el sistema se ajusta para predecir una etiqueta de sentimiento dada una entrada. La arquitectura compartida con otros modelos no determina por sí sola la tarea.

> [!question]- ¿Un generativo tiene que producir muestras de buena calidad?
> No. Puede definir un procedimiento válido de muestreo y producir muestras pobres porque sus supuestos simplifican demasiado los datos.

> [!question]- ¿El resultado de Ng y Jordan demuestra que todo generativo gana con pocos datos?
> No. Es una comparación bajo condiciones concretas. Sirve para entender regímenes posibles, no para decidir sin evaluar.


> [!question]- Si spam tiene probabilidad 0.7, ¿siempre conviene enviarlo a spam?
> No. Con costo 10 por bloquear un correo normal y costo 1 por dejar spam, los costos esperados son 3 y 0.7. Con esos supuestos conviene dejarlo.
