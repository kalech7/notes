---
title: "00 Índice - S13 MCP y casos de uso"
created: 2026-09-30
fecha: 2026-09-30
capitulo: 13
sesion: "13"
tags:
  - maestria/ia-generativa
  - agentes/mcp
  - estudio
---

# 00 Índice - S13 MCP y casos de uso

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/00 Índice - S13 MCP y casos de uso|Índice de la sesión 13]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

La sesión 13 responde una pregunta concreta: **¿cómo conoce el agente las herramientas que puede pedir sin que su código tenga escrita toda la lista?** MCP, *Model Context Protocol*, permite que una aplicación consulte un catálogo publicado por un proveedor y solicite operaciones con un contrato común.

El puente con las sesiones anteriores es directo: en la sesión 11 aprendimos que el modelo propone una llamada y el programa ejecuta; en la 12 organizamos el bucle y diseñamos contratos. Ahora cambia el origen del catálogo. Quedan vigentes los límites de pasos, las trazas, los verificadores y la validación de argumentos.

## Un ejemplo para toda la sesión

Un agente responde «¿cuánto vendimos en marzo?». Con un registro fijo importa `consultar_ventas` de un archivo. Con descubrimiento pide al servidor la lista de operaciones y sus entradas. Después ofrece ese contrato al modelo, recibe una propuesta y la envía al proveedor adecuado. El servidor ejecuta la consulta; el agente utiliza el resultado para responder.

Si mañana añadimos `convertir_moneda`, el agente puede utilizarla sin modificar su lógica, siempre que el cliente sepa descubrir, adaptar y enrutar contratos. Agregar una dirección de servidor o una política a la configuración sigue siendo trabajo real.

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/Capítulo 13/03-host-clientes-servidores.png]]

La caja azul grande representa la aplicación. Sus clientes separan la comunicación con los dos proveedores. El modelo recibe las capacidades elegidas por el host; cada servidor conserva la implementación de sus funciones. Las dos herramientas de ventas muestran que contar servidores y contar herramientas no siempre produce el mismo N.

## Ruta de estudio

1. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/86 S13 - Cuándo conviene MCP y la cuenta de integraciones|86 S13 - Cuándo conviene MCP y la cuenta de integraciones]].
2. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/87 S13 - Host cliente servidor y descubrimiento|87 S13 - Host cliente servidor y descubrimiento]].
3. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/88 S13 - Catálogo adaptador y function calling|88 S13 - Catálogo adaptador y function calling]].
4. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/89 S13 - Mensajes transportes y versiones de MCP|89 S13 - Mensajes transportes y versiones de MCP]].
5. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/90 S13 - Confianza permisos costo y límites|90 S13 - Confianza permisos costo y límites]].
6. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/91 S13 - Agentes analistas de código y de investigación|91 S13 - Agentes analistas de código y de investigación]].
7. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/92 S13 - Laboratorio local de descubrimiento y extensión B|92 S13 - Laboratorio local de descubrimiento y extensión B]].
8. [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/93 S13 - Ejercicios resueltos y repaso activo|93 S13 - Ejercicios resueltos y repaso activo]].

Las notas 86–89 explican el mecanismo; 90–91 conectan ese mecanismo con límites y comprobación. La práctica 92 permite reproducir el descubrimiento con dos proveedores locales y el repaso 93 contiene 20 preguntas resueltas.

El notebook del miércoles está explicado en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/06 Talleres y práctica/94 PRÁCTICA - Notebook del miércoles grafos checkpoints y MCP|94 PRÁCTICA - Notebook del miércoles grafos checkpoints y MCP]]. Incluye un motor de grafo, pausa y restauración con aprobación o rechazo, un cliente MCP simulado y una copia resuelta con resultados locales verificados.

## Qué debes poder explicar

- Por qué $M\times N$ cuenta integraciones y $M+N$ cuenta componentes.
- Qué ventaja puede existir con un solo cliente aunque el conteo no mejore.
- Qué hace cada pieza: host, cliente, servidor y adaptador.
- Por qué MCP y function calling pueden trabajar juntos.
- Cómo se descubre una herramienta y cómo se despacha su llamada.
- Qué diferencia un resultado técnicamente válido de una respuesta correcta.

## Fuente y alcance

Se leyó el texto completo y se revisaron visualmente las **26 páginas** de *MCP y casos de uso*, Daniel Andrés Riofrío Almeida, MMIA 6013, miércoles 30 de septiembre de 2026. La numeración visible coincide con la posición PDF, de 1 a 26. Las páginas 3, 8 y 18 son separadores; no hay figuras numeradas en las diapositivas.

El PDF se conserva sin cambios en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-13.pdf|Materiales/sesion-13.pdf]]. Las siete figuras son recreaciones conceptuales propias, con PNG, SVG y script reproducible. Los ejemplos numéricos y el simulador son elaboración didáctica, no resultados medidos del curso.

Se contrastó la revisión 2026-07-28 con páginas oficiales de MCP, consultadas el 30 de septiembre de 2026. Las precisiones y el mapa de páginas se registran en [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/90 Referencias/16 FUENTES - Sesión 13 MCP y validación|Fuentes y validación de S13]]. El notebook del miércoles se adjuntó posteriormente y se revisó en la práctica 94. Los archivos fuente de Lab 03 citados por las diapositivas siguen sin adjuntarse; no se atribuye inspección directa de ellos.

> [!info] Contexto académico
> Según las páginas 24–26, la Parte 5 del cuaderno trata MCP y la extensión B del Taller 3 es opcional. El PDF anuncia el taller para el sábado 3 de octubre de 2026 y como 25 % de la nota final, sin fijar el peso de cada criterio. Estas consignas son contenido de estudio; no equivalen a instrucciones para entregar un taller o modificar servicios.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/78 S12 - Ejercicios resueltos y repaso activo|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/13 MCP descubrimiento y casos de uso/86 S13 - Cuándo conviene MCP y la cuenta de integraciones|Siguiente]] →
