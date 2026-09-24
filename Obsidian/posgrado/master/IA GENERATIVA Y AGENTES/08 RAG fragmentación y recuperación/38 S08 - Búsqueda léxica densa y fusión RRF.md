---
title: "38 S08 - Búsqueda léxica densa y fusión RRF"
sesion: "08"
tags:
  - maestria/ia-generativa
  - rag
  - estudio
fuente: "[[sesion-08.pdf]]"
---

# 38 S08 - Búsqueda léxica densa y fusión RRF

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[34 S08 - Guía para entender fragmentación y recuperación|Guía de la sesión 08]]

## 1. Buscar significa decidir qué consideramos relevante

Una vez creado el corpus de fragmentos, necesitamos ordenarlos frente a una pregunta. «Relevante» puede significar que contiene un identificador exacto o que expresa la idea solicitada con otras palabras. Esas señales son diferentes; por eso existen métodos complementarios.

La **búsqueda léxica** compara términos. La **búsqueda densa** compara representaciones aprendidas. La **búsqueda híbrida** combina sus resultados para aprovechar ambas señales. Ninguna garantiza por sí sola que el texto responda completamente a la pregunta.

## 2. Qué es BM25 y cómo razona su puntaje

BM25 es una función de recuperación léxica basada en estadísticas de términos. Cuando el PDF dice «sin modelo», se refiere a que no necesita un codificador neuronal entrenado; BM25 sí es un modelo de puntuación con parámetros.

Su lógica tiene tres partes. Un término raro en el corpus suele distinguir mejor un fragmento que uno presente por todas partes: esa es la contribución **IDF**. La repetición de un término dentro del fragmento aporta evidencia, pero cada repetición adicional aporta menos: es la **saturación de frecuencia**. Finalmente, un fragmento largo tiene más oportunidades de contener palabras por casualidad: la **normalización de longitud** modera esa ventaja.

Una forma habitual de escribirlo es:

$$\operatorname{BM25}(q,d)=\sum_{t\in q}\operatorname{IDF}(t)\frac{tf(t,d)(k_1+1)}{tf(t,d)+k_1(1-b+b|d|/avgdl)}.$$

$q$ es la consulta; $d$, el fragmento; $tf(t,d)$, la frecuencia del término; $|d|$, la longitud del fragmento; y $avgdl$, la longitud media de los fragmentos. $k_1$ regula la saturación y $b$ el efecto de la longitud. No son el número de resultados que pedimos.

No necesitas memorizar la fórmula antes de entenderla. Léela como **rareza × aporte de frecuencia ajustado por longitud**, sumado para los términos de la consulta. Las variantes concretas difieren, entre otras cosas, en la definición de IDF.

Si no hay términos compartidos, la contribución es cero en este esquema. Eso indica ausencia de coincidencia léxica, no prueba ausencia de una respuesta escrita con sinónimos. Una implementación también puede devolver resultados de puntaje cero si se le pide un top-k sin filtrarlos. «BM25 sabe decir nada» debe entenderse con ese límite.

Al cambiar los fragmentos cambian longitudes y frecuencias documentales. Por tanto, pueden cambiar los puntajes BM25 aunque las palabras del documento original sean las mismas.

### Rareza en el corpus y repetición dentro del fragmento son cosas distintas

IDF significa *inverse document frequency*, frecuencia documental inversa. Cuenta en cuántos documentos aparece un término, con la definición de «documento» usada por el índice; en este flujo cada fragmento funciona como una unidad documental. No cuenta simplemente todas las apariciones del término en el corpus.

En cambio, $tf(t,d)$ cuenta apariciones dentro de un fragmento concreto. Esta separación permite distinguir un término repetido en pocas fuentes de uno extendido por casi todo el corpus. La primera situación puede discriminar mejor entre candidatos; la segunda aporta menos información para distinguirlos.

Las longitudes de BM25 también dependen de su procesamiento de términos: minúsculas, signos, palabras descartadas u otras transformaciones. No deben confundirse con el conteo de tokens del codificador neuronal. Para que una coincidencia sea posible, consulta y corpus deben seguir reglas de procesamiento compatibles.

### Leer la fórmula por su comportamiento

Para entender el papel de la frecuencia y de la longitud, llama $f$ a $tf(t,d)$ y agrupa el ajuste de longitud así:

$$A=k_1\left(1-b+b\frac{|d|}{avgdl}\right),\qquad S(f)=\frac{f(k_1+1)}{f+A}.$$

