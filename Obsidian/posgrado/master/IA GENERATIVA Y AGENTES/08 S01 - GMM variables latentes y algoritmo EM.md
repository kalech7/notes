---
title: "08 S01 - GMM variables latentes y algoritmo EM"
tags:
  - maestria/ia-generativa
  - estudio
---

# 08 S01 - GMM variables latentes y algoritmo EM

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[sesion-01.pdf#page=13|Sesión 01, páginas 13]]. Explicaciones y ejemplos elaborados para estudiar; no son una transcripción.

## El problema: una nube con varios grupos

Imagina puntos que describen duración y tamaño de archivos. Hay varios grupos, pero no tienes etiquetas que indiquen el grupo de cada archivo. Una sola campana gaussiana podría representar mal toda la nube.

Un **modelo de mezcla de gaussianas (GMM)** combina varias distribuciones:

$$p(x)=\sum_{k=1}^{K}\pi_k\mathcal N(x\mid\mu_k,\Sigma_k).$$

- K: número de componentes de la mezcla.
- $\pi_k$: peso del componente k; los pesos suman 1.
- $\mu_k$: centro de su nube.
- $\Sigma_k$: matriz de covarianza; controla dispersión y orientación.
- $\mathcal N$: densidad gaussiana.

Un componente no equivale necesariamente a una categoría real. Es una parte de la representación estadística.

## Qué es la variable latente

Observas el punto x, pero no qué componente z lo produjo. Esa identidad es latente. El modelo supone un proceso: elegir componente y después generar un punto dentro de él.

Para obtener $p(x)$ sumamos todas las explicaciones posibles:

$$p(x)=\sum_z p(z)p(x\mid z).$$

Esta operación es **marginalizar**. No escogemos obligatoriamente un único grupo para calcular la densidad de un punto.

## Responsabilidades: Bayes vuelve a aparecer

La responsabilidad del componente k sobre el punto $x_i$ es:

$$\gamma_{ik}=P(z_i=k\mid x_i)=
\frac{\pi_k\mathcal N(x_i\mid\mu_k,\Sigma_k)}
{\sum_j\pi_j\mathcal N(x_i\mid\mu_j,\Sigma_j)}.$$

Supón dos pesos 0.6 y 0.4, y densidades en un punto de 0.2 y 0.1. Las contribuciones son 0.12 y 0.04. Al normalizar: responsabilidades 0.75 y 0.25.

La densidad 0.2 no es «20 % de probabilidad de ese punto». Lo que sí son probabilidades normalizadas son las responsabilidades del componente discreto.

## Por qué se necesita EM

Si supiéramos los grupos, estimaríamos centros y dispersiones. Si supiéramos centros y dispersiones, calcularíamos qué grupos explican cada punto. EM resuelve esa dependencia alternando pasos.

1. **Inicialización:** proponer parámetros iniciales.
2. **Paso E, esperanza:** mantener parámetros fijos y calcular responsabilidades.
3. **Paso M, maximización:** mantener responsabilidades fijas y recalcular parámetros.
4. Repetir hasta un criterio de parada.

Por ejemplo, la nueva media es un promedio ponderado:

$$N_k=\sum_{i=1}^{N}\gamma_{ik},\qquad
\mu_k^{\mathrm{nuevo}}=\frac{\sum_i\gamma_{ik}x_i}{N_k},\qquad
\pi_k^{\mathrm{nuevo}}=\frac{N_k}{N}.$$

N representa aquí la cantidad de observaciones. Un punto contribuye más al centro del componente que mejor lo explica. La covarianza también se recalcula ponderando por esas responsabilidades.

## Generar es distinto de asignar grupos

Una vez entrenado:

1. Muestrea z con probabilidades $\pi_1,\ldots,\pi_K$.
2. Muestrea x de la gaussiana elegida.

Así se obtienen puntos nuevos. No se limita a devolver observaciones del conjunto de entrenamiento. La función `gmm.sample()` mencionada en la sesión implementa este tipo de muestreo.

## Límites que conviene recordar

EM puede terminar en soluciones locales; la inicialización importa. En mezclas gaussianas sin restricciones puede haber degeneraciones cuando una covarianza colapsa alrededor de un dato. Regularizar covarianzas y comparar inicializaciones son medidas habituales.

El GMM estándar de esta sesión modela puntos independientes, no el orden de una secuencia. Para incorporar evolución temporal pasamos a [[09 S01 - Markov HMM y generación con bigramas]].

## Complemento del libro: hacer un paso M a mano

Bishop presenta las medias de EM como promedios ponderados. Supón tres observaciones unidimensionales: 0, 2 y 10. Después del paso E, las responsabilidades del primer componente son 0.9, 0.8 y 0.1.

Su cantidad efectiva de observaciones es $N_1=0.9+0.8+0.1=1.8$. La nueva media es:

$$\mu_1=\frac{0.9(0)+0.8(2)+0.1(10)}{1.8}=\frac{2.6}{1.8}\approx1.444.$$

El nuevo peso es $\pi_1=1.8/3=0.6$. Los puntos no se cuentan obligatoriamente como «dentro» o «fuera»: pueden contribuir parcialmente.

Para el segundo componente, las responsabilidades complementarias son 0.1, 0.2 y 0.9. Su media es $9.4/1.2\approx7.833$ y su peso 0.4. Esto ilustra por qué se habla de asignaciones suaves.

No has terminado de entrenar: ahora los centros, pesos y covarianzas actualizados cambian las responsabilidades del siguiente paso E. La repetición busca mejorar la verosimilitud, no fijar de una vez una etiqueta definitiva.

Una diferencia conceptual útil con K-means: en su formulación estándar, cada punto se asigna a un centro; en un GMM se calcula cuánto lo explica cada componente, incorporando pesos y dispersiones.

**Fuente de las actualizaciones:** [[bishop-2006-prml.pdf#page=459|Bishop, §9.2.2, p. impresa 439; PDF 459]]. Números elegidos para esta nota.

## Gráficos y diagramas para entender el tema

### Cómo se ve una mezcla de gaussianas

![Cómo se ve una mezcla de gaussianas](<Recursos visuales/04-gmm-componentes.png>)

**Cómo leerlo:** Los puntos grises son observaciones sintéticas; las cruces marcan medias de componentes. Las elipses muestran contornos de las gaussianas, no fronteras de clasificación ni intervalos de confianza. Un dato puede recibir responsabilidad de ambos componentes. Esta figura ilustra la familia del modelo; no es el resultado de un ajuste al material del curso.

### El ciclo de EM

![El ciclo de EM](<Recursos visuales/05-em-ciclo.png>)

**Cómo leerlo:** En E preguntas cuánto explica cada componente a cada dato. En M actualizas los parámetros con esas responsabilidades. La flecha de retorno recuerda que las nuevas medias y covarianzas cambian el siguiente paso E. El criterio de parada no demuestra que se alcanzó el mejor máximo global.

*Figuras originales elaboradas para estos apuntes. Los números y supuestos se explican en el texto; no son imágenes copiadas de los libros.*

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Qué se observa y qué es latente en el ejemplo?
> Se observan los puntos. La identidad del componente que generó cada punto no se observa y se infiere.

> [!question]- ¿Cómo se obtienen responsabilidades 0.75 y 0.25?
> Se multiplican peso y densidad: 0.12 y 0.04. Se divide cada contribución por 0.16.

> [!question]- ¿Qué mantiene fijo el paso E y qué mantiene fijo el M?
> E fija parámetros para inferir responsabilidades. M fija responsabilidades para reestimar parámetros.

> [!question]- ¿EM garantiza el mejor máximo global?
> No. Puede llegar a máximos locales o soluciones degeneradas según el modelo y la inicialización.

> [!question]- ¿Cómo genera un punto nuevo un GMM?
> Primero sortea un componente según sus pesos y luego un punto de la gaussiana de ese componente.


> [!question]- ¿Puede un componente tener 1.8 observaciones efectivas?
> Sí. Es la suma de responsabilidades, no un conteo de personas u objetos indivisibles.

> [!question]- ¿Cuánto vale la media del primer componente del ejemplo?
> 2.6/1.8≈1.444. Cada dato se pondera por la responsabilidad del componente.
