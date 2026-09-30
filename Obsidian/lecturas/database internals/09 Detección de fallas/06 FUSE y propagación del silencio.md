---
title: "Database Internals — FUSE y propagación del silencio"
created: 2026-09-30
libro: "Database Internals"
capitulo: 9
tags:
  - lecturas/database-internals
  - arquitectura/deteccion-de-fallas
---

# FUSE y propagación del silencio

[[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice del capítulo 9]]

## Cambiar la pregunta para poder propagar la falla

Los mecanismos anteriores intentan reunir evidencia sobre miembros individuales. **FUSE**, el servicio de notificación de fallas descrito por el capítulo, organiza procesos en grupos y propaga que un grupo dejó de estar disponible. La pregunta operativa pasa a ser «¿este grupo sigue pudiendo actuar como unidad?».

Enviar una noticia explícita de falla a todos puede resultar caro o imposible cuando la propia red está partida. FUSE utiliza una señal que también puede observarse cuando la comunicación se interrumpe: **el silencio**. Si un miembro detecta que otro ya no responde, deja a su vez de responder a pings. Otros detectan su ausencia y suspenden sus respuestas; la indisponibilidad se extiende a la unidad completa.

Ese silencio es **conducta del protocolo**, no necesariamente una caída física adicional. D puede seguir ejecutándose mientras decide no contestar porque el grupo ya no reúne la condición requerida. Si se confundiera esa conducta con apagado real de D, se perdería el objetivo del algoritmo.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 09/05-fuse-silencio.png]]

La caja roja inicial identifica la caída física de B. Las cajas ámbar muestran el silencio inducido en D y después en A y C. La caja roja final expresa el estado lógico de la unidad: el grupo no está disponible. Las flechas representan detección y propagación, no un contagio que apague físicamente las máquinas. El escenario es propio y explica el mismo mecanismo de la figura 9-5 con letras diferentes.

## Reconstruir la figura 9-5 sin su errata

El estado inicial muestra cuatro participantes que se comunican. P2 cae y deja de contestar. P4 detecta esa ausencia y suspende sus respuestas. Finalmente P1 y P3 detectan que **P2 y P4** ya no responden; el estado de falla del grupo se propaga.

En la enumeración d) de impresa 202, el texto nombra a **P1 y P2** como los procesos que no responden mientras P1 y P3 detectan la ausencia. Es una errata: la secuencia y el panel c) señalan a **P4 y P2**. El panel final marca al grupo completo como indisponible. La corrección evita atribuir a P1 una detección de su propio silencio antes de la transición descrita.

## Un enlace averiado puede deshabilitar todo el grupo

**Ejemplo propio.** Cuatro trabajadores deben completar juntos una fase que exige participación de los cuatro. Aunque los cuatro sigan vivos, una partición que separa a uno impide esa tarea conjunta. Propagar indisponibilidad de todo el grupo puede ser apropiado: ninguno debería continuar bajo la ilusión de que los cuatro siguen participando.

Ahora imaginemos un servicio de lectura que podría trabajar con tres de cuatro réplicas. Convertir automáticamente el aislamiento de una en indisponibilidad de todas podría sacrificar servicio innecesariamente. El mecanismo no es universalmente mejor o peor: importa la definición de la unidad que debe fallar junta.

La ventaja es que la propagación no exige que el proceso aislado envíe una explicación legible a cada miembro. La ausencia de comunicación desencadena la reacción prevista. El costo es ampliar el dominio afectado: una dificultad local puede deshabilitar procesos que conservan capacidad de cómputo y enlaces entre sí.

## Qué garantías necesitan un modelo

El libro describe FUSE como una vía de propagación confiable incluso ante patrones de desconexiones y particiones. Eso no elimina las hipótesis necesarias para que los procesos correctos ejecuten sus comprobaciones ni concede un instante global en el que todos conocen lo ocurrido. El efecto es progresivo: cada participante detecta silencio según las reglas y deja de contestar, hasta propagar la condición de falla del grupo.

Los pings siguen requiriendo una política para decidir cuándo la ausencia de respuesta es significativa. Por eso FUSE no es un detector perfecto de caídas físicas en un sistema asíncrono. Cambia la semántica de lo notificado y la manera de propagarlo.

Tampoco es una solución general para impedir cascadas accidentales. Aquí ampliar el efecto es **intencional** porque la aplicación ha definido un grupo que debe funcionar como unidad. Esa intención distingue la propagación prevista de la sobrecarga accidental de réplicas que vimos en la nota 01.

## Comparar el objetivo de cada mecanismo

| Mecanismo | Evidencia principal | Qué añade | Límite que conserva |
|---|---|---|---|
| Plazo fijo | Tiempo sin respuesta o latido | Decisión simple | El retraso puede parecer caída |
| Contadores sin timeout | Avance propagado y rutas | Evidencia indirecta sin plazo fijo en la abstracción | Interpretar avance requiere criterio y supuestos |
| Sondeo indirecto | Respuesta a través de intermediarios | Diversidad de rutas | Intermediarios pueden compartir la misma falla |
| Phi | Rareza temporal respecto de un historial | Escala adaptable | La distribución puede no describir el presente |
| Gossip | Novedades transmitidas por vecinos | Difusión de perspectivas | Vistas atrasadas y costo del contenido |
| FUSE | Silencio provocado en el grupo | Notificación de falla como unidad | Amplía la indisponibilidad a otros miembros |

> [!question]- ¿Por qué FUSE puede informar una falla de grupo aunque solo una máquina esté caída?
> Porque la propiedad vigilada es la posibilidad de operar como grupo. Los demás dejan de contestar para propagar que esa propiedad ya no se cumple. Su silencio no asegura que también se hayan apagado.

**Referencia:** PDF 7–9 · impresas 201–203 · figuras 9-5. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=7|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/09 Detección de fallas/05 Gossip y tablas de latidos|Anterior]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/07 Laboratorio y repaso resuelto|Siguiente]] →
