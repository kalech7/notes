---
title: "Atlas visual explicado · Fundamentals of Software Architecture 2.ª edición"
created: 2026-09-25
tags:
  - lecturas/software-architecture
  - recursos-visuales
---

# Atlas visual explicado

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Índice]]

Un diagrama es útil si permite responder una pregunta. Aquí se explica cómo leer las doce composiciones originales de la guía: cinco ilustraciones generadas y siete figuras vectoriales, todas disponibles en PNG. Además, los capítulos incorporan veinte diagramas exportados a PNG con sus fuentes editables. Los gráficos cuantitativos usan **datos inventados**, no mediciones ni resultados publicados por los autores.

## 1. Las cuatro dimensiones de la arquitectura

![arquitectura contexto](Recursos%20visuales/01-arquitectura-contexto.png)

Empieza arriba: el contexto incluye las metas de negocio, el dinero, el equipo y las restricciones. Las dos cajas centrales responden preguntas diferentes. Las características expresan capacidades o condiciones de éxito; los componentes organizan responsabilidades. «Gestionar pedidos» y «resistir un pico» se necesitan mutuamente, pero no son equivalentes.

La parte inferior conecta estilo y decisiones. Un estilo ofrece una organización de partida; las decisiones concretan límites y razones. No puedes justificar un estilo solo nombrándolo. «Usaremos microservicios» no dice qué capacidad necesitas, quién mantendrá cada servicio ni cómo se resolverá un fallo entre ellos.

**Lectura aplicada:** si el equipo de PedidoClaro es pequeño, operar múltiples servicios tiene un costo. Si el área de promociones debe desplegar cada hora y el resto cada mes, aparece otra presión. Ninguna caja decide por sí sola: las relaciones ayudan a identificar qué hay que investigar.

**Límite:** las flechas no representan un algoritmo obligatorio. El análisis puede avanzar en paralelo y volver atrás cuando una restricción invalida una alternativa. Véase el [[Obsidian/lecturas/Fundamentals of Software Architecture/01 Introducción|capítulo 1]].

## 2. Una cola de trabajo y una publicación a varios intereses

![colas y publicacion](Recursos%20visuales/02-colas-y-publicacion.png)

Arriba hay una cola compartida por dos trabajadores. La intención es repartir trabajo: el pedido 101 puede ir al trabajador A y el 102 al B. Añadir trabajadores aumenta capacidad solo si el recurso limitante permite ese paralelismo. No significa que ambos reciban todos los pedidos.

