---
title: "Parquet y Delta Lake: archivo frente a tabla"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Parquet y Delta Lake: archivo frente a tabla

## Dos niveles distintos

Parquet es un formato de archivos. Delta Lake es una capa de tabla que combina archivos de datos Parquet con un registro de transacciones y reglas para gestionar cambios. La distinción importa cuando varios procesos escriben, hay actualizaciones o necesitas saber qué conjunto de archivos forma una versión consistente de la tabla.

```mermaid
flowchart TD
 A["Lector de tabla Delta"] --> B["Registro de transacciones"]
 B --> C["Archivos válidos de la versión"]
 C --> D["Datos en Parquet"]
```

Si abres indiscriminadamente todos los archivos Parquet de una carpeta Delta, puedes incluir archivos que ya no pertenecen a la versión vigente. El lector de tabla usa el registro para resolver qué datos forman el estado solicitado.

| Necesidad | Parquet por sí solo | Tabla Delta |
|---|---|---|
| Datos columnares tipados | Sí | Usa Parquet como parte del almacenamiento |
| Historial transaccional de la tabla | No lo define por sí solo | Registro de cambios |
| Actualizaciones y borrados de tabla | Necesitan coordinación adicional | Operaciones gestionadas por la capa de tabla |
| Lectura de una versión anterior | Necesita diseño externo | Posible si se conserva historial y archivos necesarios |

La validación de esquema no prueba toda la calidad del negocio. Transacciones tampoco garantizan que la fórmula de puntos esté bien. Los beneficios requieren lectores/escritores compatibles y decisiones operativas sobre concurrencia y retención.

## Cuándo estudiar esta ampliación

Si la pregunta compara únicamente Parquet, JSON y CSV, responde dentro de esas opciones. Delta amplía el razonamiento cuando necesitas semántica de tabla, no reemplaza a Parquet como si fuera simplemente otra extensión de archivo equivalente.

Una exportación analítica inmutable puede funcionar bien con Parquet. Una tabla actualizada repetidamente, con lectores concurrentes y requisitos de consistencia, puede beneficiarse de una capa transaccional. También hay otros formatos abiertos de tabla; la decisión final requiere comparar capacidades y compatibilidad del entorno.

## Ejercicio

Imagina que una corrección reemplaza un archivo con ventas erróneas. Un lector empieza antes de terminar la sustitución: ¿cómo sabe qué archivos forman una versión completa? Describe qué información debe registrar una capa de tabla. Después explica por qué conservar versiones anteriores depende de no eliminar los archivos que esas versiones necesitan.

Referencia de ampliación: [documentación de Delta Lake](https://docs.delta.io/). Los ejemplos prácticos del conjunto usan Parquet/JSON/CSV y no presuponen que Delta esté instalado.

> [!tip] Regla para recordar
> Parquet organiza un archivo; Delta administra el estado de una tabla.

## Comprueba que lo entendiste

> [!question]- ¿Leer todos los .parquet de una tabla Delta equivale siempre a leer su estado actual?
> No. El registro de transacciones determina qué archivos pertenecen a la versión; leerlos sin esa información puede producir un conjunto incorrecto.

## Conexiones

- [[Obsidian/freelance/Data Engineering/Spark/08 Formatos particiones y salida|08 Formatos particiones y salida]] — describe los archivos que sirven de soporte.
- [[Obsidian/freelance/Data Engineering/DevOps/01 DevOps DataOps y CALMS|01 DevOps DataOps y CALMS]] — conecta versionado y operación de datos.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
