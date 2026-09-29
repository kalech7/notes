---
title: "10 · Datos, nube, fallos y recuperación"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/capas
capitulo: 10
---

# Datos, nube, fallos y recuperación

[[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 7 · impresa 159; PDF 9–10 · impresas 161–162** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/07 Arquitectura por capas.pdf|07 Arquitectura por capas.pdf]], capítulo 10, «Layered Architecture Style», del fragmento proporcionado de *Fundamentals of Software Architecture*. Explicación original en español. Los ejemplos, diagramas y ejercicios se identifican como elaboración didáctica; las valoraciones pertenecen a la fuente y se contextualizan, no se presentan como mediciones universales.

## La topología de datos habitual

El capítulo caracteriza la arquitectura por capas tradicional como un monolito acompañado de una base de datos común. La capa de persistencia sirve con frecuencia para traducir entre objetos del lenguaje y estructuras relacionales orientadas a conjuntos.

Esa capa evita que todas las partes de la aplicación implementen su propio acceso a datos. A cambio, una base de datos compartida puede convertirse en punto común de disponibilidad, capacidad y coordinación de cambios. Una capa de persistencia no hace desaparecer esos riesgos: los encapsula parcialmente desde la perspectiva del código.

## Trasladar capas a la nube cambia las distancias

La fuente contempla desplegar una o varias capas en infraestructura de nube. La partición técnica facilita identificar piezas que podrían moverse, pero los flujos suelen cruzar varias capas. Si se separan entre instalaciones locales y nube, aparecen viajes de red que antes podían ser locales.

**Elaboración didáctica.** Supón que un caso de uso hace cinco consultas secuenciales entre la aplicación local y una persistencia remota. Si cada ida y vuelta agrega 30 ms, solo ese componente de comunicación puede sumar aproximadamente `5 × 30 = 150 ms`. No incluye tiempo de consulta, procesamiento ni espera. La suma aplica al supuesto secuencial; si algunas operaciones pueden solaparse, el cálculo cambia.

No deduzcas que la nube es necesariamente lenta o que un traslado está prohibido. La decisión depende de ubicación, patrón de llamadas, ancho de banda, tamaño de mensajes y requisitos. El punto del capítulo es que una división física no es gratuita.

## Qué fallo aísla una capa, y cuál no

Una frontera lógica puede aislar **cambios de código** sin aislar **fallos de ejecución**. Si negocio y presentación comparten proceso, un agotamiento de memoria que termina ese proceso afecta a ambas. El libro utiliza este ejemplo para explicar la débil tolerancia a fallos del despliegue monolítico.

![Fallo de una réplica y dependencias comunes](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c10-04-fallos-escala.png)

En el gráfico, cada réplica contiene la aplicación completa. La caída de una puede ser tolerada por las demás si existen capacidad suficiente y mecanismos de recuperación y distribución de tráfico. La base de datos común sigue siendo una dependencia compartida. La figura es elaboración didáctica para matizar el riesgo del capítulo; no reproduce una topología que el fragmento especifique.

> [!warning] Debilidad inherente no equivale a imposibilidad
> La arquitectura por capas no proporciona por sí sola aislamiento de fallos entre responsabilidades que comparten proceso. Eso no significa que todo sistema por capas deba tener disponibilidad baja: réplicas, recuperación y redundancia pueden mejorarla. Esas capacidades necesitan diseño y operación adicionales.

## MTTR y disponibilidad

**MTTR** es el tiempo medio necesario para recuperar el servicio después de un fallo, según la definición operativa utilizada. El capítulo lo relaciona con la duración de arranque y recuperación de monolitos: ofrece ejemplos desde alrededor de dos minutos para aplicaciones menores hasta quince minutos o más en aplicaciones grandes.

Son ejemplos de la fuente, no tiempos universales ni una predicción para tu aplicación. Reiniciar el proceso tampoco equivale siempre a restaurar el servicio: puede faltar recuperar conexiones, reconstruir cachés o verificar que el sistema atienda correctamente. Esta última observación es una ampliación didáctica.

Una aplicación que falla pocas veces pero tarda mucho en recuperarse puede acumular una interrupción importante. Por eso evaluar disponibilidad exige mirar tanto frecuencia de fallo como tiempo y alcance de recuperación, en lugar de limitarse a contar capas.

## Escalabilidad, elasticidad y el costo de replicar todo

La ficha del capítulo puntúa bajo escalabilidad y elasticidad por el acoplamiento del despliegue. Si el trabajo intenso está en una sola función, la unidad habitual de escalado sigue siendo el monolito completo. Replicas presentación, negocio y persistencia aunque la presión no crezca por igual en todos ellos.

Esto no significa que un monolito sea incapaz de atender grandes volúmenes ni de ejecutarse con varias réplicas. Significa que el estilo no ofrece naturalmente el escalado independiente de capacidades que proporcionan otras divisiones arquitectónicas. Además, la base de datos compartida u otros recursos pueden seguir limitando la capacidad global.

La fuente menciona concurrencia, mensajería interna y procesamiento paralelo como técnicas posibles, pero con diseño adicional. Cachear datos también puede mejorar respuesta, aunque introduce otras decisiones, como actualización e invalidación. Esas técnicas cambian la implementación; no convierten automáticamente el sistema en varias unidades arquitectónicas independientes.

## El alcance de «un quantum»

El capítulo asigna **un quantum arquitectónico** al estilo que evalúa, por la unidad funcional y sus dependencias sobre interfaz, procesamiento y datos. Leerlo correctamente requiere conservar ese contexto: **no es una ley que todo software que use alguna capa tenga un solo quantum**.

Si diseñas varios servicios independientes y cada uno usa capas internamente, estás combinando dos niveles de decisión. Para determinar los quanta debes analizar independencia, despliegue y acoplamientos reales del sistema completo; contar capas o réplicas no basta.

## Preguntas resueltas

**¿Añadir otra réplica elimina el cuello de botella de datos?** No necesariamente. Puede aumentar el número de conexiones y consultas contra el mismo almacén. Hay que medir la capacidad del conjunto.

**¿Separar persistencia en otra máquina mejora siempre tolerancia a fallos?** No. Crea una frontera física, pero si todas las solicitudes dependen de ella y no existe una estrategia de recuperación, su fallo puede detener el servicio igualmente.

**¿Qué medirías antes de mover una capa?** Como ejercicio didáctico: rutas y cantidad de llamadas, latencia observada, percentiles de respuesta, volumen transferido y comportamiento cuando la dependencia no responde. La topología física debe justificarse con esos requisitos.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/10 Arquitectura por capas/00 Índice|← Volver al índice]]
