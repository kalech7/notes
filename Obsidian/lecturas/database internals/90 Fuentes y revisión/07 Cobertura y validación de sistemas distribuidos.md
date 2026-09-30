---
title: "Database Internals — Cobertura y validación de sistemas distribuidos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 8
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
  - fuentes
---

# Cobertura y validación de sistemas distribuidos

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Capítulo 8]]

Para saber qué respaldan estas notas, conviene distinguir el material efectivamente compartido de los capítulos que el libro anuncia. El escaneo permite leer la apertura de la Parte II y el contenido del capítulo 8 hasta su resumen; no contiene el capítulo 9 ni una bibliografía posterior.

## Fuente conservada y lectura

Fuente: `/Users/alech/Downloads/CamScanner 2026-09-30 16.40.pdf`. Copia sin modificar: [[Obsidian/lecturas/database internals/Materiales/08 Sistemas distribuidos.pdf|08 Sistemas distribuidos.pdf]]. Ambos archivos tienen 26 páginas y SHA-256 `74681231bac1f955c54baa99b233268b7f9368b144754d2f51695dba8d477668`.

Se renderizaron y leyeron visualmente **las 26 páginas**, orientando las páginas apaisadas según su posición real. Hay cambios de orientación dentro del mismo archivo: aplicar un solo giro a todos los escaneos deja algunos invertidos. Se revisaron las cifras de la figura 8-1, el pie de fair-loss de la impresa 183 y los dos contadores de orden en la 185 directamente sobre las imágenes. No se utilizó OCR como sustituto de la lectura; la correspondencia se obtuvo de folios visibles y continuidad.

PDF 1–3 corresponden a la apertura de Parte II y definiciones básicas. Sus folios no aparecen en el escaneo: **no se les asigna un número impreso inventado**. PDF 4–26 corresponden a las impresas 171–193, con `impresa = PDF + 167`. En PDF 25 el folio está fuera del encuadre y se identifica como 192 por continuidad entre 191 y 193.

No se detectó una página omitida entre las páginas disponibles. El archivo termina tras *Summary* en la impresa 193. No se afirma que incluya posibles páginas bibliográficas posteriores, y las remisiones a capítulos 9, 12, Spanner y Raft se explican como anticipaciones del libro, no como capítulos leídos.

## Mapa de todas las páginas

Los números de nota remiten a [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|la ruta de lectura del capítulo 8]].

| PDF | Impresa | Contenido verificado | Notas |
|---:|---:|---|---|
| 1 | No visible | Parte II, epígrafe de Lamport, motivación, escala vertical y horizontal, clústeres | 01 |
| 2 | No visible | Basic Definitions: participantes, estado local, enlaces, relojes, algoritmos, estados y pasos | 01 |
| 3 | No visible | Coordinación, cooperación, diseminación, consenso y recorrido práctico de Parte II | 01 |
| 4 | 171 | Apertura del capítulo 8, variable x y ejecución concurrente | 02 |
| 5 | 172 | Figura 8-1: resultados 2, 3, 4, 6; interleavings y modelos de consistencia | 02, 12 |
| 6 | 173 | Concurrencia/paralelismo, estado compartido remoto, timeout, sincronía y tolerancia | 02, 03 |
| 7 | 174 | Redundancia, falacias, conexión interrumpida y latencia | 02, 03 |
| 8 | 175 | Falacias adicionales, ancho de banda, procesamiento, heterogeneidad, colas y backpressure | 03, 04 |
| 9 | 176 | Desacoplamiento, pipelining, ráfagas, tamaño de cola, resultados negativos y epígrafe de tiempo | 04, 05 |
| 10 | 177 | Desfase temporal, incertidumbre, fuentes de tiempo, consistencia, conflictos y metadatos | 05 |
| 11 | 178 | Ejemplos históricos de esquema y ring; API local/remota, serialización y caídas | 05, 06 |
| 12 | 179 | Heartbeats, detectores, particiones, asimetría, fallas parciales y pruebas de fallo | 06 |
| 13 | 180 | Inyección de fallos y herramientas mencionadas; cascadas y recuperación que sobrecarga | 06 |
| 14 | 181 | Circuit breakers, backoff, jitter, corrupción, validación y coordinación de recursos | 06 |
| 15 | 182 | Abstracciones de sistemas distribuidos, enlaces, estados de un envío y figura 8-2 | 07 |
| 16 | 183 | Fair-loss y su pie preciso, duplicación finita, no creación, ACK e identificadores | 07 |
| 17 | 184 | Figura 8-3, ACK que se pierde, retransmisión, stubborn links y duplicados | 07, 08 |
| 18 | 185 | Idempotencia, cargos repetidos, deduplicación, FIFO, contadores y buffer | 08, 12 |
| 19 | 186 | Enlace perfecto, TCP y ámbito de sesión; epígrafe de Verraes y semánticas de entrega | 07, 08 |
| 20 | 187 | Transporte frente a procesamiento, persistencia, conocimiento común y apertura de dos generales | 08, 09 |
| 21 | 188 | Mensajeros y cadena de confirmaciones de dos generales; figura 8-4 | 09 |
| 22 | 189 | Último ACK, ausencia de cotas, consenso, acuerdo/validez/terminación y FLP | 09, 10 |
| 23 | 190 | FLP, sistemas asíncronos/síncronos, relojes y efecto de los supuestos temporales | 10 |
| 24 | 191 | Sincronía parcial, detección equivocada y modelos de falla; crash-stop | 10, 11 |
| 25 | 192, inferida | Identidad y reintegración, crash-recovery, estado durable y omisiones | 11 |
| 26 | 193 | Fallas arbitrarias/bizantinas, manejo de fallos y resumen del capítulo | 11 |

