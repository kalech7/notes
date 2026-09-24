---
title: "41 S08 - Recordatorio y preguntas de comprensión"
sesion: "08"
tags:
  - maestria/ia-generativa
  - rag
  - estudio
fuente: "[[sesion-08.pdf]]"
---

# 41 S08 - Recordatorio y preguntas de comprensión

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[34 S08 - Guía para entender fragmentación y recuperación|Guía de la sesión 08]]

## 1. Una explicación que deberías poder reconstruir

Un RAG permite que un modelo responda usando documentos externos. Para hacerlo, primero convierte esos documentos en fragmentos que conservan sentido y caben en el codificador. Después construye índices para localizarlos. Cuando llega una pregunta, busca candidatos, decide qué evidencia incluir y pide al modelo que redacte una respuesta sustentada. Si la respuesta falla, revisa en qué etapa se perdió o se utilizó mal la evidencia.

Esta explicación es el esqueleto. Entender la sesión significa poder explicar **por qué cada paso es necesario**, no repetir los nombres de las herramientas.

## 2. La cadena para recordar

**Conservar → dividir → representar → recuperar → seleccionar → responder → comprobar.**

| Verbo | Pregunta que activa la memoria |
| --- | --- |
| Conservar | ¿El texto extraído mantiene la información y sus relaciones? |
| Dividir | ¿Qué debe viajar junto para tener sentido? |
| Representar | ¿Qué texto vio realmente el codificador? |
| Recuperar | ¿Qué señal usamos para encontrar candidatos? |
| Seleccionar | ¿Cuál de esos candidatos conviene enviar y en qué orden? |
| Responder | ¿Qué afirmaciones permite sostener la evidencia? |
| Comprobar | ¿Puedo rastrear la respuesta y localizar un fallo? |

## 3. Distinciones que evitan la mayoría de las confusiones

| No confundas | La diferencia que debes poder explicar |
| --- | --- |
| Texto guardado / texto representado | El payload puede estar completo aunque el embedding se haya calculado con un prefijo |
| Palabras / tokens | La longitud relevante depende del tokenizador y de la entrada final |
| Tamaño del chunk / límite del embedding / ventana del LLM | Son decisiones o límites de etapas distintas |
| Parecido / evidencia suficiente | Una relación temática no implica que el pasaje responda la pregunta |
| Recuperar / reordenar | El primero obtiene candidatos; el segundo vuelve a ordenar los disponibles |
| Top-k / $k_{\mathrm{RRF}}$ / $k_1$ de BM25 | Cantidad de resultados / suavizado de rangos / saturación de frecuencia |
| Puntaje / probabilidad de verdad | Un número alto en un ranking no verifica las afirmaciones |
| Cita / sustento | Una referencia solo sustenta si el pasaje realmente respalda lo dicho |
| Falta en el contexto / falta en el corpus | La búsqueda puede haber omitido información existente |
| RAG / agente | Recuperación puede ser parte de un agente; un pipeline RAG fijo no implica autonomía |

## 4. Preguntas para explicar en voz alta

Intenta responder antes de desplegar. No hace falta usar las mismas palabras: debe conservarse la relación entre causa y consecuencia.

> [!question]- ¿Por qué un LLM capaz necesita recuperación?
> Porque capacidad de lenguaje y acceso a información son distintos. La recuperación aporta documentos que no tienen por qué estar reflejados en los parámetros y permite rastrear la evidencia usada.

> [!question]- ¿Qué cambia en el RAG básico cuando se actualiza una fuente?
> Cambia el contenido consultable y, al actualizar su índice, la evidencia que puede llegar al prompt. No es necesario modificar los pesos del generador para incorporar esa fuente al flujo.

> [!question]- ¿Por qué el chunk es una decisión sobre significado?
> Porque decide qué partes de una afirmación viajan juntas. Una regla sin sujeto, excepción o condición puede resultar ambigua o inducir una respuesta falsa.

> [!question]- ¿Cómo puede funcionar el sistema sin errores técnicos y aun así perder información?
> Si el codificador trunca silenciosamente entradas largas, genera vectores válidos de texto incompleto. El funcionamiento técnico no prueba que toda la información esté representada.

> [!question]- ¿Por qué el solapamiento del 20 % produce aproximadamente un 25 % más de ventanas?
> Porque cada ventana avanza el 80 % de su tamaño. Para cubrir un texto largo se necesitan aproximadamente $1/0.8=1.25$ veces las ventanas. Los bordes hacen que la razón finita pueda ser distinta.

> [!question]- ¿Qué diferencia hay entre estructura y semántica al fragmentar?
> La estructura utiliza señales explícitas como párrafos y títulos. La fragmentación semántica aplica un criterio de cambio de significado. Pueden combinarse, pero no son lo mismo.

> [!question]- ¿Por qué la búsqueda densa puede devolver algo cuando no hay respuesta?
> Porque ordena candidatos disponibles por cercanía. La existencia de un vecino mejor que los demás no implica que alguno contenga evidencia suficiente. Hace falta una política de rechazo o verificación adicional.

> [!question]- ¿Por qué BM25 da menos valor a repeticiones adicionales?
> Porque muchas repeticiones no aportan proporcionalmente la misma información sobre relevancia. La saturación evita que repetir una palabra domine sin límite el aporte de ese término.

> [!question]- ¿Por qué RRF usa rangos?
> Porque los puntajes de diferentes buscadores no tienen una escala común. Los rangos permiten combinar preferencias, aunque pierden información sobre las diferencias originales de puntuación.

> [!question]- ¿Por qué un cross-encoder es más costoso que comparar vectores precalculados?
> Porque debe procesar conjuntamente cada pareja consulta-fragmento. El resultado para una pregunta no puede precalcularse antes de que esa pregunta exista.

