---
title: "Database Internals — Capítulo 11 · Modelos como contratos de visibilidad"
created: 2026-09-30
libro: "Database Internals"
capitulo: 11
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Modelos como contratos de visibilidad

[[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice del capítulo]]

Un **historial** reúne las invocaciones y respuestas de varios clientes. Un modelo de consistencia selecciona cuáles de esos historiales son aceptables. Es un contrato de resultados observables: permite razonar sobre lo que puede leer un cliente sin conocer exactamente cómo se copiaron los bytes.

El capítulo supone que cada cliente ejecuta sus operaciones secuencialmente: termina una antes de comenzar la siguiente. Aun así, operaciones de clientes distintos pueden solaparse. Un programa que escribe y después lee aporta un orden local; no aporta por sí solo un reloj compartido para todos los demás clientes.

## Una escritura y dos lecturas

Ejemplo propio: `x=0`; P1 ejecuta `write(x,1)` y P2 realiza `R1=read(x)`, luego `R2=read(x)`. En un registro atómico, y sin otras escrituras, los resultados posibles son `(0,0)`, `(0,1)` y `(1,1)` según el lugar de la escritura respecto a las lecturas. `(1,0)` exigiría que la misma escritura apareciera antes de R1 y después de R2, contrariando el orden de P2.

Pero conocer sólo el texto del programa no indica en qué caso estaremos. Necesitamos los intervalos de las llamadas, el contrato del registro y las otras operaciones de la historia. Con replicación también puede existir una demora de visibilidad aun después de recibir una respuesta, si el contrato lo permite.

## Estado y operaciones

Podemos formular consistencia desde el **estado**, preguntando qué relación debe existir entre copias, o desde las **operaciones**, preguntando qué orden explica las respuestas. Dos réplicas iguales al final no prueban que todas las lecturas anteriores fueran válidas. Y diferencias internas temporales no prueban por sí solas una violación si el protocolo impide exponerlas de forma prohibida.

| Modelo | Restricción principal | Lectura atrasada tras escritura confirmada de otro cliente |
|---|---|---|
| Linealizable | Orden total que respeta precedencia real | No, si esa escritura precede a la lectura y no fue reemplazada |
| Secuencial | Orden total que conserva orden de cada cliente | Puede admitirse |
| Causal | Orden de dependencias causales | Puede admitirse si no se pierde el contexto requerido |
| PRAM/FIFO | Orden de escrituras de cada origen | No establece un orden común entre orígenes |
| Eventual | Convergencia cuando cesan cambios y se propagan | Puede admitirse durante la divergencia |

No todos los modelos se comparan mediante una única escalera. Las garantías de sesión describen una perspectiva del cliente; la convergencia eventual describe el destino de las réplicas. Un sistema puede combinarlas. El resumen del capítulo ordena varios modelos de operación por fuerza, pero no convierte todas las propiedades del tema en categorías mutuamente excluyentes.

## El costo de restringir historias

Mantener un orden puede requerir intercambiar mensajes, esperar respuestas, persistir información de recuperación y ejecutar más trabajo. El costo incluye latencia, CPU, disco y tráfico de red. Esos recursos permiten excluir resultados peligrosos: la decisión se evalúa contra la operación que necesita la aplicación.

Una consistencia **estricta** teórica supone que una escritura está visible globalmente de forma instantánea según un reloj universal. El capítulo la distingue de linealizabilidad, que permite ubicar el efecto dentro de un intervalo real. Linealizabilidad no exige comunicación instantánea ni que el sistema distribuido consulte un reloj global para cada operación.

> [!question]- ¿Que dos réplicas terminen iguales prueba linealizabilidad?
> No. Podrían converger después de devolver una lectura vieja que comenzó tras confirmar una escritura. El contrato linealizable se revisa sobre todo el historial observable.

**Referencia:** PDF 25–27 · impresas 221–223. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=25|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/11 Replicación y consistencia/04 Registros e intervalos concurrentes|Anterior]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/11 Replicación y consistencia/06 Linealizabilidad puntos de efecto y costo|Siguiente]] →
