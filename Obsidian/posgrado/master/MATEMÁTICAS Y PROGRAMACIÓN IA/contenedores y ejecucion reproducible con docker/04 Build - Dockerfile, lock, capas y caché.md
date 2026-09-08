---
title: "Build - Dockerfile, lock, capas y caché"
modulo: M09
tags:
  - master/matematicas-programacion
  - m09
---

# Build - Dockerfile, lock, capas y caché

## Build y run responden preguntas distintas

**Build** construye la imagen. **Run** crea una ejecución desde ella. El contexto del build es el conjunto de archivos que Docker puede usar para construir; no debe confundirse con los datos montados después al ejecutar.

![[assets/m09-13.png|1000]]

### Qué entra en el contexto

Código, `pyproject.toml`, `uv.lock` y `Dockerfile` describen el software. `.dockerignore` excluye datos, artefactos y estado local innecesario, como `.venv` o cachés. Un archivo excluido no puede copiarse desde ese contexto durante el build.

El **lock** conserva una resolución de dependencias. Declarar solamente nombres de paquetes no determina todas sus versiones transitivas. Aun con lock hay que verificar compatibilidad con la plataforma objetivo.

## Capas: ordenar para reconstruir lo necesario

![[assets/m09-15.png|1000]]

Lee el Dockerfile del dibujo en cuatro bloques:

1. **Runtime:** imagen base y herramientas de instalación.
2. **Dependencias:** se copian metadatos y lock; se instalan las dependencias.
3. **Código:** se copia el paquete del proyecto.
4. **Proceso:** `ENTRYPOINT` establece el ejecutable principal.

Si copias primero el lock y después el código, cambiar un archivo del programa normalmente permite reutilizar la capa de dependencias. Si cambia el lock, esa instalación debe reevaluarse y las capas posteriores también pueden invalidarse.

`uv sync --frozen` usa el lock sin actualizarlo. Esto no demuestra que un lock creado para otro entorno sea suficiente: la compatibilidad debe comprobarse. Los digests/versiones «por verificar» en la diapositiva son placeholders del ejercicio; no son valores listos para producción.

## Caché no equivale a reproducibilidad

![[assets/m09-16.png|1000]]

La caché pregunta: «¿puedo reutilizar esta etapa?». La reproducibilidad pregunta: «¿qué software, entradas y comando se ejecutaron?». Un build rápido no responde la segunda.

| Cambio | Consecuencia esperada del diseño del módulo |
|---|---|
| solo código | reutilizar dependencias y reconstruir código |
| `uv.lock` | reinstalar dependencias afectadas y reconstruir lo posterior |
| datos fuera del contexto | no cambia el build, pero sí puede cambiar el experimento |
| `.dockerignore` | puede cambiar qué archivos recibe el build |

## Identificar lo construido

La etiqueta `fashion-train:local` es cómoda para invocar. El registro necesita ID de imagen y OS/arquitectura observados. El ejemplo propone Linux CPU; no certifica que una combinación concreta de versiones esté validada en tu máquina.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- ¿Cambiar datos siempre invalida la caché?
> No, si están fuera del contexto y entran mediante mounts. Aun así cambia la entrada del experimento y debe registrarse.

> [!question]- ¿Por qué copiar el lock antes que el código?
> Para que cambios de código no invaliden innecesariamente la instalación de dependencias.

> [!question]- ¿Una etiqueta local identifica inmutablemente una imagen?
> No. Puede reasignarse; registra el ID y la plataforma efectivamente usados.

## Fuente y ruta

Material base: [[assets/module_09.pdf#page=13|M09, páginas 13, 14, 15, 16, 17]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M09 Docker y ejecución reproducible]].
