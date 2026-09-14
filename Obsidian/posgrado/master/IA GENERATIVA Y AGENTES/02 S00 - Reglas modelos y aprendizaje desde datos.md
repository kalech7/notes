---
title: "02 S00 - Reglas modelos y aprendizaje desde datos"
tags:
  - maestria/ia-generativa
  - estudio
---

# 02 S00 - Reglas modelos y aprendizaje desde datos

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-00.pdf#page=11|Sesión 00, páginas 11–13]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción.

## Un modelo es una representación que puede fallar

Un modelo simplifica un fenómeno para calcular algo sobre él. Un mapa no contiene todos los detalles de una ciudad, pero permite planificar una ruta. De manera parecida, un modelo de clasificación conserva relaciones útiles para predecir una etiqueta.

Sus supuestos determinan qué representa bien y qué puede ignorar. Un modelo puede ser matemáticamente correcto y describir mal el fenómeno porque sus supuestos no se cumplen.

## Dos maneras de introducir conocimiento

**Enfoque simbólico:** una persona expresa hechos, reglas y relaciones. Un motor de inferencia utiliza esas reglas para obtener conclusiones.

```text
Hecho: Ana entregó el proyecto.
Hecho: Ana aprobó el examen.
Regla: si alguien entregó el proyecto y aprobó el examen,
       cumple los requisitos académicos considerados.
Conclusión: Ana cumple esos requisitos.
```

Aquí podemos inspeccionar la derivación. Pero la conclusión solo vale respecto de esas reglas y hechos: si falta un requisito, la derivación no garantiza que la decisión sea correcta en el mundo real.

LISP y Prolog aparecen en la sesión como herramientas históricas importantes. LISP está asociado al procesamiento de listas y funciones; Prolog permite expresar hechos y reglas lógicas. No necesitas dominar estos lenguajes para comprender la diferencia entre escribir conocimiento y aprender parámetros.

**Enfoque estadístico:** se define una familia de modelos y se ajustan sus parámetros a partir de ejemplos. Para detectar spam, en lugar de escribir todas las reglas posibles, se proporcionan correos y etiquetas y se optimiza un criterio de aprendizaje.

La frase «nadie escribe el conocimiento» es una simplificación: las personas siguen eligiendo datos, variables, arquitectura y objetivo. Lo aprendido es la configuración concreta de parámetros.

| Aspecto | Reglas explícitas | Aprendizaje estadístico |
| --- | --- | --- |
| Contenido principal | Hechos y reglas | Parámetros ajustados |
| Cambio habitual | Editar reglas | Volver a entrenar o ajustar |
| Dificultad | Mantener excepciones | Conseguir datos y generalizar |
| Explicación | Puede ofrecer derivación formal | Requiere analizar comportamiento y evidencia |

Las familias pueden combinarse. Un sistema puede generar texto con una red neuronal y comprobar reglas de negocio mediante código.

## Qué ocurre al entrenar

1. Se representan las entradas mediante números.
2. El modelo produce una predicción usando sus parámetros actuales.
3. Una función de pérdida mide el desacuerdo con el objetivo.
4. Un procedimiento de optimización modifica los parámetros.
5. Se evalúa con datos distintos de los usados para ajustar.

**Entrenamiento** significa ajustar. **Inferencia**, en el uso habitual de aprendizaje automático, significa aplicar el modelo entrenado. Un ejemplo nuevo puede cambiar la respuesta sin cambiar los pesos.

### Memorizar no es generalizar

Si estudias únicamente las respuestas exactas de un examen viejo, puedes fallar ante una pregunta equivalente redactada de otra forma. A un modelo también le puede pasar: aprender detalles del conjunto de entrenamiento no garantiza funcionar en casos nuevos.

Por eso se separan datos de entrenamiento, validación y prueba. La validación ayuda a tomar decisiones de desarrollo; la prueba permite una evaluación final que no debería guiar repetidamente esas decisiones.

## Qué cambia con deep learning

En aprendizaje estadístico tradicional era frecuente diseñar manualmente características: presencia de palabras, longitud del texto o número de signos. Las redes profundas pueden aprender representaciones intermedias útiles a partir de los datos.

Esto no elimina el diseño humano; desplaza parte del trabajo hacia seleccionar la arquitectura, el objetivo y el procedimiento de aprendizaje. La siguiente nota muestra la unidad más sencilla de ese enfoque: [[03 S00 - Perceptrón redes neuronales y XOR]].

## Complemento del libro: entender el sobreajuste con una curva

Bishop empieza con puntos generados alrededor de una curva. Compara modelos con distinta flexibilidad: uno demasiado rígido no sigue la tendencia; uno muy flexible pasa por todos los puntos, pero oscila entre ellos. Ajustar exactamente las observaciones también puede significar ajustar su ruido.

Imagina que mides temperatura a diferentes horas. Las mediciones contienen una tendencia y pequeñas variaciones del sensor. Si fuerzas al modelo a reproducir cada variación, quizá prediga mal una hora no medida. El objetivo es capturar la relación que persiste, no cada accidente de la muestra.

| Lo que observas | Interpretación posible | Qué revisar |
| --- | --- | --- |
| Error alto en entrenamiento y validación | Modelo demasiado restrictivo o ajuste deficiente | Representación, capacidad y entrenamiento |
| Error muy bajo en entrenamiento y alto en validación | Posible sobreajuste | Datos, complejidad y regularización |
| Error bajo en ambos | Buena señal en esa evaluación | Prueba independiente y condiciones de uso |

Estos patrones orientan el diagnóstico; no identifican por sí solos una causa única. Datos mal divididos también pueden hacer que la validación parezca excelente.

**Capacidad** significa qué funciones puede representar el modelo. **Generalización** significa cómo funciona fuera de los datos de ajuste. La primera no garantiza la segunda. En la figura del libro, el polinomio más flexible incluye a los simples entre sus posibilidades, pero el ajuste elegido a partir de pocos datos resulta peor fuera de la muestra.

**Fuente:** [[bishop-2006-prml.pdf#page=26|Bishop, §1.1, pp. impresas 6–8; PDF 26–28]]. El ejemplo de temperatura y la tabla son explicaciones propias.

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Qué diferencia hay entre un modelo y la realidad?
> El modelo es una representación con supuestos y simplificaciones. Puede ser útil y aun así fallar en situaciones que sus supuestos no cubren.

> [!question]- ¿Por qué una derivación lógica no garantiza una conclusión verdadera en el mundo?
> Porque depende de la corrección y suficiencia de los hechos y reglas. Una derivación válida a partir de premisas equivocadas puede producir una conclusión inaplicable.

> [!question]- ¿Qué cambia al entrenar y qué suele permanecer fijo al usar un modelo?
> Durante el entrenamiento se ajustan parámetros. Durante la inferencia ordinaria se usan esos parámetros fijos; cambian las entradas y las activaciones.

> [!question]- ¿Por qué no basta con medir aciertos en los ejemplos de entrenamiento?
> Porque puede haber memorización o sobreajuste. Se necesitan ejemplos nuevos para evaluar generalización.


> [!question]- ¿Por qué pasar por todos los puntos puede ser una mala señal?
> Porque esos puntos pueden contener ruido. Ajustarlo exactamente puede producir predicciones inestables entre observaciones.

> [!question]- ¿Capacidad y generalización son sinónimos?
> No. Capacidad describe qué puede representar la familia; generalización describe el desempeño aprendido en casos nuevos.
