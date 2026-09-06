---
title: Sistemas lineales, factorización QR y evitar la inversa
tags:
  - master/matematicas-programacion
  - algebra-numerica
  - sistemas-lineales
---

# Sistemas lineales, factorización QR y evitar la inversa

## Resolver no es invertir

Para $Ax=b$, el objetivo es obtener $x$. Calcular explícitamente:

$$x=A^{-1}b$$

suele costar más, almacenar más y acumular más error que usar un solver por factorización.

## Eliminación y LU

LU factoriza:

$$PA=LU,$$

donde $P$ permuta filas, $L$ es triangular inferior y $U$ superior. Luego se resuelven dos sistemas triangulares.

El pivoteo evita dividir por elementos pequeños cuando existe una alternativa más estable.

## QR

$$A=QR,$$

con $Q^TQ=I$ y $R$ triangular superior. Las transformaciones ortogonales preservan norma y suelen ser numéricamente favorables.

Para mínimos cuadrados:

$$\min_x\|Ax-b\|_2,$$

$$\|Ax-b\|=\|QRx-b\|=\|Rx-Q^Tb\|.$$

Se resuelve el sistema triangular $Rx=Q^Tb$ sin formar $A^TA$.

## Por qué evitar ecuaciones normales

$$A^TAx=A^Tb.$$

Aunque correctas en aritmética exacta:

$$\kappa(A^TA)=\kappa(A)^2.$$

Un problema moderadamente sensible puede volverse muy sensible al cuadrar el condicionamiento.

## Residuo no siempre implica error pequeño

$$r=b-A\hat x.$$

Un residuo pequeño indica que $\hat x$ casi satisface la ecuación. Si $A$ está mal condicionada, soluciones muy diferentes pueden producir residuos pequeños.

## Elección práctica

| Problema | Método habitual |
|---|---|
| cuadrado general | LU con pivoteo |
| simétrico definido positivo | Cholesky |
| mínimos cuadrados | QR |
| rango deficiente o análisis de direcciones | SVD |
| matriz enorme dispersa | método iterativo |

## Autoevaluación

1. ¿Por qué `solve(A,b)` es preferible a `inv(A)@b`?
2. ¿Qué conserva una matriz ortogonal?
3. ¿Por qué $A^TA$ empeora el condicionamiento?
4. ¿Puede haber residuo pequeño y error grande?

---

Anterior: [[01 Punto flotante, estabilidad y condicionamiento]] · Siguiente: [[03 Mínimos cuadrados, pseudoinversa, SVD y regularización]]

