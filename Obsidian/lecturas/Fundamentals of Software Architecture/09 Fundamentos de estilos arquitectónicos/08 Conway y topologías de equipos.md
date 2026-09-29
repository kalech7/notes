---
title: "Conway y topologías de equipos"
created: 2026-09-28
capitulo: 9
tags:
  - lecturas/software-architecture
  - arquitectura/estilos
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/00 Índice|← Índice del capítulo 9]]

# Conway y topologías de equipos

**La arquitectura también se construye mediante conversaciones.** Si para cambiar una función se necesitan permisos y coordinación entre muchos grupos, esa estructura humana influye en qué fronteras, interfaces y soluciones resultan viables.

## 1. La observación de Conway

La ley de Conway, tal como la presenta el capítulo, relaciona la estructura de comunicación de una organización con la estructura de los sistemas que diseña. No debe leerse como una ley física que permite predecir cada clase a partir de un organigrama. Es una observación sobre restricciones y tendencias de colaboración.

**Ejemplo propio.** Si interfaz, reglas y datos pertenecen a tres grupos aislados, un cambio de compra necesita tres negociaciones. Esa coordinación puede reforzar una arquitectura dividida por especialidades. Si un equipo reúne las capacidades necesarias para trabajar sobre Compra, resulta más factible mantener una frontera alrededor de esa responsabilidad.

La **maniobra inversa de Conway** busca modificar estructuras de equipos y colaboración para favorecer la arquitectura deseada. Cambiar nombres de departamentos sin cambiar decisiones, dependencias o propiedad no produce esa transformación.

**Fuente:** PDF pp. 9–10, impresas 138–139.

## 2. Cuatro tipos de equipos

El capítulo resume la clasificación de *Team Topologies* de Matthew Skelton y Manuel Pais. No se trata de cuatro niveles jerárquicos: cada tipo atiende una clase de necesidad.

| Tipo | Responsabilidad | Ejemplo propio | Riesgo si se interpreta mal |
|---|---|---|---|
| Alineado con un flujo de valor | Entregar resultados para un producto, capacidad o conjunto coherente de funciones | Equipo responsable del proceso de compra | Asignarle todas las especialidades difíciles sin apoyo |
| Habilitador | Ayudar a cerrar una brecha de capacidad o conocimiento | Acompañar al equipo de compra para aprender instrumentación | Convertir el apoyo en una aprobación obligatoria permanente |
| Subsistema complicado | Encapsular trabajo que exige conocimiento especializado | Motor de optimización de rutas | Exponer sus detalles internos y transferir la complejidad a consumidores |
| Plataforma | Ofrecer servicios y bloques internos que faciliten el trabajo de otros equipos | Entornos, despliegue y observabilidad como capacidades consumibles | Crear una cola de tickets para cualquier operación rutinaria |

El término **carga cognitiva** se refiere aquí a cuánto conocimiento debe manejar un equipo para trabajar correctamente. Un límite útil permite concentrarse en su responsabilidad sin dominar cada detalle interno de todas las dependencias.

**Fuente:** PDF p. 22, impresa 151.

![Los cuatro tipos de equipos y su propósito](../Recursos%20visuales/Cap%C3%ADtulos%209%20y%2010/c09-04-equipos.png)

La imagen parte del equipo que entrega una capacidad de negocio. Los otros tipos de equipo reducen fricciones de distintas maneras: enseñan una habilidad, encapsulan conocimiento especializado o ofrecen servicios de plataforma. Las conexiones representan apoyo o consumo de capacidades, no una cadena de mando. Es una elaboración propia del resumen de la impresa 151.

El gráfico no define un organigrama obligatorio, tamaño de equipo ni regla de un equipo por microservicio. La organización concreta depende de flujo de trabajo, complejidad y capacidades disponibles.

## 3. Distinguir apoyo, encapsulación y plataforma

