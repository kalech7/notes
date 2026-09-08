---
title: "Calidad de datos: seis preguntas y su contexto"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Calidad de datos: seis preguntas y su contexto

## Un dato puede ser válido y falso

La fecha `2000-01-01` cumple un formato y podría ser un día real. Eso no demuestra que sea el cumpleaños de la persona. Calidad no significa únicamente que el archivo se abra o la consulta termine: significa que los datos son adecuados para un uso.

| Dimensión | Pregunta | Ejemplo de falla | Control posible |
|---|---|---|---|
| Exactitud / accuracy | ¿Representa la realidad? | Edad registrada equivocada | Comparar con una fuente confiable |
| Completitud | ¿Falta información requerida? | Email obligatorio ausente | Contar nulos y vacíos |
| Consistencia | ¿Concuerdan representaciones relacionadas? | País distinto entre dos catálogos | Reconciliar por una misma identidad |
| Singularidad / uniqueness | ¿Se repite una entidad que debería ser única? | Mismo ID duplicado | Agrupar por clave y contar |
| Oportunidad / timeliness | ¿Llega cuando se necesita? | Reporte diario con datos de hace una semana | Medir retraso respecto a la necesidad |
| Validez | ¿Cumple dominio y reglas? | Fecha imposible o goles negativos | Validar formatos y rangos |

Los **metadatos** permiten interpretar esas preguntas: definición de campos, unidad, zona horaria, fuente, propietario y fecha de carga. No son necesariamente una séptima dimensión en todos los marcos; son contexto indispensable.

## Diagnóstico de tres filas

| id | email | nacimiento como texto |
|---:|---|---|
| 1 | a@test.com | 2000-01-01 |
| 2 | NULL | 2001-03-01 |
| 2 | b@test.com | 99-99-9999 |

Falta un email: problema de completitud **si es requerido**. Se repite ID 2: problema de singularidad **si ID identifica una sola fila**. La fecha imposible viola validez. No podemos concluir que los demás cumpleaños sean exactos sin compararlos con la realidad. Tampoco podemos afirmar inconsistencia entre sistemas con una sola fuente.

## Cómo convertirlo en métricas

Si 90 de 100 filas tienen email informado, la completitud de ese campo es 90 %. Define primero si cadenas vacías y espacios cuentan como ausencia. Para duplicados, distingue «filas que pertenecen a claves repetidas» de «filas adicionales que habría que resolver»: dos filas con ID 2 dan dos en la primera métrica y una en la segunda. Nombrarlas evita porcentajes engañosos.

```mermaid
flowchart LR
 A["Uso del dato"] --> B["Regla y población"]
 B --> C["Métrica con denominador"]
 C --> D["Umbral acordado"]
 D --> E["Acción ante incumplimiento"]
```

## Error común y ejercicio

No reemplaces automáticamente todos los nulos por cero. «Desconozco cuántos goles» no significa «anotó cero». Ese reemplazo cambia promedios y rankings. Diseña reglas para país, goles y fecha: indica si un valor inválido detiene la carga, se aparta con motivo o puede mantenerse marcado. La respuesta depende del uso, no de la comodidad de la función.

> [!tip] Regla para recordar
> Formato correcto, dato completo y dato verdadero son comprobaciones diferentes.

## Comprueba que lo entendiste

> [!question]- Si una fecha es válida, ¿también es exacta?
> No. Puede ser una fecha real asignada a la persona equivocada. Exactitud exige correspondencia con la realidad.

## Conexiones

- [[Obsidian/freelance/Data Engineering/Calidad/02 Validación Unicode y contratos|02 Validación Unicode y contratos]] — convierte las dimensiones en pasos operativos.
- [[Obsidian/freelance/Data Engineering/DevOps/01 DevOps DataOps y CALMS|01 DevOps DataOps y CALMS]] — integra las métricas en operación y retroalimentación.
- [[Obsidian/pregrado/big data/extract transform load|extract transform load]] — profundiza los controles de transformación y carga que mencionas.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
