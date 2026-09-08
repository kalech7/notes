---
title: "Imagen, contenedor, host y persistencia"
modulo: M09
tags:
  - master/matematicas-programacion
  - m09
---

# Imagen, contenedor, host y persistencia

## Primero imagínalo así

Una **imagen** se parece a una caja preparada con Python, bibliotecas y código. Un **contenedor** es una ejecución creada desde esa caja. El **host** aporta la máquina donde ocurre la ejecución. Puedes crear dos contenedores de la misma imagen: comparten la base, pero tienen procesos y estados de ejecución distintos.

![[assets/m09-04.png|1000]]

### Cómo leer la imagen

1. El rectángulo grande es el host: CPU, kernel y recursos siguen importando.
2. La imagen agrupa código, dependencias y runtime.
3. El proceso `fashion-train` vive en el contenedor.
4. `/data` y `/config` reciben entradas; `/artifacts` permite sacar resultados.

En Docker con contenedores Linux sobre macOS, el kernel Linux normalmente está en una máquina virtual administrada por Docker. Empaquetar Python no reemplaza toda la máquina por una idéntica.

## Qué persiste y por qué

![[assets/m09-05.png|1000]]

| Lugar | Ejemplo | Al eliminar el contenedor |
|---|---|---|
| Imagen | código y dependencias | la imagen permanece si no se elimina por separado |
| Capa escribible del contenedor | archivo creado dentro de su raíz | desaparece con el contenedor |
| `tmpfs` | temporales en `/tmp` | no es almacenamiento persistente |
| Bind mount | archivo en `/artifacts` respaldado en el host | permanece en la carpeta del host |

Un bind mount hace visible una carpeta del host dentro del contenedor. No es una copia automática: una escritura permitida allí modifica los archivos respaldados en el host.

Ejemplo: si `/Users/ana/resultados` se monta en `/artifacts`, guardar `/artifacts/metrics.json` deja el archivo en `/Users/ana/resultados/metrics.json`. Eliminar el contenedor no borra por sí mismo esa carpeta.

## «Funciona aquí» no explica las condiciones

Dos personas pueden tener el mismo código y resultados distintos por versiones de bibliotecas, datos, particiones o CPU/GPU. La imagen reduce variación de software; los mounts declaran datos/configuración; el programa fija semillas y orden; el registro documenta el host.

Una **etiqueta** como `fashion-train:local` es un nombre que puede apuntar después a otra imagen. Para identificar lo ejecutado se registra también el ID de la imagen y su plataforma. Un digest identifica contenido direccionado en un registro; conviene no usar indistintamente etiqueta, ID local y digest.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- Si elimino el contenedor, ¿pierdo metrics.json?
> Depende de dónde se guardó. En un bind mount hacia el host permanece; en la capa escribible del contenedor eliminado se pierde.

> [!question]- ¿Dos contenedores de la misma imagen son el mismo proceso?
> No. Cada contenedor puede ejecutar una instancia distinta y recibir otros datos, argumentos y mounts.

> [!question]- ¿Qué significa que Docker reduzca variación?
> Que fija parte del software. No demuestra que datos, hardware, semillas y aritmética coincidan.

## Fuente y ruta

Material base: [[assets/module_09.pdf#page=1|M09, páginas 1, 2, 3, 4, 5, 6]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M09 Docker y ejecución reproducible]].
