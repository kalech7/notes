---
title: "06 · Gobernar capas: del dibujo a una regla ejecutable"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/medicion
---

# Gobernar capas: del dibujo a una regla ejecutable

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, capítulo 6. **PDF 10–12 · impresas 90–92** del [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf|PDF conservado]]. «Libro» identifica sus planteamientos; las ampliaciones, plantillas y datos supuestos se señalan como elaboración didáctica.

Un diagrama de capas comunica intención, pero el código puede violarla si nadie comprueba las dependencias. Una llamada directa desde una capa superior a persistencia quizá resuelva una tarea inmediata mientras salta una frontera que el diseño necesitaba conservar. El capítulo presenta ArchUnit y NetArchTest como ejemplos de herramientas capaces de comprobar estas relaciones.

## Figura 6-4: estructura y dependencias

![Figura 6-4 recreada: cuatro capas y reglas de acceso](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c06-07-capas.png)

**Procedencia:** a la izquierda, recreación de la composición de la figura 6-4, p. 91: presentación, controlador, servicio, persistencia y base de datos. A la derecha, ampliación de las reglas del ejemplo 6-4.

En la parte izquierda, la caja grande representa un monolito organizado en capas; los rectángulos apilados representan responsabilidades, no procesos independientes. La base de datos se dibuja fuera del bloque. La flecha bidireccional entre persistencia y base representa interacción de datos; no equivale a que la base importe código de persistencia.

En la parte derecha, las flechas continuas son dependencias permitidas: controlador puede usar servicio y servicio puede usar persistencia. La flecha roja discontinua representa el salto directo controlador → persistencia que esas reglas pretenden evitar. Aquí las flechas sí representan uso o dependencia, no el sentido en que viaja una respuesta HTTP.

**Secuencia causal:** al exigir que acceso a persistencia pase por servicio, se preserva un punto donde residen las reglas de negocio. Una consulta directa desde controlador puede saltarse validación, coordinación o invariantes que ese servicio aplica. El análisis detecta la relación prohibida antes de que se normalice como práctica.

**Conclusión:** el dibujo gana capacidad de gobierno cuando las relaciones relevantes se convierten en reglas comprobables. **Límite:** esas relaciones corresponden al ejemplo y no demuestran que todas las arquitecturas deban usar cuatro capas. Una arquitectura diferente puede justificar otros límites.

## Qué expresa realmente el ejemplo de ArchUnit

El código del libro define tres capas mediante patrones de paquetes y limita quién puede acceder a ellas. Traducido a reglas legibles:

1. Entre las capas declaradas por esa comprobación, ninguna debe acceder a controlador.
2. Solo controlador debe acceder a servicio.
3. Solo servicio debe acceder a persistencia.

La dirección de lectura importa. **«Servicio solo puede ser accedido por controlador»** restringe dependencias entrantes a servicio; no significa «servicio solo puede acceder a controlador». Confundir ambas frases invierte el diseño.

> [!note] Dibujo y alcance de la prueba
> La figura del libro incluye presentación, pero el fragmento de ArchUnit declara controlador, servicio y persistencia. Por ello no debe afirmarse que ese fragmento por sí solo gobierna exhaustivamente las cuatro capas. En una implementación real hay que precisar qué clases entran al análisis, cómo se trata presentación y qué accesos quedan fuera de las capas declaradas.

En estas notas se explica la intención del ejemplo; no se presenta su sintaxis histórica como una implementación verificada contra una versión actual de la biblioteca.

## Transformación a un verificador conceptual

```text
clasificar clases en capas según paquetes acordados
extraer dependencias entre clases incluidas
para cada dependencia origen -> destino:
    si origen y destino están en capas gobernadas diferentes:
        comprobar que la pareja (origen, destino) está permitida
si hay infracciones:
    mostrar clase origen, clase destino y regla incumplida
```

La implementación debe decidir qué cuenta como dependencia: uso de un tipo, llamada a método, herencia, anotación u otros vínculos. También debe distinguir una regla intercapas de relaciones internas permitidas. Sin esa definición, el equipo no puede anticipar qué fallará.

**Ejemplo supuesto:** `PedidoController` empieza a importar `PedidoRepository`. Si pertenecen a controlador y persistencia respectivamente, la comprobación falla. La corrección no consiste en renombrar el paquete para engañar al detector, sino en evaluar si el acceso debe pasar por un servicio existente o si la regla arquitectónica requiere una revisión razonada.

## El ejemplo de NetArchTest

La p. 92 muestra una comprobación equivalente en intención para .NET: las clases de presentación no deben depender directamente del espacio de nombres de datos. Se selecciona un conjunto de tipos, se expresa una restricción y se evalúa el resultado.

Es importante distinguir **calcular un resultado booleano** de **hacer que la prueba falle**. En el fragmento del libro, la cadena termina en `IsSuccessful`; para integrarla en una prueba completa debe consumirse ese resultado mediante una aserción o un mecanismo equivalente. Guardar `false` en una variable e ignorarlo no bloquea un cambio. Esta observación es una precisión didáctica del fragmento.

## Qué logra y qué puede escaparse

Un análisis estático detecta dependencias representadas en el código o artefactos analizados. Puede no detectar algunos vínculos creados por cadenas de texto, reflexión, configuración externa o acceso directo a un recurso compartido. Por ejemplo, dos servicios que comparten una tabla pueden estar muy acoplados aunque no importen clases entre sí.

Tampoco comprueba que las responsabilidades estén bien colocadas: un servicio puede tener lógica incorrecta aun cumpliendo la dirección de dependencia. Por eso estas funciones son piezas de gobierno y necesitan complementarse con pruebas de comportamiento y revisión de límites.

## Ejercicio resuelto

**Casos:** A) controlador usa servicio; B) servicio usa persistencia; C) persistencia usa servicio; D) controlador usa persistencia.

**Resultado según las reglas del ejemplo:** A y B son admisibles. C viola la regla de que servicio solo sea accedido por controlador. D viola la regla de que persistencia solo sea accedida por servicio. La razón no es que C y D necesariamente fallen al ejecutarse; es que erosionan las relaciones que el equipo decidió conservar.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/06 Ciclos y distancia a la secuencia principal|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/08 Gobierno en operación y práctica integradora|Siguiente →]]
