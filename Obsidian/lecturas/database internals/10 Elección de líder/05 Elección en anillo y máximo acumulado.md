---
title: "Elección en anillo y máximo acumulado"
created: 2026-09-30
libro: "Database Internals"
capitulo: 10
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Elección en anillo y máximo acumulado

[[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice del capítulo]]

## Un recorrido ordenado

El algoritmo en **anillo** usa una topología lógica: cada proceso conoce el orden de sus compañeros y cómo encontrar sucesores. «Lógica» significa que la disposición puede existir en la configuración y el protocolo aunque el cableado físico no forme un círculo.

Cuando un proceso detecta la falla del líder, empieza un mensaje de elección que avanza al siguiente proceso. Cada receptor añade su identificador al conjunto de nodos visitados y lo reenvía. Si el sucesor no responde, se prueba con el siguiente del orden hasta encontrar uno accesible. Esta capacidad requiere conocer más que un único sucesor inmediato: si únicamente se conociera al vecino caído, no se podría encontrar a quien lo sigue para saltarlo.

La idea se parece al detector sin timeouts de la impresa 197 del capítulo 9, en el que los mensajes acumulan la ruta. Aquí la finalidad es elegir al mayor rango entre los procesos encontrados. El silencio de un sucesor sigue siendo una observación de accesibilidad; el mecanismo de detección determina cuándo se decide saltarlo.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 10/05-anillo.png]]

La recreación de la figura 10-5 separa sus dos recorridos. A la izquierda, 3 inicia, el conjunto crece y 5 salta al líder caído 6 para enviar a 1. Cuando 2 devuelve el conjunto a 3, este calcula que 5 es el rango máximo. A la derecha, el resultado circula por el mismo conjunto vivo. La primera vuelta obtiene información; la segunda comunica una decisión que los receptores de la primera vuelta todavía no podían conocer.

## Por qué una sola vuelta no basta

Cuando 4 recibe {3}, aún no sabe si hay un nodo 5 vivo más adelante. Cuando 5 recibe {3, 4}, tampoco sabe todavía qué nodos verá el resto del recorrido. Solo al cerrar la vuelta el iniciador posee el conjunto completo observado en esa ejecución. Elegir al máximo en ese punto produce un dato nuevo que necesita propagarse.

Para cinco nodos vivos, una vuelta contiene cinco entregas entre procesos: 3→4→5→1→2→3. La segunda contiene otras cinco. Hay **10 entregas exitosas** bajo el supuesto de un recorrido estable y un único iniciador. El intento dirigido a 6, sus esperas y las retransmisiones no se incluyen en ese número. La latencia depende de la cadena de saltos y de la detección de sucesores inaccesibles, aunque cada nodo haga poco trabajo local.

## Guardar solo el máximo

Si el único resultado deseado es el mayor rango, llevar el conjunto entero conserva más información de la necesaria. La variante del libro mantiene un **máximo acumulado**: cada proceso compara su rango con el que recibió y pasa el mayor.

En el ejemplo: 3 inicia con 3; 4 produce max(3, 4)=4; 5 produce max(4, 5)=5; 1 mantiene max(5, 1)=5; 2 mantiene max(5, 2)=5. Al regresar a 3, el valor final es 5. La segunda vuelta todavía hace falta para difundirlo.

La operación máximo es **conmutativa**: cambiar el orden de dos argumentos no cambia el resultado. También es **asociativa**: agrupar las comparaciones de distinta forma no cambia el máximo final. Por esas propiedades, acumular el máximo produce el mismo ganador que calcularlo sobre el conjunto completo, siempre que ambos métodos visiten a los mismos nodos.

| Contenido del mensaje | Información conservada | Tamaño conceptual |
|---|---|---|
| Conjunto de visitados | Todos los IDs observados | Crece con la cantidad de nodos |
| Máximo acumulado | Solo el mayor ID observado | Un identificador, más metadatos del protocolo |

Guardar solo un identificador ahorra espacio de carga útil, pero no elimina los mensajes del recorrido ni demuestra que se visitó todo el clúster. Para regresar al iniciador y distinguir rondas concurrentes hacen falta metadatos y reglas que el resumen del capítulo no especifica en detalle.

## Saltar nodos no evita particiones

Saltar a 6 ayuda a continuar cuando un nodo aislado del recorrido está caído y los demás aún pueden comunicarse. Si la red se separa en grupos y cada uno logra cerrar su propio recorrido sobre accesibles, puede elegir un máximo distinto. El algoritmo continúa funcionando localmente y sigue sin garantizar un único líder global.

Además, los nodos observados no necesariamente estuvieron vivos al mismo tiempo: un proceso puede caer después de haber añadido su ID. El ganador calculado puede no estar accesible al recibir el anuncio. En esa situación se necesita detectar la falta de progreso y volver a elegir; el dibujo supone una ejecución estable durante sus dos vueltas.

> [!question]- Si el mensaje trae máximo 5 y el nodo actual es 2, ¿debe reemplazarlo por 2 porque fue el último visitado?
> No. Debe enviar max(5, 2)=5. Reemplazar por el último ID destruiría el significado de máximo acumulado y haría depender el resultado del punto donde empezó el recorrido.

**Referencia:** PDF 16–17 · impresas 211–212 · figura 10-5 y variante del máximo. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=16|Fuente del algoritmo en anillo]].

---

← [[Obsidian/lecturas/database internals/10 Elección de líder/04 Invitación y fusión de grupos|Anterior]] · [[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/10 Elección de líder/06 Split brain mayorías y relación con consenso|Siguiente]] →
