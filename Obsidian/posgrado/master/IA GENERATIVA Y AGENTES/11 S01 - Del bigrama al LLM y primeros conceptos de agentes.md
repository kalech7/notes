---
title: "11 S01 - Del bigrama al LLM y primeros conceptos de agentes"
tags:
  - maestria/ia-generativa
  - estudio
---

# 11 S01 - Del bigrama al LLM y primeros conceptos de agentes

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-01.pdf#page=18|Sesión 01, páginas 18–20]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción. El apartado de agentes es una orientación adicional basada en el glosario; estas sesiones todavía no desarrollan el tema.

## Lo que se conserva al pasar al LLM

Un modelo grande de lenguaje, **LLM**, de tipo autorregresivo aprende una distribución del próximo token dado el prefijo:

$$P_\theta(x_1,\ldots,x_n)=\prod_{t=1}^{n}P_\theta(x_t\mid x_{<t}).$$

Es la misma regla del producto estudiada antes. Lo que cambia frente al bigrama es cómo se calcula cada distribución y cuánto contexto puede utilizar.

## Qué le falta al bigrama del ejercicio

| Aspecto | Bigrama por conteo | LLM autorregresivo tipo GPT |
| --- | --- | --- |
| Contexto | Un elemento anterior | Prefijo disponible dentro de su contexto |
| Representación | Identidades y conteos | Representaciones vectoriales aprendidas |
| Parámetros | Filas de una tabla | Pesos compartidos de una red |
| Relaciones | Frecuencias locales | Patrones aprendidos entre posiciones |
| Escala | Corpus de juguete | Preentrenamiento de gran escala |

Tres diferencias suficientes para explicar el salto son contexto más amplio, representaciones aprendidas y una red con parámetros compartidos. Tener más datos ayuda, pero una tabla de bigramas no se convierte en transformer solo por crecer.

La expresión «GPT de contexto 1» de la actividad es una analogía para el muestreo secuencial, no una equivalencia de arquitecturas.

## Un token no equivale a una palabra

Un token es una unidad del vocabulario del modelo. Puede corresponder a una palabra, una parte, un signo u otra unidad según el tokenizador.

Separar una oración con `split()` por espacios sirve en un ejercicio introductorio, pero no reproduce necesariamente la tokenización de un LLM. No conviene deducir el número exacto de tokens a partir del número de palabras.

## Entrenar y generar hacen cosas distintas

Durante preentrenamiento autorregresivo se ajustan los pesos para asignar alta probabilidad a los tokens observados según su contexto. La pérdida habitual es una suma o promedio de log-probabilidades negativas.

Durante generación se calcula una distribución y se elige un token. Después ese token pasa a formar parte del prefijo y se repite el proceso. Elegir siempre el más probable se llama decodificación greedy; muestrear permite elegir otras opciones según sus probabilidades.

Ejemplo inventado: tras «estudio», el modelo asigna 0.5 a «Bayes», 0.3 a «IA» y 0.2 a «probabilidad». Greedy elige «Bayes». Un muestreo podría elegir cualquiera de las tres, con esas frecuencias a largo plazo. Producir opciones variadas no garantiza mejores respuestas.

## Por qué un texto probable puede ser falso

El objetivo de predecir texto no es idéntico a verificar cada afirmación en el mundo. Los datos pueden contener errores, faltar información o mezclar contextos. Un modelo puede construir una continuación plausible que no tenga respaldo.

La probabilidad de un token tampoco es directamente la probabilidad de que una afirmación completa sea verdadera. Para estudiar, contrasta definiciones y cálculos con las fuentes y verifica los resultados.

## Orientación: modelo, RAG y agente

Estos conceptos aparecerán más adelante. Aquí basta con ubicarlos:

- **Modelo de lenguaje:** componente que procesa lenguaje y produce salidas.
- **RAG, recuperación aumentada con generación:** recuperar documentos relevantes y proporcionarlos como contexto para generar una respuesta respaldada en esas fuentes.
- **Agente:** sistema que usa un modelo dentro de un proceso de selección de acciones, uso de herramientas y observación de resultados para avanzar hacia una tarea.

Ejemplo educativo: responder qué es Bayes con información del entrenamiento usa el modelo; buscar el apartado en tus apuntes y contestar con esa evidencia añade recuperación; planificar una búsqueda, ejecutar una calculadora y revisar si se resolvió la tarea introduce un ciclo de acciones.

