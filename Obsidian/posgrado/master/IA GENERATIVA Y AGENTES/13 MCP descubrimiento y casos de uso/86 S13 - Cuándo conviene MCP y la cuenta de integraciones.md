---
title: "86 S13 - Cuándo conviene MCP y la cuenta de integraciones"
created: 2026-09-30
fecha: 2026-09-30
capitulo: 13
sesion: "13"
tags:
  - maestria/ia-generativa
  - agentes/mcp
  - estudio
---

# 86 S13 - Cuándo conviene MCP y la cuenta de integraciones

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|Índice de la sesión 13]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

## El problema antes del protocolo

Una **integración** es el trabajo que permite a una aplicación utilizar un sistema: saber qué operación pedir, con qué datos, dónde enviarla y cómo entender la respuesta. Si un agente, un IDE y un chat de soporte necesitan acceder a ventas, documentos, calendario e incidencias, hay 3 aplicaciones y 4 sistemas.

En el modelo de la diapositiva cada aplicación se conecta a cada sistema, por lo que hay:

$$M\times N=3\times4=12\text{ integraciones específicas}.$$

Con un contrato común, los proveedores exponen sus capacidades y las aplicaciones reutilizan clientes compatibles. El dibujo cuenta:

$$M+N=3+4=7\text{ componentes reutilizables}.$$

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 13/01-integraciones-y-piezas.png]]

A la izquierda cada flecha representa una integración propia entre una aplicación y un sistema. A la derecha las aplicaciones y proveedores utilizan el mismo protocolo. La franja naranja expresa el contrato compartido; no es necesariamente un servicio central que haya que desplegar. Las cantidades comparan la forma de crecimiento del trabajo, no segundos, dinero ni rendimiento.

## La desigualdad paso a paso

El conteo de pares supera el de piezas cuando:

$$MN>M+N.$$

Restamos ambos términos de la derecha y sumamos uno:

$$MN-M-N+1>1.$$

El lado izquierdo se factoriza:

$$\boxed{(M-1)(N-1)>1}.$$

| Aplicaciones M | Unidades proveedoras N | MN: integraciones | M+N: piezas | Resultado del conteo |
| --- | --- | --- | --- | --- |
| 1 | 3 | 3 | 4 | La suma es mayor |
| 1 | 10 | 10 | 11 | La suma es mayor |
| 2 | 2 | 4 | 4 | Empate |
| 2 | 3 | 6 | 5 | El producto es mayor |
| 3 | 4 | 12 | 7 | El producto es mayor |
| 5 | 5 | 25 | 10 | El producto es mayor |

Con $M=1$, el producto $(M-1)(N-1)$ vale cero, aunque aumentemos N. El protocolo no se justifica por reducir ese conteo. Esta conclusión **solo vale para el argumento de conteo**: todavía puede convenir por reutilización, desacople o proveedores ya disponibles.

## Qué cuenta realmente N

Las diapositivas alternan «herramientas», «sistemas» y «servidores» para explicar la simplificación. En una implementación, un servidor puede publicar diez herramientas. Conviene fijar N como **unidades que habría que integrar por separado** y conservar esa unidad en las dos columnas. No tiene sentido contar diez funciones a la izquierda y dos servidores a la derecha sin explicar la agrupación.

La cuenta también supone una red completa: todas las aplicaciones necesitan todos los proveedores. Si solo se requieren cinco pares, hay cinco integraciones directas, no doce. Además, un host puede crear un cliente por servidor. $M+N$ representa componentes o adaptaciones reutilizables, no el número de todas las instancias, conexiones o despliegues.

## El argumento de la herramienta siguiente

El beneficio con un agente pequeño puede ser que la nueva capacidad no obligue a editar su lógica. Con un registro fijo, `convertir_moneda` debe añadirse donde el agente conoce nombres, contratos y rutas. Con descubrimiento, el proveedor la publica y el cliente vuelve a consultar el catálogo.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 13/02-herramienta-siguiente.png]]

El primer recorrido coloca el conocimiento de la herramienta en el agente. El segundo lo desplaza hacia el proveedor y el cliente. El agente sigue consumiendo un catálogo y pidiendo una operación por nombre. Se conserva su código, pero se debe actualizar la configuración necesaria y comprobar el nuevo comportamiento.

**Costo marginal** significa el trabajo adicional de incorporar la siguiente capacidad. No es igual al costo total de haber creado y operado el sistema. El protocolo puede mejorar el primero y aumentar el segundo en un laboratorio de una sola aplicación.

## Una decisión razonada

Un script pequeño con tres funciones estables puede resolverse con un registro explícito. Varias aplicaciones que comparten capacidades, herramientas mantenidas por otros equipos o incorporaciones frecuentes pueden justificar descubrimiento. Para decidir hacen falta cambios esperados, compatibilidad, mantenimiento y costos observados; el álgebra ayuda a plantear el problema.

> [!question]- Si 25/10=2,5, ¿el agente será 2,5 veces más rápido?
> No. Se dividieron integraciones entre componentes, no dos mediciones de latencia. La cantidad no es un factor de velocidad ni de ahorro económico.

Fuente de clase: PDF 4–7 · numeración visible igual a la página PDF · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-13.pdf#page=4|Sesión 13]].

Las aclaraciones sobre redes incompletas, unidades y costo marginal son elaboración propia a partir del modelo de las diapositivas.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/87 S13 - Host cliente servidor y descubrimiento|Siguiente]] →
