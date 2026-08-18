* es la restriccion selectiva del acceso de un bien o un sistema o recurso de red 
* proteje la informacion del bien determinando quien puede acceder a que 
* usa identificacion ,authentication y authorization para restringir o garantizar acceso a un bien o recurso especifico 
![[Pasted image 20241014062614.png]]
es un metodo por el cual se limita el acceso a los recursos de la organizacion para los usuarios un aspecto crucial de implentar control de acceso es para mantener integridad confidencialidad y disponibilidad de la inforacion 
## pasos
1) el usuario provee sus crendecuales mientras se logea al sistema 
2) el sistema valida el usuario con la database en base de las credenciales proporcionadas
3) cuando la identifacion es exitosa el sistema da al usuario acceso al sistema
4) el sistema luego permite al usuario realizar solamente operaciones a las cuales solo esta destinado hacer 
## terminologias
- sujeto 
se refiere a un usuario en particular o processo que quiere acceder al recurso
-  objeto
se refiere a un recurso especifico que el usuario quiere el acceso como un archivo o una pieza de hardware 
- reference monitor
chequea si la regla de control de acceso para restriciones especificas
- operation
representa la accion tomanda por un sujeto en un objeto 
![[Pasted image 20241014063559.png]]
## principios
### separation of duties (SoD)
- Implica un desglose del proceso de autorización en varios pasos.
- En cada paso se asignan diferentes privilegios a los sujetos individuales que solicitan un recurso.
- Esto garantiza que ningún individuo tenga los derechos de autorización para realizar todas las funciones y, al mismo tiempo, niega el acceso a todos los objetos a un solo individuo.
### need to know
segun el principio de control de acceso, se proporciona acceso unicamente a la informacion que se requiere para realizar una tarea especifica 
### principle of least privilege (POLP)
 - El principio del mínimo privilegio amplía el principio de necesidad de saber para brindar acceso a un sistema
 - POLP cree en brindar a los empleados un acceso que se ajuste a la necesidad de saber, es decir, ni más ni menos
- Ayuda a una organización al protegerla de comportamientos maliciosos, logrando una mejor estabilidad y seguridad del sistema
## modelos de control de acceso
son estandares los cuales proveen un prederminado framework para implementar el nivel necesario de control de acceso.
### mandatory access control (mac)
- solo el administrador o el owner tiene los derechos para asignar privilegios 
- no permite que el usuario final decida quien accede a la informacion 
### discretionary access control (dac)
- el usuario final tiene acceso completo a la informacion que posee 
### role-based access control (rbac)
- permiso para asignar basado en roles 
### rule-based access control (rb-rbac)
* permisos son asignados para el rol dinamico del usuario basado en un conjunto de reglas definadas del administrador 
## gestion de acceso
autorizacion
autenticacion autorizacion 
## administracion de identidad
repositorio de identidad 
administracion de identidad 
