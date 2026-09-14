---
title: "06 S01 - Modelos discriminativos y generativos"
tags:
  - maestria/ia-generativa
  - estudio
---

# 06 S01 - Modelos discriminativos y generativos

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. Un mismo correo, dos formas de aprender

Quieres decidir si un correo es spam. Un modelo **discriminativo** puede aprender directamente a relacionar las características del mensaje con esa etiqueta.

Un modelo **generativo** puede aprender cómo son los correos de cada clase: qué características aparecen en spam, cuáles en normales y con qué frecuencia ocurre cada clase. Después aplica Bayes para decidir qué clase explica mejor el correo recibido.

Ambos pueden clasificar. La diferencia está en qué aprenden para llegar a la decisión.

## 2. Qué significan X e Y aquí

En esta nota, X representa el correo mediante características y Y representa su etiqueta. Por ejemplo, X puede ser una lista de conteos de palabras e Y puede valer «spam».

El discriminativo probabilístico aprende $P(Y\mid X)$: dada la entrada, qué probabilidad tiene cada etiqueta.

El generativo de clasificación aprende $P(X,Y)=P(Y)P(X\mid Y)$: cómo se distribuyen las clases y cómo son los datos de cada una. Después obtiene $P(Y\mid X)$ con Bayes.

No clasifiques un sistema solo por ver una fórmula condicional. En otros problemas Y podría ser un texto completo por generar, en lugar de una etiqueta. Aquí estamos comparando enfoques de **clasificación**.

## 3. Las tres opciones que explica Bishop

| Opción | Qué entrega o aprende | Ejemplo |
| --- | --- | --- |
| Generativa | Modelo de datos y clases | Naive Bayes |
| Discriminativa probabilística | Probabilidades de etiquetas dada la entrada | Regresión logística |
| Función de decisión | Puntaje o etiqueta, sin probabilidades obligatorias | SVM |

En clase se agrupan las dos últimas como discriminativas. Una SVM no entrega automáticamente una probabilidad: su puntaje necesita una interpretación adecuada.

Un BERT ajustado para sentimiento realiza una tarea discriminativa porque predice etiquetas a partir del texto. Compartir el tipo de arquitectura transformer con GPT no hace idénticos sus objetivos.

## 4. Por qué el enfoque generativo también puede crear datos

Si aprendiste cómo se distribuyen los datos de cada clase, puedes elegir primero una clase y después sortear un dato compatible con ella.

Por ejemplo: eliges spam y sorteas palabras según sus frecuencias en spam. Eso puede producir «oferta premio oferta». El procedimiento genera datos, pero no garantiza una oración gramatical. La calidad depende de las relaciones que el modelo representa.

## 5. ¿Cuál enfoque es mejor?

Depende del problema. Un modelo que hace supuestos fuertes puede necesitar menos datos para ajustarse, pero esos supuestos pueden limitar su resultado. Otro más flexible puede necesitar más ejemplos.

Ng y Jordan estudian esta diferencia comparando Naive Bayes y regresión logística bajo condiciones concretas. Encontraron situaciones con dos regímenes: uno puede rendir mejor con pocos datos y el otro con más. No es una ley de que cualquier generativo siempre gane con pocos ejemplos.

## 6. La etiqueta más probable no siempre dicta la acción

Supón que el modelo asigna 0.7 a spam y 0.3 a normal. Si bloquear un normal cuesta 10 unidades y dejar pasar un spam cuesta 1:

- Bloquear tiene costo esperado $0.3\times10=3$.
- Dejar pasar tiene costo esperado $0.7\times1=0.7$.

Con esos costos, dejarlo tiene menor costo esperado. El modelo no cambió de opinión sobre la clase: cambiaron las consecuencias que consideramos al decidir.

Esto explica por qué separar **probabilidad** y **acción** es útil. Elegir la clase más probable es apropiado para ciertos costos, no para todos.

## 7. Cómo conecta con los modelos de lenguaje

El recorrido de reglas a aprendizaje profundo también cambió la representación de los datos. Antes era habitual diseñar características a mano; una red puede aprender representaciones útiles. Las RNN procesan secuencias mediante un estado que se actualiza paso a paso. La atención permite combinar información de distintas posiciones y los transformers facilitan cálculos por posiciones durante entrenamiento.

Un modelo fundacional es un modelo preentrenado que puede servir de base para distintas tareas. No todos se describen exclusivamente como generadores autorregresivos. En este curso nos centraremos especialmente en esa forma de generar lenguaje.

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-01.pdf#page=3|Sesión 01, páginas 3–7]]
- [[ng-jordan-2001-discriminative-vs-generative.pdf|Ng y Jordan, introducción y planteamiento de la comparación]]
- [[bishop-2006-prml.pdf#page=64|Bishop, §1.5.4, pp. impresas 44–45; PDF 64–65]]

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
