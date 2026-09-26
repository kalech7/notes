---
title: "DDIA — Atlas visual explicado: sigue el dato y sus cambios"
created: 2026-09-25
tags:
  - lecturas/ddia
  - aprendizaje-visual
  - fundamentos
---

# DDIA — Atlas visual explicado

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/00 Índice|Guía y fundamentos]]

Los cuatro fenómenos comparten una dificultad: lo visible para una aplicación no muestra todo el estado físico o distribuido. Una actualización puede dejar bytes antiguos, un lector puede completar un campo ausente, un timeout puede ocultar un efecto terminado y una búsqueda puede devolver solo candidatos. Las imágenes son analogías originales; el texto explica el mecanismo y sus límites sin requerir los PDF.

> [!info] Recuerda antes
> - Un mismo **dato lógico** puede tener varias representaciones físicas o versiones; las reglas de visibilidad deciden cuál responde una lectura.
> - Un **contrato** permite interpretar bytes, pero no inventa hechos ausentes ni garantiza conservar campos al reescribir.
> - En sistemas distribuidos debes separar lo que un actor **observa** de lo que realmente pudo ocurrir en otro componente.

## 1. Si actualizo un pedido, ¿por qué sigue existiendo su valor antiguo?

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/05-lsm-versiones-y-compactacion.png|1100]]

### Tres estados físicos de P42

**Antes:** P42 tiene el estado `pendiente` en un archivo ordenado ya publicado. En este diseño ese archivo es inmutable: una nueva actualización no abre el archivo para sustituir sus bytes por otros.

**Nueva versión:** llega `P42 = enviado`. El motor registra la escritura según su protocolo de recuperación e incorpora la versión a la memtable, la estructura reciente en RAM. Ahora existen dos representaciones físicas del mismo pedido, pero eso no obliga a mostrar ambas como dos pedidos diferentes. Una lectura del estado actual debe seleccionar la versión vigente, aquí `enviado`.

**Después de compactar:** el motor publica un archivo nuevo que conserva las versiones necesarias. Cuando ya sea seguro, retira archivos anteriores. No modifica mágicamente el archivo ámbar dentro de su caja: crea otra caja con su propio contenido.

### Lo que hay entre el segundo y el tercer panel

La imagen omite pasos para que la idea central sea visible. Este es el recorrido completo simplificado:

1. **Recuperación:** el cambio se anota en el log correspondiente; la confirmación depende de la garantía de persistencia configurada. RAM, por sí sola, no basta para sobrevivir al apagado.
2. **Acumulación:** una memtable ordenada recibe cambios.
3. **Flush:** al alcanzar el umbral, se congela esa memtable y se escribe una SSTable ordenada; otra memtable puede seguir recibiendo cambios.
4. **Compactación:** se combinan SSTables. Si la misma clave aparece varias veces, se conservan las versiones que exigen la lectura y la política del motor.
5. **Publicación y retirada:** se hace visible el resultado válido antes de retirar entradas anteriores que ya no hacen falta.

No todos los motores implementan esos pasos igual. La ilustración representa un modelo de estudio, no una secuencia universal de llamadas.

### Qué cambia cuando hay una eliminación o una lectura histórica

Si llega `borrar P42`, retirar solo la copia más reciente sería peligroso: todavía podría encontrarse `pendiente` en un archivo antiguo. Una **tombstone** dice que la ausencia también tiene una versión y que no se debe recuperar un valor anterior. Solo se retira cuando las reglas del motor garantizan que no reaparecerá información que debía permanecer borrada.

Si una lectura usa un **snapshot**, pide ver el estado correspondiente a un punto lógico anterior. Puede necesitar una versión que ya no es la más nueva. Por eso “compactar” no significa necesariamente “guardar solo el último valor de cada clave y borrar todo lo demás”.

> [!question]- En el panel central, ¿tener dos versiones significa tener dos pedidos?
> No. Son dos estados físicos de una misma identidad. La consulta y las reglas de visibilidad determinan cuál corresponde al estado que pidió el lector.

**Imagen mental para recordar:** una ficha nueva puede cambiar la respuesta sin destruir al instante el archivo antiguo. Desarrollo completo en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/02 LSM SSTables compactación y Bloom|LSM, SSTables, compactación y Bloom]].

## 2. ¿Cómo lee un programa nuevo un registro al que le falta un campo?

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/06-avro-dos-esquemas.png|1100]]

### Dos instrucciones diferentes sobre la mesa

El paquete representa datos antiguos: el ID `P42` y el importe `1200`. El papel de la izquierda dice **cómo se escribieron**: primero un string para el ID, después un long para el importe. El de la derecha dice **qué espera ahora el lector**: además de esos campos, una moneda.

La imagen abrevia `total_centavos` como `total` para que se lea con claridad. No propone renombrar realmente ese campo. Los rótulos del papel son un resumen visual, no la sintaxis completa de un esquema Avro.

