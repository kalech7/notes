---
title: "13 PRÁCTICA - Repaso integrado y ejercicios resueltos"
tags:
  - maestria/ia-generativa
  - estudio
---

# 13 PRÁCTICA - Repaso integrado y ejercicios resueltos

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** sesiones 00 y 01, especialmente [[sesion-01.pdf#page=19|Sesión 01, páginas 19–20]]. Ejercicios propios para estudiar. No es el notebook oficial mencionado en las diapositivas.

## Cómo practicar

Primero explica el concepto con tus palabras, luego calcula sin mirar y por último abre la respuesta. Si aciertas por intuición pero no sabes justificarlo, vuelve a la nota correspondiente.

Estas actividades convierten el temario en situaciones concretas. El ZIP contiene libros y artículos; no incluye el notebook original citado por las diapositivas. Por eso los ejercicios de esta nota son una adaptación didáctica, no una entrega resuelta del curso.

## Ejercicio 1: identificar el enfoque

Clasifica tres sistemas: A usa reglas explícitas para decidir requisitos; B aprende directamente probabilidades de clase; C aprende probabilidades de palabras por clase y luego aplica Bayes. Explica de dónde viene su conocimiento.

## Ejercicio 2: Bayes con una tasa base diferente

En un conjunto, el 10 % de los correos es spam. «Premio» aparece en el 80 % de los spam y en el 20 % de los normales. Calcula la probabilidad de spam cuando aparece «premio». Escribe prior, verosimilitud y evidencia.

## Ejercicio 3: generar desde una distribución

Un modelo condicionado en spam da 0.5 a `oferta`, 0.3 a `premio` y 0.2 a `hoy`. En 1 000 extracciones, ¿qué conteos esperas? ¿Deben salir exactamente? ¿Hay alguna garantía de gramática?

## Ejercicio 4: responsabilidades de una mezcla

Dos componentes tienen pesos 0.25 y 0.75. Sus densidades en un punto son 0.4 y 0.2. Calcula las responsabilidades y explica por qué el componente de mayor densidad no necesariamente tiene la mayor responsabilidad.

## Ejercicio 5: tabla de bigramas

Considera las oraciones `yo estudio ia`, `yo estudio bayes` y `yo aprendo ia`. Cuenta continuaciones de `yo` y de `estudio`. Explica cómo generarías una nueva secuencia y qué harías al terminar.

## Ejercicio 6: leer una fórmula

Explica, sin leer símbolo por símbolo, qué quiere decir:

$$P(x_1,\ldots,x_n)=\prod_{t=1}^{n}P(x_t\mid x_{<t}).$$

Después indica qué modifica un bigrama y qué conserva un LLM autorregresivo.

## Ejercicio 7: usar un modelo o actuar con él

Un asistente escribe una explicación, otro recupera un PDF antes de responder y un tercero consulta documentos, ejecuta un cálculo y revisa el resultado. Identifica las capacidades añadidas, sin asumir que todos esos sistemas son igual de fiables.

## Ejercicio 8: detectar afirmaciones demasiado fuertes

Revisa: «EM siempre encuentra el mejor modelo», «un HMM solo usa la última observación», «los VAE no pueden generar texto», «una respuesta fluida prueba comprensión» y «muchos datos garantizan que cualquier discriminativo gane».

## Autoevaluación sugerida

Asigna 0 puntos si no sabes responder, 1 si recuerdas el término pero no lo justificas y 2 si explicas el mecanismo o cálculo. Con 8 ejercicios hay 16 puntos posibles. Es una guía personal, no la rúbrica del profesor.

Más útil que el total es detectar dónde fallas: si confundes condicionales, vuelve a Bayes; si confundes estados y observaciones, vuelve a HMM; si confundes pesos y latentes, revisa GMM y VAE.

## Segunda ronda: aplicar los complementos de los libros

**Ejercicio 9.** Un clasificador dice que un correo es spam con probabilidad 0.8. Bloquear un normal cuesta 6 y dejar un spam cuesta 1. Calcula el costo esperado de cada acción.

**Ejercicio 10.** Con prior Beta(1,1), observas dos caras y dos cruces. Calcula posterior y predicción de cara.

**Ejercicio 11.** Para un componente GMM, dos puntos 2 y 8 tienen responsabilidades 0.75 y 0.25. Calcula su nueva media.

**Ejercicio 12.** Un modelo de lenguaje asigna 0.5 al objetivo en dos posiciones. Calcula pérdida promedio con logaritmo natural y perplejidad.

Estas cuatro actividades suman hasta 8 puntos adicionales si usas la escala anterior. El bloque original conserva su máximo de 16; ambos juntos dan 24.

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- Respuesta 1: ¿qué tipo es cada sistema?
> A es simbólico: usa reglas expresadas por personas. B es discriminativo probabilístico. C es un clasificador generativo como Naive Bayes: modela datos por clase y calcula la posterior con Bayes.

> [!question]- Respuesta 2: ¿cuál es la posterior de spam?
> Prior 0.1; verosimilitud 0.8; evidencia 0.8×0.1+0.2×0.9=0.26. Posterior 0.08/0.26=4/13≈30.77 %. Una palabra frecuente en spam no elimina la importancia de la tasa base.

> [!question]- Respuesta 3: ¿qué conteos se esperan?
> 500, 300 y 200 en promedio. Los conteos concretos fluctúan por azar. Muestrear palabras independientemente no garantiza gramática ni coherencia.

> [!question]- Respuesta 4: ¿cuáles son las responsabilidades?
> Contribuciones: 0.25×0.4=0.1 y 0.75×0.2=0.15. Normalizadas: 0.4 y 0.6. La responsabilidad combina densidad y peso previo, no solo densidad.

> [!question]- Respuesta 5: ¿cómo queda la tabla?
> Después de «yo»: estudio 2/3 y aprendo 1/3. Después de «estudio»: ia 1/2 y bayes 1/2. Se muestrea una continuación y se repite; con marcadores se detiene en fin, o se aplica una regla de parada explícita.

> [!question]- Respuesta 6: ¿qué expresa la factorización?
> La probabilidad de una secuencia se obtiene multiplicando probabilidades sucesivas condicionadas en el pasado. El bigrama restringe el contexto a un elemento; un LLM autorregresivo aprende factores con una red usando el prefijo disponible.

> [!question]- Respuesta 7: ¿qué capacidades aparecen?
> El primero genera lenguaje; el segundo añade recuperación documental, propia de RAG; el tercero incorpora un ciclo de herramientas y observación compatible con un agente. Cada resultado sigue necesitando evaluación.

> [!question]- Respuesta 8: ¿qué hay que corregir?
> EM puede quedar en máximos locales. El HMM conserva información del historial en su distribución de estados. Existen VAE para texto, con dificultades. Fluidez no prueba comprensión general. La comparación de tamaños de muestra depende de supuestos, familias y datos.


> [!question]- Respuesta 9: ¿cuál es la acción de menor costo esperado?
> Bloquear cuesta 0.2×6=1.2; dejar cuesta 0.8×1=0.8. Con esos costos conviene dejarlo.

> [!question]- Respuesta 10: ¿qué posterior y predicción obtienes?
> Beta(3,3); la predicción de cara es 3/6=0.5.

> [!question]- Respuesta 11: ¿cuánto vale la media ponderada?
> (0.75×2+0.25×8)/(0.75+0.25)=3.5.

> [!question]- Respuesta 12: ¿qué pérdida y perplejidad obtienes?
> La pérdida promedio es −ln(0.5)=ln(2)≈0.6931 y la perplejidad es 2.
