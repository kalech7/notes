---
title: "Laboratorio guiado y autoevaluación - M09"
modulo: M09
tags:
  - master/matematicas-programacion
  - m09
---

# Laboratorio guiado y autoevaluación - M09

## Caso para resolver sin instalar nada

Ana y Luis usan la etiqueta `fashion-train:local`. Ana obtiene accuracy $0.86$ y Luis $0.83$. Ambos anotaron la semilla 42. Luis concluye que Docker no funciona.

Antes de leer respuestas, escribe qué evidencia pedirías. Los números son ficticios y sirven para practicar diagnóstico.

![[assets/m09-23.png|1000]]

La imagen propone terminar con tres piezas: mecanismo, evidencia y límite. «Fijé el software» necesita explicar mediante qué imagen y cómo se identificó. «No garantizo igualdad numérica» necesita indicar qué plataforma y comparación sí se registraron.

## Hoja de trabajo

| Paso | Acción de estudio | Evidencia que buscarías |
|---|---|---|
| 1 | distinguir etiqueta e identidad | ID y plataforma de imagen |
| 2 | comparar entradas | hashes de dataset, split y configuración |
| 3 | revisar programa | seed, dispositivo, versiones, orden de datos |
| 4 | revisar contrato | comando, mounts, red y salida |
| 5 | evaluar resultado | exit code, artefactos y tolerancia acordada |

## Ejercicio de persistencia

Imagina que el programa guarda un archivo en `/tmp/a.txt` y otro en `/artifacts/metrics.json`, con el contrato de la nota 02. Después termina el contenedor con `--rm`. Predice cuál puedes leer en el host.

## Ejercicio de formas

Un lote tiene forma $(16,1,28,28)$. Recorre Flatten, Linear(784,128), ReLU y Linear(128,10). Explica qué representa cada eje, no solo su número.

## Ejercicio de construcción

Cambias únicamente el código de entrenamiento. El dataset está fuera del contexto. Explica qué capa quieres reutilizar y por qué reutilizarla no acredita que dos entrenamientos usaron las mismas entradas.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- ¿La diferencia 0.86 frente a 0.83 demuestra un fallo de Docker?
> No. La etiqueta podría señalar imágenes distintas y la semilla no fija datos, split, configuración ni aritmética. Primero se comparan registros.

> [!question]- ¿Qué archivo persiste en el ejercicio?
> metrics.json, si /artifacts está montado en la carpeta del host. /tmp en tmpfs es temporal.

> [!question]- ¿Cuáles son las formas de la red?
> (16,1,28,28) → (16,784) → (16,128) → (16,128) → (16,10). El primer eje conserva los 16 ejemplos.

> [!question]- ¿Qué capa se reutiliza al cambiar solo código?
> En el orden propuesto, la de dependencias si sus entradas no cambiaron. Los datos montados no están fijados por esa caché.

> [!question]- ¿Qué tres elementos debe tener tu conclusión?
> Mecanismo que fijó una condición, evidencia observada para comprobarla y límite de lo que no se verificó.

> [!question]- ¿Debo construir la imagen para estudiar estas notas?
> No. Este laboratorio es conceptual. Ejecutar el proyecto original requiere su código, lock compatible, datos locales e imagen verificada; los PDF no incluyen una certificación de esos elementos.

## Fuente y ruta

Material base: [[assets/module_09.pdf#page=1|M09, páginas 1, 23]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M09 Docker y ejecución reproducible]].
