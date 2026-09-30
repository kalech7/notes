# Fundamentals of Software Architecture · 2.ª edición

Guía detallada en español basada en los doce escaneos compartidos, organizada por capítulos. Autores del libro: Mark Richards y Neal Ford. Las explicaciones, ilustraciones, diagramas y ejercicios propios están diferenciados del material de la fuente.

## Leer por capítulos

1. [Introducción: arquitectura, contexto y responsabilidad](01%20Introducci%C3%B3n/00%20%C3%8Dndice.md)
2. [Pensamiento arquitectónico](02%20Pensamiento%20arquitect%C3%B3nico/00%20%C3%8Dndice.md)
3. [Modularidad, cohesión y acoplamiento](03%20Modularidad/00%20%C3%8Dndice.md)
4. [Características arquitectónicas](04%20Caracter%C3%ADsticas%20arquitect%C3%B3nicas/00%20%C3%8Dndice.md)
5. [Identificar y priorizar características](05%20Identificar%20y%20priorizar%20caracter%C3%ADsticas/00%20%C3%8Dndice.md)
6. [Medición y gobierno](06%20Medici%C3%B3n%20y%20gobierno/00%20%C3%8Dndice.md)
7. [Alcance y quanta](07%20Alcance%20y%20quanta/00%20%C3%8Dndice.md)
8. [Pensamiento basado en componentes](08%20Pensamiento%20basado%20en%20componentes/00%20%C3%8Dndice.md)
9. [Fundamentos de estilos arquitectónicos](09%20Fundamentos%20de%20estilos%20arquitect%C3%B3nicos/00%20%C3%8Dndice.md)
10. [Arquitectura por capas](10%20Arquitectura%20por%20capas/00%20%C3%8Dndice.md)
11. [Monolito modular](11%20Monolito%20modular/00%20%C3%8Dndice.md)
12. [Arquitectura pipeline](12%20Arquitectura%20pipeline/00%20%C3%8Dndice.md)
13. [Arquitectura microkernel](13%20Arquitectura%20microkernel/00%20%C3%8Dndice.md)
14. [Arquitectura basada en servicios](14%20Arquitectura%20basada%20en%20servicios/00%20%C3%8Dndice.md)

15. [Arquitectura dirigida por eventos](15%20Arquitectura%20dirigida%20por%20eventos/00%20%C3%8Dndice.md)

Cada enlace abre el índice de una carpeta de capítulo, con notas numeradas por tema y navegación anterior/siguiente. Los capítulos 1–5 contienen **37 notas de estudio** y los capítulos 6–8 añaden **25 notas temáticas y 31 gráficos PNG**, además de sus índices y un laboratorio; cada capítulo termina con preguntas y un ejercicio resuelto. Los capítulos 9–10 añaden 17 notas temáticas, dos índices, ocho PNG y un atlas con laboratorio transversal. El capítulo 11 añade nueve notas temáticas, un índice, ocho PNG en `Recursos visuales/Capítulo 11` y ocho diagramas Mermaid. El capítulo 12 añade nueve notas temáticas, su índice, tres PNG y cinco diagramas Mermaid. Los capítulos 13 y 14 añaden 21 notas temáticas, dos índices, 14 PNG y 12 diagramas Mermaid sobre microkernel y arquitectura basada en servicios, con mecanismos, casos completos y laboratorios resueltos. La comparación transversal añade dos PNG y un Mermaid. Una comparación visual conecta módulos, filtros, plugins y servicios. El capítulo 15 añade 18 notas temáticas, un índice, trece PNG y diagramas Mermaid, con pedido completo, subastas y laboratorio de fallos resuelto.

Cada capítulo incluye imágenes PNG visibles directamente en GitHub y Obsidian, explicaciones de sus mecanismos y límites, preguntas y un ejercicio resuelto. Los diagramas iniciales conservan `.mmd` y `.svg` en `Recursos visuales/Diagramas`. Los nuevos gráficos, inspirados en la estructura de las figuras del libro y explicados paso a paso, conservan generadores editables en `Recursos visuales/Capítulos 6 a 8`.

![Separación lógica y física: monolito modular, microservicios y monolito distribuido](Recursos%20visuales/03-modularidad.png)

La ilustración sirve para diferenciar modularidad y despliegue: contar cajas o bases de datos no basta para determinar la calidad de los límites.

## Estructura de la carpeta

- **01–15:** una carpeta por capítulo, cada una con su propio índice y notas temáticas.
- **06 Apoyo y repaso:** atlas visual, laboratorios y glosario. Se conserva el nombre histórico; es distinta de **06 Medición y gobierno**.
- **90 Fuentes y revisión:** cobertura, procedencia y prompts.
- **Materiales** y **Recursos visuales:** PDF, imágenes y fuentes editables.

Las fórmulas permanecen en los archivos Markdown, con notación LaTeX, variables y ejemplos explicados.

## Practicar y profundizar

