---
title: "Database Internals — Laboratorio y repaso resuelto"
created: 2026-09-30
libro: "Database Internals"
capitulo: 9
tags:
  - lecturas/database-internals
  - arquitectura/deteccion-de-fallas
---

# Laboratorio y repaso resuelto

[[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice del capítulo 9]]

Los ejercicios siguientes son **elaboración propia**. Usan reglas pequeñas y explícitas para practicar lo explicado; no son una implementación productiva de SWIM, phi-accrual o FUSE.

## 1. Medir el costo de una sospecha falsa

A inicia un ping a B en `t = 0 ms`. Su plazo es `200 ms`. B recibe el mensaje y produce un ACK que solo llega a A en `t = 320 ms`. A procesa sus timers sin pausa. La aplicación conserva el estado sospechoso hasta recibir nueva evidencia de B y entonces lo revisa.

> [!question]- ¿B necesariamente cayó? ¿En qué intervalo A sospecha?
> No. El enunciado indica que B produjo una respuesta. A sospecha desde 200 ms hasta recibir y procesar el ACK a 320 ms. El intervalo dura `320 − 200 = 120 ms`. La política de revisar la sospecha al recibir el ACK es un supuesto de este ejercicio, no una regla universal para toda aplicación.

> [!question]- Si A envía cada 500 ms y B cae después de un ACK, ¿cuánto tarda la detección nominal?
> Bajo programación ideal, desde una caída justo antes del próximo ping hasta una caída justo después del anterior, el rango se acerca a `200 ms`–`500 + 200 = 700 ms`. Si A también se pausa, el rango ya no es una cota del tiempo real.

## 2. Sondear mediante un intermediario

El ACK directo B→A se pierde. C puede enviar a B y recibe su ACK. C informa el resultado a A.

> [!question]- ¿Qué cambia frente al silencio de la ruta directa?
> Hay evidencia positiva reciente de que B responde mediante C. A puede evitar una acusación basada solo en A–B. La evidencia no demuestra salud de todos los enlaces ni que una operación de negocio se haya confirmado.

> [!question]- Si C y D tampoco logran contactar a B, ¿ya existe una prueba de caída?
> No bajo el modelo asíncrono. Ambos pueden compartir un enlace, una región o una partición. Existe evidencia suficiente para una sospecha según cierta política, y la acción posterior debe tolerar que B continúe vivo.

## 3. Calcular phi y cambiar el modelo

Suponemos una normal de intervalos con media 100 ms y desviación estándar 20 ms. La cola se obtiene con la función complementaria de error, disponible en la biblioteca estándar de Python:

```python
import math

def phi_normal(espera_ms, media_ms, desviacion_ms):
    if desviacion_ms <= 0:
        raise ValueError("La dispersión debe ser positiva")
    z = (espera_ms - media_ms) / desviacion_ms
    cola = 0.5 * math.erfc(z / math.sqrt(2.0))
    return -math.log10(max(cola, 1e-300))
```

El piso `1e-300` evita calcular el logaritmo de cero por limitaciones numéricas; no es una probabilidad estimada por el modelo. Este ejercicio fija media y desviación para concentrarse en la interpretación. No simula una ventana que aprende de datos.

| Espera | Media | Desviación | Phi aproximado | Sospecha con umbral 3 |
|---|---|---|---|---|
| 100 ms | 100 ms | 20 ms | 0,301 | No |
| 140 ms | 100 ms | 20 ms | 1,643 | No |
| 160 ms | 100 ms | 20 ms | 2,870 | No |
| 180 ms | 100 ms | 20 ms | 4,499 | Sí |
| 160 ms | 150 ms | 50 ms | 0,376 | No |

> [!question]- ¿Qué significa el valor 4,499 de la cuarta fila?
> La cola normal calculada para esperar más de 180 ms es aproximadamente `3,167 × 10⁻⁵`. Su logaritmo decimal negativo es 4,499. El silencio es muy extraño bajo el modelo; no se ha calculado una probabilidad posterior de que el proceso esté muerto.

> [!question]- ¿Por qué la última fila baja tanto pese a esperar los mismos 160 ms?
> El historial modelado es más lento y variable. `z = (160 − 150)/50 = 0,2`; una espera superior a ese valor no es rara, con cola aproximadamente 0,42074. La comparación depende de la distribución, no solo del número de milisegundos.

