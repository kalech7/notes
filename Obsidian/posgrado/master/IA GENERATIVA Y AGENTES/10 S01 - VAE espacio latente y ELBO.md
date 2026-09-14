---
title: "10 S01 - VAE espacio latente y ELBO"
tags:
  - maestria/ia-generativa
  - estudio
---

# 10 S01 - VAE espacio latente y ELBO

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-01.pdf#page=17|Sesión 01, páginas 17–18]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción.

## Intuición: generar a través de una representación oculta

Un **autocodificador variacional (VAE)** propone que un dato puede generarse a partir de una variable latente continua z. En una imagen de un dígito, esa representación podría codificar variaciones de forma o trazo, aunque no se garantiza que cada dimensión tenga una interpretación humana clara.

El modelo generativo tiene un prior $p(z)$ y un decodificador probabilístico $p_\theta(x\mid z)$. Para aprender a partir de datos se añade un codificador $q_\phi(z\mid x)$ que aproxima la posterior del latente.

## Dos redes, dos funciones

| Parte | Entrada y salida | Papel |
| --- | --- | --- |
| Codificador | De x a parámetros de una distribución sobre z | Inferir latentes plausibles |
| Decodificador | De z a una distribución sobre x | Reconstruir o generar |

En el caso gaussiano diagonal usual, el codificador produce una media $\mu$ y varianzas $\sigma^2$. No entrega solo un código fijo: define una distribución de códigos para esa entrada.

Los parámetros $\phi$ pertenecen al codificador y $\theta$ al decodificador. El latente z es diferente: se infiere o muestrea por ejemplo y no es el conjunto de pesos de las redes.

## Por qué aparece la ELBO

Queremos modelar:

$$p_\theta(x)=\int p_\theta(x\mid z)p(z)\,dz.$$

La integral suele ser difícil de calcular exactamente. Se optimiza una cota inferior de la log-probabilidad, llamada **ELBO**:

$$\mathcal L(x)=\mathbb E_{q_\phi(z\mid x)}[\log p_\theta(x\mid z)]
-D_{KL}(q_\phi(z\mid x)\Vert p(z)).$$

El primer término recompensa que el decodificador explique bien x usando códigos del codificador. El segundo penaliza que la distribución codificada se aparte del prior. **Se maximiza la ELBO**; si el programa utiliza una pérdida para minimizar, suele emplear su negativo.

Una forma de comprender ambos términos: no basta con reconstruir cada dato mediante códigos arbitrarios; también queremos que el espacio donde muestreamos produzca códigos útiles. El equilibrio es una propiedad del objetivo, no una promesa de que toda muestra será buena.

La divergencia KL es no negativa y no es una distancia simétrica. En general, intercambiar sus dos distribuciones cambia el resultado.

## Reparametrización con números

En lugar de escribir un muestreo cuya dependencia de los parámetros resulte difícil de derivar, se usa:

$$\epsilon\sim\mathcal N(0,I),\qquad z=\mu+\sigma\odot\epsilon.$$

$\odot$ indica multiplicación componente a componente. La aleatoriedad se concentra en $\epsilon$ y el resto se expresa como operaciones diferenciables respecto de $\mu$ y $\sigma$.

En una dimensión, si $\mu=2$, $\sigma=0.5$ y se obtiene $\epsilon=-1$, entonces z=1.5. Multiplicamos por la desviación estándar $\sigma$, no por la varianza $\sigma^2$.

## Reconstruir y generar

**Reconstruir:** partir de un dato x, codificarlo, muestrear z de $q_\phi(z\mid x)$ y decodificar.

**Generar:** muestrear z directamente del prior, por ejemplo $\mathcal N(0,I)$, y usar el decodificador. No hace falta una entrada observada para este paso.

## Matices de la diapositiva

«El VAE falla en texto» resume dificultades, no una imposibilidad general. Hay modelos variacionales de texto. Sus problemas pueden incluir objetivos difíciles de equilibrar y colapso del posterior, donde el decodificador usa poco la información latente.