Con $k_1>0$, longitudes positivas y $0\leq b\leq1$, si $f=0$ el aporte es cero. Si $f$ aumenta mucho, el numerador y el denominador crecen aproximadamente al mismo ritmo y $S(f)$ se aproxima a $k_1+1$. Ahí está la saturación: repetir el término no hace crecer indefinidamente **su aporte** para un IDF fijo.

Si un fragmento es más largo que la media y $b>0$, aumenta $A$. Con la misma frecuencia $f$, un denominador mayor reduce el puntaje. Eso formaliza la corrección por longitud. Si $b=0$, desaparece esa corrección; si $b=1$, el factor depende plenamente de la razón entre longitud y media.

$k_1$ determina cuánto tarda la frecuencia en acercarse a su saturación. En un fragmento de longitud media, donde $A=k_1$, un $k_1$ más alto da más margen a repeticiones adicionales antes de saturar. Un valor cercano a cero hace que, para términos presentes, importe sobre todo su presencia. Estas observaciones se derivan de la fórmula; no son una recomendación de valores para tu corpus.

La normalización de longitud está **dentro del denominador que regula la frecuencia**, no es un tercer multiplicador independiente. Pensar en rareza, frecuencia y longitud ayuda a interpretar el mecanismo; la fórmula muestra cómo interactúan realmente.

## 3. Qué hace la búsqueda densa

La densa representa consulta y fragmentos en un espacio compatible y los ordena mediante una medida como el coseno. Los vectores de los fragmentos pueden calcularse antes de recibir preguntas, lo que permite reutilizar el trabajo.

¿Por qué puede encontrar paráfrasis? Porque el entrenamiento puede acercar expresiones que cumplen funciones semánticas relacionadas aunque no compartan palabras. ¿Por qué puede fallar? Porque esa representación comprime información y puede acercar textos del mismo tema que difieren en un número, una negación o una condición decisiva.

Un top-k sin criterio de rechazo devuelve los mejores candidatos disponibles, hasta el límite solicitado y de lo que exista en el índice. «Mejor entre los disponibles» no significa «suficientemente bueno». Si ninguna fuente responde, todavía puede haber vecinos cercanos.

| Necesidad | Señal especialmente útil | Límite que conviene recordar |
| --- | --- | --- |
| Códigos, siglas o nombres concretos | Coincidencia léxica | El tokenizador puede separar identificadores |
| Expresiones diferentes para una idea | Representación semántica | La cercanía puede ser solo temática |
| Mezcla de términos exactos y paráfrasis | Ambas señales | Combinar añade decisiones y no garantiza mejora |

BM25 no es un buscador exacto de frases por definición; la búsqueda de una secuencia literal puede requerir posiciones, filtros o funciones específicas. Del mismo modo, la densa puede acertar con un código: lo que no ofrece es una garantía de coincidencia literal.

### Qué hace el índice y qué significa que el espacio sea compatible

Un índice organiza representaciones para localizar candidatos. Conceptualmente podrías comparar la consulta con todos los vectores y ordenar los puntajes. En sistemas grandes se pueden usar métodos que evitan examinar exhaustivamente todos los candidatos, aceptando una aproximación a los vecinos más cercanos. El índice afecta cómo se encuentra la lista; el modelo de embeddings afecta qué relaciones expresa la geometría de esa lista.

Por eso hay dos sentidos distintos de «aproximado». Una búsqueda puede encontrar **exactamente** los vecinos más cercanos según los vectores y aun así equivocarse respecto a la relevancia humana. También puede omitir algún vecino por usar un método de búsqueda aproximada. En la sesión 08 el índice se trata como una caja negra; esta distinción aclara el concepto sin exigir estudiar sus algoritmos internos.

Compatibilidad no significa solamente que ambos vectores tengan el mismo número de componentes. Sus coordenadas deben pertenecer a representaciones entrenadas para compararse. Dos modelos distintos pueden producir vectores de igual dimensión y organizar el significado de maneras incompatibles. Algunas arquitecturas usan codificadores diferentes para consulta y documento, pero entrenados para trabajar juntos.

### Ordenar y rechazar son decisiones diferentes

Si el puntaje es similitud, normalmente preferimos valores mayores; si es distancia, menores. Un umbral de aceptación debe respetar esa dirección. Su función es decidir si un candidato cumple un mínimo exigido, mientras que el ranking solo establece quién va antes.

Un umbral demasiado exigente puede rechazar evidencia útil; uno demasiado permisivo puede aceptar texto que solo comparte tema. No hay un número universal porque la distribución de puntajes cambia con el modelo, la medida, el corpus y las consultas. Comprobar preguntas sin respuesta disponible permite observar si el sistema confunde cercanía relativa con suficiencia de evidencia.

