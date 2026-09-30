---
title: "Database Internals — Fallas parciales, particiones y cascadas"
created: 2026-09-30
libro: "Database Internals"
capitulo: 8
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Fallas parciales, particiones y cascadas

[[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice del capítulo 8]]

Un sistema puede seguir funcionando en algunas partes mientras otras no responden. Esa combinación es más difícil que una parada total: los participantes aún activos toman decisiones con información incompleta y pueden aumentar el daño al intentar recuperarse.

## Silencio, sospecha y partición

Un **heartbeat** es un mensaje periódico usado como señal de actividad. Un **detector de fallas** interpreta esas señales y otros datos para sospechar que un proceso no está disponible. Su resultado depende de las condiciones temporales: perder señales puede deberse a una caída, congestión, una pausa larga o un enlace defectuoso.

Una **partición de red** impide comunicar ciertos participantes o grupos. No exige que todos los nodos estén caídos. En una partición A y B pueden funcionar dentro de un grupo mientras C funciona por separado. También puede haber fallo **asimétrico**: A recibe de B pero B no recibe de A. «Puedo hablarle» y «podemos intercambiar información» no siempre son equivalentes.

Una **falla parcial** afecta solo a algunos componentes o comunicaciones. Si un pedido se replicó pero se perdió su confirmación, el cliente puede sospechar fracaso mientras una réplica ya conserva el dato. Diseñar solo el camino exitoso deja sin definir qué responder, reintentar o recuperar en ese caso.

## Una cascada amplifica un problema

Una **falla en cascada** ocurre cuando el problema de un componente aumenta la presión o corrompe el comportamiento de otros. Si un nodo saturado cae, su tráfico puede desplazarse a los demás y saturarlos también. Si cada cliente reintenta inmediatamente, el tráfico de recuperación añade trabajo precisamente cuando hay menos capacidad.

Un nodo que vuelve después de un tiempo fuera puede necesitar recibir muchas actualizaciones. Si los compañeros envían todo sin límite, pueden agotar red y recursos o derribar de nuevo al recién recuperado. La recuperación también necesita presupuesto de capacidad y coordinación.

| Mecanismo | Qué limita | Qué no garantiza por sí solo |
|---|---|---|
| Circuit breaker | Llamadas repetidas a una dependencia que falla | Que el fallback tenga datos actuales |
| Backoff | Frecuencia de reintentos de un cliente | Que varios clientes no reintenten juntos |
| Jitter | Sincronización accidental de reintentos | Que un reintento sea semánticamente seguro |
| Checksums y validación | Detección de corrupción o formato inválido | Defensa ante todos los mensajes adversarios |
| Coordinación de carga | Trabajo simultáneo y recuperación excesiva | Un plan perfecto frente a toda carga futura |

Un **circuit breaker** registra fallos y suspende temporalmente nuevas llamadas para dar espacio a la recuperación; debe definir cómo prueba si el servicio vuelve y cómo informa la degradación. **Backoff** aumenta la espera entre intentos. **Jitter** introduce variación aleatoria para que muchos clientes no despierten exactamente a la vez.

Ejemplo propio: 100 clientes esperan 1 s y reintentan simultáneamente; ese instante concentra 100 solicitudes. Si el intervalo se distribuye entre 0,5 y 1,5 s, el pico tiende a dispersarse, aunque no se garantiza una carga uniforme ni desaparecen todos los picos. También se necesitan límites de intentos y un presupuesto total de tiempo cuando la operación lo requiere.

## Probar fallos permite comprobar las garantías

El capítulo propone provocar particiones, latencias altas, relojes divergentes, diferencias de velocidad y corrupción. Menciona Toxiproxy, Chaos Monkey, CharybdeFS y CrashMonkey como ejemplos de herramientas disponibles en el contexto del libro. Las notas no suponen su vigencia o compatibilidad actual ni ejecutan experimentos sobre servicios reales.

Una prueba útil verifica una propiedad concreta: «aunque se pierda la confirmación y se reintente, el pedido no se duplica». La simulación final comprueba ese caso en un modelo pequeño. Probar muchas fallas aumenta la confianza, pero la frase del libro sobre encontrar todos los problemas debe entenderse como énfasis: un conjunto finito de pruebas no demuestra ausencia de todo bug posible.

**Referencia:** PDF 11–15 · impresas 178–182. [[Obsidian/lecturas/database internals/Materiales/08 Sistemas distribuidos.pdf#page=11|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/05 Relojes consistencia y llamadas remotas|Anterior]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/07 Enlaces fair-loss ACK y retransmisión|Siguiente]] →
