[[Funcionamiento del Sistema de Memoria]]
* El objetivo de la memoria caché es lograr que la velocidad de la memoria sea lo más rápida posible, consiguiendo al mismo tiempo un tamaño grande al precio de memorias semiconductoras (menos costosas).
* La caché contiene una copia de partes de la memoria principal. Cuando el procesador intenta leer una palabra de memoria, se hace una comprobación para determinar si la palabra está en la caché. Si es así, se entrega dicha palabra al procesador. Si no, un bloque de memoria principal se transfiere a la caché y después la palabra es entregada al procesador
![[Pasted image 20230730184934.png]]
## Memoria principal
2<sup>𝑛</sup> palabras direccionables.
Cada palabra tiene una única dirección de n bits.
Bloques de longitud fija: K palabras por bloque.
* Número total de bloques (M):
$$ M= \frac {2^{n}}{K}    \mathsf bloques $$ ![[Pasted image 20230730190942.png]]
## Memoria Cache
Consta de c líneas.
* Cada línea contiene K palabras, más una etiqueta de unos cuantos bits.
* Tamaño de línea es el número de palabras que hay en la línea (tamaño de bloque).
*  C < < M (# líneas << # de bloques)
*  En todo momento, un subconjunto de los bloques de memoria reside en líneas de la caché.
* Si se lee una palabra de un bloque, éste es transferido a una de las líneas de la caché.
* Etiqueta: identifica que bloque almacena.
![[Pasted image 20230730191120.png]]
### Organizacion del cache
* La caché se conecta con el procesador mediante líneas de datos, de direcciones y de control 
* Las líneas de direcciones y de datos conectan con buffers de datos y de direcciones que las comunican con un bus del sistema (mem. principal) 
* Si existe un acierto de caché, los buffers de datos y de direcciones se inhabilitan (procesador y caché). Caso contrario, la dirección se carga en el bus del sistema y el dato es llevado, a través del buffer de datos, tanto a la caché como al procesador
![[Pasted image 20230730191355.png]]

## Elementos de diseño
### Tamaño de cache 
el tamaño sea lo suficientemente pequeño como paraque el coste total medio por bit se aproxime al de la memoria principal, y que fuera lo suficientemente grande como para que eltiempo de acceso medio total sea próximo al de la caché sola.
Cuanto más grande es, mayor es el número de puertas implicadas en direccionar la caché y por tanto tienden a ser ligeramente más lentas. 
El tamaño de caché está también limitado por las superficies disponibles de chip y de tarjeta
### Funcion de correspondencia
* La función de correspondencia determina cómo se organiza la caché. 
* Se necesita: I) un algoritmo que haga corresponder bloques de memoria principal a líneas de caché y II) algún medio para determinar qué bloque de memoria principal ocupa actualmente una línea dada de caché. 
* Existen 3 técnicas diferentes: directa, asociativa, y asociativa por conjuntos.
![[Pasted image 20230730192432.png]]
## Función de Correspondencia Directa
* Es sencilla y poco costosa de implementar. Su principal desventaja es que hay una posición concreta de caché para cada bloque. 
* Si un programa referencia repetidas veces a palabras de dos bloques diferentes asignados en la misma línea, dichos bloques se estarían intercambiando continuamente en la caché, y la tasa de aciertos sería baja, este fenómeno es conocido como vapuleo (thrashing). 
* Desde el punto de vista del acceso a caché, cada dirección de memoria principal se divide en tres campos: etiqueta, línea y palabra. ![[Pasted image 20230730193153.png]]
Cuando un bloque es realmente escrito en la línea que tiene asignada, es necesario etiquetarlo para distinguirlo del resto de los bloques que pueden introducirse en dicha línea. Para ello se emplean los bits de etiqueta (s-r bits)
Además, m representa el número de líneas de caché.
![[Pasted image 20230730193411.png]]
![[Pasted image 20230730193431.png]]
### Ejercicio
[[Ejercicio Correspondencia directa.excalidraw]]
## Correspondencia Asociativa
Permite que cada bloque de memoria principal pueda cargarse en cualquier línea de la caché. En este caso, la lógica de control de la caché interpreta una dirección de memoria simplemente como una etiqueta (identifica unívocamente un bloque de memoria principal) y un campo de palabra
Para determinar si un bloque está en la caché, su lógica de control debe examinar simultáneamente todas las etiquetas de líneas para buscar una coincidencia
![[Pasted image 20230815145932.png]]
### **Funcionamiento** 
![[Pasted image 20230815150330.png]]

### Ejercicio
