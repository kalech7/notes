---
title: "01 Introducción: arquitectura, contexto y responsabilidad · 2.ª edición"
created: 2026-09-25
tags:
  - lecturas/software-architecture
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Índice]]

# 01 · Introducción · 2.ª edición

## Alcance y forma de leer esta guía

Esta nota desarrolla la introducción de *Fundamentals of Software Architecture*, segunda edición, de Mark Richards y Neal Ford. Su fuente es el primer PDF, páginas **1–12**, correspondiente a las páginas impresas **1–12**, con una inversión: **PDF 10 = impresa 11; PDF 11 = impresa 10**. Las referencias siguientes respetan esa diferencia. El escaneo pasa después de la impresa 12 a la 17: esta nota no reconstruye las páginas 13–16 ni pretende cubrir el libro completo.

> [!info] Qué procede de dónde
> Las definiciones, leyes y ocho expectativas se explican a partir del libro. **PedidoClaro** es una tienda de sándwiches inventada para esta guía, distinta de la kata *Silicon Sandwiches* del libro. Sus cifras, decisiones y problemas son supuestos didácticos. Los diagramas son elaboración propia; el ejemplo de ADR también es una ampliación y no reproduce el capítulo sobre documentación de decisiones.

Fuente de consulta: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/01 Introducción y pensamiento arquitectónico.pdf|PDF: Introducción y pensamiento arquitectónico]].

## 1. Arquitectura: decidir cómo encajan las partes

Un programa puede calcular correctamente un precio y, aun así, fracasar como sistema: quizá se bloquea durante el almuerzo, pierde pedidos al reiniciarse o exige semanas de trabajo para cambiar una promoción. La arquitectura obliga a mirar conjuntamente el comportamiento, la organización del software y las condiciones bajo las cuales debe funcionar.

El libro presenta al arquitecto como alguien que analiza sistemas complejos y toma decisiones con compensaciones, a veces con información incompleta. También reconoce al «arquitecto accidental»: quien ya decide sobre arquitectura aunque su cargo no lo diga. La responsabilidad nace del alcance de las decisiones, no exclusivamente del título profesional. **Fuente: PDF 1, impresa 1.**

**Ejemplo inventado.** PedidoClaro vende sándwiches mediante una web y una caja presencial. Cobrar, registrar un pedido y enviarlo a cocina son comportamientos. Mantener esos comportamientos durante el pico del almuerzo, poder corregir una promoción y recuperarse de una interrupción son condiciones de éxito. Elegir una estructura sin entender ambas cosas puede producir software técnicamente elegante que el negocio no puede utilizar.

### El contexto económico cambia las respuestas

Los autores explican que, a finales del siglo XX, aprovechar infraestructura compartida tenía mucho sentido porque sistemas operativos, servidores de aplicaciones y bases de datos comerciales eran costosos. Su ejemplo de intentar desplegar numerosos servicios aislados en 2002 muestra que una estructura viable depende de licencias, infraestructura y prácticas operativas. Relacionan la viabilidad posterior de esas arquitecturas con el código abierto y la evolución de DevOps. **Fuente: PDF 1–2, impresas 1–2.**

Es una explicación histórica de incentivos: cuando cambia el costo de separar partes, cambia el equilibrio entre compartir y aislar.

**Cálculo ilustrativo propio:** si operar diez unidades separadas costara 200 unidades monetarias mensuales por unidad, la base sería 2.000; una plataforma compartida de 500 parecería atractiva. Si nuevas herramientas redujeran el costo por unidad a 20, la base separada sería 200. Pero todavía faltaría sumar coordinación, observabilidad y trabajo humano. Comparar únicamente infraestructura puede invertir artificialmente la conclusión.

![El contexto económico cambia las respuestas ](Recursos%20visuales/Diagramas/cap01-diagrama-01.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap01-diagrama-01.mmd)

**Interpretación:** las opciones técnicas dependen del entorno y los resultados permiten revisar lo decidido. **Límite:** el dibujo simplifica relaciones simultáneas; no afirma que el dinero sea la única causa ni que cada evaluación produzca una alternativa ganadora inequívoca.

