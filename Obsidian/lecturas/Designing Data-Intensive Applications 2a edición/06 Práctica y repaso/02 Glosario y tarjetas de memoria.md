---
title: "DDIA — Glosario y tarjetas de memoria"
created: 2026-09-25
tags:
  - lecturas/ddia
  - repaso
  - glosario
---

# DDIA — Glosario y tarjetas de memoria

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/00 Índice|Práctica y repaso]]

> [!tip] Cómo usar esta nota
> Primero responde sin mirar. Después abre la respuesta y explica qué parte omitiste. Una definición se vuelve útil cuando puedes reconocer **un ejemplo y un contraejemplo**. Las analogías ayudan a recordar; no sustituyen los mecanismos de las notas detalladas.

## El vocabulario, con una imagen mental

| Término | Significado útil | Recordatorio y límite |
|---|---|---|
| Motor de almacenamiento | Componente que organiza persistencia y acceso a datos | El almacén detrás del mostrador; no equivale a toda la base de datos |
| Índice | Estructura adicional que acelera ciertos accesos | Un mapa que también hay que mantener |
| OLTP | Carga operacional con numerosas operaciones, habitualmente sobre pocos registros | Atender pedidos; no significa «cualquier sistema que usa SQL» |
| OLAP | Carga de análisis que suele agregar muchos registros | Entender ventas; también puede usar SQL |
| Log append-only | Secuencia a la que se añaden registros al final | Cuaderno cronológico; por sí solo no ofrece búsquedas rápidas |
| WAL | Registro previo usado para recuperación | Anotar cómo recuperar antes de dar por protegida una modificación; no todo log es un WAL |
| Memtable | Estructura en memoria para escrituras recientes de un LSM | Mesa de trabajo; su persistencia requiere otro mecanismo |
| SSTable | Archivo de pares clave-valor ordenados por clave | Archivador ordenado y normalmente inmutable |
| LSM-tree | Organización que combina memoria, segmentos ordenados y compactación | Acumular, ordenar y fusionar; no es solo una lista de logs |
| Compactación | Reorganización y combinación de segmentos; descarta versiones cuando es seguro | Ordenar el archivo sin borrar información aún necesaria |
| Tombstone | Marca que representa una eliminación | Aviso de «ya no existe» para impedir que reaparezca una versión vieja |
| B-tree | Árbol balanceado con muchos hijos por nodo, adecuado para páginas | Guía de rangos; no es un árbol binario |
| Bloom filter | Estructura probabilística para descartar pertenencia | «Seguro que no» o «quizá sí», si está correctamente mantenido |
| Amplificación de escritura | Bytes físicos escritos respecto a bytes lógicos incorporados | Una pequeña noticia puede obligar a reorganizar mucho papel |
| Amplificación de lectura | Trabajo extra para encontrar los datos solicitados | Abrir varios archivadores para responder una pregunta |
| Amplificación de espacio | Almacenamiento adicional respecto al volumen lógico considerado | Versiones, índices y estructuras auxiliares; indica qué incluyes al medir |
| Índice de cobertura | Índice que contiene lo necesario para una consulta | El mapa incluye la respuesta; evitar accesos adicionales depende del motor |
| Almacenamiento columnar | Agrupa valores por columna en sus unidades físicas | Leer solo las partes de la ficha que necesitas |
| Vista materializada | Resultado de consulta almacenado | Respuesta preparada que hay que actualizar |
| Índice invertido | Asocia términos con los documentos que los contienen | Palabra → lista de documentos |
| Embedding | Vector numérico que representa características aprendidas | Coordenadas de una representación, no hechos garantizados |
| ANN | Búsqueda aproximada de vecinos cercanos | Ahorrar búsqueda aceptando que se puede perder algún vecino |
| Serialización | Conversión de valores a una representación transmisible o almacenable | Empaquetar valores en bytes |
| Esquema | Descripción de campos, tipos y reglas estructurales | Instrucciones para interpretar; no captura automáticamente todo el negocio |
| Compatibilidad hacia atrás | Un lector nuevo interpreta datos antiguos | Nuevo mira atrás |
| Compatibilidad hacia delante | Un lector antiguo interpreta datos nuevos | Antiguo tolera lo que llega después |
| Field tag | Identificador numérico estable de un campo en Protobuf | Número de casillero, no posición visual ni nombre |
| Writer schema / reader schema | Esquemas usados al escribir y al leer en Avro | Qué se envió y qué espera quien recibe |
| RPC | Invocación de una operación en otro proceso mediante comunicación | Parece una llamada, pero cruza una red con fallos parciales |
| Idempotencia | Repetir una operación conserva su efecto previsto | Repetir la solicitud no debe repetir el cobro |
| Ejecución durable | Recuperación del avance de un workflow a partir de estado/historial persistente | Retomar el proceso; no vuelve infalibles sus efectos externos |
| Broker de mensajes | Intermediario que recibe y entrega mensajes | Buzón; retención, orden y duplicados dependen del sistema y configuración |

