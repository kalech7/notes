---
title: Prueba exacta por cambios de signo
aliases:
  - Sign-flip test
  - Prueba de permutación de signos
tags:
  - posgrado
  - estadistica
  - prueba-exacta
  - randomizacion
related: "[[00 Índice - Comparación estadística de modelos]]"
---

# Prueba exacta por cambios de signo

Anterior: [[04A Diagnóstico de normalidad con Shapiro-Wilk]] · Volver al [[00 Índice - Comparación estadística de modelos|índice]] · Siguiente: [[06 Unidad de análisis, dependencia y validación cruzada]]

## 1. La idea intuitiva

La prueba conserva la identidad de cada par y la magnitud $|d_i|$, pero permite invertir el signo:

$$
d_i^{(b)}=s_i^{(b)}|d_i|,
\qquad s_i^{(b)}\in\{-1,+1\}.
$$

Para cada configuración $b$ se recalcula la media:

$$
\bar d^{(b)}=\frac{1}{n}\sum_{i=1}^{n}s_i^{(b)}|d_i|.
$$

En una prueba bilateral se compara $|\bar d^{(b)}|$ con $|\bar d_{\text{obs}}|$.

```mermaid
flowchart LR
    A[Entrada fija<br/>pares y magnitudes abs d_i] --> B[Asignar a cada unidad<br/>signo -1 o +1]
    B --> C[Multiplicar<br/>s_i por abs d_i]
    C --> D[Promediar]
    D --> E[Comparar abs media nula<br/>con 0.019]
    E -->|repetir todas| B
    E --> F[Proporción extrema]
```

### Cómo leer el diagrama

- La identidad y la magnitud de cada diferencia permanecen fijas.
- Solo cambia qué lado del cero ocupa cada magnitud.
- Cada vector de signos produce una posible media bajo la referencia nula.
- La proporción de medias al menos tan extremas como la observada es el $p$-value de esta prueba.

## 2. Ejemplo pequeño con tres diferencias

Supón magnitudes $0.04$, $0.01$ y $0.03$. Existen

$$
2^3=8
$$

configuraciones de signos:

| Signos | Media nula |
| --- | ---: |
| $(-,-,-)$ | $-0.0266667$ |
| $(-,-,+)$ | $-0.0066667$ |
| $(-,+,-)$ | $-0.0200000$ |
| $(-,+,+)$ | $0$ |
| $(+,-,-)$ | $0$ |
| $(+,-,+)$ | $0.0200000$ |
| $(+,+,-)$ | $0.0066667$ |
| $(+,+,+)$ | $0.0266667$ |

No se inventan nuevas magnitudes. Se pregunta cómo se distribuiría el promedio si las orientaciones permitidas por la nulidad cambiaran.

## 3. Las 1024 configuraciones del ejemplo

Con diez pares:

$$
2^{10}=1024.
$$

La extremidad bilateral se define antes de contar:

$$
|\bar d^{(b)}|\ge|0.019|.
$$

Sesenta y ocho configuraciones cumplen la condición:

$$
p_{\text{signos}}
=\frac{68}{1024}
=0.06640625.
$$

![[assets/distribucion-nula-signos.png|900]]

### Cómo leer el gráfico

- El eje horizontal muestra todas las medias que aparecen al invertir signos.
- El eje vertical cuenta cuántas configuraciones producen cada media.
- Las líneas moradas marcan $-0.019$ y $+0.019$, la extremidad observada.
- Las barras naranjas pertenecen a las dos colas y suman 68 configuraciones.
- La distribución es simétrica porque a cada vector de signos le corresponde su inversión total.

> [!note] La diferencia igual a cero
> El caso 6 tiene $d_6=0$. Cambiar su signo no altera el valor numérico, por lo que algunas configuraciones producen el mismo vector transformado. Enumerar ambos signos duplica todos los resultados de forma uniforme y no cambia la proporción $68/1024$.