Abajo, cocina y analítica son intereses diferentes. Ambos necesitan enterarse del pedido, de modo que el distribuidor produce una entrega para cada cola. Dentro de cocina todavía podrías tener dos trabajadores que repartan su propia carga. Por tanto, **difusión entre intereses y reparto dentro de un interés pueden coexistir**. Esta separación está ilustrada en el [tutorial oficial de publicación/suscripción de RabbitMQ](https://www.rabbitmq.com/tutorials/tutorial-three-python).

El dibujo deliberadamente no escribe «exactamente una vez». Si un consumidor procesa un evento pero falla antes de confirmar, puede recibirlo de nuevo. Un identificador de pedido y una operación idempotente ayudan a evitar duplicar efectos; las garantías precisas dependen del protocolo y de cómo se persista el resultado.

**Comprueba tu comprensión:** si añades tres réplicas de analítica a la misma cola, ¿todas verán cada evento? No: repartirán las entregas de esa cola. Si cada interés necesita su copia, requiere una suscripción independiente. Véase el [[Obsidian/lecturas/Fundamentals of Software Architecture/02 Pensamiento arquitectónico|capítulo 2]].

## 3. Separación lógica y separación de despliegue

![modularidad](Recursos%20visuales/03-modularidad.png)

La primera escena representa un límite de despliegue que contiene tres módulos. Los colores sugieren responsabilidades distintas. Es posible cambiar una regla de un módulo sin invadir los demás, aunque al publicar se entregue una aplicación completa.

La segunda separa los límites físicos. Cada servicio tiene datos bajo su responsabilidad y necesita comunicación explícita. Esto puede permitir despliegues o escalado independientes, pero esa independencia debe existir en contratos, pruebas, operación y organización. Tres bases dibujadas no la garantizan.

La tercera muestra dependencias densas: aunque las piezas están físicamente separadas, siguen exigiendo cambios coordinados. Es la intuición del monolito distribuido. La base compartida es un posible mecanismo de acoplamiento, pero no es condición necesaria ni suficiente para diagnosticarlo.

**Cómo usar la analogía:** pregunta qué cambios exigen tocar varias piezas, cuáles fallan juntas y cuáles requieren desplegarse juntas. Esas observaciones dicen más que contar cajas. Los tres puentes de la escena central tampoco son una recomendación de conectar todos los servicios entre sí.

**Límite:** el dibujo no mide cohesión, latencia ni calidad. Tampoco afirma que un estilo siempre gane. Véase el [[Obsidian/lecturas/Fundamentals of Software Architecture/03 Modularidad|capítulo 3]].

## 4. Secuencia principal: una métrica y sus límites

![secuencia principal](Recursos%20visuales/04-secuencia-principal.png)

El eje horizontal representa **inestabilidad** `I = Ce / (Ca + Ce)`: dependencia saliente relativa, no frecuencia observada de fallos. El vertical representa **abstracción** `A = Na / (Na + Nc)`: proporción de tipos abstractos frente al total de tipos contados.

La diagonal cumple `A + I = 1`. El punto B está sobre ella: `0,80 + 0,20 = 1`; su distancia normalizada es cero. P está cerca del extremo concreto y muy dependido: `D = |0,10 + 0,20 − 1| = 0,70`. U combina abstracción alta con inestabilidad alta: `D = |0,90 + 0,85 − 1| = 0,75`.

Las zonas tienen nombres deliberadamente llamativos para invitar a investigar. En la zona de dolor, cambiar implementaciones concretas de las que dependen muchos módulos puede ser costoso. En la zona de inutilidad, puede existir abstracción sin consumidores suficientes que la justifiquen. Un módulo de entidades estables puede estar cerca del origen por buenas razones: el contexto manda.

**Detalle matemático:** la fórmula del libro `|A + I − 1|` es normalizada. La distancia geométrica perpendicular a la recta es esa cantidad dividida por `√2`. No intercambies ambas cuando compares herramientas.

**No concluyas:** «B está sobre la recta, por tanto está bien diseñado». Un nombre equivocado, un concepto de negocio mal modelado o una dependencia dinámica invisible pueden coexistir con métricas atractivas.

## 5. LCOM: contar pares, no mirar el dibujo por intuición

![lcom](Recursos%20visuales/05-lcom.png)

Tenemos cuatro métodos. Dos usan el campo `a`; los otros dos usan `b`. Cuatro métodos producen `4 × 3 / 2 = 6` pares no ordenados. Dos pares comparten estado (`Q = 2`) y cuatro no lo comparten (`P = 4`). Para la variante LCOM1 utilizada aquí: `max(P − Q, 0) = 2`.

Que existan dos grupos disjuntos sugiere revisar si se mezclaron responsabilidades. Pero la decisión de separar requiere entender el dominio: quizá ambos grupos son partes inseparables de un mismo concepto, o quizá la clase es una bolsa de utilidades accidentales.

**Trampa crucial:** el resultado 2 coincide con los dos grupos conexos de este ejemplo. No significa que LCOM1 cuente grupos. Si un campo fuera usado por cuatro métodos y otro por uno, los pares compartidos serían 6 y los disjuntos 4: LCOM1 daría cero, aun cuando el grafo tuviera dos componentes. Una variante que cuenta componentes y LCOM1 pueden discrepar.

**Prueba mental:** si todos los métodos acceden artificialmente a un campo de registro, la métrica podría mejorar sin mejorar las responsabilidades. Las métricas observan estructura; no comprenden por sí solas el significado.

## 6. Crecer y adaptarse al pico no son lo mismo

![escalabilidad elasticidad](Recursos%20visuales/06-escalabilidad-elasticidad.png)

A la izquierda, una instancia admite 100 solicitudes/s; dos, 180; cuatro, 300. La eficiencia no es lineal: hay trabajo compartido o sobrecarga. Si definimos eficiencia relativa como capacidad real dividida por `instancias × capacidad de una instancia`, obtenemos 100 %, 90 % y 75 %. Estos números solo tienen sentido **manteniendo la misma operación, datos y objetivo de respuesta**.

A la derecha, la demanda aumenta al mediodía y luego cae. La línea de capacidad cambia para acompañarla. La elasticidad debe resolver tanto el crecimiento como la reducción: sostener recursos máximos toda la noche puede servir para atender, pero desperdicia capacidad. Provisionar después de que el pico terminó tampoco satisface el objetivo.

El gráfico agrupa observaciones cada dos horas; no muestra segundos de arranque ni garantiza que no haya colas entre puntos. Hay que medir cuánto tarda en detectarse el pico, iniciarse recursos, calentarse cachés y repartirse el tráfico. Para un almuerzo previsible puede ser apropiado escalar antes del evento.

**Límite físico del caso:** más capacidad informática no prepara más sándwiches si la cocina está saturada. La respuesta del sistema podría ser ampliar la hora de entrega ofrecida o limitar admisiones de forma explícita, en vez de confirmar plazos imposibles. Véanse los capítulos [[Obsidian/lecturas/Fundamentals of Software Architecture/04 Características arquitectónicas|4]] y [[Obsidian/lecturas/Fundamentals of Software Architecture/05 Identificar y priorizar características|5]].

## 7. Dos relojes en un incidente: RPO y RTO

![recuperacion](Recursos%20visuales/07-recuperacion.png)

El último estado recuperable corresponde a las 10:00. El fallo ocurre a las 10:05. Si no hay registros adicionales recuperables, están en riesgo hasta cinco minutos de modificaciones. Eso se compara con el **RPO**, el objetivo que limita la pérdida temporal aceptable de datos.

El servicio vuelve a operar a las 10:20: han transcurrido quince minutos desde el fallo. Ese tiempo observado se compara con el **RTO**, el objetivo de restauración del servicio. Objetivo y resultado son distintos: decir «nuestro RTO es quince minutos» no demuestra que se pueda cumplir.

Si el negocio aceptara un RPO de un minuto, este resultado no lo cumpliría aunque la recuperación del servicio fuera rápida. Si aceptara veinte minutos de interrupción y cinco de datos, ambos resultados entrarían en esos límites, siempre que la integridad y el alcance del servicio restaurado también fueran los acordados.

**La prueba necesaria:** restaurar una copia, verificar datos y reconstruir las dependencias de operación. Tener archivos de respaldo no prueba que claves, permisos, versiones y procedimientos permitan usarlos a tiempo.

## 8. De una frase a evidencia

![requisitos decisiones](Recursos%20visuales/08-requisitos-decisiones.png)

La primera frase expresa una preocupación, pero todavía es ambigua. El segundo paso acota un escenario. El tercero identifica capacidades; el cuarto propone una respuesta estructural; el quinto plantea cómo buscar evidencia.

«Registrar antes de confirmar» protege una expectativa precisa: no comunicar al cliente una aceptación que existe únicamente en memoria volátil. «Aislar el fallo de mapas» evita que una ayuda de navegación derribe la función principal. Cada decisión todavía necesita detalles y pruebas; el esquema no promete durabilidad absoluta ni pago correcto.

Para leer el diagrama al revés, toma cualquier prueba y pregunta qué decisión valida; toma esa decisión y pregunta qué necesidad justifica su costo. Si una caja no conecta con las demás, puede faltar una razón, una prueba o un requisito entendido correctamente.

**Ejercicio de cierre:** cambia la preocupación a «lanzar promociones cada semana sin interrumpir ventas». El escenario y las capacidades pasan a incluir modificabilidad, pruebas y despliegue. Si conservas exactamente las mismas decisiones sin revisarlas, probablemente estás aplicando una solución memorizada.

## 9. Ver la cohesión antes de calcularla

![Responsabilidades mezcladas y módulos cohesivos](Recursos%20visuales/09-cohesion-responsabilidades.png)

Los tickets representan pedidos; las monedas, pagos; los vehículos, entregas. A la izquierda los conceptos están mezclados dentro de cada frontera. A la derecha se agrupan y comunican por interfaces. La idea no es eliminar todo puente, sino concentrar cada regla y reducir el conocimiento innecesario entre módulos. «Baja dependencia» es una intención del ejemplo, no un resultado medido. Pregunta dónde cambiarías una regla de reembolso en cada escena.

## 10. Arquitectura como un conjunto de preguntas

![Cuatro dimensiones conectadas por el contexto](Recursos%20visuales/10-cuatro-dimensiones.png)

Recorre las cuatro zonas: ¿qué capacidades necesito?, ¿qué responsabilidades existen?, ¿cómo se organizan?, ¿por qué elegí esas reglas? La tienda conecta las respuestas con el negocio. No confundas los componentes con dispositivos físicos ni el estilo con el número de contenedores: son símbolos para recordar las preguntas del capítulo 1.

## 11. Aprender a lo ancho y en profundidad

![Amplitud y profundidad del conocimiento técnico](Recursos%20visuales/11-amplitud-profundidad.png)

Las islas muestran alternativas que puedes reconocer; la excavación representa una especialidad que puedes implementar y diagnosticar. Identificar una nueva posibilidad mueve conocimiento hacia «sé que lo desconozco». Dominarla exige práctica y mantenimiento. Los puentes representan exploración, no una arquitectura de servicios.

## 12. No mezclar tiempo individual y producción conjunta

![Latencia, throughput y escalabilidad mediante una cocina](Recursos%20visuales/12-rendimiento-y-capacidad.png)

Cronometrar un pedido da una latencia. Contar pedidos terminados en un intervalo da throughput. Añadir estaciones plantea una pregunta de escalabilidad: ¿cuánto crece el trabajo útil bajo el mismo objetivo? Si todas esperan por un paso compartido, los recursos extra no se aprovechan completamente. La imagen no cuantifica ese límite; las cifras del capítulo 4 permiten practicar cómo medirlo.
