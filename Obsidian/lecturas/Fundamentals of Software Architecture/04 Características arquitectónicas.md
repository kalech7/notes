---
title: "04 · Características arquitectónicas · 2.ª edición"
created: 2026-09-25
tags:
  - lecturas/software-architecture
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Índice]]

# 04 · Características arquitectónicas · 2.ª edición

> [!info] Fuente y alcance
> Basado en Mark Richards y Neal Ford, *Fundamentals of Software Architecture*, segunda edición, capítulo 4: **páginas 1–11 del PDF «03 Características e identificación», correspondientes a las impresas 55–65**. Las referencias siguientes distinguen ambas numeraciones. No se presupone contenido de páginas ausentes. [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/03 Características e identificación.pdf#page=1|Abrir la fuente]].
>
> **PedidoClaro es una tienda de sándwiches inventada para esta guía**, distinta de la kata Silicon Sandwiches del libro. Sus cifras, decisiones y ejercicios son elaboración propia. Las fórmulas y precisiones técnicas también son ampliaciones didácticas, no citas de los autores.

## 1. Comportamiento y capacidades: dos preguntas distintas

El dominio describe **qué hace** el sistema. En PedidoClaro: seleccionar pan, calcular un precio y registrar un pedido. Una característica arquitectónica expresa una capacidad necesaria para que ese comportamiento resulte útil: responder dentro de cierto tiempo, resistir fallos o permitir cambios sin afectar funciones ajenas. Una compra correctamente calculada que tarda veinte minutos puede resultar comercialmente inútil.

El libro contrapone *behavior*, comportamiento del dominio, y *capabilities*, capacidades del sistema. Prefiere «características arquitectónicas» a «requisitos no funcionales» y «atributos de calidad» para destacar su importancia durante el diseño. Otros equipos pueden usar los términos alternativos con rigor. **Fuente: PDF pp. 1–3; impresas 55–57.**

Para los autores deben concurrir **tres criterios**:

1. **Consideración ajena a la funcionalidad del dominio.** «Calcular descuentos» define comportamiento; «calcularlos con p95 inferior a 300 ms bajo una carga acordada» añade una capacidad.
2. **Influencia estructural.** El requisito obliga a considerar organización, límites, dependencias, distribución o mecanismos de infraestructura. No toda buena práctica local determina la arquitectura.
3. **Importancia para el éxito.** Debe existir una razón concreta para invertir: pérdida de pedidos, riesgo de datos, imposibilidad de evolucionar o interrupción del negocio.

![1. Comportamiento y capacidades: dos preguntas distintas ](Recursos%20visuales/Diagramas/cap04-diagrama-01.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap04-diagrama-01.mmd)

**Interpretación:** los tres criterios se necesitan conjuntamente. **Límite:** las flechas no representan una secuencia ni un algoritmo automático; determinar la influencia estructural requiere juicio contextual.

Cambiar el color de un botón puede ser local. Garantizar accesibilidad en cientos de pantallas puede exigir componentes compartidos, navegación uniforme y verificaciones continuas: el alcance cambia las consecuencias arquitectónicas.

**Explícitas e implícitas.** Una característica explícita aparece en documentos o instrucciones; una implícita se descubre al comprender el negocio. «No perder pedidos cobrados» puede no estar escrito, pero de allí se derivan necesidades de integridad y recuperación. Inferirlas no autoriza a inventar exigencias ilimitadas: hay que convertir la hipótesis en una condición verificable y validarla con quienes conocen el negocio. **Fuente: PDF pp. 3–4; impresas 57–58.**

### Una precisión sobre seguridad y monolitos

En la página impresa 58, el libro contrasta prácticas de seguridad locales con estructuras especializadas y señala límites al escalado monolítico. **Matiz técnico de esta guía:** un monolito puede escalar horizontalmente mediante varias instancias, siempre que gestione adecuadamente estado, sesiones y recursos compartidos. Separar servicios tampoco garantiza escalabilidad: una base de datos saturada o llamadas encadenadas pueden conservar el cuello de botella.

La seguridad requiere analizar amenazas y controles en cualquier estilo. Un monolito puede necesitar aislamiento o separación de privilegios; contratar un proveedor de pagos no protege automáticamente sesiones, autorizaciones ni datos del resto de PedidoClaro. La pregunta útil es qué estructura necesita el riesgo concreto.

## 2. Catálogo completo de las cuatro tablas

Las tablas siguientes incluyen **todas las entradas de las tablas 4-1 a 4-4**. Las explicaciones desarrollan su significado y los ejemplos son propios. Las categorías ayudan a conversar; no son compartimentos exclusivos ni una lista de todo lo que existe.

### Operacionales: qué ocurre mientras funciona

**Fuente: tabla 4-1, PDF p. 5; impresa 59.**

| Entrada del libro | Significado y ejemplo en PedidoClaro |
|---|---|
| Disponibilidad (*availability*) | Estar operativo y accesible cuando se necesita. La compra debe funcionar durante el horario acordado; un proceso vivo que rechaza pedidos no basta. |
| Continuidad (*continuity*) | Capacidad frente a desastres. Si se pierde un centro de cómputo, existe una estrategia para sostener o restablecer la operación. |
| Rendimiento (*performance*) | Comportamiento temporal y bajo carga. Evaluar respuestas, picos y operaciones frecuentes; una prueba con un usuario no representa el almuerzo. |
| Recuperabilidad (*recoverability*) | Recuperar servicio y estado tras un fallo. Restaurar pedidos desde copias verificadas y medir cuánto demora. |
| Fiabilidad / seguridad frente a daños (*reliability/safety*) | El libro agrupa ambas y menciona criticidad, vidas y pérdidas. Aquí se distinguen: fiabilidad es funcionar correctamente durante un intervalo; *safety* trata de evitar daños inaceptables. Mostrar correctamente alérgenos ilustra esta última. |
| Robustez (*robustness*) | Manejar errores y condiciones límite sin comportamiento descontrolado. Una conexión interrumpida produce un resultado claro y permite reintentar sin duplicar compras. |
| Escalabilidad (*scalability*) | Sostener la operación al aumentar usuarios o solicitudes. Añadir capacidad debe permitir atender más pedidos dentro de objetivos acordados. |

Continuidad es la capacidad global de afrontar la interrupción; recuperabilidad se concentra en volver a un estado operativo. Robustez incluye entradas inválidas y condiciones extremas; no se limita a duplicar servidores. *Safety* tampoco equivale a *security*: prevenir daños y proteger frente a accesos o acciones indebidas son preocupaciones relacionadas, pero distintas.

### Estructurales: qué permite la organización interna

**Fuente: tabla 4-2, PDF p. 6; impresa 60.**

| Entrada del libro | Significado y ejemplo propio |
|---|---|
| Configurabilidad (*configurability*) | Facilitar que usuarios finales cambien opciones mediante interfaces: modificar horarios sin editar código. |
| Extensibilidad (*extensibility*) | Incorporar funcionalidad adicional: introducir nuevos tipos de promociones mediante límites preparados para esa variación. |
| Instalabilidad (*installability*) | Instalar en las plataformas necesarias con dificultad controlada: preparar una nueva caja sin pasos manuales ambiguos. |
| Aprovechamiento / reutilización (*leverageability/reuse*) | Usar componentes comunes en distintos productos: compartir un cálculo monetario entre tienda y administración. |
| Localización (*localization*) | Adaptar idiomas de pantallas y campos. En el ejemplo, mostrar etiquetas y formatos locales; traducir texto no resuelve por sí solo todos los formatos. |
| Mantenibilidad (*maintainability*) | Aplicar correcciones y mejoras con esfuerzo y riesgo razonables: ajustar impuestos sin romper pagos. |
| Portabilidad (*portability*) | Funcionar en distintas plataformas: cambiar de motor de datos sin rehacer toda la aplicación. |
| Actualizabilidad (*upgradeability*) | Pasar a nuevas versiones de servidores y clientes con facilidad: actualizar cajas y conservar compatibilidad durante la transición. |

Extender agrega posibilidades; mantener incluye corregir y adaptar. Instalar establece una versión en un entorno; actualizar transforma una instalación existente y puede requerir migraciones. Reutilizar tampoco es gratis: una biblioteca compartida exige coordinar contratos y versiones entre consumidores.

### Nube: capacidades ofrecidas por el proveedor

**Fuente: tabla 4-3, PDF p. 6; impresa 60.**

| Entrada del libro | Significado y ejemplo propio |
|---|---|
| Escalabilidad bajo demanda (*on-demand scalability*) | Obtener recursos dinámicamente al aumentar la demanda: ampliar instancias para más sucursales. |
| Elasticidad bajo demanda (*on-demand elasticity*) | Ajustarse a fluctuaciones: aumentar capacidad durante el almuerzo y reducirla después. |
| Disponibilidad por zonas (*zone-based availability*) | Separar recursos entre zonas para reducir el impacto de ciertos fallos: mantener instancias en dos zonas. |
| Privacidad y seguridad por regiones (*region-based privacy and security*) | Considerar dónde pueden residir los datos y qué restricciones regionales afectan al proveedor: elegir ubicación de datos y copias según obligaciones verificadas. |

La capacidad del proveedor no equivale a la propiedad del sistema. Dos zonas pueden depender de una base de datos sin recuperación. Una región tampoco demuestra cumplimiento: intervienen copias, registros, accesos y transferencias. Una obligación concreta exige comprobar jurisdicción, contratos y criterio profesional aplicable.

### Transversales: atraviesan componentes y responsabilidades

**Fuente: tabla 4-4, PDF p. 7; impresa 61.**

| Entrada del libro | Significado y ejemplo propio |
|---|---|
| Accesibilidad (*accessibility*) | Permitir el uso por personas con diversas capacidades: navegación por teclado y mensajes que no dependan solo del color. |
| Archivabilidad (*archivability*) | Archivar o eliminar datos tras períodos definidos: separar historial operativo y archivo según una política acordada. |
| Autenticación (*authentication*) | Comprobar identidad: verificar quién inicia sesión como encargado. |
| Autorización (*authorization*) | Limitar acciones y datos por permisos: un encargado solo modifica su sucursal. |
| Legal (*legal*) | Restricciones normativas y derechos relevantes para construcción, despliegue y datos. El libro menciona GDPR y Sarbanes-Oxley como ejemplos; no se presume su aplicabilidad a PedidoClaro. |
| Privacidad (*privacy*) | Restringir exposición de información; el libro destaca ocultarla incluso a personal interno privilegiado. Ejemplo: limitar el acceso a direcciones de clientes. |
| Seguridad (*security*) | Controles de protección, cifrado, comunicaciones y acceso. Ejemplo: proteger credenciales y verificar permisos en el servidor. |
| Soportabilidad (*supportability*) | Facilitar soporte y diagnóstico: correlacionar un pedido con sus errores sin revelar datos innecesarios. |
| Usabilidad / logro de objetivos (*usability/achievability*) | Permitir alcanzar objetivos con formación razonable: completar un pedido sin instrucciones externas. |

Autenticarse no concede todos los permisos. Cifrar no garantiza privacidad si demasiadas personas poseen acceso legítimo. Añadir registros mejora diagnóstico, pero registrar direcciones completas aumenta exposición: una decisión afecta varias características simultáneamente.

## 3. Las familias ISO tal como aparecen en el libro

Los autores presentan una selección de definiciones ISO **reformuladas por ellos**. Esta sección reproduce esa organización conceptual; **no afirma cuál es la versión vigente de una norma ni su conformidad literal**. **Fuente: PDF pp. 8–10; impresas 62–64.**

| Familia presentada | Subcaracterísticas y lectura práctica |
|---|---|
| Eficiencia del rendimiento | Comportamiento temporal, utilización de recursos y capacidad. No basta responder rápido: importa con qué recursos y bajo qué límites. |
| Compatibilidad | Coexistencia e interoperabilidad. Compartir un entorno sin interferencia excesiva es distinto de intercambiar información utilizable. |
| Usabilidad | Reconocimiento de adecuación, facilidad de aprendizaje, protección frente a errores del usuario y accesibilidad. Comprender que una pantalla sirve para cancelar no significa poder operarla fácilmente. |
| Fiabilidad | Madurez, disponibilidad, tolerancia a fallos y recuperabilidad. Agrupa operación normal, acceso, continuidad ante fallos y restauración. |
| Seguridad | Confidencialidad, integridad, no repudio, responsabilidad trazable (*accountability*) y autenticidad. Identificar al actor y conservar evidencia de acciones resuelven necesidades diferentes. |
| Mantenibilidad | Modularidad, reutilización, analizabilidad, modificabilidad y testabilidad. Entender un fallo, modificarlo y comprobar la corrección son capacidades complementarias. |
| Portabilidad | Adaptabilidad, instalabilidad y reemplazabilidad. Cambiar entorno y sustituir una pieza no son la misma operación. |
| Adecuación funcional | Completitud, corrección y pertinencia funcional. Cubrir tareas, producir resultados correctos y facilitar objetivos son dimensiones diferentes. |

Los autores **excluyen la adecuación funcional** de su catálogo porque describe motivaciones y funciones del dominio. No significa que la corrección importe menos: «cobrar el importe correcto» es indispensable, aunque pertenezca a otra categoría de su marco.

En la discusión previa, el libro diferencia interoperabilidad como facilidad de integración y compatibilidad como atención a estándares. Después, la clasificación ISO presentada incluye interoperabilidad dentro de compatibilidad. No conviene fundir ambas organizaciones como si fueran idénticas: muestran por qué hace falta declarar el vocabulario utilizado.

## 4. Rendimiento: medir la experiencia que se quiere proteger

![Latencia de una operación, throughput de resultados completados y escalabilidad con más recursos](Recursos%20visuales/12-rendimiento-y-capacidad.png)

**Cómo leer la imagen:** a la izquierda seguimos un pedido desde su inicio hasta su resultado: latencia. En el centro contamos resultados terminados durante un intervalo: throughput. A la derecha aumentamos recursos, pero estos siguen compartiendo un paso: el cuello de botella puede limitar la mejora. Tres cocineros no garantizan tres veces más capacidad, y el único sándwich final es un símbolo del recurso compartido, no un resultado cuantitativo. En software hay que definir las fronteras de la operación y medir la carga real.

**Ampliación didáctica.** La latencia es el tiempo entre dos eventos definidos; por ejemplo, enviar una compra y recibir su confirmación. El *throughput* es trabajo completado por unidad de tiempo, como pedidos por segundo. La capacidad es el máximo volumen sostenible **bajo condiciones y objetivos definidos**; puede expresarse en solicitudes por segundo, usuarios concurrentes o almacenamiento según la pregunta.

Un sistema que completa muchas respuestas de error tiene throughput, pero quizá casi ningún pedido útil. Por eso deben fijarse operación, carga, mezcla de solicitudes, tamaño de datos, errores y ventana de medición.

### Promedio y p95 cuentan historias diferentes

Supongamos 1.000 solicitudes: 950 tardan 100 ms y 50 tardan 2.000 ms. El promedio es:

$$
\bar{x}=\frac{950(100)+50(2000)}{1000}=195\ \text{ms}.
$$

Usando el percentil por **rango más próximo**, ordenamos las observaciones y definimos:

$$
p_{95}=x_{(\lceil0{,}95n\rceil)}.
$$

Aquí p95 = 100 ms y p99 = 2.000 ms. El promedio oculta cómo se distribuye la espera; p95 tampoco protege al 5 % restante. Diferentes herramientas interpolan percentiles de otra manera: hay que acordar el método. No se obtiene el p95 global promediando los p95 de servidores.

Un objetivo inventado sería «p95 ≤ 300 ms para confirmar compras con 100 solicitudes/s durante 20 minutos, y errores ≤ 0,1 %». Debe precisarse cómo se contabilizan tiempos de espera agotados: excluirlos puede hacer que una caída parezca una mejora.

### Colas, recursos y límites

Cuando las llegadas superan la capacidad de finalización, se acumula trabajo. Para un sistema estable, con fronteras consistentes y promedios de largo plazo, la ley de Little relaciona concurrencia media, throughput y tiempo medio dentro del sistema:

$$
L=\lambda W.
$$

Si se completan 80 pedidos/s y cada pedido permanece 0,25 s de media, hay 20 pedidos en curso de media. Esto incluye espera dentro de la frontera elegida; no implica 20 hilos ni permite sustituir el promedio por p95. Tampoco describe un régimen estable si la cola crece indefinidamente.

### Escalabilidad y elasticidad

Escalabilidad pregunta si más recursos permiten sostener más carga. Elasticidad pregunta cómo se ajustan recursos a las subidas **y bajadas**, con qué demora y desperdicio. Crecer verticalmente aumenta recursos de una instancia; horizontalmente añade instancias.

![Escalabilidad y elasticidad ](Recursos%20visuales/Diagramas/cap04-diagrama-02.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap04-diagrama-02.mmd)

**Interpretación:** la elasticidad implica un ciclo de ajuste, no únicamente crecimiento. **Límite:** el diagrama omite tiempos de arranque, cuotas, estados y cuellos de botella que pueden impedir una respuesta útil.

Si una instancia sostiene 50 solicitudes/s y cuatro sostienen 160 bajo el mismo objetivo, el factor de escalado es 160/50 = 3,2; la eficiencia respecto del escalado lineal es 3,2/4 = 80 %. No demuestra que ocho alcancen 320. Si las nuevas instancias tardan tres minutos en arrancar, pueden llegar después de un pico de dos minutos: existe escalabilidad, pero la elasticidad resulta insuficiente para ese escenario.

![escalabilidad elasticidad](Recursos%20visuales/06-escalabilidad-elasticidad.png)

*Figura original con datos hipotéticos independientes del ejemplo anterior: a la izquierda se compara capacidad con recursos; a la derecha, demanda y capacidad a lo largo del día.*

## 5. Disponibilidad, fiabilidad y recuperación

**Ampliación didáctica sobre conceptos presentes en PDF pp. 5 y 8; impresas 59 y 62.** Disponibilidad pregunta si el servicio está utilizable; fiabilidad, si cumple su función durante un intervalo bajo condiciones especificadas. Un servicio accesible que pierde pedidos no es fiable para esa función. Tolerancia a fallos permite seguir funcionando pese a ciertos fallos; recuperabilidad permite restablecer datos y operación después de una interrupción.

Para una medición temporal con disponibilidad binaria:

$$
A=\frac{T_{\text{observado}}-T_{\text{indisponible}}}{T_{\text{observado}}}.
$$

En 30 días de servicio continuo hay 43.200 minutos. Un objetivo de 99,9 % permite como máximo 43,2 minutos de indisponibilidad en esa ventana. Hay que acordar qué significa «disponible», qué horario cuenta y cómo tratar fallos parciales. Una proporción de solicitudes exitosas usa otro denominador y no equivale automáticamente al porcentaje temporal.

Una instancia alternativa puede aportar tolerancia al fallo de otra, pero no a un error compartido por ambas. Una copia de seguridad aporta recuperabilidad potencial; solo una restauración probada demuestra que permite recuperar el estado requerido.

### RTO y RPO: dos pérdidas diferentes

RTO es el **objetivo de tiempo de recuperación**: cuánto puede tardarse en restablecer el servicio definido. RPO es el **objetivo de punto de recuperación**: cuánta antigüedad máxima puede tener el estado recuperado respecto del incidente, expresada en tiempo. Son objetivos, no resultados garantizados por escribirlos.

![RTO y RPO: dos pérdidas diferentes ](Recursos%20visuales/Diagramas/cap04-diagrama-03.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap04-diagrama-03.mmd)

**Interpretación:** el tramo previo representa una ventana potencial de pérdida de datos de dos minutos; el posterior, ocho minutos de recuperación. **Límite:** no muestra fallos parciales ni recuperación de cada subsistema; hay que definir cuándo se considera restablecido el servicio.

Con RTO = 10 min y RPO = 2 min, este resultado cumple ambos, suponiendo que el estado recuperado sea consistente. El tiempo efectivo es 12:08 − 12:00 = 8 min; la antigüedad del punto recuperable, 12:00 − 11:58 = 2 min. A 30 pedidos confirmados/min, y suponiendo pérdida completa de las escrituras de esa ventana, podrían faltar 60 pedidos. **RPO no mide número de pedidos**: esa conversión depende de la tasa y de qué escrituras se pierdan realmente.

Una copia cada dos minutos no garantiza RPO de dos minutos: puede fallar, estar incompleta o resultar inutilizable. Además, recuperación técnica y reconciliación comercial difieren: restaurar la base no cancela cobros ya aceptados por un proveedor externo.

![recuperacion](Recursos%20visuales/07-recuperacion.png)

*Otro incidente hipotético: la ventana de datos en riesgo precede al fallo; la interrupción termina cuando el servicio vuelve a operar. Los objetivos se comparan con esos resultados.*

## 6. Lenguaje ubicuo, compromisos e iteración

El libro recomienda un **lenguaje ubicuo** compartido dentro de la organización. «Aprendizaje» podría significar facilidad de aprender a usar el producto o adaptación automática del sistema; una palabra compartida no garantiza una idea compartida. **Fuente: PDF pp. 7 y 10–11; impresas 61 y 64–65.**

En PedidoClaro, definir «confirmado» como «persistido y aceptado para preparación» cambia qué medimos respecto de definirlo como «recibido en memoria». Cada objetivo necesita nombre, operación, condiciones, umbral y evidencia. Así, negocio, desarrollo y operaciones pueden discutir la misma promesa.

Los autores proponen la arquitectura **menos mala (*least worst*)**: compromisos aceptables para el contexto. Las características cuestan diseño, implementación y mantenimiento; maximizarlas todas genera complejidad. Se mantienen mínimos necesarios y se decide dónde invertir soporte especial.

![6. Lenguaje ubicuo, compromisos e iteración ](Recursos%20visuales/Diagramas/cap04-diagrama-04.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap04-diagrama-04.mmd)

**Interpretación:** decidir arquitectura implica observar consecuencias y corregir hipótesis. **Límite:** iterar no vuelve gratuitas las migraciones; conviene reconocer decisiones difíciles de revertir.

Ejemplo propio: replicar pedidos de forma síncrona puede reducir pérdida de datos, pero añadir latencia y dificultar aceptar escrituras cuando falla una réplica. Hacerlo de forma asíncrona puede reducir la espera a cambio de una ventana de pérdida. La decisión depende de los objetivos, no del atractivo del mecanismo.

El libro usa seguridad y rendimiento para ilustrar interacciones. No toda mejora de seguridad empeora inevitablemente el rendimiento: el efecto debe medirse. También existen beneficios conjuntos; eliminar datos innecesarios de registros puede reducir exposición y almacenamiento. La iteración permite comprobar qué efectos aparecen realmente. **Fuente del enfoque: PDF pp. 10–11; impresas 64–65.**

## 7. Preguntas de comprobación

### 1. ¿Toda exigencia importante es una característica arquitectónica?

> [!success]- Solución
> No. Debe reunir los tres criterios del libro. Calcular correctamente un precio es importante, pero describe funcionalidad del dominio; un objetivo temporal que obliga a reorganizar el procesamiento puede constituir una característica arquitectónica.

### 2. ¿Un promedio de 195 ms garantiza p95 inferior a 300 ms?

> [!success]- Solución
> No: el promedio no determina la distribución. En el ejemplo concreto sí se calcula p95 = 100 ms por rango más próximo, pero ese resultado proviene de las observaciones, no del promedio.

### 3. ¿Cuatro instancias prueban elasticidad?

> [!success]- Solución
> No. Podrían permanecer siempre encendidas. Hay que observar el ajuste ante demanda cambiante, incluida la reducción y el tiempo necesario para disponer de capacidad útil.

### 4. ¿Una restauración en ocho minutos cumple RPO de dos minutos?

> [!success]- Solución
> No puede deducirse. Ocho minutos describe recuperación efectiva y se compara con RTO. Para RPO necesitamos la antigüedad del estado recuperado respecto del incidente.

### 5. ¿Autenticar al encargado permite que consulte cualquier sucursal?

> [!success]- Solución
> No. La identidad comprobada es entrada para decidir permisos. La autorización debe delimitar acciones y datos, y verificarse en el servidor.

### 6. ¿Por qué los autores excluyen adecuación funcional de su catálogo?

> [!success]- Solución
> Porque la consideran parte de las funciones y motivaciones del dominio. Discrepan de la clasificación presentada; no niegan la importancia de completitud, corrección y pertinencia funcional.

### 7. ¿Dos zonas y un proveedor de pagos garantizan una tienda segura y disponible?

> [!success]- Solución
> No. Hay que analizar dependencias comunes, persistencia, recuperación y permisos. Esas capacidades externas ayudan, pero la arquitectura debe utilizarlas de modo coherente con amenazas y fallos concretos.

## 8. Ejercicio aplicado: justificar una decisión

**Supuestos inventados:** PedidoClaro recibe 40 solicitudes/s normalmente y 140 durante quince minutos. Una instancia soporta 50 con p95 ≤ 300 ms; cuatro soportan 160. Arrancar capacidad adicional tarda tres minutos. Se exige RTO ≤ 10 min, RPO ≤ 2 min y disponibilidad temporal de 99,9 % sobre treinta días completos.

Propón una estructura inicial, identifica tres riesgos y explica cómo verificarías los objetivos. Calcula el margen de capacidad del pico y el presupuesto temporal de indisponibilidad. No presupongas que un estilo garantiza propiedades.

> [!success]- Solución orientativa
> Un monolito replicado, balanceador y persistencia con recuperación probada es una hipótesis inicial posible. Cuatro instancias dejan 160 − 140 = 20 solicitudes/s de margen: 12,5 % de la capacidad medida. No demuestra tolerancia al fallo de una instancia: falta medir la capacidad con tres.
>
> Tres riesgos son la demora de arranque, la dependencia compartida de datos y la pérdida o duplicación de pedidos durante recuperación. Un pico previsible permite preparar capacidad con antelación; uno inesperado requiere reserva u otra estrategia que se pruebe bajo carga.
>
> Verificaríamos latencias y errores con la mezcla realista de operaciones, retiraríamos una instancia durante la prueba y ensayaríamos restauración y reconciliación de pedidos. El presupuesto temporal es 43,2 minutos; cumplir RTO por incidente no garantiza cumplir disponibilidad mensual si los incidentes se repiten. La propuesta se acepta solo si la evidencia satisface los objetivos y su coste resulta justificable.
