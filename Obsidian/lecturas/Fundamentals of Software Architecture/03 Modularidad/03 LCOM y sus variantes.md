---
title: "Capítulo 3 · Modularidad · LCOM y sus variantes"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 3
orden: 3
---

# LCOM y sus variantes

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 3 · Modularidad](00%20%C3%8Dndice.md) → Nota 3 de 7

**Objetivo:** Calcular LCOM y reconocer qué no mide.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

## 3. LCOM: medir estructura sin confundirla con intención

LCOM significa *Lack of Cohesion of Methods*: falta de cohesión entre métodos. Hay distintas variantes y no comparten necesariamente escala, fórmula o tratamiento de casos especiales. Antes de comparar resultados de herramientas hay que verificar qué calculan.

### LCOM1 con cuatro métodos

Usaremos la formulación que el capítulo denomina versión 1. Para cada método se obtiene el conjunto de campos de instancia que utiliza. Después se examinan **pares no ordenados de métodos distintos**:

- $P$: conjunto de pares cuyos conjuntos de campos son disjuntos.
- $Q$: conjunto de pares que comparten al menos un campo.

$$
\mathrm{LCOM1}=\max\left(|P|-|Q|,0\right)
$$

**Aclaración técnica:** se cuentan pares, no métodos aislados ni accesos individuales. $|Q|$ es un conteo no negativo; no se va «decrementando». Compartir tres campos sigue aportando un solo par a $Q$. La prosa de la página impresa 43 puede inducir a confusión en este punto.

Supongamos una clase de PedidoClaro con cuatro métodos:

| Método | Campos usados |
|---|---|
| `subtotal()` | `lineas` |
| `cantidadArticulos()` | `lineas` |
| `destinatario()` | `correo` |
| `cambiarDestinatario()` | `correo` |

Hay $4\times3/2=6$ pares. Dos comparten campos: los dos primeros métodos entre sí y los dos últimos entre sí. Los cuatro pares que cruzan grupos no comparten campos. Por tanto, $|P|=4$, $|Q|=2$ y **LCOM1 = 2**. Esto sugiere dos responsabilidades para investigar, no ordena una extracción automática.

![LCOM1 con cuatro métodos ](../Recursos%20visuales/Diagramas/cap03-diagrama-02.png)

[Fuente editable del diagrama](../Recursos%20visuales/Diagramas/cap03-diagrama-02.mmd)

**Interpretación:** aparecen dos grupos desconectados de métodos y campos. **Límite:** el dibujo no muestra llamadas entre métodos, reglas de negocio ni acceso indirecto al estado. Esas omisiones importan al elegir una variante de LCOM.

### LCOM1 no es LCOM4

**Ampliación técnica propia:** LCOM4 cuenta componentes conexas en un grafo de métodos, conectados por acceso a campos comunes o por llamadas entre ellos, según las reglas de la herramienta. Si no hay llamadas adicionales, el ejemplo anterior tiene dos componentes: LCOM4 = 2. La coincidencia numérica con LCOM1 es accidental.

Para comprobarlo, imaginemos tres métodos que comparten `lineas` y un cuarto que usa únicamente `correo`. Hay tres pares compartidos y tres disjuntos: LCOM1 = 0. Sin llamadas adicionales siguen existiendo **dos componentes conexas**. Por tanto, un cero en LCOM1 no demuestra que toda la clase esté conectada.

### La expresión LCOM96b de la página 43

La ecuación 3-2 se comprobó directamente en la imagen ampliada del escaneo. El libro imprime bajo el nombre **LCOM96b**:

$$
\mathrm{LCOM96b}=\frac{1}{a}\sum_{j=1}^{a}\frac{m-\mu(A_j)}{m}.
$$

Para interpretar esa expresión, tomamos $a$ como número de atributos, $m$ como número de métodos y $\mu(A_j)$ como número de métodos que utilizan el atributo $A_j$. Para cada atributo contamos qué proporción de métodos **no lo usa**; después promediamos esas proporciones. Es equivalente a $1-\sum_j\mu(A_j)/(am)$, cuando $a>0$ y $m>0$.

En nuestro ejemplo hay dos atributos y cuatro métodos; cada atributo es utilizado por dos métodos. El resultado es $\frac12[(4-2)/4+(4-2)/4]=0.5$. Si todos los métodos utilizan todos los atributos, da cero. Si ningún método utiliza ningún atributo, da uno. Esta fórmula tampoco cuenta componentes conexas ni demuestra cohesión semántica. Sin métodos o sin atributos queda indefinida bajo la expresión escrita; una herramienta puede establecer una convención propia.

**Precisión sobre variantes:** se está explicando la expresión impresa del escaneo. Existen otras normalizaciones que emplean $m-1$ en el denominador; no producen necesariamente el mismo resultado ni deben sustituirse silenciosamente al comparar herramientas. La explicación de los símbolos y el cálculo anterior son elaboración didáctica propia, porque el libro no desarrolla sus variables.

Una clase de funciones matemáticas puras puede no tener campos y aun así poseer una responsabilidad coherente. A la inversa, compartir un campo `contexto` entre todos los métodos puede producir un indicador favorable y ocultar muchas responsabilidades. La métrica descubre estructura; el dominio explica su conveniencia.

![lcom](../Recursos%20visuales/05-lcom.png)

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=7|PDF pp. 7–8; impresas pp. 43–44]].

---

**Anterior:** [Cohesión y responsabilidades](02%20Cohesi%C3%B3n%20y%20responsabilidades.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Acoplamiento y dependencias](04%20Acoplamiento%20y%20dependencias.md)
