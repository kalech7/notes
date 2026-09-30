---
title: "DDIA — Conflictos: evitar, LWW, siblings y reglas del dominio"
created: 2026-09-29
capitulo: 6
tags:
  - lecturas/ddia
  - arquitectura/replicacion
cobertura: "Impresas 222–226 y 228–229"
---

# DDIA — Conflictos: evitar, LWW, siblings y reglas del dominio

[[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Índice de Replicación]]

El mayor problema de la replicación multilíder, tanto entre regiones como entre dispositivos con un sync engine, es que **dos líderes pueden aceptar escrituras concurrentes sobre el mismo dato**. Cada líder las considera correctas por separado; el conflicto solo aparece cuando se intercambian los cambios. Con un único líder no aparece ese conflicto entre historiales aceptados independientemente por varios líderes, porque todos los cambios pasan por un punto de ordenación. Eso no elimina las actualizaciones perdidas en la aplicación: dos clientes aún pueden leer el mismo valor y sobrescribirse si el control de concurrencia no protege la operación.

## Qué significa «concurrente»

En un tablero de proyectos compartido, el nombre de un proyecto es «Lanzamiento». Marta, en Lima, lo cambia a «Lanzamiento Q3». Diego, en Madrid, lo cambia a «Beta pública». Cada cambio se confirma en su líder regional. Al replicarse, el líder de Madrid recibe «cambia Lanzamiento por Lanzamiento Q3», pero el valor actual allí ya es «Beta pública». Es la situación de la figura 6-9 del libro (título de una wiki que pasa de A a B en un líder y de A a C en otro).

Dos escrituras son **concurrentes** cuando **ninguna conocía a la otra** al hacerse. No importa si ocurrieron en el mismo segundo: si Marta editó sin conexión el lunes y Diego el martes sin ver el cambio de Marta, siguen siendo concurrentes. Lo que cuenta es si una escritura se hizo en un estado donde la otra ya había tenido efecto. Cómo detecta eso una base de datos se explica en [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/13 Causalidad versiones y vectores|causalidad y vectores de versión]]; aquí se asume que el conflicto ya se detectó y hay que resolverlo.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-09.png|1000]]

Ambos líderes parten del título A. Uno acepta B y el otro acepta C, y cada usuario recibe confirmación antes de que los líderes intercambien cambios. Al replicar, cada líder descubre una modificación incompatible con la suya. La concurrencia significa que ninguna modificación se basó en la otra, aunque sus relojes indiquen horas diferentes.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=27|PDF 27 · impresa 223 · figura 6-9]].

## Primera estrategia: que no ocurra

**Evitar conflictos** significa garantizar que todas las escrituras de un registro pasen por el mismo líder. La base de datos sigue siendo multilíder, pero para ese registro se comporta como si tuviera un solo líder. Si un usuario solo puede editar sus propios datos, puedes asignarle una **región «hogar»** (por ejemplo, la más cercana) y enrutar siempre allí sus lecturas y escrituras.

La estrategia puede romperse si cambias el líder asignado sin una transferencia de autoridad segura: una región cae y rediriges el tráfico, o la usuaria se muda de Lima a Madrid. Durante un cambio inseguro, una escritura puede llegar al líder viejo y otra al nuevo, y vuelves a tener un conflicto. Con un traspaso que impida al líder antiguo aceptar nuevas escrituras puedes mantener la exclusividad. Tampoco funciona para un dispositivo que edita sin conexión.

Otra forma de evitar conflictos, del libro: si dos líderes generan identificadores con un contador autoincremental, uno puede asignar solo **impares** y el otro solo **pares**. Así nunca asignan el mismo ID a registros distintos.

## Last write wins: converger descartando

Si no puedes evitar el conflicto, lo más simple es **etiquetar cada escritura con una marca de tiempo y quedarte con la mayor**. Es *last write wins* (LWW, «gana la última escritura»). Si dos marcas empatan, se desempata comparando los valores (por ejemplo, orden alfabético) para que todas las réplicas elijan lo mismo.

