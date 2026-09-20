> [!info] Explicación de INSERT
> La sentencia `INSERT INTO` se utiliza para agregar nuevos registros (filas) a una tabla en una base de datos. Puedes especificar las columnas en las que deseas insertar datos, lo cual es muy útil si la tabla tiene columnas que aceptan valores nulos o que tienen un valor por defecto.

```sql
-- Sintaxis básica para insertar datos
INSERT INTO tabla (columnas_que_quiero_incluir)  
VALUES (valores_que_tienen_las_columnas_separados_con_coma);
```

## Constraint (Restricciones)

> [!info] Explicación
> Los `Constraints` (restricciones) son reglas aplicadas a las columnas de una tabla para limitar el tipo de datos que pueden insertarse. Esto asegura la exactitud y confiabilidad de los datos en la base de datos (Integridad de datos).

Algunas restricciones comunes son:
```sql
NOT NULL -- Asegura que la columna no pueda tener un valor nulo.
UNIQUE   -- Asegura que todos los valores en la columna sean diferentes (no se repitan).
```
[[SQL]]

## Notas relacionadas
- [[Comandos]]
- [[Principales tipo de datos]]
- [[Transaccion]]
