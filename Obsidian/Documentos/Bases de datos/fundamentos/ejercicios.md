Revisar [[Subconsultas]] y los [[ejemplos]] que se hicieron antes 
```sql
--- cuales son los tributos de las peliculas que nunca han sido alquiladas 
SELECT title
FROM film
EXCEPT
FROM  film F 
INNER JOIN inventory I ON (F.film_id=I.film_id)
INNER JOIN  rental R ON (I.inventory_id=R.inventory_id)

```
Revisar [[Fechas]]

```sql
SELECT DATE ('2021-01-01')+15
SELECT CURRENT_DATE
SELECT RPAD(nombre_prod,15,'.')
FROM productos
--- cuales son los nombres de los productos comprados durante el año 2020?
SELECT nombre_prod
FROM productos P, fecha_fact
INNER JOIN  items I ON (I.id_producto=P.id_producto)
INNER JOIN facturas F ON (I.num_factura=F.num_factura)
WHERE Date_part('year',fecha_fact)=2020

--- cuando fue la ultima compra que hizo la señora 'erazo'
SELECT fecha_fact,nombre_cli
FROM facturas F
INNER JOIN clientes C ON(C.id_cliente =F.id_cliente )
WHERE  nombre_cli LIKE '% Erazo'
ORDER BY fecha_fact DESC
LIMIT 1
--- en que viven lugares viven los clientes que no ham comprado nada el año 2020
SELECT nombre_cli,dir_cli
FROM clientes

	EXCEPT

SELECT nombre_cli,dir_cli
FROM clientes C 
INNER JOIN facturas F ON (C.id_cliente=F.id_cliente)
WHERE DATE_PART('YEAR',fecha_fact)=2020

---en que meses del año 2020 se ha vendido shampoo
SELECT DATE_PART ('MONTH',fecha_fact)
FROM productos P
INNER JOIN items I ON (P.id_producto=I.id_producto)
INNER JOIN facturas F ON (I.num_factura=F.num_factura)
WHERE LOWER (nombre_prod) LIKE '%shampoo%'
--- CUANROS SHAMPPOS Mensuales se han vendido en el 2020
SELECT SUM(cant),DATE_PART('MONTH',fecha_fact)
FROM productos P
INNER JOIN items I ON(P.id_producto=I.id_producto)
INNER JOIN facturas F ON (I.num_factura=F.num_factura)
WHERE LOWER(P.nombre_prod ) LIKE ('%shampoo')
AND DATE_PART('YEAR ',fecha_fact)=2020
GROUP BY DATE_PART('MONTH',fecha_fact)
--- en que mes se vendieron 100 shampoos
SELECT DATE_PART ('MONTH',fecha_fact)
FROM productos P
INNER JOIN items I ON (P.id_producto=I.id_producto)
INNER JOIN facturas F ON (I.num_factura=F.num_factura)
WHERE cant=100 AND nombre_prod='shampoo'
-- cuantos dias han transcurrido desde la ultima ves que se compro shampoo 
SELECT CURRENT_DATE-fecha_fact
FROM facturas F
INNER JOIN items I ON (I.num_factura=F.num_factura)
INNER JOIN productos P ON (P.id_producto=I.id_producto)
WHERE LOWER (nombre_prod)='shampoo'
ORDER BY dias
LIMIT 1
--cuantos productos se han cendido a partir del 20/dic/2020 que han sido 
--provistos por los andes
SELECT COUNT (*)
from facturas F
items I
productos P
INNER JOIN items I ON (I.num_factura=F.num_factura)
INNER JOIN productos P ON (I.id_producto=P.id_producto)
INNER JOIN porveedores V ON (P.id_proveedor =V.id_proveedor)
WHERE fecha_fact> DATE('2020-12-20') AND nombre_prov LIKE 'Los an%'
--- cual es el nombre del producto que mas se ha vendido en enero del 2020
SELECT nombre_prod,SUM(cant)"SUMA"
FROM productos P
INNER JOIN items I ON(P.id_producto=I.id_producto)
INNER JOIN facturas F ON (I.num_factura=F.num_factura)
WHERE DATE_PART('MONTH',fecha_fact)=01
AND DATE_PART('YEAR',fecha_fact)=2020
GROUP BY nombre_prod
ORDER BY suma DESC
limit 1

```
