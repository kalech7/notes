---
title: "Database Internals — Modelos de fallas y tolerancia"
created: 2026-09-30
libro: "Database Internals"
capitulo: 8
tags:
  - lecturas/database-internals
  - arquitectura/sistemas-distribuidos
---

# Modelos de fallas y tolerancia

[[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice del capítulo 8]]

Un algoritmo solo puede prometer tolerancia a los fallos que su modelo contempla. Decir «aguanta que algo falle» resulta insuficiente: detenerse, olvidar mensajes y enviar valores contradictorios son comportamientos diferentes.

## Caída definitiva y recuperación

En **crash-stop**, un proceso deja de ejecutar y participar en la instancia del algoritmo. La prueba de corrección no se apoya en que vuelva. Eso no impide reparar físicamente la máquina ni incorporarla después mediante un procedimiento distinto; no permite introducir su retorno como si la instancia original hubiese modelado recuperación.

En **crash-recovery**, el proceso puede detenerse y volver a ejecutar. El diseño debe distinguir estado **volátil**, que se pierde al caer, y estado **durable**, que conserva las decisiones necesarias para recuperarse. Si un servidor olvida IDs de cobro después de reiniciar, la deduplicación solo funcionó durante su vida anterior. Persistirlos junto al efecto evita ese olvido en el modelo del laboratorio.

Cambiar arbitrariamente la identidad del proceso recuperado no vuelve equivalentes los modelos. Una identidad nueva puede alterar quién pertenece al grupo o cuántos fallos permite el protocolo. Debe existir una regla de membresía y reintegración compatible con esas garantías.

## Omisiones y comportamiento arbitrario

Una **falla por omisión** deja sin ejecutar o sin comunicar un paso esperado: no enviar, no recibir o perder un mensaje. Una partición puede modelarse como omisiones entre grupos. Una caída se parece desde fuera a omitir toda comunicación; un proceso lento puede parecer omitente frente a un plazo, aunque no haya dejado de funcionar.

Una **falla arbitraria o bizantina** permite comportamiento contrario al protocolo: valores inválidos, mensajes incompatibles para destinatarios distintos o engaño deliberado. No requiere un atacante: un bug o incompatibilidad puede causar ese comportamiento. Un algoritmo que tolera silencios no necesariamente tolera respuestas falsas.

| Modelo | Comportamiento permitido del participante que falla | Pregunta de diseño |
|---|---|---|
| Crash-stop | Se detiene y no vuelve a la instancia | ¿Pueden progresar los restantes sin él? |
| Crash-recovery | Se detiene y vuelve con parte del estado | ¿Qué información debe sobrevivir? |
| Omisión | Falta un paso o una comunicación | ¿Cómo se reintenta sin duplicar efectos? |
| Bizantino | Puede enviar resultados arbitrarios | ¿Cómo validar y resistir contradicciones? |

El libro cita aeronáutica y criptomonedas como contextos donde interesan fallas bizantinas. No son una lista exclusiva ni significan que todo sistema de esos campos use el mismo protocolo. Tampoco hay un único número universal de réplicas: las cotas dependen del tipo de fallo, autenticación, sincronía y algoritmo.

## Redundancia oculta fallos bajo condiciones

**Enmascarar un fallo** significa que el servicio conserva su comportamiento observable pese a que un componente falle. Introducir varios participantes permite hacerlo solo si existe un protocolo que use correctamente las copias y si el fallo está dentro de lo soportado. Copiar datos corruptos sin validarlos puede multiplicar el problema.

La ruta de recuperación suele consumir más recursos y tiempo que la ruta normal. El sistema debe reservar capacidad y aceptar que una degradación de rendimiento pueda coexistir con corrección. Revisiones de software y pruebas reducen errores; reintentos y timeouts ayudan a comunicar, pero no convierten por sí solos toda ejecución en correcta.

El resumen del capítulo junta las piezas: enlaces imperfectos, procesos que caen y redes particionadas exigen vocabulario y contratos explícitos. El libro indica que muchos de sus siguientes algoritmos se enfocan en caídas; no debemos atribuirles por extensión tolerancia bizantina.

> [!question]- ¿Tres réplicas convierten cualquier algoritmo en tolerante a fallas bizantinas?
> No. La cantidad sin el protocolo ni las hipótesis no dice qué garantía existe. Además de almacenar copias, hay que establecer cómo validar mensajes, resolver contradicciones y decidir bajo el modelo previsto.

**Referencia:** PDF 24–26 · impresas 191–193. [[Obsidian/lecturas/database internals/Materiales/08 Sistemas distribuidos.pdf#page=24|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/10 Consenso FLP y sincronía|Anterior]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/08 Introducción a sistemas distribuidos/12 Laboratorio y repaso resuelto|Siguiente]] →
