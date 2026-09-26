---
title: "05 · Identificar y priorizar características · 2.ª edición"
created: 2026-09-25
tags:
  - lecturas/software-architecture
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Índice]]

# 05 · Identificar y priorizar características · 2.ª edición

> [!info] Alcance y procedencia
> Basado en el capítulo 5 de *Fundamentals of Software Architecture*, segunda edición, de Mark Richards y Neal Ford: **PDF 21.37, páginas 12–24; páginas impresas 67–79**. En esta guía, el archivo correspondiente es [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/03 Características e identificación.pdf|03 Características e identificación.pdf]]. «Libro» identifica sus planteamientos; «elaboración propia» desarrolla explicaciones y herramientas. **PedidoClaro es una tienda de sándwiches inventada para estudiar**, diferente de Silicon Sandwiches, la kata del libro. Sus cifras son supuestos pedagógicos, no datos de la fuente ni compromisos reales.

## 1. Identificar significa convertir necesidades en decisiones justificables

Una funcionalidad describe algo que el sistema permite hacer: registrar un pedido. Una característica describe una condición relevante para hacerlo: seguir aceptándolo durante un pico de demanda. Identificar características consiste en descubrir qué condiciones importan tanto que pueden orientar la estructura del sistema. No consiste en reunir palabras terminadas en «-idad».

**Libro — PDF p. 12, impresa 67:** hay al menos tres fuentes: preocupaciones del dominio, requisitos del proyecto y conocimiento implícito del dominio. Deben combinarse. Los requisitos pueden indicar cuántas personas usarán una aplicación; el conocimiento del negocio puede revelar que todas intentarán entrar a la misma hora.

En PedidoClaro, «no perder el almuerzo de las oficinas» expresa una preocupación comercial. Debemos preguntar cuándo se concentra la demanda y qué puede fallar. Aceptar pedidos durante un pico importa, pero recibir más de los que la cocina puede preparar empeora el problema.

![1. Identificar significa convertir necesidades en decisiones justificables ](Recursos%20visuales/Diagramas/cap05-diagrama-01.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap05-diagrama-01.mmd)

**Interpretación:** las tres fuentes convergen en situaciones concretas antes de justificar decisiones. **Límite:** el diagrama simplifica un proceso iterativo; probar una decisión puede revelar requisitos omitidos y obligar a volver atrás.

## 2. Traducir preocupaciones sin convertirlas en equivalencias

**Libro — PDF pp. 12–13, impresas 67–68:** negocio y arquitectura suelen emplear vocabularios diferentes. La tabla 5-1 propone estas correspondencias, traducidas aquí:

| Preocupación del negocio | Características relacionadas en el libro |
|---|---|
| Fusiones y adquisiciones | Interoperabilidad, escalabilidad, adaptabilidad, extensibilidad |
| Tiempo de salida al mercado | Agilidad, capacidad de prueba, capacidad de despliegue |
| Satisfacción del usuario | Rendimiento, disponibilidad, tolerancia a fallos, capacidad de prueba y despliegue, agilidad, seguridad |
| Ventaja competitiva | Agilidad, capacidad de prueba y despliegue, escalabilidad, disponibilidad, tolerancia a fallos |
| Tiempo y presupuesto | Simplicidad, viabilidad |

La tabla abre conversaciones; no prescribe paquetes obligatorios. Adquirir otra empresa puede exigir integrar pedidos inmediatamente o sustituir su sistema en dos años: situaciones distintas. Una interfaz confusa también puede explicar insatisfacción aunque el servidor responda rápidamente.

**Elaboración propia:** tres preguntas ayudan a traducir: «¿qué resultado quieren conseguir?», «¿qué lo impediría?» y «¿cómo reconoceremos que lo conseguimos?». Si PedidoClaro necesita publicar promociones sin esperar una semana, primero hay que averiguar dónde transcurre esa semana: desarrollo, pruebas, aprobación comercial o despliegue. Separar servicios no arreglará automáticamente una aprobación manual que tarda seis días.

### Características compuestas: una promesa depende de varias condiciones

