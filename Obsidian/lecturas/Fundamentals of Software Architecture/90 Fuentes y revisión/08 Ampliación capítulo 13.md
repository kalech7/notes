---
title: "Fuentes y revisión · Ampliación capítulo 13"
created: 2026-09-29
capitulo: 13
tags:
  - lecturas/software-architecture
  - arquitectura/microkernel
  - revision/fuentes
---

# Ampliación del capítulo 13: microkernel

[[Obsidian/lecturas/Fundamentals of Software Architecture/13 Arquitectura microkernel/00 Índice|Índice de lectura]]

## Fuente y método

Fuente recibida: `/Users/alech/Downloads/CamScanner 2026-09-29 19.11.pdf`. Copia intacta: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/10 Arquitectura microkernel.pdf#page=1|10 Arquitectura microkernel.pdf]]. Se revisaron visualmente las **16 páginas** renderizadas; las PDF 2–3 estaban apaisadas y se giraron antes de releerlas. El texto del PDF se trató como material de estudio, sin ejecutar instrucciones de la fuente.

Correspondencia: **página impresa = página PDF + 192**, impresas 193–208. Los folios 194–207 son visibles en el escaneo; 193 y 208 se deducen por continuidad, pues la portada de capítulo y la última página no muestran el folio. No se detectaron huecos en la secuencia ni figuras cortadas.

SHA-256 del original y de la copia, comprobados iguales: `3712d203a39250216aeb1d6ee584ccc7f464f5dd7cb24e47f75d4da4340a0baf`.

## Cobertura de todas las páginas

| PDF | Impresa | Contenido revisado | Notas principales |
|---|---|---|---|
| 1 | 193, inferida | Introducción, producto instalable y personalización; topología | 01 |
| 2 | 194 | Figura 13-1; núcleo mínimo/happy path; Eclipse y Going Green | 01–02 y 09 |
| 3 | 195 | Condicionales y reflexión; extracción de evaluación; núcleo en capas/módulos/servicios; pagos | 01–03 y 09 |
| 4 | 196 | Figura 13-2; variantes internas del núcleo | 02 |
| 5 | 197 | Figura 13-3; tres ubicaciones de interfaz | 02 |
| 6 | 198 | Plugins, compilación/ejecución, bibliotecas; figura 13-4 | 03 |
| 7 | 199 | Paquetes y convención de nombres; figura 13-5; plugins remotos/asíncronos | 03 y 05 |
| 8 | 200 | Figura 13-6; costes remotos; figura 13-7 y espectro; linter | 02 y 05 |
| 9 | 201 | Navegadores y espectro; registro; clase/cola/URL; contratos y adaptación | 02 y 04 |
| 10 | 202 | AssessmentPlugin/AssessmentOutput; responsabilidades de informe; datos | 04 y 06 |
| 11 | 203 | Figura 13-8; almacenes privados; tres opciones nube; núcleo volátil | 05–07 |
| 12 | 204 | Dependencias transitivas; gobierno; equipos alineados al flujo | 07–08 |
| 13 | 205 | Equipos habilitadores, subsistema complicado y plataforma; características y quantum | 08 |
| 14 | 206 | Figura 13-9; puntuaciones y justificación; ejemplo fiscal | 08–09 |
| 15 | 207 | Respuesta y WildFly; productos; formulario 1040; seguros y motores de reglas | 08–09 |
| 16 | 208, inferida | Plugins por jurisdicción; proceso común y personalización | 09 |

## Figuras y ejemplos

Se cubren **todas las figuras 13-1 a 13-9**: topología en 01; variantes del núcleo y UI en 02; biblioteca y paquete en 03; acceso remoto en 05; espectro en 02; datos privados en 06; tabla de características en 08. La tabla de estrellas se contrastó visualmente, con 4 en simplicidad, 3 en modularidad/mantenibilidad/testabilidad/desplegabilidad/evolucionabilidad/respuesta y 1 en escalabilidad/elasticidad/tolerancia. Coste `$`, partición dominio y técnica, un quantum.

