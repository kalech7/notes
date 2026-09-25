---
title: "45 S09 - Preguntas negativas y abstención"
sesion: "09"
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-09.pdf]]"
---

# 45 S09 - Preguntas negativas y abstención

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[42 S09 - Guía para evaluar un RAG|Guía de la sesión 09]]

## 1. Recuperar resultados no significa encontrar una respuesta

Fuente base: [[sesion-09.pdf#page=16|PDF, pp. 16–18]]. Un buscador top-k devuelve los resultados mejor puntuados entre los disponibles. Incluso si todos son malos, alguno será el primero. En la configuración descrita por el PDF, la recuperación no tiene un umbral que rechace automáticamente esos resultados.

Por eso «hay cinco resultados» no equivale a «hay información suficiente». La abstención requiere una decisión posterior: valorar evidencia, aplicar una política y, si corresponde, explicar que el corpus no permite contestar.

Un umbral de similitud puede ayudar, pero no prueba que exista una respuesta: similitud temática y suficiencia de evidencia son conceptos distintos. Las distancias de ejemplo del PDF pertenecen a una configuración concreta; no son umbrales que puedas copiar a otro modelo o corpus.

## 2. El falso 0,70

El ejemplo de la sesión contiene diez preguntas: cuatro simples, tres multi-chunk, dos negativas y una adversarial anotada sin documento fuente. Esta última se trata como no respondible. Quedan siete respondibles.

Si el sistema recupera evidencia en todas ellas, el Hit Rate correcto sobre respondibles es 7/7 = 1. Si incluyes como fallos las otras tres, obtienes 7/10 = 0,70. Cambió el denominador, no la recuperación.

Eso no prueba que el sistema completo sea perfecto: todavía hay que ver si respondió correctamente las siete y si se abstuvo ante las otras tres. Separar métricas permite localizar los errores sin ocultarlos.

## 3. Dos tasas que deben leerse juntas

$$
A_{neg}=\frac{\text{abstenciones en preguntas negativas}}{\text{número de negativas}}
$$

$$
A_{resp}=\frac{\text{abstenciones en preguntas respondibles}}{\text{número de respondibles}}
$$

Buscamos $A_{neg}$ alto y $A_{resp}$ bajo. Si no hay preguntas de una de las clases, la tasa correspondiente es no aplicable. No se convierte automáticamente en cero.

| Situación | El sistema responde | El sistema se abstiene |
| --- | --- | --- |
| Hay evidencia suficiente en el corpus | Puede ser útil; aún hay que juzgar corrección | Abstención indebida a nivel del sistema |
| No hay evidencia suficiente | Respuesta sin soporte del corpus, salvo política explícita de fuentes externas | Abstención correcta |

Un matiz importante: si el corpus sí contiene la respuesta pero la recuperación no la entregó, abstenerse puede ser prudente para el generador. En la evaluación de extremo a extremo sigue siendo una oportunidad perdida. La tasa señala el resultado; el diagnóstico debe localizar la causa.

## 4. Gráfico de comportamiento

![[30-s09-abstencion.png]]

### Cómo leer el gráfico

El eje horizontal mide abstención correcta en negativas: más a la derecha es mejor. El vertical mide abstención indebida en respondibles: más abajo es mejor. El punto ideal está abajo a la derecha, en (1,0).

«Siempre responde» está en (0,0): nunca rechaza una negativa, aunque no rechace ninguna respondible. «Siempre se abstiene» está en (1,1): reconoce todas las negativas a costa de no ayudar en ninguna respondible. El sistema didáctico está en (0,75; 0,125), que corresponde al ejemplo siguiente. La zona sombreada orienta la lectura; no establece un umbral universal de aceptación.

Los puntos son comportamientos hipotéticos, no mediciones de tu RAG. Moverse hacia la derecha y hacia abajo mejora estas dos tasas, pero todavía no demuestra que las respuestas emitidas sean fieles.

## 5. Ejemplo con cuentas completas

Tienes 8 respondibles y 4 negativas. El sistema se abstiene en 3 negativas y en 1 respondible:

- Abstención correcta: 3/4 = 0,75.
- Abstención indebida: 1/8 = 0,125.
- Una negativa recibió respuesta y una respondible quedó sin respuesta.

No dividas las 4 abstenciones totales entre 12 para sustituir estas tasas. Ese 33,3 % solo dice cuánto se calló el sistema; mezcla silencios deseables e indeseables.

Tampoco uses las dos tasas para calcular Hit Rate: las abstenciones describen la respuesta final, mientras Hit Rate describe la recuperación. Un sistema puede recuperar bien y abstenerse de más por un prompt excesivamente restrictivo.

## 6. Abstención y ataques son ejes distintos

Una pregunta puede contener «ignora los documentos» y al mismo tiempo tener una respuesta claramente sustentada. El comportamiento deseado puede ser responder al contenido legítimo usando evidencia, sin seguir la instrucción adversarial.

Por tanto, «se abstuvo» no demuestra por sí solo resistencia a ataques ni «respondió» demuestra que obedeció el ataque. Hay que mirar qué respondió y qué instrucciones siguió. Las etiquetas de la evaluación deben reflejar esa diferencia.

> [!abstract] Para recordar
> Evaluar el «no sé» requiere contar las veces que era necesario y las veces que no lo era.
