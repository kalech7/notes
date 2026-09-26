---
title: "02 Pensamiento arquitectónico · 2.ª edición"
created: 2026-09-25
tags:
  - lecturas/software-architecture
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Índice]]

# 02 · Pensamiento arquitectónico · 2.ª edición

## Alcance y modo de lectura

Esta guía desarrolla el capítulo 2, *Architectural Thinking*, de **Mark Richards y Neal Ford, Fundamentals of Software Architecture, segunda edición**. La fuente disponible corresponde al **PDF 21.32, páginas 13–31**, equivalentes a las **páginas impresas 17–35**. Se consultó el texto extraído de cada página y se revisaron las imágenes del escaneo. El archivo de consulta es [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/01 Introducción y pensamiento arquitectónico.pdf|01 Introducción y pensamiento arquitectónico]]. Los números «PDF» de esta nota se refieren a ese fragmento, no a una edición digital completa.

> [!info] Libro, elaboración y supuestos
> Las referencias identifican las ideas del libro. **PedidoClaro es una tienda de sándwiches inventada para esta guía**, distinta de la kata *Silicon Sandwiches*. Sus cifras, decisiones y ejercicios son elaboración didáctica propia. La explicación de agilidad compuesta es una ampliación: no aparece desarrollada con ese nombre en las páginas asignadas. La corrección sobre RabbitMQ se distingue y enlaza a documentación oficial.

Pensar arquitectónicamente significa preguntar qué consecuencias tendrá una decisión sobre el sistema y las personas que lo construyen y operan. Elegir una biblioteca puede parecer un detalle local; si condiciona los despliegues de diez equipos durante cinco años, sus consecuencias dejan de ser locales. La mirada arquitectónica conecta estructura, restricciones, conocimiento y negocio. **Fuente: PDF p. 13; impresa p. 17.**

## 1. Arquitectura y diseño forman un espectro

El libro introduce la diferencia mediante una casa: distribución general frente a decisiones interiores. La analogía orienta, pero no convierte todo diseño de software en apariencia visual. Diseñar una clase, un algoritmo o una interacción también supone decisiones internas. Lo decisivo es el alcance de sus consecuencias.

Richards y Ford proponen tres criterios: **carácter estratégico, esfuerzo de construcción o cambio y relevancia de las compensaciones**. Una compensación, o *trade-off*, existe cuando conseguir una ventaja implica aceptar un costo, una restricción o un riesgo. **Fuente: PDF pp. 13–16; impresas pp. 17–20.**

![1. Arquitectura y diseño forman un espectro ](Recursos%20visuales/Diagramas/cap02-diagrama-01.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap02-diagrama-01.mmd)

**Interpretación:** los tres criterios permiten discutir cuánto alcance tiene una decisión. **Límite:** no son una fórmula ni una votación; una sola consecuencia difícil de revertir puede justificar atención arquitectónica.

### Estrategia: cuánto futuro estamos comprometiendo

Una decisión estratégica dirige muchas acciones posteriores. El libro propone observar cuánto análisis requiere, cuántas personas participan y cuánto tiempo se espera que dure. Son indicios, no pruebas: una reunión multitudinaria también puede discutir un detalle trivial.

En PedidoClaro, cambiar el orden de dos campos del formulario suele ser táctico. Decidir que cada franquicia conservará pedidos localmente cuando pierda conexión condiciona sincronización, identificación de pedidos, conciliación y soporte. Su alcance estratégico procede de esas dependencias, no del cargo de quien decide.

### Esfuerzo: la reversibilidad tiene precio

Una decisión difícil de cambiar suele estar cerca del extremo arquitectónico. El esfuerzo incluye código, migración de datos, formación, operaciones y coordinación. **Supuesto didáctico:** cambiar una biblioteca encapsulada cuesta dos jornadas; reemplazar un formato de pedidos compartido por doce integraciones requiere ocho semanas. Aunque ambos cambios afecten pocos archivos centrales, sus costos reales son diferentes.

El criterio también invita a diseñar opciones reversibles. Si un adaptador permite cambiar un proveedor sin modificar reglas comerciales, reduce el costo de una decisión futura. No elimina las diferencias funcionales entre proveedores ni hace gratuita la migración.

