[[Fechas]]

> [!info] Explicación
> Esta nota agrupa los comandos fundamentales de SQL para el lenguaje de definición de datos (DDL) y el lenguaje de manipulación de datos (DML). Se incluyen las operaciones básicas de CRUD (Crear, Leer, Actualizar, Eliminar) y ejemplos prácticos de cómo realizar consultas combinando múltiples tablas a través de la cláusula JOIN.

## Create 
```sql
CREATE TABLE (nombre)(
	nombre_col1 (tipo de dato) (key?),
	...
);
```

## Eliminar
```sql
DROP (TABLE o DATABASE)
```

## Modificar

```sql
ALTER TABLE (tabla) ADD (nombre_columna) tipo_de_dato
ALTER TABLE (tabla) DROP (nombre_columna)
```

## Insertar

```sql
INSERT INTO tabla (argumentos)
```

## Select
**SELECT** sirve para realizar consultas a la base de datos.

Los comandos tienen CLÁUSULAS. El orden lógico de escritura suele ser:
**SELECT — FROM — WHERE — GROUP BY — HAVING — ORDER BY**

```sql
SELECT (lista_de_atributos) FROM tabla;
```

La cláusula `FROM` es opcional si los datos no se obtienen de tablas específicas.

> [!info] Explicación de las Cláusulas
> Comúnmente las sentencias `SELECT` van acompañadas, después del `FROM`, de la cláusula `WHERE`. Esta cláusula permite añadir filtros a la consulta para restringir o filtrar los registros que se van a devolver. Existen además otras cláusulas después del `WHERE` que repercuten en cómo se agruparán los registros y el orden en que se visualizarán, como por ejemplo `GROUP BY` y `ORDER BY`.

No es sensible a mayúsculas o minúsculas (case-insensitive) en el caso de las palabras clave del comando SQL.

_**Imprime la inicial del nombre y el apellido:**_

```sql
SELECT SUBSTRING(first_name, 1, 1) || '.' || ' ' || last_name, create_date
FROM Customer;
```

## Alias de columna

Se utiliza para colocar nombres personalizados a las columnas en el resultado de la consulta.

_**Cambia de nombre las columnas por un texto descriptivo:**_

```sql
SELECT SUBSTRING(first_name, 1, 1) || '.' || ' ' || last_name as "inicial + nombre", create_date as "fecha de creacion"
FROM Customer;
```

# Comando JOIN

> [!info] Explicación de JOIN
> Los `JOIN` permiten unir tablas basándose en una columna común para hacer consultas más complejas y relacionadas. Hay tres tipos principales de JOIN:
> - **INNER JOIN:** Devuelve los registros que tienen coincidencias en ambas tablas.
> - **LEFT OUTER JOIN:** Devuelve todos los registros de la tabla de la izquierda, y las coincidencias de la derecha (si no hay coincidencia, retorna NULL).
> - **RIGHT OUTER JOIN:** Devuelve todos los registros de la tabla de la derecha, y las coincidencias de la izquierda.
> 
> Para realizar un JOIN, se utiliza la cláusula `ON`, que especifica la condición para unir las tablas (generalmente igualando Primary Key y Foreign Key). Además, el `NATURAL JOIN` iguala automáticamente los atributos con el mismo nombre.

**Tabla 1 || Intersección || Tabla 2**

Left Outer || Inner || Right Outer

_Tabla izquierda_ INNER JOIN _tabla derecha_ ON (condición)

_Tabla izquierda_ LEFT OUTER JOIN _tabla derecha_ ON (condición)

_Tabla izquierda_ RIGHT OUTER JOIN _tabla derecha_ ON (condición)

_Tabla izquierda_ NATURAL JOIN _tabla derecha_

En el `NATURAL JOIN` automáticamente se igualan los atributos con el mismo nombre.

```sql
SELECT first_name, last_name
FROM customer C INNER JOIN Rental R 
ON (C.customer_id = R.customer_id);
```

```sql
-- Los nombres de los clientes que han rentado películas o que nunca lo han hecho
SELECT first_name || ' ' || last_name AS 'Nombre'
FROM customer C LEFT OUTER JOIN Rental R
ON (C.customer_id = R.customer_id);

-- Desplegar la fecha de realización de alquiler
SELECT first_name || ' ' || last_name as "nombre", rental_date
FROM customer C LEFT OUTER JOIN Rental R
ON (C.customer_id = R.customer_id)
-- WHERE rental_date ... (incompleto en el original)

-- Cuáles son los alquileres que se han realizado a los clientes, con registro de clientes o no.
-- Desplegar el ID de alquiler y el nombre del cliente.
-- En caso de que no se haya registrado el cliente, desplegar un NULL.
SELECT rental_id, first_name || ' ' || SUBSTRING(last_name, 1, 1) || '.' AS "nombre"
FROM customer C RIGHT OUTER JOIN Rental R
ON (C.customer_id = R.customer_id)
WHERE C.customer_id IS NULL;

-- Despliegue los nombres de los clientes que han realizado algún alquiler junto a la fecha de realización
SELECT first_name || ' ' || last_name AS "nombre", rental_date as "fecha de alquiler"
FROM Customer C INNER JOIN rental R 
ON (C.customer_id = R.customer_id)
WHERE C.customer_id IS NULL OR R.customer_id IS NULL; -- Nota: Al usar INNER JOIN, esto normalmente será vacío.

-- Cuáles son los montos de los pagos que ha realizado la cliente Susan 
SELECT amount, R.rental_id
FROM payment P INNER JOIN rental R
ON (P.rental_id = R.rental_id)
INNER JOIN customer C 
ON (R.customer_id = C.customer_id) 
WHERE first_name = 'susan';
```

| Customer | Rental | Payment |
|---|---|---|
| customer_id (pk) | rental_id (pk) | rental_id(fk) |
| | customer_id(fk) | |

> [!info] Explicación de Relaciones
> Siempre se relaciona una clave primaria (Primary Key - PK) de una tabla principal con una clave foránea (Foreign Key - FK) de una tabla dependiente, asegurando así la integridad referencial.

```sql
-- En qué película ha actuado Grace Mostel 
SELECT title
FROM film F INNER JOIN film_actor FA ON f.film_id = fa.film_id 
INNER JOIN actor A ON (FA.actor_id = A.actor_id) 
WHERE first_name = 'grace' AND last_name = 'mostel';

-- La segunda opción (solo por primer nombre)
SELECT title, first_name, last_name 
FROM film F INNER JOIN film_actor FA ON f.film_id = fa.film_id 
INNER JOIN actor A ON (FA.actor_id = A.actor_id) 
WHERE first_name = 'grace';
```
[[ejemplos]]
[[ejercicios]]

## Notas relacionadas
- [[SQL]]
- [[Principales tipo de datos]]
- [[Insertar datos]]
- [[Subconsultas]]
- [[Vistas]]
- [[Transaccion]]
