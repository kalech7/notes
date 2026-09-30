---
title: "12 · Gobierno con etiquetas y pruebas"
created: 2026-09-29
capitulo: 12
tags:
  - lecturas/software-architecture
  - arquitectura/pipeline
---

# Gobierno con etiquetas y pruebas

[[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/00 Índice|← Índice del capítulo 12]]

**Gobernar el pipeline significa conservar el propósito de cada etapa mientras el código cambia.** El capítulo propone identificar explícitamente el rol de los filtros; también reconoce que probar automáticamente su significado completo es difícil.

## 1. Dos tipos de gobierno

El gobierno **operativo** depende del caso: tiempos de respuesta, disponibilidad, capacidad y demás características deben medirse según requisitos concretos. El gobierno **estructural** protege la organización: cada filtro conserva una responsabilidad y un papel en el flujo.

Una regla puede comprobar que un productor no recibe conexiones de otros filtros. Es mucho más difícil demostrar solo con análisis estático que un transformador «calcula tendencias y nada más». El código puede esconder una validación de negocio en un método auxiliar o realizar efectos laterales no declarados.

**Análisis estático** es examinar el código sin ejecutarlo; **metadatos** son datos que describen una clase o componente. Los metadatos ayudan a explicitar intención, pero no equivalen a probar comportamiento.

## 2. La propuesta del libro: etiquetas de rol

El capítulo usa anotaciones en Java y atributos personalizados en C#. Declara un conjunto de valores: `PRODUCER`, `TESTER`, `TRANSFORMER`, `CONSUMER`. El tipo permite varios valores, aunque el objetivo del estilo siga siendo una responsabilidad definida por filtro.

En Java, el ejemplo de la fuente define `@Filter`, con una propiedad `value()` que recibe un arreglo de roles. `@Retention(RetentionPolicy.RUNTIME)` conserva la anotación durante ejecución; `@Target(ElementType.TYPE)` permite aplicarla a tipos. La etiqueta no ejecuta por sí sola la transformación: la clase conserva el trabajo real.

Una segunda etiqueta, `@FilterEntrypoint`, marca la **clase de entrada** del filtro. Es útil cuando el componente tiene varias clases: el rol se asocia a la puerta por la que otros componentes lo utilizan, no a todas sus clases auxiliares indiscriminadamente.

El ejemplo de uso del analizador se puede expresar así, con las etiquetas definidas por el libro:

```java
@FilterEntrypoint
@Filter(Filter.FilterType.TRANSFORMER)
public class TrendAnalyzerFilter {
    // La implementación realiza el análisis de tendencias.
}
```

Se califica el enum como `Filter.FilterType` porque el libro lo define anidado dentro de `Filter`. El fragmento describe intención y requiere las definiciones/importaciones correspondientes; no constituye un programa autónomo.

## 3. Precisión en el ejemplo de C#

La definición impresa de C# declara un campo de roles, pero después usa `[Filter(FilterType.TRANSFORMER)]` sin mostrar el constructor que recibe ese argumento. Copiar los fragmentos como código completo deja una definición insuficiente para ese uso. Esta variante propia hace explícita la pieza que falta:

```csharp
using System;

public enum FilterType { Producer, Tester, Transformer, Consumer }

[AttributeUsage(AttributeTargets.Class)]
public sealed class FilterAttribute : Attribute
{
    public FilterType Role { get; }
    public FilterAttribute(FilterType role) => Role = role;
}

[AttributeUsage(AttributeTargets.Class)]
public sealed class FilterEntrypointAttribute : Attribute { }

[FilterEntrypoint]
[Filter(FilterType.Transformer)]
public sealed class TrendAnalyzerFilter { }
```

Los argumentos posicionales de un atributo se reciben en su constructor, como explica [Microsoft Learn](https://learn.microsoft.com/en-us/dotnet/csharp/advanced-topics/reflection-and-attributes/creating-custom-attributes). Esta versión conserva un único rol para hacer explícita la intención del componente. El atributo `FilterEntrypoint` señala la clase de entrada; `Filter` declara que transforma. No impide que alguien escriba dentro una regla indebida: ese comportamiento sigue necesitando revisión y pruebas. El código de la fuente ilustra el enfoque; esta variante corrige su definición, no es una transcripción.

## 4. Qué puede comprobarse realmente

| Evidencia | Qué protege | Qué no demuestra |
|---|---|---|
| Rol y punto de entrada declarados | Intención visible y localizable | Que todo el código cumpla esa intención |
| Reglas de dependencias | Ausencia de accesos prohibidos a internos | Corrección del cálculo |
| Pruebas de contrato | Formatos, campos y unidades compatibles | Todas las situaciones de negocio |
| Casos de comportamiento | Criterios y resultados seleccionados | Comportamiento sobre cualquier entrada |
| Métricas en operación | Latencia, fallos y acumulación observables | Buena modularidad por sí sola |

Esta tabla amplía el gobierno del capítulo. Una política útil combina pruebas mecánicas con revisión del propósito. Una etiqueta sin consumidores que la inspeccionen es documentación; una prueba que la usa puede hacerla parte de una regla automatizada.

## 5. Un acuerdo de equipo aplicable

Para cada filtro, registrar entrada, salida, rol, efectos externos y errores esperados. Al revisar un cambio, preguntar qué nuevo motivo de cambio introduce. Si el analizador ahora consulta clientes para decidir quién puede ejecutar el informe, probablemente apareció una responsabilidad de autorización que conviene ubicar explícitamente.

Conectar dos filtros que comparten el mismo contrato puede ser seguro; hacer que uno acceda a clases internas de otro reduce la independencia. La disciplina importa incluso dentro de un proceso, donde la llamada sería técnicamente fácil.

> [!question]- ¿La etiqueta `Transformer` garantiza que no se descarte ningún registro?
> No. Declara intención. Para comprobarla hacen falta reglas o pruebas que examinen el comportamiento esperado, y una revisión de los casos que esas pruebas no cubren.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/09 Arquitectura pipeline.pdf#page=6|PDF 6–8 · impresas 186–188 · anotaciones, atributos y punto de entrada]]

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/05 Riesgos errores y recuperación|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/12 Arquitectura pipeline/07 Equipos características y elección|Siguiente →]]