Un equipo **habilitador** ayuda a que otro aprenda. Si acompaña a instrumentar un servicio, la meta es que el equipo pueda continuar con mayor capacidad. Un equipo de **subsistema complicado** conserva conocimiento especializado dentro de una responsabilidad concreta; no pretende necesariamente enseñar toda esa especialidad a todos. Un equipo de **plataforma** proporciona un producto interno utilizable, de modo que otros equipos no repitan tareas comunes o negociaciones innecesarias.

Estas diferencias evitan una confusión común: «todo lo que ayuda a otros es plataforma». Enseñar a interpretar una traza, ofrecer una plataforma de trazas y mantener un algoritmo experto que necesita trazas son responsabilidades distintas.

La plataforma también puede integrar reglas necesarias de calidad o seguridad. El capítulo enfatiza que su función es disminuir fricción con servicios internos y autoservicio. El gobierno puede quedar incorporado en un camino de uso claro en lugar de exigir coordinación manual para cada operación.

## 4. Caso resuelto: PedidoClaro incorpora entregas

**Supuesto propio.** Un equipo controla el flujo desde crear un pedido hasta confirmar una entrega. Aparece un cálculo de rutas que requiere conocimiento avanzado; además, el equipo tiene dificultades para interpretar fallos entre servicios.

Una propuesta razonada es que el equipo del flujo conserve las decisiones de negocio del pedido; un equipo especializado mantenga el optimizador con un contrato entendible; una plataforma proporcione despliegue e instrumentación comunes; un equipo habilitador acompañe el aprendizaje necesario para investigar incidentes.

La estructura no exige crear cuatro equipos nuevos inmediatamente. En una organización pequeña puede haber personas compartiendo funciones de forma explícita. El ejercicio sirve para distinguir necesidades antes de multiplicar grupos.

**Condición de éxito:** el equipo del flujo puede entregar cambios habituales sin esperar coordinación innecesaria. **Costo:** existen contratos y servicios internos que mantener. **Evidencia por observar:** tiempos de espera entre equipos, bloqueos recurrentes y dependencias que obligan a coordinar cada cambio.

## 5. Relación con partición y distribución

Una partición por dominio puede alinearse con un equipo responsable de una capacidad de negocio; esa alineación es posible dentro de un monolito modular. Un servicio separado no concede autonomía si el equipo depende de otros para cada modificación de datos o despliegue.

La pregunta completa es: **¿la frontera del código, la propiedad del dato, la responsabilidad del equipo y el modo de entrega permiten cambiar esta capacidad con una coordinación razonable?** Si una dimensión contradice las demás, el diagrama técnico puede prometer una autonomía que la operación no permite.

> [!question] ¿Cada microservicio requiere un equipo?
> No se deduce de esta clasificación. Lo relevante es una responsabilidad y una carga manejables; contar despliegues no determina por sí solo equipos.

> [!question] ¿Un equipo habilitador debe aprobar cada cambio futuro?
> Esa dependencia permanente contradice el propósito de cerrar una brecha y reducir fricción. La gobernanza necesaria debe diseñarse explícitamente, no aparecer por accidente como cola de aprobación.

> [!question] ¿La plataforma solo entrega herramientas?
> El capítulo la presenta como servicios, APIs, conocimiento y apoyo organizados como producto interno. Su utilidad se evalúa por lo que permite hacer a quienes la consumen.

## Fuente principal

- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/06 Fundamentos de estilos arquitectónicos.pdf#page=9|Fundamentals of Software Architecture, 2.ª ed., capítulo 9, PDF pp. 9–10; impresas 138–139]].
- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/06 Fundamentos de estilos arquitectónicos.pdf#page=22|Fundamentals of Software Architecture, 2.ª ed., capítulo 9, PDF p. 22; impresa 151]].

Las explicaciones, diagramas y ejemplos identificados como propios son elaboraciones didácticas; las páginas indicadas permiten contrastar los conceptos con el escaneo.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/07 Versionado compensación y observabilidad|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/09 Fundamentos de estilos arquitectónicos/09 Laboratorio y repaso|Siguiente →]]
