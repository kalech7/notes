en machine learning la medicon del rendimiento es una tarea ensencial entonces cuando se trata de un problema de clasificacion
excatitud, preciion sensibilidad especidicidad puntaje de f1
para verficar el rednimiento de cualquier modelo de clasificiacion 
roc viene de las caracterisitica de funcionamiento del receptor y auc del area bajo la curva 
la curva roc nos dice que tan bueno puede distinguir el modelo entre dos cosas
mejores modelos pueden distinguir con precision entre los dos mientras que un modelo pobre tendra dificultades para distinguir entre los dos 
![[Pasted image 20240617191423.png]]
![[Pasted image 20240617191702.png]]
el auc es el area bajo la curva roc este puntaje nos da una idea de que tan bien funciona el modelo
cuando auc=1  las curvas no se superpones en absoluto el modelo tiene una medida ideal de separacion  distingue perfectamente en clase positiva y clase negativa 
auc=0.7 cuando las distribuciones se superponen introducen errores dependiendo del umbral podemos minimizarlo o maximizarlos  significa que hay 70% de probabilidad de que el modelo pueda distinguir entre clase positiva y clase negativa

la peor situacion es cuando el auc es aprox 0.5 el modelo no tiene la capacidad de diiscriminacion para distinguir entre las clases positivas y negativas 

cuando auc es aprox 00 el modelo en realidad esta correspondiendo las clases significa que el modelo predice la clase negativa como una positiva y viceversa 

## Notas relacionadas
- [[metricas para clasificadores]]
- [[metodo hold out]]
- [[tipos de machine learning]]
