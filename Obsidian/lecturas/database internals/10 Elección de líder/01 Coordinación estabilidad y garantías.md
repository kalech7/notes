---
title: "Coordinación, estabilidad y garantías de una elección"
created: 2026-09-30
libro: "Database Internals"
capitulo: 10
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Coordinación, estabilidad y garantías

[[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice del capítulo]]

## Qué trabajo hace el líder

Un **líder**, también llamado coordinador, es un proceso al que se asigna la responsabilidad de dirigir algún trabajo distribuido. El resto de los procesos puede tener el mismo código y capacidad para asumir ese papel. La distinción es un rol del protocolo, no necesariamente una máquina de mayor tamaño ni una autoridad permanente.

Imagina cinco réplicas que deben ordenar dos operaciones: crear una cuenta y actualizar su saldo. Si cada réplica habla con las otras para acordar cada paso, hay muchas conversaciones y muchas oportunidades de intercalar mensajes de manera diferente. Un coordinador puede recibir ambas operaciones, proponer un orden y distribuirlo. Esto reduce la coordinación entre pares, aunque el protocolo todavía necesita las confirmaciones que hagan confiable ese orden.

El libro enumera usos como mantener estado global, ordenar mensajes de un broadcast, iniciar el sistema y organizarlo después de una falla. **Broadcast** significa distribuir un mensaje a varios destinatarios; **orden total** significa que los participantes colocan los mensajes en el mismo orden relativo. Tener un proceso que asigna posiciones ayuda a construir ese orden, pero por sí solo no protege contra su caída, el envío incompleto o la existencia de otro líder.

## Por qué se prefiere un líder estable

Una elección tiene un costo: consultas, respuestas, anuncios y, a veces, transferencia de estado. Si el líder se mantiene durante muchas operaciones, ese costo se reparte entre ellas. Si se reemplaza a cada instante, el sistema puede consumir su tiempo coordinando sustituciones en lugar de ejecutar el trabajo útil.

Por ejemplo, supón —como modelo propio— que elegir y preparar un líder tarda 200 ms y que después coordina 10 000 operaciones. Hay una sola interrupción de 200 ms para ese tramo. Si una máquina inestable provoca otra elección cada segundo, el mismo costo ocupa repetidamente una fracción importante del tiempo. Esto no calcula el rendimiento de ningún sistema real: muestra por qué la frecuencia de elecciones importa tanto como la duración de cada elección.

La centralización también tiene un límite. Si todas las peticiones pasan por un solo proceso, sus recursos pueden convertirse en el **cuello de botella**, es decir, la etapa que impide aumentar el rendimiento aunque las otras tengan capacidad. El libro propone dividir los datos en conjuntos de réplicas independientes y elegir un líder para cada conjunto. Varios líderes de particiones distintas no son un split brain si coordinan recursos distintos y el protocolo mantiene clara esa separación.

## Seguridad, vivacidad y conocimiento del resultado

La **vivacidad** de una elección pide que el sistema termine eligiendo un líder bajo sus condiciones de funcionamiento. La **seguridad** ideal de la elección pide que no haya más de un líder efectivo para la misma función. **Split brain** es la situación en que dos grupos operan con líderes incompatibles sin conocer al otro. Se dice que la elección debe producir una decisión determinista para todos, pero los algoritmos de este capítulo no mantienen esa propiedad ideal frente a particiones.

Una regla de desempate como «gana el mayor identificador» da el mismo resultado **si todos usan el mismo conjunto de participantes disponibles**. No obliga a los procesos a compartir esa vista. Si A ve los nodos {1, 2, 3} y B ve {4, 5}, ambos pueden aplicar la regla correctamente y anunciar ganadores distintos.

Elegir también incluye comunicar. No sirve que 5 se considere líder si las réplicas continúan enviando peticiones a 6. El resultado debe llegar a los participantes, y el protocolo debe manejar anuncios retrasados, nuevas elecciones y cambios de estado. El capítulo explica la necesidad; no presenta una implementación completa para todas esas carreras.

```mermaid
flowchart LR
 A[Inicio o líder inaccesible] --> B[Sospecha de falla]
 B --> C[Elección según las reglas]
 C --> D[Anunciar el nuevo líder]
 D --> E[Coordinar el trabajo]
 E --> F[Seguir detectando fallas]
 F --> B
```

La flecha desde la detección a la elección representa una decisión tomada a partir de información local. El anuncio lleva el resultado a otros procesos; después, el líder coordina mientras el sistema sigue vigilando su accesibilidad. El ciclo explica por qué la elección depende de los detectores del capítulo 9: un timeout demasiado agresivo puede volver a iniciarlo cuando el líder solo está retrasado.

## Elección y bloqueo distribuido

Un **bloqueo distribuido** asigna acceso exclusivo a un recurso o a una sección crítica. En un bloqueo típico importa que el recurso no tenga dos propietarios efectivos y que otros puedan adquirirlo más adelante. Los demás procesos no siempre necesitan saber quién lo ocupa. En una elección, conocer al líder permite dirigirle trabajo y aceptar sus mensajes como parte del protocolo.

| Aspecto | Elección de líder | Bloqueo para sección crítica |
|---|---|---|
| Propósito | Mantener un coordinador conocido | Controlar quién accede al recurso |
| Duración deseada | Un líder estable puede durar mucho | Se busca liberación y avance de los que esperan |
| Notificación | Los participantes necesitan identificar al líder | La identidad del propietario puede ser irrelevante para otros |
| Preferencia | Puede favorecer a un nodo apropiado | Una preferencia persistente puede causar inanición |

**Inanición** significa que un proceso espera indefinidamente aunque otros sigan obteniendo el recurso. Favorecer siempre al mismo solicitante puede causar ese problema en un bloqueo. En liderazgo, mantener al coordinador sano es normalmente deseable. Ambos mecanismos requieren garantías explícitas: la semejanza conceptual no convierte un timeout o una identidad conocida en exclusión segura.

> [!question]- ¿Tener tres líderes siempre indica un error?
> No. Si cada uno coordina una partición diferente, la arquitectura puede requerirlos. El problema aparece cuando dos líderes pretenden ejercer autoridad incompatible sobre el mismo recurso o conjunto de réplicas.

**Referencia:** PDF 10–11 · impresas 205–206. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=10|Fuente del rol, garantías y comparación con bloqueos]].

---

← [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Anterior: capítulo 9]] · [[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/10 Elección de líder/02 Bully rangos y sucesores preparados|Siguiente]] →