## 4. ¿Qué nulidad hace válida la inversión?

La prueba no se justifica solo diciendo «la media es cero». Requiere una invariancia de la distribución conjunta ante las inversiones de signo permitidas:

$$
\mathcal L(D\mid H_0)
=\mathcal L(S\odot D\mid H_0),
$$

donde $S$ es un vector de signos permitidos y $\odot$ representa multiplicación elemento a elemento.

En lenguaje más intuitivo: bajo la nulidad, conservar o invertir el lado de cada diferencia debe ser una transformación defendible del experimento.

Esta condición puede surgir de:

- asignación aleatoria intercambiable dentro del par;
- simetría conjunta de las diferencias alrededor de cero;
- un diseño que autorice explícitamente intercambiar las etiquetas A y B en cada par.

> [!warning] Nulidad más fuerte
> $\mathbb E[D]=0$ por sí sola no garantiza simetría ni invariancia de signos. Una distribución muy asimétrica puede tener media cero y, aun así, no admitir esta referencia exacta.

## 5. «Exacta» se refiere al cálculo

La enumeración es exacta porque recorre las 1024 configuraciones sin muestreo Monte Carlo:

- no usa semilla;
- no aproxima la proporción mediante un subconjunto aleatorio;
- no presenta error de simulación.

Pero todavía quedan dos preguntas:

1. **Validez interna del modelo nulo:** ¿la inversión de signos es defendible?
2. **Generalización externa:** ¿qué población, tareas o casos representa el diseño?

Por eso:

$$
\text{exactitud computacional}\ne\text{validez universal}.
$$

## 6. Prueba $t$ y cambios de signo: contratos distintos

| Elemento | Prueba $t$ | Cambios de signo |
| --- | --- | --- |
| Nulidad principal | $\mathbb E[D]=0$ bajo un modelo para las diferencias | Invariancia conjunta ante signos permitidos |
| Estadístico mostrado | $T=\bar d/(s_d/\sqrt n)$ | $\lvert\bar d\rvert$ en la enumeración del módulo |
| Referencia | Distribución $t_{n-1}$ | Distribución discreta de transformaciones |
| Resultado | $p_t=0.04625$ | $p_{\text{signos}}=0.06641$ |
| Riesgo principal | Normalidad aproximada, atípicos, independencia | Inversión de signos no defendible, dependencia |

Los $p$-values cambian porque cambia la pregunta condicional y la distribución de referencia. No se debe ejecutar ambos métodos y elegir el menor.

## 7. No confundir con la prueba de los signos

La **prueba de los signos** clásica usa principalmente cuántas diferencias son positivas o negativas y descarta sus magnitudes. La prueba de **cambios de signo** de esta nota conserva cada $|d_i|$ y enumera sus orientaciones. Son procedimientos relacionados, pero no idénticos.

## 8. ¿Cuál método usar?

No existe una regla «no paramétrico siempre es mejor». La elección depende del diseño:

- usa la referencia $t$ si el objetivo es la media y sus supuestos sobre diferencias son defendibles;
- usa cambios de signo si el diseño o simetría justifican la invariancia de signos;
- usa un método que preserve clústeres, sujetos, series temporales o *folds* si existe dependencia estructural;
- si ninguna referencia es defendible, describe el efecto y limita la inferencia en vez de forzar un $p$-value.

## 9. Conclusión conjunta del ejemplo

La dirección y magnitud observadas no cambian: $\bar d=0.019$ favorece a B. Lo que cambia es la fuerza de evidencia bajo cada contrato:

- prueba $t$: $p=0.0463$;
- cambios de signo: $p=0.0664$.

Esto muestra por qué el umbral $0.05$ no es el veredicto. La conclusión debe explicar qué referencia se usó, por qué era apropiada y cuál es el alcance del diseño.

Anterior: [[04A Diagnóstico de normalidad con Shapiro-Wilk]] · Siguiente: [[06 Unidad de análisis, dependencia y validación cruzada]]
