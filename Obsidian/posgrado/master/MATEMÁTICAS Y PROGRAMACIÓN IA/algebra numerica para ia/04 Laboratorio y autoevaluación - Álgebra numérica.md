---
title: Laboratorio y autoevaluación - Álgebra numérica
tags:
  - master/matematicas-programacion
  - algebra-numerica
  - laboratorio
related:
  - "[[../laboratorios fundamentos ia/algebra_numerica.py]]"
---

# Laboratorio y autoevaluación: álgebra numérica

Archivo: [[../laboratorios fundamentos ia/algebra_numerica.py]].

## Experimentos

1. Compara suma de un número grande y muchos pequeños en órdenes distintos.
2. Evalúa $\sqrt{1+x}-1$ directa y racionalizada.
3. Compara softmax ingenua y estable.
4. Resuelve dos sistemas casi singulares con perturbaciones pequeñas.
5. Compara residuo y error de solución.
6. Ajusta una recta con ecuaciones normales y con una formulación estable.

## Predicciones

- la forma racionalizada conservará más dígitos para $x$ pequeño;
- softmax estable permanecerá finita;
- el sistema mal condicionado amplificará perturbaciones;
- un residuo pequeño no garantizará error pequeño;
- regularizar reducirá sensibilidad a cambio de introducir sesgo.

## Pruebas de dominio

| Debes poder | Evidencia |
|---|---|
| distinguir problema y algoritmo | ejemplo condicionado con solver estable |
| explicar singular pequeña | dirección casi perdida |
| evitar inversa explícita | usar sistema/factorización |
| justificar tolerancia | escala y precisión declaradas |
| comparar métodos | residuo, error y coste |

## Checklist

- [ ] Expliqué cancelación catastrófica.
- [ ] Calculé un número de condición simple.
- [ ] Expliqué por qué QR evita $A^TA$.
- [ ] Interpreté pseudoinversa en coordenadas SVD.
- [ ] Ejecuté las aserciones del laboratorio.

---

Anterior: [[03 Mínimos cuadrados, pseudoinversa, SVD y regularización]] · Volver al [[00 Índice y recordatorio - Álgebra numérica para IA]]

