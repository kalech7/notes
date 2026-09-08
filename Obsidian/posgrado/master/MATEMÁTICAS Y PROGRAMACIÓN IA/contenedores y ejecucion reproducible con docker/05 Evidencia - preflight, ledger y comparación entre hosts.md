---
title: "Evidencia - preflight, ledger y comparación entre hosts"
modulo: M09
tags:
  - master/matematicas-programacion
  - m09
---

# Evidencia - preflight, ledger y comparación entre hosts

## Evidencia significa una observación registrada

Es distinto escribir «usaremos la misma imagen» y registrar el ID de la imagen utilizada. El módulo convierte promesas en comprobaciones.

![[assets/m09-18.png|1000]]

### Preflight: antes del run

Comprueba imagen local, dataset, manifiesto de partición, configuración y carpeta de salida. Si una entrada falta, aún no hay una ejecución lista bajo el contrato. No se completa un campo «por observar» con una suposición.

La preparación de datos puede usar red antes del entrenamiento. El run de entrenamiento del módulo es offline. Son fases distintas.

## Dos registros complementarios

![[assets/m09-20.png|1000]]

Un **ledger** es un registro estructurado del experimento, comparable a una ficha de laboratorio.

| Quién observa | Qué puede registrar |
|---|---|
| Programa dentro del contenedor | seed, versiones de Python/PyTorch, dispositivo, hashes de entradas, métricas |
| Host que lo ejecuta | ID de imagen, OS/arquitectura, comando exacto y código de salida |

El programa no conoce automáticamente toda la identidad del contenedor. El módulo completa esa parte desde el host. Guardar un archivo JSON no garantiza que todos sus campos correspondan a observaciones reales.

## Post-run: éxito y persistencia

Primero revisa el código de salida. Después comprueba que los artefactos esperados existen y son legibles. Confirma que permanecen al terminar y eliminar el contenedor.

Una prueba negativa controlada intenta escribir en una entrada montada en solo lectura y debe fallar. Ese fallo esperado confirma una restricción; no significa que el entrenamiento haya fracasado. Debe distinguirse del código de salida del entrenamiento y hacerse sobre una ruta de prueba prevista.

## Comparar dos hosts requiere declarar el criterio

![[assets/m09-22.png|1000]]

- **Identidad de entradas/software:** comparar huellas, configuración e imagen.
- **Equivalencia numérica:** definir tolerancias para métricas o tensores; por ejemplo $|a-b|\leq\varepsilon$ con una tolerancia justificada por el objetivo.
- **Equivalencia funcional:** verificar un comportamiento acordado, como producir los artefactos y predicciones con el formato esperado.

No elijas la tolerancia después de ver qué diferencia quieres aceptar. Mismas métricas tampoco prueban mismos datos: resultados distintos pueden coincidir por casualidad.

Una conclusión defendible sería: «Se usaron las mismas huellas de datos y configuración y el mismo ID local de imagen en estas plataformas; la métrica difirió menos que la tolerancia acordada. No se evaluó equivalencia bit a bit». Es un ejemplo de redacción, no un resultado medido aquí.


## Comprueba lo aprendido

Haz clic en cada pregunta para mostrar u ocultar la respuesta. Intenta responder primero.

> [!question]- ¿Exit code 0 basta para aceptar el experimento?
> No. Hay que comprobar entradas, identidad de software y existencia/contenido/persistencia de salidas.

> [!question]- ¿Por qué hay un registro del programa y otro del host?
> Porque observan niveles diferentes. El programa mide su ejecución; el host identifica la imagen, plataforma, comando y terminación.

> [!question]- ¿Igualdad de accuracy implica igualdad bit a bit?
> No. Una métrica resumida puede coincidir aunque pesos y predicciones individuales difieran.

## Fuente y ruta

Material base: [[assets/module_09.pdf#page=18|M09, páginas 18, 19, 20, 21, 22, 23]]. Las analogías y los ejemplos pequeños son ampliaciones didácticas.

Volver a [[00 Índice - M09 Docker y ejecución reproducible]].
