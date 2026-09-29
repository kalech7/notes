---
title: "Capítulo 7 · Nube aplicación y repaso"
created: 2026-09-28
capitulo: 7
orden: 7
tags:
  - lecturas/software-architecture
  - arquitectura/quanta
---

# Nube aplicación y repaso

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Capítulo 7 · Alcance y quanta]] · Nota 7 de 7

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, segunda edición, capítulo 7. Fuente local: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Las páginas PDF se cuentan desde el archivo suministrado; la impresa aparece en el libro. «Elaboración» y «ampliación didáctica» identifican material propio.

**Objetivo:** aplicar los límites arquitectónicos cuando parte de las capacidades se delega a la nube y comprobar que puedes razonar sobre todo el capítulo.

## La nube también entra en el análisis del alcance

**Libro — PDF pp. 11–12, impresas 105–106.** Los recursos de nube encapsulan muchas capacidades operacionales. Esto cambia la forma de obtenerlas, pero no elimina la necesidad de analizar compromisos. El capítulo diferencia dos escenarios.

| Uso de la nube | Qué debe analizar el arquitecto |
|---|---|
| **Alojar y orquestar contenedores** | Características de los contenedores y restricciones de la herramienta de orquestación; el libro menciona Kubernetes como ejemplo. |
| **Componer la solución con recursos del proveedor** | Capacidades anunciadas y mantenidas por servicios como funciones activadas por eventos o bases de datos. |

El libro recuerda que características que hoy parecen opciones de configuración, como elasticidad, antes exigieron mucho trabajo en infraestructura física. La facilidad de configuración desplaza parte del esfuerzo, pero quedan compromisos como disponibilidad del proveedor y seguridad.

## Diagrama de las dos formas de delegación

![Dos formas de delegar capacidades en la nube](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-09-nube-delegacion.png)

*Diagrama didáctico redibujado en PNG; fuente lógica editable: [c07-09-nube-delegacion.mmd](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-09-nube-delegacion.mmd).*

Las cajas distinguen decisiones y capas de responsabilidad, no procesos simultáneos. Las dos ramas son escenarios del capítulo; una solución real también puede combinarlos. Las flechas muestran qué aspectos condicionan la evaluación. Ambas ramas desembocan en observar el resultado de la capacidad del negocio.

**Conclusión:** alojar en nube no convierte automáticamente una parte en un quantum independiente ni prueba una característica. **Límite:** este esquema propio no describe un producto concreto ni garantiza capacidades actuales de ningún proveedor. Su objetivo es organizar la lectura del capítulo, no ofrecer una recomendación de infraestructura.

## Aplicación a Going Green

**Ampliación didáctica.** Supongamos que Evaluación corre como una función administrada y utiliza un almacén propio. Tener un recurso separado no basta para concluir que escala sin límites. Habría que revisar la capacidad efectiva del almacén, concurrencia, restricciones del servicio y forma de comunicación.

Si la parte pública invoca Evaluación y espera su resultado, el usuario percibe el comportamiento de ambos. Si se adopta una solicitud asíncrona, puede ser necesario mostrar un estado pendiente. En ambos casos se conserva la pregunta del capítulo: ¿qué componentes y dependencias deben satisfacer las características de este recorrido?

Estas son hipótesis de estudio, no detalles de la kata original. La fuente no establece que GG use funciones administradas ni determina un proveedor.

## Método de repaso en seis preguntas

1. **Propósito:** ¿qué capacidad concreta ofrece la unidad?
2. **Características:** ¿cuáles son sus prioridades y mínimos?
3. **Dependencias:** ¿qué necesita para funcionar y qué comparte?
4. **Límite:** ¿dónde está el quantum candidato y por qué?
5. **Interacción:** ¿cómo cambian las propiedades observadas al llamar a otros?
6. **Evidencia:** ¿cómo se comprobarían despliegue, comportamiento y límites?

La secuencia es una herramienta didáctica propia que integra las ideas de las páginas 95–106. No es una lista textual del libro.

## Ejercicio de diagnóstico con solución

**Enunciado propio.** Oferta, Estado y Evaluación están en tres contenedores. Oferta y Estado leen una base compartida. Evaluación tiene su propio almacén. Oferta solicita una valoración y espera la respuesta. Los equipos afirman: «Hay tres contenedores, por tanto tres quanta totalmente independientes».

**Solución:** la conclusión no se sostiene. En el modelo del capítulo, Oferta y Estado están ligados por la base compartida y constituyen un único quantum candidato. Evaluación puede representar otro si se verifica su independencia y cohesión. El recorrido de Oferta depende operacionalmente de Evaluación por la espera síncrona. Eso exige analizar latencia, capacidad y fallos; no obliga por mera definición a fusionar ambos límites ni permite afirmar independencia total.

**Cambio A:** un equipo propone compartir también la base con Evaluación. Eso introduce un punto común de acoplamiento estático que puede reunir el alcance. Habría que reconsiderar la independencia que se quería obtener.

**Cambio B:** se sustituye la llamada por una cola. Se amortiguan ciertos picos si el negocio acepta esperar. La dependencia semántica continúa, la cola requiere capacidad y el trabajo pendiente debe observarse. El cambio no garantiza por sí solo una mejor experiencia de usuario.

## Preguntas cortas con respuesta

- **¿Un quantum es una clase grande?** No: es una unidad arquitectónica con dependencias y alcance de características, a una escala superior a componentes individuales.
- **¿Un microservicio siempre es un quantum?** No automáticamente; hay que revisar dependencias, cohesión y funcionamiento.
- **¿Una base propia garantiza independencia?** No. Es una separación relevante, pero pueden quedar otras dependencias compartidas.
- **¿La asincronía elimina el acoplamiento?** No: modifica el dinámico y la forma de esperar; no elimina dominio, contratos ni capacidad requerida.
- **¿Todos los grupos pueden ignorar seguridad salvo el que la prioriza?** No. Priorizar una característica no exime de mínimos a otros ámbitos.
- **¿El árbol del capítulo elige una tecnología concreta?** No. Orienta estilos y decisiones, que luego se validan frente al problema.

## Qué deberías poder explicar sin mirar

Deberías poder dibujar una base compartida entre servicios, proponer un límite de quantum y justificarlo; explicar los cuatro términos de acoplamiento; mostrar dónde espera el trabajo con y sin cola; y reconstruir los tres grupos de Going Green. Si puedes describir cada flecha sin confundir un flujo de negocio con una llamada de red, has comprendido el propósito de los diagramas.


---

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/06 Going Green explicado paso a paso|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Índice]]
