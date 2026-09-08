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

## Qué es la tasa de aprendizaje

La **tasa de aprendizaje**, representada por $\eta$ (*eta*), es un número positivo que determina cuánto se escala el gradiente antes de cambiar los parámetros.

En descenso de gradiente:

$$
\underbrace{g_t=\nabla L(\theta_t)}_{\text{sensibilidad}},
\qquad
\underbrace{\Delta\theta_t=-\eta g_t}_{\text{paso}},
\qquad
\underbrace{\theta_{t+1}=\theta_t+\Delta\theta_t}_{\text{nuevo estado}}.
$$

El gradiente y la tasa tienen responsabilidades diferentes:

- el **signo y la dirección del gradiente** indican hacia dónde cambia la pérdida;
- la **tasa de aprendizaje** indica qué tan grande será el movimiento;
- el producto $-\eta g_t$ es el paso que realmente se suma a los parámetros.

> [!tip] Analogía
> El gradiente es una señal que dice “la bajada está hacia ese lado”. La tasa de aprendizaje es la longitud de la zancada. Una zancada diminuta avanza lentamente; una enorme puede saltar al otro lado del valle.

## Para qué sirve

La tasa sirve para controlar el compromiso entre:

1. **velocidad:** cuánto avanzan los parámetros en cada actualización;
2. **estabilidad:** si los pasos permanecen cerca de una trayectoria de descenso;
3. **precisión local:** el gradiente describe bien el entorno cercano, pero un paso enorme puede abandonar ese entorno;
4. **capacidad de aprendizaje:** con $\eta=0$ los parámetros no cambian; con una tasa extremadamente pequeña el entrenamiento puede parecer detenido.