Un agente no es necesariamente otro modelo más grande. Importa el sistema que lo rodea: herramientas, estado, permisos y criterio de parada. También debe distinguir instrucciones del usuario de texto encontrado en documentos, que puede contener instrucciones ajenas a la tarea.

Esta orientación no sustituye apuntes detallados de las futuras sesiones de agentes: el material principal aportado aquí corresponde al preámbulo y a Bayes/modelos generativos.

## Complemento de los libros: cómo el texto se vuelve aprendizaje

*Hands-On Large Language Models* distingue el vector de entrada de un token y la representación que resulta de procesarlo en contexto. El primero se busca en una tabla aprendida; la segunda depende también de lo que lo rodea.

Ejemplo propio: «banco» en «me senté en el banco» y «deposité dinero en el banco» puede partir del mismo vector de token, si el tokenizador lo representa con el mismo identificador. Después de procesar contexto, sus representaciones pueden diferir. No significa que los pesos se entrenen de nuevo con cada frase: cambian las activaciones.

Raschka explica además que el texto trae sus propios objetivos. Para `[yo, estudio, Bayes, hoy]`, una entrada puede ser `[yo, estudio, Bayes]` y los objetivos `[estudio, Bayes, hoy]`. No se necesita que una persona etiquete manualmente el próximo token de cada posición.

La pérdida penaliza asignar poca probabilidad al token realmente observado. Así se conecta la máxima verosimilitud de Bayes con el entrenamiento de un LLM. El preentrenamiento enseña patrones de continuación; aprender a seguir instrucciones requiere una adaptación del comportamiento y datos apropiados.

Para ver este recorrido con tablas y un cálculo de pérdida, sigue con [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]].

**Fuentes:** [[Hands-On_Large_Language_Models.pdf#page=48|Alammar y Grootendorst, p. impresa 26; PDF 48]] y [[Hands-On_Large_Language_Models.pdf#page=79|pp. 57–59; PDF 79–81]]; [[Build_a_Large_Language_Model_From_Scrat.pdf#page=59|Raschka, §2.6, pp. 37–38; PDF 59–60]] y [[Build_a_Large_Language_Model_From_Scrat.pdf#page=159|§5.1, pp. 137–139; PDF 159–161]].

## Gráficos y diagramas para entender el tema

### Seguir una vuelta de generación

![Seguir una vuelta de generación](<Recursos visuales/08-llm-ciclo.png>)

**Cómo leerlo:** El contexto se tokeniza, se representa con vectores y se procesa para obtener probabilidades del siguiente token. Después de elegirlo, se añade al contexto. Esa realimentación modifica la entrada, no los pesos en inferencia ordinaria. El dibujo omite detalles internos del transformer para resaltar el ciclo.

*Figuras originales elaboradas para estos apuntes. Los números y supuestos se explican en el texto; no son imágenes copiadas de los libros.*

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Qué tres cosas le faltan al bigrama para acercarse a un GPT?
> Contexto más amplio, representaciones aprendidas y una red que comparta parámetros entre contextos. También importan arquitectura y escala de entrenamiento.

> [!question]- ¿Cada token es una palabra?
> No. Depende del vocabulario y del tokenizador; una palabra puede dividirse en varias unidades.

> [!question]- ¿Generar normalmente actualiza los pesos?
> No. Se usan los pesos entrenados para calcular distribuciones; cambian el prefijo y las activaciones.

> [!question]- ¿Una continuación muy probable está necesariamente verificada?
> No. Probabilidad de texto y verdad de una afirmación son conceptos distintos.

> [!question]- ¿Qué diferencia básica hay entre RAG y un agente?
> RAG incorpora recuperación de información al proceso de respuesta. Un agente incorpora un ciclo de decisiones y acciones con herramientas y observaciones. Pueden combinarse.


> [!question]- ¿Por qué una palabra puede tener representaciones diferentes sin reentrenar?
> Porque el contexto cambia las activaciones internas. La tabla de entrada y los demás pesos pueden permanecer fijos.

> [!question]- ¿De dónde salen los objetivos del preentrenamiento autorregresivo?
> Del propio texto: el objetivo de cada posición es el siguiente token observado.