### Haz de decodificador

1. Consigue el esquema escritor correcto. No basta con saber que el archivo “es Avro”: hay que saber con qué estructura se escribió ese registro.
2. Interpreta los bytes según esa estructura. Así identificas `id = P42` y `total_centavos = 1200`.
3. Compara lo que el escritor produjo con lo que el lector necesita. Los campos que coinciden y tienen tipos compatibles pueden entregarse.
4. El lector espera `moneda`, pero el escritor antiguo no la tenía. Busca el **default del esquema lector** para resolver esa ausencia.
5. Como el ejemplo define `default: null` y admite null en el tipo del campo, entrega `moneda = null`.

No se agregan retrospectivamente bytes al archivo. El lector construye una representación actual a partir de datos antiguos y reglas de resolución.

### Ausente, null y valor por defecto no son lo mismo

| Situación | Lo que sabes |
|---|---|
| El esquema escritor no tenía `moneda` | El campo no formaba parte de ese registro antiguo |
| Un esquema permite `null` | Ese valor es válido para el campo |
| El esquema lector declara `default: null` | Hay una regla para completar ese campo cuando falta en el esquema escritor |
| El registro tiene `moneda: "USD"` | El dato contiene una afirmación concreta sobre la moneda |

Permitir null no equivale a declarar un default. Y un default no demuestra un hecho histórico: usar USD requiere saber que ese era el contrato de los datos antiguos. En el dibujo se conserva la ausencia de información como null.

### El caso inverso: datos nuevos ante un lector antiguo

Si el escritor nuevo incorpora moneda y el lector antiguo no la espera, la resolución puede ignorar ese campo para producir la estructura antigua. Eso es una cuestión distinta de conservarlo al volver a escribir: reconstruir y guardar solo los dos campos antiguos podría perder la moneda. Por tanto, prueba la ruta completa, no solo que la lectura no lance una excepción.

> [!question]- ¿El default se busca en el esquema viejo o en el nuevo lector que necesita el campo?
> En el esquema del lector que espera ese campo ausente. El esquema escritor sigue siendo indispensable para interpretar lo que sí está en los bytes.

**Imagen mental para recordar:** un manual describe el paquete recibido; el otro describe el resultado esperado. Desarrollo en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/04 Avro y resolución de esquemas|Avro y resolución de esquemas]].

## 3. Si agoté el tiempo de espera, ¿la operación falló?

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/07-timeout-tres-historias.png|1100]]

### Empieza por lo que puede observar el cliente

Las tres pantallas dicen exactamente lo mismo: **sin respuesta**. La persona frente a la pantalla no ve el interior de la oficina. Nosotros sí lo vemos en el dibujo para comparar tres historias posibles.

- **A. La petición no llegó.** La operación no comenzó en el servicio. El cliente esperaba una respuesta que no puede producirse por esa petición perdida.
- **B. La petición está procesándose.** El cliente agotó su plazo mientras el servicio todavía trabaja. Que el cliente deje de esperar no cancela automáticamente el trabajo remoto.
- **C. El efecto ya ocurrió.** El servicio completó la operación, pero la confirmación se perdió. Repetirla como si nunca hubiera sucedido puede duplicar el efecto.

Estas tres historias bastan para demostrar la incertidumbre, pero no son una lista exhaustiva: también puede haber respuestas retrasadas, fallos durante el proceso o una cancelación cuyo resultado haya que confirmar.

### Por qué el reintento necesita identidad

Supón que el pago lógico tiene la clave `pago-P42`. En el primer intento envías esa clave con la solicitud. En el reintento debes conservarla: si generas `pago-P43`, el servicio puede interpretarlo como otro pago válido.

Una implementación de idempotencia necesita decidir cómo registra la clave, cómo la vincula al contenido de la solicitud, cómo coordina ese registro con el efecto y durante cuánto tiempo puede reconocer reintentos. Cuando el resultado ya es conocido, puede devolver el mismo resultado lógico. Cuando sigue en curso, necesita un comportamiento definido, como informar ese estado o esperar según el protocolo.

La clave no es un amuleto: si el servicio guarda “terminado” antes de ejecutar o ejecuta sin poder recuperar el resultado, puede seguir habiendo inconsistencias. La garantía depende de todo el protocolo y de los sistemas externos implicados.

### Vincúlalo con un workflow durable

El workflow puede guardar que una actividad terminó. Pero si el pago se realizó y el worker cayó antes de registrar la confirmación, el historial puede seguir incompleto. El motor podría volver a intentar la actividad: el proveedor de pagos debe reconocer la misma operación o permitir reconciliar su estado.

> [!question]- ¿Esperar más tiempo elimina la necesidad de idempotencia?
> Puede reducir algunos timeouts, pero no elimina respuestas perdidas, caídas ni resultados inciertos. La política de tiempo de espera y la corrección de los reintentos resuelven problemas diferentes.