> [!question]- ¿Por qué recuperar más y mandar más contexto son decisiones diferentes?
> Puedes ampliar la lista inicial para no perder candidatos y después seleccionar pocos fragmentos suficientes. El generador no necesita recibir todos los resultados encontrados.

> [!question]- ¿Qué observarías antes de cambiar el prompt de una respuesta equivocada?
> La fuente, la extracción, los fragmentos, el truncamiento, los candidatos y el contexto final. Solo entonces sabría si el generador tuvo evidencia suficiente para responder bien.

## 5. Cómo saber si ya lo entendiste

Puedes considerar que tienes una comprensión inicial sólida si puedes dibujar las dos etapas de RAG sin mirar, explicar las diferencias de la tabla y justificar una decisión sin recurrir a «porque así viene por defecto».

Si recuerdas un término pero no puedes explicar qué problema resuelve, regresa a esa nota. Si puedes definirlo pero no distinguirlo del paso anterior, repasa el flujo completo. Si comprendes el mecanismo pero dudas de una fórmula, traduce primero cada símbolo a una cantidad concreta.

## 6. Un repaso breve que exige recordar

Cierra las notas y reconstruye la cadena de siete verbos. Escoge tres preguntas y respóndelas en voz alta. Después abre las soluciones, identifica qué relación faltaba y escribe una corrección breve con tus propias palabras. En otro momento vuelve a intentar las preguntas que no pudiste explicar.

No necesitas memorizar 128, 512, 8192, 20 o 5 como si fueran leyes. Necesitas recordar **qué límite representa cada número, qué componente lo usa y cómo comprobarlo**.

## 7. Comprobar profundidad: anticipar consecuencias

Estas preguntas no se responden repitiendo una definición. Intenta explicar el mecanismo, qué esperarías observar y qué dato faltaría para concluir.

> [!question]- Cambio solo el modelo de las preguntas por otro con igual dimensión. ¿Por qué podría empeorar todo?
> Tener el mismo número de coordenadas no significa que las coordenadas representen las mismas relaciones. Si el nuevo modelo no es compatible con el que produjo los vectores del corpus, las comparaciones pierden su significado previsto. Debería comprobarse la compatibilidad del par de codificadores; normalmente cambiar a otro espacio exige recalcular también los vectores documentales.

> [!question]- Todos los fragmentos caben en el codificador. ¿Ya resolví el problema de representación?
> Resolviste la condición de longitud observada en esa etapa, no toda la calidad representacional. Un vector todavía puede no distinguir una negación o un número. Además, el reranker y el generador tienen entradas y límites propios. Hay que inspeccionar la información útil que sobrevive en cada paso.

> [!question]- Añado títulos solo después de buscar. ¿Puede eso mejorar los resultados de esa búsqueda?
> No retrospectivamente: el ranking ya se calculó con las representaciones previas. Puede mejorar la interpretación del contexto final. Para que el título influya en la búsqueda densa, tendría que formar parte de la entrada representada o de otro mecanismo de selección que realmente se utilice.

> [!question]- Recupero más fragmentos, pero casi todos repiten el mismo párrafo. ¿Por qué podría no mejorar la respuesta?
> Aumentó la cantidad de resultados, pero poco la información distinta. Si falta una excepción en otra sección, las repeticiones no la reemplazan. Hay que comprobar diversidad y suficiencia del conjunto, además del número de candidatos.

> [!question]- Un reranker mejora el orden y la respuesta sigue equivocada. ¿Es una contradicción?
> No. Puede haber priorizado un pasaje relevante pero insuficiente, haber recibido candidatos que omiten otra fuente necesaria o haber entregado evidencia que el generador interpreta mal. Mejora de una etapa no equivale a corrección del sistema completo.

> [!question]- La respuesta tiene citas válidas y aun así da una política obsoleta. ¿Qué relación faltó comprobar?
> Las citas permiten localizar fuentes, pero no garantizan que sean las aplicables. Debe verificarse su vigencia y alcance. Una respuesta puede reproducir fielmente un documento antiguo y no responder correctamente sobre la política actual.

## 8. Una pauta para evaluar tu propia explicación

Una explicación **inicial** identifica qué hace el componente. Una explicación **conectada** explica sus entradas, salidas y su dependencia de las otras etapas. Una explicación **profunda para esta sesión** permite anticipar qué puede cambiar al modificarlo, reconocer cuándo no resolvería el problema y decir qué observarías para comprobarlo.

Por ejemplo, para el reranking deberías poder explicar por qué depende de la consulta, por qué no puede añadir un candidato ausente, cómo afecta el límite de entrada y por qué un mejor ranking no garantiza una respuesta correcta. No es necesario repetir una fórmula para demostrar esas relaciones.

Si te cuesta una pregunta, vuelve al mecanismo concreto: [[35 S08 - RAG contexto memoria y generación fundamentada|entrada y generación]], [[36 S08 - Fragmentos tokens y truncamiento|representación y límites]], [[37 S08 - Estrategias de fragmentación y solapamiento|unidades de sentido]], [[38 S08 - Búsqueda léxica densa y fusión RRF|señales de búsqueda]], [[39 S08 - Reranking contexto y abstención|selección y sustento]] o [[40 S08 - Diagnóstico de fallos y decisiones del taller|diagnóstico con evidencia]].

> [!abstract] Qué llevarte de toda la sesión
> **La calidad de la respuesta empieza antes de generar: en cómo conservas, representas y seleccionas la evidencia.**

**Base:** síntesis propia de [[sesion-08.pdf]] y de las notas 35–40. No constituye un examen ni una rúbrica oficial del curso.
