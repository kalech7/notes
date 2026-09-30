---
title: "12 GLOSARIO - Diccionario explicado para estas sesiones"
tags:
  - maestria/ia-generativa
  - estudio
---

# 12 GLOSARIO - Diccionario explicado para estas sesiones

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

**Base:** [[glosario-mmia-6013.pdf|Glosario del curso, versión suministrada del 13 de septiembre de 2026]], secciones de notación y términos de sesiones 01–04. Selección comentada, no transcripción completa.

## Cómo usar este glosario

Busca aquí una palabra cuando te frene la lectura. Primero lee su explicación y el ejemplo; después vuelve a la nota. No necesitas memorizar todos los símbolos antes de empezar.

## Cómo leer las letras sin perderte

| Símbolo | Significado en estas notas | Ejemplo |
| --- | --- | --- |
| X, x | Variable de datos y valor observado | Un correo |
| Y, y | Variable de clase y etiqueta concreta | Spam |
| D | Conjunto observado | Corpus de entrenamiento |
| $\theta$ | Parámetros de un modelo | Pesos o probabilidades ajustadas |
| z | Variable latente | Componente oculto de una mezcla |
| $\pi_k$ | Peso de un componente | 0.3 de peso en un GMM |
| $\mu$ | Media | Centro de una distribución |
| $\sigma^2$ | Varianza | Dispersión en una dimensión |
| $\Sigma$ | Covarianza | Dispersión y orientación multivariada |
| $x_{<t}$ | Elementos anteriores a t | Prefijo de una secuencia |
| $Q,K,V$ | Queries, keys y values de atención | Puntuar relevancia y combinar contenido |
| $d_k$ | Dimensión de una key/query por cabeza | Factor de escala $\sqrt{d_k}$ |
| $\pi_\theta$ | Política o distribución del modelo | Probabilidad de una respuesta |
| $r_\phi(x,y)$ | Recompensa estimada para una respuesta | Señal proxy en RLHF |
| $T$ | Temperatura de decodificación | Reescala logits antes de softmax |
| $\sum$ | Sumar posibilidades | Marginalizar componentes |
| $\prod$ | Multiplicar factores | Probabilidad de una secuencia |
| $\mathbb E$ | Promedio bajo una distribución | Término esperado de ELBO |
| $\arg\max$ | Valor que maximiza una función | Parámetro MLE |

Una letra puede cambiar de significado entre contextos. Por ejemplo, K cuenta componentes en GMM y símbolos en el ejemplo de Markov. Lee siempre la definición local. No confundas una covarianza mayúscula $\Sigma$ con el operador de suma $\sum$.

## Probabilidad y aprendizaje

**Prior:** lo que asumimos sobre las posibilidades antes de incorporar el dato nuevo. Ejemplo: antes de leer un correo, el 20 % de los mensajes del conjunto es spam.

**Verosimilitud:** qué tan compatible es el dato observado con una explicación o un valor del parámetro. Ejemplo: qué tan frecuente es encontrar «oferta» entre los spam. No responde todavía cuántos correos con «oferta» son spam.

**Posterior:** las probabilidades que obtenemos después de usar la nueva información. Ejemplo: la probabilidad de spam después de leer «oferta». Indica siempre qué estamos intentando averiguar.

**Evidencia:** probabilidad del dato observado considerando todas las explicaciones. En el ejemplo, cuenta la presencia de «oferta» tanto en spam como en normales. Es el denominador de Bayes.

**MLE, máxima verosimilitud:** elegir el valor del parámetro que hace más probables los datos observados. Para siete caras en diez lanzamientos, la estimación de probabilidad de cara es 0.7.

**Pérdida:** número que penaliza los errores según el criterio de entrenamiento. El ajuste intenta reducirlo. Su utilidad depende de que ese criterio se relacione con la tarea que nos importa.

**Parámetro:** valor que se aprende al entrenar, como un peso. **Hiperparámetro:** configuración del aprendizaje o del modelo, como el tamaño de cada actualización o la cantidad de componentes de una mezcla.

**Generalización:** funcionar bien con ejemplos nuevos. **Sobreajuste:** aprender también detalles o ruido del entrenamiento que hacen fallar en otros ejemplos; parecido a memorizar un examen sin entender cómo resolver preguntas nuevas.

**Muestrear:** sortear un resultado respetando unas probabilidades. Si A tiene 80 % y B 20 %, ambos pueden salir. Elegir siempre A sería otra estrategia.

## Modelos y estructuras

