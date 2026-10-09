---
title: "10 S17 - Repaso activo y preguntas resueltas"
created: 2026-10-09
capitulo: 17
sesion: 17
tags:
  - maestria/ia-generativa
  - agentes/observabilidad
  - estudio
---

# 10 S17 - Repaso activo y preguntas resueltas

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/00 Índice - S17 Observabilidad y prompts|Índice de S17]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Estas preguntas integran los conceptos de la sesión y distinguen los datos del material de las decisiones de diseño. Las respuestas están plegadas para practicar recuperación activa: intentar explicar primero, luego contrastar.

## Comprensión de los registros

> [!question]- 1. ¿Cuál es la diferencia entre traza, span y sesión?
> La traza describe una ejecución completa. Un span describe una operación dentro de esa ejecución. Una sesión agrupa varias trazas relacionadas, por ejemplo las preguntas de una conversación. Cada corrida necesita identidad propia aunque comparta sesión.

> [!question]- 2. ¿Puede una corrida tener `error = null` y estar mal?
> Sí. `error = null` indica que no se registró una excepción técnica. Puede haber una respuesta falsa, fuera de alcance, excesivamente cara o lenta. Esos resultados necesitan criterios de evaluación y métricas además del campo de error.

> [!question]- 3. ¿Por qué conservar el modelo y la versión del prompt por llamada?
> El modelo determina comportamiento y tarifas; el prompt determina instrucciones. Si una corrida usa distintos modelos o prompts, un valor global no describe cada llamada. Registrar la relación permite atribuir consumo y reconstruir qué produjo una respuesta.

> [!question]- 4. ¿Por qué «si no está en la traza, no pasó» no es una afirmación literal sobre la realidad?
> Es una regla de evidencia. Algo puede ocurrir sin registro, pero luego no podrá demostrarse ni atribuirse usando la traza. La observabilidad busca evitar esos huecos.

## Cuentas de costo

> [!question]- 5. Una llamada tiene 2 800 tokens de entrada y 295 de salida. ¿Costó 0,004275 USD?
> Solo bajo las tarifas de 1 USD por millón de entrada y 5 USD por millón de salida, aplicadas a todo ese consumo: `0,0028 + 0,001475 = 0,004275 USD`. Si faltan modelo, tarifa o categorías de uso, no puede afirmarse el costo real. Ese es el hueco que destaca la página 7 frente al total impreso de 0,011 USD.

> [!question]- 6. ¿Cómo puede dominar el gasto la entrada si la salida cuesta cinco veces más por token?
> Porque la cantidad también importa. En los datos del PDF, 59 000 tokens de entrada cuestan 0,059 USD y 2 914 de salida cuestan 0,01457 USD. La entrada es mucho más abundante y aporta el 80,2 % del total.

> [!question]- 7. ¿Qué significa que una corrida represente el 10 % del tráfico y el 41 % del gasto?
> En un conjunto de diez, una corrida es el 10 % de las consultas. Si cuesta 0,03013 USD de un total de 0,07357 USD, concentra `0,03013 / 0,07357 ≈ 40,95 %` del gasto. La cantidad de consultas y el costo por consulta no tienen por qué distribuirse igual.

## Cuentas de tiempo

> [!question]- 8. En diez corridas, p50 = 272 ms, media = 346 ms y p95 = 740 ms. ¿Cuál se acerca más a la experiencia lenta?
> p95 describe la cola lenta mejor que p50 o la media. Pero la corrida máxima de 1 111,69 ms queda por encima de p95. El panel debe permitir abrir casos extremos y recordar que diez observaciones ofrecen una muestra pequeña.

> [!question]- 9. Dos llamadas paralelas tardan 800 ms cada una. ¿La corrida tarda 1 600 ms?
> No necesariamente. Si empiezan juntas y no hay otros pasos, la duración transcurrida puede acercarse a 800 ms. Sumar tiempos de trabajo no equivale a medir tiempo de espera cuando hay solapamiento.

> [!question]- 10. ¿Por qué «la corrida más cara es la segunda más rápida» no prueba independencia estadística?
> Demuestra que costo y tiempo no son sustitutos en esos ejemplos. La independencia estadística requiere analizar su relación en una distribución. En otros sistemas aumentar tokens puede aumentar tanto gasto como duración.

## Instrumentación y privacidad

> [!question]- 11. Una validación dura 400 ms y el cronómetro empieza después. ¿Qué latencia queda mal?
> La latencia de extremo a extremo: excluye los 400 ms. La traza raíz debe comenzar antes de validar, incluso si esa validación bloquea la entrada.

> [!question]- 12. ¿Cómo se evita perder la corrida que falla?
> Se registra el error y se cierra la medición en una ruta que también se ejecuta ante excepciones. El mecanismo conserva la evidencia y relanza el error; la capa responsable decide reintentar o informar. Un cierre abrupto del proceso todavía puede requerir medidas adicionales de persistencia.

