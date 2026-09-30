---
title: "14 · Equipos y características"
created: 2026-09-29
capitulo: 14
tags:
  - lecturas/software-architecture
  - arquitectura/service-based
---

# Equipos y características

[[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/00 Índice|← Índice del capítulo 14]]

**La arquitectura facilita cambios por dominio cuando los equipos también pueden entregar por dominio.** Si un cambio requiere pasar sucesivamente por un equipo de interfaz, otro de negocio y otro de base, se mantiene una coordinación transversal que reduce la autonomía buscada.

## Equipos alineados con el trabajo

Un **equipo multidisciplinario** tiene las capacidades necesarias para entregar una función, por ejemplo interfaz, reglas, persistencia y pruebas. Eso no exige que cada persona domine todo ni elimina especialistas. Permite que la responsabilidad por una capacidad del negocio no quede repartida entre colas organizativas separadas.

El capítulo examina cuatro tipos de equipos:

| Tipo | Relación con el estilo | Condición o matiz |
|---|---|---|
| Alineado con un flujo de valor | Puede evolucionar un servicio de dominio completo | El flujo debe caber razonablemente en esa frontera; si atraviesa varios, revisar partición o estilo |
| Facilitador (*enabling*) | Ayuda a desarrollar capacidades y realizar experimentos | El libro ve menos encaje que en estilos más finos; módulos internos bien identificados crean lugares útiles de intervención |
| Subsistema complicado | Se ocupa de una parte especializada y difícil | La modularidad por dominio o subdominio permite aislar ese trabajo |
| Plataforma | Proporciona herramientas, APIs y operaciones comunes | Debe apoyar a los dominios sin imponer una nueva cadena de dependencia para cada cambio |

Ejemplo propio: Evaluación necesita modelos especializados para dispositivos electrónicos. Un equipo con esa especialidad puede trabajar en un módulo interno de Evaluación, mientras la plataforma proporciona despliegue y observación comunes. No es necesario convertir el modelo en un servicio remoto solo porque existe un equipo especialista.

La organización técnica por capas tampoco es intrínsecamente inválida. La afirmación del libro es de encaje: en este estilo, una responsabilidad de negocio que salta entre varios equipos técnicos exige comunicación y esperas que dificultan entregarla de punta a punta.

## Tabla de características del libro

Las estrellas indican apoyo relativo del estilo habitual a cada característica. Una estrella es apoyo débil y cinco fuerte. No son medidas de rendimiento, porcentajes, ni una función que permita calcular un «puntaje total» sumándolas.

![Valoraciones ordinales del capítulo y errata de tolerancia a fallos](../Recursos%20visuales/Cap%C3%ADtulo%2014/c14-08-caracteristicas.png)

La tabla recrea en español la figura 14-8: simplicidad y modularidad tienen tres estrellas; las cuatro características de ingeniería tienen cuatro; respuesta y escalabilidad tres; elasticidad dos; tolerancia a fallos tres. El recuadro amarillo conserva las categorías de costo, partición y quanta. El rojo documenta la contradicción entre tabla y prosa en tolerancia a fallos.

| Característica | Figura 14-8 | Por qué tiene sentido esa valoración |
|---|---|---|
| Simplicidad | ★★★ | Menos piezas que una partición muy fina, pero todavía hay red, datos y operación distribuida |
| Modularidad | ★★★ | Los dominios se separan, pero cada servicio reúne bastante funcionalidad y puede compartir contratos de datos |
| Mantenibilidad | ★★★★ | Los cambios coherentes quedan concentrados en un ámbito |
| Facilidad de pruebas | ★★★★ | Se prueba un dominio con menos coordinación remota que en un flujo muy dividido |
| Facilidad de despliegue | ★★★★ | Una entrega del dominio puede ser menor que la de toda la aplicación |
| Capacidad de evolución | ★★★★ | Los dominios pueden cambiar con ciclos relativamente propios |
| Capacidad de respuesta | ★★★ | Evitar cadenas de red ayuda, pero persisten red y motor compartido |
| Escalabilidad | ★★★ | Se agregan instancias por servicio, con granularidad amplia |
| Elasticidad | ★★ | Ajustar replicas de una unidad grande copia funciones que quizá no necesitan la capacidad |
| Tolerancia a fallos | ★★★ | Se aíslan algunos procesos, pero quedan dependencias compartidas |

El costo es **$$**, una categoría relativa del libro, no un presupuesto monetario. La partición es por **dominio**. Los quanta pueden ser de **uno a varios**, según UI, bases y dependencias. El capítulo no asigna ninguna valoración de cinco estrellas a este estilo.

## La errata que hay que conservar visible

En PDF 13, figura 14-8, tolerancia a fallos muestra **tres** estrellas. En PDF 15 la prosa dice **cuatro** y relaciona esa afirmación con disponibilidad. Estas notas registran tres al reproducir la tabla y explican el argumento de independencia sin tratarlo como un cuatro confirmado.

**Disponibilidad** es que la capacidad esté lista para usarse; **tolerancia a fallos** es continuar con un comportamiento aceptable cuando falla una parte. Están relacionadas, pero no son la misma propiedad. La tabla tampoco añade una fila separada de disponibilidad, por lo que no debe inventarse una valoración numérica para ella a partir de la prosa.

## De valoración orientativa a escenario verificable

Una arquitectura no cumple «cuatro estrellas de pruebas» por adoptar el nombre del estilo. Necesita contratos definidos, datos de prueba, automatización y aislamiento real. Un servicio de dominio sin modularidad interna puede ser difícil de probar aunque tenga una caja separada en el diagrama.

Como elaboración propia, la pregunta de despliegue puede formularse así: «Al cambiar una regla de Evaluación, ¿podemos publicar Evaluación sin reemplazar Reciclaje ni interrumpir Cotización?». La de tolerancia a fallos: «Si Evaluación no responde durante diez minutos, ¿qué consultas públicas continúan funcionando y qué estado se muestra?». Los escenarios revelan dependencias que la tabla ordinal no tiene espacio para expresar.

> [!question]- ¿Cuatro estrellas significan que este estilo es dos veces mejor que otro con dos?
> No. La escala es ordinal: expresa un orden de apoyo relativo, sin unidades ni distancia cuantificada entre valores. No permite razones, promedios de rendimiento ni garantías.

> [!question]- ¿Puede un equipo facilitador ayudar aunque el libro vea menor encaje?
> Sí. Puede intervenir en capacidades y componentes internos. La comparación del libro describe la afinidad general, no una prohibición ni la inutilidad de especialistas.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/11 Arquitectura basada en servicios.pdf#page=12|PDF 12–15 · impresas 220–223 · equipos, figura 14-8 y contradicción tabla/prosa]].

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/07 Operación nube riesgos y gobierno|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/09 Going Green y quanta|Siguiente →]]
