---
title: Laboratorio y autoevaluación - Cálculo multivariable
tags:
  - master/matematicas-programacion
  - calculo
  - laboratorio
related:
  - "[[../laboratorios fundamentos ia/calculo_multivariable.py]]"
---

# Laboratorio y autoevaluación: cálculo multivariable

Archivo: [[../laboratorios fundamentos ia/calculo_multivariable.py]].

## Experimento 1: predicción local

Para

$$f(x,y)=x^2+3xy+y^2,$$

en $(1,2)$:

1. calcula el gradiente;
2. predice el cambio para $\Delta=(0.01,-0.02)$;
3. evalúa el cambio real;
4. calcula el error de la aproximación.

El error debería reducirse aproximadamente de forma cuadrática al escalar $\Delta$.

## Experimento 2: gradient check

Compara cada componente analítica con diferencia central:

$$g_j^{num}=\frac{f(x+he_j)-f(x-he_j)}{2h}.$$

Usa error relativo:

$$\frac{|g_j-g_j^{num}|}{\max(1,|g_j|,|g_j^{num}|)}.$$

Prueba varios $h$: demasiado grande introduce error de truncamiento; demasiado pequeño sufre cancelación flotante.

## Experimento 3: VJP sin Jacobiano explícito

Para $y=Ax$ y $L=c^Ty$:

$$\nabla_xL=A^Tc.$$

Calcula primero $A^Tc$ y compáralo con construir $J=A$ y multiplicar. El resultado coincide, pero el VJP expresa mejor lo que necesita reverse mode.

## Experimento 4: condicionamiento

Compara descenso en:

$$f_1(x,y)=\frac12(x^2+y^2),$$

$$f_2(x,y)=\frac12(x^2+100y^2).$$

La segunda función limita la tasa estable por la dirección de curvatura 100, aunque la dirección $x$ sea suave.

## Pruebas semánticas

| Prueba | Invariante |
|---|---|
| gradiente | tiene la forma de la entrada |
| Jacobiano | salida × entrada |
| VJP | devuelve sensibilidad respecto de la entrada |
| Hessiano cuadrático | es simétrico |
| Taylor | mejora al reducir el paso antes del límite flotante |

## Autoevaluación final

1. Explica derivada como modelo local.
2. Distingue gradiente de Jacobiano.
3. Explica reverse mode usando VJP.
4. Deriva el gradiente de mínimos cuadrados.
5. Explica punto silla con autovalores del Hessiano.
6. Explica por qué $X^TX$ puede empeorar condicionamiento.

> [!question]- Respuestas clave
> El gradiente corresponde a salida escalar; el Jacobiano, a salida vectorial. Reverse mode propaga combinaciones de filas y evita materializar Jacobianos. En mínimos cuadrados el residuo vuelve por $X^T$. Los autovalores mixtos del Hessiano indican direcciones de subida y bajada. El número de condición de $X^TX$ es aproximadamente el cuadrado del de $X$.

## Criterio de finalización

- [ ] Puedo predecir un cambio antes de evaluar.
- [ ] Puedo auditar una derivada con diferencia central.
- [ ] Puedo indicar la forma de cada Jacobiano.
- [ ] Puedo explicar broadcasting hacia delante y reducción hacia atrás.
- [ ] Ejecuté el laboratorio sin fallos.

---

Anterior: [[03 Hessiano, convexidad y cálculo matricial]] · Volver al [[00 Índice - Cálculo multivariable y matricial]]

