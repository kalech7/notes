---
title: "05 S01 - Probabilidad y teorema de Bayes paso a paso"
tags:
  - maestria/ia-generativa
  - estudio
---

# 05 S01 - Probabilidad y teorema de Bayes paso a paso

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-01.pdf#page=9|Sesión 01, páginas 9–10]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción.

## Vocabulario antes de la fórmula

Una variable aleatoria representa resultados posibles. $Y$ puede ser la clase de un correo: spam o normal. $X$ puede representar características del correo.

| Expresión | Cómo leerla |
| --- | --- |
| $P(Y)$ | Probabilidad de una clase antes de observar el correo |
| $P(X,Y)$ | Probabilidad conjunta de características y clase |
| $P(X\mid Y)$ | Probabilidad de las características si conocemos la clase |
| $P(Y\mid X)$ | Probabilidad de la clase después de ver las características |

La barra significa «dado». Cambiar lo que está antes y después de ella cambia la pregunta. Que «oferta» sea frecuente en spam no implica que todo correo con «oferta» sea spam.

Para variables continuas se emplean densidades, usualmente escritas $p$. Una densidad en un punto no es la probabilidad de ese punto y puede superar 1; las probabilidades se obtienen integrando sobre regiones.

## Derivación de Bayes

La conjunta se puede escribir de dos maneras:

$$P(X,Y)=P(X\mid Y)P(Y)=P(Y\mid X)P(X).$$

Si $P(X)>0$, dividir por $P(X)$ da:

$$P(Y\mid X)=\frac{P(X\mid Y)P(Y)}{P(X)}.$$

La posterior combina una frecuencia previa con lo compatible que resulta la nueva observación con cada posibilidad. El denominador normaliza para que las probabilidades de todas las clases sumen 1.

## Ejemplo completo con correos

Imagina 1 000 correos: 200 spam y 800 normales. De los spam, 120 contienen «oferta»; de los normales, 80 contienen esa palabra.

1. **Prior:** $P(S)=200/1000=0.2$.
2. **Verosimilitud:** $P(O\mid S)=120/200=0.6$.
3. Para normales: $P(O\mid N)=80/800=0.1$.
4. **Evidencia:** $P(O)=0.6(0.2)+0.1(0.8)=0.2$.
5. **Posterior:** $P(S\mid O)=0.6(0.2)/0.2=0.6$.

Comprobación por conteo: hay 200 correos con «oferta», de los cuales 120 son spam; 120/200 es 60 %. Observar la palabra eleva la probabilidad del 20 % al 60 %, pero no la lleva al 100 %.

## El mismo teorema en dos planos

**Plano de clase:** desconocemos Y y observamos X. Calculamos $P(Y\mid X)$.

**Plano de parámetros:** desconocemos $\theta$ y observamos un conjunto de datos D. Calculamos:

$$p(\theta\mid D)=\frac{p(D\mid\theta)p(\theta)}{p(D)}.$$

Aquí $\theta$ podría ser la probabilidad desconocida de que una moneda salga cara. Antes de lanzar la moneda tenemos un prior sobre sus valores posibles; después de observar resultados lo actualizamos.

La **verosimilitud** $p(D\mid\theta)$ mantiene D fijo y compara diferentes valores de $\theta$. No es, por ese hecho, una distribución normalizada sobre $\theta$.

## Máxima verosimilitud no es toda la inferencia bayesiana

La estimación por máxima verosimilitud, MLE, elige un valor:

$$\hat\theta=\arg\max_\theta p(D\mid\theta).$$

Si una moneda produce 7 caras en 10 lanzamientos independientes, la verosimilitud de la secuencia es $\theta^7(1-\theta)^3$ y su máximo está en $\hat\theta=0.7$. Si modelamos solo el conteo, aparece además un coeficiente binomial que no cambia ese máximo.

MLE devuelve una estimación puntual. La inferencia bayesiana calcula una distribución posterior que incorpora un prior y representa incertidumbre. No se deben usar ambos nombres como sinónimos.

Para observaciones independientes, la verosimilitud es un producto. Tomar logaritmos lo convierte en suma; maximizar la log-verosimilitud equivale a minimizar su negativo. Esta es una fuente importante de funciones de pérdida, aunque no todas las pérdidas de aprendizaje automático son de ese tipo.

## Complemento del libro: una posterior conserva más información que un número

Murphy desarrolla el ejemplo de una moneda para explicar cómo actualizar incertidumbre. Si ves 7 caras y 3 cruces, MLE entrega 0.7. Con un prior uniforme Beta(1,1), la posterior es Beta(8,4): una distribución completa de valores plausibles de la probabilidad de cara.

Su media es $8/(8+4)=2/3$. No contradice el 0.7: responde a una operación diferente que incluye el prior. La moda de esta posterior es 0.7, mientras su media es aproximadamente 0.667. Resumir una distribución por el pico o por el promedio no es lo mismo.

Esta diferencia explica por qué «todavía no lo vi» no significa «es imposible». Con tres caras y ninguna cruz, MLE asigna cero a la siguiente cruz; la predicción bayesiana con ese prior le asigna 1/5.

Para seguir los cálculos sin alargar esta nota, tienes [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]]. Allí se explica Beta, posterior, MAP y predicción desde cero.

**Fuente:** [[murphy-2022-pml-introduction.pdf#page=160|Murphy, §4.6.2, pp. impresas 130–134; PDF 160–164]]. Los conteos del ejemplo son propios.

## Gráficos y diagramas para entender el tema

### Ver Bayes como un cambio de grupo

![Ver Bayes como un cambio de grupo](<Recursos visuales/03-bayes-conteos.png>)

**Cómo leerlo:** Primero divide los 1 000 correos por clase. Después conserva los que contienen «oferta»: 120 spam y 80 normales. La posterior usa como denominador ese nuevo grupo de 200 correos. Así se ve por qué P(oferta dado spam) y P(spam dado oferta) responden preguntas diferentes.

*Figuras originales elaboradas para estos apuntes. Los números y supuestos se explican en el texto; no son imágenes copiadas de los libros.*

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿P(oferta dado spam) y P(spam dado oferta) son iguales?
> No. La primera se calcula entre los spam; la segunda entre los correos que contienen «oferta». Sus denominadores y preguntas son diferentes.

> [!question]- En el ejemplo, ¿por qué la posterior es 60 % y no 100 %?
> Porque también existen correos normales con «oferta». Entre los 200 que contienen la palabra, 120 son spam y 80 normales.

> [!question]- ¿Para qué sirve la evidencia?
> Normaliza. En clasificación suma la verosimilitud multiplicada por el prior de cada clase, de modo que las posteriores sumen 1.

> [!question]- ¿Qué debes aclarar cuando dices posterior?
> De qué variable hablas: clase, parámetros o variable latente. El teorema es el mismo, pero la incógnita es diferente.

> [!question]- ¿MLE proporciona una distribución sobre los parámetros?
> No por sí sola. Selecciona el valor que maximiza la verosimilitud; una posterior bayesiana sí es una distribución sobre parámetros.


> [!question]- ¿Por qué MLE, MAP y media posterior pueden dar números diferentes?
> MLE maximiza la verosimilitud, MAP maximiza la posterior y la media promedia la posterior. Son operaciones distintas y pueden usar información diferente.
