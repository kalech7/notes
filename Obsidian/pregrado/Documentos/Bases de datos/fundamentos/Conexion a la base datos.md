[[Diagrama conexion base de datos.excalidraw]]
Para hacer una conexion a una base de datos postgreSQL con python
se necesita la libreria ***pg8000 o Psyco2pg*** que permite conectarse con el comando especifiando el usuario la contra el ervidor el puerto y la base de datos:

```python
import pg8000
import Psyco2pg
connect(user="",host="",database="",port="",password="")
```
la base de datos permanece abierta hasta que se decida cerrarse de forma explicita 

* Las filas del cursos se manipulan con una estructoura de repeticion 
* Una vez terminada la manipulacion de datos se cierra la conexion 
Se crea el cursor el cual vienen los datos 

```python 
strComm="SELECT * FROM clientes"
cur=conn.cursor()
datos= cur.execute(strComm)
for fila in datos:
	print(fila)
cur.close()
conn.close()
```
[[ejemplos]]
[[SQL]]
data control access

## Notas relacionadas
- [[SQL]]
- [[Comandos]]
- [[Conexion remota]]
- [[SQL data adapter]]
