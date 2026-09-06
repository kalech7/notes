---
title: Autodiferenciación con micrograd y PyTorch
tags:
  - master/matematicas-programacion
  - autodiferenciacion
  - micrograd
  - pytorch
related:
  - "[[00 Índice - Gradientes, autodiferenciación y optimización]]"
  - "[[poo ia/05 Scalar y autodiferenciación]]"
---

# Autodiferenciación con micrograd y PyTorch

## Idea central

<code>torch.autograd</code> es el motor de **diferenciación automática** de PyTorch. Su funcionamiento puede resumirse en una frase:

> [!summary]
> **Autograd recuerda cómo se calculó la pérdida y después recorre esas operaciones al revés para determinar cuánto influyó cada parámetro.**

El proceso completo es:

$$
\text{parámetros entrenables}
\xrightarrow{\text{forward}}
\text{pérdida con historial}
\xrightarrow{\text{backward}}
\text{gradientes}
\xrightarrow{\text{optimizer.step()}}
\text{parámetros actualizados}.
$$

Cada etapa tiene una responsabilidad diferente:

| Etapa | Qué hace |
|---|---|
| forward | calcula la predicción y la pérdida; además construye el grafo |
| <code>backward()</code> | aplica la regla de la cadena y calcula gradientes |
| <code>step()</code> | utiliza los gradientes para modificar los parámetros |
| <code>zero_grad()</code> | prepara los acumuladores para una iteración nueva |

> [!tip] Frase para recordarlo
> **Autograd registra y deriva; el optimizador actualiza.**

## Ejemplo mínimo: calcular y recordar

```python
import torch

w = torch.tensor(1.0, requires_grad=True)
loss = 0.5 * (w - 3.0) ** 2

print(w.is_leaf)       # True
print(loss.item())     # 2.0
print(loss.grad_fn)    # operación que conecta loss con su historia
```

La pérdida es:

$$
L=\frac12(w-3)^2.
$$

Para $w=1$:

$$
L=\frac12(1-3)^2=2.
$$

PyTorch no guarda solamente el resultado $2$. Como <code>w</code> tiene <code>requires_grad=True</code>, también registra las operaciones ejecutadas:

```text
w → restar 3 → elevar al cuadrado → multiplicar por 0.5 → loss
```

Ese historial de dependencias forma un **grafo computacional dinámico**: se crea durante la ejecución concreta del forward.

### Recorrer el cálculo al revés

```python
loss.backward()
print(w.grad)  # tensor(-2.)
```

<code>backward()</code> calcula:

$$
\frac{\partial L}{\partial w}.
$$

Como:

$$
L=\frac12(w-3)^2,
$$

entonces:

$$
\frac{\partial L}{\partial w}=w-3.
$$

En $w=1$:

$$
\frac{\partial L}{\partial w}=-2.
$$

### Cómo interpretar el gradiente

El valor $-2$ no es una nueva pérdida ni una modificación automática del peso. Indica cómo cambiaría aproximadamente la pérdida ante una variación pequeña de $w$:

$$
\Delta L
\approx
\frac{\partial L}{\partial w}\Delta w.
$$

Si aumentamos $w$ en $0.01$:

$$
\Delta L\approx(-2)(0.01)=-0.02.
$$

Por tanto, cerca del punto actual, aumentar ligeramente $w$ reduce la pérdida. El gradiente proporciona **dirección y sensibilidad**, pero todavía no cambia el parámetro.

## Qué son las hojas

Las **hojas** (*leaf tensors*) son los tensores situados al comienzo del grafo. En entrenamiento, normalmente son los pesos y sesgos creados directamente por el usuario o por una capa del modelo.

```python
w = torch.tensor(1.0, requires_grad=True)

print(w.is_leaf)  # True
print(w.grad_fn)  # None
```

<code>w</code> es una hoja porque no fue producido por otra operación registrada. En cambio:

```python
loss = 0.5 * (w - 3.0) ** 2

print(loss.is_leaf)  # False
print(loss.grad_fn)  # operación que produjo loss
```

<code>loss</code> no es una hoja porque es el resultado de varias operaciones.