**Discriminativo:** en clasificación, aprende a decidir o calcular la etiqueta a partir de una entrada. Ejemplo: dado este correo, estimar si es spam.

**Generativo:** aprende una distribución de datos con la que podemos plantear cómo producir ejemplos. Puede generar puntos o palabras; que genere no garantiza que el resultado sea bueno.

**Latente:** algo que el modelo supone pero que no observamos directamente. En un GMM vemos el punto, pero no sabemos qué componente lo produjo.

**GMM:** modelo que combina varias distribuciones gaussianas para describir datos. Es útil para representar varias concentraciones de puntos con centros y dispersiones diferentes.

**Responsabilidad:** probabilidad de que un componente explique un dato después de observarlo. Por ejemplo, 75 % para el primer componente y 25 % para el segundo.

**EM:** algoritmo que repite dos pasos: calcula cuánto corresponde cada dato a cada componente y luego recalcula los parámetros usando esos aportes.

**Markov de orden M:** modelo que utiliza los M elementos anteriores para predecir el siguiente. Un bigrama usa solo uno.

**HMM:** modelo de una secuencia con estados que no vemos y observaciones que sí recibimos. Ejemplo: estado de una máquina y ruido que emite.

**VAE:** modelo que aprende a generar datos a partir de códigos ocultos. Un codificador propone códigos para los datos conocidos y un decodificador aprende a producir datos desde esos códigos.

**ELBO:** objetivo que se maximiza al entrenar un VAE. Equilibra explicar bien el dato y mantener los códigos compatibles con un prior. Matemáticamente es una cota inferior de la log-probabilidad del dato.

**KL (divergencia de Kullback–Leibler):** cuantifica cuánto difiere una distribución $q$ de una distribución de referencia $p$ en el sentido de $D_{\mathrm{KL}}(q\|p)$. No es una distancia métrica: puede ser infinita, no es simétrica y no satisface en general la desigualdad triangular.

## Lenguaje y sistemas: vocabulario de transición

**Representación vectorial o embedding:** lista de números que representa un token o texto para que el modelo pueda calcular con él. Sus valores se aprenden o se calculan con un modelo entrenado.

**Atención:** cálculo que combina información de distintas posiciones y asigna diferente peso a cada una. El nombre no significa que la máquina tenga una intención consciente.

**Query, key y value:** tres proyecciones del mismo token o de fuentes distintas. Query y key producen scores; los pesos normalizados combinan values.

**Máscara causal:** restricción que impide a una posición atender a tokens futuros. Las conexiones prohibidas reciben $-\infty$ antes de softmax y terminan con peso cero.

**Multi-head attention:** varias atenciones con proyecciones distintas que operan en paralelo; sus salidas se concatenan y proyectan.

**LM head:** capa que convierte una representación del transformer en un logit por token del vocabulario.

**Ventana de contexto:** límite de tokens que el sistema puede considerar en el contexto definido. No indica cuántos pesos tiene ni cuántos números contiene cada vector.

**Inferencia:** depende del tema. En un modelo probabilístico puede significar calcular o aproximar una distribución de variables desconocidas después de observar datos. En un LLM suele referirse a ejecutar el modelo ya entrenado para producir una salida. El segundo uso no implica actualizar sus pesos.

**Prompt:** la entrada con la que orientas al modelo: puede incluir una pregunta, instrucciones, documentos y ejemplos.

**Aprendizaje en contexto:** dar ejemplos dentro del prompt para orientar la respuesta sin cambiar los pesos. **Ajuste fino:** entrenar parámetros para adaptar el comportamiento del modelo.

**SFT:** ajuste supervisado sobre demostraciones de instrucción y respuesta. Conserva la predicción de siguiente token, pero cambia el corpus.

**RLHF:** ajuste por preferencias humanas que suele entrenar un modelo de recompensa y después optimizar una política con aprendizaje por refuerzo.

**DPO:** optimización directa de pares preferido/rechazado sin un modelo de recompensa separado ni bucle de PPO.

**Constitutional AI:** enfoque que usa principios escritos para criticar y revisar respuestas y puede usar preferencias generadas por IA junto a señales humanas.

**Política de referencia:** copia congelada del modelo usada para limitar cuánto se aleja una política durante el ajuste por preferencias.

**Greedy:** elegir en cada paso el token de mayor score. Es una decisión local y no maximiza necesariamente toda la secuencia.

**Temperatura:** divisor positivo aplicado a logits. Menor que 1 concentra la distribución; mayor que 1 la aplana.