**Libro — PDF pp. 13–14, impresas 68–69:** la agilidad es una característica compuesta. No tiene una única medida objetiva; reúne, entre otras cosas, modularidad, capacidad de prueba y capacidad de despliegue. Optimizar solo un componente deja intactos los demás obstáculos.

El ejemplo del libro es calcular a tiempo los precios de fondos al cierre de la jornada por exigencias regulatorias. La cadena causal completa importa:

- **Rendimiento:** cada cálculo y el procesamiento conjunto deben caber en la ventana disponible.
- **Disponibilidad:** el sistema debe estar accesible cuando empieza esa ventana; una máquina rapidísima apagada no procesa fondos.
- **Escalabilidad:** al incorporarse más fondos, el tiempo total no debe crecer hasta incumplir el cierre.
- **Fiabilidad:** el procesamiento necesita continuar sin fallar durante su ejecución.
- **Recuperabilidad:** si falla cuando lleva el 85 %, debe poder retomar el trabajo aprovechable.
- **Auditabilidad:** debe existir evidencia que permita examinar los resultados y su cálculo. La puntualidad carece de valor si los precios son incorrectos.

La fuente vincula la última preocupación con auditabilidad. **Precisión de esta guía:** auditar ayuda a detectar y explicar errores; no garantiza por sí solo que una fórmula sea correcta. También hacen falta reglas de cálculo correctas y comprobación de resultados.

**Ejemplo numérico propio:** una ejecución tarda 50 minutos y dispone de una hora. Un fallo al 85 % ocurre a los 42,5 minutos. Reiniciar desde cero, incluso con recuperación instantánea del servicio, termina a los 92,5 minutos. Si hay puntos de recuperación válidos y restaurar tarda 3 minutos, retomar exactamente el trabajo pendiente permitiría terminar en 53 minutos. Supone que el resultado parcial es consistente, que no hay tareas que repetir y que el fallo no reaparece. Si el volumen se duplica y el coste es lineal, también hará falta aumentar capacidad o reducir trabajo: los puntos de recuperación no resuelven la escalabilidad.

![Características compuestas: una promesa depende de varias condiciones ](Recursos%20visuales/Diagramas/cap05-diagrama-02.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap05-diagrama-02.mmd)

**Interpretación:** el objetivo comercial depende de varias condiciones conjuntas. **Límite:** las ramas no son independientes ni cuantifican probabilidades; falta considerar datos de entrada, dependencias externas y validación del cálculo.

## 3. Conocimiento implícito: cuestionar el promedio

**Libro — PDF p. 14, impresa 69:** una universidad tiene 1.000 estudiantes y diez horas de matrícula. El ejemplo contrapone repartirlos uniformemente y recibirlos durante los últimos diez minutos. El objetivo es mostrar cómo el conocimiento del dominio modifica el diseño aunque no aparezca escrito.

**Cálculo propio sobre esas cifras:** diez horas son 600 minutos. El promedio uniforme es 1.000/600 = **1,67 estudiantes por minuto**. Concentrarlos en diez minutos produce **100 por minuto**, sesenta veces más. Diseñar con el promedio ocultaría el pico.

Estudiantes por minuto no equivale a solicitudes por segundo ni a sesiones concurrentes. Si suponemos veinte solicitudes por estudiante, el segundo escenario produce unas 33,3 solicitudes por segundo en promedio durante el pico. La simultaneidad dependerá de la duración de las sesiones; las solicitudes pueden agruparse todavía más alrededor de una apertura de cupos. Estas cifras adicionales son supuestos, no mediciones.

La observación del libro sobre procrastinación sirve para plantear una hipótesis. En un proyecto real conviene comprobar horarios, campañas, historial y comportamiento. En PedidoClaro, el almuerzo sugiere picos, pero una promoción o pedidos programados pueden cambiar su forma. Conocimiento implícito no significa permiso para presentar intuiciones como datos.

## 4. Practicar con katas: problema, restricciones y discusión

**Libro — PDF pp. 15–16, impresas 70–71:** una kata arquitectónica es un ejercicio acotado para practicar decisiones sin esperar años entre proyectos. Ted Neward desarrolló este formato de práctica; los autores lo adaptaron. Sus secciones son **descripción**, **usuarios**, **requisitos** y **contexto adicional**.