## Las confusiones que conviene separar

| Pareja | Diferencia |
|---|---|
| Serialización / serializabilidad | Convertir datos a bytes / propiedad de aislamiento de transacciones |
| Vectorización / embeddings | Procesar lotes de valores / representar objetos en un espacio de características |
| Columnas físicas / wide-column | Disposición analítica de almacenamiento / familia de modelos de datos; el nombre no garantiza el mismo diseño |
| Compactación / compresión | Reorganizar y combinar segmentos / codificar usando menos espacio |
| Parquet / Delta Lake | Formato de archivos / capa de tabla que administra estados y operaciones sobre archivos |
| Compatibilidad binaria / corrección de negocio | Poder interpretar la estructura / preservar el significado de los valores |
| Replicación / copia de seguridad | Mantener réplicas para servir y tolerar fallos / conservar estados recuperables frente a pérdidas o errores; una no sustituye automáticamente a la otra |

La última distinción es una ampliación para evitar una confusión frecuente; estos escaneos no desarrollan el capítulo de replicación.

## Tarjetas: almacenamiento

> [!question]- 1. ¿Qué gana y qué pierde una base que solo añade registros al final?
> Simplifica el camino de escritura. Sin índice, encontrar el último valor de una clave puede exigir recorrer mucho historial. Además necesita controlar versiones obsoletas y crecimiento del archivo.

> [!question]- 2. ¿Por qué ordenar una SSTable permite un índice disperso?
> Si conozco puntos de referencia de claves ordenadas, ubico el bloque donde podría estar la clave y busco allí. No necesito una entrada en memoria por cada clave. El orden también sirve para recorrer rangos y fusionar segmentos.

> [!question]- 3. Un Bloom filter responde «sí». ¿Puedo devolver el registro?
> No. Responde «puede estar». Debes buscar el registro y comprobar su vigencia. Una respuesta negativa sí permite descartar esa estructura, bajo las condiciones normales del filtro.

> [!question]- 4. ¿Por qué una eliminación en un LSM no siempre borra físicamente la clave al momento?
> Puede haber versiones antiguas en otros segmentos. Una marca de eliminación evita que vuelvan a verse. Su eliminación física debe esperar a que ya no oculte datos relevantes y a que las reglas de retención o snapshots lo permitan.

> [!question]- 5. Si un B-tree tiene altura 4, ¿son siempre cuatro lecturas del disco?
> No. Puede haber páginas en caché; la búsqueda puede requerir además datos fuera del índice o devolver muchas coincidencias. La altura orienta la navegación, no describe todo el costo.

> [!question]- 6. ¿Por qué «LSM para escribir y B-tree para leer» no basta para elegir?
> Es una intuición, no un resultado universal. Importan tamaño de valores, mezcla de operaciones, caché, compactación, hardware, concurrencia, latencia de cola y objetivos de espacio y durabilidad.

> [!question]- 7. ¿Qué ventaja columnar cambia si pido todas las columnas?
> Disminuye o desaparece el ahorro por proyección de columnas. Aun pueden importar compresión, ejecución y organización física. Tampoco una consulta de pocas columnas está garantizada como rápida.

> [!question]- 8. ¿Qué precio tiene una vista materializada?
> Espacio y trabajo para construirla y mantenerla, más la gestión de su frescura. Acelera preguntas compatibles con lo que ya calculó; no responde automáticamente cualquier nueva agrupación.