El nombre engaña. Entre dos escrituras concurrentes **no existe una «última»**: el orden de sus marcas de tiempo es, en la práctica, aleatorio. Lo que LWW hace es **elegir una ganadora mediante un orden determinista pero arbitrario respecto a la causalidad y descartar en silencio las demás**, aunque cada líder ya hubiera confirmado la suya al usuario. Todas las réplicas acaban iguales (convergen), pero a costa de **perder datos**.

LWW no tiene problema si nunca hay dos escrituras sobre la misma clave: por ejemplo, si solo insertas eventos con un identificador único y nunca los actualizas. Si actualizas registros existentes, o dos líderes pueden insertar la misma clave, tienes que decidir si perder actualizaciones es aceptable.

Además, si la marca de tiempo sale del reloj real del servidor, LWW depende de que los relojes estén sincronizados. Un ejemplo numérico:

| Hora real | Nodo y reloj | Escritura | Marca asignada |
|---|---|---|---|
| 12:00:00 | X, adelantado 10 s | estado = «Beta» | 12:00:10 |
| 12:00:04 | Y, reloj correcto, **ya vio «Beta»** | estado = «Lanzamiento» | 12:00:04 |

La segunda escritura es claramente posterior (se hizo conociendo la primera), pero tiene marca menor y **LWW la descarta**. Un reloj lógico, que se estudia más adelante en el libro, corrige este efecto del desfase; no corrige el descarte de escrituras realmente concurrentes, que es la naturaleza de LWW.

## Segunda estrategia: guardar todos los valores (siblings)

Si descartar al azar no es aceptable, la base de datos puede **guardar todos los valores escritos concurrentemente**: en el ejemplo, «Lanzamiento Q3» y «Beta pública». Esos valores se llaman **siblings** (hermanos). La siguiente lectura devuelve todos, y tú los resuelves, automáticamente en código o preguntando al usuario, y escribes un valor nuevo con el contexto causal de los siblings que conocías, para sustituirlos sin borrar una actualización concurrente que todavía no recibiste. Es parecido a un conflicto de *merge* en Git, salvo que la replicación no se detiene esperando a un humano. CouchDB funciona así.

Tiene costes:

- **La API cambia.** El nombre del proyecto deja de ser un texto y pasa a ser un conjunto de textos, casi siempre con uno solo. Todo el código de la aplicación tiene que contemplar el caso con varios. Los siblings identifican versiones alternativas del registro: dos versiones pueden tener el mismo texto y seguir siendo versiones distintas.
- **Pedir al usuario que fusione cansa.** Hay que construir la interfaz de resolución, y el usuario puede no entender qué se le pregunta ni por qué. Muchas veces es mejor fusionar automáticamente.
- **Fusionar automáticamente sin cuidado sorprende.** El carrito de Amazon fusionaba siblings con la **unión** de conjuntos. Adaptando la figura 6-10: el carrito tiene {DVD, Libro}; el dispositivo 1 quita Libro y añade Jabón, quedando {DVD, Jabón}; el dispositivo 2 quita DVD, quedando {Libro}. La unión da {DVD, Libro, Jabón}: **los dos artículos borrados reaparecen**. La unión no distingue «nunca lo tuve» de «lo quité».
- **Resolver también puede crear conflictos.** Si dos nodos ven el conflicto y lo resuelven a la vez, uno puede escribir «Q3/Beta» y otro «Beta/Q3». Al fusionar esas dos resoluciones podrías obtener «Q3/Beta/Beta/Q3». Para evitarlo, la fusión debe ser **determinista**: todos deben resolver el mismo conjunto de versiones de la misma manera. Ordenar los siblings antes de concatenarlos elimina el desacuerdo B/C frente a C/B en ese ejemplo. Como complemento, ordenar textos no evita por sí solo duplicados si se vuelven a fusionar resultados ya fusionados: para tolerar repetición y agrupaciones distintas hacen falta reglas idempotentes, conmutativas y asociativas, o metadatos que identifiquen las aportaciones originales. La nota siguiente muestra estas propiedades con contadores y conjuntos.

![[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Recursos visuales/Capítulo 06/figura-6-10.png|1000]]

El dispositivo 1 elimina el libro y añade jabón; el dispositivo 2 elimina el DVD. Si el servidor fusiona únicamente mediante la unión de los conjuntos que recibe, conserva el DVD de una rama y el libro de la otra: reaparecen ambos artículos borrados. Registrar también las operaciones de eliminación permite conservar su intención y obtener únicamente {jabón} en este ejemplo.

