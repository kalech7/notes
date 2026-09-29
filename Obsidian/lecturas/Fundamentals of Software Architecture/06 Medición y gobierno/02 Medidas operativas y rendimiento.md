---
title: "06 · Medidas operativas: promedios, colas y presupuestos"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/medicion
---

# Medidas operativas: promedios, colas y presupuestos

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, capítulo 6. **PDF 2–3 · impresas 82–83** del [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf|PDF conservado]]. «Libro» identifica sus planteamientos; las ampliaciones, plantillas y datos supuestos se señalan como elaboración didáctica.

## 1. ¿Qué estamos midiendo y para qué?

Las **características operativas** describen cómo se comporta un sistema mientras está funcionando. Por ejemplo:

- **Tiempo de respuesta:** ¿cuánto tarda en responder una petición?
- **Capacidad de atender tráfico:** ¿cuántas peticiones procesa por segundo?
- **Consumo de recursos:** ¿cuánta memoria o CPU utiliza?

Imagina una tienda en línea. No basta con decir «la tienda es rápida»: buscar un producto puede ser rápido y pagar puede ser lento. Además, una misma operación puede funcionar bien para muchos usuarios y mal para unos pocos.

Por eso, antes de medir, hay que concretar **qué operación observamos, desde dónde la medimos y durante cuánto tiempo**.

> [!example] Ejemplo didáctico
> «Mediremos cuánto tarda el servidor en responder las peticiones de búsqueda recibidas entre las 10:00 y las 10:05».
>
> Esto es más preciso que «mediremos la velocidad de la aplicación». Todavía no estamos midiendo cuánto tarda el usuario en ver los resultados en su pantalla.

**Idea central de la nota:** una cifra puede ser correcta y, aun así, no contar toda la historia. Hay que elegir medidas que respondan a la necesidad real.

## 2. El promedio puede esconder las peticiones lentas

El **promedio o media** se calcula sumando todos los tiempos y dividiendo entre el número de peticiones. Sirve para resumir los datos, pero no indica que todas las peticiones hayan tardado algo parecido.

El libro plantea el problema de una minoría de peticiones que tarda diez veces más que las demás. Para entenderlo, usaremos estos **datos inventados**:

| Grupo | Cantidad de peticiones | Tiempo de cada petición |
|---|---:|---:|
| Rápidas | 990 | 100 ms = 0,1 segundos |
| Lentas | 10 | 1 000 ms = 1 segundo |
| **Total** | **1 000** | No todas tardan lo mismo |

![Latencia de 990 peticiones rápidas y 10 lentas frente a la media](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c06-02-cola-latencia.png)

La altura de cada columna representa el tiempo de respuesta; el rótulo inferior indica cuántas peticiones pertenecen al grupo. La línea roja muestra el promedio. El ancho de las columnas **no** representa la cantidad de peticiones.

**Procedencia:** datos inventados para desarrollar el ejemplo de la p. 82; no son mediciones del libro.

### Calculemos el promedio paso a paso

1. Las 990 peticiones rápidas aportan: `990 × 100 = 99 000 ms`.
2. Las 10 peticiones lentas aportan: `10 × 1 000 = 10 000 ms`.
3. La suma de todos los tiempos es: `109 000 ms`.
4. Dividimos entre las 1 000 peticiones: `109 000 / 1 000 = 109 ms`.

$$\bar t = \frac{990(100)+10(1000)}{1000}=109\;\text{ms}.$$

Si solo miramos el promedio, parece que el sistema responde en aproximadamente una décima de segundo. Sin embargo, **10 peticiones tardaron un segundo completo**.

¿Por qué el promedio sube tan poco? Porque hay muchísimas más peticiones rápidas que lentas: las rápidas constituyen el 99 % de los datos. Si todas hubieran tardado 100 ms, la media sería 100 ms; las diez lentas solo la elevan a 109 ms.

> [!important] Lo que el promedio no permite afirmar
> «El promedio es 109 ms» **no significa** «todas las peticiones tardan unos 109 ms». De hecho, en este ejemplo ninguna tarda exactamente 109 ms: tardan 100 o 1 000 ms.