Las cuatro figuras se explican de manera autónoma: la tabla de nota 02 reconstruye 8-1; las capas y el diagrama de nota 07 desarrollan 8-2 y 8-3; el diagrama de nota 09 reconstruye la cadena de conocimiento de 8-4. No se transcriben párrafos del libro ni se pide al lector consultar la fuente para entender un concepto.

## Precisiones técnicas

Estas aclaraciones conservan el propósito del capítulo y delimitan frases que, tomadas literalmente, podrían dar garantías equivocadas:

- **FLP:** la impresa 189–190 habla de consenso en tiempo acotado. El artículo original establece posibilidad de **no terminación**, incluso ante una sola caída, en el modelo determinista totalmente asíncrono. El problema no es solo desconocer una duración máxima. La nota 10 distingue seguridad de vivacidad. [Fischer, Lynch y Paterson, 1985](https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf).
- **Sincronía parcial:** se usa la formulación de cotas desconocidas o válidas eventualmente; decir «la mayoría del tiempo» sin condiciones no define la garantía formal. La sincronía no exige relojes de pared idénticos. [Dwork, Lynch y Stockmeyer, 1988](https://groups.csail.mit.edu/tds/papers/Lynch/jacm88.pdf).
- **Acuerdo y terminación:** las garantías se expresan para procesos correctos, salvo que se declare la variante uniforme. El acuerdo no requiere esperar una respuesta unánime de procesos caídos. Validez impide inventar el valor y terminación aporta progreso bajo el modelo.
- **Fair-loss:** se conserva la formulación precisa del pie de página: infinitos envíos del mismo mensaje entre procesos correctos implican infinitas entregas. No se aplica esa garantía a una partición permanente ni se propone tráfico infinito como implementación.
- **Enlace perfecto y FIFO:** entrega eventual, no duplicación y no creación no incorporan automáticamente orden FIFO. El buffer y los contadores son un mecanismo adicional de orden por secuencia; recibir y procesar no son el mismo hito.
- **TCP:** se distingue flujo de bytes de mensajes de aplicación, ámbito de conexión de reconexión, y ACK de transporte de un efecto durable. La especificación describe servicio fiable y ordenado de bytes. [RFC 9293 §2.2](https://www.rfc-editor.org/rfc/rfc9293.html#section-2.2).
- **Una vez:** la ausencia de reintentos es un ejemplo sencillo de a lo sumo una vez, no su definición universal. Los efectos únicos requieren ámbito y contrato: identidad estable, efecto e ID atómicos, memoria de deduplicación y condiciones de recuperación. No se transforma la discusión del libro en «exactamente una vez es imposible siempre».
- **Pruebas:** se matiza la frase de la impresa 180 sobre encontrar todo problema. La inyección de fallos mejora evidencia, pero una batería finita no demuestra ausencia de cualquier bug posible.

Los casos históricos de Cassandra se atribuyen al libro y no se describen como errores actuales. Toxiproxy, Chaos Monkey, CharybdeFS y CrashMonkey se registran como herramientas mencionadas en el capítulo; no se recomienda una versión actual ni se han ejecutado sobre sistemas reales.

## Contexto, epígrafes y elaboración propia

Cada nota comienza con una frase que conecta el problema nuevo con el anterior. Se conservan tres epígrafes breves traducidos y atribuidos: Lamport en apertura de Parte II; Ford Prefect, personaje de la obra de Douglas Adams, en tiempo; y Mathias Verraes en orden/entrega. En cada caso se explica la relación de la frase con el concepto y, en el tercero, se conservan la numeración fuera de orden y la repetición que producen el chiste.

Cifras de colas, tiempos de red, montos de cobro y IDs son ejemplos propios. La tabla de carreras conserva el ejemplo del libro; el programa enumera las seis historias de su modelo abstracto. Las notas separan garantía matemática e implementación, y no confunden un contador lógico con hora de calendario ni un timeout con prueba de caída.

## Recursos y verificación realizada

Se crearon 13 notas de capítulo: índice, contextual de Parte II, diez temáticas y laboratorio/repaso, más esta nota de cobertura. Hay cuatro diagramas Mermaid en las notas 00, 04, 07 y 09.

El PNG [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 08/ack_perdido.png|ack_perdido.png]] fue generado con [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 08/generar_visuales.py|generar_visuales.py]] y revisado visualmente: texto completo, cajas sin solapes y contraste suficiente. La explicación inmediatamente debajo del embed forma parte de nota 08. Es un esquema de aplicación, no una reproducción literal de TCP.

