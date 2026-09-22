---
title: "33 PRÁCTICA - Embeddings y similitud semántica"
tags:
  - maestria/ia-generativa
  - embeddings
  - practica
---

# 33 PRÁCTICA - Embeddings y similitud semántica

[[32 S06 - Elegir modelo y reconocer límites|Anterior]] · [[00 INICIO - Ruta de aprendizaje|Volver al índice]]

Resuelve primero cada pregunta y abre la respuesta después. Los números calculados a mano son **ejercicios didácticos**, no resultados de un modelo de embeddings.

## 1. Predice antes de medir

Ordena de más a menos similares, según tu intuición, estos cuatro pares del PDF:

1. «El gato duerme en el sofá» ↔ «Un felino descansa en el mueble».
2. «El gato duerme en el sofá» ↔ «El gato no duerme en el sofá».
3. «El gato duerme en el sofá» ↔ «Python lanza una excepción».
4. «¿Cómo facturo con RUC?» ↔ «Pasos para emitir factura electrónica».

Escribe tu orden **antes** de abrir lo siguiente.

> [!success]- Qué se puede concluir
> No hay un orden numérico único sin fijar el modelo y calcular sus embeddings. Los pares 1 y 4 tienen relaciones semánticas claras pese a palabras diferentes; el par 3 cambia de tema. El par 2 es el caso difícil: comparte tema y casi todas las palabras, pero contradice la afirmación. Si un modelo lo puntúa alto, muestra qué tipo de similitud aprendió. Evita presentar tu orden intuitivo como medición.

## 2. Distingue niveles de representación

Un texto tiene 12 tokens. El encoder produce 12 vectores de 384 coordenadas y se aplica MEAN pooling. ¿Cuántos vectores se usarán para comparar ese texto con otro? ¿De cuántas coordenadas?

> [!success]- Solución
> Uno, de 384 coordenadas. Pooling reduce la cantidad de vectores de 12 a 1; no reduce por sí solo la dimensión 384. La comparación se hace entre los vectores finales de ambos textos.

## 3. Haz pooling a mano

Para $t_1=(4,0,0)$, $t_2=(0,5,0)$ y $t_3=(2,1,3)$, calcula MEAN y MAX. ¿MAX es alguno de los tres tokens?

> [!success]- Solución
> $\mathrm{MEAN}=((4+0+2)/3,(0+5+1)/3,(0+0+3)/3)=(2,2,1)$. $\mathrm{MAX}=(4,5,3)$. MAX no coincide con ningún $t_i$: cada máximo procede de un token diferente. Tampoco es un múltiplo de MEAN, así que su dirección cambia.

## 4. Detecta la métrica real

Una persona cambia `normalize_embeddings=True` por `False`, pero mantiene `scores = V_corpus @ V_consulta`. Elige la descripción correcta:

- A. El programa falla porque no existe el producto punto de vectores no normalizados.
- B. El puntaje ya no es coseno, pero el ranking siempre se conserva.
- C. El puntaje ya no es coseno y el ranking puede cambiar.

> [!success]- Solución
> **C.** El producto punto existe para esos vectores, así que A es falsa. La longitud del candidato puede alterar el ranking, así que B es falsa. El contraejemplo de [[31 S06 - Coseno producto punto y normalización#3. Contraejemplo: cambia el ganador|la nota 31]] muestra una inversión concreta.

## 5. Calcula una búsqueda pequeña

Sean $q=(1,0)$, $a=(0.6,0.8)$ y $b=(2,0)$. Calcula producto punto y coseno con ambos documentos. ¿Cuál gana por cada medida?

> [!success]- Solución paso a paso
> $\|q\|=1$, $\|a\|=1$ y $\|b\|=2$. Productos punto: $q\cdot a=0.6$ y $q\cdot b=2$, por lo que gana $b$. Cosenos: $\cos(q,a)=0.6$ y $\cos(q,b)=2/(1\cdot2)=1$, por lo que **también** gana $b$. Este caso enseña que la falta de normalización *puede* cambiar el orden, pero no lo cambia en todos los conjuntos. Para ver una inversión usa el caso de la nota 31.

## 6. Umbral con una sola cara normalizada

Dos consultas tienen coseno $0.3$ respecto de su mejor documento normalizado. Una consulta tiene norma 1 y otra norma 2. Se usa producto punto y una regla «responder si el puntaje es al menos $0.35$». ¿Qué ocurre?

> [!success]- Solución
> Los productos punto son $1\cdot0.3=0.3$ y $2\cdot0.3=0.6$. La primera se abstiene; la segunda responde. Aunque la similitud angular es igual, el umbral produce decisiones distintas por la longitud de la consulta. Deben normalizarse ambos lados o calibrarse explícitamente el puntaje usado.

## 7. Diagnostica una recuperación fallida

Fragmentos de 512 tokens se embeben con un modelo que acepta como máximo 128. Una pregunta sobre el final del fragmento no recupera su respuesta. Formula una hipótesis y una medición concreta.

> [!success]- Solución
> Hipótesis: el texto pertinente fue truncado antes de generar el embedding. Medición: contar con el tokenizador del modelo los tokens de cada fragmento y registrar cuántos exceden el límite y dónde aparece la respuesta. Como control, comparar recuperación de preguntas respondidas al inicio y al final. La cifra exacta de tokens perdidos depende de la tokenización y de los tokens especiales.

## 8. Diseña una comparación mínima

Quieres averiguar si **normalizar** mejora una recuperación que usa producto punto. ¿Qué mantendrías fijo y qué medirías?

> [!success]- Solución orientativa
> Mantendría iguales el corpus, las consultas, el modelo, los fragmentos y la versión del índice. Compararía producto punto con vectores originales frente a producto punto con consulta y documentos normalizados. Mediría, con respuestas esperadas anotadas, cuántas consultas ponen un fragmento correcto en el primer puesto o en los primeros $k$, además de inspeccionar cambios de ranking. Si uso umbral, lo calibraría por separado porque la escala cambió.

## 9. Autoevaluación rápida

Si puedes explicar estas cinco frases sin mirar las notas, ya tienes la base de la sesión:

1. Un embedding es una representación aprendida; la cercanía depende de la tarea y de la métrica.
2. El vector de un token de entrada, su salida contextualizada y el vector del texto no son lo mismo.
3. SBERT entrena sobre relaciones entre textos y permite calcular cada embedding por separado.
4. Producto punto equivale a coseno **en valor** solo si ambos vectores tienen norma 1.
5. Recuperar un texto cercano no garantiza que afirme lo correcto ni que el contenido relevante haya entrado al modelo.

## Fuente y alcance

- [[sesion-06.pdf#page=11|Sesión 06, p. 11]]: ejercicio de predicción de pares.
- [[sesion-06.pdf#page=17|Sesión 06, p. 17]]: pregunta diagnóstica de normalización.
- [[sesion-06.pdf#page=19|Sesión 06, p. 19]]: caso de truncamiento.
- Los cálculos y soluciones detalladas de esta nota son ampliaciones originales para estudiar.
