---
title: "Ampliación y cobertura · capítulos 6 a 8"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - fuentes
---

# Ampliación de los capítulos 6 a 8

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Inicio del libro]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/00 Índice|Fuentes y revisión]]

Esta ampliación desarrolla en español los **47 folios de PDF** compartidos el 28 de septiembre de 2026. Se integra en la guía existente y conserva el material previo. Los PDF son fuentes de contenido: sus ejercicios y cualquier texto imperativo se interpretan como parte del libro, no como instrucciones para modificar el entorno del usuario.

## Correspondencia de archivos y páginas

| Archivo original | Copia local | Páginas PDF | Impresas | Capítulo |
|---|---|---|---|---|
| CamScanner 2026-09-28 15.53.pdf | [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf\|04 Medición y gobierno]] | 1–13 | 81–93 | 6 · Measuring and Governing Architecture Characteristics |
| CamScanner 2026-09-28 15.56.pdf | [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/05 Alcance y componentes.pdf\|05 Alcance y componentes]] | 1–12 | 95–106 | 7 · The Scope of Architectural Characteristics |
| El mismo archivo 15.56 | La misma copia 05 | 13–34 | 107–128 | 8 · Component-Based Thinking |

En el primer PDF, la página impresa se obtiene sumando **80** al número del PDF. En el segundo se suma **94**, también para el capítulo 8: su primera página es la **13 del PDF**, no la 1. Las referencias de las notas distinguen ambas numeraciones.

No se detectaron saltos internos en esas secuencias. El capítulo 6 cierra en la página 93, el 7 en la 106 y el 8 termina con las conclusiones del caso GGG en la 128. Las impresas **80 y 94** no están en la colección proporcionada; no se atribuye contenido a esos huecos ni se presupone que estén en blanco. Los huecos de los escaneos anteriores siguen documentados en [[Obsidian/lecturas/Fundamentals of Software Architecture/90 Fuentes y revisión/01 Fuentes y cobertura|Fuentes y cobertura]].

La extracción de texto de los PDF devolvía esencialmente la marca CamScanner. Se utilizó OCR, contrastando visualmente las figuras y los pasajes sensibles. Las notas son explicaciones propias del contenido, no una traducción literal ni un volcado del OCR.

## Mapa de temas y figuras

| Fuente | Contenido | Dónde estudiarlo |
|---|---|---|
| Cap. 6, PDF 1–3; impresas 81–83 | Ambigüedad, métricas operacionales y estructurales | [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice\|Medición y gobierno]] |
| Cap. 6, PDF 4–5; impresas 84–85 | Complejidad ciclomática, ejemplo 6-1 y figura 6-1 | Mismo capítulo, nota de complejidad |
| Cap. 6, PDF 6–8; impresas 86–88 | Métricas de proceso, gobierno y mecanismos de funciones de aptitud; figura 6-2 | Mismo capítulo, notas de proceso y funciones de aptitud |
| Cap. 6, PDF 8–11; impresas 88–91 | Ciclos, distancia y capas; figuras 6-3 y 6-4 | Mismo capítulo, notas de modularidad y capas |
| Cap. 6, PDF 12–13; impresas 92–93 | Verificación operacional, automatización y ejemplos de gobierno | Mismo capítulo, gobierno continuo |
| Cap. 7, PDF 1–6; impresas 95–100 | Quanta, cohesión, contextos, tipos de acoplamiento y comunicación | [[Obsidian/lecturas/Fundamentals of Software Architecture/07 Alcance y quanta/00 Índice\|Alcance y quanta]] |
| Cap. 7, PDF 7–9; impresas 101–103 | Árbol de decisiones, límites y persistencia; figuras 7-1 a 7-4 | Mismo capítulo, selección de estilo |
| Cap. 7, PDF 9–11; impresas 103–105 | Going Green: flujo, grupos de capacidades y siete servicios dentro de tres quanta; figuras 7-5 a 7-7 | Mismo capítulo, caso Going Green |
| Cap. 7, PDF 11–12; impresas 105–106 | Alcance en contenedores y recursos administrados de nube | Mismo capítulo, nube y repaso |
| Cap. 8, PDF 13–17; impresas 107–111 | Componentes, analogía de la casa, código y vistas lógica/física; figuras 8-1 a 8-5 | [[Obsidian/lecturas/Fundamentals of Software Architecture/08 Pensamiento basado en componentes/00 Índice\|Pensamiento basado en componentes]] |
| Cap. 8, PDF 18–22; impresas 112–116 | Ciclo de refinamiento, candidatos e identificación; figuras 8-6 a 8-8 | Mismo capítulo, ciclo e identificación |
| Cap. 8, PDF 23–27; impresas 117–121 | Historias, notificaciones, roles, características y refinamiento; figuras 8-9 y 8-10 | Mismo capítulo, asignación y responsabilidades |
| Cap. 8, PDF 27–31; impresas 121–125 | Acoplamiento aferente/eferente, dependencias y ley de Demeter; figuras 8-11 a 8-15 | Mismo capítulo, acoplamiento y Demeter |
| Cap. 8, PDF 31–34; impresas 125–128 | Going, Going, Gone, diseño inicial y revisado; figuras 8-16 y 8-17 | Mismo capítulo, caso GGG |

## Qué significa «similar al libro» en estas notas