Normalmente $\eta$ es un **[[00 Glosario visual - términos del entrenamiento#Hiperparámetro|hiperparámetro]]**: no lo calcula <code>backward()</code>. Lo eliges al configurar el optimizador y puede modificarse durante el entrenamiento mediante un *scheduler*.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
#                                              ^^^^^^
#                                      tasa de aprendizaje
```

## Schedulers: warmup y decaimiento

Una tasa no tiene que ser constante. Un **scheduler** define $\eta_t$ como función del paso. En modelos grandes es común separar dos fases:

1. **warmup:** la tasa comienza pequeña y crece hasta un máximo;
2. **decay:** después disminuye para hacer ajustes progresivamente más finos.

Un warmup lineal de $W$ pasos puede escribirse como:

$$
\eta_t=\eta_{\max}\frac{t}{W},
\qquad 0\le t\le W.
$$

Después puede usarse, por ejemplo, decaimiento coseno hasta $\eta_{\min}$ durante un total de $T$ pasos:

$$
\eta_t
=\eta_{\min}
+\frac12(\eta_{\max}-\eta_{\min})
\left[1+\cos\left(\pi\frac{t-W}{T-W}\right)\right],
\qquad W<t\le T.
$$

### Por qué ayuda el warmup

Al inicio, representaciones, gradientes y momentos del optimizador todavía atraviesan un transitorio. Aplicar inmediatamente la tasa máxima puede producir una actualización grande basada en estadísticas poco estabilizadas. Warmup limita cuánto pueden mover los primeros lotes y facilita alcanzar el régimen de entrenamiento previsto.

Esto puede reducir la influencia desproporcionada de los primeros ejemplos, pero **no corrige por sí solo el orden de los datos**: siguen siendo necesarios muestreo, mezcla y lotes representativos. Tampoco rescata una $\eta_{\max}$ absurda, una inicialización defectuosa o una pérdida mal escalada.

### Para qué sirve el decaimiento

Al principio conviene recorrer distancia; cerca de una región útil conviene reducir el ruido de las actualizaciones y evitar rebotar alrededor de soluciones. El decay cambia esa escala temporalmente, pero no decide la dirección: esa sigue viniendo del gradiente y del estado del optimizador.

> [!question]- ¿Warmup es lo mismo que usar siempre una tasa pequeña?
> No. Warmup protege una fase inicial y luego permite llegar a una tasa pico capaz de avanzar con rapidez. Una tasa pequeña constante puede permanecer segura pero avanzar demasiado lento durante todo el entrenamiento. Lo importante es interpretar la **curva completa $\eta_t$**, su unidad —pasos o tokens— y cómo interactúa con batch, optimizador y duración total.

## Cómo interpretar un valor como $\eta=0.1$

$\eta=0.1$ **no significa** “aprender el $10\%$”, “reducir la pérdida un $10\%$” ni “moverse un $10\%$ hacia el mínimo”. Significa: **multiplicar el gradiente por $0.1$ para construir el paso**.

Si el parámetro actual es $w=1$ y el gradiente es $g=-2$:

$$
\Delta w=-\eta g=-0.1(-2)=+0.2,
$$

$$
w_{\text{nuevo}}=1+0.2=1.2.
$$

El signo negativo del gradiente hizo que el paso fuera positivo. La tasa solo escaló su tamaño.

| Tasa | Gradiente | Paso $-\eta g$ | Interpretación inmediata |
|---:|---:|---:|---|
| $0$ | $-2$ | $0$ | no hay aprendizaje porque el parámetro no se mueve |
| $0.01$ | $-2$ | $+0.02$ | paso muy pequeño |
| $0.1$ | $-2$ | $+0.2$ | paso diez veces mayor que con $0.01$ |
| $0.8$ | $-2$ | $+1.6$ | paso grande; puede ser útil si la curvatura lo permite |
| $2.2$ | $-2$ | $+4.4$ | en el ejemplo visual se pasa del mínimo y la pérdida aumenta |

![[assets/17-tasa-aprendizaje-intuicion.png|1000]]

### Cómo leer el gráfico

- Los tres paneles comienzan exactamente en $w=1$, con pérdida $L=2$ y gradiente $g=-2$.
- El punto naranja es el estado inicial y la estrella es el mínimo.
- Solo cambia $\eta$; por eso las flechas tienen la misma dirección pero longitudes diferentes.
- Con $\eta=0.1$, la pérdida baja poco: el paso es seguro pero lento.
- Con $\eta=0.8$, el paso queda cerca del mínimo en una sola iteración.
- Con $\eta=2.2$, el parámetro salta demasiado lejos y la pérdida sube de $2$ a $2.88$.

> [!warning] No existe una tasa universal
> $0.1$ puede ser pequeña en un problema y enorme en otro. Su efecto depende de la escala de los datos, la definición de la pérdida, la curvatura, el optimizador y el tamaño del lote. Compara tasas solo dentro de un protocolo controlado.

## Por qué no controla solamente la velocidad

Es tentador pensar que aumentar $\eta$ solo produce pasos más grandes y rápidos. En realidad puede cambiar la dinámica de monótona a oscilatoria y de convergente a divergente. Para entender por qué, necesitamos estudiar cómo interactúa con la curvatura.

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

### Cómo interpretar $a$, $\eta$, $e_t$ y $\rho$

| Símbolo | Qué mide | Si aumenta |
|---|---|---|
| $a$ | curvatura de la pérdida | la pendiente cambia más rápido y la tasa estable máxima $2/a$ disminuye |
| $\eta$ | escala aplicada al gradiente | el paso crece, pero también aumenta el riesgo de cruzar repetidamente el mínimo o divergir |
| $e_t=\theta_t-\theta^*$ | distancia **firmada** al mínimo | el signo indica el lado; $|e_t|$ indica la distancia |
| $\rho=1-\eta a$ | factor que transforma un error en el siguiente | no se interpreta por ser “mayor”, sino por su signo y por si $|\rho|$ es menor, igual o mayor que $1$ |

Ejemplo: con $a=4$ y $\eta=0.4$, $\rho=1-4(0.4)=-0.6$. El signo negativo hace que el error cambie de lado; el módulo $0.6$ hace que conserve solo el $60\%$ de su tamaño anterior. Por eso oscila y converge.

## Tu imagen de $e_t$: separar posición, distancia y altura

![[assets/26-error-firmado-referencia.png|1100]]

### Léela en tres pasos

1. $\theta_t$ indica dónde estás en el eje horizontal; $\theta^*$ indica dónde está el mínimo.
2. $e_t=\theta_t-\theta^*$ dice cuánto y hacia qué lado te separas. A la izquierda es negativo; a la derecha es positivo. La distancia sin signo es $|e_t|$.
3. La altura es $L(\theta_t)=\frac a2e_t^2$. Dos errores $+3$ y $-3$ tienen la misma altura aunque estén en lados opuestos.

### Ejemplo que puedes seguir con el dedo

Usa $a=4$, $\theta^*=2$, $\theta_0=7$ y $\eta=0.4$. Entonces $e_0=5$ y $\rho=1-4(0.4)=-0.6$.

| Iteración $t$ | Error $e_t$ | Parámetro $\theta_t=2+e_t$ | Pérdida $2e_t^2$ |
|---:|---:|---:|---:|
| 0 | 5 | 7 | 50 |
| 1 | -3 | -1 | 18 |
| 2 | 1.8 | 3.8 | 6.48 |
| 3 | -1.08 | 0.92 | 2.3328 |

La posición salta a ambos lados, pero la distancia se reduce. La pérdida **no alterna de signo**: es no negativa y, en este ejemplo, se multiplica por $\rho^2=0.36$ en cada paso.

> [!note] Cómo interpretar el recuadro de divergencia de la referencia
> La imagen también muestra $\rho>1$ como caso general de una recurrencia. Para esta cuadrática con $a>0$ y descenso con $\eta>0$, siempre $\rho=1-\eta a<1$: la divergencia por una tasa positiva excesiva ocurre con $\rho<-1$. Con $\eta=0$, $\rho=1$ y no hay movimiento. Con $\rho=-1$ hay oscilación sin acercamiento; con $\rho=0$ se llega al mínimo en un paso exacto.

Fuente: [[assets/guia_estudiante_m08_gradientes_autodiferenciacion_optimizacion.pdf#page=21|Guía M08, páginas 21–24]].

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

### Cómo leer el valle

- Cada óvalo es una curva de igual pérdida.
- La dirección vertical tiene curvatura $6$: el gradiente cambia con mayor intensidad y el paso cruza el valle.
- El factor $-0.68$ indica cambio de lado y contracción al $68\%$ en esa dirección.
- La dirección horizontal tiene factor $0.72$: conserva el lado y avanza más lentamente.
- El zigzag no significa por sí mismo divergencia; importa si la distancia al mínimo disminuye.

> [!warning] Alcance
> La recurrencia y la cota anterior son exactas para una cuadrática con $H\succ0$. En funciones no cuadráticas, la curvatura cambia con la posición; el gráfico ofrece intuición local, no una ley universal.

## Tu imagen de curvatura: la misma tasa no da el mismo comportamiento

![[assets/25-curvatura-referencia.png|1100]]

### Qué mirar en cada panel

El panel izquierdo muestra un valle con dos direcciones principales. La sección azul es ancha: su curvatura $\lambda_1$ es pequeña. La roja es estrecha: su curvatura $\lambda_2$ es mayor. Los paneles de la derecha cortan ese valle para estudiar una dirección a la vez.

En esos ejes principales:

$$L(z_1,z_2)=\frac12(\lambda_1z_1^2+\lambda_2z_2^2),\qquad z_{i,t+1}=(1-\eta\lambda_i)z_{i,t}.$$

$z_i$ es la componente de la posición respecto al mínimo en una dirección propia del Hessiano; no es la altura de la superficie. Los autovalores $\lambda_i$ miden la curvatura en esas direcciones.

Prueba $\lambda_1=1$, $\lambda_2=6$, $\eta=0.28$, empezando en $(z_1,z_2)=(1,1)$:

- En azul, el factor es $0.72$: $1\to0.72\to0.5184$. Se acerca sin cruzar el cero.
- En rojo, el factor es $-0.68$: $1\to-0.68\to0.4624$. Cruza de lado, pero cada vez está más cerca.

**«Misma zancada» en el dibujo significa misma tasa $\eta$, no igual distancia recorrida.** El paso real en cada dirección es $-\eta\lambda_i z_i$; depende también de la pendiente. Una curva más cerrada cambia antes de signo su factor al aumentar la tasa.

El límite conjunto es $\eta<2/6\approx0.3333$. Si subes a $\eta=0.4$, la dirección suave aún tiene factor $0.6$, pero la estrecha tiene $-1.4$ y se aleja. Para garantizar convergencia desde cualquier posición inicial, todas las direcciones deben contraerse. Si una componente inicial es exactamente cero, esa dirección no se excita en la recurrencia ideal, pero la cota general sigue protegiendo frente a perturbaciones en ella.

Fuente: [[assets/guia_estudiante_m08_gradientes_autodiferenciacion_optimizacion.pdf#page=23|Guía M08, página 23]]. Imagen de referencia aportada por ti.

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


## Preguntas con respuesta desplegable

Haz clic en cada pregunta después de intentar responder.

> [!question]- Con $\rho=-0.6$, ¿diverge porque cambia de signo?
> No. Cambia de lado porque $\rho<0$, pero se acerca porque $|\rho|=0.6<1$.

> [!question]- Si $e_t=-3$ y $a=4$, ¿cuánto vale la pérdida?
> $L=\frac42(-3)^2=18$. El error es negativo; la pérdida no.

> [!question]- Con curvaturas 1 y 6, ¿es estable $\eta=0.4$ desde cualquier inicio?
> No. El factor de la dirección de curvatura 6 es $1-0.4(6)=-1.4$, cuya magnitud supera uno.

> [!question]- ¿Misma tasa significa mismo tamaño de paso?
> No. El paso es tasa por gradiente; la pendiente puede ser diferente por dirección y posición.

---

Anterior: [[05 Lotes, reducción y formas del gradiente]] · Siguiente: [[07 Mini-batch y SGD como estimador]]