> [!note] La afirmación sobre inteligencia artificial
> En PDF 1, los autores sostienen que evaluar compensaciones en contextos cambiantes hace especialmente difícil sustituir al arquitecto mediante IA. Debe leerse como su valoración, situada en el momento de escritura, **no como un hecho demostrado ni como una garantía sobre el futuro laboral**. El argumento útil aquí es la importancia del juicio contextual.

## 2. Cuatro dimensiones y una estructura que las conecta

![Las cuatro dimensiones de la arquitectura ilustradas mediante una tienda de sándwiches](Recursos%20visuales/10-cuatro-dimensiones.png)

**Cómo leer la imagen:** el reloj, el escudo y el indicador representan capacidades; pedidos, pagos y cocina representan responsabilidades. Las cajas agrupadas o separadas evocan organizaciones posibles y el registro de decisión conserva el porqué. La tienda central es el contexto del negocio. Es una analogía: un estilo no se reduce a contar contenedores, y los componentes de software no son necesariamente las máquinas físicas dibujadas.

La definición del libro reúne **características arquitectónicas, componentes lógicos, estilo arquitectónico y decisiones de arquitectura**. La estructura aparece como el soporte que conecta esas dimensiones; no basta con presentar cajas y flechas sin explicar qué sostienen. **Fuente: PDF 2–6, impresas 2–6, figuras 1-1 a 1-5.**

### Características: bajo qué condiciones tiene éxito el sistema

El libro menciona disponibilidad, confiabilidad, escalabilidad, seguridad, rendimiento, capacidad de prueba y otras capacidades. Estas expresan criterios de éxito del sistema. «Permitir comprar un sándwich» describe comportamiento; «seguir aceptando compras durante un pico de demanda» introduce una característica que influye en la construcción. **Fuente: PDF 3, impresa 3.**

**Ampliación didáctica:** para decidir conviene transformar adjetivos en escenarios observables. Supongamos que PedidoClaro necesita confirmar el 95 % de los pedidos en menos de dos segundos con veinte solicitudes por segundo. Ahora hay una carga, una operación y un umbral que se pueden comprobar. Decir solamente «rápido» permite que negocio y desarrollo crean estar de acuerdo mientras imaginan objetivos distintos.

**Aclaración propia:** rendimiento describe cómo responde con una carga determinada; escalabilidad plantea cómo cambia su capacidad al crecer la demanda y los recursos.

### Componentes lógicos: organizar el comportamiento

Los componentes lógicos estructuran dominios, entidades y flujos de trabajo. En PedidoClaro podríamos reconocer Catálogo, Pedidos, Cobros y Cocina. Cada nombre debe corresponder a responsabilidades comprensibles: Pedidos conserva el estado de la compra; Cocina organiza su preparación. **Base del libro: PDF 4, impresa 4. Ejemplo: elaboración propia.**

Un componente lógico no implica por sí mismo un servidor, un contenedor ni un despliegue independiente. Podemos separar esas responsabilidades dentro de un único programa. Confundir separación lógica con distribución física incorpora costos de comunicación y operación antes de demostrar que hacen falta.

### Estilo: un punto de partida estructural

Después de analizar características y componentes, el arquitecto dispone de información para escoger un estilo como punto de partida. El libro lo relaciona con encontrar un camino de implementación apropiado para los requisitos. No propone comenzar por el estilo de moda y adaptar después el problema a él. **Fuente: PDF 5, impresa 5.**

**Supuesto para PedidoClaro:** con un equipo pequeño y un volumen moderado, podríamos explorar una aplicación única organizada por módulos y capas. Eso es una hipótesis que debe contrastarse, no una recomendación universal extraída del capítulo. El estilo orienta relaciones y límites, pero no resuelve automáticamente todas las decisiones concretas.

### Decisiones: restricciones justificadas

Las decisiones arquitectónicas establecen reglas de construcción y delimitan lo permitido. El ejemplo del libro restringe el acceso a persistencia a las capas de negocio y servicios, impidiendo el acceso directo desde presentación. **Fuente: PDF 5–6, impresas 5–6; consecuencias en PDF 11, impresa 10.**

