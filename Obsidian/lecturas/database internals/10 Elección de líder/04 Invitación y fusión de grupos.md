---
title: "Invitación y fusión de grupos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 10
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Invitación y fusión de grupos

[[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice del capítulo]]

## Cambiar la unidad de coordinación

El algoritmo de **invitación** permite varios líderes desde el inicio: cada uno dirige un grupo. No intenta que todos los procesos se comparen inmediatamente en una elección global. Primero crea grupos y después los fusiona. Su unidad de coordinación es el grupo existente.

Al comenzar, cada proceso es líder de un grupo que solo lo contiene a él. Un líder contacta procesos que no pertenecen a su grupo y les ofrece unirse. Si el proceso contactado también es líder, ambos pueden coordinar la fusión directamente. Si es un miembro ordinario, responde con la identidad de su líder para que el invitante contacte a ese coordinador. Esa redirección evita tratar separadamente a todos los miembros del otro grupo.

Por ejemplo, si 1 contacta a 4 y 4 pertenece al grupo de 3, 4 responde «mi líder es 3». Entonces 1 y 3 pueden negociar la unión de ambos grupos. Conocer un miembro funciona como punto de entrada, pero no lo convierte en la autoridad para cambiar el grupo entero.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 10/04-invitacion.png]]

Las tres cajas recrean la figura 10-4. Se parte de cuatro grupos individuales; las invitaciones 1→2 y 3→4 producen {1, 2} y {3, 4}. Después 1 y 3 acuerdan la unión, y 1 queda como líder de los cuatro. Las flechas representan fusiones sucesivas; la caja verde muestra el grupo unido. El recuadro inferior añade un ejemplo propio que explica el criterio para reducir las notificaciones al conservar al líder del grupo mayor.

## Quién conserva el liderazgo

A diferencia de Bully, lo esencial no es que gane el identificador máximo. Cualquiera de los dos líderes puede dirigir el grupo unido si el protocolo comunica una decisión coherente. El libro propone conservar al líder del grupo más grande para reducir los cambios de referencia.

Supón que A tiene siete miembros, incluido su líder, y B tiene dos. Si se conserva al líder A, los dos miembros de B actualizan su referencia al coordinador. Si se conserva al líder B, los siete de A actualizan esa referencia. **2 frente a 7 actualizaciones** representa cinco referencias menos que cambiar. No es el conteo completo de mensajes de la fusión: negociar, confirmar y propagar la nueva membresía puede requerir comunicación adicional.

En la figura del libro los dos grupos tienen el mismo tamaño. Conservar a 1 no prueba que el algoritmo siempre prefiera un ID menor; simplemente es la decisión del ejemplo. La optimización por tamaño no determina por sí sola cómo desempatar grupos iguales.

## Qué evita y qué no garantiza

Invitación evita comenzar desde cero cada vez que dos conjuntos ya organizados se descubren. En lugar de reelegir entre todos sus miembros, los dos coordinadores pueden negociar una unión y comunicar el cambio al grupo afectado. Esto aprovecha el estado que ya existía.

Pero el algoritmo admite que permanezcan grupos separados y, por tanto, líderes separados. Si una partición impide que sus coordinadores se contacten, no hay un canal para realizar la fusión. La existencia de varios líderes es parte del modelo, aunque se vuelve problemática si se usa ese modelo para conceder autoridad exclusiva sobre un recurso global.

También hay una diferencia entre «acordar la fusión» y «todos ya conocen la nueva membresía». Un miembro puede seguir enviando mensajes a su líder anterior mientras la notificación está en tránsito. El texto presenta la idea de la fusión, pero no detalla versiones de grupo, fusiones concurrentes ni recuperación cuando uno de los líderes falla a mitad de la unión. Por eso no debe tomarse el dibujo como una implementación lista para producción.

## Compararlo con preferencia por rango

| Pregunta | Bully | Invitación |
|---|---|---|
| ¿Cómo empieza? | Un proceso busca al mayor rango accesible | Cada proceso empieza como líder de su propio grupo |
| ¿Cómo converge? | Consultas y anuncio del ganador | Fusión de grupos existentes |
| ¿Quién gana? | El mayor rango observado | Uno de los líderes, con posible preferencia por el grupo mayor |
| ¿Puede haber varios líderes? | Ocurre como problema bajo partición | Se permite por definición, uno por grupo |
| ¿Ahorro principal? | No consulta a inferiores que no pueden ganar | No reorganiza todos los grupos desde cero |

> [!question]- Si el grupo de 3 tiene diez miembros y el de 1 tiene dos, ¿conviene conservar a 1 por haber invitado?
> El hecho de iniciar no obliga a ganar. Conservar a 3 reduce las referencias al líder que deben cambiar de diez a dos, bajo el modelo de actualización explicado. La decisión final necesita una regla coherente entre ambos líderes.

**Referencia:** PDF 15–16 · impresas 210–211 · figura 10-4. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=15|Fuente de invitación y optimización por tamaño]].

---

← [[Obsidian/lecturas/database internals/10 Elección de líder/03 Candidatos ordinarios y elecciones simultáneas|Anterior]] · [[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/10 Elección de líder/05 Elección en anillo y máximo acumulado|Siguiente]] →
