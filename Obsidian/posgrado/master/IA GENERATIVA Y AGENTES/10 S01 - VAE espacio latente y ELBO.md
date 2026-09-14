---
title: "10 S01 - VAE espacio latente y ELBO"
tags:
  - maestria/ia-generativa
  - estudio
---

# 10 S01 - VAE espacio latente y ELBO

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. Qué problema intenta resolver un VAE

Imagina muchas imágenes de números escritos a mano. Hay distintos tamaños, inclinaciones y grosores de trazo. Quieres aprender de esas imágenes para producir otras nuevas que se parezcan a ellas.

Un **VAE, autocodificador variacional**, aprende a generar datos usando una representación oculta llamada z. Puedes pensar en z como una lista de números que sirve de punto de partida para generar una imagen. No debes asumir que cada número tiene un significado claro, como «inclinación»: esa interpretación no está garantizada.

## 2. Primero entiende las dos redes

El **codificador** recibe una imagen y propone una distribución de códigos z que podrían servir para representarla.

El **decodificador** recibe un código z y produce una distribución sobre imágenes. Durante entrenamiento intentamos que pueda explicar bien las imágenes originales.

![Los dos recorridos del VAE](<Recursos visuales/07-vae.png>)

En la ruta superior partes de una imagen conocida. En la inferior partes de un código sorteado. Ambas rutas utilizan el mismo decodificador.

## 3. Por qué el codificador entrega una distribución

Un autocodificador determinista suele asignar un código concreto a una entrada. En el VAE gaussiano habitual, el codificador produce una media y una varianza para cada coordenada del código.

La **media** indica alrededor de qué valor se concentra esa coordenada. La **varianza** describe cuánto se dispersan sus valores. Después sorteamos un código usando esa distribución. A sortear siguiendo probabilidades se le llama **muestrear**.

Por eso dos pasadas de la misma imagen pueden utilizar códigos distintos. No significa que los pesos de la red hayan cambiado.

## 4. Reconstruir y generar tienen puntos de partida distintos

**Reconstruir:** tomas una imagen, la codificas, sorteas z y la decodificas. Puedes comparar el resultado con la imagen original.

**Generar una imagen nueva:** sorteas z de una distribución de referencia, llamada **prior**, y lo pasas al decodificador. No necesitas una imagen de entrada para esta ruta.

Un prior frecuente es $\mathcal N(0,I)$: coordenadas gaussianas con media cero y covarianza identidad. Es una distribución sencilla de la que podemos obtener códigos.

## 5. Qué debe aprender el modelo

No basta con reconstruir las imágenes conocidas mediante códigos arbitrarios. También queremos que los códigos sorteados del prior sean útiles para generar.

El entrenamiento combina dos objetivos:

1. Que el decodificador explique bien la imagen original a partir del código.
2. Que la distribución de códigos propuesta por el codificador no se aleje demasiado del prior.

El segundo se expresa mediante **divergencia KL**, una medida de diferencia entre distribuciones. No es simétrica: intercambiar las distribuciones puede cambiar el resultado.

## 6. La ELBO explicada antes de memorizarla

La **ELBO** es la cantidad que se maximiza al entrenar. Se puede leer como «qué tan bien explica el dato, menos una penalización por alejar el código del prior».

Supón que el primer término vale −5 y la penalización vale 2. ELBO = −5−2 = −7. Si otro ajuste obtiene −4 y penalización 5, ELBO = −9. Aunque mejoró la primera parte, empeoró el total. Como queremos maximizar, −7 es mejor que −9.

En símbolos:

$$\mathcal L(x)=\mathbb E_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)]-D_{KL}(q_\phi(z\mid x)\Vert p(z)).$$

Lee cada parte con calma:

- x es la imagen observada y z su código oculto.
- $q_\phi(z\mid x)$ es la distribución de códigos que propone el codificador.
- $p_\theta(x\mid z)$ es el modelo de imágenes del decodificador.
- $\mathbb E$ significa tomar un promedio sobre los códigos posibles.
- $\phi$ y $\theta$ son los pesos de las redes; no son el código z.

ELBO significa una **cota inferior**: queda por debajo de la log-probabilidad del dato que querríamos optimizar. Se usa porque calcular esa probabilidad exacta normalmente exige una integral difícil. En programas que minimizan una pérdida se usa a menudo el negativo de ELBO.

## 7. Cómo muestrear y seguir entrenando

Para calcular derivadas útiles se escribe el código como:

$$z=\mu+\sigma\odot\epsilon,\qquad\epsilon\sim\mathcal N(0,I).$$

Primero sorteamos ruido $\epsilon$. Después lo escalamos con la desviación estándar $\sigma$ y sumamos la media $\mu$. $\odot$ significa multiplicar coordenada por coordenada.

En una dimensión, con media 2, desviación 0.5 y ruido −1, obtenemos $z=2+0.5(-1)=1.5$. Se usa la desviación, no la varianza. Este procedimiento se llama **reparametrización** y permite calcular cómo cambiar los parámetros aunque haya muestreo.

## 8. Por qué se aprende un codificador

Averiguar qué código explica cada imagen mediante una búsqueda nueva puede ser costoso. El codificador aprende una función que reutilizamos para muchas imágenes. Murphy llama a esto **inferencia amortizada**: se invierte en aprender la función y luego se aplica a cada entrada.

Hay VAE para texto, aunque tienen dificultades. Una de ellas es que el decodificador termine utilizando poco el código oculto. Tampoco todos los VAE producen la salida de la misma manera: depende de cómo se diseñe el decodificador.

**Qué debes recordar:** el codificador ayuda a inferir códigos para datos conocidos; el decodificador utiliza códigos para modelar y generar datos. El entrenamiento conecta ambas partes.

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-01.pdf#page=17|Sesión 01, páginas 17–18]]
- [[doersch-2016-tutorial-vae.pdf|Doersch, introducción a modelos generativos y variables latentes]]
- [[murphy-2022-pml-introduction.pdf#page=713|Murphy, §20.3.5, pp. impresas 683–685; PDF 713–715]]

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿El codificador de un VAE gaussiano produce solo un vector fijo?
> Produce parámetros de una distribución, normalmente media y varianza. De esa distribución se muestrea el código latente.

> [!question]- ¿Qué equilibran los dos términos de la ELBO?
> El primer término favorece que el decodificador explique bien el dato original. El segundo penaliza que los códigos que propone el codificador se alejen demasiado de la distribución de la que queremos generar.

> [!question]- Con media 1, desviación 2 y epsilon 0.5, ¿cuánto vale z?
> z=1+2×0.5=2. Se utiliza la desviación estándar, no su cuadrado.

> [!question]- ¿Necesitas codificar un dato real para generar una muestra nueva?
> No. Puedes muestrear z del prior y decodificar. Codificar un dato se utiliza en reconstrucción e inferencia del latente.

> [!question]- ¿La KL es una distancia simétrica?
> No. Aunque es no negativa, en general KL(q‖p) no coincide con KL(p‖q).


> [!question]- ¿Qué significa inferencia amortizada?
> Significa aprender un codificador que propone códigos para muchas entradas. Así no hace falta empezar una búsqueda independiente y costosa cada vez que llega una nueva imagen.

> [!question]- ¿Qué ELBO es mejor: −7 o −9?
> −7, porque se maximiza la ELBO. Si se minimiza su negativo, 7 es mejor que 9.
