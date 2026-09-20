[[Comandos]]

> [!info] Explicación
> El manejo de fechas en SQL es crucial para filtrar registros en periodos de tiempo, calcular diferencias o transformar información temporal. Dependiendo del gestor de base de datos (PostgreSQL, MySQL, SQL Server), las funciones exactas pueden variar, pero la mayoría soportan operaciones aritméticas simples (sumar/restar días) y extracción de partes específicas de la fecha.

```sql
fecha + integer       -- Incremento en días (devuelve una fecha futura)
fecha - integer       -- Decremento en días (devuelve una fecha pasada)
DATE('string con el formato de fecha') -- Transforma un texto (string) en un tipo de dato fecha
CURRENT_DATE          -- Devuelve la fecha actual del sistema
fecha1 - fecha2       -- Calcula la diferencia y retorna el número (#) de días entre ambas
fecha1 > fecha2       -- Condicional lógico: retorna True o False si fecha1 es posterior a fecha2
DATE_PART('YEAR', fecha)  -- Extrae y retorna el año de la fecha indicada
DATE_PART('MONTH', fecha) -- Extrae y retorna el mes de la fecha indicada
DATE_PART('DAY', fecha)   -- Extrae y retorna el día de la fecha indicada
```

> [!info] Ejemplos de uso
> - Para saber hace cuántos días ocurrió un registro: `CURRENT_DATE - fecha_registro`
> - Para filtrar registros del año en curso: `WHERE DATE_PART('YEAR', fecha) = 2023`

## Notas relacionadas
- [[Comandos]]
- [[Principales tipo de datos]]
- [[Transaccion]]
