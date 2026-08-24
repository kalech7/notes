DML insert-delete -update
DDL Create-drop-alter
DCL Create Roles,users
		Eliminar roles de usarios 
		GRANT 
		REVOQUE
		se crea el superuser -> create user 
											-> grant       -> privilegios  
											-> revoke (quita privilegios que dio el superuser)
## DCL 

``` sql
CREATE USER epn
WITH PASSWORD "epn"

GRANT SELECT,UPDATE ,DELETE
ON clientes
TO epn
SELECT * FROM productos 
INSERT INTO productos
VALUES()
```

## Notas relacionadas
- [[Comandos]]
- [[Principales tipo de datos]]
- [[Insertar datos]]
- [[Vistas]]
- [[Transaccion]]
