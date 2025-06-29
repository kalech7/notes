usa una arquitectura pipeline 
para crrear un grafico en el computador 
los sharders son aplicaciones que se ejecutan en la gpu 
dos tipos de shaders son obligadoras: 
* fragment shader (se encarga de los colores con los que se rellean el objeto)
* vertex shader(se encarga de los vertices de la forma )
* geometry shader(no se usa porque se usa el vertex shader)
glsl programacion en paralell

la ultima version es opengl 4.6 y contiene esas distribuciones 
* open gl ES (embeded system)
* web gl (navegadores)
es multiplataforma

cada sistema operatico tiene sus propios librerias de gestor de ventanas y opengl para el relleno de la ventana pero tambien glfw es una libreria de gestor de ventanas multiplataforma