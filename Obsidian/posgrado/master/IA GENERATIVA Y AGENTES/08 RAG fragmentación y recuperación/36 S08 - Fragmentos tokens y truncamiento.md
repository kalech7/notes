---
title: "36 S08 - Fragmentos tokens y truncamiento"
sesion: "08"
tags:
  - maestria/ia-generativa
  - rag
  - estudio
fuente: "[[sesion-08.pdf]]"
---

# 36 S08 - Fragmentos tokens y truncamiento

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[34 S08 - Guía para entender fragmentación y recuperación|Guía de la sesión 08]]

## 1. Por qué dividir un documento

Un documento puede contener varios temas, condiciones y excepciones. Si calculas una única representación para todo, la pregunta específica tendrá que competir con el contenido restante. Además, los modelos tienen límites de entrada. Dividir permite buscar a una escala más precisa y controlar el texto que finalmente se entrega al generador.

Un **fragmento** o *chunk* es una porción del documento que el sistema utiliza como unidad de representación y recuperación. No tiene por qué ser un número fijo de caracteres: puede corresponder a un párrafo, una sección o una ventana de tokens.

El tamaño adecuado depende de qué debe conservarse para que la información tenga sentido. Una condición separada de la regla que limita puede producir una respuesta equivocada incluso cuando ambos textos siguen existiendo en el corpus.

## 2. El fragmento tiene cuatro papeles

El mismo fragmento se representa mediante un embedding, se guarda con un identificador, se recupera para construir el contexto y se vincula a la evidencia usada para evaluar. Por eso cambiar los cortes no es una modificación meramente visual: modifica qué textos existen como candidatos y cómo se relacionan con las respuestas esperadas.

Conviene distinguir:

| Elemento | Qué contiene | Para qué sirve |
| --- | --- | --- |
| Texto del fragmento | El pasaje legible | Dar contexto y mostrar evidencia |
| Embedding | Una representación numérica | Comparar con una consulta |
| Identificador | Una referencia al fragmento | Localizarlo dentro de una versión del índice |
| Metadatos | Origen, página, sección, versión | Interpretar, filtrar y citar |

Guardar el texto completo no implica que el embedding lo represente completo. Esa diferencia explica el truncamiento.

### Cómo se llega del fragmento al vector

El recorrido tiene varios objetos diferentes. Primero hay caracteres legibles. El tokenizador los convierte en identificadores de tokens. El codificador procesa esos identificadores y produce representaciones internas. Después, según la arquitectura, una operación de agregación o una representación designada resume la entrada en el vector utilizado para búsqueda. Ese último vector es el embedding del fragmento.

En la arquitectura de **un vector por fragmento** que estamos estudiando, su número de componentes es fijo para el modelo. Aumentar la longitud del fragmento no crea automáticamente más coordenadas. El modelo debe representar más contenido con la misma cantidad de componentes, y no todas las distinciones serán igual de útiles para la tarea de búsqueda.

No hay que imaginar cada coordenada como una casilla que almacena una palabra. La representación es distribuida y se aprende para conservar relaciones útiles según el objetivo de entrenamiento. Por eso «vector de 384 dimensiones» y «límite de 128 tokens» responden a preguntas diferentes: cuántos números produce y cuánta entrada admite.

El tokenizador del buscador y el del generador pueden ser distintos. Un fragmento que ocupa cierta cantidad de tokens al indexarlo puede ocupar otra al construir el prompt del LLM. El control de longitud debe hacerse en cada etapa con su tokenizador.

## 3. Qué es el truncamiento y cómo ocurre

El texto pasa por un tokenizador y se convierte en una secuencia de tokens. Si esa secuencia supera el límite efectivo del codificador y la configuración aplica truncamiento, una parte se elimina antes del cálculo del embedding. El sistema puede continuar sin excepción.

El índice conserva entonces un vector calculado con una porción del contenido, aunque el texto almacenado como *payload* siga estando completo. La búsqueda vectorial usa el vector, no vuelve a leer todo el payload en cada comparación.

![Texto almacenado frente a texto representado](<../Recursos visuales/21-s08-truncamiento.png>)

**Cómo leer el gráfico:** es un escenario didáctico de 900 **tokens**, no una medición de las 900 palabras de la diapositiva. Si el presupuesto útil fuera 128 tokens, se representaría como máximo el 14,2 % de esos tokens. La proporción de tokens retenidos no equivale a porcentaje de significado preservado ni a exactitud de recuperación.

El contenido omitido no contribuye directamente a ese vector. Aun así, podría llegar al generador si el fragmento se recupera por su parte inicial o mediante otra búsqueda y se entrega el payload completo. Por eso «no está representado» es más preciso que «es absolutamente imposible recuperarlo».