### ¿Qué significa “cola” en este contexto?

Si ordenamos los tiempos desde el más corto hasta el más largo, las peticiones más lentas quedan al final. A esa zona de valores altos la llamamos **cola de la distribución**.

Aquí, «cola» **no significa una fila de solicitudes esperando para ser atendidas**. Significa el extremo lento de los tiempos observados. Una fila de espera puede causar lentitud, pero es otro concepto.

Mirar la cola permite preguntar: **«¿qué tan lentas son las peticiones que peor se comportan?»**, en lugar de quedarse únicamente con el promedio.

## 3. Máximo y percentiles: distintas formas de mirar los mismos datos

El libro sugiere complementar el promedio con el **máximo**. Los **percentiles** se explican aquí como ampliación didáctica.

### El máximo: la petición más lenta observada

En nuestro ejemplo, el máximo es **1 000 ms**.

Responde a esta pregunta:

> «¿Cuánto tardó la petición más lenta de este conjunto?»

Es útil para detectar un extremo, pero no dice si hubo una sola petición así o muchas. Además, un único evento excepcional puede cambiarlo bastante. Tampoco garantiza cuál será el máximo de las peticiones futuras.

### Los percentiles: un límite que cubre una proporción de peticiones

Para entender un percentil, imagina que colocamos todas las peticiones en una fila, **ordenadas de la más rápida a la más lenta**.

El **p95** señala un tiempo que cubre al menos el 95 % de las observaciones con el método que usaremos. Por ejemplo, si p95 es 100 ms, significa que al menos el 95 % de las peticiones tardó **100 ms o menos**.

No significa:

- que el promedio sea 100 ms;
- que todas las peticiones hayan tardado 100 ms;
- que exactamente el 5 % restante necesariamente haya tardado más: puede haber tiempos empatados.

### Apliquémoslo al ejemplo

Nuestra fila ordenada queda así:

```text
Posiciones 1 a 990:       100 ms cada una
Posiciones 991 a 1 000: 1 000 ms cada una
```

Usaremos el método de **rango más próximo**: multiplicamos la proporción deseada por el número de datos y redondeamos hacia arriba para elegir una posición. Las posiciones se cuentan desde 1.

Para p95: `0,95 × 1 000 = 950`. Miramos la posición 950: allí hay una petición de **100 ms**.

| Medida | ¿Qué hacemos? | Resultado | ¿Qué nos dice? |
|---|---|---:|---|
| Media | Sumamos los tiempos y dividimos entre 1 000 | 109 ms | El promedio del conjunto |
| p95 | Miramos la posición 950 | 100 ms | Al menos el 95 % tardó 100 ms o menos |
| p99 | Miramos la posición 990 | 100 ms | Al menos el 99 % tardó 100 ms o menos |
| p99,9 | Miramos la posición 999 | 1 000 ms | Para cubrir el 99,9 %, ya llegamos al grupo lento |
| Máximo | Miramos la última posición | 1 000 ms | Es el mayor tiempo observado |

**¿Por qué p99 sigue siendo 100 ms si existen peticiones de 1 000 ms?** Porque la posición 990 todavía pertenece al grupo rápido. Las 10 lentas aparecen después: son exactamente el último 1 %.

> [!warning] Un percentil alto tampoco lo cuenta todo
> En este ejemplo, p99 parece bueno y aun así hay 10 peticiones mucho más lentas. El percentil que interesa depende de cuánto retraso y qué proporción de peticiones permite el objetivo.

Estos resultados corresponden al método indicado. Algunas herramientas usan otros métodos, con interpolación, y pueden dar resultados distintos cerca del límite entre grupos.

Además, **un porcentaje de peticiones no equivale necesariamente al mismo porcentaje de usuarios**: una persona puede realizar muchas peticiones. Para estudiar usuarios afectados hay que medir también esa relación.

## 4. Una medición necesita contexto