**Top-k:** conserva una cantidad fija de candidatos. **Top-p:** conserva el prefijo mínimo de tokens cuya probabilidad acumulada alcanza un umbral.

**Salida estructurada:** respuesta limitada a un esquema. Cumplir el esquema no garantiza que el contenido sea correcto.

**Test-time compute:** cómputo adicional utilizado durante inferencia, por ejemplo tokens internos de razonamiento o múltiples rutas.

**RAG:** buscar información pertinente y entregarla al modelo para que responda con ese contexto. Ejemplo: recuperar un apartado de tu PDF antes de explicarlo.

**Agente:** en el marco clásico, sistema que percibe un entorno y actúa sobre él. En el criterio operativo de este curso, el agente basado en LLM puede elegir acciones, usar herramientas, observar sus resultados y decidir si continúa o termina una tarea. Por ejemplo: buscar datos, ejecutar un cálculo y comprobar si resolvió la pregunta. El LLM puede ser una parte del sistema; darle un prompt o hacer una sola búsqueda no constituye por sí solo un ciclo de agente.

## Embeddings y recuperación: vocabulario de la sesión 06

**Embedding de texto:** vector de dimensión fija calculado para una oración o fragmento completo. La cercanía tiene sentido según el entrenamiento y la métrica usada. [[28 S06 - Qué es un embedding y qué significa cercanía|Ejemplo visual]].

**Vector contextualizado de token:** representación de un token después de procesar el resto del texto; difiere del vector fijo de entrada asociado a su ID. [[29 S06 - De tokens a un vector de texto|Tres niveles de representación]].

