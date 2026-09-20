# Ensemble Methods (Métodos de Ensamblaje)

Los **Métodos de Ensamblaje** consisten en técnicas avanzadas que combinan las predicciones individuales de múltiples modelos base (a menudo denominados "estimadores débiles") con el objetivo principal de mejorar drásticamente la capacidad de generalización y la robustez predictiva, superando ampliamente el rendimiento de un único estimador aislado. Estos métodos operan bajo el principio estadístico conocido como la "Sabiduría de las Multitudes".

## 1. Bagging (Bootstrap Aggregating)

El objetivo central del Bagging es reducir la Varianza (el sobreajuste o *overfitting*) presente en modelos altamente complejos.

- **Funcionamiento:** Se construyen múltiples modelos predictivos totalmente independientes, los cuales se entrenan en paralelo. Cada modelo se entrena utilizando un subconjunto aleatorio diferente, extraído de los datos originales mediante un proceso de muestreo con reemplazo. Una vez entrenados, la predicción final del ensamble se calcula mediante el promedio (en tareas de regresión) o mediante un sistema de voto mayoritario (en tareas de clasificación).
- **Random Forest:** Es el algoritmo estrella y más famoso de esta categoría. Se trata de un ensamble constituido por múltiples [[Árboles de decisión]]. Para garantizar una alta diversidad estructural, además de emplear subconjuntos aleatorios de datos, cada árbol de decisión individual evalúa únicamente un subconjunto aleatorio de características en cada punto de división nodal.

```mermaid
flowchart TD
    Data[(Dataset Original)] --> S1[Subconjunto Aleatorio 1]
    Data --> S2[Subconjunto Aleatorio 2]
    Data --> S3[Subconjunto Aleatorio N]
    
    S1 --> M1[Modelo Base 1]
    S2 --> M2[Modelo Base 2]
    S3 --> M3[Modelo Base N]
    
    M1 --> V{Agregación \n(Promedio / Voto)}
    M2 --> V
    M3 --> V
    V --> P[Predicción Final]
```

## 2. Boosting

El propósito primordial del Boosting es reducir el Sesgo (el subajuste o *underfitting*) mediante la combinación estratégica de modelos sumamente simples (aquellos que apenas superan el nivel de acierto del azar).

- **Funcionamiento:** A diferencia de la estrategia en paralelo del Bagging, en el Boosting los modelos se entrenan de forma **secuencial** y dependiente. El modelo 1 intenta aprender inicialmente de los datos; acto seguido, el modelo 2 se entrena prestando especial y mayor atención en corregir los errores específicos cometidos por el modelo 1; a continuación, el modelo 3 se enfoca en corregir los errores residuales dejados por los modelos 1 y 2, y este proceso continúa iterativamente.
- **Implementaciones (XGBoost, LightGBM):** Algoritmos como XGBoost, LightGBM y Gradient Boosting representan implementaciones modernas, sofisticadas y ultra-optimizadas de esta técnica. Históricamente, han dominado y arrasado en las plataformas de competencias de Data Science (como Kaggle) cuando se trata del análisis de datos tabulares estructurados, ofreciendo una precisión de nivel estado del arte.

> [!info] Explicación Práctica
> La premisa matemática sólida que respalda a los ensambles radica en que si combinas múltiples modelos predictivos que individualmente son mejores que lanzar una moneda al azar, y que además cometen errores de forma independiente (es decir, no se equivocan exactamente en las mismas observaciones), el error estadístico colectivo del ensamble tenderá progresivamente a cero.
> 
> - **Regla de oro:** Utiliza métodos de Bagging (como Random Forest) cuando diagnostiques que tu modelo inicial sufre de un problema de sobreajuste. Por otro lado, emplea métodos de Boosting (como XGBoost) cuando identifiques que tu modelo inicial sufre de subajuste y requieras incrementar forzosamente su poder analítico y predictivo.

## Notas relacionadas
- [[Ajuste de modelos]]
- [[bias y viarianza]]
- [[Árboles de decisión]]