Una cifra aislada, como «p95 = 100 ms», deja preguntas abiertas:

| Dato que debemos aclarar | ¿Por qué importa? |
|---|---|
| Operación medida | Buscar productos no es lo mismo que confirmar un pago |
| Inicio y final de la medición | El tiempo del servidor no incluye necesariamente toda la espera del usuario |
| Ventana de tiempo | Un resumen de todo el día puede esconder una hora problemática |
| Número de peticiones | Diez observaciones y un millón no aportan la misma cantidad de evidencia |
| Región, dispositivo o tipo de conexión | Mezclar grupos puede ocultar que uno de ellos funciona mal |

El ejemplo anterior simplifica la realidad usando solo dos tiempos posibles. En un sistema real habrá tiempos mucho más variados. **Ver la distribución** significa observar cómo se reparten esos tiempos, no solo reducirlos a una cifra.

## 5. Monitoreo estadístico: comparar lo observado con lo esperado

El libro describe equipos que usan datos históricos para modelar el comportamiento esperado del sistema y generar alertas cuando las mediciones se apartan de él.

Un **modelo**, en este contexto, es una forma de estimar qué comportamiento sería normal dadas ciertas condiciones. No tiene por qué ser una inteligencia artificial compleja.

El proceso se entiende mejor por pasos:

1. **Recoger historia:** registrar el tráfico de días o semanas anteriores.
2. **Identificar patrones:** por ejemplo, los lunes suele haber más solicitudes que los domingos.
3. **Estimar un rango esperado:** calcular qué tráfico sería razonable para ese momento.
4. **Comparar con la realidad:** observar si el tráfico nuevo se sale de ese rango.
5. **Investigar la diferencia:** buscar una explicación antes de decidir qué hacer.

### Ejemplo supuesto

Para un momento concreto, el modelo espera entre **800 y 1 200 solicitudes por minuto**, pero llegan **1 900**.

La alerta significa: **«está ocurriendo algo distinto de lo previsto»**. No significa automáticamente: «el sistema está fallando».

Podrían existir varias explicaciones:

- Comenzó una promoción y el aumento es legítimo.
- Hay un error que provoca solicitudes repetidas.
- La medición está contando mal.
- El modelo no contempla un patrón importante y necesita ajustarse.

> [!tip] No confundas anomalía con avería
> Una anomalía es una diferencia respecto a lo esperado. Una avería es un fallo del sistema. La primera puede ayudar a detectar la segunda, pero no la demuestra por sí sola.

## 6. Rendimiento: responder rápido no es lo mismo que estar listo para usar

La p. 83 distingue medidas generales de respuesta y presupuestos específicos. Para entender la diferencia, piensa en lo que ocurre al abrir una página:

```text
El usuario abre la página
    → se solicitan y descargan recursos
    → se procesa código y contenido
    → aparece contenido en pantalla
    → la interfaz puede responder a las acciones del usuario
```

Es un esquema simplificado: en una página real varias tareas se solapan.

Una API —el servicio al que la interfaz pide datos— puede responder rápido y, aun así, la pantalla tardar en estar lista porque necesita descargar más archivos o ejecutar mucho código.

Por eso hay que decidir **qué tramo estamos midiendo**:

- ¿Cuánto tarda el servidor en preparar una respuesta?
- ¿Cuánto tarda esa respuesta en llegar al navegador?
- ¿Cuándo aparece contenido visible?
- ¿Cuándo puede el usuario interactuar sin que la pantalla se quede bloqueada?

El libro menciona estas medidas y presupuestos:

| Término del libro | Explicación sencilla |
|---|---|
| **First contentful paint** | Momento en que aparece el primer contenido, como texto o una imagen; no significa que toda la página esté lista |
| **First CPU idle** | Medida histórica orientada a detectar un primer momento en que el navegador está suficientemente desocupado para atender interacción |
| **K-weight** | Presupuesto del peso de los recursos que se descargan, expresado en kilobytes |

Se conservan como ejemplos del libro, **no como una lista actual de métricas recomendadas**. La idea importante es que «rendimiento» incluye varias esperas diferentes.

