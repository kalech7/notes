---
title: "54 S10 - Hit Rate y MRR con un experimento completo"
sesion: "10"
fecha: 2026-09-27
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-10.pdf]]"
---

# 54 S10 - Hit Rate y MRR con un experimento completo

[[50 S10 - Guía para comprender el taller RAG|Guía de la sesión 10]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[53 S10 - Golden set y límites de lo respondible]]

Siguiente: [[55 S10 - Abstención fidelidad y errores del evaluador]]

## 1. Antes de calcular: qué cuenta como acierto

Supondremos que cada pregunta respondible tiene al menos una evidencia relevante anotada y que conocemos la posición del primer resultado que coincide con esa referencia. Evaluaremos el mismo ranking a dos cortes: $k=3$ y $k=5$.

La letra $k$ indica cuántas posiciones inspeccionamos. La posición comienza en 1. Si el primer relevante está en la posición 4, hay acierto a cinco y no a tres.

## 2. Hit Rate: ¿aparece al menos un relevante?

Para una pregunta $i$:

$$H_i@k=\begin{cases}1&\text{si hay un relevante en las primeras }k\text{ posiciones}\\0&\text{si no lo hay}\end{cases}$$

Sobre $N$ preguntas respondibles:

$$\operatorname{HitRate}@k=\frac{1}{N}\sum_{i=1}^{N}H_i@k$$

Es una proporción de **preguntas con acierto**, no de fragmentos relevantes. No distingue un relevante primero de uno quinto, siempre que ambos entren en el corte. Tampoco comprueba que hayas recuperado todas las evidencias requeridas.

## 3. MRR: ¿qué tan pronto aparece el primer relevante?

El recíproco de la posición es $1/r$. Si el relevante está primero, vale 1; segundo, $1/2$; tercero, $1/3$. Al limitarlo a $k$:

$$RR_i@k=\begin{cases}1/r_i&r_i\le k\\0&\text{si no aparece un relevante dentro del corte}\end{cases}$$

$$\operatorname{MRR}@k=\frac{1}{N}\sum_{i=1}^{N}RR_i@k$$

MRR promedia esas recompensas. Valora encontrar pronto la primera evidencia, pero no evalúa todos los relevantes posteriores ni la respuesta generada. Si una pregunta requiere combinar tres fragmentos, llegar pronto al primero puede seguir siendo insuficiente.

## 4. Experimento didáctico de ocho preguntas

![[38-s10-metricas-por-pregunta.png]]

**Cómo leerlo:** cada fila es una pregunta. Un recuadro verde marca el primer relevante; los anteriores son candidatos no relevantes. Las columnas finales muestran lo que aporta esa fila al promedio. Las preguntas q5 y q8 tienen cero porque no hay relevante en el top-5; no afirmamos que sea imposible encontrarlo más abajo.

| Pregunta | Primer relevante | H@3 | RR@3 | H@5 | RR@5 |
| --- | ---: | ---: | ---: | ---: | ---: |
| q1 | 1 | 1 | 1 | 1 | 1 |
| q2 | 2 | 1 | 1/2 | 1 | 1/2 |
| q3 | 4 | 0 | 0 | 1 | 1/4 |
| q4 | 5 | 0 | 0 | 1 | 1/5 |
| q5 | Fuera del top-5 | 0 | 0 | 0 | 0 |
| q6 | 1 | 1 | 1 | 1 | 1 |
| q7 | 3 | 1 | 1/3 | 1 | 1/3 |
| q8 | Fuera del top-5 | 0 | 0 | 0 | 0 |

A tres aparecen relevantes en q1, q2, q6 y q7:

$$H@3=\frac{4}{8}=0{,}5$$

$$MRR@3=\frac{1+1/2+0+0+0+1+1/3+0}{8}
=\frac{17}{48}\approx0{,}3542$$

A cinco se añaden q3 y q4:

$$H@5=\frac{6}{8}=0{,}75$$

$$MRR@5=\frac{1+1/2+1/4+1/5+0+1+1/3+0}{8}
=\frac{197}{480}\approx0{,}4104$$

**Interpretación:** al ampliar el corte, dos preguntas más encuentran evidencia, pero esta aparece relativamente tarde. Nada en estas cuatro cifras dice si el generador contestó correctamente.

## 5. Por qué MRR nunca supera Hit Rate en esta comparación

En cada pregunta sin acierto, ambos aportes son 0. En cada pregunta con acierto, $H_i=1$ y $RR_i=1/r_i\le1$. Por tanto:

$$0\le RR_i@k\le H_i@k$$

Al promediar sobre **las mismas preguntas, referencias y corte**:

$$0\le MRR@k\le HitRate@k\le1$$

Si un reporte muestra $MRR@5=0{,}8$ y $H@5=0{,}6$ bajo esas condiciones, hay una inconsistencia. Puede estar promediando MRR solo sobre aciertos, usando otra población o mezclando cortes.

«MRR alto y Hit Rate bajo no existe» es una simplificación de esta desigualdad. La afirmación rigurosa es $MRR\le H$. Las palabras alto y bajo necesitan un criterio numérico explícito.

## 6. Una lectura más profunda: MRR condicionado al acierto

Si $H@k>0$, podemos escribir:

$$\frac{MRR@k}{H@k}
=\text{promedio de }1/r_i\text{ entre las preguntas que sí acertaron}$$

En el ejemplo:

$$0{,}4104/0{,}75\approx0{,}5472$$

Esto separa la frecuencia de encontrar evidencia de qué tan pronto aparece cuando se encuentra. **No** equivale al inverso de la posición media, porque promediar y tomar recíprocos son operaciones diferentes.

## 7. Qué significa realmente una mejora con ocho respondibles

Cambiar de seis a siete aciertos hace pasar Hit Rate de $0{,}75$ a $0{,}875$: **12,5 puntos porcentuales**. Es un único caso de diferencia, no una prueba amplia de superioridad.

El incremento mínimo de Hit Rate con ocho casos es $1/8=0{,}125$. MRR puede cambiar en cantidades menores al mover una evidencia del puesto 5 al 4, incluso sin ganar ninguna pregunta.

Compara por pregunta: cuál mejoró, cuál empeoró y por qué. Si eliges la extensión después de mirar estos mismos casos, estás usando el conjunto para desarrollo. Para estimar mejor la generalización, una evaluación posterior debería incluir preguntas nuevas mantenidas aparte.

## 8. Qué puede significar un 0,70

Sin nombre de métrica, referencia, corte y población, el número es ambiguo. Puede ser un coseno, una proporción de aciertos, un promedio de rangos recíprocos o una evaluación de fidelidad; sus interpretaciones son distintas.

Además, con ocho respondibles y promedio binario simple, **0,70 no es un Hit Rate exacto posible**: los valores avanzan de 0,125 en 0,125. Podría proceder de otra cantidad de casos, otra agregación o un redondeo poco preciso. La página 3 menciona «aquel 0,70», pero este PDF no permite identificar su experimento original. No debemos inventarlo.

> [!abstract] Plantilla para explicar una cifra
> «Esta métrica mide ___, usa como referencia ___, se calcula a k=___ sobre ___ preguntas y vale ___. No mide ___».

**Fuente:** PDF, pp. 3, 5, 11 y 13. Los ocho rankings y todas sus cuentas son ejemplos propios, reproducibles en `verificar_ejemplos_s10.py`.
