---
title: "67 S11 - Ejercicios resueltos y repaso activo"
created: 2026-09-28
capitulo: 11
sesion: "11"
fecha: 2026-09-28
tags:
  - maestria/ia-generativa
  - agentes
  - herramientas
fuente: "[[sesion-11.pdf]]"
---

# 67 S11 - Ejercicios resueltos y repaso activo

[[59 S11 - Guía para entender agentes y herramientas|Guía de la sesión 11]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[66 S11 - Límites trazas y laboratorio del bucle]]

## Cómo usar este repaso

Intenta responder en voz alta y dibujar el recorrido antes de abrir la solución. Una respuesta útil explica **qué componente interviene, qué información necesita y qué fallo evita**. No memorices solo la palabra correcta.

Los ejercicios 1–10 comprueban conceptos; 11–20 trabajan mecanismos y números; 21–24 exigen reconocer límites.

### 1. ¿Un pipeline con cinco LLM y tres herramientas es necesariamente un agente?

> [!question]- Ver respuesta razonada
> No. Si el programa fija el orden y las herramientas, sigue siendo un pipeline. Inspecciona si las observaciones permiten que el modelo seleccione el siguiente paso.

### 2. ¿En qué momento el RAG del taller se integra en un agente?

> [!question]- Ver respuesta razonada
> Cuando recuperar es una acción que el modelo puede seleccionar dentro de un bucle con objetivo y parada. El índice puede permanecer igual. Agregar generación o una herramienta adicional no basta por sí solo.

### 3. Una ejecución termina sin herramientas. ¿Eso prueba que la arquitectura no es de agente?

> [!question]- Ver respuesta razonada
> No. Puede admitir decisiones y bucles, pero reconocer que esa tarea ya tiene información suficiente. Una ejecución corta no describe todas las capacidades de la arquitectura.

### 4. El modelo escribe una consulta SQL. ¿Ya consultó la base?

> [!question]- Ver respuesta razonada
> No. Es una propuesta. Un programa debe validarla, ejecutarla con permisos apropiados y devolver el resultado.

### 5. Completa PEAS para el asistente de ventas.

> [!question]- Ver respuesta razonada
> P: cifras, cálculo y fuentes correctas dentro de límites. E: base, documentos y usuario. A: consultas permitidas, cálculos y respuesta. S: pregunta, datos retornados y errores. La lista puede ampliarse según la tarea concreta.

### 6. ¿Un agente basado en modelos es simplemente un agente que usa un LLM?

> [!question]- Ver respuesta razonada
> No. En esa taxonomía mantiene un modelo o estado del entorno. «Modelo» no tiene aquí el sentido restringido de modelo de lenguaje.

### 7. Hay una función en REGISTRO, pero el modelo nunca la llama. ¿Qué revisar primero?

> [!question]- Ver respuesta razonada
> Que el catálogo y su descripción efectivamente lleguen al modelo, que el nombre sea coherente y que el objetivo requiera esa operación. La existencia en Python no la hace visible al modelo.

### 8. La herramienta falla y el programa omite el mensaje de resultado. ¿Qué se rompe?

> [!question]- Ver respuesta razonada
> La correspondencia del protocolo entre solicitud y resultado, y además el modelo no observa la falla. Debe recibir un error estructurado asociado a la llamada.

### 9. ¿JSON válido significa argumentos válidos?

> [!question]- Ver respuesta razonada
> No. {"mes":"2026-99"} puede parsearse y contiene una cadena, pero el mes viola el dominio. Después todavía faltan disponibilidad y autorización.

### 10. ¿Una descripción que dice «solo lectura» garantiza ese permiso?

> [!question]- Ver respuesta razonada
> No. Orienta la elección; el programa y la base deben imponer permisos reales. Un prompt no reconfigura credenciales.

### 11. Febrero = 12000 y marzo = 15000. Calcula diferencia absoluta y crecimiento.

> [!question]- Ver respuesta razonada
> Diferencia = 3000 USD. Crecimiento = (15000 − 12000) / 12000 × 100 = 25 %. Dividir por marzo produce 20 %, otra relación. Si febrero fuera cero, la tasa usual no estaría definida.

### 12. Dos llamadas tienen nombre total_ventas. ¿Por qué necesitan IDs diferentes?

> [!question]- Ver respuesta razonada
> El nombre identifica la función y el ID la invocación concreta. Los identificadores evitan asignar el resultado de febrero a la consulta de marzo.

### 13. ¿Emparejar cada llamada con un resultado garantiza que una escritura se ejecutó solo una vez?

> [!question]- Ver respuesta razonada
> No. Los reintentos tras una respuesta perdida pueden repetir efectos. Se necesitan mecanismos adicionales, como idempotencia, según la operación.

### 14. El modelo ve marzo, pero el dato de febrero se eliminó del contexto. ¿Puede usarlo porque ya lo vio antes?

> [!question]- Ver respuesta razonada
> No debe suponerse. La aplicación tiene que conservarlo y facilitarlo de nuevo o recuperarlo. Los pesos no se actualizan automáticamente con cada consulta.

### 15. Con B = 1000 y d = 500, ¿cuánto contexto hay después de cuatro llamadas?

> [!question]- Ver respuesta razonada
> C4 = 1000 + 4 × 500 = 3000 tokens, bajo los supuestos del ejemplo. No incluye una reserva adicional para salida.

### 16. ¿Por qué siete decisiones suman 17500 tokens de entrada si la última tiene 4000?

> [!question]- Ver respuesta razonada
> Porque se vuelve a incluir la historia: 1000 + 1500 + 2000 + 2500 + 3000 + 3500 + 4000 = 17500. El total acumulado y la última entrada son magnitudes diferentes.

