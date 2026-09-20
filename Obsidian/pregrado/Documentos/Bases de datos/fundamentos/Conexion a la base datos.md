[[Diagrama conexion base de datos.excalidraw]]

> [!info] Explicación
> Para interactuar con una base de datos PostgreSQL desde Python, necesitamos usar librerías específicas que funcionen como adaptadores de base de datos (drivers). Estas librerías permiten establecer una conexión de red con el servidor de la base de datos enviando las credenciales adecuadas, y luego facilitan el envío de consultas SQL y la recuperación de sus resultados.

Para hacer una conexión a una base de datos PostgreSQL con Python se necesita la librería **pg8000** o **psycopg2** (Psyco2pg), que permite conectarse a través de un comando especificando el usuario, la contraseña, el servidor (host), el puerto y el nombre de la base de datos:

```python
import pg8000
import psycopg2 # Librería psycopg2

# Ejemplo general de conexión
conn = psycopg2.connect(user="", host="", database="", port="", password="")
```
La base de datos permanece abierta hasta que se decida cerrarla de forma explícita.

* Las filas del cursor se manipulan con una estructura de repetición (como un bucle `for`).
* Una vez terminada la manipulación de datos, es fundamental cerrar el cursor y la conexión para liberar recursos.
* Se crea el cursor, el cual funciona como un canal por el que vienen los datos desde la base de datos a nuestra aplicación.

```python 
strComm = "SELECT * FROM clientes"
cur = conn.cursor()
cur.execute(strComm)
datos = cur.fetchall() # o iterar directamente sobre cur

for fila in datos:
	print(fila)

cur.close()
conn.close()
```
[[ejemplos]]
[[SQL]]
Data control access

## Notas relacionadas
- [[SQL]]
- [[Comandos]]
- [[Conexion remota]]
- [[SQL data adapter]]
