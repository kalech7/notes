Ejemplos sin usar conjuntos 
```sql
--cuales son los nnombre de los clientes que han comprado en la tienda 1 y que vieven en la direccion 55
SELECT SUBSTRING (c.first_name,1,1)||'.'||c.last_name
FROM customer C ,rental R, staff S
WHERE C.customer_id =R.customer_id
AND R.staff_id=S.staff_id
AND  S.store_id=1
AND c.address_id=55
--cuales son los nnombre de los clientes que han comprado en la tienda 1 y que no vieven en la direccion 55
SELECT SUBSTRING (c.first_name,1,1)||'.'||c.last_name
FROM customer C ,rental R, staff S
WHERE C.customer_id =R.customer_id
AND R.staff_id=S.staff_id
AND  S.store_id=1
AND c.address_id!=55
--cuales son los nnombre de los clientes que han comprado en la tienda 1 y que vieven en la direccion 55
SELECT SUBSTRING (c.first_name,1,1)||'.'||c.last_name
FROM customer C ,rental R, staff S
WHERE C.customer_id =R.customer_id
AND R.staff_id=S.staff_id
AND  S.store_id=1


```
Ejemplo usando conjuntos 
es mas legible usando codigo en conjuntos 
```sql
INTERSECT
SELECT SUBSTRING (c.first_name,1,1)||'.'||c.last_name
FROM customer C ,rental R, staff S
WHERE C.customer_id =R.customer_id
AND R.staff_id=S.staff_id
AND c.address_id=55
--cuales son los nnombre de los clientes que han comprado en la tienda 1 y que vieven en la direccion 55
SELECT SUBSTRING (c.first_name,1,1)||'.'||c.last_name
FROM customer C ,rental R, staff S
WHERE C.customer_id =R.customer_id
AND R.staff_id=S.staff_id
AND  S.store_id=1

EXCEPT 
SELECT SUBSTRING (c.first_name,1,1)||'.'||c.last_name
FROM customer C ,rental R, staff S
WHERE C.customer_id =R.customer_id
AND R.staff_id=S.staff_id
AND c.address_id=55
```

```sql
-- cuales son los cliuentes que han alquilado en la tienda 1 y que viven en una de los ciudades:Oyo,Namibe,Jelets y 
SELECT SUBSTRING ( C.first_name,1,1)||'.'||c.last_name
FROM Customer C,Rental R
WHERE C.customer_id =R.customer_id
AND store_id=1
INTERSECT 
SELECT SUBSTRING ( C.first_name,1,1)||'.'||c.last_name
FROM customer C,address A,city T
Where C.address_id= A.address_id
AND A.city_id=T.city_id
AND city IN ('Oyo','Namibe','Jelets ','Pune')
```
Solo sirve con inner join igualar clave primaria con clave extranjera

## Notas relacionadas
- [[Comandos]]
- [[Subconsultas]]
- [[ejercicios]]
