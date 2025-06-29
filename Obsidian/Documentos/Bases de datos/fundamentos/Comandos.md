[[Fechas]]
## Create 
```sql
CREATE TABLE (nombre)(nombre_columnas
			nombre_col1 (tipo de dato ) (key?),
);

```
## Eliminar
```sql
DROP (table o database)
```
## Modificar

```sql
ALTER TABLE (columna) ADD (nombre col) tipodedato
					  DROP 
```
## Insertar

```sql
INSERT INTO tabla (argumentos)
```

## Select
**select** sirve para realizar consultas a la base de datos

Los comandos tienen CLAUSULAS

**Select— from—-where—group by—having—- order by**

SELECT (lista_de _atributos) FROM tabla;

La clausula FROM es opcional si los datos nose obtienen de tablas

Comúnmente las sentencias `SELECT` van acompañadas después del `FROM` de la cláusula `WHERE`, que permite añadir filtros a la consulta para restringir o filtrar los registros a devolver. Existen además otras clausulas después del `WHERE` que repercuten en cómo se visualizarán los registros y el orden en que se visualizarán, como por ejemplo el **GROUP BY** y **ORDER BY**.

no es sensible al uppercase en el caso de las plabras clave del comando

_**imprime la inicial del nombre y el apellido**_

```sql
SELECT SUBSTRING (first_name,1,1)|| '.' || '' || last_name,create_date
FROM Customer
```

## Alias de columna

Coloca nombres a las columnas

_**Cambia de nombre las columnas por lo que tenga**_

```sql
SELECT SUBSTRING (first_name,1,1)|| '.' || '' || last_name as  "inicial + nombre",create_date as "fecha de creacion"
FROM Customer
```

# Comando JOIN


Los JOIN permiten unir tablas para hacer consultas más complejas. Hay tres tipos principales de JOIN: INNER JOIN, LEFT OUTER JOIN y RIGHT OUTER JOIN.

- Inner Join: devuelve los registros que corresponden a cada tabla solo si hay una relación entre ellos.
- Left Outer Join: devuelve todos los registros de la tabla de la izquierda y los registros de la derecha que cumplen con la condición especificada.
- Right Outer Join: devuelve todos los registros de la tabla de la derecha y los registros de la izquierda que cumplen con la condición especificada.

Para realizar un JOIN, se utiliza la cláusula ON, que especifica la condición para unir las tablas.

Los JOIN también se pueden combinar con otras cláusulas, como WHERE, GROUP BY y ORDER BY, para obtener resultados más específicos.

**Tabla 1 || intersection|| Tabla 2**

Left Outer|| Inner || Right outer

_Tabla izquierda_ Inner Join _tabla derecha_ ON (condicion)

_Tabla izquierda_ LEFT OUTER JOIN _tabla derecha_ ON (condicion)

_Tabla izquierda_ RIGTH OUTER JOIN _tabla derecha_ ON (condicion)

Tabla izquierda NATURAL JOIN _tabla derecha_

en el natural join automáticamente se igualan los atributos con el mismo nombre

```sql
SELECT first_name,Last_name
From custimer C INNER JOIN Rental R 
ON (C.customer_id=R.customer_id)
```

```sql
--los nombres de los clientes que han rentado peliculas o que nunca lo han hecho
SELECT first_name||''||last_name AS 'Nombre'
FROM customer C LEFT OUTER JOIN Rental R
ON (C.custumer_id=R.customer_id)
-- desplegar la fecha de realizacion de alquier
SELECT firs_name ||''||last_name as "nombre",rental_date
FROM customer C LEFT OUTER JOIN Rental R
ON (C.custumer_id=R.customer_id)
where rental_date as 
--cuales son los alquieres que se han realizados a los clientes con registro de clientes o no
--desplegar el id de alquiler y el nombre del cliente  en caso de que nose haya registrado el cliente
---en caso de que nose haya registrado desplegar el null 
SELECT rental_id,first_name||''|| SUBSTRING(last_name,1,1)||'.' AS "nombre"
FROM customer C RIGHT OUTER JOIN Rental R
ON (C.customer_id=R.customer_id)
WHERE C.Customer_id IS NULL
-- Despligue los nombres de los clientes que han realizados algun alquiler junti a la fecha de realizaacion
SELECT first_name ||''|| last_name AS "nombre",rental_date"fecha de alquiler"
FROM Customer C INNER JOIN rental R 
ON (C. customer_id = R.customer_id)
WHERE C.customer_id IS NULL OR R.customer_id IS NULL
-- cuales osn los mmontos de los pagos que ha realizados la cliente susan 
SELECT amount ,R.rental_id
FROM payment P INNER JOIN rental R
ON P.rental_id=R.rental_id)
INNER JOIN customer C 
ON (R.customer_id=C.costumer_id) 
WHERE first_name='susan'
```

|Customer|Rental|Payment|
|---|---|---|
|customer_id (pk)|rental_id (pk)|rental_id(fk)|
||customer_id(fk)||

siempre se realzaciona una pk(primary key) con una fk (foreign key)

```sql
-- en que pelicula ha actuado grace mostel 
select title
FROM film F INNER JOIN film_actor FA ON f.film_id= fa.film_id 
INNER JOIN actor A ON (FA.actor_id= A.actor_id) 
WHERE first_name='grace' AND last_name='mostel'
-- la segunda opcion 
select title, first_name,last_name 
FROM film F INNER 
JOIN film_actor FA ON f.film_id= fa.film_id 
INNER JOIN actor A ON (FA.actor_id= A.actor_id) 
WHERE first_name='grace'
```
[[ejemplos]]
[[ejercicios]]
