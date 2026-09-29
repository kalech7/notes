---
title: "Latencia ancho de banda y costo"
created: 2026-09-28
capitulo: 9
tags:
  - lecturas/software-architecture
  - arquitectura/estilos
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/00 Índice|← Índice del capítulo 9]]

# Latencia, ancho de banda y costo

Las falacias 2, 3 y 7 distinguen tres recursos: **tiempo de espera, capacidad de transferencia y dinero**. Son relacionados, pero no intercambiables. Una llamada rápida puede ser cara; una red con gran capacidad puede presentar alta latencia; reducir datos puede aliviar saturación sin eliminar cada viaje remoto.

## 1. Latencia: lo remoto no cuesta lo mismo que lo local

Una llamada local suele evitar serialización, transporte y esperas de red. Una remota añade esos pasos y puede esperar en colas del cliente, red o servidor. El capítulo compara órdenes de magnitud de llamadas locales y remotas, no ofrece una medición universal para todo equipo.

Para un recorrido **secuencial**, un modelo útil es:

$$
T_{total} = T_{trabajo\ local} + \sum_{i=1}^{n} T_{llamada\ remota,i}
$$

Hay que fijar qué incluye cada término. Si se mide de extremo a extremo una llamada remota, ya puede incluir espera, transporte y procesamiento del destino; no se deben sumar esas partes de nuevo.

**Ejemplo del capítulo, explicitado:** diez llamadas secuenciales con 100 ms cada una añaden aproximadamente 1.000 ms. A eso se añade el trabajo no incluido en esas mediciones. Si las llamadas son independientes y se ejecutan en paralelo, el modelo temporal cambia: el tramo suele esperar a la más lenta, más los costos de coordinación. No es correcto sumar diez llamadas como si fueran secuenciales cuando no lo son.

**Fuente:** PDF pp. 15–16, impresas 144–145, figura 9-8.

## 2. El promedio no describe la experiencia de todos

La **mediana** representa el punto bajo el que queda aproximadamente la mitad de las observaciones. El **p95** es un umbral que aproximadamente el 95 % no supera; el 5 % restante puede ser mucho más lento. El **p99** concentra la atención en una cola todavía más extrema.

El ejemplo del libro contrapone una media de 60 ms con un p95 de 400 ms. Eso puede coexistir: pocos casos lentos quedan diluidos en la media. Tampoco se puede obtener el p95 de una cadena sumando automáticamente los p95 de cada servicio. Los percentiles de una suma dependen de distribuciones y correlaciones; hay que medir el recorrido completo.

**Ejercicio propio.** El negocio exige respuesta en menos de 500 ms para el 95 % de solicitudes. Hay ocho llamadas secuenciales cuyo tiempo medio observado es 70 ms, más 50 ms de trabajo local. La media estimada sería 610 ms. Ya hay evidencia de que el diseño necesita investigación, pero ese cálculo no determina el p95. Se debe medir el recorrido con carga representativa y considerar reducir viajes, agrupar consultas, cambiar coordinación u optimizar el tramo dominante.

![Latencia acumulada y transferencia de datos](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c09-03-latencia-datos.png)

La parte temporal de la imagen muestra cómo una cadena secuencial acumula viajes. La parte de datos compara enviar un perfil completo con enviar el dato necesario, a una misma frecuencia de solicitudes. Las dos partes usan unidades distintas: los milisegundos miden duración y los bytes por segundo miden tasa. Es una elaboración propia de los ejemplos de las impresas 145–146.

Las cifras son cálculos de escenario, no mediciones de producción. No incluyen todos los encabezados, retransmisiones, compresión ni trabajo de procesamiento. El efecto final sobre la latencia requiere ensayo.

## 3. Ancho de banda: un contrato demasiado amplio tiene costo multiplicado

El capítulo describe un servicio de listas de deseos que necesita el nombre del cliente, pero recibe un perfil de 45 atributos. Este caso ejemplifica **stamp coupling**: transferir una estructura amplia cuando el consumidor utiliza una fracción.

La cuenta dimensional básica es:

$$
\text{tasa de datos} = \text{bytes por respuesta} \times \text{respuestas por segundo}
$$

Usando unidades decimales y las cifras del libro:

