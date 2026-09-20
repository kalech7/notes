---
title: "27 PRÁCTICA - Sesiones 02 a 05"
tags:
  - maestria/ia-generativa
  - practica
  - autoevaluacion
---

# 27 PRÁCTICA - Sesiones 02 a 05

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

Intenta resolver cada ejercicio antes de abrir la respuesta.

## 1. Ordena el pipeline

Ordena estas piezas: `softmax`, `tokenizador`, `LM head`, `embedding`, `bloques transformer`, `muestreo`.

> [!success]- Solución
> Tokenizador → embedding y posición → bloques transformer → LM head → softmax → muestreo o argmax.

## 2. Parámetros o valores dinámicos

Clasifica cada elemento:

1. $W_Q$, $W_K$, $W_V$.
2. Pesos de atención para «el gato duerme».
3. Embedding del token.
4. Temperatura.

> [!success]- Solución
> 1 y 3 son parámetros aprendidos. Los pesos de atención se calculan para cada entrada. La temperatura es una configuración de decodificación externa a los pesos.

## 3. Softmax causal a mano

Para la segunda posición hay scores escalados `[0, 0.707, -∞]`.

1. Calcula $e^s$ aproximadamente.
2. Normaliza.
3. Explica por qué el tercer peso es cero.

> [!success]- Solución
> $e^0=1$, $e^{0.707}\approx2.028$ y $e^{-\infty}=0$. La suma es 3.028. Los pesos son aproximadamente `[0.330, 0.670, 0]`. La máscara causal convirtió el futuro en $-\infty$ antes de softmax.

## 4. Varias cabezas

Un modelo tiene $d_{model}=768$ y 12 cabezas con dimensiones repartidas uniformemente. ¿Cuánto vale $d_k$ por cabeza?

> [!success]- Solución
> $d_k=768/12=64$. No significa que cada cabeza reciba solo algunos tokens; recibe proyecciones de todos los tokens permitidos con dimensión 64.

## 5. Identifica la etapa de entrenamiento

Relaciona:

| Situación | Etapa |
| --- | --- |
| Predecir el token siguiente en un corpus masivo | ? |
| Imitar respuestas escritas por anotadores | ? |
| Ordenar dos respuestas y optimizar con PPO | ? |
| Optimizar directamente pares preferido/rechazado | ? |

> [!success]- Solución
> Preentrenamiento; SFT; RLHF; DPO.

## 6. Recompensas desplazadas

Un modelo de recompensa asigna 2.4 y 1.1 a dos respuestas. Otro ajuste asigna 12.4 y 11.1. ¿Cambió la preferencia Bradley-Terry?

> [!success]- Solución
> No. La diferencia sigue siendo 1.3. La pérdida depende de diferencias, no del origen absoluto de la escala.

## 7. Decodificación

Una distribución ordenada es `[0.55, 0.25, 0.10, 0.06, 0.04]`.

1. ¿Qué conserva top-k = 3?
2. ¿Qué conserva top-p = 0.80 usando el prefijo mínimo que alcanza el umbral?
3. ¿Qué ocurrirá probablemente con el tamaño del núcleo si subes mucho la temperatura?

> [!success]- Solución
> Top-k conserva los tres primeros. Top-p conserva los dos primeros porque suman 0.80. Al subir la temperatura la distribución suele aplanarse, así que se necesitarán más tokens para acumular la misma masa.

## 8. Zero-shot, few-shot o fine-tuning

Decide la primera prueba razonable:

1. La salida tiene claves equivocadas.
2. El modelo desconoce documentos privados.
3. Necesitas cambiar una conducta de forma persistente en millones de llamadas.

> [!success]- Solución
> 1: esquema estricto o few-shot de formato, con validación. 2: investigar RAG. 3: evaluar fine-tuning después de establecer una línea base de prompting. La decisión final depende de métricas y costo.

## 9. Las cuatro compuertas

Para cada salida, identifica el primer fallo:

```text
A. Aquí está: {"categoria": "ventas", "urgencia": 3}
B. {"categoria": "ventas", "urgencia": "3"}
C. {"categoria": "magia", "urgencia": 3}
D. {"categoria": "ventas", "urgencia": 3}, pero el ticket era técnico
```

> [!success]- Solución
> A puede fallar al parsear directamente por el prefijo textual. B falla el tipo. C falla el dominio. D pasa forma y dominio, pero falla corrección semántica.

## 10. Costo

Una llamada usa 4 000 tokens de entrada y 800 de salida. La entrada cuesta 1 USD por millón y la salida 5 USD por millón.

> [!success]- Solución
> Entrada: $4000/10^6\times1=0.004$ USD. Salida: $800/10^6\times5=0.004$ USD. Total: 0.008 USD.

## 11. Diseña un mini-experimento

Problema: clasificar tickets en `facturacion`, `tecnico`, `ventas` u `otro`.

Escribe antes de abrir la respuesta:

- diez casos y sus etiquetas;
- normalización;
- tratamiento de JSON inválido;
- variables que mantendrás fijas;
- métricas;
- número de corridas.

> [!success]- Propuesta
> Usa casos balanceados y algunos ambiguos. Valida JSON, esquema y enum; una salida inválida cuenta como fallo de formato y no se convierte en una categoría inventada. Mantén prompt, casos, límite y parser. Mide exactitud, validez, latencia, tokens y costo. Ejecuta al menos tres corridas por configuración si existe muestreo y conserva cada respuesta cruda.

## 12. Preguntas de explicación corta

> [!question]- ¿Por qué atención no es una explicación causal automática?
> Porque muestra pesos de combinación dentro del modelo. No prueba que cambiar esa conexión cause la decisión ni que el peso exprese una razón humana fiel.

> [!question]- ¿Por qué DPO necesita una referencia?
> La referencia define cuánto se aleja la política y permite expresar la recompensa implícita como una razón de probabilidades.

> [!question]- ¿Por qué pedir más razonamiento puede empeorar?
> Añade oportunidades para distracción, supuestos espurios y errores intermedios; su utilidad depende de la tarea.

> [!question]- ¿Cuál es la diferencia entre validar forma y validar acierto?
> La forma comprueba sintaxis, claves y tipos. El acierto compara el contenido con la realidad o con una respuesta esperada.

## Ruta de repaso recomendada

1. [[18 S02 - Transformer de extremo a extremo]].
2. [[19 S02 - Atención Q K V paso a paso]].
3. [[21 S03 - Preentrenamiento autosupervisado y MLE]].
4. [[22 S03 - SFT RLHF DPO y Constitutional AI]].
5. [[23 S04 - Greedy temperatura top-k y top-p]].
6. [[24 S04 - Zero-shot few-shot y razonamiento]].
7. [[25 S04 - Salidas estructuradas costo y razonamiento interno]].
8. [[26 S05 - Diseñar una comparación de modelos]].

## Material relacionado

- [[sesion-02.pdf]]
- [[sesion-03-1.pdf]]
- [[sesion-04.pdf]]
- [[sesion-05.pdf]]
- `talleres/taller-01-foundation-models.ipynb`: laboratorio existente del vault.
- `talleres/resultados.csv`: resultados crudos existentes.