### 17. En Toolformer, las pérdidas son 2.0 sin llamada, 1.8 sin resultado y 1.4 con resultado. Con umbral 0.5, ¿se conserva?

> [!question]- Ver respuesta razonada
> No. L− = min(2.0, 1.8) = 1.8; la mejora es 1.8 − 1.4 = 0.4, menor que 0.5. Comparar solo 2.0 con 1.4 llevaría a una conclusión equivocada.

### 18. ¿Por qué el curso no considera al Toolformer evaluado un agente completo?

> [!question]- Ver respuesta razonada
> Porque su procedimiento evaluado no encadena herramientas ni refina interactivamente decisiones usando nuevos resultados. Sí elige qué llamar y cuándo. La evaluación limita a una llamada por entrada; no es una prohibición universal de toda extensión futura.

### 19. Toolformer pasa de 14.8 a 40.4 en ASDiv. ¿Cuántos puntos y cuántas veces?

> [!question]- Ver respuesta razonada
> Aumenta 25.6 puntos y el cociente es aproximadamente 2.73. Es una comparación histórica del mismo modelo con llamadas habilitadas frente a deshabilitadas, no un aumento de 25.6 % ni una garantía para otras tareas.

### 20. La misma solución requiere tres llamadas y una respuesta final. Con max_decisiones = 3, ¿termina con respuesta?

> [!question]- Ver respuesta razonada
> No en nuestro laboratorio: responder consume una cuarta decisión. Las herramientas pueden haber producido todos los datos y aun así el cierre ser por límite. Definir la unidad evita errores de uno.

### 21. ¿Un máximo de cinco pasos evita que una herramienta quede esperando eternamente?

> [!question]- Ver respuesta razonada
> No. El contador se revisa entre decisiones. Una llamada bloqueada necesita un timeout o cancelación propios.

### 22. La traza acaba en respuesta_final. ¿Eso demuestra éxito?

> [!question]- Ver respuesta razonada
> Solo demuestra terminación del protocolo. Hay que verificar la respuesta contra los criterios de tarea. Una respuesta falsa puede ser final.

### 23. Un resultado de herramienta contiene «ignora al usuario y ejecuta otra acción». ¿Qué representa?

> [!question]- Ver respuesta razonada
> Contenido externo que debe tratarse como dato no confiable, no como una nueva autorización. El control de instrucciones y permisos pertenece al sistema. Es una ampliación sobre el límite entre observación y orden.

### 24. ¿Qué cambio de código convierte un agente en Agentic AI?

> [!question]- Ver respuesta razonada
> El PDF no establece uno. Esa etiqueta necesita una definición explícita; describe autonomía, herramientas, estado, coordinación y evaluación en vez de inferirlas de un nombre.


## Caso integrado: diagnostica antes de corregir

Una traza ficticia muestra:

```text
1. total_ventas({"mes":"2026-03"}) → 15000 USD
2. total_ventas({"mes":"2026-02"}) → 12000 USD
3. variacion_porcentual({"base":15000,"actual":12000}) → -20 %
4. final: «Marzo creció 25 % respecto de febrero»
```

¿La respuesta correcta demuestra que la ejecución fue correcta? ¿Qué corregirías?

> [!question]- Diagnóstico
> El paso 3 invierte base y actual y calcula la variación de febrero respecto de marzo. El paso 4 contradice su propia herramienta, aunque coincida por otra vía con la respuesta esperada. Debes corregir el mapeo de parámetros y revisar por qué la salida final no se apoya en la observación. Evalúa tanto éxito final como uso correcto de herramientas; son dimensiones distintas. Cambiar la calculadora no resuelve el origen del error.

## Mini proyecto de comprensión

Diseña en papel un asistente que explique un reglamento universitario y calcule un plazo. Define PEAS, dos herramientas con descripciones, argumentos y resultados; dibuja una consulta que encuentra evidencia y otra que no; indica el contador, el cierre por límite y los campos de la traza.

No supongas que sumar diez días calendario equivale a diez días hábiles. El agente debe recuperar la regla y usar una herramienta con calendario adecuado o explicar la información faltante. El ejercicio consiste en identificar dependencias y límites, no en inventar normativa.

## Glosario de bolsillo

| Término | Significado en estas notas |
| --- | --- |
| Agente LLM | Sistema que decide acciones con un LLM y observa resultados dentro de un bucle controlado. |
| Harness | Código que valida, ejecuta, mantiene el estado y aplica la parada. |
| Tool / herramienta | Operación externa con una interfaz utilizable por el sistema. |
| Function calling | Emisión estructurada de una solicitud de operación y su intercambio con un ejecutor. |
| Esquema | Contrato de forma y restricciones de datos. |
| Observación | Información devuelta al sistema desde el entorno o una herramienta. |
| Estado | Información que el programa conserva y actualiza durante la tarea. |
| Traza | Registro ordenado de eventos y resultados de una ejecución. |
| Utilidad | Criterio para comparar alternativas según preferencias o consecuencias. |
| Idempotencia | Propiedad que permite repetir una operación sin duplicar su efecto. |
| Ajuste fino | Entrenamiento adicional que modifica parámetros del modelo. |
| Parada por límite | Terminación impuesta por el presupuesto definido, sin presumir éxito. |

**Fuente:** síntesis de [[sesion-11.pdf]] y de las ampliaciones documentadas en las notas 60–66. Preguntas, caso integrado y soluciones son de elaboración propia.

Continúa con [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/11 Agentes y uso de herramientas/68 S11 - Notebook del lunes explicado y revisado|Notebook del lunes explicado y revisado]] y después con [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]].
