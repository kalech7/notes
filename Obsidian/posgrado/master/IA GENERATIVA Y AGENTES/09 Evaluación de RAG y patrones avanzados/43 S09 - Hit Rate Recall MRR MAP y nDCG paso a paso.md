---
title: "43 S09 - Hit Rate Recall MRR MAP y nDCG paso a paso"
sesion: "09"
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-09.pdf]]"
---

# 43 S09 - Hit Rate Recall MRR MAP y nDCG paso a paso

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[42 S09 - Guía para evaluar un RAG|Guía de la sesión 09]]

## 1. Un mismo ranking responde tres preguntas distintas

Fuente base: [[sesion-09.pdf#page=4|PDF, pp. 4–8]]. Los desarrollos de AP y nDCG y el ejemplo con varias preguntas son ampliaciones didácticas.

Para una pregunta q, llamamos $R_q$ al conjunto de unidades relevantes anotadas y $T_{q,k}$ a las unidades de los primeros k puestos. Una unidad puede ser un fragmento o un documento, pero la referencia y los resultados deben usar la misma unidad. Un **puesto** empieza en 1; el identificador de un fragmento no es su puesto.

En el ejemplo del PDF, el ranking es `[3, 7, 12, 1, 9]`. El identificador relevante es 7 y está en el puesto 2. Con k = 5:

- Hay un acierto: Hit@5 = 1.
- Se recuperó el único relevante: Recall@5 = 1/1 = 1.
- El primer acierto llegó segundo: RR@5 = 1/2 = 0,5.

MRR es el promedio de los RR de varias preguntas. Para una sola pregunta, su valor coincide con ese RR, pero conviene conservar la distinción conceptual.

## 2. Hit Rate: ¿apareció al menos uno?

$$
\mathrm{Hit}_q@k=\mathbf{1}\{|R_q\cap T_{q,k}|>0\}
$$

El símbolo $\mathbf{1}$ vale 1 si la condición se cumple y 0 si no se cumple. Si N es el número de preguntas respondibles:

$$
\mathrm{HitRate}@k=\frac{1}{N}\sum_{q=1}^{N}\mathrm{Hit}_q@k
$$

Hit Rate no distingue recuperar una pieza de recuperar todas. Tampoco distingue el primer puesto del último admitido. Es útil para saber en cuántas preguntas llegó **alguna evidencia relevante**, pero un acierto no demuestra que haya evidencia suficiente para responder todo.

## 3. Recall: ¿qué fracción de lo necesario recuperé?

$$
\mathrm{Recall}_q@k=\frac{|R_q\cap T_{q,k}|}{|R_q|}
$$

Si hacen falta los fragmentos A, B y C y recuperas solo A, el recall es 1/3. El Hit de esa pregunta es 1. Si recuperas A dos veces por un error de duplicación, no has recuperado dos piezas distintas: la intersección de conjuntos cuenta A una sola vez.

En estas notas el agregado es el **promedio por pregunta**, o macro-promedio. Un promedio micro, que suma aciertos y relevantes de todas las preguntas antes de dividir, ponderaría más las preguntas con muchos relevantes. Son convenciones distintas y deben declararse.

Con exactamente un relevante por pregunta, Hit Rate y Recall coinciden. La coincidencia no demuestra que el evaluador mida dos capacidades diferentes. Tampoco depende del nombre «simple»: depende del número de unidades relevantes que anotaste.

## 4. RR y MRR: ¿qué tan pronto aparece la primera evidencia?

Sea $r_q$ el puesto del primer relevante:

$$
\mathrm{RR}_q@k=\begin{cases}1/r_q,&r_q\leq k\\0,&\text{sin acierto dentro del corte}\end{cases}
\qquad
\mathrm{MRR}@k=\frac{1}{N}\sum_q\mathrm{RR}_q@k
$$

El corte importa. Si el primer relevante está quinto, RR@3 = 0 y RR@5 = 0,2. No puedes revisar todo el ranking al calcular una métrica que declaraste cortada en 3.

![[28-s09-metricas-y-posicion.png]]

### Cómo leer el gráfico

El panel izquierdo muestra un ejemplo propio: A y B son necesarios; A está segundo y B cuarto. Verde significa relevante, gris significa no relevante y la línea naranja cierra el top-3. Dentro del corte hay una de dos piezas: Hit@3 = 1, Recall@3 = 0,5 y RR@3 = 0,5. Al ampliar a 5, Recall sube a 1, pero RR sigue en 0,5 porque el primer acierto no se movió.

En el panel derecho, el eje horizontal es el puesto del primer relevante y el vertical es su rango recíproco. Pasar del puesto 2 al 1 suma 0,5; pasar del 5 al 4 suma solo 0,05. Esa curva explica por qué MRR recompensa especialmente tener evidencia al comienzo. No representa probabilidades ni resultados de un modelo.

Dos preguntas con primeros aciertos en 1 y 5 tienen MRR = (1 + 0,2)/2 = 0,6. Su posición promedio es 3 y el inverso de esa posición es 0,333. **Promediar inversos no es invertir el promedio.** El inverso de MRR, 1,67, tampoco es un puesto promedio observado; cuando todos aciertan es la media armónica de los puestos.

## 5. Ejemplo completo con tres preguntas

Todos los identificadores de este ejemplo representan fragmentos distintos. Se evalúa con k = 3.

| Pregunta | Relevantes | Ranking top-3 | Hit | Recall | RR |
| --- | --- | --- | ---: | ---: | ---: |
| Q1 | A | X, A, Y | 1 | 1 | 1/2 |
| Q2 | B, C | B, X, Y | 1 | 1/2 | 1 |
| Q3 | D | X, Y, Z | 0 | 0 | 0 |

$$HitRate@3=2/3\approx0{,}667$$
$$Recall@3=(1+0{,}5+0)/3=0{,}5$$
$$MRR@3=(0{,}5+1+0)/3=0{,}5$$

La lectura es: dos de tres preguntas reciben alguna evidencia; en promedio se recupera la mitad de las piezas anotadas; el primer acierto recibe una puntuación recíproca media de 0,5. Esta última cifra no significa «siempre llega segundo»: Q3 ni siquiera tiene un acierto.

## 6. AP y MAP: importa también el resto de relevantes

MRR mira solo el primer acierto. Para distinguir rankings con varios relevantes, AP considera la precisión en cada puesto relevante. La **precisión en i** es relevantes encontrados hasta i dividido por i.

Una convención explícita de AP truncada es:

$$
AP@k=\frac{1}{|R_q|}\sum_{i=1}^{k}P@i\cdot rel(i)
$$

$rel(i)$ vale 1 si el resultado del puesto i es relevante. Algunos evaluadores usan otro denominador para AP@k; hay que comprobarlo antes de comparar cifras.

Con relevantes A y B y ranking `[X,A,Y,B,Z]`, las precisiones en los puestos relevantes son P@2 = 1/2 y P@4 = 2/4. AP@5 = (0,5 + 0,5)/2 = 0,5. AP@3 = 0,5/2 = 0,25: el relevante fuera del corte no aporta. MAP es la media de AP sobre preguntas.

Con un único relevante por pregunta, MAP@k coincide con MRR@k si ambos usan el mismo corte, la misma población y esta convención. Con varios relevantes, la igualdad deja de estar garantizada.

## 7. nDCG: relevancia de distintos grados

A veces un resultado es parcialmente útil y otro responde completamente. Puedes anotar grados, por ejemplo 0, 1 y 2. Una formulación habitual es:

$$DCG@k=\sum_{i=1}^{k}\frac{2^{g_i}-1}{\log_2(i+1)},\qquad nDCG@k=\frac{DCG@k}{IDCG@k}$$

$g_i$ es el grado en el puesto i. La ganancia $2^{g_i}-1$ da más peso a los grados altos; el logaritmo descuenta los puestos tardíos. IDCG es el valor del orden ideal con los mismos juicios y corte. Hay variantes con ganancia lineal: especifica la usada.

Ejemplo: grados `[0,2,1]`. DCG ≈ 0 + 3/1,585 + 1/2 = 2,393. El orden ideal `[2,1,0]` produce IDCG ≈ 3 + 1/1,585 = 3,631. Por tanto nDCG ≈ 0,659. No quiere decir «65,9 % de respuestas correctas»: es ganancia descontada relativa al orden ideal. Si IDCG = 0, el protocolo debe declarar cómo maneja ese caso.

## 8. Dónde no usar estas cuentas

Las preguntas negativas tienen cero relevantes. Recall tendría denominador cero. En el protocolo de esta sesión se excluyen de Hit Rate, Recall y MRR y se evalúan por abstención. Si no hay preguntas respondibles, reporta **no aplicable**, no un cero que sugiera fracaso.

> [!abstract] Para recordar
> Hit Rate = presencia de alguna evidencia. Recall = cobertura de la evidencia anotada. MRR = prontitud del primer acierto. MAP = orden de varios aciertos. nDCG = orden con grados de relevancia.

**Comprueba tu comprensión:** si mantienes el primer relevante segundo y añades otro relevante cuarto, ¿qué cambia? Recall y posiblemente AP; RR no cambia. La respuesta completa depende del corte y del total de relevantes anotados.
