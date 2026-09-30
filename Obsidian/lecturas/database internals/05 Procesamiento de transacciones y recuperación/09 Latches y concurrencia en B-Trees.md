---
title: "Database Internals — Latches y concurrencia en B-Trees"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/concurrencia
  - arquitectura/b-trees
---

# Latches y concurrencia en B-Trees

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Capítulo 5]]

Un B-Tree guarda páginas con claves, offsets y punteros. Insertar puede desplazar entradas de un directorio; dividir una página crea otra, distribuye datos y modifica enlaces. Si un hilo leyera entre dos pasos físicos incompatibles, podría interpretar una mezcla que nunca fue una estructura válida.

Los **latches** protegen esa representación física mientras se accede a ella. La transacción puede seguir viva mucho más tiempo que un latch sobre una página. Esta vida corta permite que otras operaciones usen pronto la estructura sin tener que esperar al final de la transacción.

El capítulo explica latches, primitivas de lectores/escritor, acoplamiento al descender por el árbol y B-link trees. Los ejemplos con capacidades y claves concretas de esta nota son elaboración propia. La figura de crabbing adapta la figura 5-9; la de half-split desarrolla la explicación del texto.

## Qué estado intermedio hay que ocultar

Supongamos que una hoja `[20,40,60,75,90]` se divide. El motor tiene que crear una hoja nueva, copiar o mover algunas claves, establecer enlaces y actualizar el padre. Una lectura sin protección podría encontrar el nuevo contador de celdas con el directorio viejo, un puntero todavía incompleto o una clave momentáneamente duplicada o ausente.

El problema es físico incluso cuando las transacciones lógicas modifican cuentas diferentes. También aparece si un proceso de mantenimiento compacta páginas o modifica enlaces mientras una consulta las utiliza.

Un latch no decide si una transacción puede observar una versión no confirmada: esa visibilidad pertenece al protocolo transaccional. El latch asegura que el objeto que consulta tiene una representación física válida. Mantener ambos problemas separados evita atribuir al latch una garantía de aislamiento que no proporciona.

**Referencia:** PDF 25 · impresa 103. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=25|Latches y representación física]].

## Readers-writer: varias lecturas pueden compartir una página

Una primitiva **readers-writer**, o **RW**, permite dos modos:

- **Compartido, S:** varios lectores pueden mantenerlo simultáneamente.
- **Exclusivo, X:** un escritor necesita usar el objeto sin otros lectores ni escritores simultáneos.

| Modo retenido / modo solicitado | Compartido S | Exclusivo X |
|---|---|---|
| Compartido S | Compatible | Espera |
| Exclusivo X | Espera | Espera |

Dos lectores no se interfieren por leer el mismo contenido. Un escritor puede cambiar la representación a mitad de lectura, y dos escritores pueden pisarse modificaciones. Por eso solo S con S es compatible.

En la figura 5-8 del libro, tres lectores acceden mientras un escritor espera. En el otro caso, un escritor tiene acceso exclusivo y tanto los lectores como otro escritor esperan. La tabla anterior recrea en términos de compatibilidad las figuras 5-7 y 5-8, sin insinuar que “exclusivo” signifique que dos participantes exclusivos puedan entrar juntos.

Las lecturas compartidas siguen necesitando la gestión de la caché: por ejemplo, no cargar la misma página dos veces simultáneamente por una carrera entre solicitudes. Poder compartir la lectura de un contenido estable no elimina la coordinación necesaria para localizarlo y prepararlo.

Como ampliación, una política que admita lectores nuevos indefinidamente puede retrasar mucho a un escritor que espera. Compatibilidad y justicia de la cola son cuestiones distintas; la tabla describe acceso simultáneo, no el orden en que se atienden las solicitudes.

**Referencia:** PDF 25–26 · impresas 103–104 · figuras 5-7 y 5-8. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=26|Compatibilidad y acceso lectores/escritor]].

## Esperar dormido, girar en CPU o hacer cola

El capítulo distingue dos formas de esperar por acceso a una página:

