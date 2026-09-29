---
title: "Capítulo 7 · Anatomía de un quantum"
created: 2026-09-28
capitulo: 7
orden: 2
tags:
  - lecturas/software-architecture
  - arquitectura/quanta
---

# Anatomía de un quantum

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Capítulo 7 · Alcance y quanta]] · Nota 2 de 7

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, segunda edición, capítulo 7. Fuente local: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Las páginas PDF se cuentan desde el archivo suministrado; la impresa aparece en el libro. «Elaboración» y «ampliación didáctica» identifican material propio.

**Objetivo:** reconocer un quantum por sus propiedades y no por el número de cajas del dibujo.

## Las piezas de la definición

**Libro — PDF pp. 2–5, impresas 96–99.** Un quantum establece el alcance de un conjunto de características arquitectónicas, especialmente operacionales. La edición proporcionada enumera despliegue independiente, alta cohesión funcional, bajo acoplamiento estático externo de implementación y comunicación síncrona con otros quanta como aspectos que deben analizarse.

| Aspecto | Qué quiere decir | Error que evita |
|---|---|---|
| Despliegue independiente | La unidad incluye los elementos necesarios para funcionar independientemente de otras partes. | Contar solo el ejecutable y olvidar sus datos. |
| Alta cohesión funcional | Sus elementos contribuyen a un propósito reconocible del dominio. | Agrupar funciones arbitrarias porque son «utilidades». |
| Bajo acoplamiento estático externo | Las dependencias de implementación no atan fuertemente esa unidad a las demás. | Confundir separación física con independencia real. |
| Comunicación y operación | Hay que estudiar qué sucede al interactuar con otros quanta, en particular si se espera una respuesta. | Suponer que los límites del despliegue aíslan todo comportamiento operacional. |

> [!important] Particularidad de esta edición
> El texto contempla **comunicación síncrona entre quanta**. No se debe sustituir su definición por la regla «toda llamada síncrona convierte automáticamente ambos servicios en un único quantum». La comunicación puede afectar los límites y las características observadas; hay que analizar el caso. La nota siguiente sobre sincronía desarrolla esa diferencia.

## Desplegar una parte no equivale a que funcione sola

Un archivo binario, una imagen de contenedor o un proceso son artefactos de implementación. El quantum responde a otra pregunta: ¿qué conjunto mínimo coherente necesita la capacidad para operar? Si un servicio depende de una base de datos, esa dependencia forma parte del análisis. El libro señala que los sistemas tradicionales ligados a una única base suelen formar un solo quantum.

**Precisión didáctica:** aquí «base compartida» alude al punto de dependencia común que muestra el libro, como un esquema o datos de los que dependen varias partes. Alojar bases lógicamente separadas en un mismo servidor o proveedor no permite fusionar automáticamente todos sus quanta. La infraestructura común puede introducir riesgos correlacionados, que se deben describir, pero no sustituye el análisis de los límites y dependencias.

Esto no afirma que todo elemento tenga que vivir en la misma máquina o que se reinstale la base con cada versión. Describe un límite arquitectónico: qué elementos están unidos por dependencias necesarias y restricciones de evolución.

![01 limites](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-01-limites.png)

## Explicación del gráfico: el almacenamiento cambia el alcance

**Procedencia:** diagrama didáctico propio basado en PDF pp. 2–5 / impresas 96–99; no es una figura numerada del libro.

1. **A la izquierda**, Catálogo y Envíos son dos servicios representados con cajas. Las flechas apuntan a la base de datos común, dibujada como un cilindro: ambos dependen de ella.
2. El **contorno punteado único** señala que, en el modelo del libro, el punto compartido los vincula dentro del mismo quantum. Un cambio incompatible de esquema puede perjudicar a ambos.
3. **A la derecha**, cada servicio dispone de sus propios datos dentro de un contorno diferente. Se han eliminado las dependencias compartidas del dibujo, pero queda una comunicación mediante contrato explícito.
4. Esa flecha horizontal exige analizar compatibilidad y funcionamiento. No prueba por sí misma ni independencia absoluta ni fusión obligatoria.

**Conclusión:** contar dos servicios no permite concluir que hay dos quanta. Hay que inspeccionar lo que comparten y cómo funcionan. **Límite:** el segundo dibujo es una hipótesis simplificada; omite bibliotecas, infraestructura, mecanismos de despliegue y dependencias adicionales que podrían cambiar el diagnóstico.

## Cohesión y contexto delimitado

El libro conecta la alta cohesión con el **diseño guiado por el dominio** (*Domain-Driven Design*, DDD): modelar el software a partir de las reglas y el lenguaje del negocio. Su **bounded context**, o contexto delimitado, establece dónde un modelo y sus términos conservan un significado preciso. Dentro de un contexto, un modelo expresa con precisión una parte del negocio; fuera de él, se comunica mediante límites explícitos. Por ejemplo, «cliente» puede significar algo diferente para ventas y para facturación.

La explicación del texto no obliga a construir una clase Cliente universal. Compartir un modelo único por toda la organización puede introducir coordinación y cambios en cascada. Modelos locales permiten que cada dominio evolucione conforme a sus reglas y que las diferencias se resuelvan en la comunicación.

**Ampliación didáctica:** contexto delimitado, servicio y quantum describen perspectivas relacionadas pero diferentes: significado del dominio, forma de implementación y alcance arquitectónico. A menudo coinciden, pero no hay una equivalencia automática uno a uno. La figura de Going Green mostrará varios servicios dentro de un mismo quantum.

## Una prueba conceptual útil

Explica el propósito de la unidad en una oración; enumera las dependencias sin las que no funciona; identifica qué cambios externos pueden romperla; y describe qué promesas de operación dependen de otros participantes. Si solo puedes responder «es el contenedor X», todavía no has analizado el quantum.


---

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/01 El alcance de las características|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/03 Cuatro formas de acoplamiento|Siguiente →]]
