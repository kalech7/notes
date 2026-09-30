---
title: "Database Internals — Capítulo 11 · CAP PACELC y sus límites"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# CAP PACELC y sus límites

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

**CAP** plantea una imposibilidad concreta: cuando una partición de red impide comunicar ciertos participantes, no se puede garantizar simultáneamente linealizabilidad y una respuesta válida para toda solicitud dirigida a cada nodo que no ha fallado. La condición de partición debe entrar en el diseño porque la red puede interrumpirse incluso con todas las máquinas encendidas.

La **C** significa consistencia linealizable: las operaciones parecen ejecutarse una a una, respetando el orden real de las que no se solapan. La **A** significa disponibilidad en el sentido del modelo: cada solicitud a un nodo no fallado obtiene finalmente una respuesta conforme al servicio. La **P** se refiere a seguir considerando ejecuciones con comunicaciones interrumpidas. No es una tercera calidad que pueda reducirse mediante un selector.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 11/01 CAP y PACELC.png]]

Las dos ramas separan la partición de la operación normal. Cuando A y B no se comunican, responder desde la vista local mantiene acceso pero puede contradecir una escritura ya confirmada en el otro lado. Cuando sí se comunican, decidir cuánto esperar todavía cambia latencia y garantías de visibilidad.

## Un caso mínimo de la imposibilidad

Ejemplo propio: inicialmente A y B tienen `x=0`. La comunicación se corta. A acepta `write(x,1)` y confirma al cliente. Después otro cliente inicia `read(x)` en B. B no puede distinguir una ejecución sin escritura de otra en la que A ya confirmó 1.

- Si devuelve 0 en la segunda ejecución, viola la precedencia real exigida por linealizabilidad.
- Si espera información de A para resolver la duda, no puede prometer completar durante una partición que dure indefinidamente.
- Si rechaza la solicitud por falta de autoridad, conserva seguridad pero renuncia a la disponibilidad definida por CAP para esa operación.

Una respuesta de error no satisface automáticamente A: de otro modo un servidor que rechazara todas las solicitudes sería «disponible» y el resultado perdería su sentido.

## CP, AP y PACELC

Una política **CP** impide responder con resultados que violen el orden prometido. Un grupo con autoridad de mayoría puede seguir trabajando en el lado mayoritario y detener operaciones en el minoritario. **AP** permite resultados de vistas locales durante la separación y necesita resolver divergencias después. AP no significa resultados arbitrarios: el servicio conserva las garantías más débiles que haya prometido.

**PACELC**, extensión discutida por el libro, distingue dos situaciones: con partición, disponibilidad frente a consistencia; en condiciones normales, latencia frente a coordinación para consistencia. Esperar una respuesta intercontinental puede mejorar una garantía aunque ningún nodo esté fallando. Esto describe una decisión de diseño, no permite calcular la latencia de una base a partir de su etiqueta.

## Diferencias que evitan confusión

| Concepto | Qué significa aquí | Qué no basta para cumplirlo |
|---|---|---|
| C de CAP | Linealizabilidad de operaciones | Aplicar cada cambio sin partes intermedias |
| C de ACID | Preservar invariantes de datos | Que todas las réplicas tengan la última versión |
| Disponibilidad CAP | Respuesta eventual de cada nodo no fallado | Un porcentaje alto de uptime |
| Alta disponibilidad operativa | Servicio utilizable bajo objetivos concretos | Una respuesta sin cota de demora |
| Partición de red | Grupos no pueden comunicarse | Que un proceso se haya apagado |

> [!warning] Precisión de la fuente
> La caja de la impresa 218 describe C de CAP mediante «todo o nada» y estados consistentes. Esa formulación mezcla atomicidad e invariantes con visibilidad. En estas notas C se usa como **linealizabilidad**, que es la definición indicada antes por el propio capítulo. Además, la frase amplia de la impresa 217 sobre imposibilidad de disponibilidad en un sistema asíncrono se interpreta con la condición conjunta de CAP y sus fallas, no como imposibilidad de cualquier servicio disponible.

CAP no determina los efectos de una caída de nodo, de un reinicio ni de cada combinación de fallas. Tampoco etiqueta correctamente toda una base cuando distintas operaciones usan distintos protocolos. Permite identificar una obligación imposible bajo partición y pedir al diseño que declare cuál garantía conserva.

> [!question]- ¿La partición exige que alguna máquina esté caída?
> No. A y B pueden funcionar perfectamente y no intercambiar mensajes. La incertidumbre sobre lo que aceptó el otro lado basta para crear la tensión.

**Referencia:** PDF 20–22 · impresas 216–218. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=20|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/01 Replicar para tolerar fallas|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/03 Disponibilidad parcial harvest y yield|Siguiente]] →
