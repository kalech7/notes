---
title: "Capítulo 3 · Modularidad · Abstracción inestabilidad y distancia"
created: 2026-09-25
tags:
  - lecturas/software-architecture
capitulo: 3
orden: 5
---

# Abstracción inestabilidad y distancia

[Inicio del libro](../00%20Empieza%20aqu%C3%AD.md) → [Capítulo 3 · Modularidad](00%20%C3%8Dndice.md) → Nota 5 de 7

**Objetivo:** Calcular A, I y D e interpretar sus límites.

> [!info] Contexto del capítulo
> Segunda edición. PedidoClaro y sus cifras son ejemplos didácticos propios; Silicon Sandwiches es la kata del libro. El [índice del capítulo](00%20%C3%8Dndice.md) conserva el alcance y las referencias generales.

> [!info] Recuerda antes
> $C_a$ cuenta dependencias entrantes y $C_e$ salientes bajo una unidad de análisis declarada. Esos conteos describen dirección, pero todavía no explican si un módulo dependido por muchos puede cambiar sin propagar daños.

## 5. Abstracción, inestabilidad y secuencia principal

### Abstracción: contar tipos, no líneas

Para una unidad con $N_a$ tipos abstractos —interfaces o clases abstractas— y $N_c$ tipos concretos:

$$
A=\frac{N_a}{N_a+N_c}
$$

Si Pedidos tiene dos tipos abstractos y ocho concretos, $A=2/10=0.2$. **No intervienen las líneas de código.** El ejemplo narrativo de las 5.000 líneas en la página impresa 46 mezcla unidades y no debe utilizarse para calcular esta métrica. Si solo hubiera una clase concreta y ningún tipo abstracto, $A=0$, independientemente de su longitud. Sin tipos contables, el denominador es cero y el valor queda indefinido.

### Inestabilidad: una relación de dependencias

$$
I=\frac{C_e}{C_a+C_e}
$$

Retomamos el grafo de [Acoplamiento y dependencias](04%20Acoplamiento%20y%20dependencias.md): Pedidos tiene tres dependencias entrantes, $C_a=3$, y dos salientes, $C_e=2$. Por tanto, $I=2/(3+2)=0.4$. En esta terminología, una unidad con muchos dependientes tiene más restricciones para cambiar: se considera relativamente estable. Una unidad que depende de otras y tiene pocos consumidores dispone de mayor libertad estructural para cambiar y queda más expuesta a sus proveedores.

**$I$ no es una probabilidad de fallo**, ni mide cuántos defectos aparecen, ni la frecuencia real de cambios. Si $C_a=0$ y $C_e>0$, resulta $I=1$, incluso con un solo proveedor. Si $C_e=0$ y $C_a>0$, resulta $I=0$. Si ambos son cero, $I$ está **indefinida**; una herramienta puede adoptar una convención, que debe documentarse.

### Distancia y zonas

La secuencia principal es la recta $A+I=1$. Relaciona estabilidad estructural y abstracción: las unidades muy utilizadas pueden beneficiarse de contratos abstractos; las implementaciones concretas pueden ubicarse en unidades con mayor libertad de cambio.

$$
D=|A+I-1|
$$

Esta es la **distancia normalizada** del capítulo. La distancia geométrica perpendicular a la recta, usando ejes con la misma escala, es:

$$
d_{\perp}=\frac{|A+I-1|}{\sqrt{2}}
$$

En Pedidos, $A=0.2$ e $I=0.4$: $D=0.4$ y $d_{\perp}\approx0.283$. No son fórmulas contradictorias: la primera normaliza el máximo posible dentro del cuadrado unitario a 1.

| Región | Valores próximos | Qué invita a investigar |
|---|---|---|
| Zona de dolor | $A=0, I=0$ | Muchas dependencias hacia implementaciones concretas pueden encarecer cambios. |
| Secuencia principal | $A+I=1$ | Equilibrio estructural según este modelo; no certificación de calidad. |
| Zona de inutilidad | $A=1, I=1$ | Abstracciones con pocos consumidores y dependencias salientes pueden aportar poco valor. |

Los nombres de las zonas son provocadores. Una biblioteca concreta, pequeña y muy estable puede estar en la zona de dolor sin causar dolor real. Una abstracción nueva puede no tener consumidores todavía y seguir siendo necesaria. Además, $D$ pierde dirección: $(A=0.1,I=0.1)$ y $(A=0.9,I=0.9)$ producen $D=0.8$, pero plantean preguntas diferentes.

![secuencia principal](../Recursos%20visuales/04-secuencia-principal.png)

**Uso responsable:** medir con criterios constantes, establecer una referencia, investigar cambios y contrastarlos con mantenimiento real. Añadir interfaces únicamente para acercarse a una recta puede aumentar complejidad sin resolver ninguna necesidad. Si $A$ o $I$ están indefinidas, tampoco corresponde presentar $D$ como una medida válida.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=9|PDF pp. 9–12; impresas pp. 45–48]].

---

**Anterior:** [Acoplamiento y dependencias](04%20Acoplamiento%20y%20dependencias.md) · **Índice:** [Volver al capítulo](00%20%C3%8Dndice.md) · **Siguiente:** [Connascencia y refactorización](06%20Connascencia%20y%20refactorizaci%C3%B3n.md)
