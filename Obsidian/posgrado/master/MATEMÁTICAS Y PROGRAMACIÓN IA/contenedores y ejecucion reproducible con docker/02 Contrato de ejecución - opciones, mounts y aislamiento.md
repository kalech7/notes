---
title: "Contrato de ejecución - opciones, mounts y aislamiento"
modulo: M09
tags:
  - master/matematicas-programacion
  - m09
---

# Contrato de ejecución - opciones, mounts y aislamiento

## La idea del contrato

Un contrato de ejecución declara **qué entra, qué puede hacer el proceso y dónde deja la salida**. «Que corra» no basta: también queremos predecir qué acción debería fallar.

![[assets/m09-08.png|1000]]

Lee el comando por su posición:

```text
docker run [opciones de Docker] IMAGEN [argumentos del programa]
```

Las opciones anteriores a la imagen controlan el contenedor. Con el `ENTRYPOINT` del módulo, los argumentos posteriores configuran `fashion-train`. No son opciones que Docker interprete como propias.

## Traducción de las opciones

| Fragmento | Significado | Qué permite comprobar |
|---|---|---|
| `--rm` | elimina el contenedor al terminar | los resultados necesarios deben externalizarse |
| `--pull=never` | no descarga una imagen implícitamente | debe existir la imagen local |
| `--network none` | desactiva red externa; queda loopback | no puede descargar el dataset durante el run |
| `--read-only` | raíz del contenedor en solo lectura | una escritura allí debe fallar |
| `--tmpfs /tmp:...` | temporales en memoria | trabajo temporal sin hacerlo persistente |
| mount de `/data` con `readonly` | datos de entrada sin escritura | el proceso no debe alterar el dataset |
| mount de `/config` con `readonly` | configuración sin escritura | el experimento no reescribe sus decisiones |
| mount de `/artifacts` escribible | salida persistente | métricas y pesos sobreviven al contenedor |

`--read-only` no prohíbe escribir en todo lugar: los mounts escribibles y `tmpfs` siguen teniendo su política propia.

## Un mount visto desde ambos lados

```text
Host: ./data       → Contenedor: /data       (solo lectura)
Host: ./config     → Contenedor: /config     (solo lectura)
Host: ./artifacts/run-01 → /artifacts         (escritura)
```

`src` es la ruta en el host; `dst` es la ruta visible dentro. El argumento `--data-root /data` pertenece al programa: le dice dónde leer el dataset ya montado.

## Predecir fallos ayuda a comprender

![[assets/m09-09.png|1000]]

Si falta el bind mount de datos, el programa puede iniciar y luego fallar al cargar archivos. Si intenta descargar con la red deshabilitada, falla la descarga. Si intenta guardar resultados en la raíz de solo lectura, falla la escritura. Estos son fallos diferentes: corregirlos requiere identificar qué condición del contrato se incumplió.

Las imágenes del módulo muestran un comando de referencia para un proyecto específico. Las rutas y el ejecutable necesitan existir; copiar el comando no crea el dataset, la imagen ni el programa.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- ¿Dónde va --network none?
> Antes del nombre de la imagen, porque configura Docker.

> [!question]- ¿Por qué /artifacts puede escribirse con --read-only?
> Porque es un mount con permiso de escritura. La raíz y los mounts tienen políticas diferentes.

> [!question]- ¿Qué ocurre si el programa descarga datos durante este run?
> La descarga externa falla. El dataset debe prepararse antes y la aplicación debe usarlo localmente, como en download=False.

## Fuente y ruta

Material base: [[assets/module_09.pdf#page=7|M09, páginas 7, 8, 9, 12, 19]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M09 Docker y ejecución reproducible]].
