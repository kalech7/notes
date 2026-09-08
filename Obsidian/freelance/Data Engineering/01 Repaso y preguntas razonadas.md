---
title: "Repaso: preguntas que debes poder explicar"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Repaso: preguntas que debes poder explicar

## Cómo usar este repaso

Oculta la columna derecha o responde antes de leerla. Una respuesta dominada incluye ejemplo, motivo y límite; reconocer una palabra no basta. Los números de la tabla siguiente corresponden a las 30 preguntas de comprensión de la ampliación del spec.

| N.º | Pregunta resumida | Respuesta razonada |
|---:|---|---|
| 1 | Separar Qatar vs. Ecuador | INSTR localiza « vs. »; SUBSTR extrae antes y después, tras validar el delimitador |
| 2 | Separar 3,2 | Localizar coma y extraer ambos lados |
| 3 | Por qué CAST | Los goles deben ser numéricos para calcular; primero validar texto |
| 4 | UPPER, TRIM, REPLACE | Homogeneizar representaciones según reglas; no resuelve toda identidad Unicode |
| 5 | Por qué UNION ALL | Conservar cada contribución de cada partido |
| 6 | Granularidad | Partido → participación → equipo/grupo |
| 7 | Puntuación con CASE | Victoria 3, empate 1, derrota 0; tratar marcador desconocido aparte |
| 8 | Dos mejores por grupo | ROW_NUMBER por grupo y filtro <=2 con desempate completo |
| 9 | Cambiar por RANK | Los empates pueden ampliar la salida si no los rompe otro criterio |
| 10 | PARTITION BY grupo | Reinicia la competencia lógica en cada grupo |
| 11 | Quintiles | NTILE(5) sobre el orden requerido |
| 12 | NTILE y PERCENT_RANK | Uno reparte filas; el otro expresa rango relativo |
| 13 | Join con LIKE | Depende de texto ambiguo; preferir claves extraídas y validadas |
| 14 | Schema explícito | StructType con campos/tipos; createDataFrame con datos compatibles |
| 15 | Convertir goles/partidos | Evitar orden y operaciones sobre representaciones textuales |
| 16 | Temporary view | Nombre consultable por SQL durante la sesión; no archivo ni tabla permanente |
| 17 | Mejor por país | Ventana con orden según métrica y política de empates |
| 18 | Tasa frente a total | Divide por exposición; requiere denominador positivo y valorar tamaño de muestra |
| 19 | Array de structs | collect_list de struct o NAMED_STRUCT; ordenar después si importa |
| 20 | Riesgo de collect | Todo el resultado acaba en memoria del Driver |
| 21 | JSON multiline | Cuando un documento JSON por archivo ocupa varias líneas físicas |
| 22 | Promedio X/Y | Filtrar puntos completos y finitos; groupBy más avg de ambas coordenadas |
| 23 | Distancia euclidiana | Longitud recta en un plano con unidades compatibles |
| 24 | Punto más cercano | Unir centroide al detalle, calcular distancia y rankear ascendente |
| 25 | Costo UDF | Ejecución Python y menor visibilidad de su interior para el optimizador |
| 26 | Parquet analítico | Organización columnar, tipos y lectura selectiva; rendimiento depende de carga |
| 27 | Directorios part | Escritura paralela por tareas y configuración de salida |
| 28 | NBSP | Carácter de espacio distinto de ASCII; reemplazarlo explícitamente si corresponde |
| 29 | Nombre exacto del archivo | Una diferencia de ruta o nombre impide cargar la fuente prevista |
| 30 | Validar limpieza | Comparar originales/limpios, incidencias, nulos, NBSP y correspondencia con catálogo |

## Ocho tarjetas de conceptos generales

> [!question]- ¿Un índice mejora siempre la consulta?
> No. Depende de selectividad, cobertura, plan y costo de mantenimiento. Un scan puede ser apropiado.

> [!question]- ¿Qué aportan las estadísticas?
> Información de distribución para estimar filas y costos. Las estimaciones pueden fallar incluso con estadísticas recientes.

> [!question]- ¿DevOps es Azure DevOps?
> No. DevOps reúne cultura y prácticas; Azure DevOps es una plataforma que puede apoyar parte del trabajo.

> [!question]- ¿Commit, tag y PR son lo mismo?
> No: instantánea histórica, marcador y propuesta de integración tienen funciones diferentes.

> [!question]- ¿Confirmación es regresión?
> La confirmación verifica un defecto corregido; la regresión busca efectos adversos en comportamiento existente.

> [!question]- ¿Validez equivale a exactitud?
> Un valor puede cumplir formato y dominio y aun así representar mal la realidad.

> [!question]- ¿Un stage aparece por cada línea del programa?
> No. La planificación y las dependencias, especialmente shuffle, determinan los límites.

> [!question]- ¿Spark siempre trabaja solo en RAM?
> No. Puede leer y escribir almacenamiento, usar disco para shuffle y derramar datos.

## Lista de dominio

- [ ] Explico la granularidad de entrada y salida de cada CTE.
- [ ] Predigo empates y buckets sin ejecutar.
- [ ] Distingo NOT IN, NOT EXISTS y LEFT JOIN con nulos.
- [ ] Identifico el dialecto antes de copiar una función SQL.
- [ ] Justifico cuándo un índice o una partición pueden ayudar.
- [ ] Dibujo rama, PR, CI e integración de un hotfix.
- [ ] Distingo nivel, objetivo, confirmación y regresión de pruebas.
- [ ] Defino reglas y métricas de calidad con sus denominadores.
- [ ] Explico Driver, Executor, acción, stage y shuffle.
- [ ] Leo un schema, valido tipos y comparo API con SQL.
- [ ] Calculo un centroide a mano y justifico los empates.
- [ ] Distingo arrays distribuidos de collect al Driver.
- [ ] Elijo formato de salida y explico los archivos part.
- [ ] Puedo contar qué cambió al pasar de diez a millones de filas.

No marques una casilla solo por haber leído: resuelve un ejemplo nuevo y explica una falla plausible.

## Conexiones

- [[Obsidian/freelance/Data Engineering/Laboratorios/01 Laboratorio SQL resuelto|01 Laboratorio SQL resuelto]] — comprueba tus predicciones con ejecución real.
- [[Obsidian/freelance/Data Engineering/Laboratorios/02 Laboratorio Spark guiado|02 Laboratorio Spark guiado]] — lleva los conceptos al mismo caso distribuido.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
