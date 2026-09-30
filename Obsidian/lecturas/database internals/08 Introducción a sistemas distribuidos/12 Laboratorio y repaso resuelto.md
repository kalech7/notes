---
title: "Database Internals — Laboratorio y repaso resuelto · Sistemas distribuidos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 8
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Laboratorio y repaso resuelto · Sistemas distribuidos

[[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice del capítulo 8]]

Ahora podemos convertir las definiciones en historias que produzcan resultados comprobables. Este laboratorio usa modelos pequeños y deterministas para que cada estado sea visible; no intenta simular todos los fallos de un clúster real.

El programa [[Obsidian/lecturas/database internals/Materiales/Laboratorios/08 sistemas_distribuidos.py|08 sistemas_distribuidos.py]] se ejecuta con Python sin dependencias adicionales. Enumera carreras, calcula una cola, reordena mensajes y compara un cobro reintentado con y sin memoria durable. Los ejemplos y cifras son propios.

## 1. Enumerar todas las carreras

El sumador y multiplicador de la nota 02 tienen cada uno una lectura y una escritura. Para preservar `R+ < W+` y `R× < W×` existen seis mezclas. El programa recorre las permutaciones, descarta las que rompen ese orden y calcula cada estado.

Resultado: `{2, 3, 4, 6}`. Hay cuatro resultados distintos y seis historias. La comprobación hace explícito el modelo de lecturas/escrituras individuales atómicas; no ejecuta hilos con una carrera real ni se apoya en garantías de un lenguaje con comportamiento indefinido.

> [!question]- ¿Por qué 5 no aparece?
> Si ambos leen 1, la última escritura deja 2 o 3. Si la lectura de uno sucede después de la escritura del otro, obtiene 2 y suma 2 = 4, o recibe 3 y multiplica por 2 = 6. No hay un paso que escriba 5 en este modelo.

## 2. Calcular una cola finita

Durante 3 s entran 160 solicitudes/s y salen 100/s. Pendientes: `(160 − 100) × 3 = 180`. Al bajar la llegada a 70/s, el exceso baja 30/s y desaparece en 6 s. Si el límite es 120, no cabe todo el exceso: hay que esperar, rechazar o perder trabajo según el contrato. Guardarlo silenciosamente en memoria extra rompe el límite supuesto.

> [!question]- ¿Cuánto tardaría en vaciar si siguen llegando 100/s?
> No baja: todo el trabajo completado se reemplaza por otro nuevo. A 160/s aumenta; a 70/s disminuye. Para vaciar sin detener ingreso la capacidad de salida debe superar la llegada durante suficiente tiempo.

## 3. Recibir fuera de orden

Entrada: `1, 3, 2, 3, 5, 4`. El receptor conserva buffer y entrega solo la secuencia consecutiva:

| Entrada | Entrega nueva | Buffer posterior | Último procesado |
|---:|---|---|---:|
| 1 | 1 | vacío | 1 |
| 3 | ninguna | 3 | 1 |
| 2 | 2, 3 | vacío | 3 |
| 3 | ninguna, duplicado | vacío | 3 |
| 5 | ninguna | 5 | 3 |
| 4 | 4, 5 | vacío | 5 |

El resultado es `1, 2, 3, 4, 5`, sin aplicar dos veces el 3. El programa combina entrega y procesamiento inmediatos para mantener pequeño el ejemplo. Un receptor real puede tener etapas separadas y necesitar registrar su avance al reiniciar.

## 4. Perder el ACK después del cobro

Sin deduplicación, cobrar 20 y repetir el cobro después de perder el ACK acumula 40. Con un ID `pedido-42`, el primer intento guarda el resultado y el segundo devuelve ese mismo resultado: el total queda en 20. El programa representa una transacción atómica mediante creación de un nuevo snapshot en memoria; una aserción comprueba que efecto e ID aparecen juntos.

Después se construye otra instancia desde ese snapshot, modelando recuperación con estado durable. El reintento conserva 20. Una instancia que recupera el total pero olvida el registro del ID vuelve a cobrar y alcanza 40. Esta diferencia verifica la importancia de la memoria de deduplicación; el programa no realiza escrituras de disco, fallos entre instrucciones ni transacciones con proveedores externos.

> [!question]- ¿Cambiar a un ID nuevo al reintentar conserva la garantía?
> No. El servidor lo interpreta como otra operación. El cliente debe conservar el identificador de la operación original y evitar asociarlo a contenidos diferentes.

## 5. Separar seguridad de progreso

Supón A, B y C, y C deja de contestar. «Nadie decide algo incompatible» es seguridad. «Los procesos correctos terminan decidiendo» es vivacidad. Un protocolo puede conservar seguridad y esperar porque no tiene condiciones suficientes para progresar. De FLP no se deduce que deba inventar una decisión al vencer un plazo.

> [!question]- ¿FLP solo dice que desconocemos cuántos segundos tardará el consenso?
> No. Bajo sus supuestos, un protocolo determinista no garantiza terminación eventual para toda ejecución admisible. Puede decidir en numerosas ejecuciones, pero existe una ejecución que evita la decisión. No es una afirmación sobre el rendimiento típico de un sistema real.

> [!question]- ¿Sincronía parcial significa que casi siempre llega rápido?
> Esa descripción informal no basta. El modelo exige una hipótesis precisa sobre cotas desconocidas o cotas que empiezan a valer en un instante desconocido. La garantía de progreso depende de cuándo se cumplen las condiciones del protocolo.

> [!question]- ¿Qué demuestra recibir un ACK TCP?
> La confirmación definida en la capa de transporte, no la ejecución durable de un pedido. La aplicación necesita su confirmación y contrato para relacionarlo con un commit o un efecto externo.

> [!question]- ¿Qué diferencia una partición de una caída?
> En una partición los procesos pueden seguir ejecutando, pero ciertos enlaces impiden comunicación. Desde otro proceso la falta de respuesta puede parecer una caída. Una caída detiene el proceso según el modelo; el silencio solo no identifica cuál de las dos ocurrió.

> [!question]- ¿Qué error puede causar un reloj de pared que retrocede?
> Restar lecturas puede dar una duración negativa o alterar un plazo si se utiliza la fuente equivocada. Una fuente monotónica sirve para intervalos locales; no establece por sí sola el orden causal entre máquinas.

## Transferir las ideas a un diseño

Para una API de pedidos describe el ID de operación, qué efecto confirma la respuesta, qué estado sobrevive a reiniciar y qué hace ante resultado desconocido. Después identifica límites de cola, política de reintento y fallo de red. Finalmente expresa qué modelo soporta el acuerdo entre réplicas. Si alguna de esas condiciones queda implícita, el resultado normal puede ocultar un problema precisamente cuando hace falta recuperar.

**Referencia:** Síntesis de PDF 1–26 · ejercicios y simulación propios. [[Obsidian/lecturas/database internals/Materiales/08 Sistemas distribuidos.pdf#page=4|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/11 Modelos de fallas y tolerancia|Anterior]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Siguiente: capítulo 9]] →
