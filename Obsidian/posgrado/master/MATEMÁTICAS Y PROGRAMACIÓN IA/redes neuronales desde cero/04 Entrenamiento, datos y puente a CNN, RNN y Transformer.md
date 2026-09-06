---
title: Entrenamiento, datos y puente a CNN, RNN y Transformer
tags:
  - master/matematicas-programacion
  - deep-learning
  - entrenamiento
---

# Entrenamiento, datos y puente a CNN, RNN y Transformer

## Ciclo completo

```python
model.train()
for X, y in loader:
    optimizer.zero_grad(set_to_none=True)
    logits = model(X)
    loss = criterion(logits, y)
    loss.backward()
    optimizer.step()
```

Cada línea responde una pregunta:

| Línea | Función |
|---|---|
| `train()` | activa comportamiento de entrenamiento |
| `zero_grad()` | evita acumular pasos anteriores |
| forward | calcula predicción |
| loss | construye objetivo escalar |
| backward | calcula sensibilidades |
| step | actualiza parámetros |

## Dataset y DataLoader

`Dataset` define cómo obtener una observación; `DataLoader` organiza lotes, orden y paralelismo. El split debe existir antes de construir loaders que mezclen ejemplos.

## Evaluación

```python
model.eval()
with torch.inference_mode():
    for X, y in validation_loader:
        logits = model(X)
```

Acumula numeradores y denominadores globales; no promedies F1 de mini-batches como si cada lote fuera una unidad equivalente.

## CNN: compartir en espacio

Una convolución aplica el mismo kernel en distintas posiciones. Introduce:

- localidad;
- compartición de parámetros;
- equivariancia aproximada a traslaciones.

En 1D puede procesar señales temporales; en 2D, imágenes.

## RNN: estado secuencial

$$h_t=\phi(W_xx_t+W_hh_{t-1}+b).$$

Comparte parámetros a través del tiempo y resume el prefijo en un estado. Su cálculo secuencial dificulta paralelizar posiciones.

## Transformer: interacción por atención

$$\operatorname{Attention}(Q,K,V)=
\operatorname{softmax}\left(\frac{QK^T}{\sqrt H}+M\right)V.$$

Cada posición puede leer otras posiciones directamente. Requiere mecanismos de posición y tiene coste denso cuadrático en longitud.

## Qué inductive bias elegir

| Datos | Estructura útil | Modelo inicial |
|---|---|---|
| tabla | características explícitas | lineal, árbol, MLP |
| imagen | localidad 2D | CNN/ViT |
| señal temporal | continuidad/localidad/orden | 1D CNN, RNN, Transformer |
| texto | tokens y contexto largo | Transformer |

## Monitorización

Registra por época:

- loss de train y validation;
- métrica primaria;
- tasa de aprendizaje;
- norma de gradiente;
- tiempo;
- configuración y semilla.

## Early stopping

Selecciona un checkpoint con validation. No uses test para decidir cuándo detener. Conserva el mejor estado, no solo el último.

## Autoevaluación

1. ¿Por qué se limpian gradientes?
2. ¿Qué diferencia Dataset de DataLoader?
3. ¿Qué comparte una CNN?
4. ¿Qué estado conserva una RNN?
5. ¿Qué permite atención y qué coste introduce?

---

Anterior: [[03 Normalización, dropout y conexiones residuales]] · Siguiente: [[05 Laboratorio y autoevaluación - Red neuronal desde cero]]

