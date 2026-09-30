---
title: "76 S12 - Toolsets validación errores y límites efectivos"
created: 2026-09-29
fecha: 2026-09-29
capitulo: 12
sesion: "12"
tags:
  - maestria/ia-generativa
  - agentes
  - estudio
---

# 76 S12 - Toolsets validación errores y límites efectivos

[[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/69 S12 - Guía para entender patrones y toolsets|Guía de la sesión 12]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/00 Inicio/00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Un **toolset** es el conjunto de operaciones que el agente puede solicitar. Delimita sus capacidades prácticas: si no hay acceso al esquema de la base ni información equivalente en el contexto, el modelo puede tener que adivinar nombres. Dar más herramientas aumenta posibilidades, pero también decisiones y fallas posibles.

## 1. Nombre y descripción: elegir con información

Una herramienta debería decir qué devuelve y cuándo utilizarla. `consultar_ventas` devuelve filas; `estadisticas_ventas` devuelve agregados. Describir ambas como «sirve para ventas» deja ambigua la elección. También conviene indicar el significado de cada campo y errores posibles.

La frase del lunes «la descripción es el prompt» enfatiza que esa descripción influye en la selección. No significa que sea el único factor ni que controle permisos. El objetivo, otras herramientas, ejemplos y resultados también influyen.

## 2. El contrato tiene que llegar hasta la ejecución

![[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Recursos visuales/56-s12-contrato-completo.png|56-s12-contrato-completo.png]]

Las cajas recorren descubrimiento, validación, ejecución y retorno. Las flechas representan cambios de responsabilidad del programa. Un esquema informa qué entradas son esperables; la validación rechaza una propuesta que no cumple. El límite efectivo se aplica al ejecutar, y el resultado vuelve con procedencia y estado.

Un esquema de entrada define propiedades, campos requeridos y dominios. La documentación oficial de [objetos en JSON Schema](https://json-schema.org/understanding-json-schema/reference/object) confirma que declarar `properties` no exige por sí solo que estén presentes y que los campos extra requieren una política explícita. `required` y `additionalProperties` resuelven aspectos distintos.

Para el ejemplo, podría exigirse un mes `YYYY-MM`, una región enumerada y ausencia de campos adicionales. Un patrón puede comprobar forma básica y mes 01–12. Además hace falta validar si el período existe en los datos: formato válido y datos disponibles son dos comprobaciones distintas.

La firma de Python rechaza ciertos argumentos con `TypeError`; eso no reemplaza validar dominios antes de ejecutar. Las anotaciones de tipo tampoco comprueban automáticamente valores en cada llamada.

## 3. Errores que permiten recuperarse

Un resultado útil podría ser:

```json
{
  "ok": false,
  "error": {
    "codigo": "MES_SIN_DATOS",
    "mensaje": "No hay filas para 2025-03",
    "meses_disponibles": ["2026-03", "2026-04"],
    "reintentable": false
  }
}
```

El código identifica la clase de fallo y los meses permiten corregir una suposición. `reintentable: false` significa que repetir sin cambiar la condición no ayudará, no que sea imposible resolver la tarea de otra forma. La información disponible debe respetar los permisos del usuario.

No todos los errores deben tratarse igual. Un error de entrada puede corregirse; una falla transitoria puede admitir reintentos acotados; una violación de permisos debe rechazarse; un fallo inesperado puede requerir detener la corrida. El programa puede usar excepciones internamente y convertirlas en resultados apropiados en el límite de la herramienta. «El error se devuelve» no prohíbe toda excepción en cualquier parte del código.

## 4. Los seis huecos del Lab 03 según la presentación

| Defecto descrito en PDF 21–22 | Consecuencia | Diseño que lo atiende |
| --- | --- | --- |
| `tool(**args)` sin validación ni captura | Un argumento mal escrito rompe la corrida | Validar y clasificar errores en el harness |
| Consulta SQL sin manejo de fallas | Tabla inexistente o sintaxis incorrecta interrumpe | Resultado de error útil y límites de consulta |
| No se describe el esquema de datos | El modelo adivina tablas y columnas | Contexto de esquema o herramienta que lo describa |
| `row_limit` controlado por el modelo | Puede solicitar un resultado excesivo | Máximo interno no superable |
| `output_path` público | Puede intentar escribir fuera del destino previsto | Destino autorizado resuelto por el programa |
| Se descarta `usage` | Falta consumo real acumulado para presupuesto de tokens | Registrar uso y aplicar reservas y topes |

Estas son **afirmaciones de las diapositivas**, no un diagnóstico ejecutado sobre una copia del Lab 03. Solo se recibieron los dos notebooks y el PDF. Además, la diapositiva 21 cita un archivo fuente del lunes con un bucle resuelto; el notebook de estudiante recibido deja esa implementación vacía. No es evidencia de que el `try/except` ya esté en tu notebook.

Hay además una inconsistencia dentro del propio PDF: en la tabla visual de la página 24, la fila «validar antes de actuar; el error se devuelve como valor» marca **sí** para Lab 03. Las páginas 21–22 muestran `tool(**args)` sin esquema ni captura y explican que la excepción mata el proceso. No se deben combinar esas dos afirmaciones como si fueran compatibles; aquí se conserva el diagnóstico detallado del código mostrado y se señala el conflicto de la síntesis. El notebook de estudiante tampoco contiene el bucle resuelto que cita la presentación.

## 5. El caso de `ventas` frente a `sales`

Si el modelo propone `SELECT * FROM ventas` y solo existe `sales`, la consulta falla. Con el flujo sin captura descrito en el PDF, el modelo no recibe una observación corregible y el proceso puede morir antes de guardar la traza. Que el modelo haya emitido un nombre no demuestra que ese nombre provenga del esquema.

Una operación como `describir_esquema()` podría devolver tablas, columnas, tipos y relaciones. Pero no es obligatoria en toda arquitectura: también se puede proporcionar un esquema estático autorizado en el contexto. Lo que hace falta es información verificable de los datos y una forma de corregir la consulta.

Dar un esquema reduce adivinación; no autoriza cualquier consulta sobre él. Leer datos sigue necesitando permisos, máximo de filas y tiempo de ejecución.

## 6. Los límites públicos y los internos

La diapositiva afirma que un límite que viaja en el esquema público «no es un límite». La precisión es: **no es suficiente si el sistema permite que el modelo lo aumente arbitrariamente**. Se puede ofrecer un límite solicitado y aplicar siempre un máximo interno:

$$L_{\text{efectivo}}=\min(L_{\text{solicitado}},L_{\text{máximo interno}})$$

Antes se validan signo y tipo. Por ejemplo, el usuario puede pedir 20 filas y el sistema admitir como máximo 100. Pedir 100 000 no debe elevar el tope. También se puede omitir ese parámetro público, como recomienda el diseño del curso.

En SQL, comprobar solo que una cadena empieza por `SELECT` no garantiza acceso autorizado ni costo limitado. Los permisos de base, los controles de consulta y el timeout deben imponer la política efectiva. No se ejecutó SQL ni se conectó a ninguna base en esta ampliación.

## 7. Efectos, idempotencia y trazas

Una herramienta que lee ventas y genera una imagen **escribe un archivo**, aunque no modifique la base. El contrato debería declarar ese efecto y resolver el destino permitido. «Solo lectura» debe indicar a qué recurso se refiere.

**Idempotencia** significa que repetir la misma operación no añade un efecto diferente después de la primera ejecución, según el contrato. Establecer un estado puede ser idempotente; incrementar un contador normalmente no. Una clave de operación ayuda a reconocer reintentos, pero requiere almacenamiento y lógica del servicio para evitar duplicados.

La traza útil incluye identificador, nombre, argumentos apropiados, resultado o error, latencia en milisegundos y motivo de parada. La persistencia debe contemplar caminos de error. Un `finally` o un manejador central puede mejorar la cobertura; la persistencia incremental reduce pérdidas ante una caída abrupta. Un proceso terminado a la fuerza puede impedir ejecutar un cierre normal.

> [!question]- ¿Agregar `describir_esquema` arregla todos los defectos del toolset?
> No. Informa nombres y relaciones; no impone permisos, valida todas las consultas, limita consumo ni preserva la traza de cualquier error. Cada responsabilidad necesita su control.

Fuentes: [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/Materiales/sesion-12.pdf#page=21|PDF 21–24]], notebook del lunes celdas 2–5, referencia oficial enlazada. Los errores estructurados y controles detallados son ejemplos propios de diseño.

---

← [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/75 S12 - Plan-and-Execute y elección de patrones|Anterior]] · [[Obsidian/posgrado/master/IA GENERATIVA Y AGENTES/12 Patrones de agentes y diseño del toolset/77 S12 - Laboratorio local y soluciones del martes|Siguiente]] →

