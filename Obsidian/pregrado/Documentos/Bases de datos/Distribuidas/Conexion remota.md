[[Diagrama conexion base de datos.excalidraw]]
Para hacer una conexión a una base de datos PostgreSQL con Python, se necesita la librería ***pg8000*** o ***psycopg2***. Estas librerías permiten establecer la conexión mediante un comando específico, en el cual se debe indicar el usuario, la contraseña, el servidor, el puerto y el nombre de la base de datos:

```python
import pg8000
import psycopg2
# Ejemplo genérico de conexión
connect(user="", host="", database="", port="", password="")
```

La conexión a la base de datos permanece abierta hasta que se decida cerrarla de forma explícita.

* Las filas obtenidas mediante el cursor se manipulan utilizando una estructura de repetición (como un bucle `for`).
* Una vez terminada la manipulación de los datos, es indispensable cerrar la conexión para liberar recursos.
* Primero se crea el cursor, a través del cual se obtienen e iteran los datos devueltos por la consulta.

```python 
strComm = "SELECT * FROM clientes"
cur = conn.cursor()
datos = cur.execute(strComm)
for fila in datos:
	print(fila)

# Cierre explícito de recursos
cur.close()
conn.close()
```

> [!info] Explicación
> **¿Qué es un cursor?** Un cursor en bases de datos es un objeto de control que permite recorrer fila por fila los resultados de una consulta SQL. Es como un puntero o un iterador. 
> **¿Por qué cerrar la conexión?** Las bases de datos tienen un límite máximo de conexiones simultáneas. Si no cierras las conexiones con `.close()`, podrías agotar ese límite y bloquear temporalmente el acceso a la base de datos (connection leak).

[[ejemplos]]
[[SQL]]
Data Control Access (DCL)

## Notas relacionadas
- [[SQL]]
- [[Comandos]]
- [[Conexion remota]]
- [[SQL data adapter]]