Pequeños equipos trabajan durante un tiempo fijado, producen análisis de características y diagramas, presentan resultados y comparan propuestas; el formato descrito incluye una votación. Un arquitecto experimentado puede revisar compensaciones omitidas y alternativas. La limitación temporal hace que se evalúe el razonamiento, no una implementación completa.

**Propuesta propia:** dedicar quince minutos a preguntas, veinte a características, veinte a alternativas y diez a revisión. Registrar supuestos permite descubrir si las propuestas difieren porque imaginaron cargas o presupuestos distintos.

### Silicon Sandwiches: enunciado completo de la fuente

**Libro — PDF p. 16, impresa 71; paráfrasis del enunciado:** una cadena nacional de sándwiches quiere incorporar pedidos por internet al servicio telefónico existente. Espera miles de usuarios y, posiblemente, millones en el futuro.

Sus requisitos son:

1. Permitir realizar pedidos y elegir recogida o entrega cuando el local ofrezca reparto.
2. Dar a quienes recogen una hora y direcciones al local, integrándose con varios servicios externos de mapas que incluyan información del tráfico.
3. Despachar al repartidor con el pedido para la entrega al cliente.
4. Permitir acceso desde dispositivos móviles.
5. Ofrecer promociones y especiales diarios nacionales.
6. Ofrecer promociones y especiales diarios locales.
7. Aceptar pagos en línea, en el local o al entregar.

El contexto adicional aporta tres condiciones: los locales son franquicias con propietarios diferentes; la matriz planea expandirse al extranjero próximamente; y busca contratar personal de bajo coste para maximizar beneficios.

Este enunciado pertenece a **Silicon Sandwiches**; PedidoClaro no añade requisitos retroactivamente a la kata.

## 5. Derivar características: explícitas, implícitas y candidatas

**Libro — PDF pp. 17–21, impresas 72–76:** «explícita» no exige que el documento use el nombre técnico. Una previsión de usuarios puede expresar escalabilidad en lenguaje comercial. «Implícita» indica que la necesidad se deduce del dominio o de condiciones generales. Una inferencia sigue necesitando validación.

### Crecimiento, picos, rapidez y continuidad

Los miles de usuarios y la posibilidad de millones señalan **escalabilidad**. Para dimensionar, hace falta distinguir usuarios registrados, activos y concurrentes: un millón de cuentas no significa un millón de pedidos simultáneos.

Las horas de comida sugieren **elasticidad**, aunque el enunciado no la solicite literalmente. El libro la presenta como capacidad de afrontar ráfagas. Como elaboración operativa, podemos evaluar además cuánto tarda en ajustarse la capacidad y cómo se reduce después. Soportar crecimiento sostenido no demuestra que el sistema responda a un pico súbito.

El **rendimiento** requiere tiempos de respuesta aceptables, especialmente en móvil y durante esos picos. Debe definirse junto con la carga: «responde en un segundo» carece de contexto si solo se probó con una persona. La **disponibilidad**, implícita, permite acceder al servicio; la estabilidad de las interacciones evita conexiones interrumpidas y sesiones que obligan a empezar de nuevo.

![Crecimiento, picos, rapidez y continuidad ](Recursos%20visuales/Diagramas/cap05-diagrama-03.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap05-diagrama-03.mmd)

**Interpretación:** escala y elasticidad imponen condiciones distintas al rendimiento. **Límite:** no define una topología ni demuestra que aumentar servidores elimine un cuello de botella en base de datos o cocina.

### Recorrer todos los requisitos sin inflar la arquitectura

