---
title: Variables aleatorias, distribuciones, esperanza y CLT
tags:
  - master/matematicas-programacion
  - probabilidad
  - distribuciones
  - clt
---

# Variables aleatorias, distribuciones, esperanza y CLT

![[../assets/ruta maestra ia/03-clt-medias.gif|900]]

## Variable aleatoria

Una variable aleatoria es una función que asigna un número a cada resultado del proceso. No significa “un número que cambia caprichosamente”.

Ejemplos:

- $Y\in\{0,1\}$ indica sesión legítima o impostora;
- $N\in\{0,1,2,\ldots\}$ cuenta clics;
- $T\ge0$ mide duración;
- $X\in\mathbb R^D$ reúne características.

## Distribuciones esenciales

| Distribución | Qué modela | Parámetro | Media |
|---|---|---|---|
| Bernoulli | un evento binario | $p$ | $p$ |
| binomial | éxitos en $n$ intentos | $n,p$ | $np$ |
| categórica | una clase entre $K$ | $p_1,\ldots,p_K$ | vector de probabilidades |
| normal | variación continua alrededor de una media | $\mu,\sigma^2$ | $\mu$ |
| exponencial | espera entre eventos bajo tasa constante | $\lambda$ | $1/\lambda$ |

## Esperanza: promedio de largo plazo

Para una variable discreta:

$$E[X]=\sum_x x\,P(X=x).$$

Si $X$ vale 0 con probabilidad 0.7 y 1 con probabilidad 0.3:

$$E[X]=0(0.7)+1(0.3)=0.3.$$

Esto no dice que una observación valga 0.3; resume muchas repeticiones.

## Varianza: distancia cuadrática respecto de la media

$$\operatorname{Var}(X)=E[(X-\mu)^2]=E[X^2]-\mu^2.$$

La desviación estándar $\sigma$ vuelve a las unidades originales:

$$\sigma=\sqrt{\operatorname{Var}(X)}.$$

## Covarianza y correlación

$$\operatorname{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])].$$

- positiva: tienden a moverse en el mismo sentido;
- negativa: tienden a moverse en sentidos opuestos;
- cercana a cero: no hay relación lineal clara.

La correlación normaliza unidades:

$$\rho_{XY}=\frac{\operatorname{Cov}(X,Y)}{\sigma_X\sigma_Y}.$$

> [!warning] Cero correlación no implica independencia
> Si $X$ es simétrica y $Y=X^2$, la relación es determinista aunque la correlación lineal pueda ser cero.

## Media muestral y error estándar

Con observaciones independientes $X_1,\ldots,X_n$:

$$\bar X=\frac1n\sum_{i=1}^nX_i,$$

$$\operatorname{Var}(\bar X)=\frac{\sigma^2}{n},\qquad
SE(\bar X)=\frac{\sigma}{\sqrt n}.$$

Duplicar $n$ no divide el error por dos. Para reducirlo a la mitad hace falta cuadruplicar el número de unidades independientes.

## Ley de los grandes números

Al crecer $n$, la media muestral se acerca a la esperanza bajo condiciones apropiadas:

$$\bar X_n\xrightarrow[]{P}\mu.$$

No afirma que una muestra pequeña sea exacta ni que desaparezca el sesgo de muestreo.

## Teorema central del límite

La media estandarizada se aproxima a una normal:

$$\frac{\bar X-\mu}{\sigma/\sqrt n}\Rightarrow\mathcal N(0,1).$$

El CLT describe la **distribución de la media**, no obliga a que los datos individuales sean normales.

```mermaid
flowchart LR
    A[Distribución original] --> B[Tomar muchas muestras de tamaño n]
    B --> C[Calcular una media por muestra]
    C --> D[Distribución de medias]
    D --> E[Se concentra cerca de mu]
```

## Monte Carlo

Cuando una cantidad es una esperanza, podemos aproximarla simulando:

$$E[g(X)]\approx\frac1M\sum_{m=1}^M g(X^{(m)}).$$

El error típico decrece como $1/\sqrt M$. Simular 100 veces más reduce aproximadamente diez veces el error aleatorio.

## Conexión con mini-batch

El gradiente de un mini-batch es un estimador del gradiente poblacional. Lotes pequeños suelen tener mayor varianza; lotes grandes son más estables pero cuestan más memoria y pueden reducir la diversidad de actualizaciones.

## Autoevaluación

1. ¿Por qué la esperanza de Bernoulli es $p$?
2. ¿Qué unidades tiene la varianza y cuáles la desviación estándar?
3. ¿Qué distribuye aproximadamente el CLT?
4. ¿Por qué duplicar filas del mismo usuario no duplica información independiente?

---

Anterior: [[01 Eventos, probabilidad condicional, independencia y Bayes]] · Siguiente: [[03 Verosimilitud, entropía, cross-entropy y KL]]
