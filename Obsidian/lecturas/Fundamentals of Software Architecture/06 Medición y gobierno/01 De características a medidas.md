---
title: "06 · De características arquitectónicas a medidas compartidas"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/medicion
---

# De características arquitectónicas a medidas compartidas

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, capítulo 6. **PDF 1–2 · impresas 81–82** del [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf|PDF conservado]]. «Libro» identifica sus planteamientos; las ampliaciones, plantillas y datos supuestos se señalan como elaboración didáctica.

Una característica arquitectónica sirve para orientar decisiones, pero su nombre no basta para comprobar que el sistema la cumple. «Rápido», «ágil» o «fácil de desplegar» pueden expresar deseos legítimos y, al mismo tiempo, significar cosas distintas para desarrollo, operaciones y negocio. El capítulo plantea un paso decisivo: **acordar qué significa una característica y buscar evidencia objetiva de que se conserva**.

## Tres obstáculos que identifica el libro

| Obstáculo | Qué ocurre | Cómo empezar a resolverlo |
|---|---|---|
| No son magnitudes físicas bien definidas | «Muy rápido» no tiene unidad ni procedimiento de medición | Convertir el adjetivo en un comportamiento observable |
| Las definiciones cambian entre equipos | Backend mide respuesta de API y producto mide cuándo se puede usar la pantalla | Acordar alcance, punto inicial y punto final |
| Muchas características son compuestas | «Agilidad» reúne modularidad, testabilidad y desplegabilidad | Descomponerla antes de medir |

La solución propuesta por el libro combina **lenguaje compartido** y **descomposición**. No pretende que toda cualidad humana pueda reducirse a una cifra. Busca que, cuando alguien diga «la desplegabilidad empeoró», otras personas puedan examinar el mismo fenómeno y discutir con evidencia.

## Gráfico: el recorrido desde la intención hasta la decisión

![Del significado de una característica a su medición y gobierno](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c06-01-medicion.png)

**Procedencia:** esquema propio que desarrolla el razonamiento de las pp. 81–82.

El recorrido empieza arriba a la izquierda, avanza hacia la derecha y regresa por la fila inferior. Las cajas superiores transforman una necesidad en una definición. Las inferiores incorporan contexto, producen evidencia y llevan a una decisión. La flecha azul vuelve a la descomposición porque descubrir una medida inútil obliga a revisar la definición.

**Secuencia causal:** si «cambiar rápido» depende de probar y desplegar, conviene observar ambos pasos. Si el despliegue tarda poco pero recuperar un fallo tarda horas, una sola medida de duración no representa toda la necesidad. La evidencia permite corregir el sistema o mejorar la regla cuando esta describe mal el problema.

**Conclusión:** una métrica es útil cuando conecta una preocupación con una decisión. **Límite:** el diagrama no establece umbrales universales ni garantiza que una medición sea causal; un aumento de tiempo puede tener varias causas.

## Ficha para convertir una característica en algo verificable

Esta ficha es una **ampliación didáctica**; el libro no presenta esta plantilla literal.

1. **Propiedad:** qué se quiere preservar. Ejemplo: desplegabilidad del servicio de pedidos.
2. **Escenario:** qué cambio, en qué ambiente y con qué carga. Ejemplo: nueva versión compatible con la base de datos existente.
3. **Indicador:** qué se observará. Ejemplo: tiempo desde iniciar el despliegue hasta que la versión pasa comprobaciones de salud.
4. **Unidad y población:** minutos por despliegue; todos los despliegues de producción del mes.
5. **Criterio:** qué se considera aceptable. Ejemplo supuesto: al menos 19 de 20 despliegues terminan en menos de 10 minutos.
6. **Mecanismo:** cómo se recoge la evidencia y quién revisa las excepciones.
7. **Respuesta:** qué se hará si no cumple, y cuándo se revisará el criterio.

Los números del ejemplo son inventados. La ficha obliga a descubrir ambigüedades: ¿cuenta un despliegue cancelado?, ¿«terminar» implica servir tráfico?, ¿se considera exitoso si requiere corrección inmediata? Si no se aclaran estas preguntas, dos equipos pueden obtener cifras incompatibles con los mismos eventos.

## Característica, medida, umbral y función de aptitud

No son sinónimos. **Rendimiento** es una característica; **latencia observada** es una medida; **p95 menor o igual a 300 ms** es un criterio; **ejecutar un escenario y comprobar ese criterio** puede funcionar como una función de aptitud. El umbral no es parte inevitable de toda métrica, y una función de aptitud también puede comprobar una regla estructural sin medir tiempo alguno, como «no existen ciclos entre paquetes».

Medir es describir un estado. Gobernar es preservar principios a través del tiempo con mecanismos que detectan desviaciones y permiten actuar. Un tablero que nadie mira conserva datos, pero por sí solo no constituye un proceso eficaz de gobierno.

## Ejercicio resuelto

**Enunciado:** un equipo pide «mejorar la agilidad un 20 %». ¿Es ya una condición comprobable?

**Respuesta:** no. Falta definir qué componente de la agilidad cambia, la referencia inicial y la forma de medir. Una reformulación posible sería: «en el escenario de despliegue habitual, reducir la mediana de duración de 10 a 8 minutos, sin empeorar la proporción de despliegues exitosos». La reducción es `(10 − 8) / 10 = 20 %`. Esa mejora afecta una dimensión de la desplegabilidad; **no demuestra por sí sola que toda la organización sea un 20 % más ágil**.

**Para comprobar que lo entendiste:** explica por qué elegir una herramienta de monitoreo antes de definir el fenómeno puede producir muchas métricas y poco conocimiento.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/02 Medidas operativas y rendimiento|Siguiente →]]