## 4. Por qué no sumar directamente los puntajes

El coseno está entre −1 y 1. BM25 no usa una escala universal equiparable: su magnitud depende de términos, corpus y configuración. Sumar ambos sin tratar sus escalas puede hacer que uno domine por su rango numérico, no por aportar mejor evidencia.

Existen métodos de normalización y combinación de puntajes. **RRF** evita esa calibración inicial usando las posiciones de los resultados en cada lista.

## 5. Qué es RRF y cómo combina

RRF significa *Reciprocal Rank Fusion*, fusión por rango recíproco. Cada lista aporta un voto que disminuye con la posición. Si un candidato no aparece en una lista, no recibe contribución de ella:

$$\operatorname{RRF}(d)=\sum_{i:d\in L_i}\frac{1}{k_{\mathrm{RRF}}+\operatorname{rank}_i(d)}.$$

La posición empieza en 1. $k_{\mathrm{RRF}}$ suaviza cuánto favorecemos las primeras posiciones; **no es el top-k de resultados**. El PDF usa 60 como valor convencional, no como una constante obligatoria.

![Aportes de las listas a la fusión](<../Recursos visuales/23-s08-rrf.png>)

Con $k_{\mathrm{RRF}}=60$, un candidato segundo en ambas listas recibe $2/62\approx0.03226$. Uno primero en una lista y ausente en la otra recibe $1/61\approx0.01639$. El gráfico muestra que el acuerdo puede superar una posición excelente aislada.

RRF no inspecciona el contenido ni decide si una afirmación es verdadera. Tampoco recupera por sí solo fragmentos que no están en ninguna lista de entrada. Necesita identificar cuándo ambas listas se refieren al mismo fragmento; de otro modo puede contar duplicados como si fueran candidatos diferentes.

Un valor mayor de $k_{\mathrm{RRF}}$ reduce las diferencias entre posiciones cercanas. Con 60, el aporte del puesto 1 es aproximadamente 1,148 veces el del 10; visto al revés, el puesto 10 aporta un 12,9 % menos. Es una forma de interpretar el «13 %» de la diapositiva.

### Cómo se construye la lista fusionada, paso a paso

Primero se obtiene una lista de cada buscador con identificadores de fragmento. Después se forma la **unión**: todos los candidatos que aparecieron al menos en una lista. Para cada identificador se suman las contribuciones de las listas donde aparece. Finalmente se ordena por el total y se conserva la cantidad deseada.

Usar la unión importa porque la búsqueda híbrida pretende permitir que una modalidad aporte candidatos que la otra no vio. Exigir que un fragmento aparezca en ambas sería una intersección y podría eliminar justamente esos aportes complementarios.

RRF recompensa el acuerdo, pero acuerdo no significa independencia ni verdad. Si ambas listas comparten el mismo error, la fusión puede reforzarlo. Además, usar solamente posiciones ignora si el primer resultado estaba muy por encima del segundo o casi empatado. Es el intercambio que permite combinar escalas diferentes sin calibrar sus puntajes originales.

## 6. Por qué no hay un ganador universal

La página 21 muestra que la recuperación densa superó a BM25 en varias tareas de preguntas y respuestas del estudio citado, mientras BM25 obtuvo una pequeña ventaja en FEVER. Esas cifras pertenecen a tareas y métricas específicas. No prueban que combinar siempre mejore ni predicen el resultado de tu corpus.

Una interpretación útil de esa comparación es que tareas que dependen de entidades exactas pueden beneficiarse de señales léxicas; las paráfrasis pueden beneficiarse de representaciones aprendidas. La decisión final necesita preguntas representativas del uso real.

> [!abstract] Para recordar
> **Léxica: términos. Densa: representaciones. RRF: posiciones.** Ninguna de esas tres cosas equivale a verificar una respuesta.

> [!question] Comprueba que lo entendiste
> ¿Por qué RRF puede combinar buscadores con escalas diferentes?
>
> Porque utiliza el orden de cada lista y no la magnitud original de los puntajes. A cambio, descarta parte de la información sobre sus diferencias de puntuación.

**Ampliación:** los efectos de $k_1$ y $b$ se deducen de la fórmula presentada; no son mediciones. Se consultó [[Hands-On_Large_Language_Models.pdf#page=254|cap. 8, p. impresa 232 (PDF 254)]] para el índice y la recuperación de texto mediante identificadores.

**Fuente:** [[sesion-08.pdf#page=18|páginas 18–22]]. Los cálculos RRF son propios a partir de la fórmula. Continúa con [[39 S08 - Reranking contexto y abstención]].
