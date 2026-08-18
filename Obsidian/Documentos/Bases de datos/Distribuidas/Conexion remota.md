local
ip:172.31.103.80
nombre:Frappe-lap

remoto
ip: 172.31.103.105
nombre:1-20-03-E005-23


```sql
create user achavez identified by achavez
default tablespace users 
temporary tablespace temp
profile default;
```


para borrar usuario 

```sql
drop user (nombre) cascade
```

damos privilegios para que se conecten a la maquina 

```sql
grant connect,resource to achavez
alter user achavez quota unlimited on users;
```
string de conexion 
![[Pasted image 20231209113703.png]]
ponemos el nombre de la maquina destino
comando para ver estatus del proceso listener

```
lsnrctl status
```
para ingresar a la base de datos

```
sqlplus /as sysdba
```

para ver el nombre de la base

```sql
show parameters service
```
