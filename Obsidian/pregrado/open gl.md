## Notas relacionadas
- [[Documentos/computacion grafica/OpenGl|OpenGL y shaders]]
- [[Documentos/computacion grafica/pipeline grafico|Pipeline gráfico]]
- [[Documentos/computacion grafica/pixeles|Píxeles]]
- [[Untitled 4]]

# Element buffer objects 
Es un buffer que alamacena indices que opengl usa para decidir que vertices usar para dibujar
unsigned int EBO
glGenBuffers(1,&EBO) aqui se crea el buffer  el indicador 1 es porque genera solo uno y si edentificador es ebo 
glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO); vincula el buffer identificado por ebo  al objetivo gl 
glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indices), indices, GL_STATIC_DRAW); copia los datos de la cpu al ebo (gpu)

![[Pasted image 20241126214620.png]]

# vertex shader 
crea memoria en la GPU donde almacenamos los datos de los vértices, configuramos cómo OpenGL debe interpretar la memoria y especificamos cómo enviarlos datos a la tarjeta gráfica.La ventaja de usar esos objetos de búfer es que podemos enviar grandes lotes de datos de una sola vez a la tarjeta gráfica y mantenerlos allí si queda suficiente memoria libre, sin tener que enviar datos de a un vértice por vez. Enviar datos a la tarjeta gráfica desde la CPU es relativamente lento.

Al igual que cualquier objeto en OpenGL, este búfer tiene un ID único correspondiente a ese búfer, por lo que podemos generar uno con un ID de búfer utilizando la función glGenBuffers

unsigned int VBO;
glGenBuffers(1, &VBO);
un objeto de búfer de vértices es GL_ARRAY_BUFFER. Podemos vincular el búfer recién creado al objetivo GL_ARRAY_BUFFER con
glBindBuffer

glBindBuffer(GL_ARRAY_BUFFER, &VBO);

luego Podemos hacer una llamada a la función glBufferData que copia los datos de vértice previamente definidos en la memoria del buffer

glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW) es una función específicamente diseñada para copiar datos definidos por el usuario en el búfer actualmente enlazado.

se debo escribir el vertex shader en el lenaguje glsl y compilar el shader glsl tiene un vector datatype que contiene 1 a 4 flotantes basados en el digito postfix cada verticie tiene cordennadas 3d entonce se debe crear un vec3 input variable con el nombre a pos con la location=0

gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);
tiene un tamañao de 4 en cada uno de estos valores puede ser recivido via vec.x, vec.y, vec.z and vec.w respectivamente y donde cada uno de ellos represneta una coordenada en el espacio  vecw respresenta division de perspectiva 


# fragment shader
es el segundo y el shader final donde vamos u crear una renderizacion al triangulo. se trata de calcula el output del color de los pixeles 
![[Pasted image 20241126224237.png]]

los colores en computadores se representan en un array de  4 valores rojo verde azul y opacidad RGBA
el fragment shader solamnete requiere un output y es un vecotr de tamaño 4 que define el color final que nosotros debemos calcular

#version 330 core 
out vec4 FragColor; 
void main() 
{ FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f); }

# shader program
es una version final de multiples shaders combinados pra usar los shaders compilados debesmos enlazarlos a un shader program objecto cuando se rendereizan los objetoos 
![[Pasted image 20241126225406.png]]
![[Pasted image 20241126225506.png]]
## vertex processor
opera sobre los valores de los vertices y sus datos asociados 
* transformacions de vertices 
* transformacion de la normal y normalizacion 
* generaicon y tranformacion de coordenadas de texturas 
* iluminacion 
* aplicacion del colore de materiales
# fragment processor 
son estruturas de datos por pixel que son creados por la restarizacion de primitivas graficas
* operacione en valores interpolados 
* accesos a texturas
* niebla 
* suma de colores 