Se ejecutó [[Obsidian/lecturas/database internals/Materiales/Laboratorios/08 sistemas_distribuidos.py|08 sistemas_distribuidos.py]]. Todas las aserciones pasaron: seis historias concurrentes con cuatro resultados, cola de 180 y vaciado de 6 s, FIFO `1,2,3,4,5` y cobros `40/20/40` para repetición sin dedup, registro recuperado y registro olvidado. El programa rechaza reutilizar un ID con otro importe. No implementa persistencia física, hilos ni un fallo real entre instrucciones.

Los cuatro Mermaid del capítulo renderizaron correctamente con mermaid-cli y Chrome. Una revisión independiente de las 13 notas comprobó claridad, atribuciones y límites técnicos; se corrigió el epígrafe de Verraes para conservar el chiste visible. La copia del PDF coincide byte a byte con el original. La validación conjunta del vault comprueba YAML, wikilinks, embeds, navegación y anclas de PDF antes de entrega; su resultado se registra en la cobertura general de esta ampliación.

## Resultado de la validación conjunta

Validación final realizada el 30 de septiembre de 2026, sin incidencias pendientes: 31 YAML nuevos, destinos de enlaces y páginas PDF válidos, navegación continua, cuatro PNG revisados y nueve Mermaid renderizados entre ambos capítulos y la ruta general. Ambos laboratorios pasaron todas sus aserciones y ambas copias PDF coinciden con los originales. El alcance y el informe están en [[Obsidian/lecturas/database internals/90 Fuentes y revisión/01 Fuentes y cobertura#Revisión conjunta de la ampliación del 30 de septiembre|Revisión conjunta de la ampliación]].

---

← [[Obsidian/lecturas/database internals/90 Fuentes y revisión/06 Cobertura y validación del capítulo 7|Capítulo 7]] · [[Obsidian/lecturas/database internals/90 Fuentes y revisión/00 Índice|Índice de fuentes]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Capítulo 8]] →
