---
title: "07 Repaso activo, transferencia y respuestas - M11"
modulo: M11
tags:
  - master/matematicas-programacion
  - m11
---

# 7. Recordar, explicar y transferir el método

## La historia que debes poder contar sin mirar

“Recibo resultados anteriores y una ficha HTML del origen. Extraigo su estructura, limpio el texto y preparo columnas tipadas. Reviso nulos, dominios, claves y referencias. Integro con el registro experimental y con un diseño esperado independiente. Compruebo que cada combinación tenga exactamente una ejecución elegible. Resumo por configuración, calculo el ranking preservando empates y organizo sus dependencias en dbt. Reconstruyo desde salidas limpias y comparo contenido. Declaro qué demuestra el resultado y qué no”.

## Frases cortas para recordar lo difícil

| Frase | Qué evita olvidar |
|---|---|
| parser encuentra; regex reconoce; Polars tipa | estructura, forma y tipo son niveles distintos |
| DuckDB calcula; dbt organiza | motor SQL y dependencias no son la misma responsabilidad |
| primero lista de invitados, luego asistentes | diseño esperado independiente |
| convertir no es validar todo | strict=True no sustituye nulos, dominio y claves |
| más filas no son más corridas | multiplicidad del JOIN |
| cobertura antes de promedio | no comparar grupos incompletos como si fueran equivalentes |
| ref es dependencia; ON es correspondencia | grafo y unión relacional son distintos |
| hash conserva; prueba comprueba | bytes iguales no implican validez |
| igual respuesta no exige igual archivo | comparación de contenido frente a hash de la base |
| dependencia + prueba + límite | estructura de una defensa del producto |

## Diccionario pequeño

| Término | Explicación sencilla |
|---|---|
| pipeline | pasos conectados para transformar datos |
| fixture | entrada fija y controlada para un ejercicio o prueba |
| procedencia | origen y evidencia asociados a una entrada |
| esquema | nombres y tipos de las columnas |
| contrato | condiciones que una entrada o salida debe cumplir |
| granularidad | qué representa una fila |
| cardinalidad | cuántas correspondencias hay entre entidades o filas |
| población elegible | ejecuciones que cumplen las condiciones del análisis |
| cobertura | correspondencia entre lo esperado y lo encontrado |
| predicado | condición concreta que una prueba evalúa |
| staging | etapa inicial de transformación; en este caso integra la población |
| mart | producto tabular preparado para una pregunta analítica |
| dependencia | un resultado necesita otro para construirse |
| reconstrucción limpia | producir de nuevo desde entradas sin depender de salidas previas |

## Mini examen: abre la respuesta después de intentarlo

> [!question]- 1. ¿Para qué sirve M11 si M10 ya calcula el ranking?
> Para explicitar las entradas, sus contratos, el orden de las transformaciones y las pruebas que permiten reconstruir y aceptar el producto. La SQL de comparación puede conservarse.

> [!question]- 2. ¿Qué componente descarga la web en este ejercicio?
> Ninguno tiene que hacerlo: el HTML docente ya está guardado localmente. El parser interpreta su estructura. Descargar mediante HTTP sería una etapa anterior distinta.

> [!question]- 3. ¿Una regex que acepta “28 × 28” prueba que todas las imágenes tienen ese tamaño?
> No. Solo reconoce la forma del texto. Contrastar la ficha con su fuente e inspeccionar imágenes son verificaciones distintas.

> [!question]- 4. ¿Un número entero positivo y no nulo puede seguir siendo incorrecto?
> Sí. Puede no corresponder al origen real. Tipos y dominio no reemplazan la procedencia ni el contraste factual.

> [!question]- 5. ¿Por qué usar Arrow si ya tenemos Polars?
> Para entregar la tabla en una representación común con esquema y tipos a otra herramienta. No se usa para redefinir el ranking.

> [!question]- 6. ¿Por qué se vuelven a validar referencias después de cargar DuckDB?
> Porque copiar datos no garantiza que se hayan transferido todas las restricciones ni que la integración conserve los contratos.

> [!question]- 7. ¿Qué hace mal quien calcula expected_seed_count a partir de staging?
> Puede convertir las ausencias en parte del supuesto diseño. Lo esperado debe venir del plan independiente y validado, no de lo que sobrevivió.

> [!question]- 8. ¿Una media idéntica antes y después del JOIN descarta duplicados?
> No. Una duplicación simétrica puede dejarla igual. Hay que comprobar claves, conteos y unidad de fila.

> [!question]- 9. ¿Qué devuelve RANK para medias 0.9, 0.9 y 0.8?
> 1, 1 y 3, si la ventana ordena solo por la media descendente. El empate ocupa dos filas y el siguiente puesto salta a 3.

> [!question]- 10. ¿Una prueba unique que pasa puede corresponder a una tabla vacía?
> Sí. No hay claves repetidas, pero pueden faltar todas las combinaciones esperadas. Hace falta cobertura.

