---
tags:
  - machine-learning
  - poo
  - python
  - autodiff
---

# Grafo computacional, neurona lineal y backpropagation

Anterior: [[05 Scalar y autodiferenciación]] · Volver al índice: [[00 Índice - POO e IA]]

## 1. Neurona lineal con memoria

```python
x = Scalar(0.8, label="x")
w = Scalar(1.25, label="w")
b = Scalar(-0.30, label="b")

product = w * x
score = product + b
score.label = "score"

print("product =", product)  # Scalar(data=1.0, op='*')
print("score   =", score)    # Scalar(data=0.7, label='score', op='+')
```

El cálculo numérico es $z = wx + b = 1.25(0.8) - 0.30 = 0.70$. Pero ahora `score` conserva que fue creado por una suma, que uno de sus padres fue `product` y que `product` provino de `w` y `x`.

## 2. Grafo acíclico dirigido

```text
  w (1.25) ──┐
             ├──► [*] product (1.00) ──┐
  x (0.80) ──┘                         ├──► [+] score (0.70)
                                       │
  b (-0.30) ───────────────────────────┘
```

Cada flecha representa una dependencia. El grafo es acíclico porque una operación no debe depender de sí misma directa o indirectamente.

## 3. Orden topológico

Para evaluar el grafo o propagar gradientes, los padres deben procesarse antes que sus hijos.

```python
def topo(root):
    ordered = []
    visited = set()

    def visit(node):
        if id(node) in visited:
            return
        visited.add(id(node))

        for parent in node.parents:
            visit(parent)

        ordered.append(node)

    visit(root)
    return ordered

def node_name(node):
    return node.label or node.op or str(node.data)

ordered = topo(score)
names = [node_name(node) for node in ordered]
print(" -> ".join(names))
```

Un resultado posible es:

```text
w -> x -> * -> b -> score
```

`id(node)` identifica cada objeto durante su vida. Es útil porque dos nodos pueden compartir el mismo valor numérico, pero siguen siendo objetos distintos.

## 4. Neurona lineal como composición

```python
class LinearNeuron:
    def __init__(self, weight, bias):
        self.weight = Scalar(weight, label="w")
        self.bias = Scalar(bias, label="b")

    def forward(self, x):
        x = x if isinstance(x, Scalar) else Scalar(x, label="x")
        output = self.weight * x + self.bias
        output.label = "score"
        return output

neuron = LinearNeuron(1.25, -0.30)
prediction = neuron.forward(0.8)
print(prediction)
```

`LinearNeuron` compone objetos `Scalar`: tiene un peso, un sesgo y produce nuevos nodos al ejecutar `forward()`.

## 5. Puente hacia backpropagation

Para convertir este grafo en un motor de autodiferenciación como Micrograd o PyTorch Autograd faltan cuatro piezas:

1. `self.grad = 0.0` para acumular la derivada de la pérdida respecto al nodo.
2. `self._backward()` para guardar la derivada local de cada operación.
3. Recorrer `reversed(topo(loss))` para procesar de efectos hacia causas.
4. Acumular con `+=` cuando una variable participa en varias ramas.

Para la suma $c = a + b$:

$\frac{\partial \mathcal{L}}{\partial a} = \frac{\partial \mathcal{L}}{\partial c} \cdot 1$

Para la multiplicación $c = a \cdot b$:

$\frac{\partial \mathcal{L}}{\partial a} = \frac{\partial \mathcal{L}}{\partial c} \cdot b$

La POO no calcula estas derivadas por sí sola. Proporciona la estructura para guardar nodos, relaciones, operaciones y comportamiento local.

## Resumen final

| Concepto | Idea principal |
| :--- | :--- |
| Clase e instancia | Molde frente a objeto concreto con estado propio. |
| `self` | Objeto receptor de una llamada. |
| `__init__` | Inicializa el estado de una instancia. |
| Composición | Un objeto contiene y utiliza otros objetos. |
| Dunder | Conecta sintaxis nativa con métodos de una clase. |
| `Scalar` | `data` + `parents` + `op` + `label`. |
| Grafo computacional | Conserva la historia causal de las operaciones. |
| Orden topológico | Procesa dependencias antes que resultados. |
| Backpropagation | Recorre el grafo hacia atrás y aplica la regla de la cadena. |

## Repaso

- ¿Por qué los padres deben procesarse antes que los hijos?
- ¿Qué representa `parents` en el grafo?
- ¿Qué añade `grad` a la clase `Scalar`?
- ¿Por qué se recorre `reversed(topo(loss))` durante backpropagation?
