---
title: "56 S10 - Elegir una extensión y comprobar su efecto"
sesion: "10"
fecha: 2026-09-27
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-10.pdf]]"
---

# 56 S10 - Elegir una extensión y comprobar su efecto

[[50 S10 - Guía para comprender el taller RAG|Guía de la sesión 10]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[55 S10 - Abstención fidelidad y errores del evaluador]]

Siguiente: [[57 S10 - Reproducibilidad entregables y reflexión]]

## 1. Elegir por mecanismo de falla

La presentación ofrece cuatro extensiones. La elección debe responder a un problema observado. Un par de promedios orienta la investigación, pero no identifica una causa única.

![[40-s10-diagnostico-extensiones.png]]

Para cada síntoma, revisa primero la evidencia indicada. Después elige la intervención que podría afectar esa causa. La última columna muestra qué debe cambiar si la hipótesis era correcta. No son promesas de mejora.

## 2. Opción A: otra fragmentación

Es apropiada si la evidencia se corta, pierde su título, mezcla temas o queda fuera de la entrada efectiva del encoder. Una hipótesis concreta sería: «El plazo y su excepción quedan en fragmentos separados; mantenerlos juntos permitirá recuperar la regla completa».

Puedes probar límites por párrafo o sección, tamaño en tokens y solapamiento. Un fragmento más grande aporta contexto, pero puede mezclar temas o exceder el límite. Uno más pequeño mejora precisión local, pero puede perder condiciones y aumentar la cantidad de piezas que hay que combinar.

**Qué verificar:** compara el texto antes y después, confirma que la evidencia quedó dentro del presupuesto real y revisa resultados por pregunta. Reasocia las referencias a los nuevos fragmentos como se explica en [[53 S10 - Golden set y límites de lo respondible]].

Hit Rate y MRR bajos también pueden surgir de un archivo omitido, un filtro incorrecto o anotaciones equivocadas. Cambiar cortes sin revisar esas posibilidades puede dejar intacta la falla.

## 3. Opción B: búsqueda híbrida con BM25 y RRF

La búsqueda densa compara embeddings y puede reconocer paráfrasis. BM25 usa coincidencia léxica: pondera términos, su frecuencia y la longitud del documento. Puede ayudar con identificadores como «EQ-17», siglas o números cuya forma exacta distingue un procedimiento.

Híbrida significa combinar señales. Una consulta puede obtener candidatos por ambos caminos y fusionarlos. **RRF**, *Reciprocal Rank Fusion*, usa posiciones de los rankings en vez de sumar directamente scores con escalas diferentes.

Usaremos una convención didáctica con posiciones desde 1:

$$RRF(d)=\sum_{j:\,d\in L_j}\frac{1}{c+r_j(d)}$$

$L_j$ es una lista de candidatos; $r_j(d)$, la posición de $d$ en esa lista; $c$ suaviza diferencias entre posiciones. No confundas $c$ con el corte top-k. Si un candidato no aparece en una lista, esa lista no le aporta puntaje.

Con $c=60$, supongamos:

| Documento | Posición densa | Posición léxica | Puntaje fusionado |
| --- | ---: | ---: | ---: |
| A | 1 | No aparece | $1/61\approx0,01639$ |
| B | 2 | 1 | $1/62+1/61\approx0,03252$ |
| C | No aparece | 2 | $1/62\approx0,01613$ |

El orden fusionado es B, A, C. B recibe apoyo de ambos métodos. Esto no demuestra que B sea relevante: explica cómo se combinó la evidencia de los rankings.