**Pooling:** operación que resume varios vectores de token en uno de texto. MEAN promedia, CLS selecciona una posición y MAX toma máximos por coordenada. [[29 S06 - De tokens a un vector de texto#2. El problema de longitud variable|Cálculo explicado]].

**SBERT:** familia estudiada en la sesión que adapta un encoder para producir embeddings de oraciones comparables, usando entrenamiento sobre relaciones entre textos. [[30 S06 - Cómo se entrena SBERT y por qué permite buscar|Entrenamiento]].

**Bi-encoder:** calcula el embedding de cada texto por separado; permite guardar los vectores de los documentos. **Cross-encoder:** recibe el par junto y puntúa ese par, con mayor costo al comparar muchos candidatos. [[30 S06 - Cómo se entrena SBERT y por qué permite buscar#4. Bi-encoder y cross-encoder|Diagrama]].

**Coseno:** similitud que compara la orientación de dos vectores no nulos. **Producto punto:** suma de productos por coordenada; también responde a la longitud si los vectores no están normalizados. [[31 S06 - Coseno producto punto y normalización|Contraejemplo]].

**Normalización L2:** dividir un vector por su norma para dejarla en 1. Con consulta y documento normalizados, producto punto y coseno coinciden en valor. [[31 S06 - Coseno producto punto y normalización#2. Qué hace normalizar|Derivación]].

**Truncamiento:** descarte de tokens que exceden el máximo aceptado por el modelo; puede ocultar al buscador la parte final de un fragmento sin producir un error visible. [[32 S06 - Elegir modelo y reconocer límites#2. El límite de tokens puede borrar contenido sin error visible|Caso 512/128]].

## Índices, bases vectoriales y RAG — sesiones 07 a 10

**kNN:** búsqueda de los k vecinos más cercanos según una medida. «Exacto» significa devolver el top-k sobre los vectores disponibles, sin garantizar que contenga evidencia útil. [[80 S07 - Búsqueda exacta aproximación y costo]].

**ANN:** búsqueda aproximada que reduce candidatos y puede perder vecinos del exacto. Su recall compara IDs con ese exacto; el recall de evidencia compara contra documentos anotados como relevantes. Son referencias distintas. [[83 S07 - Recall del índice latencia y memoria]].

**IVF:** índice que agrupa vectores en listas. `nlist` fija cuántas; `nprobe`, cuántas se abren al consultar. Abrir solo una puede perder el vecino al otro lado de una frontera. [[81 S07 - IVF celdas centroides y nprobe]].

**HNSW:** grafo de proximidad con capas para orientar y refinar la búsqueda. `M` controla conexiones; `ef_construction`, exploración al construir; `ef_search`, exploración al consultar, según la implementación. Más exploración no vuelve mejores los embeddings. [[82 S07 - HNSW capas conexiones y exploración]].

**Payload:** metadatos asociados a un punto, como fuente, texto o tema. Un filtro define qué puntos pueden responder a la consulta; la similitud ordena candidatos elegibles. [[84 S07 - Colecciones payload filtros y operación]].

**Fragmentación (chunking):** dividir documentos en unidades recuperables. El solapamiento repite parte del texto entre vecinos para conservar continuidad, pero puede duplicar evidencia y aumentar costo. [[37 S08 - Estrategias de fragmentación y solapamiento]].

**BM25:** puntaje de recuperación léxica que considera coincidencias de términos, rareza y longitud del documento. **RRF:** fusión de listas que suma aportes según la posición de cada resultado; no mezcla directamente scores de escalas distintas. [[38 S08 - Búsqueda léxica densa y fusión RRF]].

**Reranking:** volver a puntuar una lista de candidatos con otro criterio o modelo. No puede rescatar un fragmento que nunca llegó a esa lista. [[39 S08 - Reranking contexto y abstención]].

**Golden set:** preguntas, evidencia y expectativas anotadas para evaluar un sistema. Su cobertura, caducidad y ambigüedades afectan qué significa una buena métrica. [[44 S09 - Golden sets anotación y caducidad]].

**Hit Rate@k:** fracción de consultas que recuperan al menos una evidencia anotada en las primeras k posiciones. **Recall@k de evidencia:** fracción de elementos relevantes recuperados, con denominador definido por la anotación. **MRR:** promedio del inverso de la posición del primer relevante. Recuperar uno no prueba que estén todos los necesarios. [[43 S09 - Hit Rate Recall MRR MAP y nDCG paso a paso]].

**MAP de recuperación:** media de las precisiones promedio por consulta; no confundirla con MAP bayesiano, estimación que maximiza la posterior. **nDCG:** ganancia acumulada descontada dividida por el ideal calculado con todos los elementos relevantes elegibles, no solo los recuperados. [[43 S09 - Hit Rate Recall MRR MAP y nDCG paso a paso]].

**Abstención:** reconocer que la evidencia disponible no permite responder. Hay que evaluar tanto abstención correcta en preguntas negativas como abstención indebida en preguntas respondibles. **Fidelidad:** respaldo de las afirmaciones en el contexto; una cita existente no basta si no respalda lo afirmado. [[45 S09 - Preguntas negativas y abstención]] y [[46 S09 - Evaluar respuestas fidelidad y citas]].

**p95 / p99 de latencia:** percentiles: tiempos que no superan aproximadamente el 95 % o 99 % de las consultas de la muestra. No son el máximo ni garantías para cualquier consulta futura. [[83 S07 - Recall del índice latencia y memoria]].

## Tres distinciones para repasar siempre

Probabilidad no es certeza. Representar una relación no identifica necesariamente una causa. Cambiar el contexto de entrada no equivale a entrenar los pesos.

## Términos de los libros incorporados a las notas

| Término | Explicación | Dónde verlo aplicado |
| --- | --- | --- |
| Capacidad | Conjunto de funciones que un modelo puede representar | [[02 S00 - Reglas modelos y aprendizaje desde datos]] |
| Costo esperado | Promedio del costo de una acción según las probabilidades de cada resultado | [[06 S01 - Modelos discriminativos y generativos]] |
| Prior conjugado | Prior cuya familia se conserva al actualizar con una verosimilitud determinada | [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]] |
| MAP | Valor que maximiza la posterior | [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]] |
| Posterior predictiva | Distribución de resultados nuevos promediando incertidumbre sobre parámetros | [[15 AMPLIACIÓN - Bayes incertidumbre y suavizado con números]] |
| Inferencia amortizada | Red entrenada para aproximar la posterior de distintos datos | [[10 S01 - VAE espacio latente y ELBO]] |
| Representación contextual | Vector calculado en función del contexto de una entrada | [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] |
| Autosupervisión | Objetivos de aprendizaje construidos desde los propios datos | [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] |
| Logits | Puntajes antes de normalizarlos como probabilidades | [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] |
| Entropía cruzada | Pérdida que, con objetivos categóricos, penaliza la baja probabilidad del objetivo observado | [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] |
| Perplejidad | Exponencial de la pérdida promedio por token con logaritmos naturales | [[16 AMPLIACIÓN - Cómo aprende un LLM desde el texto]] |
| Atención escalada | Softmax de $QK^\top/\sqrt{d_k}$ aplicado a V | [[19 S02 - Atención Q K V paso a paso]] |
| Decoder-only | Transformer causal que trata el prompt como prefijo de la misma secuencia | [[20 S02 - Posición familias y decoder-only]] |
| Modelo base | Resultado del preentrenamiento antes del ajuste para instrucciones | [[21 S03 - Preentrenamiento autosupervisado y MLE]] |
| Preferencia | Orden relativo entre respuestas al mismo prompt | [[22 S03 - SFT RLHF DPO y Constitutional AI]] |
| Nucleus sampling | Otro nombre de top-p | [[23 S04 - Greedy temperatura top-k y top-p]] |
| Auto-consistencia | Muestrear varias rutas y votar la respuesta final | [[24 S04 - Zero-shot few-shot y razonamiento]] |
| Validación semántica | Comprobar que un valor bien formado sea correcto para el caso | [[25 S04 - Salidas estructuradas costo y razonamiento interno]] |
| Latencia de extremo a extremo | Tiempo de reloj de la llamada completa | [[26 S05 - Diseñar una comparación de modelos]] |

Esta ampliación reúne términos de Bishop, Murphy, Alammar y Grootendorst, y Raschka; las notas enlazadas indican las páginas consultadas. La definición resumida sirve para recordar; el ejemplo de cada nota explica el mecanismo.

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Qué diferencia hay entre z y theta?
> z es una variable latente inferida o muestreada para los datos; theta representa parámetros aprendidos del modelo.

> [!question]- ¿Muestrear es tomar siempre la opción más probable?
> No. El muestreo elige según una distribución; tomar siempre el máximo es una estrategia diferente.

> [!question]- ¿Ventana de contexto y dimensión de embeddings son lo mismo?
> No. Una mide cantidad de tokens de contexto; la otra cantidad de coordenadas de los vectores.

> [!question]- ¿Dar tres ejemplos en el prompt es ajuste fino?
> No si no se actualizan los pesos. Es uso de ejemplos en contexto.


> [!question]- ¿MAP es lo mismo que posterior predictiva?
> No. MAP elige un valor del parámetro; la posterior predictiva describe resultados nuevos integrando sobre su incertidumbre.


## Ampliación de agentes — sesión 11

El [[67 S11 - Ejercicios resueltos y repaso activo#Glosario de bolsillo|glosario de la sesión 11]] desarrolla harness, herramientas, esquemas, observaciones, estado, trazas, utilidad, idempotencia y parada. Para distinguir el sentido de «agente» en el marco clásico y en el criterio operativo del curso, consulta [[60 S11 - Chatbot pipeline RAG y agente quién decide]] y [[61 S11 - PEAS racionalidad y observación parcial]].

## Ampliación de patrones — sesión 12

El [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/78 S12 - Ejercicios resueltos y repaso activo#Glosario de bolsillo|glosario de la sesión 12]] define trayectoria, Thought, Action, Observation, verificador, reflexión, ablación y replanning. Las notas 70–76 explican sus diferencias y mecanismos.


## MCP y descubrimiento — sesión 13

| Término | Explicación | Ejemplo |
| --- | --- | --- |
| MCP | Protocolo para intercambiar capacidades y contexto con proveedores | Descubrir y solicitar una consulta de ventas |
| Host | Aplicación que coordina modelo, clientes y políticas | Agente analista |
| Cliente MCP | Conector que habla con un servidor | Cliente del proveedor de ventas |
| Servidor MCP | Proveedor de recursos, herramientas o plantillas | Servicio que publica consultar_ventas |
| Catálogo | Lista de contratos publicados | Nombre, descripción y esquema de entrada |
| Descubrimiento | Obtener capacidades durante la ejecución | Consultar tools/list |
| Adaptador | Conversión entre contratos de dos componentes | Traducir inputSchema al formato de la API del modelo |
| Dispatcher | Componente que enruta una llamada | Resolver ventas__consultar_ventas hacia su servidor |
| JSON-RPC | Formato para pedir una operación y correlacionar su respuesta | Método tools/call con id 7 |
| Tool | Operación invocable | Calcular un total |
| Resource | Contenido disponible para contexto | Reporte de ventas |
| Prompt | Plantilla reutilizable de mensajes | Estructura de comparación de períodos |
| TTL | Tiempo de frescura de una respuesta cacheada | ttlMs en milisegundos |
| Costo marginal | Trabajo adicional de incorporar la siguiente capacidad | Añadir una tool sin editar la lógica del agente |

Desarrollo: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|índice de la sesión 13]]. Definiciones didácticas propias basadas en el PDF de clase y la documentación oficial contrastada; fuentes en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/16 FUENTES - Sesión 13 MCP y validación|registro de S13]].
