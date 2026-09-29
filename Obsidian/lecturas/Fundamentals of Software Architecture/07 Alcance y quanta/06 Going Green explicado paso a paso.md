---
title: "Capítulo 7 · Going Green explicado paso a paso"
created: 2026-09-28
capitulo: 7
orden: 6
tags:
  - lecturas/software-architecture
  - arquitectura/quanta
---

# Going Green explicado paso a paso

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Capítulo 7 · Alcance y quanta]] · Nota 6 de 7

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, segunda edición, capítulo 7. Fuente local: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Las páginas PDF se cuentan desde el archivo suministrado; la impresa aparece en el libro. «Elaboración» y «ampliación didáctica» identifican material propio.

**Objetivo:** recorrer la kata del libro desde el flujo del negocio hasta los límites arquitectónicos, explicando por qué siete servicios aparecen agrupados en tres quanta.

## 1. El problema de negocio

**Libro — PDF p. 9, impresa 103.** Going Green (GG) recicla y revende dispositivos electrónicos usados. La persona indica el modelo y su estado mediante un quiosco o un sitio web. GG hace una oferta; si la persona acepta, entrega el dispositivo en el quiosco o recibe una caja para enviarlo. Al recibirlo, GG lo evalúa y paga a la persona. Luego estima su valor y decide reciclarlo o revenderlo. El sistema genera además informes y análisis.

![04 going green flujo](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-04-going-green-flujo.png)

### El flujo de la figura 7-5

El redibujo conserva los participantes y las relaciones principales de la figura 7-5, **PDF p. 10 / impresa 104**, y añade números para estudiarlos.

1. La caja de la persona representa al participante externo y su dispositivo; la caja de interfaces reúne web y quiosco.
2. La ida transporta datos del modelo y estado. La vuelta lleva una oferta. Todavía no hay evaluación física definitiva.
3. Si acepta, la persona entrega o envía el dispositivo. La flecha larga hacia Evaluación representa un paso del negocio, que incluye logística física.
4. El resultado de evaluar pasa a la operación interna.
5. El pago vuelve a la persona. Información, dinero y dispositivo son objetos distintos aunque se representen todos con flechas.
6. La operación decide entre reventa y reciclaje y genera los registros asociados.

**Conclusión:** existe un recorrido de negocio conectado, pero sus partes tienen necesidades diferentes. **Límite:** este gráfico no especifica APIs, llamadas síncronas, colas, estados de pago ni transporte físico concreto. No se deben interpretar todas sus flechas como conexiones de software.

## 2. Tres conjuntos de características

**Libro — PDF p. 10, impresa 104; figura 7-6.** Del análisis emergen tres grupos de prioridades.

![05 going green prioridades](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-05-going-green-prioridades.png)

### Explicación de cada grupo

**Atención al cliente: escalabilidad, disponibilidad y agilidad.** La parte pública debe atender consultas y cambios de uso sin deteriorar el acceso. La escala de esa interfaz puede ser muy diferente a la de los procesos internos. Agilidad expresa la capacidad de adaptar la solución con eficacia.

**Evaluación de dispositivos: mantenibilidad, desplegabilidad y testabilidad, que contribuyen a la agilidad.** Los nuevos modelos electrónicos aparecen constantemente. Poder incorporar pronto reglas de evaluación favorece el negocio: los dispositivos más recientes pueden tener mayor valor de reventa. Aquí se conecta un motivo económico con una necesidad técnica concreta de cambio frecuente y confiable.

**Reciclaje, informes y contabilidad: seguridad, integridad de datos y auditabilidad.** La operación necesita proteger los datos, mantenerlos correctos y reconstruir qué ocurrió. La trazabilidad y los controles pueden introducir ritmos diferentes a los de un módulo que cambia continuamente.

Las flechas del gráfico **asocian una capacidad a sus prioridades**; no indican orden de ejecución. Las tres columnas permiten comparar ámbitos. No afirman que la interfaz pública no necesite seguridad ni que contabilidad pueda ser indisponible: expresan énfasis, no eliminación de mínimos.

## 3. Convertir el análisis en límites

**Libro — PDF p. 11, impresa 105; figura 7-7.** La arquitectura ilustrada separa los conjuntos mediante líneas punteadas.

![06 going green quanta](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c07-06-going-green-quanta.png)

### Explicación de la topología — figura 7-7

Cada caja con pequeños rectángulos internos representa un servicio con componentes; no son servidores físicos ni núcleos de CPU. Cada cilindro es una base de datos. Las líneas sólidas indican dependencia del almacenamiento. Los contornos punteados delimitan los quanta.

**Primer límite:** Oferta y Estado del artículo son dos servicios que usan la misma base. Se agrupan en un quantum orientado a la atención pública.

**Segundo límite:** Evaluación dispone de su propia base y queda separada, de modo que su prioridad de cambiar las reglas de valoración tiene un ámbito distinguible.

**Tercer límite:** Recepción, Reciclaje, Contabilidad e Informes comparten datos en un quantum de operación interna. Hay cuatro servicios, pero el dibujo no presenta cuatro ámbitos independientes de persistencia.

Las siete cajas de servicios se conectan con solo tres cilindros, y los servicios que comparten cilindro quedan dentro del mismo contorno: por eso hay tres quanta. El número relevante para este análisis no se deduce del número de servicios.

**Conclusión:** los grupos de características sirven de guía para definir granularidad y dependencias. **Límite:** la figura no dibuja la comunicación entre los tres quanta ni prueba que todas sus operaciones sean independientes. Habría que completar esos contratos y analizar el recorrido de extremo a extremo. Tampoco prueba que esta sea la única arquitectura válida.

## 4. Por qué no imponer todas las prioridades con igual intensidad a todo

El libro admite que se podría intentar cumplir simultáneamente todos los objetivos en todo el sistema, pero señala que sería difícil: algunos compromisos chocan. Por ejemplo, los controles asociados a auditabilidad pueden dificultar un despliegue muy rápido, y el volumen de la interfaz pública no coincide necesariamente con el de la operación interna.

Separar alcances permite concentrar esfuerzo donde aporta más valor. No resuelve por sí mismo los conflictos del flujo completo: una cotización que depende de un evaluador lento seguirá experimentando esa limitación, aunque las cajas estén separadas.

## 5. Preguntas resueltas para profundizar

**¿Por qué no poner Evaluación dentro del grupo público si participa en las ofertas?** Porque compartir una relación funcional no implica idénticas prioridades de evolución. El libro destaca el cambio frecuente de modelos electrónicos. La propuesta separa ese ámbito; después hay que diseñar cómo se integra.

**¿Siete servicios implican siete despliegues completamente independientes?** No puede concluirse del gráfico. En particular, hay bases compartidas dentro de los grupos. Hay que revisar código, contratos y procedimientos de despliegue reales.

**¿El grupo público puede ignorar los datos contables?** No. Separar modelos y persistencia exige definir qué información intercambian. El dibujo de límites no elimina el acoplamiento semántico del negocio.

**¿Qué falta para implementar?** Como ampliación propia: contratos, estados del dispositivo, políticas de error, comunicación, objetivos medibles y estrategia de consistencia. La kata permite practicar decisiones de arquitectura, pero la figura no contiene una especificación implementable completa.


---

[[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/05 Del alcance al estilo arquitectónico|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/07 Nube aplicación y repaso|Siguiente →]]
