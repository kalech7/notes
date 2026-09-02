---
title: Tasa de aprendizaje, curvatura y estabilidad
tags:
  - master/matematicas-programacion
  - descenso-de-gradiente
  - estabilidad
  - curvatura
related:
  - "[[00 Índice - Gradientes, autodiferenciación y optimización]]"
  - "[[espectro svd y rango bajo/02 Autovalores, autovectores y espectro]]"
---

# Tasa de aprendizaje, curvatura y estabilidad

## La tasa no controla solo la velocidad

En descenso de gradiente:

$$\theta_{t+1}=\theta_t-\eta\nabla L(\theta_t),$$

$\eta$ es la tasa de aprendizaje. Es tentador pensar que aumentarla solo produce pasos más grandes. En realidad puede cambiar la dinámica de monótona a oscilatoria y de convergente a divergente.

## Caso cuadrático unidimensional

Sea:

$$
L(\theta)=\frac a2(\theta-\theta^*)^2,
\qquad a>0.
$$

**Qué representa $a$:** curvatura constante. Una $a$ grande hace que la pendiente cambie más rápidamente al alejarse del mínimo.

Derivada:

$$L'(\theta)=a(\theta-\theta^*).$$

Aplicamos GD:

$$
\theta_{t+1}
=\theta_t-\eta a(\theta_t-\theta^*).
$$

Definimos el error firmado:

$$e_t=\theta_t-\theta^*.$$

Restamos $\theta^*$:

$$
\boxed{e_{t+1}=(1-\eta a)e_t}.
$$

Llamemos:

$$\rho=1-\eta a.$$

Entonces:

$$e_t=\rho^t e_0.$$

Toda la estabilidad está contenida en el signo y el módulo de $\rho$.

## Los cinco regímenes

| Tasa | Factor $\rho$ | Dinámica |
|---|---:|---|
| $0<\eta<1/a$ | $0<\rho<1$ | converge sin cambiar de lado |
| $\eta=1/a$ | $\rho=0$ | llega al mínimo en un paso exacto |
| $1/a<\eta<2/a$ | $-1<\rho<0$ | alterna de lado y converge |
| $\eta=2/a$ | $\rho=-1$ | oscila con magnitud constante |
| $\eta>2/a$ | $\rho<-1$ | oscila y diverge |

La condición exacta de convergencia es:

$$
|\rho|<1
\iff
|1-\eta a|<1
\iff
\boxed{0<\eta<\frac2a}.
$$

![[assets/01-regimenes-tasa-aprendizaje.png|1100]]

### Cómo leer el gráfico

- El eje vertical muestra error firmado, no pérdida.
- Cambiar de signo significa cruzar el mínimo.
- Disminuir en magnitud significa acercarse.
- Con $\rho=-1$, la secuencia se mueve, pero no aprende porque no se acerca.
- Con $|\rho|>1$, cada oscilación es mayor.

## Contraste reproducible

```python
def quadratic_gd(theta0, eta, a=4.0, steps=8):
    theta = float(theta0)
    trace = [theta]
    for _ in range(steps):
        grad = a * theta  # theta* = 0
        theta -= eta * grad
        trace.append(theta)
    return trace

for eta in (0.10, 0.25, 0.40, 0.50, 0.60):
    rho = 1 - 4 * eta
    trace = quadratic_gd(theta0=1.0, eta=eta)
    assert all(
        abs(trace[t + 1] - rho * trace[t]) < 1e-12
        for t in range(len(trace) - 1)
    )
    print(eta, rho, trace)
```

Primero clasifica usando $\rho$; después ejecuta para contrastar. Mirar la curva y bautizarla después no prueba que entendiste la causa.

## Varias dimensiones: cada dirección tiene su factor

Para una cuadrática:

$$
L(\theta)
=\frac12(\theta-\theta^*)^\mathsf{T}H(\theta-\theta^*),
\qquad H\succ0,
$$

$H$ es el **Hessiano**, la matriz de segundas derivadas:

$$
H_{ij}
=
\frac{\partial^2L}
{\partial\theta_i\,\partial\theta_j}.
$$

La diagonal describe curvatura por coordenada y los términos fuera de la diagonal describen cómo se acoplan dos coordenadas. Las direcciones propias de $H$ encuentran ejes donde ese acoplamiento desaparece y cada dirección evoluciona por separado.

Si $H v_i=\lambda_i v_i$ y $z_{i,t}$ es la componente del error sobre $v_i$:

$$
z_{i,t+1}=(1-\eta\lambda_i)z_{i,t}.
$$

Todas las direcciones deben ser estables:

$$
|1-\eta\lambda_i|<1
\quad\text{para todo }i.
$$

La mayor curvatura impone la restricción común:

$$
\boxed{0<\eta<\frac{2}{\lambda_{\max}(H)}}.
$$

## Por qué aparece el zigzag

En el gráfico siguiente:

$$\lambda_{\min}=1,\qquad \lambda_{\max}=6,\qquad\eta=0.28.$$

Los factores son:

$$
1-\eta\lambda_{\min}=0.72,
\qquad
1-\eta\lambda_{\max}=-0.68.
$$

La dirección suave conserva el signo; la dirección curva lo alterna. Ambas reducen magnitud, así que la trayectoria converge mientras zigzaguea.

![[assets/02-valle-curvatura-gd.png|950]]

> [!warning] Alcance
> La recurrencia y la cota anterior son exactas para una cuadrática con $H\succ0$. En funciones no cuadráticas, la curvatura cambia con la posición; el gráfico ofrece intuición local, no una ley universal.

## Consecuencias prácticas

- Escalar características puede reducir diferencias extremas de curvatura.
- Una tasa que funciona en una dirección puede ser inestable en otra.
- Reducir $\eta$ puede estabilizar, pero no corrige un grafo desconectado ni formas erróneas.
- Momentum y Adam cambian la regla dinámica; no anulan la necesidad de observar estabilidad.

## Qué, por qué, cómo y para qué

| Pregunta | Respuesta |
|---|---|
| ¿qué? | $\eta$ escala la transformación del gradiente en paso |
| ¿por qué importa? | determina el multiplicador efectivo del error |
| ¿cómo se analiza? | recurrencia del error y curvatura |
| ¿para qué? | anticipar convergencia, oscilación o divergencia |

---

Anterior: [[05 Lotes, reducción y formas del gradiente]] · Siguiente: [[07 Mini-batch y SGD como estimador]]
