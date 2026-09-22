---
title: "31 S06 - Coseno producto punto y normalización"
tags:
  - maestria/ia-generativa
  - embeddings
  - similitud-vectorial
  - estudio
---

# 31 S06 - Coseno, producto punto y normalización

[[30 S06 - Cómo se entrena SBERT y por qué permite buscar|Anterior]] · [[32 S06 - Elegir modelo y reconocer límites|Siguiente]]

## 1. Las tres medidas

Sean $q$ el vector de la consulta y $s$ el de un documento. La **norma** $\|q\|=\sqrt{\sum_j q_j^2}$ mide la longitud del vector.

| Medida | Fórmula | ¿Mejor significa...? | Sensibilidad a longitud |
| --- | --- | --- | --- |
| Coseno | $\displaystyle \frac{q\cdot s}{\|q\|\|s\|}$ | mayor | no cambia si escalamos por constantes positivas |
| Producto punto | $\displaystyle q\cdot s=\sum_jq_js_j$ | mayor | sí |
| Distancia euclídea | $\displaystyle\|q-s\|$ | menor | sí, en general |

El coseno requiere vectores no nulos y cae entre $-1$ y $1$. El producto punto no tiene esa cota. Una distancia euclídea es no negativa. No se debe llamar «coseno» al producto punto sin verificar la normalización.

## 2. Qué hace normalizar

Normalizar un vector no nulo significa dividirlo por su longitud:

$$\hat q=\frac{q}{\|q\|},\qquad \hat s=\frac{s}{\|s\|},\qquad \|\hat q\|=\|\hat s\|=1.$$

Cuando **ambos lados** tienen norma 1:

$$\hat q\cdot\hat s=\cos(q,s)$$

y, al expandir el cuadrado,

$$\|\hat q-\hat s\|^2
=\|\hat q\|^2+\|\hat s\|^2-2\hat q\cdot\hat s
=2-2\cos(q,s).$$

Para una consulta fija y los mismos candidatos, maximizar coseno o producto punto normalizado y minimizar distancia euclídea normalizada produce **el mismo orden**. Los valores numéricos de los tres puntajes no son iguales; especialmente, un umbral debe definirse en la escala de la medida usada.

## 3. Contraejemplo: cambia el ganador

Usamos el ejemplo exacto de la sesión:

$$q=(1,0),\qquad s_1=(0.8,0.6),\qquad s_2=(1,2).$$

Las longitudes son $\|q\|=\|s_1\|=1$ y $\|s_2\|=\sqrt5\approx2.236$. Ahora compara:

| Candidato | Producto punto $q\cdot s_i$ | Coseno | Posición por producto punto | Posición por coseno |
| --- | ---: | ---: | ---: | ---: |
| $s_1$ | $0.8$ | $0.8$ | 2 | **1** |
| $s_2$ | $1.0$ | $1/\sqrt5\approx0.447$ | **1** | 2 |

![Vectores y cambio de ranking](<../Recursos visuales/18-coseno-producto-punto.png>)

El producto punto favorece a $s_2$ por su longitud. Tras normalizarlo, $\hat s_2=(1/\sqrt5,2/\sqrt5)$ y $q\cdot\hat s_2\approx0.447$: vuelve a ganar $s_1$. **No cambió el texto**, cambió la métrica aplicada al vector.

## 4. Normalizar solo los documentos: falla menos visible

Si cada documento $\hat s_i$ tiene norma 1, pero la consulta $q$ no, entonces:

$$q\cdot\hat s_i=\|q\|\cos(q,s_i).$$

Para **una misma consulta**, $\|q\|$ es el mismo factor positivo para todos los candidatos. Por eso el orden coincide con el coseno. Pero los puntajes pueden salir del intervalo $[-1,1]$ y un umbral fijo deja de significar lo mismo entre consultas.

![Mismo coseno, distinto puntaje por norma de consulta](<../Recursos visuales/19-normalizacion-umbral.png>)

En el gráfico didáctico, dos consultas tienen coseno $0.30$ con su mejor documento, pero normas 1 y 2. Sus productos punto son $0.30$ y $0.60$. Con umbral $0.35$, un sistema se abstendría en una y respondería en la otra, aun con la misma similitud angular. No son datos medidos: es una demostración de la fórmula.

## 5. El caso del notebook citado

El PDF muestra que el notebook llama `encode(textos, normalize_embeddings=True)` y luego calcula `V_corpus @ V_consultas[idx_consulta]`. El `@` hace productos punto. Solo puede interpretarse como coseno porque la línea anterior generó vectores de norma 1 a **ambos lados**. Si alguien cambia la opción a `False` y deja `@`, el código sigue ejecutándose, pero el puntaje ya no es coseno y el orden **puede** cambiar, como acabamos de comprobar.

```python
import numpy as np

q = np.array([1.0, 0.0])
S = np.array([[0.8, 0.6], [1.0, 2.0]])  # filas: s1 y s2
q_u = q / np.linalg.norm(q)
S_u = S / np.linalg.norm(S, axis=1, keepdims=True)
scores_coseno = S_u @ q_u
print(scores_coseno)  # [0.8, 0.4472136]
```

En datos reales hay que gestionar vectores de norma cero y asegurar que consulta y documentos se embeban con la misma configuración.

> [!question]- Comprueba tu comprensión
> **Si normalizo solo los documentos, ¿qué se conserva y qué se pierde?** Se conserva el ranking dentro de cada consulta respecto del coseno; se pierde la escala comparable del puntaje entre consultas, lo que afecta umbrales fijos.

## Fuente y alcance

- [[sesion-06.pdf#page=13|Sesión 06, p. 13]]: fórmulas y equivalencia bajo norma 1.
- [[sesion-06.pdf#page=14|Sesión 06, p. 14]]: contraejemplo de inversión del primer lugar.
- [[sesion-06.pdf#page=15|Sesión 06, p. 15]]: normalización de un solo lado y umbral.
- [[sesion-06.pdf#page=16|Sesión 06, p. 16]] y [[sesion-06.pdf#page=17|p. 17]]: código y pregunta diagnóstica.