## 7. ¿Qué es un presupuesto de rendimiento?

Un **presupuesto** es un límite que el equipo acuerda no superar. Aquí no hablamos necesariamente de dinero: el límite puede ser de tiempo, bytes u otra medida.

**Ejemplo didáctico:** «Los recursos necesarios para la carga inicial no deben superar 100 kB transferidos».

Si se propone añadir una biblioteca que hace superar ese límite, el presupuesto obliga a revisar la decisión: reducir recursos, cargar algo más tarde o justificar un cambio del límite. Así, una intención vaga como «la página debe ser liviana» se convierte en una condición comprobable.

### ¿Por qué importa el peso de la descarga?

Una conexión solo puede transferir cierta cantidad de datos por segundo. Si mantenemos la misma velocidad, transferir más datos requiere más tiempo.

Supongamos una conexión ideal de **2 000 kilobits por segundo**. Cuidado con las unidades:

- Un **byte** contiene **8 bits**.
- `kB` significa kilobytes y `kb` significa kilobits.
- En este ejemplo usamos unidades decimales: `1 kB = 1 000 bytes`.

**Descarga de 500 kB:**

1. Convertimos a kilobits: `500 × 8 = 4 000 kb`.
2. Dividimos entre la velocidad: `4 000 kb / 2 000 kb/s = 2 segundos`.

**Descarga de 100 kB:**

1. Convertimos: `100 × 8 = 800 kb`.
2. Dividimos: `800 kb / 2 000 kb/s = 0,4 segundos`.

Reducir de 500 a 100 kB hace que el tiempo ideal de transferencia sea cinco veces menor. **No implica que la página completa cargue exactamente cinco veces más rápido**, porque también hay otras esperas y trabajo de procesamiento.

Estos cálculos aíslan la transferencia y suponen velocidad constante. No modelan latencia inicial, protocolos, descargas simultáneas, caché, compresión ni ejecución de código. Sirven para entender la relación entre peso y tiempo, no para predecir una carga real con exactitud.

## 8. Ejercicio resuelto: ¿el sistema cumple o no?

Volvamos a nuestras 1 000 peticiones:

- 990 tardan 100 ms.
- 10 tardan 1 000 ms.
- El promedio es 109 ms.

Ahora evaluemos **los mismos datos con tres objetivos diferentes**:

| Objetivo supuesto | ¿Cumple? | Explicación |
|---|---|---|
| El promedio debe ser menor de 500 ms | **Sí** | 109 ms es menor de 500 ms |
| Todas las peticiones deben tardar menos de 500 ms | **No** | Hay 10 peticiones que tardan 1 000 ms |
| Al menos el 99 % debe tardar menos de 500 ms | **Sí, exactamente** | Cumplen 990 de 1 000: el 99 % |

No hay contradicción: cada objetivo exige algo distinto. Estos resultados describen el conjunto observado, no garantizan el comportamiento futuro.

> [!important] Primero se define la necesidad; después se evalúan los datos
> No debemos cambiar el objetivo después de ver los resultados solo para decir que el sistema cumple. La medida elegida debe representar la experiencia que queremos ofrecer.

## Resumen para recordar

- **Promedio:** resume todos los tiempos, pero puede esconder peticiones lentas.
- **Cola:** es el extremo lento de la distribución de tiempos.
- **Percentil:** indica un tiempo que cubre cierta proporción de las peticiones ordenadas; no es un promedio.
- **Máximo:** muestra la petición más lenta observada, pero no cuántas fueron lentas.
- **Modelo estadístico:** ayuda a detectar diferencias frente a lo esperado; una alerta requiere interpretación.
- **Presupuesto de rendimiento:** convierte una intención en un límite medible, como un tiempo o un peso máximo de descarga.

**La pregunta clave no es solo «¿qué número obtuvimos?», sino «¿qué experiencia representa ese número y qué problema podría estar ocultando?».**

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/01 De características a medidas|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/03 Complejidad ciclomática|Siguiente →]]
