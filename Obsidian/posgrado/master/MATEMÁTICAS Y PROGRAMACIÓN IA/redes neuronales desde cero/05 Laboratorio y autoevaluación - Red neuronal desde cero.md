---
title: Laboratorio y autoevaluación - Red neuronal desde cero
tags:
  - master/matematicas-programacion
  - deep-learning
  - laboratorio
related:
  - "[[../laboratorios fundamentos ia/red_neuronal_desde_cero.py]]"
---

# Laboratorio y autoevaluación: red neuronal desde cero

Archivo: [[../laboratorios fundamentos ia/red_neuronal_desde_cero.py]].

## Red para XOR

XOR no es separable por una sola recta:

| $x_1$ | $x_2$ | $y$ |
|---:|---:|---:|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

Una capa oculta con no linealidad puede construir regiones intermedias y resolverlo.

## Arquitectura

```text
entrada (B,2)
  ↓ Linear(2,4)
oculta (B,4)
  ↓ tanh
  ↓ Linear(4,1)
logit (B,1)
  ↓ BCE
pérdida escalar
```

El laboratorio implementa forward y backward con listas de Python para hacer visibles todos los pasos.

## Experimentos

1. Entrena sin capa oculta y observa el límite lineal.
2. Entrena el MLP.
3. Elimina la activación y comprueba que vuelve a ser lineal.
4. Inicializa todos los pesos iguales y observa la simetría.
5. Aumenta demasiado la escala inicial y observa saturación de `tanh`.

## Pruebas mínimas

- salida con forma `(4,1)`;
- pérdida finita;
- gradientes finitos;
- pérdida final menor que inicial;
- cuatro predicciones correctas después de entrenamiento estable;
- reproducibilidad con la misma semilla.

## Preguntas de dominio

1. ¿Qué hace cada matriz de pesos?
2. ¿Dónde aparece la no linealidad?
3. ¿Por qué la pérdida es escalar?
4. ¿Cómo llega el error a la primera capa?
5. ¿Qué indicadores distinguen saturación de tasa excesiva?

> [!tip] Explicación oral esperada
> “La primera capa crea cuatro combinaciones de las dos entradas. `tanh` las curva. La segunda capa combina esas características para producir un logit. BCE produce una señal $p-y$ que vuelve por la segunda matriz y luego por la derivada de `tanh` hasta la primera.”

## Checklist

- [ ] Predije todas las formas.
- [ ] Derivé al menos un peso a mano.
- [ ] Ejecuté el caso sin activación.
- [ ] Comparé inicialización correcta e incorrecta.
- [ ] Expliqué por qué un Transformer sigue siendo una red neuronal.

---

Anterior: [[04 Entrenamiento, datos y puente a CNN, RNN y Transformer]] · Volver al [[00 Índice y recordatorio - Redes neuronales desde cero]]

