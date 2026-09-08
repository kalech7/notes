---
title: Guía de comprensión - del ejemplo a todo el entrenamiento
modulo: M08
tags:
  - master/matematicas-programacion
  - gradientes
---

# Guía de comprensión: del ejemplo a todo el entrenamiento

Esta nota conecta la guía del estudiante con tus notas. Recorre la cadena completa sin tener que memorizar primero todas las fórmulas.

## 1. Una observación: qué quiero mejorar

Con $x=2$, $y=5$, $w=1$, $b=0$, la predicción es $\hat y=2$. El residuo $r=2-5=-3$ dice que nos quedamos cortos; la pérdida $L=r^2/2=4.5$ mide el costo de ese error.

![[assets/27-gradiente-3d-referencia.png|1000]]

El punto naranja es el estado actual. La altura es pérdida; el suelo contiene los parámetros. Aumentar un poco $w$ o $b$ mejora la predicción en este punto. Las derivadas son $\partial L/\partial w=rx=-6$ y $\partial L/\partial b=r=-3$. Sus signos describen sensibilidad de la pérdida, no el signo del parámetro.

Más detalle y lectura de la línea de mínimos: [[02 Gradiente, aproximación local y dirección de descenso]].

## 2. Cómo llega la pérdida hasta los pesos

El forward conserva valores y dependencias: $u=wx$, $\hat y=u+b$, $r=\hat y-y$, $L=r^2/2$.

El backward parte de $\partial L/\partial L=1$. Lleva sensibilidad $r=-3$ hasta la predicción y la multiplica por $x=2$ al llegar a $w$: resulta $-6$. En cada ruta se multiplican derivadas locales; entre rutas se suman aportes.

Ejemplo de ramas: si $z=a^2+a$ y $a=2$, la rama cuadrada aporta 4 y la directa 1; el resultado es 5. Esa suma necesaria **dentro del grafo** se distingue de acumular dos llamadas separadas a backward sin limpiar gradientes.

Más detalle: [[03 Grafo computacional y backpropagation]] y [[04 Autodiferenciación con micrograd y PyTorch]].

## 3. Un lote: tres errores se convierten en una pérdida

Con entradas $1,2,3$, objetivos $3,5,7$ y los mismos parámetros iniciales, los residuos son $-2,-3,-4$.

$$L=\frac{(-2)^2+(-3)^2+(-4)^2}{2(3)}=\frac{29}{6}.$$

$$\frac{\partial L}{\partial w}=\frac{1(-2)+2(-3)+3(-4)}3=-\frac{20}3,\qquad\frac{\partial L}{\partial b}=-3.$$

Con $\eta=0.1$, $w$ pasa a $5/3$ y $b$ a $0.3$. **Estos valores son del lote**, no del ejemplo con una sola observación, cuyo peso pasa a $1.6$ con esa tasa.

![[assets/11-formas-y-broadcasting.png|1000]]

En la imagen compara las formas antes de restar. Una predicción $(B,)$ y un objetivo $(B,1)$ pueden crear una matriz $(B,B)$: habría errores cruzados entre ejemplos. El programa puede calcular una pérdida que baje y aun así estar resolviendo otro problema.

Más detalle: [[05 Lotes, reducción y formas del gradiente]].

## 4. Calcular el gradiente no es actualizar

| Momento | Qué cambia | Qué todavía no ocurrió |
|---|---|---|
| forward | predicción y pérdida | no se han calculado nuevos gradientes de las hojas |
| backward | acumuladores `.grad` | los pesos no se han actualizado |
| step | pesos y estado del optimizador | `.grad` no se borra automáticamente |
| zero_grad | prepara acumuladores | no deshace el entrenamiento |

Momentum conserva una memoria $v_t=\mu v_{t-1}+g_t$. Si $\mu=0.9$, $g_1=-3$, $g_2=-1$, partiendo de memoria cero resulta $v_1=-3$ y $v_2=-3.7$. Aunque el nuevo gradiente es menor, con $\eta=0.1$ el segundo paso mide $0.37$, mayor que $0.30$.