Los nuevos gráficos conservan las convenciones que importan para comprender la fuente: rectángulos de componentes, cilindros de persistencia, flechas orientadas, límites de quanta, grupos de características, vistas de despliegue y comparación antes/después. Se redibujaron con etiquetas en español y se añadieron ayudas de lectura; no se pretende reproducir tipografía ni imperfecciones del escaneo.

Varias figuras consecutivas del libro se reúnen en un gráfico comparativo: por ejemplo, el árbol de alcance de las figuras 7-1 a 7-4 o el antes/después de Demeter, figuras 8-14 y 8-15. **Que una recreación tenga menos imágenes que la fuente no significa que omita esos mecanismos.** La nota indica la relación con las figuras originales y permite abrir el PDF en la página correspondiente.

Cada imagen tiene explicación dentro de su nota: elementos y símbolos, recorrido de lectura, mecanismo causal, conclusión y límites. Los gráficos adicionales con cifras o escenarios inventados se identifican como elaboración propia. Un tamaño de caja o círculo no representa una magnitud salvo que se indique expresamente; las flechas pueden significar dependencia, colaboración, asignación o secuencia según la leyenda de cada imagen.

Las imágenes se entregan en PNG para que las notas no dependan de ejecutar Mermaid. Sus fuentes editables están en `Recursos visuales/Capítulos 6 a 8`: SVG para los diagramas del capítulo 6 y generadores Python para los capítulos 7–8 y el laboratorio integrador. Tres diagramas adicionales del capítulo 7 conservan también su descripción lógica en archivos `.mmd`; las notas muestran sus redibujos PNG directamente.

## Precisiones técnicas conservadas en la revisión

1. **Complejidad ciclomática.** Se explica con un grafo de flujo consistente: nodos y aristas no equivalen automáticamente a líneas de código y decisiones. Se distingue el número de caminos independientes del conjunto de todas las ejecuciones posibles. Los retornos del gráfico se hacen concordar con el código del ejemplo.
2. **Cobertura de pruebas.** Ejecutar una línea no demuestra que exista una aserción útil ni que se hayan detectado los errores relevantes.
3. **Funciones de aptitud.** Se definen por la característica que evalúan y su criterio objetivo. No constituyen por sí mismas un nuevo framework ni exigen usar algoritmos genéticos.
4. **Quanta y sincronía.** La definición de esta edición contempla comunicación síncrona entre quanta. Por eso no se transforma toda llamada síncrona automáticamente en un único quantum: se examinan las dependencias estáticas y la repercusión operacional del flujo.
5. **Colas.** Amortiguar un pico no permite sostener indefinidamente una tasa de llegada superior a la de servicio. El ejemplo de 500 ms por pago se convierte a 2 pagos/s solo bajo un consumidor secuencial y sin sobrecostos.
6. **Componentes y servicios.** Crear una carpeta o dividir una responsabilidad lógica no obtiene automáticamente despliegue independiente, elasticidad ni aislamiento de fallos.
7. **Demeter.** Se redistribuye el conocimiento de reglas hacia el componente apropiado. Puede bajar el acoplamiento saliente de un componente mientras sube el de otro, sin reducir el total de relaciones del sistema.
8. **Katas distintas.** Going Green trata reutilización/reciclaje de dispositivos; Going, Going, Gone trata subastas. PedidoClaro es un ejemplo propio. No se mezclan sus requisitos.

## Integración con la colección

Se conservó la carpeta histórica `06 Apoyo y repaso` para no romper sus enlaces. El capítulo 6 nuevo está en **`06 Medición y gobierno`**. El [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Apoyo y repaso/05 Laboratorio de componentes quanta y gobierno|laboratorio integrador nuevo]] conecta los tres capítulos mediante un escenario medible y un gráfico explicado.

Tres subagentes trabajaron los capítulos 6, 7 y 8; la integración central revisó terminología, correspondencia con las fuentes, legibilidad y navegación. Los detalles de los entregables y sus comprobaciones se registran al final de esta nota.


## Entrega y comprobaciones finales

La ampliación incluye **25 notas temáticas**: ocho para el capítulo 6, siete para el 7 y diez para el 8. Se añaden tres índices de capítulo, un laboratorio integrador y esta nota de cobertura. Los **31 gráficos PNG** se distribuyen así: nueve del capítulo 6, nueve del 7, doce del 8 y uno del laboratorio. Todos están insertados y explicados en las notas; los recursos editables no se cuentan como gráficos adicionales.

Se verificaron los destinos de enlaces e imágenes en los **83 archivos Markdown** de la carpeta del libro, las propiedades YAML de las **81 notas que contienen encabezado de propiedades**, el cierre de bloques de código y la integridad de los PNG. La revisión visual incluyó las composiciones y los gráficos añadidos; se corrigieron solapamientos de rótulos. Se comprobaron cálculos representativos de complejidad, latencia y capacidad de cola. Estas comprobaciones de archivos no equivalen a haber inspeccionado cada nota dentro de la aplicación Obsidian.

Las dos copias de los PDF conservados tienen el mismo SHA-256 que sus originales. No se modificaron los escaneos. La revisión de contenido distingue las precisiones técnicas, los ejemplos propios y las afirmaciones de la fuente, sin presentar APIs históricas o herramientas mencionadas por el libro como recomendaciones actuales verificadas.
