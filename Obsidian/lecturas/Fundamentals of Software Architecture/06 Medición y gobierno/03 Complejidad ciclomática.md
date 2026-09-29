---
title: "06 · Medidas estructurales y complejidad ciclomática"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/medicion
---

# Medidas estructurales y complejidad ciclomática

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, capítulo 6. **PDF 3–5 · impresas 83–85** del [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf|PDF conservado]]. «Libro» identifica sus planteamientos; las ampliaciones, plantillas y datos supuestos se señalan como elaboración didáctica.

## 1. Qué es, en palabras sencillas

La **complejidad ciclomática (CC)** es una medida de la estructura de decisiones de una función. Ayuda a detectar código que puede resultar difícil de entender, probar y modificar.

Imagina que ejecutar una función es recorrer un camino. Un `if` es una bifurcación: según se cumpla o no una condición, sigues una rama u otra.

> [!tip] La idea principal
> **Más decisiones suelen implicar más casos sobre los que debes razonar.** CC mide esa estructura de caminos; no mide cuántas líneas tiene el código ni cuánto tarda en ejecutarse.

Su definición precisa es el **número de caminos linealmente independientes del flujo de control**. Más abajo veremos por qué eso no significa «todas las combinaciones posibles».

Los ejemplos cotidianos y las explicaciones paso a paso que siguen son **elaboración didáctica**; el ejemplo de `c1` y `c2` adapta el del libro.

## 2. Primero: una función sin decisiones

```python
def saludar():
    print("Hola")
    print("Bienvenido")
```

Siempre se ejecutan las mismas instrucciones en el mismo orden. No hay ninguna bifurcación.

**Su CC es 1**, no 0: existe un recorrido, aunque no haya decisiones.

## 3. Qué cambia al agregar un `if`

```python
def comprobar_edad(edad):
    if edad >= 18:
        return "Mayor de edad"
    return "Menor de edad"
```

Ahora hay dos recorridos:

1. La condición es verdadera → devuelve «Mayor de edad».
2. La condición es falsa → devuelve «Menor de edad».

**Su CC es 2.** Partíamos de un recorrido y la decisión añadió una alternativa.

Para código estructurado sencillo, con decisiones binarias contadas de forma consistente:

$$CC = \text{número de decisiones} + 1.$$

No se cuentan los `return` como decisiones: un retorno termina la función, pero no elige entre dos ramas. Tampoco debe contarse cada `else` como una decisión nueva: es la otra rama de la misma condición.

> [!note] Alcance de esta regla sencilla
> En estos ejemplos basta contar los `if`. Los bucles también introducen decisiones. Las condiciones compuestas y otras construcciones requieren conocer la convención de la herramienta que calcula CC; no conviene contar palabras del código a ciegas.

## 4. El ejemplo de la nota, paso a paso

```python
def decision(c1, c2):
    if c1 < 100:
        return 0

    if c1 + c2 > 500:
        return 1

    return -1
```

**Hay dos decisiones, por tanto CC = 2 + 1 = 3.**

Para entender sus recorridos, recuerda que **`return` termina la función inmediatamente**.

### Recorrido 1: termina en la primera condición

Usamos `c1 = 50` y `c2 = 800`:

- ¿50 es menor que 100? Sí.
- Devuelve `0` y termina.
- **La segunda condición ni siquiera se evalúa**, aunque la suma sea mayor que 500.

### Recorrido 2: llega a la segunda condición y esta se cumple

Usamos `c1 = 200` y `c2 = 400`:

- ¿200 es menor que 100? No; continúa.
- ¿200 + 400 es mayor que 500? Sí.
- Devuelve `1` y termina.

### Recorrido 3: ninguna condición se cumple

Usamos `c1 = 200` y `c2 = 100`:

- ¿200 es menor que 100? No; continúa.
- ¿200 + 100 es mayor que 500? No.
- Llega al último `return` y devuelve `-1`.

| Recorrido | Primera condición | Segunda condición | Resultado |
|---|---|---|---|
| 1 | Verdadera | No se evalúa | `0` |
| 2 | Falsa | Verdadera | `1` |
| 3 | Falsa | Falsa | `-1` |

**Aquí hay tres recorridos y no cuatro porque, cuando se cumple la primera condición, la función termina antes de llegar a la segunda.**

## 5. La confusión importante: CC no cuenta todas las combinaciones

En el ejemplo anterior, CC coincide con el número total de recorridos. **Eso no ocurre siempre.**

Mira este ejemplo sin retornos anticipados:

```python
def preparar_pedido(con_descuento, con_envio):
    if con_descuento:
        aplicar_descuento()

    if con_envio:
        agregar_envio()
```

Considerando solo las decisiones de esta función, tiene dos decisiones y **CC = 3**. Sin embargo, hay cuatro combinaciones:

| Descuento | Envío |
|---|---|
| No | No |
| Sí | No |
| No | Sí |
| Sí | Sí |

### ¿Por qué CC vale 3 y no 4?

Porque cuenta una **base de caminos independientes**, no todas sus combinaciones. Puedes entender esa base, de manera intuitiva, con tres recorridos:

1. No aplicar descuento ni agregar envío.
2. Aplicar solo descuento: incorpora la rama del descuento.
3. Agregar solo envío: incorpora la rama del envío.

El cuarto recorrido combina ramas ya presentes en los anteriores; no añade otro camino linealmente independiente.