Adaptación didáctica del esquema del libro: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=30|PDF 30 · impresa 226 · figura 6-10]].

## Algunos conflictos no se ven como conflictos

El choque de dos valores en el mismo campo es evidente. Otros son sutiles. En un sistema de reservas de salas, cada reserva es un **registro nuevo**, no la modificación de un campo, pero la regla es que no haya dos reservas solapadas de la misma sala. Si dos personas reservan la sala 3 de 10:00 a 11:00 en líderes distintos, cada una comprueba disponibilidad, ve la sala libre e inserta su registro. No hubo dos escrituras al mismo campo y sin embargo la regla del negocio se rompió. El libro no da una solución rápida aquí: la retoma en los capítulos 8 y 13.

Hay reglas que ninguna fusión automática puede respetar sin perder algo. Si una lista admite como máximo cinco elementos y dos usuarios añaden tres cada uno de forma concurrente, la única salida es descartar algunos. Lo mismo ocurre con que un saldo no sea negativo o que un nombre de usuario sea único: cada líder aprueba una escritura válida por separado, y juntas violan la regla.

## Decide campo a campo

Elaboración propia: la estrategia correcta la dicta el significado de cada dato, no la base de datos.

| Dato | ¿Perder una escritura concurrente importa? | Estrategia razonable |
|---|---|---|
| «Visto por última vez» | Se busca conservar la fecha máxima, no cada observación | Máximo de las fechas válidas; LWW solo si su orden coincide con ese significado |
| Foto de perfil | Poco | LWW, o región hogar |
| Etiquetas de un documento | Sí: se esperan todas | Fusión de conjunto que recuerde borrados (ver nota 10) |
| Texto colaborativo | Sí | CRDT u OT |
| Stock, saldo, nombre único, reserva de sala | Rompe una regla global | Coordinación y control de concurrencia para la decisión; en algunos dominios, derechos asignados de antemano |

> [!question]- Dos escrituras sobre el mismo campo se hicieron con tres horas de diferencia. ¿Pueden ser concurrentes?
> Sí. Si la segunda se hizo sin conocer la primera (por ejemplo, desde un dispositivo sin conexión), son concurrentes. La concurrencia depende del conocimiento, no de la hora.

> [!question]- ¿Qué pierde exactamente LWW y cuándo no importa?
> Pierde todas las escrituras concurrentes salvo una, aunque ya se hubieran confirmado al usuario. No importa si cada clave se escribe una sola vez (inserciones con ID único) o si el dato tolera perder actualizaciones.

> [!question]- ¿Por qué la unión de siblings resucita elementos borrados?
> Porque un conjunto solo recuerda lo que contiene. Si un sibling ya no tiene «Libro» y otro sí, la unión no puede saber si falta porque se borró o porque nunca se añadió, y lo conserva.

> [!question]- ¿Evitar conflictos con región hogar sirve para siempre?
> Sirve mientras exista una sola autoridad para el registro. Una caída regional o una mudanza obligan a transferirla: si el traspaso no impide escrituras en el líder viejo, dos líderes pueden aceptar cambios sobre el mismo registro.

## Referencias

PDF 26–30 y 32–33 · impresas 222–226 y 228–229 · figuras 6-9 y 6-10. Enlaces: [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=26|PDF 26 · impresa 222]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=27|PDF 27 · impresa 223 · figura 6-9]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=28|PDF 28 · impresa 224]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=29|PDF 29 · impresa 225]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=30|PDF 30 · impresa 226 · figura 6-10]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=32|PDF 32 · impresa 228]], [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/Materiales/06 Replicación.pdf#page=33|PDF 33 · impresa 229]]. El carrito es adaptación de la figura 6-10; el tablero, la tabla de relojes y la tabla por campo son propios.

---

**Anterior:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/08 Sync engines y software local-first|Sync engines y software local-first]] · **Índice:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/00 Índice|Replicación]] · **Siguiente:** [[Obsidian/lecturas/Designing Data-Intensive Applications 2a edición/06 Replicación/10 CRDT y transformación operacional|CRDT y transformación operacional]]