| Contrato | Cálculo a 2.000 respuestas/s | Tasa de carga útil |
|---|---|---|
| Perfil de 500 kB | 500.000 B × 2.000/s | 1.000.000.000 B/s = 1 GB/s = 8 Gbit/s |
| Nombre de 200 B | 200 B × 2.000/s | 400.000 B/s = 400 kB/s = 3,2 Mbit/s |

La reducción del volumen de carga útil es de **2.500 veces**. No significa que toda la aplicación se vuelva 2.500 veces más rápida: existen costos fijos y otros tramos.

> [!important] Corrección de unidades del escaneo
> La impresa 146 expresa el caso reducido como 400 Kbps. Esa cifra confunde bytes con bits: con 200 bytes y 2.000 respuestas por segundo, el resultado es 400 kB/s, equivalentes a 3,2 Mbit/s. Además, 1 GB/s corresponde al tráfico agregado de todas esas respuestas, no al tamaño de una sola llamada. Se conserva el ejemplo y se corrige la aritmética dimensional.

Si las cifras originales usaran unidades binarias, habría que declarar KiB/GiB y recalcular coherentemente; estas notas usan decimales para que todas las operaciones sean verificables.

## 4. Reducir datos sin crear otro problema

El libro propone alternativas como endpoints internos específicos, selección de campos, GraphQL, contratos guiados por el valor requerido y contratos de consumidores, o mensajería interna. La idea común es transmitir lo necesario.

**Compensaciones propias para evaluar:**

- Un endpoint específico simplifica el consumidor, pero demasiadas variantes dificultan mantener la API.
- Seleccionar campos reduce transferencia, pero necesita reglas claras sobre acceso y costo de consulta.
- Un contrato orientado al consumidor explicita necesidades, pero exige coordinar evolución y pruebas.
- Una copia local evita viajes en ciertos recorridos, pero introduce actualización y decisiones de consistencia; es una alternativa didáctica adicional, no una solución gratuita.

**Fuente:** PDF pp. 16–17, impresas 145–146, figura 9-9.

## 5. Costo de transporte: la séptima falacia habla de dinero

La falacia 7 se refiere al costo económico de infraestructura y operación de la comunicación. El libro menciona servidores, gateways, firewalls, subredes y proxies. Aumentar unidades remotas puede requerir capacidad y administración que no estaban disponibles.

**Ejemplo propio:** un equipo decide separar Catálogo para poder escalar sus lecturas. Su comparación debe incluir cómputo, red, observabilidad y horas de operación, además del ahorro por escalar esa parte. El costo incremental puede compensarse con un beneficio de negocio; simplemente debe hacerse explícito.

Un inventario antes de distribuir incluye capacidad, latencia, transferencia y zonas de seguridad. No se trata de asumir que todo servicio nuevo será caro en la misma proporción: se trata de estimar el costo total para la topología concreta.

**Fuente:** PDF pp. 19–20, impresas 148–149, figura 9-13.

> [!question] ¿Más ancho de banda elimina la latencia?
> Puede reducir espera debida a saturación, pero no elimina propagación, viajes, procesamiento ni coordinación.

> [!question] ¿400 kB/s es lo mismo que 400 kbit/s?
> No. Un byte son ocho bits. 400 kB/s equivalen a 3.200 kbit/s con prefijos decimales.

> [!question] ¿Puedo sumar p95 de servicios para obtener p95 del pedido?
> No como regla general. Mide el recorrido completo y conserva el contexto de carga, población y errores.

## Fuente principal

- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/06 Fundamentos de estilos arquitectónicos.pdf#page=15|Fundamentals of Software Architecture, 2.ª ed., capítulo 9, PDF pp. 15–17; impresas 144–146]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/06 Fundamentos de estilos arquitectónicos.pdf#page=19|Fundamentals of Software Architecture, 2.ª ed., capítulo 9, PDF pp. 19–20; impresas 148–149]].

Las explicaciones, diagramas y ejemplos identificados como propios son elaboraciones didácticas; las páginas indicadas permiten contrastar los conceptos con el escaneo.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/04 Monolitos distribución y fiabilidad|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/06 Seguridad topología y coordinación|Siguiente →]]
