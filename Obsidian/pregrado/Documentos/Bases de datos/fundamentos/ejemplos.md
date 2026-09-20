> [!info] Explicación
> En SQL, existen múltiples formas de obtener el mismo resultado. Se pueden resolver consultas utilizando operaciones basadas en relaciones lógicas (`JOIN`, condiciones lógicas múltiples en el `WHERE`) o mediante la teoría de conjuntos (`INTERSECT`, `EXCEPT`, `UNION`). Esta nota contrasta ambas formas de escribir consultas usando ejemplos prácticos.

Ejemplos sin usar conjuntos:
```sql
-- ¿Cuáles son los nombres de los clientes que han comprado en la tienda 1 y que viven en la dirección 55?
SELECT SUBSTRING(c.first_name, 1, 1) || '.' || c.last_name
FROM customer C, rental R, staff S
WHERE C.customer_id = R.customer_id
AND R.staff_id = S.staff_id
AND S.store_id = 1
AND c.address_id = 55;

-- ¿Cuáles son los nombres de los clientes que han comprado en la tienda 1 y que NO viven en la dirección 55?
SELECT SUBSTRING(c.first_name, 1, 1) || '.' || c.last_name
FROM customer C, rental R, staff S
WHERE C.customer_id = R.customer_id
AND R.staff_id = S.staff_id
AND S.store_id = 1
AND c.address_id != 55;

-- ¿Cuáles son los nombres de los clientes que han comprado en la tienda 1? (Consulta base sin el filtro de dirección)
SELECT SUBSTRING(c.first_name, 1, 1) || '.' || c.last_name
FROM customer C, rental R, staff S
WHERE C.customer_id = R.customer_id
AND R.staff_id = S.staff_id
AND S.store_id = 1;
```

> [!info] Explicación de Conjuntos
> El uso de operaciones de conjuntos (`INTERSECT` y `EXCEPT`) puede hacer que las consultas sean más declarativas y fáciles de leer cuando se combinan resultados independientes. 
> - **INTERSECT** devuelve solo los registros que aparecen en ambos conjuntos de resultados.
> - **EXCEPT** devuelve los registros del primer conjunto que no están presentes en el segundo conjunto.

Ejemplo usando conjuntos:
Suele ser más legible usar código estructurado en conjuntos para cruzar lógicas complejas:

```sql
-- INTERSECT: Clientes que han comprado en la tienda 1 Y viven en la dirección 55
SELECT SUBSTRING(c.first_name, 1, 1) || '.' || c.last_name
FROM customer C, rental R, staff S
WHERE C.customer_id = R.customer_id
AND R.staff_id = S.staff_id
AND S.store_id = 1

INTERSECT

SELECT SUBSTRING(c.first_name, 1, 1) || '.' || c.last_name
FROM customer C, rental R, staff S
WHERE C.customer_id = R.customer_id
AND R.staff_id = S.staff_id
AND c.address_id = 55;

-- EXCEPT: Clientes que han comprado en la tienda 1, EXCEPTO los que viven en la dirección 55
SELECT SUBSTRING(c.first_name, 1, 1) || '.' || c.last_name
FROM customer C, rental R, staff S
WHERE C.customer_id = R.customer_id
AND R.staff_id = S.staff_id
AND S.store_id = 1

EXCEPT 

SELECT SUBSTRING(c.first_name, 1, 1) || '.' || c.last_name
FROM customer C, rental R, staff S
WHERE C.customer_id = R.customer_id
AND R.staff_id = S.staff_id
AND c.address_id = 55;
```

```sql
-- ¿Cuáles son los clientes que han alquilado en la tienda 1 y que viven en una de las ciudades: Oyo, Namibe, Jelets y Pune?
SELECT SUBSTRING(C.first_name, 1, 1) || '.' || c.last_name
FROM Customer C, Rental R
WHERE C.customer_id = R.customer_id
AND store_id = 1

INTERSECT 

SELECT SUBSTRING(C.first_name, 1, 1) || '.' || c.last_name
FROM customer C, address A, city T
Where C.address_id = A.address_id
AND A.city_id = T.city_id
AND city IN ('Oyo', 'Namibe', 'Jelets', 'Pune');
```
Solo sirve con INNER JOIN para igualar clave primaria con clave extranjera al momento de cruzar las tablas de forma implícita.

## Notas relacionadas
- [[Comandos]]
- [[Subconsultas]]
- [[ejercicios]]
