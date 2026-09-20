---
title: "08 S01 - GMM variables latentes y algoritmo EM"
tags:
  - maestria/ia-generativa
  - estudio
---

# 08 S01 - GMM variables latentes y algoritmo EM

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

Práctica del notebook: [[17 PRÁCTICA - Modelos generativos Naive Bayes GMM y bigramas#2. GMM: mezcla de gaussianas|Entrenar tres componentes y generar 200 puntos nuevos]].

## 1. Imagina una nube de puntos con dos grupos

Cada punto del siguiente gráfico tiene dos características numéricas. Podrían ser tamaño y duración de un archivo. Vemos concentraciones de puntos en zonas distintas, pero los datos no incluyen una etiqueta que diga a qué grupo pertenece cada uno.

Queremos un modelo que describa esa distribución y que también pueda crear puntos nuevos parecidos.

![Dos componentes de una mezcla](<../Recursos visuales/04-gmm-componentes.png>)

Los puntos grises son datos sintéticos. Las cruces señalan centros de dos distribuciones propuestas por el modelo. Las elipses muestran cómo se extiende cada distribución alrededor de su centro; no son paredes que prohíban pertenecer a otra.

## 2. Qué significa «mezcla de gaussianas»

Una **gaussiana** es una distribución que concentra valores alrededor de un centro y describe cómo se dispersan. En una dimensión suele dibujarse como una campana. En dos dimensiones puede representarse mediante contornos elípticos como los del gráfico.

Una sola gaussiana puede resultar insuficiente para dos concentraciones separadas. Un **GMM**, o modelo de mezcla de gaussianas, combina varias. Cada gaussiana se llama **componente**.

Para describir cada componente necesitamos:

- **Media:** dónde está su centro.
- **Covarianza:** cuánto se dispersa y cómo se relacionan las direcciones de variación.
- **Peso de mezcla:** qué proporción asigna el modelo a ese componente.

Los pesos de todos los componentes suman 1. Un componente sirve para describir los datos; no necesariamente representa una categoría real del mundo.

## 3. Qué está oculto

Ves el punto x, pero no sabes qué componente lo produjo. El modelo llama z a esa identidad desconocida. Se llama **variable latente** porque no está observada en los datos.

Imagina cómo generaría un punto el modelo: primero sortea un componente según sus pesos; después sortea un punto de esa gaussiana. Cuando solo vemos el punto final, intentamos razonar en sentido inverso: ¿qué componente pudo producirlo?

## 4. Un punto puede tener dos explicaciones posibles

En lugar de forzar una etiqueta, calculamos probabilidades sobre sus posibles componentes. Por ejemplo, 75 % para el primero y 25 % para el segundo.

Estas probabilidades se llaman **responsabilidades**. No significan que el punto esté físicamente dividido; expresan nuestra incertidumbre sobre qué componente lo explica.

Supón que los componentes tienen pesos 0.6 y 0.4. Para un punto concreto, sus densidades son 0.2 y 0.1. Hacemos lo siguiente:

| Paso | Componente 1 | Componente 2 |
| --- | --- | --- |
| Peso por densidad | 0.6 × 0.2 = 0.12 | 0.4 × 0.1 = 0.04 |
| Dividir por el total 0.16 | 0.12/0.16 = 0.75 | 0.04/0.16 = 0.25 |

Eso es Bayes aplicado al componente oculto. La densidad 0.2 no equivale a 20 % de probabilidad de ese punto; las probabilidades del componente son las responsabilidades obtenidas al normalizar.

## 5. Por qué se alternan dos pasos al entrenar

Hay una dificultad: para calcular a qué grupo pertenece un punto necesitamos conocer los grupos, pero para describir los grupos necesitamos saber qué puntos les corresponden.

El algoritmo **EM, esperanza–maximización**, comienza con una propuesta y la mejora alternando dos operaciones.

![Ciclo de EM](<../Recursos visuales/05-em-ciclo.png>)

**Paso E:** con los centros, covarianzas y pesos actuales, calcula las responsabilidades de cada punto. Por ahora no cambia esos parámetros.

**Paso M:** usa esas responsabilidades para calcular nuevos centros, covarianzas y pesos. Por ahora no cambia las responsabilidades.

Después vuelve a E, porque los nuevos parámetros pueden cambiar qué componente explica mejor cada punto. Se repite hasta que se cumple un criterio de parada, como cambios suficientemente pequeños en el objetivo.

## 6. Calculemos un centro nuevo

Tenemos tres datos: 0, 2 y 10. El primer componente les asigna responsabilidades 0.9, 0.8 y 0.1. El dato 10 cuenta poco para ese componente porque su responsabilidad es baja.

Multiplica cada dato por su responsabilidad:

$$0(0.9)+2(0.8)+10(0.1)=0+1.6+1=2.6.$$

Suma las responsabilidades: $0.9+0.8+0.1=1.8$. Divide para obtener el promedio ponderado:

$$\text{centro nuevo}=2.6/1.8\approx1.444.$$

El 1.8 es una cantidad efectiva de observaciones: suma aportes parciales. El nuevo peso del componente es $1.8/3=0.6$.

Para el segundo componente, las responsabilidades son 0.1, 0.2 y 0.9. Su centro es $9.4/1.2\approx7.833$ y su peso 0.4.

## 7. Cómo se escribe todo esto con símbolos

$$p(x)=\sum_{k=1}^{K}\pi_k\mathcal N(x\mid\mu_k,\Sigma_k).$$

La fórmula dice: suma lo que aporta cada componente al dato x. K es la cantidad de componentes; $\pi_k$ su peso; $\mu_k$ su centro; $\Sigma_k$ su covarianza. $\mathcal N$ representa la densidad gaussiana.

La responsabilidad se calcula dividiendo el aporte de un componente por la suma de todos:

$$\gamma_{ik}=\frac{\pi_k\mathcal N(x_i\mid\mu_k,\Sigma_k)}{\sum_j\pi_j\mathcal N(x_i\mid\mu_j,\Sigma_j)}.$$

Es exactamente el procedimiento de la tabla. Sumar las posibilidades de una variable que no observamos se llama **marginalizar**.

## 8. Qué puede y qué no puede hacer este modelo

Una vez entrenado puede generar puntos: elegir componente y después generar dentro de él. En la actividad se usa `gmm.sample()` para ese fin.

EM puede terminar en una solución local: mejora respecto de cambios cercanos sin ser necesariamente la mejor solución posible. También pueden aparecer covarianzas que se contraen demasiado alrededor de un dato. Por eso importa la inicialización y pueden imponerse restricciones o regularización.

Este GMM no modela el orden de los puntos. Para representar una secuencia necesitamos otra estructura, como [[09 S01 - Markov HMM y generación con bigramas|un HMM]].

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-01.pdf#page=13|Sesión 01, páginas 13]]
- [[bishop-2006-prml.pdf#page=459|Bishop, §9.2.2, p. impresa 439; PDF 459]]

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Qué se observa y qué es latente en el ejemplo?
> Se observan los puntos. La identidad del componente que generó cada punto no se observa y se infiere.

> [!question]- ¿Cómo se obtienen responsabilidades 0.75 y 0.25?
> Se multiplican peso y densidad: 0.12 y 0.04. Se divide cada contribución por 0.16.

> [!question]- ¿Qué mantiene fijo el paso E y qué mantiene fijo el M?
> En E usas los centros, dispersiones y pesos actuales para calcular cuánto corresponde cada punto a cada componente. En M usas esos aportes para calcular nuevos parámetros. Solo después vuelves a E.

> [!question]- ¿EM garantiza el mejor máximo global?
> No. Puede llegar a máximos locales o soluciones degeneradas según el modelo y la inicialización.

> [!question]- ¿Cómo genera un punto nuevo un GMM?
> Primero sortea un componente según sus pesos y luego un punto de la gaussiana de ese componente.


> [!question]- ¿Puede un componente tener 1.8 observaciones efectivas?
> Sí. Es la suma de responsabilidades, no un conteo de personas u objetos indivisibles.

> [!question]- ¿Cuánto vale la media del primer componente del ejemplo?
> Primero: 0×0.9 + 2×0.8 + 10×0.1 = 2.6. Después suma los aportes: 0.9+0.8+0.1=1.8. La media es 2.6/1.8≈1.444. El punto 10 influye poco porque su responsabilidad es solo 0.1.