### Dos pérdidas diferentes: omitir texto y representar mal un detalle

El **truncamiento** elimina parte de la entrada antes de procesarla: el codificador nunca ve ese contenido. La **pérdida de detalle en la representación** puede ocurrir aunque toda la entrada quepa: el vector no distingue suficientemente un dato necesario para la búsqueda.

La diferencia determina la solución. Si el problema es truncamiento, debes hacer caber la entrada o cambiar el límite efectivo. Si el texto sí entra, aún debes examinar granularidad, modelo y tipo de consulta. Eliminar el truncamiento es una condición útil, pero no demuestra que el embedding identifique todas las respuestas posibles del fragmento.

El gráfico anterior muestra truncamiento de un prefijo en el supuesto ilustrado. Otras configuraciones pueden recortar de otra forma, o rechazar la entrada. Por eso debes inspeccionar el comportamiento real del pipeline y no deducirlo únicamente del nombre del modelo.

## 4. Las tres longitudes que no debes confundir

**Tamaño del fragmento:** decisión del sistema sobre cuánto texto agrupar. Puede estar expresado en caracteres, palabras o tokens.

**Límite del modelo de embeddings:** máximo efectivo que ese codificador procesa en la configuración utilizada. Es el límite relevante al indexar.

**Ventana del generador:** presupuesto de contexto del LLM que recibe instrucciones, pregunta, historial y evidencia; se debe reservar también el espacio de salida según el modelo y la API. Una ventana amplia del generador no arregla la información que perdió el codificador de embeddings.

Las páginas 10–11 atribuyen al notebook un límite de 128 tokens para MiniLM y al Lab 02 uno de 8192 para bge-m3. Son configuraciones reportadas por el curso. También comparan 300 caracteres, 500 tokens aproximados y 512 tokens del modelo. Los números no son comparables mientras no coincidan las unidades.

## 5. Por qué contar palabras no basta

La tokenización depende del vocabulario, el idioma y el texto. Una palabra puede dividirse en varios tokens; tampoco debe asumirse como ley universal que cada palabra separada por espacios produzca al menos un token en cualquier tokenizador.

Por eso, la cuenta $128/900$ es válida para un supuesto de **900 tokens**; para las **900 palabras** del PDF hace falta medir el texto con el tokenizador utilizado. La lección correcta de las diapositivas es detectar el truncamiento antes de indexar, no memorizar una conversión entre palabras y tokens.

El presupuesto debe incluir títulos o prefijos añadidos y los tokens especiales que requiera el modelo:

$$T_{\text{contenido}}+T_{\text{prefijos}}+T_{\text{especiales}}\leq L_{\text{efectivo}}.$$

Si el conteo del tokenizador ya incluye los tokens especiales, no se suman otra vez. La reserva de dos tokens que cita el Lab es una decisión de esa configuración, no una regla para todos los modelos.

## 6. Qué comprobar y por qué

Antes de indexar, cuenta la entrada final al codificador **sin truncarla previamente**. Si cuentas después de truncar, todas las entradas parecerán caber y esconderás el problema. Revisa la longitud máxima y cuántos fragmentos superan el límite; inspecciona también los cortes porque caber no garantiza coherencia.

Si no caben, puedes dividir mejor, reducir tamaño o usar un modelo cuyo límite y calidad sean apropiados. Cambiar de modelo exige recalcular las representaciones de los documentos y usar una representación compatible para las consultas. Tener mayor capacidad de entrada no asegura mejor recuperación.

> [!abstract] Para recordar
> **Guardado no significa representado.** Cuenta con el tokenizador del modelo y sobre la entrada completa que realmente le vas a enviar.

> [!question] Comprueba que lo entendiste
> ¿Por qué ampliar la ventana del LLM no corrige automáticamente el truncamiento del embedding?
>
> Porque son etapas distintas. El LLM solo recibe lo seleccionado después de una búsqueda que pudo haberse basado en representaciones incompletas.

**Para conectar:** [[29 S06 - De tokens a un vector de texto]] desarrolla las representaciones de tokens y su agregación. [[Hands-On_Large_Language_Models.pdf#page=257|Cap. 8, pp. impresas 235–237 (PDF 257–259)]] desarrolla el compromiso entre representar documentos completos y fragmentos.

**Fuente:** [[sesion-08.pdf#page=9|páginas 9–12]]. Las precisiones sobre unidades y alcance de la recuperación explicitan los límites del razonamiento del PDF. Continúa con [[37 S08 - Estrategias de fragmentación y solapamiento]].
