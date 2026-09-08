---
title: "Ventanas: ranking, Top N y quintiles"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Ventanas: ranking, Top N y quintiles

## Intuición

Una ventana añade una medida relacionada con otras filas sin resumirlas en una sola. `PARTITION BY grupo` crea competencias independientes y `ORDER BY puntos DESC` decide el orden dentro de cada competencia. No implica particionar archivos ni ordenar la presentación final.

## Los empates cambian la respuesta

| Empleado | Salario | ROW_NUMBER posible | RANK | DENSE_RANK | PERCENT_RANK |
|---|---:|---:|---:|---:|---:|
| Ana | 1000 | 1 | 1 | 1 | 0 |
| Luis | 1000 | 2 | 1 | 1 | 0 |
| Pedro | 900 | 3 | 3 | 2 | 2/3 |
| Carla | 800 | 4 | 4 | 3 | 1 |

Con `ORDER BY salario DESC` solamente, Ana y Luis pueden intercambiar sus ROW_NUMBER. Para hacerlo determinista agrega una clave única al orden de **ROW_NUMBER**. Si agregas esa clave a **RANK**, desaparece el empate por salario: todas las expresiones del orden participan en la igualdad.

`PERCENT_RANK = (RANK - 1)/(n - 1)` cuando n > 1; con una fila devuelve 0. El último grupo empatado puede tener percent_rank menor que 1. `CUME_DIST` cuenta la fracción de filas anteriores o empatadas con la actual: para Ana y Luis sería 2/4.

```sql
-- SQLite; exactamente hasta dos filas por grupo.
WITH tabla(grupo, equipo, puntos, diferencia) AS (
 VALUES ('A','Ecuador',4,1), ('A','Senegal',1,0), ('A','Qatar',0,-1),
        ('B','X',3,2), ('B','Y',3,1), ('B','Z',0,-3)
), ranking AS (
 SELECT *, ROW_NUMBER() OVER (
   PARTITION BY grupo
   ORDER BY puntos DESC, diferencia DESC, equipo
 ) AS rn
 FROM tabla
)
SELECT * FROM ranking WHERE rn <= 2 ORDER BY grupo, rn;
```

Aquí `equipo` es único dentro de cada grupo de ejemplo. En datos reales usa una clave única final. Si un grupo tiene una sola fila, devuelve una: ROW_NUMBER no inventa un segundo participante. Para conservar todos los líderes empatados, usa `RANK` solo sobre la métrica de negocio y filtra rango 1.

## NTILE reparte filas

```text
23 filas ordenadas → NTILE(5)
Bucket 1: █████ 5
Bucket 2: █████ 5
Bucket 3: █████ 5
Bucket 4: ████  4
Bucket 5: ████  4
```

Los grupos más grandes van primero. Con orden descendente, bucket 1 contiene las mejores filas; con ascendente, las menores. `NTILE` puede separar valores empatados. No genera cinco intervalos de igual amplitud numérica ni calcula los puntos de corte de una distribución continua. Si hay menos de cinco filas, algunos números de bucket no aparecen.

## Práctica

Cambia la consulta a Top 3 productos por categoría. Pon ventas 100, 90, 90, 80. ROW_NUMBER <= 3 devuelve tres; RANK <= 3 también tres en este caso. Añade otro 90: ahora RANK puede devolver cuatro. Justifica si tu negocio quiere tres productos o todos los empates del puesto admitido.

> [!tip] Regla para recordar
> ROW_NUMBER cuenta filas; RANK conserva empates; NTILE reparte filas ordenadas.

## Comprueba que lo entendiste

> [!question]- ¿RANK sobre distancia y código conserva dos centros a la misma distancia?
> Solo si también empatan en código. Si el código es único, el criterio adicional rompe el empate.

## Conexiones

- [[Obsidian/freelance/Data Engineering/Spark/05 Ventanas y métricas de jugadores|05 Ventanas y métricas de jugadores]] — el mismo patrón se escribe con Window de PySpark.
- [[Obsidian/posgrado/master/MATEMÁTICAS Y PROGRAMACIÓN IA/modelo relacional y sql analitico/05 CTE, ranking y auditoría de resultados|05 CTE, ranking y auditoría de resultados]] — conecta los empates deportivos con empates en accuracy.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
