---
title: "Bully: rangos y sucesores preparados"
created: 2026-09-30
libro: "Database Internals"
capitulo: 10
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Bully: rangos y sucesores preparados

[[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice del capítulo]]

## Un orden de preferencia compartido

En **Bully** cada proceso tiene un rango único y gana el mayor rango de los procesos que se consideran activos. En los ejemplos del libro, el identificador numérico hace de rango. El nombre recuerda que el de mayor rango impone su candidatura; el texto también lo compara con una sucesión monárquica.

La nota al pie de la impresa 207 precisa que los tres pasos descritos corresponden al **Bully modificado**, por ser una versión más compacta. Esta precisión importa: no conviene atribuir a este flujo todas las rondas ni todas las complejidades de otras variantes del Bully original.

El iniciador solo consulta a los procesos con rango superior porque ninguno de los inferiores puede derrotarlo según la regla. Espera sus respuestas. Si no recibe ninguna, se propone como líder y anuncia el resultado a los inferiores. Si recibe respuestas, elige la de mayor rango, le comunica que proceda y ese proceso difunde su liderazgo. Esperar es indispensable: decidir antes de dar oportunidad de responder a los superiores cambia el conjunto de candidatos y puede elegir un nodo incorrecto.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 10/01-bully.png]]

Las cuatro cajas recrean la figura 10-1. El proceso 3 envía consultas a 4, 5 y 6; responden 4 y 5, y por eso 3 delega en 5. La caja verde representa el anuncio a los nodos de menor rango. El caso supone que 6 ha fallado, pero el mensaje sin respuesta no permite distinguir una caída de una interrupción de red. El resultado observado es «5 es el mayor que respondió», no una prueba de que no exista ningún proceso superior vivo.

## Reconstruir el costo del ejemplo

Con un único iniciador, sin retransmisiones y usando un mensaje por destinatario, el ejemplo tiene:

1. Tres intentos de consulta: 3→4, 3→5 y 3→6.
2. Dos respuestas: 4→3 y 5→3.
3. Una delegación: 3→5.
4. Cuatro anuncios: 5→1, 5→2, 5→3 y 5→4.

Son **10 envíos intentados**, de los cuales el dirigido a 6 no obtiene respuesta. Es un conteo didáctico de esta ejecución, no una fórmula general del algoritmo ni una estimación del costo de transporte real. Los timeouts y elecciones concurrentes añaden costo que esta cuenta no representa.

## Dos fallas distintas

Una **partición de red** separa participantes que continúan ejecutándose. Si {1, 2, 3} no puede comunicarse con {4, 5, 6}, 3 puede anunciarse como líder del primer conjunto mientras 6 sigue siendo líder del segundo. Que ambos usen el mismo orden de rangos no soluciona que consultan conjuntos diferentes.

Otro problema es la preferencia por un nodo inestable. Un proceso de rango alto puede recuperar conectividad, reclamar liderazgo, fallar de nuevo y provocar otra elección. El libro propone incorporar métricas de calidad de los hosts a la preferencia. La consecuencia práctica es separar «identificador mayor» de «mejor coordinador»: la regla de rangos da determinismo para una vista compartida, pero no evalúa salud ni evita ciclos de reemplazo.

## Next-in-line: preparar reemplazos

La variante **next-in-line failover** evita reconstruir toda la elección cuando ya existe una lista de alternativas. El líder publica sucesores ordenados. Al sospechar que el líder falló, un proceso contacta primero al sucesor preferido; si responde, ese sucesor asume y anuncia el liderazgo. Si el detector de la falla ya es la primera alternativa, puede anunciarse directamente.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 10/02-sucesores.png]]

La recreación de la figura 10-2 parte de la lista [5, 4] publicada por 6. El proceso 3 consulta a 5, recibe una respuesta y deja de buscar. Luego 5 anuncia el resultado y puede publicar la lista [4, 3] que aparece en la figura del libro. Las flechas azules representan la secuencia de mensajes; el recuadro rojo indica el límite de la optimización: preseleccionar reemplazos ahorra pasos, pero no añade una autorización global para liderar.

En ese recorrido hay una consulta, una respuesta y cuatro anuncios: **6 envíos**, frente a los 10 del ejemplo anterior bajo los mismos supuestos. La mejora depende de que 5 esté disponible. Si no lo está, el timeout de 5 se añade al tiempo antes de probar 4. Cuando se agota la lista, hace falta una política adicional o una elección completa; estas páginas no especifican ese caso ni cómo versionar listas viejas.

> [!question]- Si 5 responde a 3 y cae antes de anunciarse, ¿ya terminó la elección?
> La respuesta demuestra disponibilidad en aquel instante. No garantiza que 5 seguirá vivo ni que todos conozcan el resultado. El sistema necesita detectar la nueva falta de progreso y recuperar un coordinador; el ejemplo sencillo omite esa carrera.

**Referencias:** PDF 12–13 · impresas 207–208 · figura 10-1 y nota al pie sobre Bully modificado. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=12|Bully]]. PDF 13–14 · impresas 208–209 · figura 10-2. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=13|Sucesores]].

---

← [[Obsidian/lecturas/database internals/10 Elección de líder/01 Coordinación estabilidad y garantías|Anterior]] · [[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/10 Elección de líder/03 Candidatos ordinarios y elecciones simultáneas|Siguiente]] →
