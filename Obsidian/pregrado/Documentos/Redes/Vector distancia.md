el uso de protocolos propietarios hace que no sa escalabe con otros dispositivos de otras marcas 
tienen intervalos regulares
los vecinos routers que comparten un enlace y que estan configurados con el mismo protocolo 

## caracterisitcas 
el tiempo de convergencia es el tiempo que los routedores tengan la misma informacion y alcanzan un estado de conocimiento constante 

la escalabilidad define que tan grande puede ser una red segun el protocolo 

con clase se usa mascara de red 
sin clase sin mascara de red 

| ventajas                                                                  | desventajas                                             |
| ------------------------------------------------------------------------- | ------------------------------------------------------- |
| implementacion y mantenimiento simple                                     | convergencia lenta: las actualizaciones periodicas      |
| pocos requisitos de recursos no requieren tanta memoria ni un cpu potente | la convergencia lenta puede limitar el tamaño de la red |
|                                                                           |                                                         |                                                                          |                                                         |

## deteccion de redes
1. descubrimiento inicial de la red
las interfaces del mismo router conectadas directamente
2. intercambio de inicial de informacion de enrutamiento
tinen informacion de vecinos
3. intercambio de informacion de enrutamiento 
los routers tienen informacion de los vecinos de los vecinos 

## mantenimiento de tablas 

* rip usa 4 temporizadores:
temporizador de actualizacion se envia 30 segundos 
temporizador de invalides 
temporizador de purge 

## Notas relacionadas
- [[Enrutamiento]]
- [[OSPFv2(Open Shortest Path First)]]
- [[estado de enlace]]