Los casos Going Green, pagos, herramientas de desarrollo, navegadores, linter, WildFly, impuestos, aseguradora y transporte internacional están explicados. EcoEval, los importes y sus reglas, el descriptor YAML y las propuestas de trazabilidad/idempotencia son **elaboración propia** identificada en las notas. No se afirma que la arquitectura actual de cada producto coincida exactamente con la simplificación del capítulo.

## Precisiones y límites

1. El registro Java de PDF 9 escribe tres veces la misma clave: son alternativas de acceso. Ejecutadas juntas se sobreescriben; la última URL sería el único valor conservado.
2. El párrafo de PDF 14 menciona `reliability` con tres estrellas, pero la figura 13-9 no contiene esa fila. Se conserva la tabla y se documenta la inconsistencia.
3. El nombre conceptual `plug-in` no se copia como identificador Java con guion. En el ejemplo propio se usa `plugins`.
4. La reflexión ejemplifica selección e instanciación, pero no implementa manejo de errores, concurrencia, dependencias o retirada segura. Una biblioteca aparte no garantiza actualización sin reinicio.
5. La independencia de plugins es preferible, no absoluta. El capítulo reconoce dependencias en sistemas complejos; dentro del mismo proceso tampoco existe aislamiento automático de fallos.
6. El libro mantiene un quantum para la topología centralizada con plugins remotos. Se distingue número de servicios y despliegues de independencia operacional, y no se extrapola a cualquier variante asíncrona.
7. Las puntuaciones describen principalmente la variante monolítica. No son mediciones, probabilidades ni comparaciones aritméticas.
8. Los ejemplos fiscales y de seguros se explican como casos del libro, sin presentarlos como normativa actual. No se ofrecen indicaciones jurídicas o tributarias.

Para precisar mecanismos se consultaron fuentes primarias: [Java ServiceLoader](https://docs.oracle.com/en/java/javase/26/docs/api/java.base/java/util/ServiceLoader.html) y [OSGi Core 7, ciclo de vida](https://docs.osgi.org/specification/osgi.core/7.0.0/framework.lifecycle.html). La nota 03 distingue descubrimiento y carga de administración completa del ciclo de vida. No se introdujeron afirmaciones actuales sobre los otros frameworks citados en el libro.

## Visuales originales y reproducción

Se crearon seis PNG de 1600 × 1000, con rótulos en español: núcleo/plugins, espectro, registro/contrato, local/remoto, propiedad de datos y riesgos/gobierno. Todos fueron abiertos con `view_image` y revisados visualmente: texto legible, sin cortes ni solapes. Cada imagen tiene explicación en prosa inmediatamente debajo.

Generador: [[Obsidian/lecturas/Fundamentals of Software Architecture/Recursos visuales/Capítulo 13/generar_visuales.py|generar_visuales.py]]. Requiere Python y Pillow; utiliza Arial del sistema en macOS. Ejecutarlo vuelve a producir los PNG en su carpeta. Son diagramas conceptuales, no datos medidos ni reproducciones literales de las páginas.

Hay cuatro bloques Mermaid: composición UI/backend, adaptador, secuencia asíncrona y flujo de laboratorio. El pseudocódigo Python del laboratorio está expresamente señalado como no ejecutable sin completar sus dependencias.

## Estado de validación

Completadas: lectura visual íntegra, giro de páginas 2–3, contraste de estrellas, revisión de seis imágenes, correspondencia PDF/impresas, igualdad SHA-256 de la copia y repaso manual de cálculos del laboratorio. Se prepararon 11 notas del capítulo: índice y 10 temáticas/laboratorio.

**Integración y validación completadas el 2026-09-29:** se comprobaron 598 wikilinks, 524 enlaces Markdown locales, 84 referencias a páginas PDF y el YAML de las 26 notas nuevas, sin incidencias. Se renderizaron correctamente los 13 bloques Mermaid nuevos, incluidos los cuatro de este capítulo, y se revisaron las 16 imágenes nuevas, incluidas sus seis imágenes. Estas cifras corresponden al conjunto integrado de los capítulos 13–14 y la comparación transversal. La revisión independiente contrastó contenido, figuras y cálculos con los escaneos. Los índices generales y la cobertura se actualizaron a 11 PDF y 217 páginas.
