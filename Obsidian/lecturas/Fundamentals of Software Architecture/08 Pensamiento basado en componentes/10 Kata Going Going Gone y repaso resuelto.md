---
title: "08 · Going, Going, Gone: descubrir, revisar y defender componentes"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/componentes
capitulo: 8
---

# Going, Going, Gone: descubrir, revisar y defender componentes

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 31–34 · impresas 125–128 · figuras 8-16 y 8-17** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Síntesis explicada del capítulo 8; los ejemplos, preguntas, tablas y diagramas adicionales se señalan como elaboración didáctica. Las recreaciones de figuras conservan la idea y las relaciones pertinentes, con rótulos en español; no son facsímiles.

## Qué pretende demostrar el caso

Going, Going, Gone (GGG) es un sistema de subastas. En estas páginas el objetivo es **descubrir componentes y ajustar sus límites**; no diseñar toda su infraestructura. El libro aplica Actor/Action a tres actores: postor, subastador y sistema. «Postor» traduce *bidder*: quien hace una oferta económica o puja.

## Primera ronda: acciones y componentes

![c08-10-ggg-inicial](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-10-ggg-inicial.png)

Las columnas conservan la estructura de la figura 8-16: actor, acción y componente. Las flechas continuas asignan acciones a componentes; las discontinuas representan colaboraciones entre componentes. Una línea discontinua **no significa automáticamente evento asíncrono**, cola o transacción independiente.

| Componente | Responsabilidad en el caso |
|---|---|
| Video Streamer — Transmitir vídeo | Mostrar la subasta en vídeo en directo |
| Bid Streamer — Transmitir pujas | Mostrar las pujas a medida que ocurren |
| Bid Capture — Capturar pujas | Captar pujas de postores y del subastador |
| Bid Tracker — Registrar pujas | Mantener el registro de pujas como fuente oficial de información |
| Auction Session — Sesión de subasta | Iniciar la subasta y gestionar el cierre del artículo y la transición correspondiente |
| Payment — Pago | Procesador externo de pagos con tarjeta |

Transmitir vídeo y Transmitir pujas ofrecen al postor vistas de lectura. **Ver una puja no equivale a capturarla, aceptarla ni registrarla oficialmente.** Separar estos conceptos evita asignar decisiones de negocio al simple canal de presentación.

## Recorrido del gráfico inicial

1. El postor ve vídeo a través de Transmitir vídeo y sigue importes mediante Transmitir pujas.
2. Cuando oferta, su acción se asigna a Capturar pujas.
3. El subastador ingresa pujas presenciales y recibe las pujas procedentes de internet; el primer diseño utiliza una captura compartida.
4. Captura colabora con la difusión y con el registro de pujas.
5. Marcar un artículo como vendido y comenzar una subasta corresponden a Sesión de subasta.
6. Al cerrar un artículo, la sesión desencadena los pasos de pago y resolución; el registro permite conservar la información relevante.

**Conclusión:** seis componentes proporcionan un punto de partida con responsabilidades comprensibles. **Límite:** el gráfico no resuelve simultaneidad de ofertas, conflictos de orden, validación de importes, reintentos o comportamiento ante cortes. No debe leerse como un algoritmo ejecutable de adjudicación.

## Segunda ronda: la misma función tiene perfiles distintos

Funcionalmente parece razonable capturar todas las pujas de la misma manera. Sin embargo, los postores pueden ser miles, mientras que la entrada del subastador representa una ruta crítica con muy pocos usuarios. Los perfiles arquitectónicos difieren:

| Aspecto | Entrada del postor | Entrada del subastador |
|---|---|---|
| Volumen de usuarios | Potencialmente muy alto | Reducido |
| Escalabilidad y elasticidad | Deben responder a la participación y sus picos | No necesitan la misma magnitud |
| Fiabilidad y disponibilidad | Importantes para cada usuario | Especialmente críticas para sostener la subasta |
| Consecuencia de una desconexión | Un participante queda afectado | Puede comprometer la conducción de la subasta |

