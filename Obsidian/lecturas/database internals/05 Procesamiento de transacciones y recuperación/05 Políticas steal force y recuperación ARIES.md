---
title: "Database Internals — Políticas steal, force y recuperación ARIES"
created: 2026-09-30
libro: "Database Internals"
capitulo: 5
tags:
  - lecturas/database-internals
  - arquitectura/recovery
---

# Políticas steal, force y recuperación ARIES

[[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|← Índice del capítulo 5]]

La caché y el commit pueden progresar a ritmos distintos. **Steal/no-steal** decide si una página puede llevar a disco cambios no confirmados. **Force/no-force** decide si el commit exige que todas las páginas modificadas hayan sido escritas. Son dos ejes independientes.

## Steal: ganar espacio puede llevar cambios incompletos a disco

Con **steal**, el motor puede escribir una página modificada por una transacción activa y reutilizar el frame. La ventaja es liberar RAM sin esperar su commit. El problema aparece si la transacción aborta o el proceso cae: el archivo de datos ya contiene un efecto que no debe conservarse. Se necesita **undo** para retirarlo.

Con **no-steal**, los efectos no confirmados no llegan a los archivos de datos. En el modelo básico, su pérdida tras el crash no requiere deshacer el disco; seguía conteniendo el estado previo. Pero el sistema debe retener o separar esos efectos mientras la transacción está activa. Si una misma página mezcla cambios de varias transacciones, la gestión puede ser más compleja que «escribirla cuando una confirma».

## Force: facilitar recuperación encarece el commit

Con **force**, las páginas modificadas por una transacción se hacen durables antes de completar su confirmación. Así no faltan sus cambios confirmados en los archivos de datos después del crash.

Con **no-force**, se puede confirmar con el WAL durable y dejar páginas dirty en RAM. Se reúnen escrituras y se evita que el commit espere todas las páginas; a cambio, un fallo puede perder la copia reciente de esas páginas. Se necesita **redo** para instalar los efectos que faltan.

El término `force` también aparece en el libro para forzar **el log**. El objeto importa: no-force de **páginas de datos** es compatible con forzar **el WAL** antes de confirmar.

| Política de páginas | ¿Puede haber efectos sin commit en disco? | ¿Pueden faltar efectos confirmados en disco? | Necesidad básica tras crash |
|---|---|---|---|
| No-steal + force | No | No | Ninguna de esas dos reparaciones de efectos |
| No-steal + no-force | No | Sí | Redo |
| Steal + force | Sí | No | Undo |
| Steal + no-force | Sí | Sí | Undo y redo |

La tabla es el modelo clásico de actualización y fallos usado para razonar el capítulo. «Ninguna» no significa que se puedan ignorar escrituras parciales, metadatos, atomicidad del commit o fallos del dispositivo. Significa que no quedan efectos completos no confirmados ni faltan efectos completos confirmados bajo las premisas de esa combinación.

> [!warning] Errata visible en el escaneo
> En PDF 14, impresa 92, la explicación de steal/force atribuye undo a transacciones confirmadas. La versión correcta es: **undo retira efectos de transacciones no confirmadas que pudieron persistirse; redo recupera efectos que deben instalarse**. Además, en ARIES redo repite la historia de confirmadas e incompletas antes del undo. La propia descripción de ARIES en PDF 15 confirma esa distinción.

## ARIES: reconstruir y después retirar lo incompleto

**ARIES**, *Algorithm for Recovery and Isolation Exploiting Semantics*, combina WAL, steal/no-force y tres fases. Su decisión característica es **repeating history**: repetir primero los cambios necesarios para reconstruir el estado registrado antes del fallo, aunque algunos pertenezcan a transacciones que no terminaron.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 05/05-aries.png|1100]]

El análisis reconstruye qué transacciones terminaron y qué páginas podrían necesitar trabajo. Redo reinstala la historia pendiente de confirmadas e incompletas. Undo elimina después los efectos de las incompletas. Los registros CLR representan el trabajo de compensación; permiten conservar el progreso si ocurre otro fallo mientras se recupera.

### 1. Análisis

Se examina el log y la información del checkpoint. Se reconstruye una **tabla de transacciones**, que identifica estados y trabajo pendiente, y una **dirty page table**, que resume páginas posiblemente atrasadas. Esta fase no vuelve a encontrar la RAM anterior: esa RAM se perdió. Reconstruye metadatos desde información durable.

