---
title: "13 · Riesgos, dependencias y gobierno"
created: 2026-09-29
capitulo: 13
tags:
  - lecturas/software-architecture
  - arquitectura/microkernel
---

# Riesgos, dependencias y gobierno

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/00 Índice|← Índice del capítulo 13]]

**El estilo pierde su ventaja si todas las variantes siguen cambiando el núcleo o si los plugins forman una red de dependencias.** El capítulo identifica estos dos riesgos y propone vigilar que la implementación respete la separación.

## Núcleo volátil

La **volatilidad** es la frecuencia y amplitud del cambio. El núcleo debería estabilizarse después de la construcción inicial; las personalizaciones se concentran en extensiones. Si cada nueva jurisdicción añade otra condición central, el diseño conserva el nombre microkernel pero pierde el beneficio de contener las variantes.

No todo cambio del núcleo es un fallo. Una capacidad común nueva, una corrección de seguridad o un ajuste de contrato pueden requerirlo. La señal de problema es que reglas particulares obliguen de forma recurrente a modificar el flujo general. El remedio del libro es refactorizar cuando la volatilidad se estimó mal: mover la decisión variable hacia el punto de extensión apropiado y revisar el contrato que la permitía filtrarse.

![Núcleo volátil y dependencias entre plugins](../Recursos%20visuales/Cap%C3%ADtulo%2013/c13-06-riesgos-gobierno.png)

Las cajas rojas muestran dos causas diferentes. A la izquierda crece el centro con condiciones por variante. A la derecha una dependencia lateral convierte la actualización de A en una coordinación con B y C. Las cajas verdes vinculan cada riesgo con su revisión: distribución del cambio para el primero y estructura/versiones para el segundo. La revisión no busca prohibir toda evolución, sino conservar una frontera útil.

## Dependencias transitivas entre extensiones

Una dependencia **transitiva** aparece cuando A necesita B y B necesita C: A queda condicionado indirectamente por C. Si dos plugins requieren versiones incompatibles de una biblioteca, la plataforma puede necesitar resolver conflictos de carga o compatibilidad.

El capítulo desaconseja dependencias entre plugins, pero reconoce que sistemas complejos como Eclipse pueden tenerlas. Por tanto, «no deben existir» describe una preferencia de diseño, no una imposibilidad técnica. Si se admiten, hay que administrar un grafo de dependencias y determinar qué combinaciones se pueden instalar, activar y actualizar.

Por ejemplo propio, un evaluador de teléfono llama directamente al evaluador de batería y este al de seguridad. Retirar el plugin de seguridad puede dejar a los otros incapaces de trabajar. Si la evaluación de batería es realmente una capacidad compartida estable, hay que decidir si pertenece a un servicio del núcleo o a una biblioteca técnica compatible. No conviene resolver automáticamente cualquier duplicación poniendo un plugin a llamar a otro: puede transformar una frontera de variantes en una cadena frágil.

## Gobierno como comprobación continua

**Gobierno arquitectónico** significa revisar que las decisiones sigan produciendo el comportamiento buscado. El libro menciona funciones de aptitud (*fitness functions*), comprobaciones que detectan desviaciones, vinculadas a historial de cambios, contratos y estructura.

| Comprobación del libro | Evidencia útil | Interpretación cuidadosa |
|---|---|---|
| Volatilidad del núcleo | Historial de cambios en control de versiones | Un pico de cambios puede ser una refactorización legítima |
| Tasa de cambio del núcleo | Cambios en períodos comparables | Interesa por qué cambia, además de cuántas veces |
| Pruebas de contrato | Compatibilidad núcleo–plugin | Detectan firmas y significado acordado |
| Verificaciones estructurales | Importaciones y dependencias | Detectan acceso lateral o acceso a internals |

Como ejemplo propio, si 8 de 10 variantes nuevas obligan a tocar el núcleo, hay evidencia para revisar la frontera. Es un conteo ilustrativo, no un umbral del libro. Si una refactorización concentró cambios en una semana y luego cada variante quedó aislada, el mismo conteo necesita otra interpretación.

Una prueba estructural puede impedir que `plugins.telefono` importe `plugins.tableta` o clases de persistencia internas del núcleo. Una prueba de contrato puede verificar que `resell=false` se maneja sin intentar registrar una venta. Una prueba de integración valida descubrimiento, registro e invocación juntos. Cada prueba responde a un riesgo distinto; probar únicamente el cálculo del plugin no cubre que el núcleo lo haya seleccionado bien.

## Versiones y terceros

El libro destaca las pruebas de contrato cuando distintos plugins evolucionan gradualmente y soportan versiones diferentes. La matriz núcleo versión A → plugins compatibles permite detectar una extensión que todavía depende de una firma retirada. Para una extensión de tercero, el adaptador puede reducir el impacto de cambios externos, pero también necesita propietario y pruebas.

Como ampliación práctica, ejecutar código de terceros dentro del proceso le concede capacidades que deben conocerse. Un contrato pequeño no es una barrera de seguridad por sí mismo. Si se requiere aislar código no confiable, hay que diseñar una frontera de ejecución apropiada; la palabra plugin no ofrece esa garantía.

> [!question]- ¿Un núcleo que cambia durante el arranque del proyecto demuestra un mal diseño?
> No. La fase inicial descubre responsabilidades y contratos. El riesgo es que las variantes continúen modificándolo repetidamente después de establecer el flujo común, sin una razón transversal.

> [!question]- ¿Una prueba del plugin garantiza que nunca rompe otro plugin?
> No. Puede compartir recursos o dependencias técnicas. Se necesitan contratos, verificaciones estructurales y pruebas de combinaciones relevantes. La independencia lógica disminuye impacto, pero no prueba aislamiento operativo.

## Fuente principal

[[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/10 Arquitectura microkernel.pdf#page=11|PDF 11–12 · impresas 203–204 · núcleo volátil, dependencias y gobierno]]. Ejemplos numéricos, reglas de importación y límites de seguridad son elaboración propia.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/06 Datos y propiedad del estado|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/08 Equipos características y elección|Siguiente →]]