Adam guarda dos promedios móviles: del gradiente y de su cuadrado. Son estado del optimizador, no nuevas derivadas producidas por autograd. Reiniciar el optimizador cada iteración borraría esa memoria.

Más detalle: [[08 Momentum y Adam - memoria del optimizador]].

## 5. Ruido y estabilidad responden preguntas diferentes

Un mini-lote estima el gradiente. Con aportes individuales $-2,-6,-12$, los pares posibles producen $-4,-7,-9$. Su promedio es $-20/3$, el gradiente completo, si los pares son equiprobables. No necesitas que cada par dé el mismo número.

La tasa y la curvatura deciden cómo se transforma esa señal en movimiento. En la cuadrática determinista, $e_{t+1}=(1-\eta a)e_t$ explica acercamiento, oscilación y divergencia. No traslades sin más esa recurrencia exacta a SGD o Adam.

Más detalle: [[06 Tasa de aprendizaje, curvatura y estabilidad]] y [[07 Mini-batch y SGD como estimador]].

## 6. Evaluar y diagnosticar

`eval()` cambia módulos como Dropout. `no_grad()` evita registrar nuevas operaciones para backward. Son dos interruptores; ninguno borra gradientes ya almacenados.

![[assets/13-matriz-train-eval-grad.png|1000]]

Lee las filas como comportamiento del módulo y las columnas como registro del grafo. Para evaluación habitual se combinan eval y no_grad. Para sensibilidad de una predicción se puede usar eval con gradientes habilitados.

Cuando algo falla, elige una observación que distinga causas:

| Síntoma | Primera comprobación |
|---|---|
| `.grad is None` inesperado | conexión al objetivo, hoja y requires_grad |
| gradiente doble | reinicio entre llamadas a backward |
| cambio de parámetros cero | gradiente, tasa y parámetros registrados en el optimizador |
| pérdida baja pero objetivo extraño | formas, reducción y emparejamiento de ejemplos |

Más detalle: [[09 train, eval, grad y no_grad]], [[10 Ciclo de entrenamiento reproducible y diagnóstico]] y [[11 Laboratorio PyTorch - predecir, observar y verificar]].

## Mapa de lectura de la guía

| Páginas de la guía PDF | Tema | Nota |
|---|---|---|
| 2–7 | objetivo, signos y descenso | 01–02 |
| 8–14 | cadena, ramas, DAG y topología | 03–04 |
| 15–20 | lote, hojas, acumulación y paso | 04–05 |
| 21–24 | error firmado y curvatura | 06 |
| 25–31 | mini-lotes, Momentum y Adam | 07–08 |
| 32–38 | train/eval y grafo | 09 |
| 39–44 | ciclo, evaluación y diagnóstico | 10–11 |
| 45 | glosario | [[00 Glosario visual - términos del entrenamiento]] |

Fuente: [[assets/guia_estudiante_m08_gradientes_autodiferenciacion_optimizacion.pdf|Guía del estudiante M08]]. La numeración de página del PDF es una unidad mayor que la de la diapositiva explicada porque incluye portada.


## Preguntas con respuesta desplegable

Haz clic en cada pregunta después de intentar responder.

> [!question]- ¿Qué dos números llevan de la pérdida inicial a los parámetros?
> Las sensibilidades son -6 para w y -3 para b en la observación x=2, y=5. Después debes elegir una tasa y una regla de actualización.

> [!question]- ¿Por qué el lote tiene gradiente -20/3 y la observación -6?
> Son objetivos distintos: uno promedia tres ejemplos, el otro usa solo x=2, y=5.

> [!question]- ¿Qué se multiplica y qué se suma en backward?
> Se multiplican derivadas a lo largo de una ruta; se suman contribuciones de varias rutas a una variable compartida.

> [!question]- ¿Por qué no basta con ver bajar loss?
> Puede bajar una pérdida construida con broadcasting incorrecto. Hay que comprobar formas, gradientes, actualización y evaluación.

> [!question]- ¿Qué añade M09 a este entrenamiento?
> Condiciones de ejecución e identidad de software/entradas para poder repetir y comparar. M10 organiza esos experimentos y sus métricas para consultar sin confundir filas.

Volver a [[00 Índice - Gradientes, autodiferenciación y optimización]].
