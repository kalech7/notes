Cisco proporciona HSRP y HSRP para IPv6 como una forma de evitar la pérdida de acceso externo a la red si falla el router predeterminado.
Es el protocolo FHRP exclusivo de Cisco diseñado para permitir la conmutación por falla transparente de los dispositivos IPv4 de primer salto.
HSRP se utiliza en un grupo de routers para seleccionar un dispositivo activo y un dispositivo de reserva. 
para la version 1 la mac address: 0000.0c07.acXX
para la version 2 la mac address: 0000.0c9f.fXXX (en esta version se puede usar para los mensajes de hello holdtime en ms) 
**En un grupo de interfaces de dispositivo:** 
<span style="background:#d3f8b6"> El dispositivo activo </span> es aquel que se utiliza para enrutar paquetes.
<span style="background:#d2cbff">El dispositivo de reserva </span>es el que toma el control cuando falla el dispositivo activo o cuando se cumplen condiciones previamente establecidas.
La función del router de suspensión del HSRP es controlar el estado operativo del grupo de HSRP y asumir rápidamente la responsabilidad de reenvío de paquetes si falla el router activo.
## Prioridad e Intento de Prioridad del HSRP
El rol de los routers activos y de reserva se determina durante el proceso de elección del HSRP.
De manera predeterminada, el router con la dirección IPv4 numéricamente más alta se elige como router activo

 ***Prioridad HSRP***
La prioridad HSRP se puede utilizar para determinar el router activo. El router con la prioridad HSRP más alta será el router activo. De manera predeterminada, la prioridad HSRP es 100.
Si las prioridades son iguales, el router con la dirección IPv4 numéricamente más alta es elegido como router activo.
para configuar utilice el comando de interfaz el rango va de  0 a 255
```cisco
standby priority
```

***Preferencias HSRP***
De forma predeterminada, después de que un router se convierte en el router activo, seguirá siendo el router activo incluso si otro router está disponible en línea con una prioridad HSRP más alta.
Para forzar un nuevo proceso de elección HSRP a tener lugar cuando un router de mayor prioridad entra en línea, la preferencia debe habilitarse mediante el comando

```cisco
standby preempt
```
 El intento de prioridad es la capacidad de un router HSRP de activar el proceso de la nueva elección
 El intento de prioridad solo permite que un router se convierta en router activo si tiene una prioridad más alta. 
 Un router habilitado para intento de propiedad, con una prioridad equivalente pero una dirección IPv4 más alta, no desplazará la prioridad de un router activo.
 ![[Pasted image 20230822161220.png]]
 El R1 se configuró con la prioridad de HSRP de 150 mientras que el R2 tiene la prioridad de HSRP predeterminada de 100. El intento de prioridad está habilitado en el R1. Con una prioridad más alta, el R1 es el router activo y el R2 es el router de reserva.
  Debido a un corte de energía que solo afecta al R1, el router activo ya no está disponible y el router de reserva R2 asume el rol de router activo. Después de que se restaura la energía, el R1 vuelve a estar en línea. Dado que R1 tiene una prioridad más alta y el intento de prioridad se encuentra habilitado, forzará un nuevo proceso de elección. R1 reanudará su rol de router activo y el R2 volverá al rol de router de reserva.
  
**Nota**: Si el intento de prioridad está desactivado, el router que arranque primero será el router activo si no hay otros routers en línea durante el proceso de elección.
  
## Estados y Temporizadores de HSRP
Un router puede ser el router HSRP activo responsable de la devolución del tráfico al segmento, donde el router puede ser un router HSRP pasivo de reserva, listo para asumir rol activo si falla el router activo. 
Cuando se configura una interfaz con HSRP o se habilita primero con una configuración HSRP existente, el router envía y recibe paquetes de saludo del HSRP para comenzar el proceso de determinar qué estado asumirá en el grupo HSRP.

| Estado de HSRP | Descripcion |
| -------------- | ----------- |
| **Inicial**        |     ingresa a través de un cambio de configuración o cuando una interfaz está disponible en primer lugar.       |
| **Aprendizaje**    |    El router no ha determinado la dirección IP virtual ha visto un mensaje de saludo desde el router activo. En este estado, el router espera para escuchar al router activo.         |
| **Escucha**        |      El router conoce la dirección IP virtual, pero no es el router activo ni el router en espera. Escucha los mensajes de saludo de esos routers.       |
| **Hablar**         |      El router envía mensajes de saludo periódicos y participa activamente en la elección del router activo y/o en espera.       |
| **En espera**               |      El router es candidato a convertirse en el próximo router activo y envía mensajes de saludo periódicos.       |

El router HSRP activo y el de reserva envían paquetes de saludo a la dirección de multidifusión del grupo HSRP cada 3 segundos, de forma predeterminada. v1: 224.0.02 v2: 224.0.0.102
El router de reserva se convertirá en activo si no recibe un mensaje de saludo del router activo después de 10 segundos. Puede bajar estas configuraciones del temporizador para agilizar las fallas o el intento de prioridad. Sin embargo, para evitar el aumento del uso de la CPU y cambios de estado de reserva innecesarios, no configure el temporizador de saludo a menos de 1 segundo o el temporizador de espera a menos de 4 segundos.

## Comandos
Router 1
```cisco
int (interfaz del router)
standby (grupo) ip (ip virtual)
standby (grupo) priority (>100)
```
Router 2
```cisco
int (interfaz del router)
standby (grupo) ip (ip virtual)
standby (grupo) preempt
```

Verificacion de hsrp conf
```cisco
sh standby brief
```
 
### Conceptos
- La prioridad predeterminada de HSRP es 100. El rango de etiquetas de prioridad es de 0 a 7. El router con la prioridad más alta se convertirá en el router activo.
- Los routers activos HSRP siguen siendo el router activo incluso si otro router con una prioridad más alta se une a la red.
- En el estado de habla HSRP, el router comienza a enviar mensajes de saludo periódicos.
- En el estado de aprendizaje de HSRP, el router aún no ha determinado la dirección IP virtual.

## Notas relacionadas
- [[FHRP (Protocolos de redundancia de primer salto)]]
- [[Enrutamiento]]
- [[VLAN]]