```text
w                                      ← hoja entrenable
│
└─ resta → cuadrado → multiplicación → loss
                                      ← tensor intermedio/final
```

Por defecto, <code>backward()</code> acumula el resultado en <code>.grad</code> de las **hojas entrenables**. Los tensores intermedios participan en la regla de la cadena, pero PyTorch normalmente no conserva su <code>.grad</code> después del recorrido.

> [!note] Matiz importante
> PyTorch también considera hojas a los tensores que no requieren gradiente. Sin embargo, cuando se habla de entrenamiento, normalmente “hoja” se refiere a una hoja con <code>requires_grad=True</code>, porque allí se acumularán los gradientes de los parámetros.

## Qué significa <code>requires_grad=True</code>

Esta propiedad le dice a PyTorch:

> Registra las operaciones relacionadas con este tensor porque después necesitaré derivar una salida respecto de él.

No significa que el gradiente ya exista:

```python
w = torch.tensor(1.0, requires_grad=True)
print(w.grad)  # None
```

El acumulador recibe un valor después de <code>backward()</code>:

```python
loss = 0.5 * (w - 3.0) ** 2
loss.backward()
print(w.grad)  # tensor(-2.)
```

| Elemento | Significado |
|---|---|
| <code>requires_grad=True</code> | solicita registrar las operaciones necesarias para derivar |
| <code>is_leaf=True</code> | el tensor está al comienzo del grafo |
| <code>grad_fn</code> | operación que produjo un tensor no hoja |
| <code>.grad</code> | acumulador del gradiente de una hoja entrenable |
| <code>backward()</code> | inicia el recorrido inverso desde la salida |

## Qué automatiza y qué no

Autodiferenciación no “adivina” la función ni el objetivo. Registra las operaciones que ejecutaste y compone sus derivadas locales mediante la regla de la cadena.

Tú decides:

- qué modelo construir;
- qué pérdida escalar usar;
- qué tensores son entrenables;
- cuándo reiniciar los gradientes;
- cuándo ejecutar el forward, el backward y la actualización.

Autograd decide:

- cómo recorrer el grafo;
- qué reglas locales utilizar;
- cómo combinar las contribuciones que llegan por diferentes rutas.

| Autograd sí hace | Autograd no hace |
|---|---|
| registra operaciones cuando corresponde | no decide qué modelo construir |
| construye el grafo del forward ejecutado | no elige la función de pérdida |
| aplica la regla de la cadena | no selecciona la tasa de aprendizaje |
| acumula gradientes en <code>.grad</code> | no actualiza los parámetros |

## Autodiferenciación no es diferenciación numérica ni simbólica

| Método | Cómo trabaja | Resultado | Principal límite |
|---|---|---|---|
| diferencias finitas | perturba una entrada y vuelve a evaluar | aproximación | depende de la perturbación y requiere muchas evaluaciones |
| derivación simbólica | manipula expresiones algebraicas | fórmula derivada | la expresión puede crecer mucho y no sigue naturalmente el control de flujo ejecutado |
| autodiferenciación | registra operaciones elementales y compone sus reglas | derivada del programa ejecutado, salvo redondeo | solo conoce las operaciones conectadas en el grafo |

Por ejemplo, las diferencias finitas estimarían:

$$
\frac{\partial L}{\partial w}
\approx
\frac{L(w+h,b)-L(w,b)}{h}.
$$

Autograd no necesita elegir $h$. Utiliza las derivadas conocidas de sumar, multiplicar, elevar al cuadrado y las demás operaciones, y luego aplica la regla de la cadena.

Las diferencias finitas no compiten con autograd: sirven para **auditarlo**. Cómo se elige $h$, por qué se divide entre $2h$ y por qué una $h$ diminuta destruye la estimación se desarrolla en [[13 Verificación de gradientes con diferencias finitas]].
El ejemplo completo del Control de lectura 3, con sus tablas y respuestas, está en [[14 Control de lectura 3 - el experimento resuelto y explicado]].

> [!tip] Por qué se utiliza el modo inverso
> Durante el entrenamiento hay una pérdida escalar y muchísimos parámetros. Un único recorrido inverso permite reutilizar sensibilidades para calcular todas las componentes del gradiente.

