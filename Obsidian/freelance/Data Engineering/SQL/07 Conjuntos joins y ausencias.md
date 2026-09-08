---
title: "Conjuntos, joins y registros sin correspondencia"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Conjuntos, joins y registros sin correspondencia

## Concatenar y comparar conjuntos

| Operación | A = [1,1,2], B = [2,3] | Significado |
|---|---|---|
| UNION ALL | [1,1,2,2,3] | Conserva todas las contribuciones |
| UNION | [1,2,3] | Elimina duplicados del resultado completo |
| EXCEPT | [1] | Valores de A ausentes de B |
| INTERSECT | [2] | Valores comunes |

El orden de esta tabla es ilustrativo: SQL requiere `ORDER BY` para garantizar presentación. Las variantes sin ALL tienen semántica de conjunto. `UNION` compara la fila seleccionada completa y suele requerir deduplicación por hash u ordenamiento. Usa UNION ALL cuando los duplicados sean válidos o ya esté garantizada la unicidad y no necesites deduplicar.

Un JOIN relaciona columnas y puede multiplicar filas. Si una clave aparece dos veces a la izquierda y tres a la derecha, el emparejamiento genera seis combinaciones. INTERSECT no equivale a cualquier INNER JOIN: puede eliminar repetidos y trata la igualdad de conjuntos de forma diferente a `=` con NULL.

## Clientes sin movimientos

```sql
-- SQLite y SQL estándar compatible; ejemplos completos.
WITH clientes(id) AS (VALUES (1),(2),(3)),
     movimientos(cliente_id) AS (VALUES (1),(NULL))
SELECT c.id
FROM clientes c
WHERE NOT EXISTS (
 SELECT 1 FROM movimientos m WHERE m.cliente_id = c.id
);
```

Devuelve 2 y 3. NOT EXISTS pregunta si hay una fila que cumpla la correlación. Un NULL ajeno no contamina esa pregunta.

`id NOT IN (1, NULL)` se parece a `id <> 1 AND id <> NULL`. Para 2, la segunda comparación es UNKNOWN; WHERE conserva solamente TRUE, así que 2 no aparece. Si la propia clave izquierda puede ser NULL, también debes definir si esa ausencia de identidad debe aparecer o excluirse.

```sql
-- Alternativa: comprobar una columna derecha que sea no nula en coincidencias.
SELECT c.id FROM clientes c
LEFT JOIN movimientos m ON m.cliente_id = c.id
WHERE m.cliente_id IS NULL;
```

Este fragmento presupone las tablas/CTE del ejemplo. Con `m.cliente_id = c.id`, una coincidencia no puede tener esa clave derecha nula. No uses cualquier columna nullable, como una descripción, para detectar ausencia.

## LEFT JOIN y filtros

Un LEFT JOIN conserva la población izquierda. Si escribes `WHERE derecha.estado = 'activo'`, descartas también las filas sin correspondencia y puedes convertirlo en un inner join de hecho. Poner esa condición en `ON` mantiene todos los registros izquierdos y enlaza solo derechos activos. Las dos consultas responden preguntas distintas.

## El join basado en texto

Buscar grupos con `LIKE '%grupo A%'` dentro de «1º del grupo A vs. 2º del grupo B» es frágil: «grupo AB» puede coincidir, la puntuación cambia y `%`/`_` son comodines. En SQLite puedes construir patrones con `||`, pero es mejor extraer y validar columnas `grupo_local`, `puesto_local`, `grupo_visitante`, `puesto_visitante`, y unir por claves exactas. Conserva como incidencia cualquier descripción ambigua.

> [!tip] Regla para recordar
> Conservar, relacionar y deduplicar son decisiones distintas.

## Comprueba que lo entendiste

> [!question]- ¿UNION corrige un JOIN que duplicó facturas?
> No de forma confiable. Puede ocultar el error o borrar hechos legítimos; primero corrige claves, granularidad y cardinalidad.

## Conexiones

- [[Obsidian/freelance/Data Engineering/SQL/05 Parsing SQLite y normalización|05 Parsing SQLite y normalización]] — permite reemplazar emparejamientos textuales por columnas confiables.
- [[Obsidian/freelance/Data Engineering/Spark/03 Joins cache y optimización|03 Joins cache y optimización]] — analiza el costo distribuido de relacionar tablas.
- [[Obsidian/posgrado/master/MATEMÁTICAS Y PROGRAMACIÓN IA/modelo relacional y sql analitico/02 Población, NULL y métricas ausentes con LEFT JOIN|02 Población, NULL y métricas ausentes con LEFT JOIN]] — tus notas de IA también preservan elementos sin métricas.
- [[Obsidian/posgrado/master/MATEMÁTICAS Y PROGRAMACIÓN IA/modelo relacional y sql analitico/03 JOIN, cardinalidad y el peligro de DISTINCT|03 JOIN, cardinalidad y el peligro de DISTINCT]] — explica por qué DISTINCT no repara un join mal definido.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
