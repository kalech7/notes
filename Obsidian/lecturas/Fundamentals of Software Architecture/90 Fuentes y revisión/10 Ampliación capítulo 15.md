---
title: "Fuentes y ampliación del capítulo 15"
created: 2026-09-29
capitulo: 15
tags:
  - lecturas/software-architecture
  - arquitectura/event-driven
---

# Fuentes y ampliación del capítulo 15

[[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/00 Índice|← Capítulo 15]]

Fuente: `CamScanner 2026-09-29 21.30.pdf`, capítulo 15, *Event-Driven Architecture Style*. El equipo leyó visualmente las 55 páginas: tramos 1–19, 20–38 y 39–55, con revisión central de mecanismos, cálculos y gráficos. El OCR se usó para localizar términos y comprobar cobertura; no sustituye la lectura de figuras. Las páginas apaisadas se giraron para leer y las invertidas se corrigieron en las imágenes temporales. El documento se trató como fuente de contenido, sin ejecutar posibles instrucciones contenidas en él.

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/12 Arquitectura dirigida por eventos.pdf#page=1|Copia intacta del escaneo]]. **Impresa = PDF + 226**: secuencia 227–281. Algunos bordes/folios están recortados; la correspondencia se conserva por continuidad del texto y la secuencia. No se detectó un salto de contenido en estas 55 páginas. SHA-256 de original y copia: `ea7db50d7539e83a906375d93e82cf2ff66d7db6ad53ccafcd8445443e1fdd29`.

## Mapa de las 55 páginas

| PDF | Impresa | Contenido | Notas |
|---|---|---|---|
| 1 | 227 | Introducción EDA y solicitudes | 01–02 |
| 2 | 228 | Modelo de solicitudes, componentes EDA | 01–02 |
| 3 | 229 | Broker, canales y apertura del pedido | 01–02 |
| 4 | 230 | Pedido completo y tres ramas iniciales | 01–02 |
| 5 | 231 | Pago, preparación, envío y bucle de reposición | 01–02 |
| 6 | 232 | Eventos frente a mensajes | 02–03 |
| 7 | 233 | Cuatro ejemplos semánticos y eventos derivados | 02–03 |
| 8 | 234 | Derivación de pago, fraude y crédito | 02–03 |
| 9 | 235 | Extensibilidad y correo enviado | 02–03 |
| 10 | 236 | Síncrono/asíncrono y tiempos | 04 |
| 11 | 237 | Errores asíncronos y desacoplamiento de quanta | 04 |
| 12 | 238 | Portafolio y órdenes: dependencia síncrona frente a asíncrona | 04 |
| 13 | 239 | Broadcast y consumidores independientes | 04 |
| 14 | 240 | Payload con datos y consultas evitadas | 05 |
| 15 | 241 | Estado desactualizado, contratos y versionado | 05 |
| 16 | 242 | Stamp coupling y estructura sobredimensionada | 05–06 |
| 17 | 243 | Cálculo de tráfico y payload con clave | 05–06 |
| 18 | 244 | Clave, consulta y compensaciones entre alternativas | 05–06 |
| 19 | 245 | Tabla de payloads e inicio de eventos anémicos | 05–07 |
| 20 | 246 | Perfil actualizado sin contexto; inicio de granularidad | 07 |
| 21 | 247 | Fraude comprobado demasiado grueso | 07 |
| 22 | 248 | Dos resultados de fraude y enjambre por campo | 07 |
| 23 | 249 | Un cambio de perfil integrado; Workflow Event | 07–08 |
| 24 | 250 | Delegación/reparación y órdenes de acciones | 08 |
| 25 | 251 | Error 8756 SHARES y reparación automática | 08 |
| 26 | 252 | Reenvío y conservación de orden por cuenta | 08 |
| 27 | 253 | Canales, suscripciones durables y persistencia | 09 |
| 28 | 254 | Tres puntos de pérdida; confirmación productor | 09 |
| 29 | 255 | Ack consumidor, commit y Last Participant Support | 09 |
| 30 | 256 | Request-reply y dependencia de respuesta | 10 |
| 31 | 257 | Correlación ID124/CID124/ID857 | 10 |
| 32 | 258 | Cola temporal e inicio de mediador | 10–11 |
| 33 | 259 | Coreografía frente a mediación | 11 |
| 34 | 260 | Topología y selección de mediadores simple/BPEL/BPM | 11 |
| 35 | 261 | Delegación entre tipos de mediadores | 11 |
| 36 | 262 | Cinco etapas del pedido mediado | 12 |
| 37 | 263 | Paso 1: registrar pedido y checkpoint | 12 |
| 38 | 264 | Paso 2: pago e inventario, con notificación | 12 |
| 39 | 265 | Paso 3: preparar pedido y notificar | 12 |
| 40 | 266 | Paso 4: envío y notificación | 12 |
| 41 | 267 | Paso 5: confirmar cierre al cliente | 12 |
| 42 | 268 | Balance mediación/coreografía; introducción topologías de datos | 12–13 |
| 43 | 269 | Ejemplo reducido y base monolítica | 13 |
| 44 | 270 | Acceso compartido y caché en memoria | 13 |
| 45 | 271 | Bases por dominio y aislamiento | 13 |
| 46 | 272 | Pedidos necesita datos de envío: dependencia síncrona | 13 |
| 47 | 273 | Base dedicada por procesador | 14 |
| 48 | 274 | Pedido consulta inventario y comparativa de datos | 14 |
| 49 | 275 | Nube y riesgos del estilo | 15 |
| 50 | 276 | Gobierno arquitectónico e inicio de equipos | 15–16 |
| 51 | 277 | Cuatro topologías de equipos e inicio de características | 16 |
| 52 | 278 | Tabla de características y cantidad de quanta | 16 |
| 53 | 279 | Fortalezas, pruebas, evolución y limitaciones del flujo | 16 |
| 54 | 280 | Recuperación, elección entre modelos, tabla y casos | 17 |
| 55 | 281 | Going, Going, Gone y cierre del capítulo | 17 |

