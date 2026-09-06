---
title: Punto flotante, estabilidad y condicionamiento
tags:
  - master/matematicas-programacion
  - algebra-numerica
  - estabilidad
---

# Punto flotante, estabilidad y condicionamiento

![[../assets/ruta maestra ia/07-condicionamiento.svg|900]]

## Los reales no caben en memoria

Un formato flotante representa un subconjunto finito de números mediante signo, exponente y significando. Operaciones reales se redondean:

$$fl(a\circ b)=(a\circ b)(1+\delta),\qquad |\delta|\lesssim u,$$

donde $u$ es la precisión de máquina bajo un modelo simplificado.

## Consecuencias

- `0.1 + 0.2` no tiene por qué ser exactamente `0.3`;
- la suma no es perfectamente asociativa;
- restar números casi iguales pierde dígitos significativos;
- exponenciales grandes desbordan;
- números pequeños pueden subdesbordar.

## Error absoluto y relativo

$$e_{abs}=|\hat x-x|,$$

$$e_{rel}=\frac{|\hat x-x|}{|x|}.$$

El relativo no es adecuado cuando $x$ está cerca de cero; se usa una escala combinada, como `atol + rtol*abs(x)`.

## Condicionamiento pertenece al problema

Para $y=f(x)$, el número de condición relativo local mide cuánto puede amplificarse una perturbación relativa.

En un sistema $Ax=b$:

$$\frac{\|\Delta x\|}{\|x\|}\lesssim
\kappa(A)\frac{\|\Delta b\|}{\|b\|}.$$

Con norma 2:

$$\kappa_2(A)=\frac{\sigma_{max}}{\sigma_{min}}.$$

Una singular mínima cercana a cero indica una dirección casi perdida.

## Estabilidad pertenece al algoritmo

Un algoritmo es backward stable si el resultado calculado es solución exacta de un problema ligeramente perturbado. No puede arreglar un problema inherentemente mal condicionado, pero evita añadir amplificación innecesaria.

## Ejemplo de cancelación

Para $x$ pequeño:

$$\sqrt{1+x}-1$$

resta números cercanos. Racionalizar:

$$\sqrt{1+x}-1=\frac{x}{\sqrt{1+x}+1}$$

es matemáticamente equivalente pero numéricamente más estable.

## Log-sum-exp

$$\log\sum_ie^{z_i}=m+\log\sum_ie^{z_i-m},\qquad m=\max_i z_i.$$

Evita overflow y es central en softmax y pérdidas probabilísticas.

## Precisión y rango

FP16 tiene menos rango exponencial que BF16; BF16 conserva un rango parecido a FP32 pero menos bits de precisión. Elegir dtype requiere separar rango, precisión, memoria y soporte de hardware.

## Autoevaluación

1. ¿Por qué una fórmula equivalente puede ser más estable?
2. ¿Qué diferencia hay entre condicionamiento y estabilidad?
3. ¿Qué indica $\sigma_{min}$ pequeña?
4. ¿Por qué `isclose` necesita tolerancia absoluta y relativa?

---

Anterior: [[00 Índice y recordatorio - Álgebra numérica para IA]] · Siguiente: [[02 Sistemas lineales, factorización QR y evitar la inversa]]
