---
title: "Laboratorio Spark: aggregate, join back y salida"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Laboratorio Spark: aggregate, join back y salida

## Estado de verificación

El script [[Obsidian/freelance/Data Engineering/Laboratorios/laboratorio_spark.py|laboratorio_spark.py]] tiene sintaxis Python revisada, pero **no se ejecutó aquí** porque PySpark no está instalado. Requiere un entorno con PySpark y Java compatibles; comprueba su versión antes de ejecutarlo. Usa datos sintéticos y crea un directorio temporal nuevo para las salidas.

En un entorno preparado, desde esta carpeta:

```bash
spark-submit laboratorio_spark.py
```

## Predicción geométrica

Hay tres centros públicos A=(0,0), B=(2,0), C=(1,3). Su promedio es (1,1). A y B están a √2; C está a 2. El centro privado D=(10,10), único válido de su grupo, tiene distancia 0 a su propio promedio.

- Con ROW_NUMBER y desempate por ID: salen A y D.
- Con RANK sobre distancia únicamente: salen A, B y D.
- Una coordenada ausente y un NaN se apartan antes de calcular.

![[Obsidian/freelance/Data Engineering/assets/centroide.png]]

## Recorrido del código

1. Construye el DataFrame y etiqueta validez de coordenadas.
2. Separa cuatro centros válidos y dos rechazados; valida finitud además de nulos.
3. Calcula medias por titularidad.
4. Reincorpora esas medias mediante join y comprueba que no multiplique filas.
5. Calcula distancia nativa y con UDF; compara con tolerancia.
6. Selecciona un ganador o todos los empatados según la ventana.
7. Construye arrays de structs y consulta una vista temporal.
8. Escribe el resultado plano en Parquet, JSON y CSV con separador `|`.
9. Lee las tres salidas y comprueba dos IDs esperados.

Los collect del script se restringen a resultados sintéticos de dos o tres IDs. No traslades ese patrón a una salida sin límite de tamaño.

## Ejercicios E a I de la ampliación

| Ejercicio | Punto de partida | Resultado que debes poder explicar |
|---|---|---|
| E: schema y casts | Nota Schemas y DataFrames | Diferencia entre edad ausente y conversión fallida |
| F: media por cliente | Sustituir titularidad por cliente_id y coordenadas por monto | Cada transacción conserva su detalle y recibe la media de su cliente |
| G: distancia | Script de este laboratorio | Igualdad aproximada nativa/UDF y política de empates |
| H: nested JSON | Nota Datos anidados y JSON | Una fila por cliente con array de productos/precios |
| I: formatos | Últimos pasos del script | Mismos datos lógicos; distinta representación física |

Ejemplo manual del ejercicio F: montos 10 y 30 del cliente A producen media 20; tras el join vuelven dos filas `(A,10,20)` y `(A,30,20)`. Agrupar a 20 y perder el detalle respondería otra pregunta.

## Cómo comparar rendimiento sin engañarte

Mira `explain('formatted')` de ambas distancias. Localiza la expresión nativa y los operadores de ejecución Python que aparezcan en tu versión. La sintaxis más corta no demuestra menor tiempo. Para medir fuerza una acción que consuma la distancia, repite con condiciones comparables y registra volumen, particiones, cache y entorno. No se incluyen tiempos inventados en estas notas.

> [!tip] Regla para recordar
> Primero comprueba la respuesta sobre pocos datos; después estudia el plan y la escala.

## Comprueba que lo entendiste

> [!question]- ¿El laboratorio exige instalar o desplegar un cluster?
> No. Está preparado para modo local con dos hilos en un entorno Spark existente. Ese modo no prueba rendimiento ni fallos de múltiples máquinas.

## Conexiones

- [[Obsidian/freelance/Data Engineering/Spark/07 Centroides distancia y UDF|07 Centroides distancia y UDF]] — explica cada paso matemático y su costo.
- [[Obsidian/freelance/Data Engineering/Spark/04 Schemas y DataFrames|04 Schemas y DataFrames]] — incluye el ejercicio de conversiones.
- [[Obsidian/freelance/Data Engineering/Spark/06 Datos anidados y JSON|06 Datos anidados y JSON]] — resuelve la estructura de clientes e hijos.
- [[Obsidian/freelance/Data Engineering/Spark/08 Formatos particiones y salida|08 Formatos particiones y salida]] — interpreta directorios part y formatos.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
