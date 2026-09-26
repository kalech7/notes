---
title: "Capítulo 4 · Características arquitectónicas · Rendimiento escalabilidad y elasticidad"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 4
orden: 4
---

# Rendimiento escalabilidad y elasticidad

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 4 · Características arquitectónicas](00%20%C3%8Dndice.md) → Nota 4 de 7

**Objetivo:** Medir latencias, percentiles, capacidad y adaptación.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 4. Rendimiento: medir la experiencia que se quiere proteger

![Latencia de una operación, throughput de resultados completados y escalabilidad con más recursos](../Recursos%20visuales/12-rendimiento-y-capacidad.png)

**Cómo leer la imagen:** a la izquierda seguimos un pedido desde su inicio hasta su resultado: latencia. En el centro contamos resultados terminados durante un intervalo: throughput. A la derecha aumentamos recursos, pero estos siguen compartiendo un paso: el cuello de botella puede limitar la mejora. Tres cocineros no garantizan tres veces más capacidad, y el único sándwich final es un símbolo del recurso compartido, no un resultado cuantitativo. En software hay que definir las fronteras de la operación y medir la carga real.

**Ampliación didáctica.** La latencia es el tiempo entre dos eventos definidos; por ejemplo, enviar una compra y recibir su confirmación. El *throughput* es trabajo completado por unidad de tiempo, como pedidos por segundo. La capacidad es el máximo volumen sostenible **bajo condiciones y objetivos definidos**; puede expresarse en solicitudes por segundo, usuarios concurrentes o almacenamiento según la pregunta.

Un sistema que completa muchas respuestas de error tiene throughput, pero quizá casi ningún pedido útil. Por eso deben fijarse operación, carga, mezcla de solicitudes, tamaño de datos, errores y ventana de medición.

### Promedio y p95 cuentan historias diferentes

Supongamos 1.000 solicitudes: 950 tardan 100 ms y 50 tardan 2.000 ms. El promedio es:

$$
\bar{x}=\frac{950(100)+50(2000)}{1000}=195\ \text{ms}.
$$

Usando el percentil por **rango más próximo**, ordenamos las observaciones y definimos:

$$
p_{95}=x_{(\lceil0{,}95n\rceil)}.
$$

Aquí p95 = 100 ms y p99 = 2.000 ms. El promedio oculta cómo se distribuye la espera; p95 tampoco protege al 5 % restante. Diferentes herramientas interpolan percentiles de otra manera: hay que acordar el método. No se obtiene el p95 global promediando los p95 de servidores.

Un objetivo inventado sería «p95 ≤ 300 ms para confirmar compras con 100 solicitudes/s durante 20 minutos, y errores ≤ 0,1 %». Debe precisarse cómo se contabilizan tiempos de espera agotados: excluirlos puede hacer que una caída parezca una mejora.

### Colas, recursos y límites

Cuando las llegadas superan la capacidad de finalización, se acumula trabajo. Para un sistema estable, con fronteras consistentes y promedios de largo plazo, la ley de Little relaciona concurrencia media, throughput y tiempo medio dentro del sistema:

$$
L=\lambda W.
$$

Si se completan 80 pedidos/s y cada pedido permanece 0,25 s de media, hay 20 pedidos en curso de media. Esto incluye espera dentro de la frontera elegida; no implica 20 hilos ni permite sustituir el promedio por p95. Tampoco describe un régimen estable si la cola crece indefinidamente.

### Escalabilidad y elasticidad

Escalabilidad pregunta si más recursos permiten sostener más carga. Elasticidad pregunta cómo se ajustan recursos a las subidas **y bajadas**, con qué demora y desperdicio. Crecer verticalmente aumenta recursos de una instancia; horizontalmente añade instancias.

![Escalabilidad y elasticidad ](../Recursos%20visuales/Diagramas/cap04-diagrama-02.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap04-diagrama-02.mmd)

**Interpretación:** la elasticidad implica un ciclo de ajuste, no únicamente crecimiento. **Límite:** el diagrama omite tiempos de arranque, cuotas, estados y cuellos de botella que pueden impedir una respuesta útil.

Si una instancia sostiene 50 solicitudes/s y cuatro sostienen 160 bajo el mismo objetivo, el factor de escalado es 160/50 = 3,2; la eficiencia respecto del escalado lineal es 3,2/4 = 80 %. No demuestra que ocho alcancen 320. Si las nuevas instancias tardan tres minutos en arrancar, pueden llegar después de un pico de dos minutos: existe escalabilidad, pero la elasticidad resulta insuficiente para ese escenario.

![escalabilidad elasticidad](../Recursos%20visuales/06-escalabilidad-elasticidad.png)

*Figura original con datos hipotéticos independientes del ejemplo anterior: a la izquierda se compara capacidad con recursos; a la derecha, demanda y capacidad a lo largo del día.*

---

**Anterior:** [Familias ISO y terminología](03%20Familias%20ISO%20y%20terminolog%C3%ADa.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Disponibilidad fiabilidad y recuperación](05%20Disponibilidad%20fiabilidad%20y%20recuperaci%C3%B3n.md)
