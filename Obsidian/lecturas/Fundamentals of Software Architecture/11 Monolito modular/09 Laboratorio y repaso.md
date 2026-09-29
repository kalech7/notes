---
title: "11 · Laboratorio y repaso resuelto"
created: 2026-09-28
capitulo: 11
tags:
  - lecturas/software-architecture
  - arquitectura/monolito-modular
---

# Laboratorio y repaso resuelto

[[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/00 Índice|← Índice del capítulo 11]]

Este laboratorio es **elaboración propia**: aplica todo el capítulo a **PedidoClaro**, nuestra tienda de sándwiches inventada, distinta de EasyMeals. Intenta responder cada paso antes de abrir la solución.

## El caso

PedidoClaro tiene hoy una aplicación por capas (`presentation/`, `business/`, `persistence/`) mantenida por seis personas. En los últimos seis meses registró 40 cambios:

| Tipo de cambio | Cantidad | Ejemplos |
|---|---:|---|
| Promociones y precios | 14 | Nuevo 2×1 de martes, precio por tamaño |
| Pedidos | 11 | Notas para cocina, pedidos programados |
| Entregas | 8 | Zonas nuevas, incidencias de reparto |
| Técnicos transversales | 3 | Actualizar la librería de registro, cambiar el servidor de correo |
| Pagos | 4 | Nuevo proveedor de tarjetas |

El negocio atiende tres barrios, con picos moderados a la hora de comer, y quiere reducir el tiempo que tarda cada cambio. No hay presupuesto para operar varios servicios.

## Paso 1 · ¿Monolito modular o seguir por capas?

> [!question]- Solución
> 37 de 40 cambios (92,5 %) son de negocio y solo 3 son técnicos transversales. El libro recomienda el monolito modular cuando la mayoría de los cambios son de dominio y la arquitectura por capas cuando dominan los técnicos. Además, los requisitos operativos son moderados y el presupuesto limitado. **Decisión: migrar a un monolito modular**, conservando un solo despliegue. **Costo aceptado:** algunos cambios técnicos podrán extenderse por varios módulos; su alcance depende de cómo se encapsulen las herramientas compartidas.

## Paso 2 · Definir módulos y namespaces

> [!question]- Solución
> Un módulo por área que concentra cambios: `com.pedidoclaro.promociones`, `com.pedidoclaro.pedidos`, `com.pedidoclaro.entregas` y `com.pedidoclaro.pagos`. El tercer nodo es el dominio. Dentro de un módulo complejo, como promociones, puede haber subdivisión técnica: `com.pedidoclaro.promociones.reglas`, `com.pedidoclaro.promociones.pantallas`. No se crea un módulo genérico `comun` ni `utilidades` como contenedor de reglas de varios dominios. Una utilidad técnica estable sí puede compartirse con un propósito y unas dependencias explícitos.

## Paso 3 · ¿Estructura monolítica o modular?

> [!question]- Solución
> Un solo equipo de seis personas y módulos que colaboran en cada compra (pedidos llama a promociones para el precio y a pagos para cobrar). Según el libro, cuando los módulos necesitan comunicarse la estructura monolítica es más eficaz. **Decisión: un repositorio con una carpeta por módulo**, acompañado de reglas de gobierno desde el primer día.

## Paso 4 · Diseñar la comunicación de la compra

La compra necesita tres pasos: calcular el precio con promociones, cobrar y registrar el pedido. Hoy lo hace una clase que llama a todo.

> [!question]- Solución
> Hay tres módulos implicados en un orden fijo, así que un **mediador** «Compra» deja explícito ese orden y evita que Pedidos, Promociones y Pagos se conozcan entre sí. Con punto a punto, Pedidos dependería de dos módulos y podría acabar dependiendo de más; con mediador, Pedidos, Promociones y Pagos no tienen dependencias entre ellos y el mediador tiene tres. **Riesgo que vigilar:** que el mediador empiece a contener reglas de negocio (por ejemplo, descuentos), que deben seguir en Promociones.

## Paso 5 · Escribir las reglas de gobierno

> [!question]- Solución
> 1. **Pertenencia:** todo namespace debe ser igual a uno de los cuatro módulos (o al mediador `com.pedidoclaro.compra`) o empezar por uno de ellos seguido de punto.
> 2. **Límite de acoplamiento:** ningún módulo puede sumar más de cuatro dependencias entrantes más salientes, contando pares de módulos.
> 3. **Prohibición concreta:** ninguna clase de `..entregas..` puede acceder a clases de `..pagos..`; una entrega nunca debe cobrar.
> 4. **Datos (añadida por nosotros):** cada módulo solo escribe en sus propias tablas. Esta regla cubre el acoplamiento por datos que las tres anteriores no ven.

