---
title: "Parsing SQLite y limpieza de texto"
created: 2026-09-07
tags:
  - freelance/data-engineering
  - estudio
---

# Parsing SQLite y limpieza de texto

## Qué problema resuelve

Parsear es extraer partes de una representación. Limpiar es homogeneizar valores. Normalizar un modelo relacional es organizar entidades y dependencias: no son exactamente la misma operación, aunque en el documento «normalización» también se usa para limpieza.

```sql
-- SQLite: ejemplo completo.
WITH origen(partido, resultado) AS (
  VALUES ('Qatar vs. Ecuador', '3,2')
)
SELECT
  SUBSTR(partido, 1, INSTR(partido, ' vs. ') - 1) AS local,
  SUBSTR(partido, INSTR(partido, ' vs. ') + 5) AS visitante,
  CAST(SUBSTR(resultado, 1, INSTR(resultado, ',') - 1) AS INTEGER) AS gl,
  CAST(SUBSTR(resultado, INSTR(resultado, ',') + 1) AS INTEGER) AS gv
FROM origen;
```

`INSTR` devuelve la primera posición, contando desde 1; devuelve 0 si no encuentra el delimitador. En este texto, « vs. » comienza en 6 y mide 5 caracteres. Por eso el primer equipo ocupa de 1 a 5 y el segundo empieza en 11. Restar 1 excluye el delimitador; sumar su longitud lo salta completo.

## El ejemplo feliz no es un parser robusto

Si falta « vs. », la extracción deja de representar local/visitante. Si aparece dos veces, no sabes cuál división era válida. Primero cuenta y valida delimitadores, luego extrae y comprueba que cada parte no esté vacía. En `Juan -> Maria`, `Pedro -> Ana ` y `Lucía->Carlos`, el delimitador real puede ser `->`: extrae por él y aplica TRIM a cada lado. Así no dependes de espacios opcionales.

SQLite permite `CAST('abc' AS INTEGER)` y puede devolver 0; `CAST('3x' AS INTEGER)` puede devolver 3. **Convertir no valida.** Para goles no negativos, valida que el texto no esté vacío y que no contenga caracteres ajenos a `0..9`; además limita su rango de negocio antes del cast.

## Nombres y caracteres invisibles

```sql
-- SQLite. CHAR(160) es NBSP, un espacio no separable.
SELECT UPPER(TRIM(REPLACE(CHAR(160) || 'Ecuador', CHAR(160), ' ')));
```

Devuelve `ECUADOR`. Cambia NBSP a un espacio corriente antes de recortar bordes. `TRIM` no es una promesa de eliminar todo Unicode. El `UPPER` incorporado de SQLite convierte ASCII; el tratamiento de mayúsculas de letras acentuadas requiere una extensión apropiada o limpieza externa. Tampoco elimina tildes.

| Función SQLite | Uso | Trampa |
|---|---|---|
| INSTR | Localizar delimitador | 0 significa ausencia |
| SUBSTR | Extraer caracteres | Posiciones basadas en 1 |
| TRIM | Quitar caracteres de bordes | No todos los espacios Unicode |
| REPLACE | Sustituir coincidencias | Puede borrar puntuación significativa |
| UPPER | Normalizar mayúsculas ASCII | Irán no se convierte automáticamente en IRAN |
| CAST | Convertir representación | Texto malo puede convertirse sin error |
| `||` | Concatenar | Concatenar con NULL produce NULL |

No borres todos los puntos o tildes de cualquier nombre sin una regla. Para «Iran» e «Irán», una tabla de equivalencias revisada que produzca un `pais_id` es más clara que transformaciones destructivas. Conserva el nombre original para rastrear errores.

> [!tip] Regla para recordar
> Extrae, valida y convierte; no confundas que algo sea convertible con que sea correcto.

## Comprueba que lo entendiste

> [!question]- ¿Qué deberías hacer antes de CAST sobre un resultado deportivo?
> Verificar delimitador, partes presentes, caracteres numéricos permitidos y rango. CAST por sí solo no acredita esos requisitos.

## Conexiones

- [[Obsidian/freelance/Data Engineering/Calidad/02 Validación Unicode y contratos|02 Validación Unicode y contratos]] — añade reglas, cuarentena y métricas de limpieza.
- [[Obsidian/freelance/Data Engineering/SQL/07 Conjuntos joins y ausencias|07 Conjuntos joins y ausencias]] — explica por qué un join textual puede fallar.

Volver a [[Obsidian/freelance/Data Engineering/00 Empieza aquí|la ruta de estudio]].
