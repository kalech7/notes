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

## Qué automatiza y qué no

Autodiferenciación no “adivina” la función ni el objetivo. Registra las operaciones que ejecutaste y aplica sus reglas locales.

Tú decides:

- qué modelo construir;
- qué pérdida escalar usar;
- qué tensores son entrenables;
- cuándo reiniciar, propagar y actualizar.

El motor decide cómo recorrer el grafo y componer las derivadas.

## Autodiferenciación no es diferenciación numérica ni simbólica

| Método | Cómo trabaja | Resultado | Principal límite |
|---|---|---|---|
| diferencias finitas | perturba una entrada y vuelve a evaluar | aproximación | depende del tamaño de la perturbación y requiere muchas evaluaciones |
| derivación simbólica | manipula expresiones algebraicas | fórmula derivada | la expresión puede crecer y no sigue naturalmente control de flujo ejecutado |
| autodiferenciación | registra operaciones elementales y compone reglas exactas | derivada del programa ejecutado, salvo redondeo numérico | solo conoce las operaciones que quedaron conectadas en el grafo |

Por ejemplo, diferencias finitas estimaría:

$$
\frac{\partial L}{\partial w}
\approx
\frac{L(w+h,b)-L(w,b)}{h}.
$$

Autograd no necesita elegir $h$. Usa que multiplicar, sumar y elevar al cuadrado tienen derivadas locales conocidas y aplica la regla de la cadena sobre la ejecución concreta.

> [!tip] Por qué se usa modo inverso
> En entrenamiento existe una salida escalar y muchísimos parámetros. Un solo recorrido inverso reutiliza sensibilidades para calcular todas las componentes del gradiente.

## Micrograd: el mismo caso escalar

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

La evidencia vale porque el código conserva exactamente el DAG de [[03 Grafo computacional y backpropagation#Por qué descomponer el cálculo|la derivación manual]].

Cada <code>Value</code> hace observables cuatro elementos:

| Elemento | Significado |
|---|---|
| valor | resultado del forward |
| padres | dependencias del DAG |
| operación | regla local que produjo el nodo |
| gradiente | sensibilidad acumulada tras backward |

> [!warning] Coincidir no basta
> Ver <code>w.grad == -6</code> es una comprobación, pero comprender exige poder reconstruir la ruta $L\to q\to r\to\hat y\to u\to w$.

## PyTorch: hojas, operaciones y pérdida

Usamos el caso por lotes que se desarrollará en la siguiente nota:

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

### Dónde queda cada cosa

| Tensor | ¿Hoja? | <code>grad_fn</code> | Resultado esperado |
|---|---:|---|---|
| <code>w</code> | sí | <code>None</code> | <code>w.grad = -20/3</code> |
| <code>b</code> | sí | <code>None</code> | <code>b.grad = -3</code> |
| <code>y_hat</code> | no | operación registrada | conecta el forward |
| <code>loss</code> | no | operación registrada | escalar que inicia backward |

<code>loss.backward()</code> recorre el grafo, pero por defecto el resultado se acumula en <code>.grad</code> de las hojas entrenables.

```python
assert w.is_leaf and b.is_leaf
assert w.grad_fn is None and b.grad_fn is None
assert loss.shape == torch.Size([])
assert loss.grad_fn is not None
```

## Acumular no es reiniciar

PyTorch suma gradientes en las hojas. Este comportamiento es necesario cuando varias rutas o varios backward aportan contribuciones.

```python
w = torch.tensor(1.0, requires_grad=True)
loss = 0.5 * (w - 3.0) ** 2

loss.backward(retain_graph=True)
print(w.grad)  # tensor(-2.)

loss.backward()
print(w.grad)  # tensor(-4.): se sumó otra contribución -2
```

Para comenzar un recorrido nuevo:

```python
optimizer.zero_grad(set_to_none=True)
```

Entonces <code>w.grad</code> queda en <code>None</code> hasta que una operación nueva aporte gradiente.

### <code>None</code> frente a cero

- <code>None</code>: todavía no existe contribución en ese recorrido;
- tensor de ceros: existe un acumulador cuyo valor es cero.

La diferencia ayuda a detectar parámetros que no participaron en el grafo.

## Actualizar sin registrar la actualización

Después de backward podemos hacer un paso explícito:

```python
eta = 0.1

with torch.no_grad():
    w -= eta * w.grad
    b -= eta * b.grad
```

<code>torch.no_grad()</code> evita que la propia actualización se añada al grafo. En un ciclo habitual:

```python
optimizer.step()
```

delega esa misma responsabilidad al optimizador.

> [!summary] Tres verbos distintos
> <code>zero_grad()</code> prepara acumuladores; <code>backward()</code> calcula gradientes; <code>step()</code> consume gradientes y cambia parámetros.

## Cómo auditar autograd

Antes de confiar en un resultado:

1. comprueba que la pérdida sea escalar;
2. identifica las hojas entrenables;
3. inspecciona <code>requires_grad</code> y <code>grad_fn</code>;
4. predice al menos el signo de cada gradiente;
5. verifica que <code>.grad</code> tenga la misma forma que su parámetro;
6. registra el cambio de parámetros después de <code>step()</code>.

---

Anterior: [[03 Grafo computacional y backpropagation]] · Siguiente: [[05 Lotes, reducción y formas del gradiente]]