| Estrategia | Qué hace el hilo | Coste principal |
|---|---|---|
| Bloqueo | Cede la CPU y el planificador lo despierta cuando puede continuar | Dormir, despertar y cambiar de contexto |
| Busy-wait o spin | Revisa repetidamente una condición sin ceder inmediatamente la CPU | Tiempo de CPU y tráfico sobre memoria compartida |

Esperar activamente puede compensar si la espera es extremadamente corta, porque evita el coste de dormir y despertar. Si el recurso tarda en liberarse, seguir girando desperdicia CPU. El capítulo describe esa compensación, sin fijar un umbral universal.

Las colas pueden gestionarse con **compare-and-swap**, o **CAS**: una instrucción que cambia un valor solo si aún coincide con el esperado. Esa comprobación y sustitución es atómica. Sirve para coordinar la incorporación de hilos a una cola y el traspaso de propiedad.

En el esquema de cola descrito, el hilo obtiene acceso inmediato si no hay nadie antes; si hay cola, espera sobre un estado asociado a su posición que actualiza su predecesor. Así se evita que todos los hilos compitan repetidamente sobre una única palabra compartida para adquirir el latch.

Como precisión propia, CAS vuelve atómica una transición concreta; no convierte automáticamente en atómico todo el split de una página. La estructura necesita un protocolo que haga coherentes sus pasos y su publicación.

**Referencia:** PDF 26 · impresa 104 · recuadro *Busy-Wait and Queueing Techniques*. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=26|Espera y técnicas de cola]].

## Latch crabbing: asegurar el siguiente nodo antes de soltar el anterior

Una estrategia sencilla toma todos los latches desde la raíz hasta la hoja y los retiene hasta terminar. Tiene una desventaja grande: casi todas las operaciones pasan por la raíz, así que retenerla durante toda la operación obliga a muchas consultas a esperar incluso cuando trabajan en hojas diferentes.

**Latch crabbing**, también llamado **latch coupling** o acoplamiento de latches, reduce la duración de esas reservas. El hilo adquiere el latch del hijo antes de soltar el del padre. Durante el traspaso puede conservar ambos, pero libera los ancestros cuando sabe que la operación ya no los necesitará.

Para una lectura, una vez localizado y protegido el hijo, puede soltar el padre en el protocolo presentado. No existe una ventana en la que el hilo abandone la protección del padre y todavía no haya asegurado el hijo al que pretende ir.

Para una modificación, además debe comprobar si el hijo es **seguro para la operación**. Seguro significa que la operación no causará un cambio estructural que necesite propagarse al ancestro que se pretende liberar.

| Operación | Criterio conceptual para soltar el padre |
|---|---|
| Lectura | Hijo localizado y protegido |
| Inserción | El hijo puede absorber la inserción o propagación pertinente sin dividirse hacia el padre |
| Borrado | El hijo conserva ocupación suficiente y no exige fusión o rebalanceo que afecte al padre |

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/09-latches-crabbing.png]]

Las tres tarjetas superiores muestran el traspaso: primero se protege la raíz, después se protege también el hijo y finalmente se libera la raíz si el hijo es seguro. Los nodos azules tienen latch retenido; los grises lo tienen libre. La comparación inferior explica la diferencia entre una hoja con espacio, cuyo padre ya puede liberarse, y una hoja llena, cuyo split puede requerir conservar el padre y quizá más ancestros.

### Ejemplo de inserción

Para simplificar, una hoja admite cuatro claves:

- Con `[10,20,30]`, insertar 25 deja `[10,20,25,30]`. La inserción cabe y no crea un separador nuevo para el padre. Una vez protegida la hoja, el padre puede liberarse.
- Con `[10,20,30,40]`, insertar 25 produce cinco claves. Puede dividir la hoja, crear una hoja hermana y añadir un separador al padre. Debe conservarse la protección necesaria para ese cambio o utilizar un protocolo alternativo que lo publique de forma segura.

En un nodo interno, tener espacio para absorber el separador que suba de un split del hijo permite cortar la propagación allí. Puede seguir habiendo cambios debajo, pero ya no necesitan modificar los ancestros liberados.

En páginas con registros variables, “no está lleno” debe interpretarse como **hay espacio suficiente para la operación real**, incluidos los metadatos pertinentes. Contar una posición libre no basta si el registro que se insertará ocupa más bytes de los disponibles. Esta precisión amplía el ejemplo del libro y lo conecta con [[Obsidian/lecturas/database internals/03 Formatos de archivo/04 Slotted pages e indirección|slotted pages]].