> [!question]- 13. ¿Por qué una máscara de listas puede dejar pasar correos?
> Porque los datos pueden llegar en tuplas, diccionarios, textos de excepción u otras estructuras. El PDF demuestra la omisión de tuplas en argumentos decorados. La prueba debe cubrir las estructuras y ramas reales antes de persistir o enviar.

> [!question]- 14. Si Langfuse está autoalojado, ¿todos los datos del agente se quedan en la máquina?
> No necesariamente. Solo describe dónde se administra la observabilidad. Un proveedor remoto del modelo sigue recibiendo sus solicitudes. Las dos rutas deben analizarse por separado.

## Versiones y evidencia de mejora

> [!question]- 15. ¿Qué diferencia hay entre v2 y production?
> v2 identifica un contenido específico. production es una etiqueta móvil que selecciona una versión. La traza debe guardar la versión que se utilizó realmente, no solo una etiqueta que mañana puede cambiar.

> [!question]- 16. ¿Qué demuestra el campo `prompt_version = v3` en diez corridas?
> Que esas corridas registran una misma versión. No demuestra que v3 sea mejor que v2. Para eso hacen falta ejemplos comparables, criterios y resultados de ambas versiones.

> [!question]- 17. ¿Qué resuelve un fallback local de prompt?
> Permite continuar obteniendo una plantilla si falla su gestión remota bajo las condiciones de esa implementación. No reemplaza un modelo caído, ni permite ignorar diferencias del contenido usado. El fallback también debe quedar registrado.

> [!question]- 18. ¿Puede compararse una cuota de 50 000 unidades con otra de 5 000 trazas y concluir cuál es más barata?
> No. Se debe conocer cómo define cada plataforma su unidad, cuántos pasos y llamadas tiene una corrida, retención, usuarios, volumen y operación. Además, las cuotas del PDF son históricas y necesitan verificación antes de una decisión actual.

## Tres ejercicios de reconstrucción

> [!question]- 19. Un padre dura 1 000 ms y tiene hijos consecutivos de 50, 300, 200 y 400 ms. ¿Qué sabemos de los otros 50 ms?
> Los hijos suman 950 ms. Bajo el supuesto de que no hay otros hijos ni solapamiento, quedan 50 ms exclusivos del padre. Su causa no queda determinada por restar: pueden incluir preparación, espera o trabajo no instrumentado. Hay que medir ese hueco antes de atribuirlo a una tarea.

> [!question]- 20. Dos generaciones cuestan 0,0017 y 0,0031 USD. La segunda se repite una vez después de una respuesta inválida. ¿Qué costo debe registrar la corrida?
> Si ambos intentos de la segunda consumieron 0,0031 USD, el total es `0,0017 + 0,0031 + 0,0031 = 0,0079 USD`. Que el primer intento no produzca una respuesta útil no elimina su consumo. Se guardan los dos intentos y el motivo de repetir.

> [!question]- 21. v1 acierta fecha y aula y falla abstenciones. v2 acierta abstenciones y falla fecha y aula. Ambas tienen 2/4. ¿Son equivalentes?
> No. El total oculta qué casos cambian. v2 introduce regresiones en preguntas que sí tenían datos. Se compara por caso y criterio, además del agregado; no se promueve una versión solo porque conserva el porcentaje global.



## Un caso integrador resuelto

Ejemplo propio: tras cambiar un prompt de calendario, el asistente responde más rápido, envía menos tokens y se equivoca en dos fechas. El panel de latencia mejora y el de costo también.

> [!question]- ¿Se debe mantener el cambio? ¿Qué evidencia hace falta?
> La mejora operativa no compensa automáticamente el fallo de calidad. Se abren las dos trazas y se identifica qué versión exacta, modelo, contexto y herramientas se usaron. Luego se compara con la versión anterior sobre el mismo conjunto de pruebas y criterios de fechas correctas. Si la nueva versión perdió información necesaria al recortar contexto, se corrige la candidata o se revierte production a una versión conocida. El informe debe mostrar calidad, costo y tiempo, no seleccionar solo las dos métricas favorables.

## Advertencia sobre las fechas académicas del material

La página 37 repite «viernes 17 de octubre» para 2026. El 17 de octubre de 2026 cae sábado. Se conserva la fecha indicada como contenido de la fuente y se señala que el día de la semana es contradictorio. Estas notas no fijan una entrega ni asumen qué dato quiso corregir el docente.

La página distingue el Taller 4 como 25 % de la nota del curso y la Parte 1 como 25 % dentro del taller; también menciona la Parte 0.c con 3 %. Son escalas distintas. Sin el enunciado completo y vigente no conviene convertir estos porcentajes en una calificación absoluta.

Fuente: PDF 1–37 · numeración visible = página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/S17 Observabilidad y versionado de prompts.pdf#page=37|Sesión 17, página 37]].

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/09 S17 - Laboratorio resuelto sin API ni servicios externos|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/17 Observabilidad y versionado de prompts/00 Índice - S17 Observabilidad y prompts|Siguiente]] →
