---
title: "08 · Descubrir componentes mediante flujos y actores"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/componentes
capitulo: 8
---

# Descubrir componentes mediante flujos y actores

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> **PDF 19–21 · impresas 113–115 · figura 8-7** de [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf|05 Alcance y componentes.pdf]]. Síntesis explicada del capítulo 8; los ejemplos, preguntas, tablas y diagramas adicionales se señalan como elaboración didáctica. Las recreaciones de figuras conservan la idea y las relaciones pertinentes, con rótulos en español; no son facsímiles.

## Candidatos antes de conocer todos los detalles

Es posible iniciar el diseño sin disponer de todas las especificaciones. Necesitamos un entendimiento de las funciones principales, no cada validación de pantalla. El libro presenta dos enfoques útiles: **Workflow**, basado en recorridos, y **Actor/Action**, basado en quién hace qué.

![c08-05-cubos](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c08-05-cubos.png)

El panel superior representa componentes candidatos como recipientes vacíos: sus nombres proponen funciones, pero todavía no tienen un contenido confirmado. Las flechas verticales indican la asignación posterior de requisitos; los documentos del panel inferior son esos comportamientos concretos. No representan mensajes que el programa intercambia.

**Cómo se utiliza:** primero nombra el recipiente según una función; después agrega las historias relevantes; finalmente examina si el contenido sigue correspondiendo al nombre. **Conclusión:** identificar no es validar. **Límite:** el tamaño del recipiente no indica líneas de código, esfuerzo ni capacidad de ejecución.

## Enfoque Workflow: seguir el recorrido principal

Partimos del camino exitoso más representativo del negocio. En el ejemplo de pedidos del libro:

| Paso del recorrido | Componente candidato |
|---|---|
| Explorar productos | Consultar catálogo |
| Registrar la compra | Registrar pedido |
| Pagar | Procesar pago |
| Recibir confirmación por correo | Notificar al cliente |
| Preparar los artículos | Preparar pedido |
| Despachar | Enviar pedido |
| Recibir aviso de envío | Notificar al cliente |
| Consultar dónde está el envío | Seguir pedido |

Observa que ocho pasos producen siete candidatos: **Notificar** aparece dos veces. No se crea un componente nuevo por cada casilla del flujo. El mismo comportamiento coherente puede intervenir en diferentes momentos.

**Procedimiento práctico:** escribe el recorrido sin tecnologías, subraya las acciones con significado de negocio, agrupa acciones que comparten responsabilidad, nombra candidatos y anota sus colaboraciones. Después repite con otros recorridos importantes. No intentes inventariar todos los caminos excepcionales en la primera sesión, pero recuerda que se incorporarán durante las siguientes iteraciones.

**Ventaja:** conserva el sentido de principio a fin. **Riesgo:** un único camino exitoso puede dejar fuera cancelaciones, devoluciones, operaciones administrativas y tareas automáticas.

## Enfoque Actor/Action: quién hace qué

Identificamos actores y sus acciones significativas. Un actor no tiene que ser una persona: el sistema también ejecuta actividades automáticas. En el ejemplo:

| Actor | Acción | Candidato |
|---|---|---|
| Cliente | Buscar productos y consultar detalles | Búsqueda y detalle de producto |
| Cliente | Registrar o cancelar pedido | Registrar pedido y Cancelar pedido |
| Cliente | Registrarse y cambiar sus datos | Registro de cliente y Perfil |
| Preparador | Elegir caja y marcar listo | Preparar pedido |
| Preparador | Despachar | Enviar pedido |
| Sistema | Ajustar existencias | Gestionar inventario |
| Sistema | Solicitar reposición al proveedor | Reponer stock |
| Sistema | Aplicar cobro | Procesar pago |

La tabla combina algunas acciones para abreviar la presentación; no establece que búsqueda y detalle tengan obligatoriamente un único componente. Como en Workflow, dos acciones pueden pertenecer al mismo componente: elegir caja y marcar listo son parte de preparar el pedido.

**Ventaja:** descubre actividades que no aparecen en el recorrido del cliente. **Riesgo:** si se convierte cada acción de interfaz en un componente, aparecen fragmentos demasiado pequeños y una red de dependencias difícil de mantener.

## Cómo combinarlos

Elaboración didáctica: usa Workflow para entender continuidad y Actor/Action para comprobar cobertura. Si el recorrido de compra no menciona al preparador, su inventario de acciones revela un hueco. Si la lista de actores produce acciones sin contexto, el flujo muestra cuándo tienen sentido.

**Ejercicio resuelto.** Un temporizador cierra una subasta al vencer el plazo. No hay clic humano. ¿Se omite el componente? No. El sistema actúa como actor: la acción «cerrar subasta» debe asignarse a una responsabilidad del modelo. Luego se revisará si corresponde a Sesión de subasta o merece otro límite por razones concretas.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/03 Ciclo de identificación y refinamiento|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/05 Trampa de entidades y nombres responsables|Siguiente →]]