- [Ruta de estudio e índice de Obsidian](00%20Empieza%20aqu%C3%AD.md)
- [Atlas visual explicado](06%20Apoyo%20y%20repaso/01%20Atlas%20visual%20explicado.md)
- [Laboratorio integrador de PedidoClaro](06%20Apoyo%20y%20repaso/02%20Laboratorio%20integrador.md)
- [Glosario y repaso](06%20Apoyo%20y%20repaso/03%20Glosario%20y%20repaso.md)
- [Método completo para tomar decisiones](06%20Apoyo%20y%20repaso/04%20M%C3%A9todo%20completo%20para%20tomar%20decisiones.md)
- [Fuentes, cobertura y páginas ausentes](90%20Fuentes%20y%20revisi%C3%B3n/01%20Fuentes%20y%20cobertura.md)
- [Procedencia de imágenes y prompts](90%20Fuentes%20y%20revisi%C3%B3n/02%20Procedencia%20y%20reproducci%C3%B3n.md)
- [Laboratorio de componentes, quanta y gobierno](06%20Apoyo%20y%20repaso/05%20Laboratorio%20de%20componentes%20quanta%20y%20gobierno.md)
- [Cobertura y figuras de los capítulos 6–8](90%20Fuentes%20y%20revisi%C3%B3n/04%20Ampliaci%C3%B3n%20cap%C3%ADtulos%206%20a%208.md)

- [Atlas y práctica de estilos y capas](06%20Apoyo%20y%20repaso/06%20Atlas%20y%20pr%C3%A1ctica%20de%20estilos%20y%20capas.md)
- [Cobertura y precisiones de los capítulos 9–10](90%20Fuentes%20y%20revisi%C3%B3n/05%20Ampliaci%C3%B3n%20cap%C3%ADtulos%209%20y%2010.md)
- [Cobertura y precisiones del capítulo 11](90%20Fuentes%20y%20revisi%C3%B3n/06%20Ampliaci%C3%B3n%20cap%C3%ADtulo%2011.md)

- [Cobertura y precisiones del capítulo 12](90%20Fuentes%20y%20revisi%C3%B3n/07%20Ampliaci%C3%B3n%20cap%C3%ADtulo%2012.md)

- [Comparación visual de módulos, filtros, plugins y servicios](06%20Apoyo%20y%20repaso/07%20Comparaci%C3%B3n%20visual%20de%20m%C3%B3dulos%20filtros%20plugins%20y%20servicios.md)
- [Cobertura del capítulo 13](90%20Fuentes%20y%20revisi%C3%B3n/08%20Ampliaci%C3%B3n%20cap%C3%ADtulo%2013.md)
- [Cobertura del capítulo 14](90%20Fuentes%20y%20revisi%C3%B3n/09%20Ampliaci%C3%B3n%20cap%C3%ADtulo%2014.md)

- [Cobertura del capítulo 15](90%20Fuentes%20y%20revisi%C3%B3n/10%20Ampliaci%C3%B3n%20cap%C3%ADtulo%2015.md)

## Fuentes locales

- [Introducción y pensamiento arquitectónico: 31 páginas](Materiales/01%20Introducci%C3%B3n%20y%20pensamiento%20arquitect%C3%B3nico.pdf)
- [Modularidad: 18 páginas](Materiales/02%20Modularidad.pdf)
- [Características e identificación: 24 páginas](Materiales/03%20Caracter%C3%ADsticas%20e%20identificaci%C3%B3n.pdf)
- [Medición y gobierno: 13 páginas](Materiales/04%20Medici%C3%B3n%20y%20gobierno.pdf)
- [Alcance y componentes: 34 páginas](Materiales/05%20Alcance%20y%20componentes.pdf)

- [Fundamentos de estilos: 23 páginas](Materiales/06%20Fundamentos%20de%20estilos%20arquitect%C3%B3nicos.pdf)
- [Arquitectura por capas: 12 páginas](Materiales/07%20Arquitectura%20por%20capas.pdf)
- [Monolito modular: 16 páginas](Materiales/08%20Monolito%20modular.pdf)

- [Arquitectura pipeline: 12 páginas](Materiales/09%20Arquitectura%20pipeline.pdf)

- [Arquitectura microkernel: 16 páginas](Materiales/10%20Arquitectura%20microkernel.pdf)
- [Arquitectura basada en servicios: 18 páginas](Materiales/11%20Arquitectura%20basada%20en%20servicios.pdf)
- [Arquitectura dirigida por eventos: 55 páginas](Materiales/12%20Arquitectura%20dirigida%20por%20eventos.pdf)

La colección reúne 272 páginas de PDF: 73 iniciales, 47 en la primera ampliación, 35 en la segunda (incluida una portada de la Parte II sin número impreso), 16 del capítulo 11, 12 del capítulo 12, 16 del capítulo 13, 18 del capítulo 14 y 55 del capítulo 15. El material no contiene el libro completo; los huecos de numeración impresa se detallan en la nota de cobertura. Los enlaces internos propios de Obsidian están pensados para navegar dentro de la aplicación; este README ofrece navegación equivalente con enlaces de Markdown para GitHub.