| Evidencia del enunciado | Derivación y límite razonable |
|---|---|
| Pedir y elegir recogida o reparto | Comportamiento funcional; el libro no deriva una característica especial por ese solo hecho. |
| Hora, direcciones y mapas con tráfico | Integraciones que pueden afectar fiabilidad. Preguntar si perder tráfico permite mostrar direcciones básicas, evitando una dependencia fatal. |
| Despachar al repartidor | Funcionalidad sin exigencia arquitectónica especial en el enunciado disponible. |
| Acceso móvil | Decisiones de experiencia y rendimiento. El libro considera una web optimizada por simplicidad y presupuesto, pero exige colaborar con UX y negocio: una función necesaria podría justificar aplicaciones nativas. |
| Promociones nacionales y locales | Variaciones de comportamiento que hacen candidata la personalización o *customizability*. |
| Tres modalidades de pago | El pago en línea exige seguridad; no demuestra por sí solo que haga falta una estructura extraordinaria. |
| Franquicias con propietarios distintos | Examinar viabilidad, costes, plazos y capacidades del personal. No presupone automáticamente aislamiento mediante servicios separados. |
| Expansión internacional | Internacionalización; puede abordarse mediante diseño sin una estructura especial, y afecta a UX. |
| Contratación de personal de bajo coste | El libro infiere importancia de usabilidad. La elaboración práctica es comprobar formación y facilidad de uso, sin asumir incapacidad individual. |

**Referencias:** PDF pp. 18–20, impresas 73–75. En PDF p. 21, impresa 76, el libro amplía su discusión de personalización con recetas, ofertas y direcciones locales; las recetas aparecen en el análisis, no como un requisito separado del enunciado original.

### Seguridad implícita no significa seguridad resuelta

El libro supone que un tercero podría procesar los pagos y que, en este escenario, prácticas adecuadas permitirían atender la seguridad sin una estructura especial. **Ese supuesto no garantiza la seguridad de la aplicación.** Como elaboración propia, siguen existiendo autenticación, autorización entre locales, protección de datos y validación del resultado de pago. Si esas necesidades requieren aislamiento estructural crítico, la seguridad asciende a característica conductora. Estar fuera del «top 3» nunca autoriza omitir controles básicos.

## 6. Personalización: ¿diseño o arquitectura?

**Libro — PDF p. 21, impresa 76:** un microkernel puede alojar comportamiento común en un núcleo y variaciones en extensiones. Otra arquitectura puede resolverlas con Template Method: una clase base define un flujo y las subclases redefinen pasos. La misma necesidad puede encontrar soluciones a diferente escala.

**Elaboración propia:** en PedidoClaro, cambiar únicamente un descuento por local puede necesitar datos configurables. Si cada franquicia aporta reglas ejecutables independientes, un modelo de extensiones gana atractivo. Ese beneficio implica definir contratos, compatibilidad y tratamiento de fallos. Template Method puede ser suficiente para unas pocas variantes mantenidas por el mismo equipo, aunque la herencia introduce acoplamiento y puede volver difíciles las combinaciones de reglas.

![6. Personalización: ¿diseño o arquitectura? ](Recursos%20visuales/Diagramas/cap05-diagrama-04.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap05-diagrama-04.mmd)

**Interpretación:** primero se comprende la variación y después se comparan mecanismos. **Límite:** no es un algoritmo de selección ni una lista exhaustiva; las opciones pueden combinarse.

La fuente pide analizar rendimiento, acoplamiento, otras características y coste. Exige colaborar con desarrollo, responsables técnicos, negocio, gestión y operaciones. Evitar la **torre de marfil** significa contrastar la propuesta con quienes implementarán y operarán sus consecuencias.

## 7. Priorizar: pocas conductoras y mínimos explícitos

**Libro — PDF pp. 22–24, impresas 77–79:** cada característica añade obligaciones y puede complicar la solución. Una prueba útil es preguntar cuál eliminaríamos primero. En Silicon Sandwiches podría dejarse la personalización al diseño; también podría reducirse la prioridad relativa del rendimiento frente a disponibilidad o escala. Eso no significa construir deliberadamente una aplicación lenta.

La hoja del libro tiene **siete espacios**, pero los autores aclaran que seis u ocho también servirían. Es una restricción práctica para conversar, no una ley científica ni un máximo universal. Las características implícitas se mantienen visibles; si necesitan atención estructural especial, pasan a la lista conductora. Una candidata desplazada se registra en **«Otras consideradas»**.

Finalmente se eligen **tres conductoras principales sin orden interno**. No se exige acordar un ranking completo: negociar cada posición consume tiempo y puede crear una precisión ficticia. El conjunto principal orienta las compensaciones sin borrar las demás condiciones.

