# Preprocesamiento de Datos

El **Preprocesamiento de Datos** es la etapa inicial e indispensable en cualquier proyecto de Machine Learning. Consiste fundamentalmente en limpiar, transformar y acondicionar los datos crudos para convertirlos en un formato coherente, comprensible y útil para los algoritmos matemáticos. Se estima que esta laboriosa etapa suele consumir entre el 60% y el 80% del tiempo total de trabajo de un científico de datos.

## 1. Limpieza de Datos (Data Cleaning)
Los datos provenientes del mundo real son inherentemente desordenados, inconsistentes y ruidosos.
- Esta sub-etapa consiste en identificar y corregir errores de tipografía, unificar formatos dispares (por ejemplo, estandarizar todas las fechas a un formato ISO) y remover registros duplicados que podrían sesgar el modelo.

## 2. Manejo de Valores Faltantes (Missing Values)
Resulta sumamente común que los datasets industriales contengan celdas vacías (representadas como NaN o Null). La gran mayoría de los algoritmos matemáticos colapsarán irremediablemente si se les alimenta con datos faltantes.
- **Eliminación:** Consiste en borrar las filas o columnas completas. Esta técnica solo se recomienda si el porcentaje de datos faltantes es muy pequeño y su ausencia se considera completamente aleatoria.
- **Imputación Simple:** Trata de rellenar los huecos utilizando métricas estadísticas básicas de la columna correspondiente, como la media, la mediana o la moda.
- **Imputación Avanzada:** Implica utilizar algoritmos predictivos (como el *KNN Imputer* o regresiones iterativas) para estimar y rellenar el valor faltante, basándose matemáticamente en la información contenida en las demás características.

## 3. Detección y Tratamiento de Outliers (Valores Atípicos)
Los *outliers* o valores atípicos son puntos de datos extremos que se desvían de manera drástica y estadísticamente significativa del resto de las observaciones. Pueden ser producto de errores de medición o, por el contrario, representar descubrimientos reales y sumamente valiosos.
- **Detección:** Se suelen utilizar herramientas visuales como gráficos de caja (Boxplots), técnicas estadísticas como el método del Rango Intercuartílico (IQR), o algoritmos especializados en anomalías como *Isolation Forest*.
- **Tratamiento:** Si se verifica que son errores, se eliminan. Si son datos legítimos pero distorsionan severamente el modelo (algo común en regresiones lineales), se pueden aplicar transformaciones matemáticas (como logaritmos) o implementar la técnica de recorte (*clipping*), limitando los valores extremos hacia un umbral máximo o mínimo.

```mermaid
flowchart LR
    A[Datos Crudos] --> B[Data Cleaning]
    B --> C[Tratamiento de Missing Values]
    C --> D[Manejo de Outliers]
    D --> E[Datos Limpios listos para ML]
```

> [!info] Explicación Estratégica
> El Preprocesamiento trabaja de manera estrictamente paralela con el [[Feature Engineering]]. Mientras que el preprocesamiento se encarga de "curar y preparar" el terreno para que los datos sean legibles, estables y sin errores, la ingeniería de características asume el rol de "elevar y potenciar" esos datos, construyendo nuevas variables que incrementen el poder predictivo del algoritmo.

## Notas relacionadas
- [[machine learning]]
- [[Feature Engineering]]
- [[K-Nearest Neighbors (KNN)]]
