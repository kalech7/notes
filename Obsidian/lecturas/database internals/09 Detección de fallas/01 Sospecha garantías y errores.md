---
title: "Database Internals — Sospecha, garantías y errores"
created: 2026-09-30
libro: "Database Internals"
capitulo: 9
tags:
  - lecturas/database-internals
  - arquitectura/deteccion-de-fallas
---

# Sospecha, garantías y errores

[[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice del capítulo 9]]

## Qué puede observar realmente un detector

Un **proceso** es una ejecución con estado propio: por ejemplo, el servicio que atiende peticiones de una réplica. Una **caída** significa que deja de ejecutar sus pasos. Un **enlace** es el medio de comunicación entre procesos. El proceso puede seguir vivo aunque un enlace pierda mensajes, o estar sano y responder tarde porque está esperando CPU, disco o una cola.

Un **detector de fallas** es un componente local que recopila esas observaciones y produce información para otros algoritmos. Es local porque A y C pueden tener diferentes noticias acerca de B. A no dispone de acceso inmediato al estado físico de B: observa mensajes que llegan, respuestas que faltan y conocimiento transmitido por terceros.

En un sistema **asíncrono** no hay una cota temporal disponible que permita concluir que todo proceso correcto ya habría respondido. Si A lleva cinco segundos esperando, las ejecuciones «B cayó» y «B sigue trabajando pero su respuesta tarda seis segundos» son compatibles con la observación de A. Aumentar la espera reduce algunas equivocaciones prácticas, pero no convierte el silencio en prueba lógica bajo ese modelo.

Conviene reservar **sospechoso** para el proceso cuya comunicación ya no satisface un criterio operativo. **Caído** describe lo que realmente ocurrió. La aplicación puede dejar de enviar tráfico a un sospechoso para evitar tiempos de espera repetidos, sin afirmar que conoce la causa física.

## Dos errores y sus consecuencias

Aquí la clase positiva significa «se detecta una falla». Esta convención importa porque otras métricas podrían llamar positivo a «sano» y cambiar los nombres.

| Realidad | Decisión local | Resultado | Consecuencia típica |
|---|---|---|---|
| B cayó | A sospecha de B | Detección acertada | Puede empezar la recuperación |
| B sigue operativo | A sospecha de B | Falso positivo | Se pierde capacidad o se inicia recuperación innecesaria |
| B cayó | A todavía confía en B | Falso negativo durante ese período | Se siguen acumulando esperas y trabajo inútil |
| B sigue operativo | A conserva confianza | Decisión acertada | Continúa el trabajo normal |

**Ejemplo propio.** Un servicio de consultas tiene tres réplicas. Si una réplica realmente cae y se mantiene en el balanceo, una parte del tráfico agotará plazos. Si el detector retira por error una réplica sana, las otras dos reciben más carga. Esa carga extra puede generar nuevas demoras y nuevas sospechas: una mala decisión local puede convertirse en una cascada. Por eso importa medir tanto cuánto tarda la detección como cuánto trabajo induce una equivocación.

## Vivacidad, seguridad, completitud y exactitud

**Vivacidad** expresa que finalmente ocurre el progreso previsto. Para un detector, una propiedad de progreso es que una caída termine siendo observada. **Seguridad** expresa que nunca ocurre un resultado prohibido. En un detector ideal, no acusar a procesos correctos sería una propiedad de ese tipo. Un detector práctico que admite sospechas falsas no satisface esa prohibición absoluta.

La **completitud** trata de no dejar invisibles las caídas. La forma fuerte mencionada por el capítulo busca que todos los procesos correctos terminen sospechando de todo proceso que cayó. «Eventualmente» no da un número de milisegundos; necesita las condiciones de conectividad y ejecución de su modelo. La **exactitud** trata de no sospechar incorrectamente de procesos correctos. Hay diferentes clases formales de exactitud y completitud; este capítulo no desarrolla toda su taxonomía.

El libro también usa exactitud en sentido operativo, incluyendo aciertos y errores de ambos tipos. Es útil distinguir ese uso cotidiano de la propiedad formal de no acusar a un proceso correcto. La **eficiencia temporal** pregunta cuánto tarda el detector en reaccionar; el costo de mensajes y memoria es otra dimensión de eficiencia.

Si el detector baja su plazo, suele reaccionar más pronto a una caída y aumenta la oportunidad de acusar a una réplica lenta. Si lo sube, suele tolerar más variación y demora la recuperación. Son tendencias de diseño, no una ley que impida mejorar simultáneamente ambos resultados al añadir mejor evidencia.

## Cómo conservar seguridad con sospechas imperfectas

La seguridad del sistema completo no debe depender de que cada sospecha sea correcta. Si A cree que el líder B cayó, puede **iniciar una elección**, pero no basta ese pensamiento para que A tenga autoridad para aceptar cualquier escritura. El protocolo debe establecer cómo se concede y revoca esa autoridad, y cómo se impide que una respuesta antigua produzca un efecto incompatible.

El resumen conecta esto con FLP. Su formulación abreviada de que «no se puede garantizar consenso asíncrono» necesita los supuestos: consenso determinista, posibilidad de una caída y exigencia de terminación en toda ejecución admisible. No prohíbe decidir en ejecuciones habituales ni afirma que un timeout resuelva automáticamente el problema. Un detector con propiedades adicionales aumenta la información disponible para el protocolo; la clase de esas propiedades determina qué progreso se puede garantizar.

El resumen menciona que algunos resultados de consenso admiten un detector que comete infinitos errores. Esto no significa que cualquier detector arbitrario sirva. Un ejemplo de condición relevante es que finalmente exista algún proceso correcto al que los demás dejen de acusar, aunque continúen acusando equivocadamente a otros. Junto con la completitud exigida por el protocolo, una estabilidad parcial de esa clase puede permitir progreso. El capítulo cita ese resultado como orientación teórica y no presenta su demostración.

Los algoritmos del capítulo presuponen **ausencia de comportamiento bizantino**: los procesos no fabrican deliberadamente mentiras sobre su estado o el de sus vecinos. Una réplica que contesta al heartbeat y corrompe resultados requiere otro análisis; «responde» y «hace bien su trabajo» son predicados distintos.

> [!question]- ¿Puede A tener razón al dejar de usar B aunque B esté vivo?
> Sí. Si A no puede alcanzar a B a tiempo para la operación, retirar temporalmente esa ruta puede ser útil. Pero esa decisión expresa disponibilidad desde A, no prueba una caída global ni concede a A nueva autoridad sobre datos compartidos.

**Referencia:** PDF 1–2 · impresas 195–196. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=1|PDF de consulta]]. El vínculo con consenso se retoma en PDF 8–9 · impresas 202–203.

---

← [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Anterior]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/02 Pings heartbeats y plazos|Siguiente]] →
