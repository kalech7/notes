---
title: "Candidatos, ordinarios y elecciones simultáneas"
created: 2026-09-30
libro: "Database Internals"
capitulo: 10
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Candidatos, ordinarios y elecciones simultáneas

[[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice del capítulo]]

## Reducir quién puede ganar

La optimización **candidate/ordinary** divide los procesos en dos grupos. Los **candidatos** pueden llegar a ser líderes; los **ordinarios** participan e incluso pueden iniciar la elección, pero no son elegibles. El objetivo es reducir las consultas necesarias para encontrar un coordinador.

Un ordinario que detecta la falla consulta a los candidatos, recibe respuestas, selecciona el de mayor rango que respondió y anuncia el resultado. Hay dos papeles distintos: quien **organiza esta elección** y quien **gana el liderazgo**. Confundirlos haría pensar que el iniciador debe asumir el rol o que un ordinario de rango alto puede imponerse.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 10/03-candidatos.png]]

La imagen recrea la figura 10-3: los candidatos son {1, 2, 6} y los ordinarios {3, 4, 5}. Al caer 6, el ordinario 4 consulta a 1 y 2; ambos responden y gana 2. La caja verde superior separa los que pueden iniciar de los que pueden ganar. Que 5 tenga un identificador superior a 2 no cambia el resultado, porque está fuera del conjunto elegible. El anuncio lo difunde 4, mientras 2 será el coordinador del trabajo posterior.

## Qué costo se reduce y cuál permanece

Si hay n procesos y k candidatos, un iniciador necesita consultar a aproximadamente k candidatos, en lugar de considerar a todo el conjunto como elegible. Sin embargo, todavía hay que difundir el resultado a los participantes. Reducir k no elimina el costo de informar a n procesos.

En el ejemplo, considerando 6 ya fuera del conjunto consultado, 4 envía dos consultas, recibe dos respuestas y anuncia a los cuatro procesos vivos distintos de él: 1, 2, 3 y 5. Son **8 envíos** bajo ese supuesto didáctico. Si también se intenta consultar al candidato 6, hay un envío fallido adicional y posiblemente una espera. La figura muestra la consulta a los candidatos restantes y no proporciona una fórmula universal de mensajes.

También cambia la disponibilidad potencial. Si todos los candidatos están caídos o aislados, puede haber muchos ordinarios sanos sin ningún proceso elegible accesible. El capítulo no desarrolla una política para reclasificar ordinarios o modificar la membresía; por tanto, esta optimización se entiende bajo el supuesto de que existe un candidato adecuado alcanzable.

## Por qué varios iniciadores generan carreras

Supón que 3 y 4 dejan de recibir mensajes de 6 casi al mismo tiempo. Ambos pueden consultar a los candidatos. Esto duplica tráfico y puede producir anuncios basados en respuestas diferentes: 3 recibió a tiempo la respuesta de 2, mientras 4 todavía solo conoce la de 1. Aunque ambos sean honestos, las demoras permiten decisiones locales distintas.

El libro propone un retardo de desempate **δ**, diferente para cada proceso. Los procesos de mayor prioridad esperan menos antes de iniciar. La idea es darle al iniciador preferido tiempo para comenzar y comunicar la elección antes de que los demás activen la suya. Los retardos se eligen separados y generalmente mayores que el tiempo de ida y vuelta de un mensaje, llamado **RTT**.

Como ejemplo propio, si el RTT típico es 20 ms, asignar δ₃=100 ms y δ₄=180 ms abre una ventana para que 3 actúe antes. Si una notificación válida llega a 4 durante esa ventana, puede evitar una ronda redundante. Pero si la red demora 300 ms, ambos pueden terminar iniciando. El ejemplo explica la intención; no afirma que esos valores basten para un protocolo completo ni ofrece una garantía bajo retardos arbitrarios.

Un retardo de desempate y un timeout de falla cumplen funciones distintas. El timeout decide cuándo sospechar del líder. δ decide cuánto posponer la propia iniciativa para dar preferencia a otro iniciador. Alargarlos indiscriminadamente puede reducir carreras, pero también retrasa el reemplazo real.

## Límite de la optimización

Reducir candidatos y escalonar iniciativas mejora el costo habitual. No demuestra unicidad global bajo particiones. Si un lado ve al candidato 1 y el otro al candidato 2, cada lado puede anunciar un líder. Un retraso fijo no lleva información entre redes desconectadas ni reemplaza las reglas de votación y aceptación necesarias para un consenso seguro.

> [!question]- ¿Un δ menor convierte automáticamente a un ordinario en líder?
> No. Le permite iniciar antes. La elegibilidad sigue limitada al conjunto candidato; el ganador se selecciona entre los candidatos que respondieron.

**Referencia:** PDF 14–15 · impresas 209–210 · figura 10-3. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=14|Fuente de candidate/ordinary y δ]].

---

← [[Obsidian/lecturas/database internals/10 Elección de líder/02 Bully rangos y sucesores preparados|Anterior]] · [[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/10 Elección de líder/04 Invitación y fusión de grupos|Siguiente]] →