El recuadro del Vasa, PDF p. 23, impresa 78, sirve aquí únicamente como **analogía de sobredimensionar y acumular objetivos incompatibles**. No utilizamos su narración como explicación histórica verificada del naufragio.

## 8. Hoja de trabajo completa: PedidoClaro

**Elaboración propia; todos los objetivos numéricos siguientes son inventados.** Esta hoja adapta el método, no reproduce la figura 5-3 literalmente.

| Campo | Acuerdo provisional |
|---|---|
| Sistema y alcance | PedidoClaro: catálogo, aceptación de pedidos y confirmación para una red de locales. |
| Equipo participante | Representante comercial, responsable de local, desarrollo, UX y operaciones. |
| Resultado buscado | Aceptar pedidos de almuerzo que los locales puedan atender. |
| Escenario de carga | 200 sesiones activas normalmente; 2.000 durante veinte minutos. El modelo de solicitudes se medirá por separado. |
| Restricción | Equipo de cuatro desarrolladores; preferencia por operación sencilla. |
| Evidencia pendiente | Historial horario, capacidad de cocina, presupuesto operativo y comportamiento de proveedores. |

### Lista corta y selección conjunta

| ¿Top 3? | Conductora candidata | Objetivo provisional y evidencia para revisarlo |
|---|---|---|
| Sí | Disponibilidad | 99,9 % de solicitudes válidas de creación aceptadas técnicamente durante horario comercial; acordar exclusiones y medir extremo a extremo. |
| Sí | Elasticidad | Soportar el paso de 200 a 2.000 sesiones en cinco minutos manteniendo los límites acordados de errores y latencia. |
| Sí | Simplicidad operativa | Desplegar y revertir mediante procedimientos que dos integrantes diferentes puedan ejecutar en una prueba de quince minutos. |
| No | Escalabilidad | Validar 4.000 sesiones con capacidad adicional y revisar coste, saturación y latencia. |
| No | Rendimiento | Percentil 95 de creación de pedido inferior a dos segundos con 2.000 sesiones y mezcla documentada de solicitudes. |
| No | Recuperabilidad | Recuperar aceptación de pedidos en diez minutos en un simulacro y reconciliar todos los pedidos ya confirmados. |
| No | Personalización | Probar si promociones locales necesitan estructura especial; si bastan configuración y diseño, retirar esta conductora. |

«No» significa fuera del conjunto principal, no descartada. Los objetivos siguen abiertos a negociación. Disponibilidad mide aquí solicitudes; no debe convertirse sin más en minutos de caída. Asimismo, sesiones no determinan por sí solas la carga: la prueba debe documentar acciones, pausas, volumen de datos y dependencias.

| Zona de la hoja | Contenido y acción |
|---|---|
| Implícitas como mínimo | Seguridad, integridad de pedidos y modularidad. Desarrollo define controles; operaciones y negocio revisan riesgos y resultados. |
| Otras consideradas | Internacionalización: pospuesta por ausencia de expansión confirmada. Extensibilidad por plugins: pospuesta hasta demostrar variaciones que la necesiten. |
| Compensación aceptada | Ante fallo de tráfico, ofrecer direcciones básicas; conservar capacidad de pedir. Confirmar el comportamiento con UX. |
| Alternativas a contrastar | Aplicación modular con configuración; microkernel si aparecen extensiones independientes justificadas. |
| Validación próxima | Prueba de carga, simulacro de dependencia caída y comparación del coste operativo. |
| Reapertura | Revisar ante expansión, incumplimiento medido o nuevas reglas por franquicia. Responsable: equipo técnico y representante comercial. |

La simplicidad puede favorecer capacidad preparada antes del almuerzo; la elasticidad exige comprobar si basta. La hoja permite discutir esa tensión.

## 9. Preguntas de comprobación

### 1. Negocio pide «máxima satisfacción». ¿Qué preguntas harías primero?

> [!success]- Solución razonada
> Pediría un problema observable, cuándo ocurre y qué resultado espera el cliente. Si abandona por tiempos de carga, relacionaría rendimiento con carga real; si recibe pedidos equivocados, investigaría integridad y proceso. No seleccionaría todas las características de la tabla automáticamente.

### 2. ¿Qué oculta dividir 1.000 matrículas entre diez horas?

