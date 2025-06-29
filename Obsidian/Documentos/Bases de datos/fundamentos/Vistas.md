muestra solamente aquello que se le permita 
[[Comandos]]

```sql
CREATE VIEW facturas_clientes
SELECT nombre_cli, num_factura,fecha_fact
FROM clientes C
INNER JOIN facturas F ON(C.id_cliente=F.id_cliente)
```
no es una tabla lo que sea crea es una vista es solo una coleccion de los elementos 

```sql
SELECT*
FROM facturas_clientes
WHERE nombre_cli LIKE '%'
```
hay vistas especiales que se guardan como tablas y se denominan como vistas materializadas

```sql
CREATE MATERIALIZED VIEW prod_prov
AS
SELECT nombre_prod, precio_unit,nombre_prov
FROM productos P
INNER JOIN proveedores V ON (P.id_proveedor = v.id_proveedor )

```
la vista materazliada crea como una foto en el momento que sea creo en ese instante no cambia se mantiene en el tiempo ni cambiar dentro de la vista nada es mantiene tal cual

