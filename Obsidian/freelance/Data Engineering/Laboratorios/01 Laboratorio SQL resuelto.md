---
title: "Laboratorio SQL resuelto: del texto al ranking"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Laboratorio SQL resuelto: del texto al ranking

## Objetivo y alcance

Este ejercicio recrea el problema descrito en el spec con datos pequeños inventados. No reproduce ni verifica el notebook original, que no se adjuntó. Usa SQLite en memoria y no modifica bases externas.

El código completo está en [[Obsidian/freelance/Data Engineering/Laboratorios/laboratorio_sql.py|laboratorio_sql.py]]. Los resultados obtenidos están en [[Obsidian/freelance/Data Engineering/Laboratorios/resultados_sql.txt|resultados_sql.txt]].

Desde esta carpeta, puedes repetirlo con:

```bash
python3 laboratorio_sql.py
```

## Predice antes de ejecutar

| Partido | Marcador | Consecuencia |
|---|---|---|
| Qatar vs. Ecuador | 0,1 | Ecuador +3; Qatar +0 |
| Ecuador vs. Senegal | 2,2 | Ambos +1 |
| Qatar vs. Senegal | 1,1 | Ambos +1 |

Resultado esperado: Ecuador 4 puntos y +1 de diferencia; Senegal 2 y 0; Qatar 1 y −1. Top 2: Ecuador y Senegal.

## Cómo estudiar cada CTE

1. `separados`: comprueba un delimitador de partido y una coma; extrae nombres y goles como texto.
2. `validos`: exige nombres no vacíos y goles de uno o dos dígitos sin signo; convierte a enteros. Ese límite es una **regla didáctica declarada**, no una regla universal del fútbol.
3. `perspectivas`: convierte cada partido en dos participaciones, invirtiendo los goles para el visitante.
4. `puntos`: aplica victoria/empate/derrota.
5. `resumen`: suma por grupo y equipo.
6. `ranking`: establece orden completo y numera dentro de cada grupo.

Cambia el SELECT final manteniendo todas las CTE anteriores para inspeccionar la etapa que quieras. Escribe junto a cada salida qué representa una fila y cuántas esperas.

## Qué se comprobó

Se ejecutaron **18 comprobaciones**: puntos, Top 2, seis participaciones, conservación de diferencia de goles, empates, percent_rank, buckets 5/5/5/4/4 con 23 filas, NOT EXISTS, NOT IN con NULL, UNION/UNION ALL, EXCEPT/INTERSECT, conversiones de SQLite, NBSP, parsing de flechas y rechazo identificable de ocho entradas mal formadas.

No se midió rendimiento en SQL Server ni en un cluster. Los resultados validan los ejemplos sintéticos y sus supuestos, no la totalidad de un dataset desconocido.

## Variaciones para dominarlo

| Ejercicio del spec | Qué cambiar | Cómo verificar |
|---|---|---|
| A: flechas | Quitar espacios de Lucía->Carlos | Los extremos siguen correctos |
| B: normalización | Añadir NBSP y punto final | Obtienes ECUADOR con la regla explícita de calidad |
| C: Top N | Usar productos y categoría; añadir empates | ROW_NUMBER limita filas; RANK puede conservar más |
| D: quintiles | Mantener 23 scores y NTILE(5) | Tamaños 5,5,5,4,4 |
| SARGability | En un entorno SQL Server de práctica, comparar YEAR y rango | Examinar lecturas y plan, no asumir una mejora |
| Anti-join | Añadir NULL al lado derecho | NOT EXISTS conserva los IDs 2 y 3 |

Para que el ejercicio sea formativo, escribe la predicción en papel y solo después consulta la salida. Si falla, inspecciona el primer paso cuya granularidad o valores ya no coincidan.

> [!tip] Regla para recordar
> Predice, ejecuta y localiza el primer paso que cambia indebidamente tus filas.

## Comprueba que lo entendiste

> [!question]- ¿Por qué probar 3x además de abc como goles inválidos?
> Porque SQLite puede convertir 3x a 3. Solo probar abc no detecta todas las conversiones parciales que aceptan texto mal formado.

## Conexiones

- [[Obsidian/freelance/Data Engineering/SQL/04 CTE y transformaciones de partidos|04 CTE y transformaciones de partidos]] — fundamento del pipeline.
- [[Obsidian/freelance/Data Engineering/SQL/06 Ranking Top N y quintiles|06 Ranking Top N y quintiles]] — interpretación de puestos y buckets.
- [[Obsidian/freelance/Data Engineering/Calidad/02 Validación Unicode y contratos|02 Validación Unicode y contratos]] — reglas para normalizar y conservar incidencias.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