### Ejemplo de borrado

Supongamos un mínimo didáctico de dos claves por hoja. Si tiene tres y se elimina una, conserva dos y puede evitar una fusión. Si tiene dos y se elimina una, puede quedar con ocupación insuficiente y necesitar un préstamo o fusión que también afecte al padre.

La condición de seguridad cambia con la operación. Una hoja cerca del mínimo puede ser segura para insertar y peligrosa para borrar; una hoja llena puede ser segura para borrar y peligrosa para insertar.

**Referencia:** PDF 27–28 · impresas 105–106 · figura 5-9. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=27|Latch crabbing durante inserción y borrado]].

## Qué ocurre si la página hija no está en memoria

Esperar a que el disco cargue el hijo mientras se retiene un latch muy solicitado alarga la contención. El libro plantea proteger el estado relacionado con la carga o liberar el padre y reiniciar el descenso después de que el hijo se haya cargado.

Reiniciar tiene un coste, pero durante la espera el árbol puede cambiar. Por eso el camino anterior no se reutiliza como si siguiera siendo una autorización válida. El capítulo menciona mecanismos para detectar cambios estructurales desde el recorrido anterior.

Como separación conceptual propia, **mantener una página en caché** y **proteger sus modificaciones concurrentes** tampoco son lo mismo. Una protección contra expulsión evita que la página desaparezca del buffer que el hilo usa; un latch evita observar una actualización física incompatible. Un protocolo real necesita manejar las dos necesidades.

**Referencia:** PDF 27 · impresa 105. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=27|Carga de páginas y reinicio del descenso]].

## Upgrading: reservar acceso compartido y convertirlo en exclusivo

El **latch upgrading** comienza usando latches compartidos en parte del recorrido y pide acceso exclusivo cuando es necesario modificar. La operación toma exclusivo en la hoja; si necesita dividir o fusionar, intenta conseguir la exclusividad necesaria en los nodos afectados.

Eso reduce exclusividad en el caso frecuente de una modificación local. Pero si dos hilos conservan modos compartidos y ambos quieren convertirse a exclusivos, una espera ingenua puede generar dependencias peligrosas. La implementación debe elegir una política de conversión segura, esperar de manera compatible con ella o soltar y reiniciar. El capítulo indica que alguno de los hilos puede tener que esperar o reintentar.

La raíz suele cambiar menos que las hojas, aunque casi toda búsqueda pasa por ella. Esa asimetría explica la ventaja de acortar su protección o validar un acceso optimista, con la posibilidad de reintentar el recorrido cuando cambia.

> [!note] La raíz no necesita que todas las hojas estén llenas para dividirse
> La impresa 107 justifica la rareza de splits de raíz diciendo que primero deben llenarse todos sus hijos. Eso es una simplificación, no un invariante general: inserciones concentradas en parte del árbol pueden producir suficientes splits de hijos para llenar el padre mientras otras páginas conservan espacio. Lo necesario es que una propagación llegue a una raíz que ya no pueda absorberla. La observación útil es que los cambios estructurales tienden a propagarse menos a los niveles altos.

**Referencia:** PDF 29 · impresa 107 · recuadro *Latch Upgrading and Pointer Chasing*. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=29|Conversión de latches y contención en la raíz]].

## B-link trees: encontrar la nueva página aunque el padre todavía no la señale

Un **B-link tree** añade dos elementos para facilitar recorridos concurrentes:

- Una **high key**, límite superior del rango que corresponde al nodo.
- Un **enlace lateral** al nodo siguiente de su nivel.

La high key puede ser un límite de rango aunque no exista un registro con exactamente esa clave. El enlace lateral da una ruta de corrección cuando el puntero que viene del padre todavía conduce a la página anterior a un split.

El estado **half-split** tiene una página nueva accesible por el enlace lateral, mientras el padre aún no contiene el puntero directo a ella. No es permiso para que un lector vea bytes medio escritos: el contenido, el límite y el enlace tienen que publicarse de manera coherente con el protocolo de latches.

### Ejemplo completo: buscar 75 durante el half-split