## Micrograd: hacer visible el proceso

Micrograd implementa el mismo principio con valores escalares y permite inspeccionar directamente el grafo:

```python
from micrograd.engine import Value

x = Value(2.0)
y = Value(5.0)
w = Value(1.0)
b = Value(0.0)

u = w * x
y_hat = u + b
r = y_hat - y
q = r ** 2
loss = 0.5 * q

loss.backward()

print(loss.data)  # 4.5
print(w.grad)     # -6.0
print(b.grad)     # -3.0
```

El modelo es:

$$
\hat y=wx+b.
$$

Con $x=2$, $y=5$, $w=1$ y $b=0$, el forward produce:

$$
u=wx=(1)(2)=2,
$$

$$
\hat y=u+b=2,
$$

$$
r=\hat y-y=2-5=-3,
$$

$$
L=\frac12r^2=\frac12(-3)^2=4.5.
$$

El grafo conserva la ruta completa:

```text
w ─┐
   ├─ multiplicar → u ─┐
x ─┘                    ├─ sumar → y_hat → restar y → r → cuadrado → loss
b ─────────────────────┘
```

Durante el backward:

$$
\frac{\partial L}{\partial b}=r=-3,
$$

$$
\frac{\partial L}{\partial w}=rx=(-3)(2)=-6.
$$

Cada <code>Value</code> hace observables cuatro elementos:

| Elemento | Significado |
|---|---|
| valor | resultado obtenido durante el forward |
| padres | nodos de los que depende |
| operación | regla local que produjo el nodo |
| gradiente | sensibilidad acumulada durante el backward |