En PedidoClaro, permitir que la pantalla consulte tablas directamente puede reducir trabajo inicial, pero vincula la interfaz a su organización. Si la tabla de pedidos cambia, también puede ser necesario cambiar pantallas. Una decisión que imponga una interfaz intermedia busca controlar esa dependencia y acepta el costo de mantener dicha interfaz.

![Decisiones: restricciones justificadas ](Recursos%20visuales/Diagramas/cap01-diagrama-02.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap01-diagrama-02.mmd)

**Interpretación:** describir la arquitectura requiere conectar las cuatro dimensiones con una organización concreta. **Límite:** las flechas no significan independencia ni un proceso estrictamente lineal; una decisión puede obligar a reconsiderar el estilo o una característica.

![arquitectura contexto](Recursos%20visuales/01-arquitectura-contexto.png)

*Figura original de la guía: el contexto influye en características y componentes; las decisiones relacionan esos elementos con un estilo. Las flechas indican influencia, no un proceso rígidamente lineal.*

## 3. Tres leyes y dos corolarios para razonar

Los autores presentan estas leyes como generalizaciones de su experiencia: dos surgieron durante la primera edición y la tercera durante la segunda. Son herramientas de razonamiento profesional, no leyes físicas ni resultados matemáticos demostrados. **Fuente: PDF 6–8, impresas 6–8.**

### Primera ley: toda decisión arquitectónica implica compensaciones

Ganar algo suele exigir pagar algo en otra dimensión. Añadir una caché puede acelerar lecturas, pero obliga a decidir cuándo actualizar o invalidar datos. Separar componentes puede facilitar cambios independientes, pero requiere coordinar sus contratos. La pregunta útil es qué mejora, qué empeora, para quién y bajo qué condiciones.

**Ejemplo propio:** si una consulta tarda 80 ms y una caché tarda 5 ms, con un 90 % de aciertos y suponiendo que cada fallo cuesta 85 ms, el tiempo medio de ese acceso sería `0,90 × 5 + 0,10 × 85 = 13 ms`. Es una mejora frente a 80 ms, pero no describe el tiempo completo de compra ni los peores casos. Si el precio permanece desactualizado, ahorrar milisegundos puede crear reclamaciones. El cálculo no decide por sí solo si conviene almacenar precios en caché.

El **primer corolario** advierte que, si no vemos la compensación, probablemente todavía no la identificamos. No obliga a inventar daños imaginarios: obliga a buscar costos desplazados, como mantenimiento, aprendizaje y recuperación ante fallos.

El **segundo corolario** afirma que no basta con analizar compensaciones una sola vez. Un criterio adoptado para cinco tiendas puede ser inadecuado para quinientas. Un estándar puede reducir decisiones repetidas, pero sigue necesitando condiciones de aplicación. **Fuente de ambos: PDF 7, impresa 7.**

### Segunda ley: el porqué importa más que el cómo

Un diagrama puede mostrar que Pedidos se comunica con Cocina mediante una cola. No explica si se buscaba absorber picos, tolerar interrupciones o desacoplar equipos. Sin esa razón, alguien podría sustituirla por una llamada directa y eliminar justamente la propiedad que motivó su incorporación. **Fuente: PDF 7, impresa 7. Ejemplo: elaboración propia.**

Conservar el porqué significa registrar contexto, alternativas y costos aceptados. Una razón convincente tampoco convierte una implementación defectuosa en correcta.

### Tercera ley: la mayoría de las decisiones admite grados

Los autores señalan que muchas decisiones se sitúan en un espectro entre extremos. «Compartir o duplicar» no exige escoger igual para todo el sistema: podemos compartir un contrato estable y separar reglas que cambian por motivos diferentes. **Fuente: PDF 7, impresa 7. Ejemplo: ampliación propia.**

PedidoClaro podría centralizar la confirmación del pago y permitir que cada local organice su cola de preparación. Esto no demuestra que el punto intermedio siempre sea mejor. Una solución intermedia también puede reunir costos de ambos extremos; necesita justificación.

![Tercera ley: la mayoría de las decisiones admite grados ](Recursos%20visuales/Diagramas/cap01-diagrama-03.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap01-diagrama-03.mmd)

**Interpretación:** hay posiciones posibles entre extremos, y podemos elegir por responsabilidad. **Límite:** no es una escala cuantificada ni demuestra que el centro sea óptimo; algunas restricciones sí producen decisiones binarias.