> [!success]- Solución razonada
> Oculta la distribución temporal. Concentrarlas en diez minutos multiplica por sesenta la tasa media de llegadas. Después faltan solicitudes por matrícula, duración de sesión y sincronización de acciones para dimensionar.

### 3. El lote de fondos es rápido, pero falla al 85 %. ¿Qué falta verificar?

> [!success]- Solución razonada
> Recuperabilidad y consistencia de resultados parciales: dónde retoma, cuánto tarda y cómo evita omitir o duplicar trabajo. También fiabilidad, crecimiento del volumen y evidencia de corrección. Medir únicamente duración de ejecuciones exitosas es insuficiente.

### 4. ¿Cómo decidirías si mapas debe bloquear los pedidos?

> [!success]- Solución razonada
> Preguntaría qué pierde el usuario sin tráfico y si puede continuar con direcciones básicas. Probaría ese fallo y acordaría una degradación aceptable. Una integración auxiliar no debería convertirse accidentalmente en condición para todo el negocio.

### 5. ¿Qué evidencia justificaría microkernel frente a Template Method?

> [!success]- Solución razonada
> Variaciones ejecutables que requieran contratos y evolución independientes, junto con beneficios que compensen su coste. Para pocas variaciones internas, diseño o configuración pueden bastar. Compararía acoplamiento, pruebas, despliegue, rendimiento y mantenimiento con el equipo.

### 6. ¿Qué harías si seguridad no está entre las tres principales?

> [!success]- Solución razonada
> Documentaría sus mínimos y los comprobaría igualmente. Si los riesgos requieren aislamiento u otra decisión estructural crítica, reconsideraría la lista. Delegar pagos no garantiza autorización correcta ni protección de los datos propios.

### 7. Aparece una octava candidata. ¿Debe rechazarse?

> [!success]- Solución razonada
> No por su número. Examinaría su necesidad y qué desplaza, conservaría alternativas en «Otras consideradas» y negociaría el conjunto principal. Siete limita la conversación; no sustituye el juicio ni obliga a un ranking total.

## 10. Ejercicio aplicado: una promoción cambia la demanda

**Supuesto nuevo:** PedidoClaro anuncia una promoción y prevé 6.000 sesiones en dos minutos. El presupuesto operativo no crece y los locales tienen capacidad limitada.

Entrega una hoja revisada: tres preguntas para negocio; demanda digital frente a capacidad de cocina; dos alternativas y sus costes; tres conductoras; una candidata desplazada; y una prueba con criterio de aceptación. Explica la admisión de pedidos y la comunicación de esperas.

> [!success]- Orientación para resolverlo
> Pregunta cuántos pedidos puede preparar cada local, si se permiten franjas futuras y qué espera quien ve la promoción. Compara preparar capacidad informática y escalonar admisiones con un ajuste dinámico de recursos; ambos necesitan limitar compromisos según cocina. Un control de admisión puede proteger continuidad, pero añade espera y exige informar con claridad. Conserva o cambia el top 3 justificando el objetivo comercial. Prueba el pico y una cocina saturada: no basta una web rápida si confirma pedidos imposibles. Todo umbral adicional debe etiquetarse como supuesto pendiente de validación.

## Referencias y recurso visual

- **PDF pp. 12–14 / impresas 67–69:** fuentes de características, traducción, compuestas y matrícula.
- **PDF pp. 15–16 / impresas 70–71:** definición, trabajo y enunciado de la kata.
- **PDF pp. 17–21 / impresas 72–76:** derivación explícita e implícita; diseño frente a arquitectura.
- **PDF pp. 22–24 / impresas 77–79:** reducción, priorización y hoja de trabajo.

![requisitos decisiones](Recursos%20visuales/08-requisitos-decisiones.png)

*Figura original: cada decisión se conecta con una necesidad y una forma de buscar evidencia. Los números son supuestos didácticos.*

> [!note] Límites de lectura
> Se usó el OCR individual de las páginas asignadas, incluida la página 24 corregida. La figura 5-3 no conserva todos sus rótulos en el OCR; la hoja anterior se apoya en la explicación textual y añade campos propios. No reconstruye etiquetas ilegibles ni cubre capítulos o páginas ausentes.