> [!question]- 9. ¿Encontrar un embedding cercano demuestra que la respuesta recuperada es verdadera?
> No. La cercanía es una señal de similitud según el modelo y la métrica. Todavía hay que evaluar relevancia, cobertura, actualidad y respaldo de las afirmaciones.

## Tarjetas: evolución y comunicación

> [!question]- 10. ¿Cuál es hacia atrás: lector antiguo con datos nuevos o lector nuevo con datos antiguos?
> Lector **nuevo** con datos **antiguos**. Describe siempre las dos versiones antes de decir «compatible».

> [!question]- 11. ¿Por qué no reutilizar un número de campo eliminado de Protobuf?
> Bytes escritos con el significado anterior podrían interpretarse con el nuevo. Se conserva la identidad de los campos y se reservan los números eliminados para evitar ese choque.

> [!question]- 12. En Avro, el lector espera un campo que el escritor no incluyó. ¿De dónde puede salir su valor?
> Del default declarado en el esquema del lector, si las reglas de resolución lo permiten. Si no hay default apropiado, la resolución puede fallar. Un campo que admite null no obtiene automáticamente un default.

> [!question]- 13. ¿Un JSON válido es también un dato válido para la aplicación?
> No. Puede tener el tipo equivocado, omitir algo necesario o usar unidades incorrectas. Sintaxis, esquema y reglas del negocio son comprobaciones distintas.

> [!question]- 14. ¿Por qué un lector antiguo puede destruir un campo nuevo al guardar de nuevo un objeto?
> Puede reconstruir el objeto solo con los campos que conoce y reemplazar el registro completo. Ignorar al leer no demuestra preservar al reescribir. Hay que comprobar el camino completo y el comportamiento de la biblioteca.

> [!question]- 15. El cliente recibe un timeout tras pedir un pago. ¿El pago falló?
> No se sabe: pudo fallar antes de aplicarse o aplicarse y perderse la respuesta. Necesitas un protocolo que permita consultar, deduplicar o reconciliar el intento.

> [!question]- 16. ¿Un workflow durable elimina la necesidad de idempotencia?
> No. El motor puede recuperar su progreso, pero una actividad externa puede repetirse o quedar con resultado incierto. La aplicación debe diseñar cómo evitar efectos duplicados.

> [!question]- 17. ¿Un broker conserva siempre los mensajes hasta que todos los lectores estén listos?
> No como regla general. Durabilidad, acknowledgements, retención, grupos de consumidores y entrega son decisiones específicas. «Asíncrono» no es una garantía de conservación ilimitada.

> [!question]- 18. ¿Qué tienen en común actualizar una tabla y publicar un evento nuevo?
> Los datos pueden sobrevivir a la versión de código que los escribió. Debes pensar en lectores antiguos y nuevos, historial persistido, cambios de significado y migración.

## Repaso espaciado sencillo

Este es un plan de práctica sugerido, no una afirmación de que exista un intervalo óptimo universal. Al terminar la primera lectura, responde cuatro tarjetas sin ayuda. Vuelve al día siguiente, unos días después y la semana siguiente. Prioriza las que fallaste y cambia los ejemplos: una reserva en vez de un pedido, temperatura en vez de dinero, archivos históricos en vez de mensajes recientes.

| Momento | Tarea | Evidencia de comprensión |
|---|---|---|
| Primera vuelta | Dibuja B-tree, LSM y las dos direcciones de compatibilidad | Puedes explicar las flechas |
| Día siguiente | Resuelve seis tarjetas al azar | Das condiciones, no solo palabras clave |
| Unos días después | Resuelve [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/01 Caso práctico de pedidos a analítica\|el caso de pedidos]] | Justificas cada elección y sus costos |
| Semana siguiente | Enseña dos conceptos con otra situación | Puedes señalar dónde deja de servir tu analogía |

Si no recuerdas una respuesta, vuelve a su explicación desde [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|el índice]]. Las tarjetas sintetizan las notas del conjunto; consulta [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/90 Fuentes y revisión/01 Fuentes y cobertura|la procedencia y límites]] para distinguir lectura de ampliaciones.

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/01 Caso práctico de pedidos a analítica|Caso práctico de pedidos a analítica]] · **Índice:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/00 Índice|Ver este bloque]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Práctica y repaso/03 Conexiones con mis otras notas|Conexiones con mis otras notas]]
