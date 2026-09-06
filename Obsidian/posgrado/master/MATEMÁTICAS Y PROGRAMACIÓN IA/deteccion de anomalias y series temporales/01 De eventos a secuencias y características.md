---
title: De eventos a secuencias y características
tags:
  - master/matematicas-programacion
  - series-temporales
  - feature-engineering
---

# De eventos a secuencias y características

## Evento de mouse

Cada fila contiene, entre otros campos:

```text
record timestamp, client timestamp, button, state, x, y
```

Una fila aislada no describe comportamiento. La información aparece en relaciones entre eventos consecutivos.

## Orden y diferencias

Para puntos $(x_i,y_i,t_i)$:

$$\Delta t_i=t_i-t_{i-1},$$

$$\Delta d_i=\sqrt{(x_i-x_{i-1})^2+(y_i-y_{i-1})^2},$$

$$v_i=\frac{\Delta d_i}{\Delta t_i}.$$

Solo calcula velocidad si $\Delta t_i>0$. Duplicados temporales requieren política explícita.

## Aceleración

$$a_i=\frac{v_i-v_{i-1}}{t_i-t_{i-1}}.$$

Las diferencias amplifican ruido, especialmente con intervalos pequeños. Usa resúmenes robustos y considera suavizado validado.

## Ángulo y curvatura

Dirección del segmento:

$$\theta_i=\operatorname{atan2}(\Delta y_i,\Delta x_i).$$

El cambio angular debe envolverse a $[-\pi,\pi]$ para evitar que pasar de $179^\circ$ a $-179^\circ$ parezca un giro de $358^\circ$.

## Características por sesión

| Familia | Ejemplos |
|---|---|
| volumen | número de eventos, movimientos, clics |
| duración | tiempo total, pausas |
| distancia | recorrido total, desplazamiento neto |
| velocidad | media, mediana, desviación, percentiles, máximo |
| aceleración | magnitud media y dispersión |
| geometría | cambios angulares, eficiencia recta/recorrido |
| interacción | frecuencia de clic, estados de botón |

## Media frente a distribución

Dos sesiones pueden tener igual velocidad media y distinta variabilidad. Incluye mediana, desviación y percentiles, sin crear cientos de variables con pocas sesiones de entrenamiento.

## Ventanas

Ventanas permiten detectar cambios dentro de una sesión, pero introducen decisiones:

- duración o número de eventos;
- solapamiento;
- tratamiento de ventanas incompletas;
- etiqueta de ventana;
- agregación a decisión de sesión.

> [!warning] Solapamiento
> Ventanas vecinas comparten eventos. Si se reparten entre train y test, la evaluación ve casi copias.

## Invariancias útiles

- trasladar toda la trayectoria no cambia velocidades;
- rotar puede o no ser relevante según interfaz;
- cambiar resolución de pantalla altera distancias en píxeles;
- cambiar frecuencia de muestreo altera diferencias y debe tratarse.

## Autoevaluación

1. ¿Por qué no dividir por $\Delta t=0$?
2. ¿Qué pierde un resumen por sesión?
3. ¿Por qué envolver ángulos?
4. ¿Qué fuga introducen ventanas solapadas?

---

Anterior: [[00 Índice y recordatorio - Anomalías y secuencias]] · Siguiente: [[02 Particiones temporales, por sesión y por identidad]]

