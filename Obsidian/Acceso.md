Politicas (lenguaje natural)
ACM (modelo de control de acceso) roles RBAC<rol, accion, objeto> , discrecional  DAC <sujeto,accion,objeto>, mandatorio MAO <sujeto, accion, nivel>

Mecanismo de autorizacion (sintaxis y semantica)


en el json se tiene esta estructura 

effect: Allow/Deny
action: S3 put object S3 get object
resource:
principal: