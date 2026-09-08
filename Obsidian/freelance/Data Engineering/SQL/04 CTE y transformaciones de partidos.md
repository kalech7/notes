---
title: "CTE, CASE y transformación de partidos"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# CTE, CASE y transformación de partidos

## La historia completa

La entrada «Qatar vs. Ecuador, 0,1» mezcla dos equipos en una fila. Para calcular puntos por equipo necesitas dos perspectivas: Qatar perdió, Ecuador ganó. Después sumas las contribuciones de todos los partidos. Una CTE es un nombre temporal para una expresión dentro de una sentencia: organiza estos pasos y ayuda a inspeccionarlos.

```mermaid
flowchart LR
 A["1 fila por partido"] --> B["Parsear y validar"]
 B --> C["UNION ALL: 2 filas por partido"]
 C --> D["CASE: puntos por equipo"]
 D --> E["GROUP BY: equipo y grupo"]
 E --> F["Ranking"]
```

## Ejemplo ejecutable en SQLite

Partimos de goles ya tipados para concentrarnos en la transformación.

```sql
WITH partidos(id, grupo, local, visitante, gl, gv) AS (
  VALUES (1, 'A', 'Qatar', 'Ecuador', 0, 1),
         (2, 'A', 'Ecuador', 'Senegal', 2, 2)
), perspectivas AS (
  SELECT id, grupo, local AS equipo, gl AS favor, gv AS contra
  FROM partidos
  UNION ALL
  SELECT id, grupo, visitante, gv, gl FROM partidos
), puntuados AS (
  SELECT *, CASE
    WHEN favor IS NULL OR contra IS NULL THEN NULL
    WHEN favor > contra THEN 3
    WHEN favor = contra THEN 1
    ELSE 0 END AS puntos
  FROM perspectivas
)
SELECT equipo, grupo, SUM(puntos) AS puntos,
       SUM(favor - contra) AS diferencia
FROM puntuados
GROUP BY equipo, grupo
ORDER BY puntos DESC, diferencia DESC, equipo;
```

Resultado: Ecuador tiene 4 puntos y diferencia +1; Senegal, 1 y 0; Qatar, 0 y −1. De dos partidos pasamos a cuatro participaciones y finalmente a tres equipos. `UNION ALL` conserva contribuciones repetidas: dos victorias idénticas en partidos diferentes deben sumar dos veces.

`CASE` devuelve el valor de la primera condición verdadera. La rama de nulos evita interpretar un marcador desconocido como derrota; después debes decidir si rechazas esa fila, la marcas o detienes el cálculo. `SUM` ignora nulos, así que conservarlos sin contar incidencias todavía puede producir un total incompleto.

## Cómo depurar y cuándo usar una CTE

Para inspeccionar `perspectivas`, ejecuta **todo el WITH** y cambia el SELECT final por `SELECT * FROM perspectivas`. El nombre no existe en otra sentencia independiente. Una CTE no garantiza materialización ni cache: su tratamiento depende del motor y del plan. Si reutilizas datos entre sentencias, evalúa una tabla temporal. Una CTE recursiva permite recorrer jerarquías con una base y un paso recursivo; requiere condición de terminación y control de ciclos.

## Ejercicio

Añade un empate 1–1 entre Qatar y Senegal. Antes de ejecutar, predice seis participaciones, Qatar con 1 punto y Senegal con 2. Comprueba también que la suma global de diferencias de goles sea cero.

> [!tip] Regla para recordar
> Una CTE nombra un paso; CASE expresa la regla; GROUP BY cambia la granularidad.

## Comprueba que lo entendiste

> [!question]- ¿Puedo ejecutar SELECT * FROM perspectivas en una sentencia nueva?
> No: la CTE vive en su sentencia. Conserva el WITH y cambia su consulta final.

## Conexiones

- [[Obsidian/freelance/Data Engineering/SQL/05 Parsing SQLite y normalización|05 Parsing SQLite y normalización]] — convierte los textos de origen en las columnas usadas aquí.
- [[Obsidian/freelance/Data Engineering/SQL/06 Ranking Top N y quintiles|06 Ranking Top N y quintiles]] — ordena el resumen obtenido.
- [[Obsidian/posgrado/master/MATEMÁTICAS Y PROGRAMACIÓN IA/modelo relacional y sql analitico/05 CTE, ranking y auditoría de resultados|05 CTE, ranking y auditoría de resultados]] — ya usas etapas lógicas equivalentes para comparar modelos.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
