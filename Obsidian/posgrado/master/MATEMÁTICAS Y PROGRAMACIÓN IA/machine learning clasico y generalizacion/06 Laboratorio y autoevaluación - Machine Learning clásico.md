---
title: Laboratorio y autoevaluación - Machine Learning clásico
tags:
  - master/matematicas-programacion
  - machine-learning
  - laboratorio
related:
  - "[[../laboratorios fundamentos ia/ml_clasico_desde_cero.py]]"
---

# Laboratorio y autoevaluación: Machine Learning clásico

Archivo: [[../laboratorios fundamentos ia/ml_clasico_desde_cero.py]].

## Parte A: regresión lineal desde cero

Implementa:

$$\hat y_i=wx_i+b,$$

$$L=\frac1{2n}\sum_i(\hat y_i-y_i)^2,$$

$$\frac{\partial L}{\partial w}=\frac1n\sum_i(\hat y_i-y_i)x_i,$$

$$\frac{\partial L}{\partial b}=\frac1n\sum_i(\hat y_i-y_i).$$

Antes de entrenar, predice el signo del gradiente con $w=b=0$ y etiquetas positivas crecientes.

## Parte B: regresión logística

Comprueba numéricamente:

$$\frac{\partial L}{\partial z}=\sigma(z)-y.$$

Entrena con puntos 1D separables y verifica que la pérdida disminuye.

## Parte C: fuga deliberada

Compara dos protocolos:

1. estandarizar todo y luego dividir;
2. dividir, ajustar media/desviación en train y aplicar a validation.

Construye un caso con cambio de distribución para hacer visible la diferencia.

## Parte D: umbral

Con scores y etiquetas fijas, recorre varios umbrales y calcula TP, FP, FN y TN. Observa que el modelo no cambió; cambió la regla de decisión.

## Auditoría mínima

| Pregunta | Evidencia |
|---|---|
| ¿qué representa una fila? | frase escrita |
| ¿qué grupos no pueden mezclarse? | intersecciones vacías |
| ¿qué se ajustó en train? | parámetros guardados |
| ¿qué eligió validation? | registro de configuración |
| ¿cuándo se abrió test? | una evaluación final |

## Autoevaluación

1. Deriva mínimos cuadrados.
2. Explica el logit como log-odds.
3. Distingue parámetro, hiperparámetro y umbral.
4. Explica bias–variance con dos curvas.
5. Compara Random Forest y boosting.
6. Distingue ranking, clasificación y calibración.
7. Diseña una partición para usuarios nuevos.

> [!question]- Criterio de dominio
> Puedes resolver el laboratorio sin copiar, justificar cada denominador de las métricas y detectar cuándo una transformación vio datos de validation o test.

## Checklist

- [ ] La pérdida inicial y final están registradas.
- [ ] El gradiente analítico coincide con diferencia finita.
- [ ] Las particiones son disjuntas por grupo.
- [ ] El umbral no usa test.
- [ ] La conclusión menciona población y limitaciones.

---

Anterior: [[05 Métricas, umbrales, calibración y validación]] · Volver al [[00 Índice y recordatorio - Machine Learning clásico]]

