Revisar [[Subconsultas]] y los [[ejemplos]] que se hicieron antes 

> [!info] Explicación
> Este documento contiene una serie de ejercicios prácticos utilizando SQL. Se incluyen técnicas como operaciones de conjuntos (`EXCEPT`), manejo de fechas (`DATE_PART`, `CURRENT_DATE`), funciones de agregación (`SUM`, `COUNT`) y limitación de resultados (`LIMIT`).

```sql
--- ¿Cuáles son los atributos (títulos) de las películas que nunca han sido alquiladas?
SELECT title
FROM film

EXCEPT

SELECT title
FROM film F 
INNER JOIN inventory I ON (F.film_id = I.film_id)
INNER JOIN rental R ON (I.inventory_id = R.inventory_id);
```

Revisar [[Fechas]]

```sql
-- Operaciones básicas
SELECT DATE('2021-01-01') + 15;
SELECT CURRENT_DATE;

-- Rellenar con caracteres a la derecha
SELECT RPAD(nombre_prod, 15, '.')
FROM productos;

--- ¿Cuáles son los nombres de los productos comprados durante el año 2020?
SELECT nombre_prod
FROM productos P
INNER JOIN items I ON (I.id_producto = P.id_producto)
INNER JOIN facturas F ON (I.num_factura = F.num_factura)
WHERE Date_part('year', fecha_fact) = 2020;

--- ¿Cuándo fue la última compra que hizo la señora 'Erazo'?
SELECT fecha_fact, nombre_cli
FROM facturas F
INNER JOIN clientes C ON (C.id_cliente = F.id_cliente)
WHERE nombre_cli LIKE '% Erazo'
ORDER BY fecha_fact DESC
LIMIT 1;

--- ¿En qué lugares viven los clientes que no han comprado nada en el año 2020?
SELECT nombre_cli, dir_cli
FROM clientes

EXCEPT

SELECT nombre_cli, dir_cli
FROM clientes C 
INNER JOIN facturas F ON (C.id_cliente = F.id_cliente)
WHERE DATE_PART('YEAR', fecha_fact) = 2020;

--- ¿En qué meses del año 2020 se ha vendido shampoo?
SELECT DATE_PART('MONTH', fecha_fact)
FROM productos P
INNER JOIN items I ON (P.id_producto = I.id_producto)
INNER JOIN facturas F ON (I.num_factura = F.num_factura)
WHERE LOWER(nombre_prod) LIKE '%shampoo%' 
AND DATE_PART('YEAR', fecha_fact) = 2020; -- Corregido para incluir la validación del año 2020

--- ¿Cuántos shampoos mensuales se han vendido en el 2020?
SELECT SUM(cant), DATE_PART('MONTH', fecha_fact)
FROM productos P
INNER JOIN items I ON (P.id_producto = I.id_producto)
INNER JOIN facturas F ON (I.num_factura = F.num_factura)
WHERE LOWER(P.nombre_prod) LIKE '%shampoo%'
AND DATE_PART('YEAR', fecha_fact) = 2020
GROUP BY DATE_PART('MONTH', fecha_fact);

--- ¿En qué mes se vendieron 100 shampoos en una factura?
SELECT DATE_PART('MONTH', fecha_fact)
FROM productos P
INNER JOIN items I ON (P.id_producto = I.id_producto)
INNER JOIN facturas F ON (I.num_factura = F.num_factura)
WHERE cant = 100 AND LOWER(nombre_prod) = 'shampoo';

-- ¿Cuántos días han transcurrido desde la última vez que se compró shampoo?
SELECT CURRENT_DATE - fecha_fact AS dias
FROM facturas F
INNER JOIN items I ON (I.num_factura = F.num_factura)
INNER JOIN productos P ON (P.id_producto = I.id_producto)
WHERE LOWER(nombre_prod) LIKE '%shampoo%'
ORDER BY dias ASC
LIMIT 1;

-- ¿Cuántos productos se han vendido a partir del 20/dic/2020 que han sido provistos por 'Los Andes'?
SELECT COUNT(*)
FROM facturas F
INNER JOIN items I ON (I.num_factura = F.num_factura)
INNER JOIN productos P ON (I.id_producto = P.id_producto)
INNER JOIN proveedores V ON (P.id_proveedor = V.id_proveedor)
WHERE fecha_fact > DATE('2020-12-20') AND nombre_prov LIKE 'Los An%';

--- ¿Cuál es el nombre del producto que más se ha vendido en enero del 2020?
SELECT nombre_prod, SUM(cant) AS "SUMA"
FROM productos P
INNER JOIN items I ON (P.id_producto = I.id_producto)
INNER JOIN facturas F ON (I.num_factura = F.num_factura)
WHERE DATE_PART('MONTH', fecha_fact) = 1
AND DATE_PART('YEAR', fecha_fact) = 2020
GROUP BY nombre_prod
ORDER BY SUMA DESC
LIMIT 1;

```

## Notas relacionadas
- [[Subconsultas]]
- [[ejemplos]]
- [[Comandos]]