## 4. Ocho expectativas del arquitecto

El libro enumera ocho expectativas, independientemente del cargo o nivel de responsabilidad. Conviene estudiarlas como actividades conectadas: decidir sin comunicar, verificar o comprender el negocio deja incompleta la función. **Lista original: PDF 8, impresa 8.**

### 1. Tomar decisiones que guíen

El arquitecto define decisiones y principios para orientar elecciones tecnológicas. El énfasis del libro está en **guiar**: establece criterios que permiten al equipo elegir. También reconoce situaciones en las que seleccionar una tecnología concreta es necesario para preservar rendimiento, disponibilidad u otra característica. **Fuente: PDF 8–9, impresas 8–9.**

En PedidoClaro, «los clientes de la interfaz no accederán directamente a la base de datos» comunica una restricción arquitectónica. Elegir una biblioteca visual normalmente requiere otro nivel de detalle. La frontera depende del contexto: una biblioteca puede adquirir importancia arquitectónica si determina una capacidad crítica. El error es clasificar por el nombre de la tecnología en lugar de por su efecto.

### 2. Analizar continuamente la arquitectura

La vitalidad arquitectónica consiste en revisar si la solución sigue siendo viable ante cambios técnicos y del negocio. El libro advierte sobre la degradación estructural cuando modificaciones locales deterioran características necesarias. Incluye pruebas y liberaciones dentro de esa evaluación. **Fuente: PDF 9, impresa 9.**

Si PedidoClaro programa una promoción en dos horas, pero necesita diez días para validarla y desplegarla, la rapidez de programación no representa la agilidad del sistema completo. Medir solo el tramo más cómodo esconde el cuello de botella que impide responder al negocio.

### 3. Mantenerse al día

Conocer tendencias ayuda porque las decisiones arquitectónicas suelen durar y resultar costosas de cambiar. El libro menciona almacenamiento y despliegue en la nube e IA generativa como ejemplos de cambios relevantes en su contexto. **Fuente: PDF 9, impresa 9.**

Estar informado no significa adoptar cada novedad. Como práctica propia para PedidoClaro, una evaluación breve puede preguntar qué problema resuelve una herramienta, cuánto cuesta introducirla y qué evidencia justificaría cambiar. Aprender aumenta las opciones; adoptar añade obligaciones.

### 4. Verificar el cumplimiento de decisiones

Aquí **compliance** significa comprobar que los equipos siguen las decisiones y principios documentados y comunicados. No equivale automáticamente a cumplimiento legal o regulatorio. El ejemplo del libro muestra cómo el acceso directo desde presentación puede frustrar el aislamiento de cambios de base de datos. También anticipa verificaciones automatizadas mediante funciones de aptitud arquitectónica. **Fuente: PDF 11, impresa 10.**

**Ampliación propia:** una comprobación de dependencias podría detectar importaciones del acceso a datos desde la interfaz. Esa prueba observaría una regla específica, no certificaría toda la arquitectura. Si la regla empieza a causar problemas reales, corresponde revisar su justificación, además de detectar incumplimientos.

### 5. Comprender tecnologías diversas

El libro favorece amplitud técnica: conocer opciones y sus ventajas e inconvenientes, sin exigir ser especialista en todas. La diversidad de entornos también obliga a entender cómo integrar sistemas construidos con tecnologías distintas. **Fuente: PDF 11, impresa 10.**

Conocer una sola herramienta de mensajería puede llevar a proponerla para cualquier comunicación. Reconocer varias alternativas permite preguntar si PedidoClaro necesita procesamiento inmediato, entrega posterior, confirmaciones o recuperación. La amplitud resulta útil cuando mejora esas preguntas; memorizar nombres comerciales no basta.

### 6. Conocer el dominio del negocio

Comprender problemas, objetivos y requisitos permite diseñar soluciones pertinentes y comunicarse con quienes operan el negocio. **Fuente: PDF 10, impresa 11.**

En nuestro ejemplo, «pedido recibido», «pagado» y «listo para preparar» podrían ser estados diferentes. Si se confunden, cocina puede preparar compras cuyo cobro falló. Conocer esas distinciones es tan necesario como dominar la base de datos: determinan qué transiciones y garantías necesita el sistema.