Tampoco todos los decodificadores VAE producen componentes de x de manera independiente o simultánea: depende de la arquitectura y de cómo se factorice $p_\theta(x\mid z)$. El ejemplo introductorio del curso usa el contraste con generación paso a paso para orientar la intuición.

**Apoyo consultado:** [[doersch-2016-tutorial-vae.pdf|Doersch, introducción a modelos generativos y variables latentes]]. La fórmula de ELBO y la reparametrización también aparecen en el glosario suministrado.

## Complemento del libro: por qué el codificador es una aproximación útil

Murphy explica el codificador como una **red de inferencia**. Dado x, queremos averiguar qué z podría haberlo generado. Resolver esa búsqueda desde cero para cada dato puede ser costoso; el codificador aprende una función reutilizable que propone una distribución latente rápidamente. A esto se le llama inferencia amortizada.

La dirección generativa sigue siendo $z\rightarrow x$. La dirección $x\rightarrow z$ del codificador ayuda a inferir y entrenar; no cambia el sentido de cómo el modelo dice que se producen los datos.

Un autocodificador determinista puede aprender a comprimir y reconstruir, pero su objetivo de reconstrucción, por sí solo, no define un prior adecuado del que muestrear códigos nuevos. El VAE incorpora explícitamente ese componente probabilístico y un objetivo que lo conecta con la reconstrucción.

### Una ELBO con números

Supón que el término esperado de reconstrucción vale −5 y la KL vale 2. Entonces ELBO = −7 y su negativo, utilizado como pérdida, vale 7. En otro ajuste, la reconstrucción mejora a −4, pero la KL sube a 5: ELBO = −9. Mejoró una parte y empeoró el objetivo conjunto.

Esto evita interpretar «reconstruye mejor» como sinónimo de «optimiza mejor el VAE». Hay que evaluar ambos términos. Los valores son inventados para entender signos y balance; no representan un experimento del libro.

**Fuente:** [[murphy-2022-pml-introduction.pdf#page=713|Murphy, §20.3.5, pp. impresas 683–685; PDF 713–715]], especialmente la explicación de inferencia amortizada y las ecuaciones de ELBO en PDF 715.

## Gráficos y diagramas para entender el tema

### Dos recorridos en un VAE

![Dos recorridos en un VAE](<Recursos visuales/07-vae.png>)

**Cómo leerlo:** Arriba: un dato pasa por el codificador, se obtiene una distribución latente y se muestrea z para decodificar. Abajo: al generar, z viene directamente del prior. El decodificador produce una distribución sobre x; su salida puede usarse para reconstruir o muestrear según el modelo. La ruta inferior evita el codificador, pero utiliza el mismo decodificador entrenado.

*Figuras originales elaboradas para estos apuntes. Los números y supuestos se explican en el texto; no son imágenes copiadas de los libros.*

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿El codificador de un VAE gaussiano produce solo un vector fijo?
> Produce parámetros de una distribución, normalmente media y varianza. De esa distribución se muestrea el código latente.

> [!question]- ¿Qué equilibran los dos términos de la ELBO?
> La capacidad de explicar o reconstruir el dato y la cercanía de la distribución latente inferida al prior.

> [!question]- Con media 1, desviación 2 y epsilon 0.5, ¿cuánto vale z?
> z=1+2×0.5=2. Se utiliza la desviación estándar, no su cuadrado.

> [!question]- ¿Necesitas codificar un dato real para generar una muestra nueva?
> No. Puedes muestrear z del prior y decodificar. Codificar un dato se utiliza en reconstrucción e inferencia del latente.

> [!question]- ¿La KL es una distancia simétrica?
> No. Aunque es no negativa, en general KL(q‖p) no coincide con KL(p‖q).


> [!question]- ¿Qué significa inferencia amortizada?
> Entrenar una función compartida, el codificador, para aproximar la posterior de distintos datos sin resolver desde cero una búsqueda separada para cada uno.

> [!question]- ¿Qué ELBO es mejor: −7 o −9?
> −7, porque se maximiza la ELBO. Si se minimiza su negativo, 7 es mejor que 9.