Usaremos high keys **inclusivas**: la página izquierda cubre `(0,40]` y la derecha `(40,100]`. Esta convención determina que el salto lateral ocurra cuando la búsqueda es **mayor** que la high key.

Antes de completar la actualización del padre:

1. El padre todavía conduce las búsquedas del rango `(0,100]` a la página original.
2. La original ya conserva `[20,40]`, con high key 40.
3. Una nueva página conserva `[60,75,90]`, con high key 100.
4. La original publica un enlace lateral hacia la nueva.
5. El padre todavía no ofrece el puntero directo a la nueva página.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/10-blink-split.png]]

La flecha azul del padre lleva a la página izquierda mediante la ruta anterior. Allí, `75>40` demuestra que la búsqueda quedó fuera del rango actual. La flecha verde lateral permite llegar a la página derecha, donde 75 está presente y pertenece a `(40,100]`. El padre puede incorporar después el separador y el puntero directo sin que esa actualización tardía haga inaccesible la clave.

La búsqueda no concluye “75 no existe” por no encontrarlo en la página izquierda, porque su high key ya indicó que esa página no puede responder por 75. Para buscar 40, la condición `40>40` es falsa y la página izquierda es la que corresponde con nuestra convención.

El coste temporal es un salto adicional. El beneficio es poder hacer accesible el nodo nuevo sin retener el padre durante toda la división. Cuando el padre se actualiza, las nuevas búsquedas pueden llegar directamente a la página correcta.

Este mecanismo reduce contención y evita ciertos deadlocks que surgirían al combinar modificaciones que bajan y después suben para bloquear padres. No elimina las necesidades transaccionales: que una consulta llegue correctamente a una página física no decide si esa transacción puede leer su versión lógica o confirmar una escritura.

El libro presenta B-link como extensión de estructuras B-Tree con estas propiedades; aquí la explicación se centra en high keys y enlaces, que son la causa de la seguridad del recorrido. La variante concreta de rebalanceo no sustituye esos dos elementos.

**Referencia:** PDF 29–30 · impresas 107–108 · explicación en prosa, sin figura numerada propia. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=29|B-link trees y half-split]].

## Dos formas de proteger el descenso

| Estrategia | Cómo conserva una ruta válida | Coste o requisito |
|---|---|---|
| Crabbing | Protege al hijo antes de soltar al padre, conservando ancestros necesarios | Retiene más latches cuando se puede propagar un cambio |
| B-link | Usa high key y enlace lateral para corregir una ruta antigua | Publicación coherente de límites y enlaces, y algún salto adicional |

Ambas estrategias intentan reducir el tiempo de protección de las páginas más compartidas. La clave del razonamiento es identificar **qué información ya es segura para liberar** y **cómo se conserva una ruta a todos los datos** mientras cambia el árbol.

> [!question]- ¿Un latch de página impide por sí solo que dos transacciones hagan write skew?
> No. Puede impedir que se dañen físicamente las páginas, pero no protege la regla lógica conjunta cuando las dos transacciones toman decisiones con información antigua.

> [!question]- ¿Por qué crabbing adquiere el latch del hijo antes de soltar el del padre?
> Para que no haya una ventana sin protección durante el traspaso a la siguiente página de la ruta.

> [!question]- ¿Por qué una hoja llena requiere más cuidado al insertar?
> Porque puede dividirse, crear un separador nuevo y obligar a modificar el padre. No basta con proteger únicamente la hoja si el protocolo necesita modificar también ancestros.

> [!question]- En el ejemplo B-link, ¿por qué 40 no salta a la derecha y 75 sí?
> La high key 40 es inclusiva: la izquierda cubre claves hasta 40. Solo las mayores salen de su rango. Así, `40>40` es falso y `75>40` es verdadero.

> [!question]- ¿Half-split significa que la búsqueda observa un split a medio escribir?
> No. Significa que existe un estado físico publicado coherente con enlace lateral y límites correctos, aunque la actualización del padre aún esté pendiente.

---

← [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/08 Bloqueos transaccionales y deadlocks|Bloqueos y deadlocks]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/10 Laboratorio y repaso resuelto|Laboratorio y repaso resuelto]] →
