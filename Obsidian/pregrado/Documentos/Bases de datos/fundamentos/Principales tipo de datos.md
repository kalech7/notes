[[SQL]]

> [!info] Explicación
> Al definir una tabla en una base de datos relacional, cada columna debe tener asignado un **tipo de dato**. Esto le indica al motor de base de datos qué tipo de información se va a almacenar (texto, números, fechas, etc.), lo que permite optimizar el almacenamiento y validar los datos antes de guardarlos.

```sql
INT            -- Números enteros (sin decimales)
DECIMAL(M,N)   -- Números decimales exactos. M es la precisión total, N son los decimales
VARCHAR(N)     -- Cadena de texto de longitud variable hasta N caracteres
BLOB           -- Binary Large Object. Sirve para almacenar datos binarios grandes (imágenes, archivos)
DATE           -- Almacena fechas en formato YYYY-MM-DD
TIMESTAMP      -- Almacena fecha y hora en formato YYYY-MM-DD HH:MM:SS. Útil para registros de creación/modificación
```

> [!info] Llaves (Keys)
> - **PRIMARY KEY**: Identificador único de cada fila en una tabla. No puede ser NULL ni repetirse.
> - **FOREIGN KEY**: Un campo (o colección de campos) en una tabla que se refiere a la `PRIMARY KEY` de otra tabla, estableciendo una relación entre ambas.

PRIMARY KEY
FOREIGN KEY

## Notas relacionadas
- [[SQL]]
- [[Comandos]]
- [[Insertar datos]]
- [[Transaccion]]
