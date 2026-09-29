---
title: "06 · Gobierno arquitectónico y funciones de aptitud"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/medicion
---

# Gobierno arquitectónico y funciones de aptitud

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, capítulo 6. **PDF 6–8 y 13 · impresas 86–88 y 93** del [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf|PDF conservado]]. «Libro» identifica sus planteamientos; las ampliaciones, plantillas y datos supuestos se señalan como elaboración didáctica.

Las prioridades arquitectónicas suelen ser importantes a largo plazo y poco urgentes hoy. Una dependencia que rompe los límites entre módulos puede ahorrar minutos en una tarea y acumular meses de dificultad futura. **Gobernar** consiste en orientar el desarrollo para conservar las propiedades que justificaron el diseño, incluso bajo presión de entrega.

El capítulo describe una continuidad entre automatización de pruebas, integración continua, prácticas de operación y gobierno arquitectónico. La automatización permite comprobar reglas repetidamente, con menor dependencia de que una persona recuerde revisar todos los detalles.

## Qué es una fitness function

Una **función de aptitud arquitectónica** es un mecanismo que proporciona una evaluación objetiva de la integridad de una característica arquitectónica o de una combinación de ellas. «Función» no obliga a que sea una fórmula matemática: puede materializarse en una prueba, un análisis, un monitor o un experimento.

El término proviene del razonamiento de computación evolutiva. El libro usa el problema del viajante: una solución candidata puede evaluarse por distancia, costo y duración. Las medidas guían hacia objetivos, pero no deciden por sí solas cómo conciliar todos los intereses. En arquitectura, una verificación cumple un papel semejante: informa si el cambio conserva una propiedad deseada.

## Figura 6-2: mecanismos posibles

![Figura 6-2 recreada: mecanismos de las funciones de aptitud](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c06-04-mecanismos.png)

**Procedencia:** recreación en español de la composición de círculos de la figura 6-2, p. 88.

El círculo central se superpone a métricas, monitores, pruebas y caos. No hay flechas ni orden temporal. Los círculos indican familias de mecanismos que pueden participar en una función de aptitud. «Otros» representa que la lista no es exhaustiva.

**Relación explicada:** una prueba unitaria que calcula impuestos verifica comportamiento funcional. Una prueba ejecutada con un framework similar que comprueba ausencia de ciclos evalúa una propiedad arquitectónica. La herramienta puede ser la misma; cambia la intención de lo que evalúa. Un monitor de latencia puede evaluar un presupuesto operativo, mientras un experimento de fallo evalúa la capacidad de recuperación.

**Conclusión:** fitness function es una forma de usar mecanismos existentes, no un framework único que deba descargarse. **Límites:** las áreas de los círculos y sus solapamientos no representan porcentajes, conjuntos matemáticos exactos ni cuánto invertir en cada técnica.

## Anatomía de una función útil

Como ampliación didáctica, conviene escribir estos elementos antes de implementarla:

| Elemento | Ejemplo de modularidad |
|---|---|
| Intención | Mantener módulos sustituibles y comprensibles |
| Objeto analizado | Dependencias entre paquetes de negocio |
| Regla observable | No debe existir un ciclo dirigido |
| Mecanismo | Construir grafo de dependencias y detectar ciclos |
| Frecuencia | Cada integración de código |
| Evidencia del fallo | Ruta concreta `pedidos → pagos → pedidos` |
| Respuesta | Corregir el acoplamiento o revisar justificadamente el límite |
| Responsable | Equipo y arquitectura acuerdan la regla y sus excepciones |

El mensaje de fallo importa. «Arquitectura inválida» obliga a adivinar. Mostrar la dependencia infractora y explicar el principio facilita corregirla. Una regla cuya intención nadie entiende termina deshabilitada o eludida.

## Medición, evaluación y acción

Estos pasos deben distinguirse. Un análisis puede producir CC = 17; una regla del proyecto puede pedir revisar métodos por encima de 10; el equipo puede descubrir complejidad esencial y aceptar temporalmente ese caso con una explicación. La regla se vuelve útil cuando la evidencia desencadena una acción proporcionada. Ser objetivo no significa que el umbral deba ignorar contexto.

El libro insiste en que arquitectos y desarrolladores deben colaborar. No propone que arquitectura redacte reglas esotéricas y las imponga desde una posición distante. Una función de aptitud debe preservar razones comprendidas por las personas que la mantienen.

## La analogía de la lista de verificación

En las páginas finales se compara este enfoque con listas usadas por profesionales que realizan trabajos complejos. La lista no implica desconocimiento: recuerda aspectos que pueden omitirse mientras compiten muchas prioridades. De forma semejante, una verificación automatizada hace persistente un principio como «no introducir una dependencia inversa».

Una función de aptitud tampoco reemplaza revisión de diseño, conversación o criterio. Una suite que comprueba solo ciclos no puede asegurar latencia, seguridad, resiliencia y costos. **Pasa** debe leerse como «satisface las reglas verificadas dentro del alcance observado», no como «arquitectura correcta en todo sentido».

## Ejercicio resuelto

**Enunciado:** el sistema tiene tres mecanismos: un test de descuentos, un monitor de tiempo de respuesta y un análisis de dependencias. ¿Cuáles son funciones de aptitud?

**Respuesta razonada:** depende de su uso. El test de descuentos es principalmente una comprobación funcional. El monitor puede funcionar como función de aptitud si evalúa la característica de rendimiento acordada. El análisis lo es si evalúa la integridad de modularidad. Una medición sin relación con un objetivo arquitectónico no adquiere automáticamente esa función por usar una herramienta sofisticada.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/04 Medidas de proceso y testabilidad|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/06 Ciclos y distancia a la secuencia principal|Siguiente →]]
