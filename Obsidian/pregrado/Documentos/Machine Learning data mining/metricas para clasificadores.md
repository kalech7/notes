# Matriz de Confusión 
![[Pasted image 20240617184110.png]]

![[Pasted image 20240617185334.png]]

Idealmente, se desea que nuestros clasificadores solo tengan valores en la diagonal principal (verdaderos negativos y verdaderos positivos). Esta diagonal indica que todos los individuos han sido correctamente categorizados por el modelo.
Un "Falso Positivo" ocurre cuando el sistema falla al predecir la clase positiva, señalando un elemento como relevante o positivo cuando en realidad no lo era.

- **Accuracy (Exactitud):** Es una buena medida general del rendimiento, especialmente útil si se tiene un número equilibrado de muestras en todas las clases.
- **Confusion Matrix (Matriz de confusión):** Es una tabla que presenta de forma resumida y detallada la comparación de todas las predicciones del modelo frente a los valores reales.

> [!info] Explicación
> **Métricas Comunes derivadas de la Matriz de Confusión:**
> - **Precisión (Precision):** De todos los que predijimos como positivos, ¿cuántos eran realmente positivos? (TP / (TP + FP)). Es vital cuando el costo de un Falso Positivo es alto (ej. marcar un correo legítimo e importante como spam).
> - **Sensibilidad o Recall:** De todos los positivos reales en la base de datos, ¿cuántos logramos identificar correctamente? (TP / (TP + FN)). Es crucial cuando el costo de un Falso Negativo es altísimo (ej. no detectar un tumor cancerígeno existente).
> - **F1-Score:** Es la media armónica entre Precisión y Recall. Útil cuando se busca un balance entre ambas métricas o cuando el dataset está muy desbalanceado.

## Notas relacionadas
- [[curvas roc]]
- [[metodo hold out]]
- [[test harness]]
- [[tipos de machine learning]]