> [!warning] Coincidir no basta
> Ver <code>w.grad == -6</code> comprueba el resultado, pero comprenderlo exige poder reconstruir la ruta $L\to q\to r\to\hat y\to u\to w$. Esta es la misma estructura estudiada en [[03 Grafo computacional y backpropagation#Por qué descomponer el cálculo|la derivación manual]].

## PyTorch: ejemplo por lotes

Ahora usamos tres observaciones a la vez:

```python
import torch

X = torch.tensor([[1.], [2.], [3.]])
y = torch.tensor([3., 5., 7.])
w = torch.tensor([1.], requires_grad=True)
b = torch.tensor(0., requires_grad=True)

y_hat = X @ w + b
residual = y_hat - y
loss = 0.5 * torch.mean(residual ** 2)

loss.backward()

print(loss.item())  # 4.833333...
print(w.grad)       # tensor([-6.6667])
print(b.grad)       # tensor(-3.)
```

El modelo es:

$$
\hat y_i=x_iw+b.
$$

Con $w=1$ y $b=0$:

$$
\hat y=[1,2,3].
$$

Como $y=[3,5,7]$, los residuos son:

$$
r=\hat y-y=[-2,-3,-4].
$$

La pérdida vale:

$$
L=\frac12\operatorname{mean}(r^2)
=\frac12\left(\frac{4+9+16}{3}\right)
=\frac{29}{6}
\approx4.8333.
$$

### Gradiente del sesgo

Cada predicción depende de $b$ con derivada $1$, por lo que:

$$
\frac{\partial L}{\partial b}
=\frac{-2-3-4}{3}
=-3.
$$

### Gradiente del peso

Cada predicción depende de $w$ mediante su entrada $x_i$:

$$
\frac{\partial L}{\partial w}
=\frac{(-2)(1)+(-3)(2)+(-4)(3)}{3}
=-\frac{20}{3}
\approx-6.6667.
$$

### Dónde queda cada cosa

| Tensor | ¿Hoja? | <code>grad_fn</code> | Después de <code>backward()</code> |
|---|---:|---|---|
| <code>w</code> | sí | <code>None</code> | <code>w.grad = -20/3</code> |
| <code>b</code> | sí | <code>None</code> | <code>b.grad = -3</code> |
| <code>y_hat</code> | no | operación registrada | conecta el forward |
| <code>loss</code> | no | operación registrada | escalar que inicia el backward |

```python
assert w.is_leaf and b.is_leaf
assert w.grad_fn is None and b.grad_fn is None
assert loss.shape == torch.Size([])
assert loss.grad_fn is not None
```

## Acumular no es reiniciar

PyTorch **suma** los gradientes que llegan a una hoja. Esto permite combinar contribuciones procedentes de varias rutas o de varios recorridos.

```python
w = torch.tensor(1.0, requires_grad=True)
loss = 0.5 * (w - 3.0) ** 2

loss.backward(retain_graph=True)
print(w.grad)  # tensor(-2.)

loss.backward()
print(w.grad)  # tensor(-4.): añadió otra contribución de -2
```

En un ciclo de entrenamiento hay que preparar los acumuladores antes de la siguiente iteración:

```python
optimizer.zero_grad(set_to_none=True)
```

### <code>None</code> frente a cero

- <code>None</code>: todavía no existe una contribución en ese recorrido;
- tensor de ceros: existe un acumulador y su valor actual es cero.

> [!warning] Interpretación de <code>None</code>
> <code>.grad is None</code> no significa necesariamente “la derivada matemática es cero”. Puede indicar que todavía no hubo backward, que se reinició el acumulador o que el parámetro no estaba conectado a la pérdida.

## Actualizar sin registrar la actualización

Después del backward se puede realizar manualmente un paso de descenso del gradiente:

```python
eta = 0.1

with torch.no_grad():
    w -= eta * w.grad
    b -= eta * b.grad
```

La regla general es:

$$
\theta_{\text{nuevo}}
=\theta_{\text{actual}}
-\eta\frac{\partial L}{\partial\theta}.
$$

Por ejemplo, si $w=1$, $\eta=0.1$ y $\partial L/\partial w=-2$:

$$
w_{\text{nuevo}}=1-0.1(-2)=1.2.
$$

El peso aumenta porque el gradiente negativo indica que, localmente, aumentar $w$ reduce la pérdida.

<code>torch.no_grad()</code> evita que la propia actualización del parámetro se registre como una operación del siguiente grafo. En un ciclo normal:

```python
optimizer.step()
```

delega la actualización al optimizador.

## Ciclo completo de entrenamiento

```python
optimizer.zero_grad(set_to_none=True)  # 1. preparar acumuladores

y_hat = model(X)                       # 2. forward
loss = criterio(y_hat, y)              #    calcular pérdida

loss.backward()                        # 3. calcular gradientes
optimizer.step()                       # 4. actualizar parámetros
```

> [!summary] Tres verbos distintos
> <code>zero_grad()</code> prepara acumuladores; <code>backward()</code> calcula gradientes; <code>step()</code> consume esos gradientes y cambia los parámetros.

## Ciclo visual de autograd

![[assets/10-ciclo-autograd.png|1000]]

### Cómo leer los estados

| Momento | Qué existe | Qué debes inspeccionar |
|---|---|---|
| después de crear $w$ y $b$ | hojas entrenables | <code>requires_grad=True</code>, <code>is_leaf=True</code>, <code>.grad is None</code> |
| después del forward | valores e historial | la pérdida tiene <code>grad_fn</code>, pero las hojas todavía no recibieron un gradiente nuevo |
| después de <code>backward()</code> | gradientes acumulados | <code>w.grad</code> y <code>b.grad</code> tienen la forma de sus parámetros |
| después de <code>step()</code> | parámetros modificados | compara copias anteriores y posteriores; <code>.grad</code> no se limpia automáticamente |
| después de <code>zero_grad(set_to_none=True)</code> | acumuladores preparados | <code>.grad is None</code> hasta el siguiente backward |

## Cómo auditar autograd

Antes de confiar en un resultado:

1. comprueba que la pérdida sea escalar;
2. identifica las hojas entrenables;
3. inspecciona <code>requires_grad</code>, <code>is_leaf</code> y <code>grad_fn</code>;
4. predice al menos el signo de cada gradiente;
5. verifica que <code>.grad</code> tenga la misma forma que su parámetro;
6. confirma que los parámetros estaban conectados a la pérdida;
7. registra el cambio de parámetros después de <code>step()</code>;
8. recuerda reiniciar los acumuladores antes de la siguiente iteración.

---

Anterior: [[03 Grafo computacional y backpropagation]] · Siguiente: [[05 Lotes, reducción y formas del gradiente]]