### Compensaciones: una ventaja no decide por sí sola

El libro contrapone beneficios y costos de los microservicios. Conviene entenderlo como una comparación de tendencias: distribuir servicios puede facilitar escalado selectivo y despliegues independientes, pero añade comunicación remota, operación y coordinación de datos. No implica que todo microservicio sea lento ni que la consistencia fuerte resulte imposible.

En PedidoClaro, separar promociones permitiría desplegarlas sin publicar el resto. A cambio, calcular el total podría depender de otra llamada de red. Si el beneficio es ahorrar una publicación mensual y el costo es introducir una dependencia en cada compra, hace falta justificar la decisión con necesidades concretas.

## 2. Amplitud y profundidad: administrar el conocimiento

![Amplitud para reconocer alternativas y profundidad para dominar una especialidad](Recursos%20visuales/11-amplitud-profundidad.png)

**Cómo leer la imagen:** recorrer varias islas equivale a descubrir alternativas; excavar en una de ellas equivale a dominar implementación y diagnóstico. Los puentes representan aprendizaje entre áreas, no dependencias entre servicios. Las tres tarjetas distinguen conocimiento operativo, lagunas reconocidas y posibilidades todavía desconocidas. El dibujo no mide conocimientos ni exige especializarse en una sola materia para siempre.

La **profundidad** permite implementar y diagnosticar una tecnología con competencia. La **amplitud** permite reconocer varias soluciones y saber qué investigar. El libro representa el conocimiento en tres niveles: lo que sabemos, lo que sabemos que desconocemos y lo que ni siquiera sabemos que existe. **Fuente: PDF pp. 16–19; impresas pp. 20–23.**

![2. Amplitud y profundidad: administrar el conocimiento ](Recursos%20visuales/Diagramas/cap02-diagrama-02.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap02-diagrama-02.mmd)

**Interpretación:** primero descubrimos una posibilidad y después profundizamos cuando hace falta. **Límite:** es una representación conceptual de la pirámide, no una medición; conocer el nombre de una herramienta todavía no permite elegirla responsablemente.

Supongamos que PedidoClaro almacena pedidos en una base relacional. Quien solo conoce esa herramienta intentará resolver con ella todos los problemas. Quien reconoce colas, cachés y procesamiento por lotes puede formular alternativas, aunque necesite ayuda para implementarlas. La amplitud mejora el conjunto de opciones; la profundidad permite comprobar que una opción funciona.

El punto delicado es que **la experiencia exige mantenimiento**. Cambian versiones, prácticas y limitaciones. El libro advierte de dos disfunciones: intentar conservar dominio profundo de demasiadas áreas hasta agotarse, y seguir decidiendo con conocimientos que han envejecido sin advertirlo.

Como ejercicio propio, imaginemos cuatro horas semanales para aprender. Si mantener seis especialidades requiere una hora por especialidad, ya faltan dos horas y no queda espacio para descubrir nada. La respuesta no consiste en aprender más deprisa indefinidamente: consiste en elegir qué dominios conservar, cuáles conocer superficialmente y cuándo consultar especialistas. Para un arquitecto, admitir «conozco la alternativa, pero necesito verificar sus garantías» es una práctica rigurosa.

## 3. Experiencia congelada, burbujas y aprendizaje deliberado

### Frozen Caveman: convertir un incidente en una ley universal

El antipatrón *Frozen Caveman* describe la insistencia en una preocupación heredada de experiencias pasadas. El libro cuenta cómo un antiguo problema de comunicación con Italia dominaba conversaciones arquitectónicas posteriores. La experiencia aporta señales; el problema aparece cuando sustituye la evaluación del contexto. **Fuente: PDF p. 20; impresa p. 24.**

En PedidoClaro, una caída de un proveedor podría llevar a exigir dos proveedores para absolutamente todo. Esa medida duplica integraciones, contratos y pruebas. La pregunta útil es qué fallos siguen siendo plausibles, qué impacto tienen y cuánto reduce cada medida ese impacto.

**Modelo propio simplificado:** si una interrupción tiene probabilidad anual de 0,10 y pérdida estimada de 20.000 unidades monetarias, su pérdida esperada es 2.000. Una mitigación anual de 12.000 requiere razones adicionales o mejores estimaciones. Este cálculo no decide por sí solo: las obligaciones contractuales, pérdidas extremas y daños difíciles de valorar pueden dominar la decisión.

