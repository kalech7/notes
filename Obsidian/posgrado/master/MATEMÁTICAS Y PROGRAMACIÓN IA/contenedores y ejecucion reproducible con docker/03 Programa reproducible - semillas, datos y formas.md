---
title: "Programa reproducible - semillas, datos y formas"
modulo: M09
tags:
  - master/matematicas-programacion
  - m09
---

# Programa reproducible - semillas, datos y formas

## Docker necesita un programa que también declare sus decisiones

La imagen puede fijar una versión de PyTorch, pero el programa aún decide la semilla, el dispositivo, el orden de los ejemplos y la partición de datos. Son responsabilidades diferentes.

![[assets/m09-11.png|1000]]

### Lee cada fila como causa y límite

- Una semilla reduce variación del generador aleatorio correspondiente; no fija todas las operaciones de todos los dispositivos.
- Un generador del cargador de datos controla el barajado de los ejemplos.
- `num_workers=0` simplifica el caso didáctico al cargar datos sin procesos trabajadores adicionales.
- `download=False` exige datos locales y evita una descarga sorpresa; no comprueba por sí solo que sean la versión correcta.

**Semilla** es el valor inicial de un generador pseudoaleatorio. Con el mismo generador y condiciones, permite repetir su secuencia. Si cambias biblioteca, dispositivo u operaciones, no debes concluir identidad numérica solo porque el entero de la semilla coincide.

## La arquitectura se inspecciona para entender las formas

![[assets/m09-10.png|1000]]

Una imagen de Fashion-MNIST tiene un canal y tamaño $28\times28$. Un lote de $B$ imágenes tiene forma $(B,1,28,28)$.

1. Aplanar desde la dimensión 1 transforma cada imagen en $784$ números: $(B,784)$.
2. La primera capa afín lleva $784$ características a $128$: $(B,128)$.
3. ReLU cambia valores, pero conserva esa forma.
4. La última capa produce diez logits: $(B,10)$.
5. Las etiquetas contienen una clase por ejemplo: $(B,)$.

Un **logit** es un puntaje de clase previo a la normalización. Para la pérdida multiclase del caso, la etiqueta es un índice de clase; no una matriz de diez etiquetas por imagen.

El módulo pide comprobar este recorrido, no rediseñar la red. Cambiar la arquitectura mientras comparas hosts introduce otra causa de variación.

## Datos, partición y configuración son objetos distintos

El dataset contiene observaciones. El manifiesto de partición declara qué índices van a train/validation/test. La configuración contiene decisiones como épocas o tasa. Registrar solo el nombre «Fashion-MNIST» no distingue distintas particiones o preparaciones de datos.

Un hash es una huella calculada sobre bytes. Registrar hashes de entradas ayuda a comprobar identidad de archivos; la huella no explica por sí misma qué significan las columnas ni si el diseño experimental es correcto.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- Con B=32, ¿qué forma sale de la última capa?
> (32,10): diez logits por cada una de las 32 imágenes. Las etiquetas tienen forma (32,).

> [!question]- ¿download=False verifica la identidad del dataset?
> No. Evita la descarga automática; hay que registrar y comparar los archivos o su huella.

> [!question]- ¿Una semilla idéntica garantiza el mismo resultado en CPU y GPU?
> No. Puede cambiar la aritmética o la implementación de operaciones. Se registra el dispositivo y se comprueban resultados con un criterio declarado.

## Fuente y ruta

Material base: [[assets/module_09.pdf#page=10|M09, páginas 10, 11, 12]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M09 Docker y ejecución reproducible]].