El capítulo no dice que la experiencia del postor carezca de importancia. Compara consecuencias diferentes y niveles de necesidad, que justifican revisar el componente compartido.

![c08-11-ggg-revisado](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-11-ggg-revisado.png)

## El diseño revisado

Ahora Capturar pujas se divide: una ruta para la captura del postor y otra para **Auctioneer Capture**, la captura del subastador. El nuevo componente aparece en verde. Ambos colaboran con la difusión y con el registro. Registrar pujas reúne la información de la ruta del subastador y las múltiples rutas de los postores.

El gráfico conserva la acción del subastador «recibir pujas web» vinculada a la captura de los postores, siguiendo la asignación de la figura del libro. Ingresar la puja local se dirige a la nueva captura del subastador. Marcar vendido continúa en Sesión de subasta.

**Paso de revisión:** identifica la necesidad diferente → divide la responsabilidad de entrada → actualiza relaciones → vuelve a comprobar las acciones. La separación añade un componente y nuevas colaboraciones, por lo que tiene coste. Su beneficio potencial es poder tratar de manera diferente necesidades que antes estaban mezcladas.

**Conclusión:** los requisitos funcionales sugieren componentes y las características arquitectónicas refinan sus límites. **Límite:** dos componentes lógicos no garantizan aislamiento de recursos o disponibilidad; la arquitectura física deberá respaldar los objetivos.

## Qué sigue pendiente según el propio capítulo

El diseño no es definitivo. Aún faltan requisitos como registro de cuentas y administración de pagos. El libro presenta esta solución como una posibilidad, no como el diseño único ni necesariamente el mejor. Cada alternativa tiene compromisos; el arquitecto compara esos compromisos con el contexto.

## Laboratorio resuelto: incorporar una regla nueva

**Supuesto didáctico, no requisito del libro:** una puja duplicada por reintento de red no debe contarse dos veces.

1. La historia atraviesa captura y registro; hay que identificar quién decide oficialmente que una puja fue aceptada.
2. La captura necesita transportar un identificador estable del intento o información suficiente para reconocer el duplicado.
3. El componente que mantiene el registro oficial necesita una regla coherente para evitar registrar dos veces el mismo intento. Esta es una propuesta a validar, no una solución especificada por el capítulo.
4. Difundir pujas debería reflejar el resultado oficial; difundir antes de aceptar requeriría distinguir estados provisionales y definitivos.
5. Las pruebas deben incluir reintentos, llegada fuera de orden y reenvío tras respuesta perdida.
6. Revisamos si el cambio obliga a modificar ambas rutas de captura o si basta un contrato común. El hecho de separar entradas no autoriza duplicar incoherentemente la regla oficial.

## Preguntas de repaso con respuesta

**¿Por qué no crear un componente por cada actor?** Porque el actor puede realizar acciones de varias responsabilidades y varios actores pueden compartir una responsabilidad.

**¿Bid Streamer es la fuente oficial de pujas?** No en el modelo presentado: esa función corresponde a Bid Tracker. Mostrar información y conservar el registro oficial cumplen propósitos diferentes.

**¿La separación demuestra que se necesitan microservicios?** No. Determina componentes lógicos; decidir unidades de despliegue requiere el análisis físico.

**¿Qué dato demuestra que el diseño inicial era inútil?** Ninguno. Sirvió para descubrir una diferencia importante y realizar una iteración informada.

**¿Cómo se aplicaría Demeter aquí?** Preguntando qué conocimiento de registro, adjudicación o pago necesita realmente cada componente. No se aplica simplemente insertando un intermediario ni borrando flechas del dibujo.

**¿Qué criterio permite aceptar el diseño provisional?** Cobertura de acciones actuales, responsabilidades comprensibles, relaciones justificadas y compromisos coherentes con las características prioritarias, con dudas pendientes explícitas.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/09 Ley de Demeter y conocimiento mínimo|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|Volver al índice →]]