Como precisión complementaria, ARIES conserva para cada página un `recLSN`: desde qué registro podría faltarle trabajo. El mínimo determina el inicio de redo. Un `pageLSN` identifica el último registro instalado en una página y permite omitir efectos ya presentes. [Artículo original, secciones 4.4 y 6.2](https://www.cs.cmu.edu/~15849g/readings/mohan92.pdf).

### 2. Redo

Se recorre la historia desde el punto necesario y se reinstalan los cambios ausentes. No se hace una suma ciega de todas las entradas. Se usa el estado de la página para determinar qué falta. El propósito es reconstruir el estado relevante para continuar con un undo correcto.

Si se filtrara de entrada toda transacción incompleta, se perderían relaciones entre cambios físicos que la recuperación espera reconstruir. La separación de fases evita que redo tenga que adivinar un estado «solo confirmado» diferente del que produjeron las operaciones registradas.

### 3. Undo

Las transacciones que no confirmaron son **perdedoras**, o *losers*. Sus efectos se recorren en sentido inverso y se compensan. Las confirmadas son *winners* y conservan sus resultados.

Un **CLR**, *compensation log record*, registra una compensación hecha durante rollback. No es un segundo commit del cambio original: evidencia que se retiró un efecto. Si vuelve a caer el proceso, la recuperación puede repetir la compensación ya registrada y continuar con lo que todavía queda por deshacer.

## Un caso completo con valores

El siguiente caso es propio y simplificado. X e Y son registros independientes, inicialmente `X = 10`, `Y = 20`. El último estado durable puede estar adelantado en una página y atrasado en otra.

| LSN | Registro | Situación antes del crash |
|---:|---|---|
| 10 | T1 inicia | T1 será confirmada |
| 20 | T1 cambia X: 10 → 15 | Solo está en RAM y WAL |
| 30 | T2 inicia | T2 no termina |
| 40 | T2 cambia Y: 20 → 7 | Esta página sí se escribe por steal |
| 50 | T1 commit | Log durable hasta aquí |
| — | Crash | Se pierde toda la RAM |

Los archivos quedan `X = 10`, `Y = 7`. No representan un estado aceptable: falta el cambio confirmado de T1 y sobra el cambio incompleto de T2.

**Análisis:** T1 es winner y T2 es loser. **Redo:** instala `X = 15`; si Y ya contiene el cambio de LSN 40, no lo aplica otra vez. El estado reconstruido contiene `X = 15`, `Y = 7`. **Undo:** revierte T2, deja `Y = 20` y registra su compensación. El estado final es `X = 15`, `Y = 20`.

Ese resultado exige tanto redo como undo. Tener únicamente redo conservaría el 7 indebido; tener únicamente undo perdería el 15 confirmado. El problema no está en una única página rota, sino en distinguir qué resultados deben sobrevivir.

## Otro crash durante undo

Imagina que undo ya compensó Y y emitió un CLR. Si el CLR y sus dependencias son durables pero la página compensada aún no fue escrita, el siguiente reinicio puede reinstalar la compensación. Si la página compensada ya fue escrita, el protocolo WAL obliga a que el CLR correspondiente la preceda en almacenamiento durable.

Si el fallo ocurre antes de hacer durable ese CLR, no se puede asumir que su trabajo quedó registrado. La recuperación debe partir de lo que sí sobrevivió. Esta misma pregunta —«¿qué evidencia durable queda si se corta aquí?»— sirve para evaluar el log, las páginas y el commit.

## Relación con los B-Trees de los capítulos anteriores

Un split toca varias páginas y publica nuevas rutas. Un crash puede ocurrir después de escribir la nueva hoja y antes de modificar el padre, o en el orden contrario. Conservar los invariantes del árbol durante ejecución y poder reconstruirlos tras el fallo son responsabilidades relacionadas, pero diferentes.

Los latches de la nota 09 protegen los pasos contra otros hilos; el WAL y recuperación protegen contra la pérdida del proceso. Un latch que nadie más puede adquirir no vuelve durable la nueva hoja. Un registro WAL durable no evita que otro hilo observe una estructura inconsistente mientras se ejecuta un split mal coordinado.

> [!question]- ¿Por qué ARIES hace redo de una transacción que después deshará?
> Porque primero reconstruye la historia registrada sobre la que las compensaciones tienen sentido. Después undo elimina sus efectos. Repetir historia no significa confirmar a las perdedoras.

> [!question]- ¿Puede una página contener un resultado que ya está en disco pero aún no está confirmado?
> Sí con steal. La presencia física no equivale a visibilidad lógica ni a commit; la recuperación debe poder retirarlo.

**Fuente:** PDF 13–15 · impresas 91–93. [[Obsidian/lecturas/database internals/Materiales/05 Procesamiento de transacciones y recuperación.pdf#page=13|Steal/force y las tres fases de ARIES]].

---

← [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/04 WAL checkpoints y registros de recuperación|Anterior]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/05 Procesamiento de transacciones y recuperación/06 Aislamiento anomalías y serialización|Siguiente →]]
