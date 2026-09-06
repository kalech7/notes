---
title: Métricas, umbrales, calibración y validación
tags:
  - master/matematicas-programacion
  - machine-learning
  - metricas
  - calibracion
---

# Métricas, umbrales, calibración y validación

## Matriz de confusión

| | predicho positivo | predicho negativo |
|---|---:|---:|
| real positivo | TP | FN |
| real negativo | FP | TN |

$$\text{precision}=\frac{TP}{TP+FP},$$

$$\text{recall}=\frac{TP}{TP+FN},$$

$$F1=2\frac{precision\cdot recall}{precision+recall}.$$

## El denominador cuenta la historia

- precision condiciona en predicciones positivas;
- recall condiciona en positivos reales;
- especificidad condiciona en negativos reales;
- accuracy condiciona en todos los casos.

Con desbalance fuerte, accuracy puede ser alta prediciendo siempre la clase mayoritaria.

## Umbral

Un score continuo $s(x)$ se convierte en decisión:

$$\hat y=\mathbf1[s(x)\ge t].$$

Al bajar $t$ suelen aumentar TP y FP. No existe un umbral universalmente óptimo: depende del coste de errores y de la población.

## ROC y PR

- ROC grafica TPR frente a FPR.
- Precision–Recall muestra la calidad de alertas positivas y es especialmente informativa con positivos raros.
- AUC resume ranking sobre muchos umbrales; no selecciona un umbral operativo.

## Calibración

Un modelo está calibrado si entre predicciones cercanas a 0.8, aproximadamente 80 % son positivas.

Discriminación y calibración son distintas:

- ordenar bien riesgos → buena discriminación;
- asignar frecuencias correctas → buena calibración.

Brier score:

$$\operatorname{Brier}=\frac1n\sum_i(p_i-y_i)^2.$$

## Selección del umbral

Debe hacerse en validation, no test. Ejemplos de criterios:

- maximizar F1;
- limitar FPR a un máximo;
- minimizar coste $C_{FP}FP+C_{FN}FN$;
- igualar FAR y FRR en biometría.

## Validación cruzada

K-fold estima variabilidad al rotar particiones, pero los folds no son experimentos independientes. Todo el pipeline debe ajustarse dentro de cada fold.

```mermaid
flowchart LR
    A[Fold train] --> B[Ajustar transformación]
    B --> C[Ajustar modelo]
    C --> D[Predecir fold validation]
    D --> E[Guardar métrica]
    E --> F[Repetir sin mezclar grupos]
```

## Nested CV

Cuando hay mucha selección de hiperparámetros:

- bucle interno elige configuración;
- bucle externo estima desempeño del procedimiento de selección.

Evita reportar como final el mismo promedio usado para elegir.

## Intervalos y unidad de análisis

No construyas intervalos tratando miles de ventanas del mismo usuario como miles de unidades independientes. Resume o remuestrea al nivel que representa la generalización: sesión, usuario o corrida.

## Autoevaluación

1. ¿Por qué AUC no fija un umbral?
2. ¿Puede un modelo tener AUC alta y mala calibración?
3. ¿Dónde se elige el umbral?
4. ¿Qué debe ocurrir con un scaler dentro de CV?

---

Anterior: [[04 Árboles, Random Forest y boosting]] · Siguiente: [[06 Laboratorio y autoevaluación - Machine Learning clásico]]