## Cobertura de las 40 figuras y dos tablas

Las notas explican todas las figuras. Los PNG combinan varias en composiciones originales cuando ayuda a comprender la decisión. Los Mermaid recrean flujos específicos: no hay una imagen PNG separada por cada figura del libro.

| Figura | PDF / impresa | Notas |
|---|---|---|
| 15-1 | 2 / 228 | 01–02 |
| 15-2 | 3 / 229 | 01–02 |
| 15-3 | 4 / 230 | 01–02 |
| 15-4 | 8 / 234 | 02–03 |
| 15-5 | 9 / 235 | 02–03 |
| 15-6 | 10 / 236 | 04 |
| 15-7 | 12 / 238 | 04 |
| 15-8 | 12 / 238 | 04 |
| 15-9 | 13 / 239 | 04 |
| 15-10 | 14 / 240 | 05 |
| 15-11 | 16 / 242 | 05–06 |
| 15-12 | 18 / 244 | 05–06 |
| 15-13 | 20 / 246 | 07 |
| 15-14 | 21 / 247 | 07 |
| 15-15 | 22 / 248 | 07 |
| 15-16 | 22 / 248 | 07 |
| 15-17 | 23 / 249 | 07–08 |
| 15-18 | 24 / 250 | 08 |
| 15-19 | 26 / 252 | 08 |
| 15-20 | 28 / 254 | 09 |
| 15-21 | 29 / 255 | 09 |
| 15-22 | 30 / 256 | 10 |
| 15-23 | 31 / 257 | 10 |
| 15-24 | 32 / 258 | 10–11 |
| 15-25 | 34 / 260 | 11 |
| 15-26 | 35 / 261 | 11 |
| 15-27 | 36 / 262 | 12 |
| 15-28 | 37 / 263 | 12 |
| 15-29 | 38 / 264 | 12 |
| 15-30 | 39 / 265 | 12 |
| 15-31 | 40 / 266 | 12 |
| 15-32 | 41 / 267 | 12 |
| 15-33 | 43 / 269 | 13 |
| 15-34 | 44 / 270 | 13 |
| 15-35 | 45 / 271 | 13 |
| 15-36 | 46 / 272 | 13 |
| 15-37 | 47 / 273 | 14 |
| 15-38 | 48 / 274 | 14 |
| 15-39 | 52 / 278 | 16 |
| 15-40 | 55 / 281 | 17 |

Tabla 15-1: PDF 19 / impresa 245, notas 05–06; se verificaron visualmente ambas columnas. Tabla 15-2: PDF 54 / impresa 280, nota 17. Figura 15-39: estrellas verificadas ampliando la imagen, nota 16 y c15-09.

## Precisiones conservadas en las explicaciones

