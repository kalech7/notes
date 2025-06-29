es un conjunto de operaciones que se realizan como una unica unidad atomica de trabajo
las transacciones debes ser atomicas consistentes,aisladas y duraderas con las cuatro propiedades  ACID (**_Atomicity, Consistency, Isolation y Durability_**)
## Propiedades ACID
1) **_Atomicidad_** todas las operaciones en una transaccion se realizan como una sola unidad atomica si alguna operacion falla todas las opereaciones se deshacen
2) **_Consistency_**  lleva a la base de datos desde un estado consistente a otro estado consistente debe cumplir todas las restricciones de integridad refererencial y otras
3) **_Isolation_** Controla como y cuando los cambios producidos por una operacion se hacen visibles para las demas operaciones concurrentes Casa transaccion se ejecuta en un entorno aislado lo que significa que no puede interferir con otras transacciones en ejecucion 
   concurrencia acceso en el mismo tiempo de usuarios
4) **_Durability_** cuando la transaccion con exito los cambios realizados por esa transaccion deben ser permanentes y sobrevivir a cualquier fallo del sistema

commit acepta todo lo ejecutado 
undo deshacer lo hecho 
en c#
try 
catch
save guarda lo hecho hasta cierto punto(puntos seguros) sin afectar a la consistencia de la base de datos