> [!question]- 11. ¿Qué significa FAIL seguido de skipped para resumen y ranking en el PDF?
> La prueba de cobertura falló y sus descendientes no se construyeron en ese build. No se debe presentar un ranking previo como resultado nuevo.

> [!question]- 12. ¿Qué diferencia hay entre ejecución ausente y métrica ausente?
> En la primera falta el registro esperado en runs o no cumple las condiciones; en la segunda la ejecución existe, pero no tiene la medición objetivo en metrics. El diagnóstico sigue las claves para distinguirlas.

> [!question]- 13. ¿Puedo restaurar una métrica con la media de las demás?
> Eso fabricaría un valor, no recuperaría evidencia original. Si no existe evidencia verificable, hay que declarar el producto incompleto o plantear otro análisis con contrato explícito.

> [!question]- 14. ¿Por qué dos salidas se comparan ordenadas?
> El orden de filas sin ORDER BY no define la identidad de una relación. Un orden estable por claves permite comparar esquema, filas y valores sin confundir diferencias de presentación con diferencias de contenido.

> [!question]- 15. Si todo se reconstruye igual, ¿ya está demostrada la calidad del experimento?
> No. Puede reconstruirse el mismo error. Además, el experimento docente usa train/validation local de 2048/512, dos épocas y dos semillas; no demuestra superioridad general.

## Transferencia a otro problema: regresión

En clasificación con accuracy el dominio es [0,1] y mayor es mejor. En una regresión con MAE, el error es no negativo, tiene las unidades de la variable objetivo y **menor es mejor**. Por eso la ordenación sería ascendente. No se conserva automáticamente el límite superior 1.

Este ejemplo es una ampliación conceptual; no afirma que el PDF ejecute una regresión.

| Decisión | Caso accuracy | Ejemplo MAE |
|---|---|---|
| pregunta | proporción de aciertos | error absoluto medio |
| dirección del ranking | DESC | ASC |
| dominio | finita, entre 0 y 1 | finita, mayor o igual que 0 |
| unidades | proporción | unidades del objetivo, por ejemplo euros |
| identidad y cobertura | diseño del experimento de clasificación | diseño propio del nuevo experimento |

El **método** se transfiere; el **contrato** se redefine: entradas, identidad, mapeo, unidad de fila, población, métrica, diseño y pruebas. Si una versión se reutiliza entre datasets, amplía las claves y las particiones.

> [!question]- Si cambio de accuracy a MAE pero dejo DESC y [0,1], ¿qué ocurre?
> Podría rechazar errores válidos mayores que 1 y poner primero el error más alto. El código puede ejecutar y aun así responder al revés de lo que necesitas.

## Aplicación a tu proyecto de dinámica de mouse

Como analogía de estudio, imagina comparar dos configuraciones sobre sesiones legítimas e impostoras. Antes de promediar tendrías que fijar la partición de usuarios/sesiones, la métrica, las semillas o repeticiones esperadas y qué constituye una ejecución válida. Si una métrica falta, no inventarías su valor. Si cambias el protocolo, ya no es automáticamente la misma comparación.

La forma de trabajar de M11 te permite rastrear qué resultado proviene de qué configuración y datos. No resuelve por sí sola la elección de un buen protocolo ni la fuga de información: esas condiciones también deben diseñarse y comprobarse.

## Defensa final: una dependencia, una prueba y un límite

Esta es la consigna de comprensión de la p. 35, adaptada para practicar. Intenta responder con tu propio ejemplo antes de abrir la solución.

> [!question]- ¿Cómo defenderías el producto en tres frases?
> **Dependencia:** el ranking necesita el resumen, y el resumen necesita una población elegible completa.
>
> **Prueba:** expected_coverage exige exactamente una ejecución por combinación del diseño; si falla en el build del caso, los descendientes se omiten.
>
> **Límite:** reconstruir el mismo contenido prueba repetibilidad bajo estas entradas y reglas, no superioridad general ni ausencia de errores en todo el diseño.

## Plan corto de recuerdo

1. **Hoy:** cuenta la historia del pipeline sin mirar y resuelve el laboratorio a mano.
2. **Mañana:** abre solamente las preguntas; apunta cuáles no puedes explicar.
3. **En tres días:** dibuja el grafo, inventa una ausencia y localiza qué prueba la detecta.
4. **En una semana:** transfiere el contrato a otra métrica y defiende una dependencia, una prueba y un límite.

Para considerarlo entendido debes poder explicar **qué es, para qué sirve, cómo funciona, por qué se necesita y qué no demuestra** cada etapa.

Fuente: [[assets/module_11.pdf#page=34|PDF pp. 34–35]] y repaso del módulo. Volver a [[00 Índice - M11 Pipeline de datos para un producto analítico]].
