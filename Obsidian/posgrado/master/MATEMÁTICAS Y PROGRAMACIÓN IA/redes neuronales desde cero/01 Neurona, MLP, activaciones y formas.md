---
title: Neurona, MLP, activaciones y formas
tags:
  - master/matematicas-programacion
  - deep-learning
  - mlp
---

# Neurona, MLP, activaciones y formas

## Neurona

$$z=w^Tx+b,\qquad h=\phi(z).$$

$w$ decide direcciones relevantes; $b$ desplaza el umbral; $\phi$ transforma la respuesta.

## Capa completa

Para $H$ neuronas:

$$Z=XW+b,$$

con:

$$X:(B,D),\quad W:(D,H),\quad b:(H),\quad Z:(B,H).$$

El sesgo se replica sobre el lote. Su gradiente sumará contribuciones de las $B$ observaciones.

## Por qué hace falta no linealidad

Sin activaciones:

$$XW_1W_2=XW,$$

por lo que muchas capas lineales colapsan en una sola transformación lineal. Las no linealidades permiten fronteras curvas y composiciones jerárquicas.

## Activaciones

| Función | Expresión | Ventaja | Riesgo |
|---|---|---|---|
| sigmoid | $1/(1+e^{-x})$ | salida interpretable binaria | saturación |
| tanh | $\tanh x$ | centrada en cero | saturación |
| ReLU | $\max(0,x)$ | simple y gradiente 1 en positivo | unidades muertas |
| GELU | $x\Phi(x)$ | transición suave | más coste |
| SiLU | $x\sigma(x)$ | suave, no monótona cerca de 0 | más coste |

Sigmoid suele usarse en salida binaria; softmax en salida multiclase. En capas ocultas se prefieren ReLU, GELU o SiLU.

## MLP

$$H_1=\phi(XW_1+b_1),$$

$$Z=H_1W_2+b_2.$$

Con $D=3$, $H=4$, $K=2$:

```text
X   (B,3)
W1  (3,4) → H1 (B,4)
W2  (4,2) → Z  (B,2)
```

## Conteo de parámetros

$$P_1=DH+H,$$

$$P_2=HK+K.$$

Para el ejemplo: $3\cdot4+4+4\cdot2+2=26$.

## Capacidad

Más anchura o profundidad aumenta funciones representables, pero también:

- coste computacional;
- riesgo de memorizar;
- sensibilidad a inicialización y optimización;
- necesidad de datos y regularización.

## Salida y pérdida deben corresponder

| Tarea | Salida | Pérdida habitual |
|---|---|---|
| regresión | números | MSE/MAE |
| binaria | un logit | BCE con logits |
| multiclase | $K$ logits | cross-entropy |
| multilabel | $K$ logits independientes | BCE por etiqueta |

> [!warning] Logits no son probabilidades
> `CrossEntropyLoss` recibe logits y aplica internamente `log_softmax`. Aplicar softmax antes puede perder estabilidad y alterar el cálculo esperado.

## Autoevaluación

1. ¿Por qué capas lineales sin activación colapsan?
2. Predice formas de un MLP $(D,H,K)=(10,32,4)$.
3. ¿Por qué sigmoid oculta puede saturarse?
4. ¿Cuántos parámetros tiene cada capa?

---

Anterior: [[00 Índice y recordatorio - Redes neuronales desde cero]] · Siguiente: [[02 Inicialización y flujo del gradiente]]