### 7. Liderar y desarrollar habilidades interpersonales

Trabajo en equipo, facilitación, liderazgo y comunicación forman parte del papel del arquitecto. El libro subraya que una orientación técnica valiosa necesita acompañamiento para convertirse en implementación. **Fuente: PDF 10, impresa 11.**

En PedidoClaro, facilitar una conversación entre caja, cocina y desarrollo permite descubrir significados contradictorios de «confirmado». Liderar no consiste únicamente en comunicar la respuesta final; también implica hacer visibles desacuerdos y ayudar a construir criterios compartidos.

### 8. Comprender y navegar la política organizativa

Las decisiones amplias redistribuyen costos y autonomía. El libro ilustra el problema restringiendo el acceso a una base de datos de CRM: mejora el control para su propietario, pero obliga a otros equipos a cambiar integraciones y asumir esfuerzo. Eso exige negociación. **Fuente: PDF 12, impresa 12.**

En PedidoClaro, limitar consultas directas puede beneficiar al equipo de Pedidos y complicar los informes de Finanzas. La objeción no demuestra ignorancia técnica: quizá identifica un costo real. Negociar una interfaz de consulta y una transición financiada hace viable la decisión. La política trata también de prioridades, recursos y responsabilidad, no solo de conflictos personales.

## 5. Principios, decisiones y un ADR breve

El libro menciona principios de diseño junto con decisiones que orientan a los equipos; describe las decisiones como reglas y remite su documentación al capítulo 21. Estas páginas no desarrollan un formato de ADR. **Fuente: PDF 5–8, impresas 5–8.**

**Distinción operativa de esta guía:** un principio expresa una orientación general, como «reducir el impacto de los cambios de datos en las interfaces». Una decisión concreta esa orientación bajo un contexto, como «la interfaz consumirá operaciones de Pedidos y no consultará sus tablas». El principio ayuda a interpretar casos nuevos; la decisión establece una restricción verificable. Una preferencia personal no se convierte en ninguna de las dos simplemente porque la anuncie el arquitecto.

> [!example] ADR-001 · Acceso a datos de pedidos — ejemplo inventado
> **Estado:** aceptado para el escenario didáctico.
> **Contexto:** web y caja comparten reglas de pedidos; esperamos cambiar su almacenamiento.
> **Decisión:** ambas interfaces accederán mediante operaciones del módulo Pedidos; quedan prohibidas sus consultas directas a tablas.
> **Alternativas:** acceso directo desde cada interfaz; módulo intermedio compartido.
> **Razón:** concentrar reglas y limitar el impacto de cambios del esquema.
> **Consecuencias:** mantener un contrato explícito y asumir trabajo adicional; centralizarlo también puede concentrar dependencias.
> **Verificación:** revisar dependencias y medir el tiempo de confirmación.
> **Revisión:** reconsiderar si el contrato impide un requisito demostrado o cambia el contexto.

ADR significa *Architecture Decision Record*, registro de decisión arquitectónica. El ejemplo desarrolla la segunda ley: conservar la razón permite revisar la decisión sin adivinar qué intentaba proteger.

![5. Principios, decisiones y un ADR breve ](Recursos%20visuales/Diagramas/cap01-diagrama-04.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap01-diagrama-04.mmd)

**Interpretación:** una orientación adquiere consecuencias mediante decisiones, implementación y evidencia. **Límite:** no prescribe una metodología del libro ni supone que toda decisión requiera aprobación centralizada; es una síntesis didáctica propia.

## 6. Preguntas de comprensión

### 1. ¿Por qué un diagrama de servicios no describe toda la arquitectura?

> [!success]- Solución
> Puede mostrar estructura, pero omitir condiciones de éxito, responsabilidades precisas y razones de las restricciones. Sin ellas no sabemos si esa organización responde al problema ni qué se perdería al cambiarla.

### 2. ¿Tener cuatro componentes lógicos exige cuatro despliegues?

> [!success]- Solución
> No. La separación de responsabilidades puede existir dentro de un único despliegue. Distribuir añade decisiones sobre comunicación y operación que necesitan una justificación propia.

