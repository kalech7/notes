---
title: "Database Internals — Ejercicios integradores"
created: 2026-09-26
tags:
  - lecturas/database-internals
  - ejercicios
  - repaso
---

# Ejercicios integradores

[[Obsidian/lecturas/database internals/00 Empieza aquí|Inicio del libro]] → [[Obsidian/lecturas/database internals/05 Práctica y repaso/00 Índice|Práctica y repaso]]

Intenta responder antes de desplegar la solución.

> [!question]- 1. Altura y fanout
> Un árbol tiene fanout efectivo 100 y tres niveles de hijos bajo la raíz. Aproxima cuántas hojas puede direccionar.
>
> **Respuesta:** alrededor de `100³ = 1 000 000` hojas. Es una aproximación: ocupación y estructura real modifican el número.

> [!question]- 2. Punto de inserción
> En `[10, 18, 27, 41]`, ¿qué devuelve una lower bound para `25`?
>
> **Respuesta:** índice 2, la posición de 27, que es el primer valor mayor o igual que 25. Insertar allí conserva orden.

> [!question]- 3. Separadores e hijos
> Un nodo contiene separadores `[20, 50, 80]`. Escribe sus cuatro intervalos.
>
> **Respuesta:** `k<20`, `20≤k<50`, `50≤k<80`, `k≥80`.

> [!question]- 4. Fragmentación
> Una página tiene huecos de 40, 90 y 70 bytes. Una celda necesita 150 bytes más un slot de 4. ¿Cabe sin compactar? ¿Y después?
>
> **Respuesta:** no sin compactar; el mayor hueco es 90. Después podría caber porque hay 200 bytes en total, siempre que el proceso pueda consolidarlos y no existan otras restricciones.

> [!question]- 5. Endianness
> Interpreta `78 56 34 12` como entero de 32 bits little-endian.
>
> **Respuesta:** `0x12345678`. El byte `78` ocupa el offset menor, pero es el menos significativo.

> [!question]- 6. Índice secundario
> Un índice por email guarda la primary key. ¿Por qué encontrar el email no entrega necesariamente toda la fila?
>
> **Respuesta:** la hoja secundaria puede contener solo email y primary key. Hace falta otra búsqueda para recuperar columnas no cubiertas.

> [!question]- 7. Split y crash
> Se escribe la nueva hoja, pero el proceso falla antes de actualizar el padre. ¿Qué estado físico queda?
>
> **Respuesta:** puede quedar una página asignada pero inalcanzable. WAL/recovery o una comprobación de consistencia debe completar o revertir la operación y reconciliar asignación.

> [!question]- 8. MVCC y vacuum
> Una fila fue actualizada, pero una transacción antigua aún puede verla. ¿Puede vacuum reclamar la versión?
>
> **Respuesta:** no. Dejó de ser actual, pero sigue siendo visible para un snapshot válido.

> [!question]- 9. Bulk loading
> ¿Por qué llenar al 100 % puede ser correcto para un árbol inmutable y malo para uno mutable?
>
> **Respuesta:** el inmutable no necesita espacio para inserts. En el mutable, la primera modificación puede provocar splits inmediatos.

> [!question]- 10. Diseña una medición
> Quieres comparar páginas de 4 y 16 KiB. ¿Qué medirías además de operaciones por segundo?
>
> **Respuesta:** percentiles de latencia, altura y fanout efectivos, page reads, bytes leídos/escritos, caché, ocupación, splits, compresión, tiempo de mantenimiento y espacio. Debe usarse la misma carga y volumen representativos.

## Reto final

Dibuja un insert que cause split de hoja y de padre. Marca:

1. páginas nuevas;
2. separadores promovidos;
3. breadcrumbs consumidos;
4. registros WAL necesarios;
5. puntos de fallo que recovery debe resolver.

Si el dibujo solo muestra el árbol final, falta la parte más importante: la transición segura.

---

**Anterior:** [[Obsidian/lecturas/database internals/05 Práctica y repaso/02 Glosario y tarjetas de memoria|Glosario y tarjetas]] · **Índice:** [[Obsidian/lecturas/database internals/05 Práctica y repaso/00 Índice|Práctica]] · **Inicio:** [[Obsidian/lecturas/database internals/00 Empieza aquí|Ruta de estudio]]