## Paso 6 · Contar el acoplamiento

Tras un año, las dependencias entre módulos son: Compra → Pedidos, Compra → Promociones, Compra → Pagos, Entregas → Pedidos, Promociones → Pedidos, Pagos → Pedidos.

> [!question]- Solución
> Contando entrantes (E) y salientes (S):
>
> | Módulo | E | S | Total |
> |---|---:|---:|---:|
> | Compra | 0 | 3 | 3 |
> | Pedidos | 4 | 0 | **4** |
> | Promociones | 1 | 1 | 2 |
> | Pagos | 1 | 1 | 2 |
> | Entregas | 0 | 1 | 1 |
>
> Nadie supera el límite de cuatro, aunque Pedidos está justo en él con cuatro entrantes. Comprobación: la suma de totales es 12, el doble de las 6 dependencias. Que un módulo reciba muchas dependencias no es malo en sí, pero el conteo no demuestra que su contrato sea estable; hay que comprobarlo. También conviene revisar por qué Promociones y Pagos consultan Pedidos directamente si ya existe un mediador.

## Paso 7 · Leer las señales de alarma

Dos años después: el arranque tarda seis minutos, dos personas modifican a menudo los mismos archivos de Promociones y un cambio en precios rompió los informes de entregas.

> [!question]- Solución
> Son tres señales del libro: arranque lento, personas que se estorban y cambios que rompen áreas inesperadas. La rotura de informes de entregas por un cambio de precios sugiere acoplamiento oculto, probablemente por datos compartidos. Acciones: reforzar la regla de datos, revisar si Promociones merece dividirse en submódulos con responsables distintos y medir el tiempo de arranque, porque afecta directamente al tiempo de recuperación.

## Paso 8 · ¿Cuándo dejar el monolito?

La tienda abre en veinte ciudades y las promociones de fin de semana multiplican por treinta la carga del cálculo de precios.

> [!question]- Solución
> Ahora la elasticidad importa y el estilo tiene una estrella en ella. El libro sugiere evolucionar hacia un estilo distribuido, como el basado en servicios o los microservicios. Los módulos ya definidos ofrecen candidatos de separación: Promociones merece evaluarse si la medición confirma que su carga domina y el costo de escalar todo no resulta aceptable. Un aumento de treinta veces no demuestra por sí solo que distribuir sea necesario. Si su base de datos ya estaba separada o sus tablas eran exclusivas, la extracción será mucho más sencilla.

## Repaso rápido

> [!question]- ¿Qué dos rasgos definen la forma del monolito modular?
> Una sola unidad de despliegue y funcionalidad agrupada por área de dominio.

> [!question]- ¿Qué indica el tercer nodo del namespace?
> En los ejemplos con prefijo `com.app`, indica el criterio de partición: técnico o de dominio. Con otro prefijo puede ocupar otra posición; importa la primera agrupación propia de la aplicación.

> [!question]- ¿Cuál es el gran riesgo de la estructura monolítica y cuál el de la modular cuando hay mucha comunicación?
> En la monolítica, degradarse en una Big Ball of Mud si las clases internas son accesibles y faltan controles de dependencias. En la modular, caer en el JAR o DLL Hell por la proliferación de contratos compartidos y sus versiones.

> [!question]- ¿Qué acoplamiento conserva el mediador?
> La coordinación del flujo y los contratos que usa el mediador. En el diseño unidireccional mostrado, el mediador depende de la API de cada módulo, pero los módulos no necesitan conocerlo.

> [!question]- ¿Por qué un monolito modular puede tener varias bases de datos?
> Porque la topología de datos es una decisión distinta del despliegue. Los módulos independientes con datos de su contexto pueden tener base propia aunque todo se despliegue junto.

> [!question]- ¿Qué valoraciones mejoran respecto a capas y cuáles no?
> Mejoran de una a dos estrellas modularidad, mantenibilidad, desplegabilidad y capacidad de evolución. Simplicidad, testabilidad, capacidad de respuesta y las tres operativas quedan igual.

> [!question]- ¿Cuándo prefiere el libro la arquitectura por capas?
> Cuando la mayoría de los cambios son técnicos, como reemplazar la interfaz o la tecnología de base de datos, porque en el monolito modular afectarían a todos los módulos.

## Fuente principal

- [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/08 Monolito modular.pdf#page=1|Fundamentals of Software Architecture, 2.ª ed., capítulo 11, PDF pp. 1–16 · impresas 165–180]].

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/08 Caso EasyMeals|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/11 Monolito modular/00 Índice|Índice del capítulo 11]]