### 3. ¿Qué falta si la caché reduce el tiempo medio de 80 a 13 ms?

> [!success]- Solución
> Evaluar vigencia de datos, fallos, mantenimiento y la operación completa. El promedio calculado solo corresponde al acceso modelado y depende del porcentaje de aciertos supuesto; no garantiza el tiempo de confirmación de pedidos.

### 4. ¿Un estándar elimina futuros análisis de compensaciones?

> [!success]- Solución
> No. Reduce trabajo repetido cuando siguen siendo válidos sus supuestos. El segundo corolario exige reevaluar el equilibrio al cambiar el contexto; aplicar el estándar requiere reconocer su ámbito de validez.

### 5. ¿Por qué incumplir una regla puede afectar una característica?

> [!success]- Solución
> La regla puede proteger una dependencia o frontera necesaria. Si la interfaz consulta tablas directamente, un cambio de esquema puede propagarse hasta ella. Detectar el incumplimiento exige conocer también la razón de la regla.

### 6. ¿Qué distingue liderazgo de imponer una decisión?

> [!success]- Solución
> Liderar incluye explicar razones, escuchar costos y facilitar la implementación. La autoridad puede imponer una restricción, pero no sustituye acuerdos, capacidades ni recursos para cumplirla.

### 7. ¿La tercera ley recomienda elegir siempre un término medio?

> [!success]- Solución
> No. Recomienda reconocer opciones graduadas. Los extremos pueden ser apropiados; una mezcla puede añadir complejidad. Hay que evaluar cada posición según objetivos y restricciones.

## 7. Ejercicio aplicado: el almuerzo de PedidoClaro

**Supuestos inventados:** el equipo tiene cuatro desarrolladores; caja y web comparten pedidos; el objetivo es confirmar el 95 % en menos de dos segundos a veinte solicitudes por segundo. Cocina solicita que ningún pedido pagado desaparezca de su lista. Finanzas consulta tablas directamente y teme perder sus informes.

Redacta una propuesta de una página: identifica las cuatro dimensiones, formula una decisión y su principio, explica dos compensaciones, plantea una verificación y propone cómo negociar con Finanzas. No es necesario escoger productos concretos. Señala cualquier dato adicional que necesites antes de comprometer una garantía.

> [!success]- Orientación de solución
> **Características:** rendimiento bajo la carga indicada y conservación de pedidos pagados, cuyo alcance debe aclararse ante fallos. **Componentes:** Pedidos, Cobros, Cocina e Informes. **Estilo candidato:** una aplicación organizada por módulos, pendiente de validación. **Decisión:** interfaces e informes usarán contratos definidos, sin consultas directas a tablas operativas. **Principio:** limitar la propagación de cambios internos.
>
> Las compensaciones incluyen el trabajo de construir contratos y la posible concentración de dependencias. Verificaríamos el objetivo temporal con carga representativa y comprobaríamos recuperación de pedidos ante interrupciones definidas. Negociaríamos con Finanzas un contrato de informes y una transición con responsables. Faltan datos sobre fallos tolerados, duración del pico y significado exacto de «confirmado». Ninguna cifra de carga permite deducir por sí sola cuántos servidores hacen falta.

## Referencias y límites de la fuente

- **PDF 1–2 / impresas 1–2:** contexto histórico, rol y definición inicial.
- **PDF 2–6 / impresas 2–6:** cuatro dimensiones y figuras estructurales.
- **PDF 6–8 / impresas 6–8:** tres leyes y dos corolarios.
- **PDF 8–9 / impresas 8–9:** lista de expectativas, decisiones, revisión y tendencias.
- **PDF 11 / impresa 10:** cumplimiento y diversidad tecnológica.
- **PDF 10 / impresa 11:** dominio del negocio y habilidades interpersonales.
- **PDF 12 / impresa 12:** política organizativa y negociación.

El OCR tiene fragmentos deteriorados, especialmente en figuras y al inicio de algunos párrafos. Se han explicado únicamente los conceptos reconocibles, sin reconstruir detalles ilegibles. Las referencias a capítulos posteriores hechas por los autores no implican que su contenido esté cubierto aquí.