### Burbujas: confundir nuestro entorno con el mundo

El libro utiliza la experiencia con Clipper y el cambio de DOS a Windows para explicar cómo una comunidad puede dejar de percibir alternativas externas. Una burbuja tecnológica refuerza opiniones porque quienes la integran comparten herramientas, intereses y fuentes. **Fuente: PDF pp. 21–22; impresas pp. 25–26.**

Salir de ella exige buscar explicaciones de personas que resuelven problemas diferentes. En PedidoClaro, leer solo casos de grandes plataformas puede inducir una complejidad operativa que un equipo de cuatro personas no puede sostener. Leer solo experiencias del propio proveedor también oculta sus límites.

### Regla de los veinte minutos

Los autores recomiendan reservar al menos veinte minutos diarios para aprender, preferentemente al comenzar la jornada y antes del correo. Es una técnica para proteger la atención, no una garantía automática de competencia. **Fuente: PDF pp. 20–21; impresas pp. 24–25.**

Con cinco días semanales y 48 semanas, veinte minutos suman **80 horas anuales**. Una rutina propia útil consiste en registrar qué problema resuelve una idea, qué supone y qué desconocemos todavía. Leer sobre cachés hoy no obliga a instalarlas mañana: puede bastar con reconocer cuándo investigar invalidación, caducidad o consistencia.

## 4. Un radar personal convierte curiosidad en decisiones

El radar presentado por el libro organiza el aprendizaje mediante **cuadrantes**, que indican el tipo de elemento, y **anillos**, que expresan una postura frente a él. No son dos listas intercambiables. **Fuente: PDF pp. 22–25; impresas pp. 26–29.**

| Cuadrante | Qué organiza | Ejemplo propio para PedidoClaro |
| --- | --- | --- |
| Herramientas | Utilidades de desarrollo e integración | Analizador de dependencias |
| Lenguajes y frameworks | Lenguajes, bibliotecas y marcos | Biblioteca de pruebas de contratos |
| Técnicas | Prácticas de ingeniería y procesos | Revisiones de decisiones |
| Plataformas | Bases de datos, nubes y sistemas operativos | Plataforma de mensajería |

Los cuatro anillos, de fuera hacia dentro, son:

| Anillo | Interpretación en el libro | Uso personal propuesto |
| --- | --- | --- |
| Hold | Evitar nuevas adopciones; su significado evolucionó | Identificar tecnologías o hábitos que conviene evitar |
| Assess | Merece exploración | Investigar una posibilidad todavía poco conocida |
| Trial | Merece una prueba o piloto | Practicar y comprobar límites concretos |
| Adopt | Recomendación favorable de adopción | Incorporar prácticas adecuadas a problemas conocidos |

El libro adapta los significados para el radar personal. **Adopt no significa «sirve para cualquier proyecto»** y **Hold no obliga a eliminar inmediatamente instalaciones existentes**. Tampoco todo elemento debe avanzar hacia el centro: descartar una opción después de investigarla puede ser el resultado correcto.

Para PedidoClaro, una plataforma de mensajes podría entrar en Assess al detectar retrasos en notificaciones. Pasaría a Trial con una prueba que mida acumulación y recuperación; solo se recomendaría para ese contexto cuando el equipo demostrase capacidad de operación. Esta secuencia es elaboración propia, no una recomendación del libro sobre un producto concreto.

Conviene anotar fecha, evidencia y próxima revisión. Sin ello, el radar puede convertirse en otra colección de preferencias antiguas. El libro subraya que reflexionar y conversar sobre el portafolio importa más que producir una visualización bonita.

## 5. Analizar compensaciones: el caso de las subastas

El ejemplo del libro contiene un productor de pujas y tres servicios: captura, seguimiento y analítica. Todos necesitan información de la puja. Se comparan una publicación a un *topic* y publicaciones dirigidas a colas separadas. **Fuente: PDF pp. 26–29; impresas pp. 30–33.**