La [documentación de Qdrant](https://qdrant.tech/documentation/search/hybrid-queries/) usa su propia convención de posiciones y configuración. Comprueba la fórmula y los valores de tu versión antes de trasladar parámetros. Los números de este ejemplo no se presentan como los valores por defecto del laboratorio.

**Límite:** RRF solo reorganiza la unión de candidatos disponibles. Si la evidencia no está en ninguna lista, la fusión no puede crearla.

## 4. Opción C: reranking

Un *reranker* recibe la pregunta y candidatos ya recuperados y vuelve a ordenarlos. En un esquema con **cross-encoder**, el modelo procesa conjuntamente cada pareja pregunta-texto para estimar su relevancia. Esto permite interacciones más detalladas que comparar dos vectores preparados por separado, a cambio de trabajo por candidato.

Ejemplo: el documento correcto está séptimo entre veinte candidatos. El generador recibe solo cinco. Un reranker puede llevarlo al segundo puesto; así mejora Hit Rate@5 aunque la recuperación inicial a veinte no cambie.

Si el reranker solo recibe cinco candidatos y el correcto está séptimo, no puede rescatarlo. Debes distinguir **profundidad de candidatos** y **corte final**. Si reordenas exactamente los mismos cinco y evalúas presencia a cinco, Hit Rate@5 se mantiene; MRR@5 sí puede cambiar.

En la tabla de la nota 54, si q3 pasa de cuarto a segundo y los demás casos permanecen iguales, Hit Rate@5 sigue en 0,75. MRR@5 aumenta:

$$\Delta MRR@5=\frac{1/2-1/4}{8}=0{,}03125$$

El nuevo valor es aproximadamente 0,4417. A k=3 también mejora Hit Rate, porque q3 cruza el corte. Esto demuestra por qué es necesario declarar ambos tamaños.

La documentación de [Sentence Transformers sobre recuperación y reranking](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html) explica esta arquitectura en dos etapas. No se atribuye a un modelo multilingüe una calidad que no haya sido evaluada sobre el idioma y la tarea relevantes.

## 5. Opción D: evaluar con RAGAS

Si la evidencia aparece pronto y con frecuencia, el siguiente punto a investigar puede ser cómo se utiliza en la respuesta. RAGAS ofrece instrumentos de evaluación; añadir medición **no modifica automáticamente el comportamiento del RAG**.

La extensión consiste en obtener evidencia adicional sobre las respuestas y explicar sus límites. Registra la configuración del evaluador, versión, modelo juez, llamadas y costo observado. Una puntuación automática es una estimación producida por un procedimiento que también puede equivocarse.

Revisa manualmente desacuerdos, ejemplos extremos y condiciones omitidas. Evita presentar una nota del juez como verdad absoluta o compararla con otra obtenida bajo criterios distintos.

## 6. Cómo diseñar una comparación interpretable

Conserva corpus, golden set, criterios, cortes y condiciones relevantes. Cambia una intervención principal. Guarda línea base y extensión de modo que puedas volver a consultarlas. Si también cambias el generador, el prompt y los documentos, ya no puedes atribuir fácilmente el resultado al reranker.

Registra por pregunta: evidencia esperada, candidatos, respuesta, métricas y diferencia entre configuraciones. Una extensión puede ganar en siglas, perder en paráfrasis y elevar latencia. El promedio debe acompañarse de esa explicación.

> [!abstract] La conclusión válida puede ser una ausencia de mejora
> «La extensión no elevó Hit Rate y añadió latencia; por ahora no hay evidencia suficiente para adoptarla» es una conclusión útil cuando está respaldada por la comparación.

## La extensión real: mejora parcial de orden

La entrega comparó búsqueda densa con **BM25 + RRF**, hasta veinte candidatos por cada ruta y constante RRF 60, sobre el mismo golden set. Sus salidas archivadas son:

| Corte | Hit denso | Hit híbrido | MRR denso | MRR híbrido |
| --- | ---: | ---: | ---: | ---: |
| k=3 | 0.875 | 0.750 | 0.5625 | 0.5625 |
| k=5 | 0.875 | 0.875 | 0.5625 | 0.59375 |

A cinco mejora MRR en 0.03125 sin ganar preguntas. A tres pierde un acierto: una evidencia pasa del puesto 1 al 4, mientras otras se adelantan. «La búsqueda híbrida mejora» sería una conclusión incompleta; su efecto depende del corte y de qué caso pesa. La extensión no registró generación comparable: no permite inferir mejor abstención, fidelidad o calidad final.

La inspección multi-fragmento encontró coberturas literales 0.5, 0.5 y 0 para las preguntas 4, 5 y 6 en ambos cortes. En la 4 aparecen pasajes alternativos que explican la distinción requerida, aunque falte una ancla esperada: hay que revisar el juicio antes de concluir insuficiencia. En la 5 falta la evidencia específica sobre solapamiento y diversidad del contexto; en la 6 ambas anclas existen en el corpus pero no llegan al top-5. Estos casos apuntan a mecanismos distintos. Tampoco se observó que los cinco vecinos de la pregunta sobre duplicados fueran cinco copias: no atribuyas automáticamente el fallo a una premisa incluida en la propia pregunta.

Fuente adicional: entrega archivada, `resultados_extension.csv`, `evidencias/comparacion_extension.csv`, `cobertura_multi_fragmento.json` y análisis de casos. No se reejecutó la extensión.


**Fuente:** PDF, pp. 3, 13 y 15. Las hipótesis, ejemplos de fusión y cálculos de reranking son ampliaciones propias.
