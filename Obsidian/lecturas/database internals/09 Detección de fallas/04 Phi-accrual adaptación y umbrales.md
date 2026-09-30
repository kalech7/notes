---
title: "Database Internals — Phi-accrual, adaptación y umbrales"
created: 2026-09-30
libro: "Database Internals"
capitulo: 9
tags:
  - lecturas/database-internals
  - arquitectura/deteccion-de-fallas
---

# Phi-accrual, adaptación y umbrales

[[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice del capítulo 9]]

## De una decisión binaria a una escala

Un detector de plazo fijo responde a «¿el silencio superó el plazo?». Un detector **phi-accrual** calcula una escala continua de **sospecha**: qué tan extraño resulta el tiempo sin noticias si los próximos latidos se comportan como los observados recientemente. La aplicación decide qué nivel justifica actuar.

Una **ventana deslizante** conserva un número limitado de muestras recientes. Cuando llega una muestra nueva se añade, y la más antigua sale si se superó el tamaño de ventana. Eso permite estimar el comportamiento reciente sin almacenar toda la vida del proceso. El capítulo presenta una aproximación normal, caracterizada por **media** —intervalo habitual— y **varianza** —dispersión de los intervalos—.

Aunque el libro habla de tiempos de llegada, el cálculo operativo se puede explicar con **intervalos entre llegadas**. Restar dos observaciones consecutivas de un reloj monotónico local produce esos intervalos; no obliga a sincronizar los relojes de las máquinas. Una pausa, pérdida o demora altera las muestras recibidas, por lo que el modelo describe el comportamiento visto por el observador.

## Una fórmula que aclara el significado

La siguiente formulación matemática es una elaboración explicativa del mecanismo, no una ecuación impresa en estas páginas. Si `X` es el intervalo aleatorio modelado y `t` es la espera desde la última llegada, se calcula la cola:

$$
q(t) = P(X > t), \qquad \varphi(t) = -\log_{10} q(t).
$$

Si `q` es grande, esperar al menos ese tiempo es habitual y phi permanece bajo. Si `q` es pequeño, el silencio resulta extraño según el modelo y phi crece. `φ = 3` significa una cola de `10⁻³ = 0,001` en el modelo. **No significa una probabilidad posterior de 99,9 % de que el proceso esté muerto.** Para calcular esa probabilidad se necesitaría modelar también caídas, sus tasas previas y cómo producen observaciones, entre otras hipótesis.

Esta precisión corrige la frase introductoria del capítulo que identifica la escala con probabilidad de caída. La interpretación útil es rareza de la espera bajo una distribución de intervalos, convertida en un número manejable. El modelo puede estar mal ajustado y la cola calculada puede ser diferente de la frecuencia real de retrasos.

![[Obsidian/lecturas/database internals/Recursos visuales/Capítulo 09/03-phi-arquitectura.png]]

Las cajas azules separan medición y cálculo; la caja ámbar aplica el criterio que activa la sospecha. Las tres cajas verdes son ejemplos algebraicos de la correspondencia entre phi y la cola: cada unidad adicional divide esa cola por diez. No son probabilidades medidas ni porcentajes de procesos caídos. Esa separación permite que dos aplicaciones consuman la misma evidencia con umbrales diferentes.

## Un cálculo propio con distribución normal

Supongamos intervalos con media `μ = 100 ms` y desviación estándar `σ = 20 ms`. La desviación estándar es la raíz de la varianza y conserva la unidad de milisegundos. Para una espera de `140 ms`, el valor normalizado es:

$$
z = \frac{140-100}{20}=2.
$$

La cola de una normal estándar por encima de 2 es aproximadamente `0,02275`. Entonces `φ ≈ −log₁₀(0,02275) ≈ 1,643`. Con un umbral de 3 todavía no hay sospecha. A `160 ms`, `z = 3`, la cola es aproximadamente `0,00135` y `φ ≈ 2,870`. El umbral 3 se cruza alrededor de `161,8 ms` en este modelo simplificado.

Ahora imaginemos que las muestras recientes pertenecen a una red más lenta y variable: `μ = 150 ms`, `σ = 50 ms`. Esperar `160 ms` da `z = 0,2`, cola aproximada `0,42074` y `φ ≈ 0,376`. El mismo silencio es menos excepcional. La adaptación está en la distribución aprendida, no en una afirmación de que el proceso ya no puede fallar.

Estos valores son un ejemplo matemático inventado. Las implementaciones reales pueden imponer dispersión mínima, márgenes para pausas, requisitos de calentamiento y métodos distintos de estimación. No se presentan aquí valores de configuración universales.

## Monitoreo, interpretación y acción

**Monitoreo** recoge muestras mediante latidos, pings o respuestas. **Interpretación** decide si el nivel supera un criterio. **Acción** ejecuta la consecuencia, como informar a la aplicación, retirar una ruta o iniciar otra comprobación. Una interfaz que entregue phi permite ajustar la interpretación sin cambiar la medición.

Un umbral bajo reacciona a silencios moderadamente extraños; un umbral alto espera evidencia temporal más extrema. En ambos casos, una caída real termina produciendo creciente silencio si el observador sigue ejecutándose y el historial no se rejuvenece con señales falsas. Pero eso no fija por sí solo una demora máxima universal.

## Dónde puede equivocarse la adaptación

Una ventana corta sigue rápidamente cambios, pero puede estimar mal la distribución por tener pocas muestras. Una larga reduce algunas fluctuaciones y puede conservar demasiado tiempo condiciones antiguas. Una demora súbita puede generar una sospecha antes de que haya suficientes muestras del nuevo régimen. Y si la red empeora progresivamente, aprender una distribución cada vez más lenta puede retrasar la detección.

La hipótesis normal es un modelo, no un hecho sobre redes. Retrasos con colas pesadas, pérdidas y pausas grandes pueden violarla. Cerca de una varianza cero, hace falta evitar una división imposible o excesiva confianza; el laboratorio usa una dispersión positiva fijada explícitamente. Un número phi preciso no repara datos insuficientes.

> [!question]- ¿Por qué dos consumidores pueden actuar con umbrales distintos?
> Porque tienen diferentes costos de equivocación y demora. Uno puede usar una sospecha temprana para desviar una consulta reversible, y otro esperar más antes de ejecutar una recuperación costosa. Ambos deben proteger sus efectos con reglas propias de seguridad.

**Referencia:** PDF 5–6 · impresas 199–200. [[Obsidian/lecturas/database internals/Materiales/09 a 11 Detección de fallas liderazgo y replicación.pdf#page=5|PDF de consulta]].

---

← [[Obsidian/lecturas/database internals/09 Detección de fallas/03 Contadores sin timeout y sondeos indirectos|Anterior]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/00 Índice|Índice]] · [[Obsidian/lecturas/database internals/09 Detección de fallas/05 Gossip y tablas de latidos|Siguiente]] →
