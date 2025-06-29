consiste en una serie de elementos y atributos que se utilizan para marcar todos los componentes de un documento para estructurarlo de una manera significativa.
son básicamente un árbol de nodos, que incluye elementos HTML y nodos de texto. Los elementos HTML proporcionan la semántica y el formato de los documentos, incluida la creación de párrafos, listas y tablas, y la incrustación de imágenes y controles de formulario.
Los elementos HTML están delineados por etiquetas, escritas con corchetes angulares ( y ).`<``>`

en el head se tiene informacion de metadata con palabras clave <meta> son etiquetas huerfanas no tienen un cierre dentro de <head> </head>

el body es la parte visible de la pagina web
  solo se puede tener un <h1> </h1>por tenemas de usabilidad
  Para asegurarnos de que el contenido de nuestros documentos sea interpretado correctamente como código HTML, debemos agregar la declaración al comienzo del archivo. se requiere al comienzo de cada documento para ayudar al navegador a decidir cómo debe generar la página web. Para documentos programados con HTML5, la declaración debe incluir el atributo html
  
### elementos  
<html></html> Este elemento delimita el código HTML. Puede incluir el atributo lang para definir el idioma del contenido del documento. 
<head></head> Este elemento se usa para definir la información necesaria para configurar la página web, como el título, el tipo de codificación de caracteres y los archivos externos requeridos por el documento. 
<body></body>Este elemento delimita el contenido del documento (la parte visible de la página).
El elemento <link></link> se usa comúnmente para cargar archivos CSS con los estilos necesarios para generar la página web. Por ejemplo, el siguiente documento carga el archivo misestilos.css.
<div></div>Este elemento define una división genérica. Se usa cuando no se puede aplicar ningún otro elemento.
<main> </main>Este elemento define una división que contiene el contenido principal del documento (el contenido que representa el tema central de la página).
<nav></nav>este elemento define una división que contiene ayuda para la navegación, como el menú principal de la página o bloques de enlaces necesarios para navegar en el sitio web.
<section></section>Este elemento define una sección genérica. Se usa frecuentemente para separar contenido temático, o para generar columnas o bloques que ayudan a organizar el contenido principal.
<aside></aside>Este elemento define una división que contiene información relacionada con el contenido principal pero que no es parte del mismo, como referencias a artículos o enlaces que apuntan a publicaciones anteriores.
<article></article>Este elemento representa un artículo independiente, como un mensaje de foro, el artículo de una revista, una entrada de un blog, un comentario, etc.
<header></header>Este elemento define la cabecera del cuerpo o de secciones dentro del cuerpo.
<footer></footer>Este elemento define el pie del cuerpo o de secciones dentro del cuerpo.
son flexibles y se pueden implementar en diferentes partes del diseño, todos siguen un patrón que se encuentra comúnmente en la mayoría de los sitios web.
![[Pasted image 20240519214757.png]]

 el elemento <nav></nav> se podría insertar dentro de etiquetas o en otra sección del cuerpo
 
### contenido
#### texto
El medio más importante que puede incluir un documento es texto es el titulo puede ir  hasta 6 <h1></h1>
Los siguientes son los elementos que ofrece HTML para representar el cuerpo del texto.

<p></p>Este elemento representa un párrafo. Por defecto, los navegadores le asignan un margen en la parte superior para separar un párrafo de otro.
<pre></pre>Este elemento representa un texto con formato predefinido, como código de 
programación o un poema que requiere que los espacios asignados a cada carácter y los 
saltos de línea se muestren como se han declarado originalmente. 
<span>Este elemento puede contener un párrafo, una frase o una palabra. No aplica 
ningún estilo al texto pero se usa para asignar estilos personalizados, como veremos en 
próximos capítulos.
  
<br></br>Este elemento se usa para insertar saltos de línea. 
<wbr></wbr>Este elemento sugiere la posibilidad de un salto de línea para ayudar al navegador a decidir dónde cortar el texto cuando no hay suficiente espacio para mostrarlo entero
<em></em>Este elemento se usa para indicar énfasis. El texto se muestra por defecto con letra cursiva. 
<strong></strong>Este elemento es utiliza para indicar importancia. El texto se muestra por defecto en negrita. 
<i></i>Este elemento representa una voz alternativa o un estado de humor, como un pensamiento, un término técnico, etc. El texto se muestra por defecto con letra cursiva. 
<u></u>Este elemento representa texto no articulado. Por defecto se muestra subrayado. <b></b>Este elemento se usa para indicar importancia. Debería ser implementado solo cuando ningún otro elemento es apropiado para la situación. El texto se muestra por defecto en negrita.
<mark></mark>Este elemento resalta texto que es relevante en las circunstancias actuales (por ejemplo, términos que busca el usuario). 
<small></small>Este elemento representa letra pequeña, como declaraciones legales, descargos, etc. 
<cite></cite>Este elemento representa el autor o título de una obra, como un libro, una película, etc.
<address></address>Este elemento representa información de contacto. Se implementa con frecuencia dentro de los pies de página para definir la dirección de la empresa o el sitio web.

### enlaces 


---
 <pre></pre>se configura por defecto con márgenes y un tipo de letra que respeta el 
formato asignado al texto original, lo que lo hace apropiado para presentar código de 
programación y cualquier clase de texto con formato predefinido