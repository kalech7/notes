---
title: "06 · Gobernar modularidad: ciclos y distancia a la secuencia principal"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/medicion
---

# Gobernar modularidad: ciclos y distancia a la secuencia principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, capítulo 6. **PDF 8–10 · impresas 88–90** del [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf|PDF conservado]]. «Libro» identifica sus planteamientos; las ampliaciones, plantillas y datos supuestos se señalan como elaboración didáctica.

La modularidad se degrada cuando un componente incorpora dependencias sin considerar el efecto conjunto. Una importación automática parece una comodidad local, pero la acumulación puede hacer imposible reutilizar o cambiar una parte sin arrastrar las demás. El capítulo usa dos verificaciones para mostrar que una regla arquitectónica puede expresarse como una prueba repetible.

## Figura 6-3: dependencias cíclicas

![Figura 6-3 recreada: dependencias cíclicas entre tres componentes](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c06-05-ciclos.png)

**Procedencia:** recreación de la topología triangular de la figura 6-3, p. 89. La fila inferior es una ampliación explicativa.

Cada caja superior representa un componente. `A → B` significa que A depende de B; una línea con dos puntas representa dependencias en ambas direcciones. El triángulo del libro contiene relaciones mutuas entre las tres parejas. Las cajas inferiores describen la detección y la consecuencia de gobierno; sus flechas no son importaciones del código.

**Secuencia causal:** para usar A hacen falta B y C; B también requiere A y C. Si se intenta separar una sola pieza, aparecen requisitos hacia las otras. El grafo ofrece ciclos cortos como `A → B → A` y recorridos mayores. Esto reduce independencia y favorece una estructura cada vez más entrelazada.

**Conclusión:** la existencia de tres carpetas no demuestra tres módulos independientes. **Límites:** no todo ciclo debe tener flechas bidireccionales entre cada pareja. `A → B → C → A` ya es un ciclo. El análisis depende del nivel elegido: puede haber un ciclo entre clases dentro de un módulo sin que exista un ciclo entre módulos.

## Cómo lo convierte el libro en una comprobación

El ejemplo 6-2 usa JDepend para analizar dependencias entre paquetes Java y fallar una prueba si encuentra ciclos. La lógica, independiente de una API concreta, es:

```text
paquetes = analizar_dependencias(artefactos_del_proyecto)
grafo = construir_grafo_dirigido(paquetes)
afirmar que grafo no contiene ciclos
si falla: mostrar los paquetes y aristas que forman el ciclo
```

Primero se debe definir qué se analiza: clases compiladas del proyecto, bibliotecas y exclusiones deliberadas. Si la herramienta solo ve la mitad del sistema, la ausencia de ciclos en ese subconjunto no demuestra ausencia en todo el sistema. Luego se integra la comprobación en el ciclo de construcción para detectar una dependencia problemática cerca del cambio que la introdujo.

Como ampliación, una búsqueda en profundidad puede marcar nodos «en exploración». Llegar de nuevo a uno de esos nodos revela un ciclo dirigido. Encontrar un nodo ya explorado por completo no basta para afirmar un ciclo. La diferencia permite evitar falsos positivos en grafos donde varias ramas llegan al mismo módulo común.

### Reparar el ciclo exige entender la responsabilidad

Opciones posibles son mover una responsabilidad al módulo adecuado, introducir un contrato en un nivel común o invertir una dependencia mediante una abstracción. A veces los componentes están tan unidos por el dominio que la mejor decisión es reconocerlos como un módulo coherente. Estas son estrategias didácticas, no una receta universal. Extraer todo a un paquete «common» puede ocultar el problema y crear un centro de acoplamiento.

## Distancia a la secuencia principal

La p. 90 retoma una métrica explicada antes en el libro y demuestra que también puede verificarse automáticamente. Para entender el ejemplo, este recordatorio es una ampliación del capítulo:

- **Abstracción `A`**: proporción de tipos abstractos e interfaces respecto del total de tipos del paquete, según las convenciones de la herramienta.
- **Inestabilidad `I`**: `Ce / (Ca + Ce)`, donde `Ce` son dependencias salientes y `Ca` entrantes.
- **Distancia normalizada `D`**: `|A + I − 1|`.

Si `Ca + Ce = 0`, la fórmula de `I` no está definida por sí sola; debe documentarse la convención de la herramienta. «Inestabilidad» aquí significa sensibilidad estructural a cambios de dependencias; no significa que el programa falle en producción.

![Abstracción e inestabilidad frente a la secuencia principal](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c06-06-distancia.png)

**Procedencia:** gráfico propio para explicar el ejemplo 6-3. Los puntos P, Q y R son inventados.

El eje horizontal es `I` y el vertical `A`, ambos de 0 a 1. La diagonal azul representa `A + I = 1`, donde `D = 0`. Los puntos no son mediciones reales. Las cajas de la derecha muestran cálculo, comparación e interpretación.

Con los valores dibujados, P tiene `A=0,2` e `I=0,8`, de modo que `D=0`. Q tiene `A=0,1`, `I=0,1` y `D=0,8`. R tiene `A=0,85`, `I=0,85` y `D=0,7`. Una tolerancia de 0,5 permite P y señala Q y R. `D` es una distancia normalizada; no debe confundirse con la distancia euclídea perpendicular dibujada en el plano, que introduce un factor `√2`.

**Causalidad e interpretación:** Q combina poca abstracción con estabilidad estructural: puede concentrar concreciones de las que otros dependen. R combina mucha abstracción con alta inestabilidad: podría contener abstracciones con poca utilidad estabilizadora. Son hipótesis para inspección, no diagnósticos concluyentes.

**Conclusión:** la regla convierte una propiedad estructural en una condición verificable. **Límite:** un paquete de datos o un caso de dominio legítimo puede apartarse de la diagonal. Forzar tipos abstractos solo para mover un punto modifica el indicador sin garantizar mejor diseño.

## La función de aptitud de la p. 90

El ejemplo establece valor ideal 0 y tolerancia 0,5, expresamente dependiente del proyecto. Analiza los paquetes y comprueba la distancia de cada uno. La tolerancia no es una recomendación universal ni debe copiarse sin justificarla. El propósito es mostrar el mecanismo: **recorrer elementos → calcular → comparar → fallar con identificación del elemento**.

**Ejercicio resuelto:** un paquete tiene 2 tipos abstractos de 10, `Ca=2` y `Ce=8`. Entonces `A=0,2`, `I=8/(2+8)=0,8` y `D=0`. Cumple la tolerancia del ejemplo. Esto no garantiza ausencia de ciclos ni buena cohesión: cada indicador observa una dimensión distinta.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/05 Gobierno y funciones de aptitud|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/07 Capas y reglas de dependencia|Siguiente →]]