**Imagen mental para recordar:** la pantalla informa lo que sabe el cliente, no todo lo que ocurrió. Continúa en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/05 Bases de datos APIs y RPC|APIs y RPC]] y [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/05 Codificación y evolución/06 Workflows durables e idempotencia|workflows durables]].

## 4. ¿Buscar una palabra es lo mismo que buscar una idea parecida?

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/08-indice-invertido-y-vectorial.png|1100]]

### Izquierda: partir del término

El catálogo tiene una entrada `coche` que apunta a los documentos donde aparece ese término. Esa inversión es la idea del **índice invertido**: en lugar de recorrer todos los documentos para preguntar cuáles contienen coche, consultamos una estructura preparada que ya asocia término con documentos.

Una consulta con varias palabras puede combinar listas de documentos, valorar frecuencias y usar información de posiciones. La tokenización y normalización establecen qué cuenta como término. Un buscador léxico también puede incorporar sinónimos y expansión de consultas; la imagen no afirma que esté condenado a una igualdad literal sin ninguna transformación.

### Derecha: partir de una representación

Un modelo convierte textos en vectores. El buscador utiliza una medida para encontrar representaciones cercanas a la consulta. En la ilustración, `reparar coche` y `arreglar automóvil` ocupan una zona cercana. **Es un ejemplo conceptual**, no una medición de un modelo concreto ni la garantía de que cualquier embedding colocará esas frases ahí.

El mapa está en dos dimensiones para que podamos verlo. Un embedding real puede tener muchas más. La distancia en el papel no equivale a una puntuación real de similitud y las coordenadas del modelo no tienen necesariamente nombres interpretables.

### Distingue dos maneras de fallar

1. La representación no captura lo que necesitas: incluso encontrar los vecinos exactos puede devolver documentos poco relevantes.
2. El índice aproximado omite un vecino que una búsqueda exhaustiva habría encontrado con esa misma representación y medida.

El primer fallo exige revisar representación, datos o criterio de relevancia. El segundo se estudia comparando la búsqueda aproximada con la exacta y ajustando la exploración. Ambos pueden coincidir, pero no se corrigen siempre con el mismo cambio.

### Un sistema puede combinar ambos caminos

Una referencia exacta, como un código de producto, puede favorecer señales léxicas. Una paráfrasis puede beneficiarse de señales semánticas. Recuperar candidatos por ambas vías y combinarlos requiere una política explícita; no es correcto sumar sin más puntuaciones de escalas distintas. Tus notas de RRF desarrollan una forma de combinar posiciones de rankings.

> [!question]- ¿Que el documento esté muy cerca de la consulta demuestra que es verdadero?
> No. La cercanía compara representaciones, no verifica los hechos. Relevancia, veracidad y suficiencia de la evidencia son evaluaciones distintas.

**Imagen mental para recordar:** el catálogo reúne apariciones; el mapa reúne vecinos de una representación. Desarrollo en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/07 Índices espaciales texto completo y vectores|índices espaciales, texto y vectores]], conectado con [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/08 RAG fragmentación y recuperación/38 S08 - Búsqueda léxica densa y fusión RRF|tu nota de búsqueda híbrida y RRF]].

## 5. ¿Cómo pasa una actualización LSM de reciente a publicada?

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/09-lsm-taller-ciclo-actualizacion.png|1100]]

El diario rojo conserva el cambio para recuperación; la mesa ámbar representa la memtable ordenada; las losas grises son SSTables inmutables; y la losa verde es una salida nueva ya publicada. La escena reúne WAL, acumulación en RAM, flush y compactación para mostrar que una actualización cambia el estado visible mediante **archivos nuevos**, no tallando de nuevo los antiguos.

La analogía no prescribe el protocolo exacto: los motores no usan trabajadores ni losas y pueden coordinar sincronización, publicación y retirada de maneras distintas. La condición esencial es no confirmar ni retirar datos de una forma que impida recuperar el estado prometido.

**Imagen mental para recordar:** primero deja una historia recuperable, después organiza y finalmente publica una versión inmutable. Desarrollo completo en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/02 LSM SSTables compactación y Bloom|LSM, SSTables, compactación y Bloom]].

## Señales de comprensión

Cierra esta nota y dibuja cinco cosas: las dos versiones de P42; los dos esquemas de Avro; las tres historias del timeout; los dos caminos de búsqueda; y el recorrido WAL → memtable → SSTables → publicación. Junto a cada dibujo escribe **una condición que la imagen no garantiza**. Poder explicar esas condiciones vale más que recordar únicamente los colores.

Las ilustraciones fueron generadas con `image_gen` y revisadas antes de incorporarlas. Sus prompts y límites están en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/03 Procedencia de imágenes y prompts|procedencia de recursos visuales]].

---

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/01 Guía y fundamentos/00 Índice|← Índice de este bloque]] · [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/04 Almacenamiento y recuperación/01 Del log al índice|Empezar el capítulo 4]]
