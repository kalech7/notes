---
title: "14 · Topología y servicios de dominio"
created: 2026-09-29
capitulo: 14
tags:
  - lecturas/software-architecture
  - arquitectura/service-based
---

# Topología y servicios de dominio

[[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/00 Índice|← Índice del capítulo 14]]

**La arquitectura basada en servicios divide la aplicación en pocos servicios de dominio, grandes y desplegables por separado.** La interfaz también se publica aparte; una base de datos compartida es habitual, aunque el estilo permite varias bases. La ventaja buscada es cambiar una parte del negocio sin publicar toda la aplicación, conservando una operación más sencilla que la de cientos de servicios pequeños.

## Qué significa cada palabra

Un **dominio** es una parte del negocio con conceptos y reglas propios: pedidos, facturación o evaluación de dispositivos. Un **subdominio** es una división más acotada dentro de ese ámbito. «Dominio» no significa nombre de Internet y tampoco equivale automáticamente a una tabla.

Un **servicio de dominio** reúne una capacidad coherente del negocio en una unidad de software accesible remotamente. **Granularidad gruesa** significa que reúne varias responsabilidades relacionadas: registrar un pedido, asignarle identificador, aplicar sus reglas de pago y ajustar existencias pueden formar parte de `OrderService`. La palabra «gruesa» describe el alcance funcional, no obliga a escribir clases gigantes.

**Distribuida** significa que hay componentes en procesos distintos y comunicación por red. Por eso una petición puede fallar aunque el código sea correcto: destino caído, red interrumpida o respuesta perdida. **Despliegue independiente** significa que el equipo puede instalar una versión de Pedidos sin sustituir el ejecutable de Envíos. Esto exige compatibilidad de contratos y datos; la separación de procesos por sí sola no la garantiza.

## La forma básica del libro

![Topología de servicios de dominio y base compartida](../Recursos%20visuales/Cap%C3%ADtulo%2014/c14-01-topologia.png)

El amarillo representa la interfaz, el azul los servicios y el verde los datos comunes. Cada servicio contiene su propia lógica y accede a la base. Las flechas superiores atraviesan la red; las inferiores representan acceso a datos. Los nombres Pedidos, Clientes, Envíos e Informes son una elaboración propia que concreta la figura 14-1. Publicar Envíos por separado reduce el alcance de la entrega, mientras que una indisponibilidad de la base puede afectar a todos.

El libro llama a esta forma una arquitectura de **macrocapas distribuidas**: interfaz, servicios y datos son grandes franjas, pero dentro de la franja de servicios la división se organiza por negocio. No es necesario convertir la arquitectura completa en capas técnicas de presentación, lógica y persistencia compartidas por todos los equipos.

Los servicios normalmente no necesitan llamarse entre sí para cada operación. Se intenta conservar la coordinación principal dentro de un dominio. La base común permite consultas SQL y **joins**, operaciones que combinan filas relacionadas de varias tablas. Se evita duplicar de inmediato cada dato y construir múltiples llamadas remotas solo para reunirlo.

## Una o varias instancias

Una **instancia** es una ejecución concreta de un servicio. Tres instancias de Pedidos siguen siendo un servicio lógico, porque ejecutan su misma responsabilidad y contrato. El libro considera común comenzar con una instancia por servicio, y añadir otras cuando el volumen o la recuperación ante fallos lo exige.

Un **balanceador** distribuye solicitudes entre instancias disponibles. Si una se cae, las otras pueden seguir atendiendo, siempre que el balanceador detecte salud y la capacidad restante baste. Duplicar una instancia no elimina la dependencia de la base común.

El acceso remoto habitual es **REST**, un enfoque de APIs basado en recursos y operaciones HTTP. También caben mensajería, **RPC** —llamada a procedimiento remoto— y SOAP, un protocolo de mensajes estructurados. Estas opciones no cambian automáticamente el tamaño del dominio. Un **localizador de servicios** resuelve a qué dirección o instancia enviar la solicitud; puede estar en la interfaz o en una capa de gateway.

## No confundir tres familias

En este libro, *service-based architecture* designa este estilo concreto. El capítulo lo presenta como una variante híbrida cercana a microservicios, pero no como un simple sinónimo. Los microservicios suelen buscar fronteras de despliegue más finas y mayor independencia del dato. Tampoco basta tener APIs o usar la palabra «servicio» para identificar el estilo. **SOA** significa arquitectura orientada a servicios y nombra otra familia; este capítulo no exige sus mecanismos de integración ni define este estilo por un bus empresarial.

La distinción útil es estructural: ¿cuánta funcionalidad vive junta?, ¿qué datos comparten?, ¿qué se publica junto?, ¿qué necesita la red para terminar una operación? Nombrar la arquitectura antes de contestar esas preguntas invita a confundirla.

> [!question]- ¿Por qué la base compartida es una ventaja y un riesgo a la vez?
> Permite consultar y modificar datos relacionados sin inventar una integración distribuida para cada relación. A cambio, los servicios dependen de su disponibilidad, capacidad y esquema. Un cambio incompatible de tabla o un fallo de base puede atravesar varias fronteras de despliegue.

> [!question]- ¿Tener doce servicios garantiza este estilo?
> No. La recomendación del libro de mantener alrededor de doce o menos es una heurística para contener coordinación, pruebas y conexiones, especialmente con base común. No hay un límite técnico que convierta al servicio trece en otro estilo.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/11 Arquitectura basada en servicios.pdf#page=1|PDF 1–2 · impresas 209–210 · figura 14-1]].

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/00 Índice|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/14 Arquitectura basada en servicios/02 Interior fachadas y granularidad|Siguiente →]]