Puede ejecutarse [[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 09/laboratorio.py|el laboratorio reproducible]] con Python 3. Usa solo la biblioteca estándar y muestra esos cálculos, una mezcla de gossip y una propagación FUSE simplificada.

## 4. Evitar que gossip vuelva inmortal a un miembro caído

A tiene guardado para C el contador 41 y `ultimo_avance = 0 s`. B envía a A estas observaciones: en `2 s` informa 42; en `4 s` vuelve a informar 42; en `6 s` informa 40. El detector usa un plazo de 5 s desde que incorpora evidencia de avance.

> [!question]- ¿Cómo queda la tabla de A después de cada mensaje?
> A los 2 s guarda 42 y actualiza `ultimo_avance` a 2 s. A los 4 s conserva ambos campos porque 42 es repetido. A los 6 s conserva ambos porque 40 es anterior. Para esta misma ejecución de C, el contador debe avanzar para rejuvenecer la evidencia.

> [!question]- ¿Qué decide A a los 7,1 s si no hay más novedades?
> Han pasado `7,1 − 2 = 5,1 s` sin avance, por encima del plazo de 5 s. A sospecha de C aunque haya recibido tablas de B a los 4 y 6 s. Si C reinicia sus contadores, hace falta distinguir su nueva ejecución; este ejercicio fija una sola generación.

## 5. Separar mensajes de bytes

Cada uno de 100 miembros envía una tabla completa una vez por ronda. Cada entrada ocupa 24 bytes y cada tabla tiene 100 entradas. Se ignoran las cabeceras.

> [!question]- ¿Cuántos mensajes y bytes se envían por ronda? ¿Qué ocurre al duplicar miembros?
> Hay 100 mensajes de 2 400 bytes cada uno: 240 000 bytes por ronda. Con 200 miembros hay 200 mensajes de 4 800 bytes: 960 000 bytes. El número de mensajes crece linealmente en este modelo y el volumen de bytes cuadráticamente.

## 6. Reconstruir FUSE

B deja de responder. D consulta a B y, al detectar ausencia, suspende sus propias respuestas. A y C detectan a D ausente y también suspenden respuestas. Definimos los cuatro como una unidad obligatoria para cierta tarea.

> [!question]- ¿Cuántos procesos se apagaron físicamente según el enunciado?
> Solo B. Los otros siguen ejecutando la conducta del protocolo, pero dejan de contestar para propagar la indisponibilidad del grupo. No hay evidencia de que D, A y C hayan sufrido una caída física.

> [!question]- ¿Conviene la misma política a lecturas que solo requieren tres réplicas?
> No necesariamente. La política modela una unidad indivisible. Si la aplicación admite operar con tres de cuatro, una regla que retire a los cuatro podría reducir disponibilidad innecesariamente. La semántica del grupo debe corresponder a la tarea.

## 7. Elegir evidencia y proteger la acción

| Necesidad de un escenario propio | Mecanismo útil | Regla que falta resolver |
|---|---|---|
| Desviar temporalmente consultas de una ruta lenta | Plazo o phi | Cómo volver a habilitar la ruta y tolerar respuestas tardías |
| Distinguir un camino roto de un miembro sin respuesta por otras rutas | Sondeo indirecto | Qué intermediarios elegir y cómo caduca la confirmación |
| Distribuir novedades entre muchos participantes | Gossip | Frescura, tamaño del contenido e identidad tras reinicio |
| Abandonar una tarea que exige todos los miembros | Notificación de grupo tipo FUSE | Definición del grupo y condición de recuperación |
| Reemplazar un líder que parece caído | Detector que active la elección | Autoridad, épocas y protección frente a un líder antiguo |

La elección de un detector se evalúa junto con sus consumidores. La pregunta decisiva no es solo «¿cuándo sospecha?», sino también «¿qué efectos ejecutamos al sospechar y siguen siendo seguros si el ausente vuelve a responder?».

**Referencia:** PDF 1–9 · impresas 195–203. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=1|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/09 Detección de fallas/06 FUSE y propagación del silencio|Anterior]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/10 Elección de líder/00 Índice|Siguiente: capítulo 10]] →
