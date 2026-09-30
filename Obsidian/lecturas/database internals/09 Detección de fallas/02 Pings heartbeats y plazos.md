---
title: "Database Internals — Pings, heartbeats y plazos"
created: 2026-09-30
libro: "Database Internals"
capitulo: 9
tags:
  - lecturas/database-internals
  - arquitectura/deteccion-de-fallas
---

# Pings, heartbeats y plazos

[[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice del capítulo 9]]

## Quién inicia el mensaje

Un **ping** es una consulta iniciada por el observador: A pregunta a B si puede responder. Un **ACK**, o acuse de recibo, es la respuesta esperada. No tiene que ser el comando de red ICMP `ping`: aquí es una operación del protocolo entre procesos.

Un **heartbeat**, o latido, es un aviso iniciado por el proceso vigilado: B envía periódicamente señales de que sigue ejecutando cierta actividad. A conserva el instante local del último aviso y evalúa cuánto tiempo ha pasado desde entonces. Los dos mecanismos permiten detectar ausencia de señales, pero distribuyen de forma diferente quién programa los envíos y cuántos mensajes intercambian.

| Mecanismo | Inicio | Evidencia recibida por A | Lo que no demuestra |
|---|---|---|---|
| Ping | A consulta a B | La petición llegó y B pudo devolver una respuesta por alguna ruta | Que todas las rutas y todas las operaciones de B estén sanas |
| Heartbeat | B publica un aviso | Un mensaje asociado a la actividad de B llegó a A | Que una petición concreta de negocio ya haya terminado |

Un contador o identificador ayuda a reconocer novedad. En un protocolo de ping conviene asociar cada ACK con su consulta: una respuesta antigua no confirma por sí misma que una consulta más reciente haya concluido. Para medir espera basta un reloj local monotónico del observador; no hace falta restar relojes de pared de máquinas distintas.

## Frecuencia y plazo son parámetros diferentes

La **frecuencia de sondeo** determina cada cuánto se inicia una consulta. El **timeout** determina cuánto se acepta esperar una respuesta o cuánto silencio se permite desde un latido. Reducir el intervalo de sondeo aumenta la carga y permite descubrir antes que empezó una falla. Reducir el plazo hace que cada falta de respuesta se convierta antes en sospecha.

**Ejemplo propio.** A envía un ping cada 500 ms y admite 200 ms por consulta. Si B cae justo antes del próximo ping, A sospecha aproximadamente 200 ms después de la caída. Si cae justo después de un ping correctamente contestado, puede pasar cerca de 500 ms hasta el siguiente envío y otros 200 ms hasta vencer su plazo. La demora nominal está entre 200 y 700 ms bajo esos supuestos; las pausas de A y la programación real pueden ampliarla. No es una garantía universal de un sistema asíncrono.

En heartbeats la cuenta cambia según la regla. Si el timeout se mide desde el último latido recibido, el disparo se programa a partir de ese instante; no se añade siempre otro intervalo de envío. Si una implementación exige varios latidos perdidos, hay que especificar cómo los cuenta. La comparación de detectores necesita explicar esa semántica, no sumar tiempos de protocolos diferentes.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 09/01-plazo-y-ack.png]]

Las líneas horizontales representan la ejecución de A y B; el tiempo avanza hacia la derecha. La flecha azul lleva la pregunta a B y la verde devuelve un ACK que llega a los 320 ms. La línea roja marca el plazo local de 200 ms. B nunca cayó, pero A pasa 120 ms con una sospecha falsa. El gráfico usa tiempos inventados para separar la decisión temporal de la realidad del proceso.

## Qué muestran las figuras del libro

La figura 9-1 muestra respuestas que regresan antes de la siguiente consulta. La figura 9-2 muestra respuestas atrasadas que llegan después de que ya comenzó otra consulta. El retraso hace posible una sospecha falsa si se cruza el criterio temporal del detector. Que un ACK llegue después del **siguiente envío** no es por sí solo la definición de timeout: son dos instantes distintos que la implementación debe establecer.

Un **detector de plazo fijo**, descrito con la implementación de Akka como ejemplo histórico del libro, observa latidos y compara su ausencia con un intervalo constante. Su ventaja es una regla sencilla; su dificultad es escoger un valor adecuado para condiciones de red y pausas del proceso que varían. Estas notas explican el mecanismo del capítulo y no documentan la API actual de Akka.

## El estado local y la recuperación

A puede conservar para cada miembro su identificador, el último instante local de evidencia nueva, el último número de secuencia y el estado `activo` o `sospechoso`. El detector no necesita borrar toda memoria al sospechar. Mantenerla permite reconocer un ACK tardío y revisar la decisión según las reglas de la aplicación.

Una transición de sospechoso a activo puede requerir más evidencia que un único paquete tardío. Esa política es una elección de la aplicación: el capítulo no prescribe una máquina de estados universal. Lo esencial es que recibir un mensaje después del plazo no altere retrospectivamente las decisiones ya tomadas por otros protocolos.

Si el tiempo esperado incluye procesamiento de aplicación, saturar B puede producir silencio sin una falla física. Si solo se atiende el heartbeat en un hilo privilegiado, B puede responder al latido mientras sus consultas reales están bloqueadas. El significado de «sano» depende de qué camino de trabajo se está vigilando.

> [!question]- ¿Enviar pings diez veces más seguido permite usar cualquier timeout corto?
> No. Hace más frecuente la observación y aumenta el trabajo. La latencia de una respuesta sigue dependiendo del transporte, la planificación y el procesamiento. Sin un modelo de esos tiempos, la frecuencia no demuestra que una respuesta ausente sea una caída.

**Referencia:** PDF 2–3 · impresas 196–197 · figuras 9-1 y 9-2. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=2|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/09 Detección de fallas/01 Sospecha garantías y errores|Anterior]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/03 Contadores sin timeout y sondeos indirectos|Siguiente]] →