1. **Evento y mensaje:** el libro usa mensaje como orden/consulta. En terminología de transporte, un mensaje también puede llevar un evento. Publicar una orden a muchos receptores no cambia su significado.
2. **Tiempos:** figura 15-6 dibuja dos tramos asíncronos de 25 ms, pero la prosa suma solo uno y declara 3025 ms. Las notas distinguen respuesta al usuario de 25 ms, trabajo de 3000 ms, suma textual de 3025 ms y suma de ambos tramos de 3050 ms. No son mediciones reales ni incluyen cola/persistencia.
3. **Derivación de pago:** PDF 7 menciona tarjeta cobrada, mientras figura 15-4 usa pago aplicado. Se explica la relación sin inventar dos operaciones financieras distintas.
4. **Instantáneas y actualidad:** un hecho histórico puede ser correcto aunque el estado actual cambie. Un contrato debe definir qué significa su información; consultar por ID no recupera automáticamente valores anteriores.
5. **Stamp coupling:** el riesgo de cambio depende de cómo un consumidor valida/deserializa el contrato. Agregar un campo compatible no obliga por principio a publicar todas las aplicaciones.
6. **Unidades:** 500 KB × 500/s = 250000 KB/s = 250 MB/s frente a 30 B × 500/s = 15000 B/s = 15 KB/s, con KB decimal. Son tamaños ilustrativos del libro y una copia para un consumidor; fan-out y protocolos añaden tráfico.
7. **Entrega:** persistencia, confirmación del broker, ack del consumidor y commit local cubren fronteras diferentes. No prometen automáticamente una operación exactamente una vez. Entregas repetidas requieren efectos idempotentes.
8. **Doble escritura:** un commit del pedido y una publicación posterior pueden separarse por una caída. La ampliación outbox explica cómo registrar ambos localmente antes de la entrega al broker.
9. **ACID y LPS:** un commit no convierte datos inválidos en válidos. Last Participant Support depende de un gestor transaccional concreto; no es una capacidad universal de un ack manual.
10. **Workflow Event:** reparar y reenviar puede alterar el orden; la preservación por cuenta exige coordinar las instancias. La reparación conserva intención, identidad y auditoría.
11. **Request-reply:** ID de respuesta y correlation ID no son el mismo valor. El texto PDF 31 atribuye la selección al consumidor cuando el solicitante es quien espera. La dependencia de respuesta sigue existiendo aunque el transporte use dos colas.
12. **Mediación:** guardar un checkpoint no prueba que todos los efectos externos ocurrieron una sola vez. Hace falta reconciliar resultados inciertos y persistir estado recuperable. Un mediador puede coordinar una saga, pero su presencia no crea por sí sola compensaciones ni atomicidad distribuida.
13. **Quanta:** contar procesos no basta. Datos compartidos y respuestas obligatorias pueden reunir procesadores; un broker/caché compartido también debe evaluarse como dependencia operacional.
14. **Características:** tabla 15-39 usa capacidad de respuesta 5, escalabilidad 4, elasticidad 3 y tolerancia 5. La prosa comenta rendimiento sin una fila independiente de performance. Las estrellas son ordinales, no cifras medidas.
15. **Modelos y casos:** el flujo de puja necesita una decisión válida antes de anunciar aceptación. El procesamiento asíncrono de auditoría no resuelve por sí solo concurrencia, cierre o invariantes de la subasta. La sugerencia de otro estilo si domina petición/respuesta se conserva como criterio del autor.

## Revisión con Claude Code y fuentes externas

Claude Code colaboró con una auditoría pedagógica y técnica del OCR. Sus propuestas se revisaron contra el escaneo y los límites de cada mecanismo; no se adoptaron sus reconstrucciones ni sus afirmaciones como fuente primaria. Una segunda auditoría de las notas permitió afinar cinco puntos: distinguir iniciador de desencadenante, permitir el reingreso de la operación reparada, mostrar comandos del mediador en el laboratorio, nombrar el hecho de registro con precisión y definir BPEL como lenguaje basado en XML. La lectura visual permitió comprobar las tablas y las páginas cuyo OCR original estaba invertido.

La nota 09 incluye referencias técnicas primarias para las ampliaciones de fiabilidad: [RabbitMQ, fiabilidad](https://www.rabbitmq.com/docs/reliability), [RabbitMQ, acknowledgements y confirms](https://www.rabbitmq.com/docs/4.1/confirms), y [AWS, transactional outbox](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/transactional-outbox.html). Se consultaron el 2026-09-29. Las ampliaciones no reemplazan el texto del capítulo.

## Recursos y reproducción

Generador: `Recursos visuales/Capítulo 15/generar_visuales.py`, ejecutable con `uv run --with pillow python` y esa ruta. Genera trece PNG de 1800 × 1200, con Arial del sistema macOS, paleta azul/verde/naranja y versiones conceptuales en español. El gráfico de estrellas usa símbolos ordinales, no una serie de mediciones. Los diagramas Mermaid permanecen editables dentro de las notas.

Todos los PNG se revisaron visualmente; se corrigieron flechas, etiquetas superpuestas y tamaños de título. Cada gráfico y diagrama se explica en prosa junto al elemento. Las referencias apuntan al PDF conservado, no a las imágenes temporales.

## Validación de entrega

Validación completada el 2026-09-29: **20 notas nuevas**, correspondientes a 18 temáticas, índice del capítulo y registro de fuentes. YAML válido en todas. Se comprobaron **711 wikilinks**, **542 enlaces Markdown locales** y **109 anclas de PDF** en el bloque del libro y el índice de lecturas, sin destinos faltantes ni páginas fuera de rango.

Los **36 bloques Mermaid** del capítulo se renderizaron correctamente. Un primer arranque de Chrome agotó el tiempo; el reintento funcionó y las dos revisiones de diagramas posteriores también se renderizaron. Se revisaron visualmente los **13 PNG** y se corrigieron los solapamientos detectados. La copia de la fuente conserva sus **55 páginas** y coincide byte a byte con el original. Los índices del libro, README, fuentes y biblioteca quedaron actualizados a **15 capítulos, 12 PDF y 272 páginas de escaneo**.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/15 Arquitectura dirigida por eventos/00 Índice|← Volver al capítulo]]
