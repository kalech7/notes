La primera mitigacion deben estar desabilitados 

```cisco
int range f0/2-24
shut

int
sw mode access
switchport port-security
```
el portsecurity no se pueden usar en puertos troncales, ethernetchannel deben estar en modo access
a las puertos no se le asigna ip solo a interfaces
solo aprende una direccion mac si hay dos solo la primera 
se  produce una violacion cuando no se cumple con la configuaricon  y el switch dehabilita el puerto

```cisco
sh port-security int 
```

se pueden cambiar los parametros con 
```cisco
sw port-security (aging)
				 (mac-address)
				 (maximum)
				 (violation)
sw port-security mac-address sticky (hace que aprenda de manera dinamica la dir mac)
```
