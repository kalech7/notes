---
title: "Elección de líder: laboratorio y repaso resuelto"
created: 2026-09-30
libro: "Database Internals"
capitulo: 10
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Laboratorio y repaso resuelto

[[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice del capítulo]]

Los ejercicios siguientes son elaboración propia a partir de los mecanismos del capítulo. Separan identidad, elegibilidad, accesibilidad y autorización. Las cuentas de mensajes asumen un mensaje por destinatario, un iniciador, ausencia de retransmisiones y una vista estable durante la ejecución, salvo cuando el enunciado indique lo contrario.

## 1. Bully modificado

Hay procesos {1, 2, 3, 4, 5, 6}. El líder 6 cae y 3 inicia. Responden 4 y 5. Reconstruye quién consulta a quién, quién gana y cuántos envíos intentados tiene el recorrido de la figura 10-1.

> [!question]- Respuesta
> 3 consulta a 4, 5 y 6: tres intentos. Recibe dos respuestas. Delega en 5 con un envío. 5 anuncia a 1, 2, 3 y 4 con cuatro envíos. Total: 3+2+1+4=10 intentos. Gana 5 porque es el máximo entre quienes respondieron. No gana 3 por haber iniciado. La cuenta incluye la consulta sin respuesta a 6 y excluye timeouts como si fueran mensajes.

Ahora supón que 6 sigue vivo, pero su respuesta llega después del timeout.

> [!question]- Respuesta
> Para 3, la ejecución puede ser indistinguible de la caída antes de que llegue esa respuesta. Puede delegar en 5 mientras 6 aún se considera líder. Elegir un timeout más largo puede reducir esta situación, pero no probar una caída cuando la red admite retardos arbitrarios.

## 2. La ruta de sucesores

El líder 6 había publicado [5, 4]. El proceso 3 sospecha su caída. 5 responde y luego anuncia a los cuatro procesos vivos de menor rango. Compara el número de envíos con el ejercicio 1.

> [!question]- Respuesta
> Una consulta a 5, una respuesta de 5 y cuatro anuncios: 1+1+4=6. Son cuatro envíos menos que los diez del recorrido anterior. La lista publicada antes de la falla no se cuenta aquí: estamos comparando solo la recuperación representada. El ahorro tiene un costo previo de mantener y comunicar sucesores.

Si 5 no responde y sí lo hace 4, ¿qué costo adicional aparece antes de poder nombrar a 4?

> [!question]- Respuesta
> Aparece como mínimo el intento dirigido a 5 y la espera que permite decidir probar a 4. Luego hay consulta y respuesta de 4, más la difusión correspondiente. No se puede obtener un tiempo total sin conocer el timeout y las latencias. La figura 10-2 solo muestra la ruta rápida con el primer sucesor disponible.

## 3. Elegibilidad y prioridad

Los candidatos son {1, 2, 6}; los ordinarios, {3, 4, 5}. Cae 6. El proceso 4 tiene el menor δ entre los ordinarios e inicia. Responden 1 y 2. ¿Quién gana? ¿Para qué sirvió δ?

> [!question]- Respuesta
> Gana 2, el mayor rango entre candidatos accesibles. 5 no puede ganar porque es ordinario y 4 no gana por iniciar antes. δ sirve para escalonar las iniciativas y dar una oportunidad de comenzar a un proceso preferido. No cambia la elegibilidad ni crea un voto mayoritario.

Los retardos de dos iniciadores son 100 y 180 ms, pero una respuesta tarda 300 ms. ¿Se ha eliminado la posibilidad de dos rondas?

> [!question]- Respuesta
> No. El segundo iniciador puede agotar su retardo antes de recibir la información de la primera ronda. Los retardos ayudan bajo ciertas condiciones de latencia; una demora que supere esas condiciones conserva la carrera.

## 4. Fusión de grupos

Un grupo A tiene siete miembros y otro B tiene dos. Ambos cuentan a su líder entre los miembros. Compara las referencias al coordinador que deben cambiar si se conserva el líder de A o el de B.

> [!question]- Respuesta
> Conservar A cambia las referencias de dos miembros de B. Conservar B cambia las de siete miembros de A. El ahorro es 7−2=5 actualizaciones. Es una comparación de referencias al líder; no demuestra que toda la fusión requiera exactamente dos mensajes. La negociación y los cambios de membresía pueden añadir comunicación.

## 5. Anillo con máximo acumulado

El orden es 1→2→3→4→5→6→1. Inicia 3, 6 está caído y los demás permanecen accesibles. Completa la carga útil de cada salto usando solo el máximo.