En la topología dibujada con colas, el productor conoce tres destinos. Añadir un servicio de historial obliga a añadir otro destino y modificar esa coordinación. Con publicación/suscripción, el productor publica para suscriptores y el nuevo servicio puede incorporarse sin cambiar su lógica. Esa ventaja procede del **desacoplamiento respecto a los receptores**, no de una propiedad mágica del nombre «topic».

El libro después examina acceso a datos, contratos y supervisión. Su intención pedagógica es valiosa: buscar costos después de identificar beneficios. Sin embargo, algunas afirmaciones son demasiado generales. La propia página PDF 29 introduce una excepción basada en separar *exchange* y cola.

> [!warning] Matiz técnico respaldado por documentación externa
> Un topic no es intrínsecamente inseguro ni impide supervisión o autoescalado. RabbitMQ combina un exchange de publicación/suscripción con una cola por suscriptor lógico; las réplicas sobre una misma cola reparten trabajo, no reciben cada una todas las copias. Hay controles de acceso y métricas de colas; el autoescalado requiere una política y un mecanismo adicionales. Referencias: [publicación/suscripción](https://www.rabbitmq.com/tutorials/tutorial-three-python), [control de acceso](https://www.rabbitmq.com/docs/access-control), [monitorización](https://www.rabbitmq.com/docs/monitoring).

### Aplicación propia: un pedido, varios intereses

En PedidoClaro, cocina, notificaciones y analítica representan tres intereses diferentes. **Supuesto:** cada pedido confirmado debe producir una tarea para cada interés. El siguiente esquema adapta la separación entre distribución y procesamiento; no reproduce la figura del libro.

![Aplicación propia: un pedido, varios intereses ](Recursos%20visuales/Diagramas/cap02-diagrama-03.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap02-diagrama-03.mmd)

**Interpretación:** hay una ruta independiente por interés; los trabajadores de cocina comparten su carga. **Límite:** el dibujo no especifica persistencia, confirmaciones, reintentos ni orden. Un evento puede volver a entregarse si se reintenta; procesarlo no debe equivaler a cobrar o preparar dos veces por accidente.

**Cálculo didáctico:** llegan 120 eventos por segundo a analítica y cada trabajador procesa 50. Con dos trabajadores, la capacidad nominal es 100 y se acumulan 20 eventos por segundo: 12.000 en diez minutos. Tres trabajadores ofrecerían 150 y, manteniendo la entrada, vaciarían esa acumulación a 30 por segundo, aproximadamente en 400 segundos.

El cálculo supone trabajo uniforme, capacidad sumable y ausencia de otro cuello de botella. Una base saturada puede impedir que el tercer trabajador aporte capacidad. Además de profundidad de cola, interesa cuánto tiempo lleva esperando el evento más antiguo: una acumulación estable también puede incumplir el servicio esperado.

### Contratos: compartir información no elimina la evolución

Un contrato define campos, tipos y significado. El ejemplo del libro observa que modificar un mensaje común puede afectar a varios consumidores. **Afectar exige evaluar compatibilidad; no equivale a romperlos automáticamente.** Esta precisión es elaboración técnica propia sobre el ejemplo.

Si añadimos `canalOrigen` como campo opcional y los consumidores toleran campos desconocidos, el cambio puede ser compatible. Si renombramos `total` o cambiamos su significado de centavos a unidades, podemos romperlos aunque el mensaje siga siendo sintácticamente válido. Una cola dedicada tampoco vuelve seguro cualquier cambio: su receptor sigue teniendo expectativas.

La pregunta arquitectónica es qué consumidores necesitan qué información, quién puede acceder, cómo evolucionan los contratos y cómo se recuperan fallos. Agregar un suscriptor puede evitar cambios en el productor y aun así exigir permisos, configuración, capacidad y pruebas. El desacoplamiento reduce determinadas dependencias; no elimina todo trabajo de integración.

## 6. Traducir negocio y entender la agilidad compuesta

El libro exige comprender los objetivos comerciales y convertirlos en características arquitectónicas. Las conversaciones con responsables del negocio son parte del trabajo técnico porque revelan qué resultados justifican los costos. **Fuente: PDF p. 29; impresa p. 33.**

«Queremos crecer» es insuficiente. Para PedidoClaro debemos distinguir más tiendas, más pedidos simultáneos o más cambios de menú. Cada crecimiento impone problemas diferentes. **Supuestos didácticos:** aceptar 120 pedidos por segundo durante una promoción plantea capacidad; confirmar el 95 % en menos de dos segundos plantea latencia; incorporar promociones semanalmente plantea facilidad para cambiar, probar y desplegar.

La **agilidad compuesta —composite agility—** se desarrolla aquí como ampliación propia: cambiar rápido depende de varias capacidades que deben funcionar juntas. Escribir código deprisa aporta poco si las pruebas tardan días o cada publicación exige coordinar todos los servicios.

![6. Traducir negocio y entender la agilidad compuesta ](Recursos%20visuales/Diagramas/cap02-diagrama-04.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap02-diagrama-04.mmd)

**Interpretación:** la agilidad emerge del recorrido completo. **Límite:** no es una ecuación universal; el proceso real contiene trabajo paralelo, retroalimentación y esperas.

En un modelo secuencial, desarrollar una promoción tarda un día, probarla tres y esperar su despliegue cinco: nueve días. Reducir programación a medio día solo ahorra medio día. Reducir pruebas a uno y espera a uno deja un recorrido de tres días, aun conservando el día de programación. La arquitectura ayuda cuando limita el impacto del cambio y facilita pruebas y despliegues; la organización también determina las esperas.

## 7. Seguir programando sin convertirse en cuello de botella

Los autores defienden mantener contacto con el código. El peligro es la **Bottleneck Trap**: asumir piezas críticas cuya entrega depende de una persona que también atiende reuniones y decisiones arquitectónicas. **Fuente: PDF pp. 29–31; impresas pp. 33–35.**

Supongamos que el componente de pagos exige veinte horas de trabajo y el arquitecto dispone de cinco horas semanales para programar. Incluso sin imprevistos, necesita cuatro semanas; los equipos dependientes heredan esa espera. No es un problema de capacidad intelectual, sino de disponibilidad y dependencia.

El libro propone delegar piezas críticas y contribuir a funcionalidad menos urgente, prevista una a tres iteraciones después. Así se conserva experiencia con el entorno real y se distribuye conocimiento. Esto no significa desentenderse de decisiones delicadas: se puede acompañar su diseño sin monopolizar implementación y aprobación.

Las alternativas del libro tienen propósitos distintos:

- **POC frecuentes:** implementar un experimento para comprobar una incertidumbre. Comparar dos cachés exige cargas y criterios equivalentes. Los autores recomiendan código cuidado porque el prototipo puede convertirse en referencia; eso no demuestra que esté listo para producción.
- **Deuda técnica:** reducir obstáculos acumulados. Matiz propio: no toda deuda es postergable; una dependencia vulnerable o una migración obligatoria puede estar en la ruta crítica.
- **Corrección de bugs:** descubrir fallos reales de comprensión y estructura. Conviene elegir trabajos compatibles con la disponibilidad; un incidente urgente no debe depender de huecos en la agenda.
- **Automatización:** eliminar comprobaciones repetitivas y crear verificaciones de arquitectura. Una regla que prohíba dependencias indebidas ofrece retroalimentación repetible, aunque no certifique la calidad completa del sistema.
- **Revisiones de código:** comprender implementación y acompañar al equipo. Exigir la aprobación personal del arquitecto en cada cambio recrearía el mismo cuello de botella.

## 8. Preguntas para comprobar comprensión

### 1. ¿Elegir un framework de interfaz siempre es diseño?

> [!success]- Solución
> No. Si compromete años de formación, accesibilidad, despliegue e integración, tiene consecuencias arquitectónicas. Deben evaluarse estrategia, esfuerzo de cambio y compensaciones, no clasificar por el nombre de la tecnología.

### 2. ¿Qué gana alguien al reconocer una herramienta que todavía no sabe usar?

> [!success]- Solución
> Amplía las alternativas investigables. Pasa de desconocer su existencia a reconocer una posibilidad y sus preguntas pendientes. Todavía necesita evidencia, práctica o apoyo especializado antes de confiar una decisión a esa herramienta.

### 3. ¿Cómo distinguir prudencia de Frozen Caveman?

> [!success]- Solución
> La prudencia actualiza probabilidad, impacto y medidas según el contexto. El antipatrón convierte un episodio pasado en preocupación dominante sin revisar evidencia. Recordar un fallo es útil; asumir que debe gobernar todos los sistemas exige justificación.

### 4. ¿Hold significa borrar una tecnología y Adopt significa adoptarla siempre?

> [!success]- Solución
> No. Hold desaconseja nuevas adopciones o señala hábitos que evitar; puede coexistir con uso existente. Adopt expresa una valoración favorable dentro de un contexto. Ambos requieren fecha, motivos y revisión.

### 5. ¿Tres consumidores de una única cola garantizan tres copias por pedido?

> [!success]- Solución
> No en el modelo de trabajadores competidores explicado aquí: reparten entregas. Si cocina, notificaciones y analítica necesitan cada pedido, deben tener suscripciones independientes, representadas por colas distintas en nuestro esquema. Los reintentos tampoco sustituyen la difusión.

### 6. ¿Un campo adicional obliga a modificar todos los consumidores?

> [!success]- Solución
> Depende del contrato y de sus reglas de compatibilidad. Un campo opcional ignorado por lectores antiguos puede ser compatible. Renombrar campos, cambiar unidades o introducir obligatoriedad requiere otro análisis. Hay que comprobar comportamiento, no solo sintaxis.

### 7. ¿Programar la pieza más difícil demuestra que el arquitecto ayuda más?

> [!success]- Solución
> Solo si su disponibilidad y la organización del trabajo lo permiten. Monopolizar una dependencia crítica puede retrasar a todos. Delegar, acompañar, experimentar y automatizar puede aportar más al resultado global que concentrar código difícil en una persona.

## 9. Ejercicio aplicado: historial de pedidos

**Escenario inventado:** PedidoClaro ya publica pedidos para cocina, notificaciones y analítica. Se añadirá historial. En campañas llegan 90 eventos por segundo; cada trabajador de historial procesa 40. Historial admite hasta treinta segundos de retraso y no necesita direcciones de entrega. El arquitecto tiene cuatro horas semanales disponibles.

Propón una suscripción, capacidad inicial, restricciones de datos, prueba de compatibilidad y reparto del trabajo. Explica una ventaja y un costo de tu opción; define qué evidencia permitiría cambiarla.

> [!success]- Solución orientativa
> Una cola propia para historial permite consumir independientemente. Dos trabajadores sumarían 80 eventos por segundo, menos que los 90 entrantes; tres ofrecen 120 nominales y un margen de 30. Esto no garantiza treinta segundos de retraso: hay que medir ráfagas, tiempos y recuperación. El mensaje destinado a historial debe excluir direcciones innecesarias; sus permisos deben limitarse a su función. Una prueba comprobaría lectores antiguos frente a un campo opcional nuevo y rechazaría cambios incompatibles de unidades. El equipo implementaría la ruta productiva y el arquitecto haría una POC acotada. La ventaja es independencia; el costo, otra suscripción y operación. Revisaríamos capacidad si la antigüedad de eventos crece o la base limita el rendimiento.

## Referencias y límites de la fuente

La correspondencia de este fragmento es **página impresa = página PDF + 4**. El encabezado inicial y el último pie presentan ruido OCR; 17 y 35 se reconstruyen por continuidad con páginas interiores legibles. Los diagramas de esta guía son elaboraciones propias, no reproducciones de figuras escaneadas.

| Tema | Páginas del PDF 21.32 | Páginas impresas |
| --- | --- | --- |
| Espectro arquitectura/diseño | 13–16 | 17–20 |
| Pirámide y mantenimiento del conocimiento | 16–19 | 20–23 |
| Frozen Caveman y veinte minutos | 20–21 | 24–25 |
| Burbujas y radar | 21–25 | 25–29 |
| Subastas y compensaciones | 26–29 | 30–33 |
| Negocio y trabajo con código | 29–31 | 33–35 |

![colas y publicacion](Recursos%20visuales/02-colas-y-publicacion.png)

*Figura original: repartir entregas dentro de una cola y difundir eventos entre intereses son operaciones distintas.* Las afirmaciones generales de mensajería deben leerse con el matiz documentado; la agilidad compuesta y las cifras de PedidoClaro son ampliaciones explícitas. Esta nota no presupone contenido de páginas ausentes.