> [!warning] Esto no significa que basten tres pruebas
> La combinación «descuento y envío» podría revelar un error de interacción. Además, hay valores límite, entradas inválidas y reglas del negocio que CC no describe. **CC no es una receta exacta para decidir cuántas pruebas necesitas.**

Por la misma razón, cuatro decisiones binarias independientes en secuencia pueden producir **16 combinaciones**, aunque su **CC sea 5**. Un bucle también puede repetirse muchas veces sin hacer infinita la CC.

## 6. Para qué sirve y qué no te dice

CC es una **señal para investigar**, no una calificación completa del código o de la arquitectura.

- **Para entender:** muchas decisiones pueden hacer difícil seguir la lógica.
- **Para probar:** más ramas suelen exigir considerar más situaciones.
- **Para modificar:** cambiar una regla puede afectar recorridos que no habías considerado.

Pero CC no mide si los nombres son claros, si el modelo del negocio es adecuado, cuánto tarda el programa ni cuántos servicios intervienen en un cambio.

Tampoco distingue entre:

- **Complejidad esencial:** el negocio realmente exige muchas reglas diferentes.
- **Complejidad accidental:** la implementación añade enredos innecesarios, por ejemplo, validaciones repetidas y responsabilidades mezcladas.

Dos funciones con la misma CC pueden ser muy distintas en claridad y calidad.

### ¿Qué valor se considera demasiado alto?

El libro menciona un umbral habitual inferior a 10 y la preferencia de los autores por valores inferiores a 5. **Son orientaciones del texto, no leyes universales.** Un valor alto invita a revisar la función; no demuestra por sí solo que esté mal.

Como caso extremo, el libro relata una función de más de 4 000 líneas con CC superior a 800. También menciona Crap4J, que combina complejidad y cobertura de pruebas; no necesitas esa herramienta para entender el concepto.

## 7. Cómo mejorar sin hacer trampa con el número

Si una función valida datos, calcula precios y gestiona el envío, separar esas responsabilidades en funciones coherentes puede facilitar su comprensión.

Pero **extraer cada rama a otra función únicamente para bajar CC no garantiza una mejora**. Las decisiones pueden seguir existiendo, solo que repartidas en otros lugares.

Después de refactorizar, pregunta:

- ¿Cada función tiene una responsabilidad clara?
- ¿Sus nombres explican qué hacen?
- ¿Es más fácil seguir el comportamiento completo?
- ¿Las pruebas siguen verificando las reglas y sus interacciones?

El libro relaciona **TDD** (*test-driven development*, desarrollo guiado por pruebas) con funciones pequeñas y enfocadas. Su ciclo consiste en escribir una prueba que falle, añadir el código suficiente para hacerla pasar y refactorizar conservando las pruebas. Puede favorecer esa estructura, pero no la garantiza.

## 8. Detalle técnico: calcular CC con un grafo

Esta sección explica la fórmula de la nota original. **No necesitas memorizarla para comprender la idea principal.**

Un grafo de control es un dibujo del recorrido del código:

- Las **cajas o nodos** representan condiciones, bloques de instrucciones, entrada o salida.
- Las **flechas o aristas** representan los pasos posibles entre ellos.

![Figura 6-1 recreada: grafo de control con complejidad ciclomática tres](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c06-03-complejidad.png)

**Procedencia:** recreación didáctica del ejemplo 6-1 y la figura 6-1, p. 84. Se han explicitado todas las salidas y una salida común para contar el grafo sin ambigüedad.

Para una sola función, con entrada y salida tratadas de forma consistente:

$$CC = E - N + 2.$$

- **N = 7 nodos:** Inicio, dos condiciones, tres retornos y Fin.
- **E = 8 aristas:** las ocho flechas que conectan esos nodos.

Por tanto:

$$CC = 8 - 7 + 2 = 3.$$

Es el mismo resultado que obtuvimos contando **dos decisiones + 1**. Las tres ramas de retorno se conectan con Fin en el dibujo, aunque una ejecución solo recorra una de ellas.

**No sustituyas líneas de código por nodos ni cantidad de `if` por aristas:** debes contar los elementos del grafo construido.

> [!note]- Precisión sobre el ejemplo impreso
> El ejemplo impreso usa una firma `void` junto con retornos de valores, y los rótulos de retorno de la figura no representan claramente las mismas ramas que el código. Aquí se conserva la lógica de las condiciones y se usan retornos coherentes. El resultado CC = 3 coincide. El cálculo reducido «3 − 2 + 2» del texto no se reutiliza como conteo de este grafo ampliado.

> [!note]- Fórmula para varios componentes
> La fórmula general `E − N + 2P` usa `P` como número de componentes conexas de los grafos analizados, bajo la convención apropiada. No es el número de métodos llamados. Para el único grafo de este ejemplo, `P = 1`.

## Qué debes recordar

> [!summary] En una frase
> **La complejidad ciclomática mide los caminos independientes creados por las decisiones de una función; ayuda a orientar revisiones y pruebas, pero no cuenta todas las combinaciones posibles ni garantiza que el código sea correcto.**

En los ejemplos simples, recuerda **CC = decisiones + 1**. En el ejemplo de `c1` y `c2`, eso da **3**. Probar sus tres recorridos sigue sin cubrir todos los valores: también conviene revisar límites como `c1 = 100` y una suma exactamente igual a `500`.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/02 Medidas operativas y rendimiento|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/04 Medidas de proceso y testabilidad|Siguiente →]]