| Salto exitoso | Máximo que sale del emisor |
|---|---|
| 3→4 | 3 |
| 4→5 | 4 |
| 5→1, saltando 6 | 5 |
| 1→2 | 5 |
| 2→3 | 5 |

El iniciador recibe 5 y comienza la difusión del ganador. La función máximo impide que un identificador posterior pero menor, como 1 o 2, reemplace al mejor observado.

> [!question]- ¿Cuántas entregas exitosas hay hasta que termina la segunda vuelta?
> Cinco para descubrir y cinco para anunciar: diez. El intento fallido a 6 se cuenta aparte. Que una variante mantenga solo el máximo reduce la carga útil; no reduce estas diez entregas del ejemplo.

## 6. Contraejemplo de split brain

Hay seis procesos. La red separa {1, 2, 3} de {4, 5, 6}. En cada grupo se aplica «gana el mayor que responde». ¿Qué decisiones locales pueden obtenerse y por qué no hay acuerdo global?

> [!question]- Respuesta
> En el primer grupo puede ganar 3 y en el segundo 6. Cada uno cumple la regla sobre su conjunto observado, pero las vistas son diferentes. No hay comunicación que permita al primer grupo comprobar la existencia y actividad de 6. Una regla determinista sobre entradas distintas produce resultados distintos.

Si ambos grupos recalculan «la mayoría» usando solo sus tres visibles, ¿quedan protegidos?

> [!question]- Respuesta
> No. Ambos podrían considerar suficientes dos votos de su grupo. Con membresía fija de seis, una mayoría estricta es ⌊6/2⌋+1=4. Ningún grupo de tres alcanza cuatro. La base de la cuenta debe ser la membresía acordada, no una vista local reducida.

## 7. Intersección y un voto por ronda

Hay cinco votantes. El candidato A obtiene {1, 2, 3} y el candidato B intenta obtener {3, 4, 5} en la misma ronda. Cada participante solo puede votar una vez por ronda.

> [!question]- Respuesta
> Ambos conjuntos contienen al participante 3. Si 3 ya votó por A, no puede dar su voto a B en esa ronda. B conserva como máximo los votos 4 y 5, que no alcanzan tres. La intersección mínima es 3+3−5=1. La seguridad del argumento depende de mantener el voto incluso después de reiniciar, y no sustituye las reglas para preservar decisiones entre rondas.

¿Cambiar de ronda permite olvidar todas las operaciones que ya se confirmaron?

> [!question]- Respuesta
> No. Una ronda nueva permite cambiar de coordinador bajo las reglas del protocolo; las decisiones anteriores deben preservarse. Ese es el puente hacia la replicación y el consenso: la elección no sustituye la recuperación y protección del estado ya acordado.

## 8. Diagnóstico de una arquitectura

Completa estas decisiones con los supuestos de tu sistema, sin asumir que cualquier elección sencilla implementa consenso:

| Pregunta | Consecuencia de una respuesta incompleta |
|---|---|
| ¿Sobre qué recurso o conjunto de réplicas manda cada líder? | Se puede confundir particionamiento legítimo con autoridad duplicada |
| ¿Qué inicia una elección y qué hipótesis temporal usa? | Un retraso puede provocar reemplazos constantes |
| ¿Quién es elegible y qué ocurre si todos los candidatos fallan? | Puede haber nodos sanos sin coordinador posible |
| ¿Qué mayoría se necesita y cuál es la membresía? | Dos grupos pueden redefinir su propio quórum |
| ¿Cómo se identifica la ronda y se conserva el voto? | Un reinicio puede permitir una autorización contradictoria |
| ¿Qué impide al líder antiguo confirmar decisiones? | Cambiar el nombre del líder no protege los datos |
| ¿Qué estado recupera el nuevo líder? | Se pueden perder decisiones que ya habían sido confirmadas |

La comparación reúne necesidades distintas. Detectar permite sospechar, elegir proporciona un coordinador y replicar con las reglas correctas protege las decisiones. Los capítulos 9, 10 y 11 abordan esas piezas; el desarrollo detallado de consenso requiere el capítulo 14 al que remite el libro.

**Referencia conceptual:** PDF 10–18 · impresas 205–213 · figuras 10-1 a 10-5. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=10|Capítulo de referencia]]. Ejercicios, conteos y contraejemplos: elaboración propia.

---

← [[Obsidian/lecturas/database internals/10 Elección de líder/06 Split brain mayorías y relación con consenso|Anterior]] · [[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Siguiente: capítulo 11]] →
