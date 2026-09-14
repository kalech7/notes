---
title: "05 S01 - Probabilidad y teorema de Bayes paso a paso"
tags:
  - maestria/ia-generativa
  - estudio
---

# 05 S01 - Probabilidad y teorema de Bayes paso a paso

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. La pregunta que vamos a resolver

Recibes un correo que contiene la palabra «oferta». Quieres saber si es spam. La palabra es una pista, pero también aparece en correos normales. **Bayes permite combinar esa pista con lo que ya sabíamos antes de leerla.**

Primero resolveremos el problema contando correos. Después veremos que la fórmula de Bayes expresa ese mismo cálculo.

## 2. Cuenta los correos antes de usar letras

Tenemos 1 000 correos: 200 spam y 800 normales. De los 200 spam, 120 contienen «oferta». De los 800 normales, 80 contienen «oferta».

| Tipo de correo | Con «oferta» | Sin «oferta» | Total |
| --- | --- | --- | --- |
| Spam | 120 | 80 | 200 |
| Normal | 80 | 720 | 800 |
| Total | 200 | 800 | 1 000 |

Antes de mirar palabras, 200 de cada 1 000 correos son spam: 20 %. Cuando sabemos que aparece «oferta», solo nos interesan los 200 de la primera columna. De ellos, 120 son spam.

Por tanto, la respuesta es $120/200=0.6$: **60 %**. La pista hizo subir la probabilidad del 20 % al 60 %, pero no al 100 %.

![Bayes explicado mediante conteos](<Recursos visuales/03-bayes-conteos.png>)

Sigue las flechas y observa cómo cambia el grupo que contamos. La respuesta final usa únicamente los correos con «oferta».

## 3. Dos preguntas que se parecen, pero no son iguales

**¿Cuántos spam contienen «oferta»?** Miras la fila de spam: 120/200 = 60 %.

**¿Cuántos correos con «oferta» son spam?** Miras la columna de «oferta»: 120/200 = 60 %.

En este ejemplo ambas dan 60 % **por coincidencia de los conteos**, no porque sean la misma pregunta. Sus grupos de referencia son distintos. Si hubiera 160 correos normales con «oferta», la primera seguiría dando 60 %, pero la segunda sería 120/280 ≈ 42.86 %.

La notación distingue el orden: $P(O\mid S)$ es «oferta dado spam» y $P(S\mid O)$ es «spam dado oferta». La barra se lee **dado que sabemos**.

## 4. Ahora sí: la fórmula de Bayes

Usaremos S para spam, N para normal y O para la presencia de «oferta».

$$P(S\mid O)=\frac{P(O\mid S)P(S)}{P(O)}.$$

Lee la fórmula así: multiplica la probabilidad de observar la pista dentro del spam por la proporción de spam; luego divide por la proporción total de correos que tienen esa pista.

1. $P(S)=0.2$: lo que sabíamos antes. Se llama **prior**.
2. $P(O\mid S)=0.6$: qué tan compatible es la pista con spam. Es la **verosimilitud** de la pista bajo esa clase.
3. $P(O)=0.6(0.2)+0.1(0.8)=0.2$: contamos la pista tanto en spam como en normales. Se llama **evidencia**.
4. $P(S\mid O)=0.6(0.2)/0.2=0.6$: lo que obtenemos después. Se llama **posterior**.

El denominador permite que las probabilidades de spam y normal sumen 1. A esta operación se le llama **normalizar**.

## 5. De dónde sale la fórmula

La probabilidad de que un correo sea spam **y** contenga «oferta» puede calcularse de dos maneras:

$$P(S,O)=P(O\mid S)P(S)=P(S\mid O)P(O).$$

En ambos lados contamos el mismo grupo de 120 correos, pero empezamos desde grupos diferentes. Dividir por $P(O)$ produce la fórmula de Bayes. No es una regla desconectada del conteo: resume ese razonamiento.

## 6. Bayes también sirve para aprender parámetros

Hasta aquí la incógnita era la clase de un correo. También puede ser un número desconocido, como la probabilidad de cara de una moneda. Llamamos $\theta$ a ese número y D a los lanzamientos observados.

$$p(\theta\mid D)=\frac{p(D\mid\theta)p(\theta)}{p(D)}.$$

La pregunta ahora es: «después de observar D, ¿qué valores de $\theta$ siguen siendo plausibles?». Por eso conviene decir siempre **posterior de qué**: de la clase, de un parámetro o de una variable oculta.

## 7. Estimar un número no es conservar toda la incertidumbre

Si observas siete caras en diez lanzamientos, **máxima verosimilitud (MLE)** elige $\hat\theta=0.7$. Selecciona el valor que mejor explica los datos según el modelo.

Una posterior bayesiana conserva una distribución de valores posibles e incorpora el prior. **MAP** elige el punto más alto de esa posterior; la **media posterior** calcula su promedio. Son operaciones distintas.

La nota [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]] desarrolla este caso lentamente. Antes de avanzar, asegúrate de poder resolver el ejemplo de correos sin memorizar la fórmula.

Cuando veas una letra p aplicada a valores continuos, como $\theta$, suele indicar una **densidad**. Su altura no es la probabilidad de un punto: las probabilidades corresponden a áreas bajo la curva. El gráfico de la ampliación lo muestra.

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-01.pdf#page=9|Sesión 01, páginas 9–10]]
- [[murphy-2022-pml-introduction.pdf#page=160|Murphy, §4.6.2, pp. impresas 130–134; PDF 160–164]]

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿P(oferta dado spam) y P(spam dado oferta) son iguales?
> No. La primera se calcula entre los spam; la segunda entre los correos que contienen «oferta». Sus denominadores y preguntas son diferentes.

> [!question]- En el ejemplo, ¿por qué la posterior es 60 % y no 100 %?
> Porque también existen correos normales con «oferta». Entre los 200 que contienen la palabra, 120 son spam y 80 normales.

> [!question]- ¿Para qué sirve la evidencia?
> Cuenta la pista considerando todas las clases. En el ejemplo suma 0.6×0.2 para spam y 0.1×0.8 para normales. Dividir por ese total permite que las probabilidades finales de ambas clases sumen 1.

> [!question]- ¿Qué debes aclarar cuando dices posterior?
> De qué variable hablas: clase, parámetros o variable latente. El teorema es el mismo, pero la incógnita es diferente.

> [!question]- ¿MLE proporciona una distribución sobre los parámetros?
> No por sí sola. Selecciona el valor que maximiza la verosimilitud; una posterior bayesiana sí es una distribución sobre parámetros.


> [!question]- ¿Por qué MLE, MAP y media posterior pueden dar números diferentes?
> MLE maximiza la verosimilitud, MAP maximiza la posterior y la media promedia la posterior. Son operaciones distintas y pueden usar información diferente.
