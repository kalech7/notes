---
title: "03 · Modularidad — 2.ª edición"
created: 2026-09-25
tags:
  - lecturas/software-architecture
---

[[Obsidian/lecturas/Fundamentals of Software Architecture/00 Empieza aquí|← Índice]]

# 03 · Modularidad: decidir qué debe cambiar junto · 2.ª edición

## Fuente y forma de estudiar este capítulo

Esta guía desarrolla el capítulo 3 de *Fundamentals of Software Architecture*, segunda edición, de Mark Richards y Neal Ford. Se basa exclusivamente en las **páginas 1–18 del PDF de modularidad, correspondientes a las páginas impresas 37–54**. Las referencias siguientes distinguen ambas numeraciones. No presuponen acceso a otros capítulos.

**Contenido del libro:** modularidad, granularidad, cohesión, acoplamiento, métricas estructurales y connascencia. **Elaboración propia:** explicaciones, cálculos, diagramas, aclaraciones de ambigüedades y ejercicios. **Supuesto transversal:** PedidoClaro es una tienda de sándwiches completamente inventada para esta guía; no es la kata *Silicon Sandwiches* del libro. Sus clientes compran productos, reciben pedidos y pagan importes calculados por el sistema.

La pregunta central es: **¿qué conocimiento y qué cambios deben permanecer dentro de una frontera?** Una frontera útil permite modificar una regla sin perseguir sus detalles por toda la aplicación. Dibujar carpetas o servicios no garantiza esa propiedad.

![modularidad](Recursos%20visuales/03-modularidad.png)

## 1. Modularidad, granularidad y separación física

El libro usa *módulo* como agrupación lógica de código relacionado: funciones, clases u otros elementos. La **modularidad** trata de esa organización y sus fronteras; la **granularidad**, del tamaño y alcance de las piezas. Son dimensiones relacionadas: separar más unidades cambia las fronteras, pero una partición más fina no necesariamente mejora el diseño.

En PedidoClaro, cálculo de subtotales, descuentos y redondeo podrían pertenecer a `Precios`. Si cada operación se convierte en un servicio remoto, calcular un pedido exige coordinar varias llamadas. Aparecen latencia, versiones de contratos y fallos parciales. Ese coste puede ser razonable si existe una necesidad concreta; no surge una ventaja solo por tener piezas pequeñas.

![1. Modularidad, granularidad y separación física ](Recursos%20visuales/Diagramas/cap03-diagrama-01.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap03-diagrama-01.mmd)

**Interpretación:** puede haber módulos con contratos definidos dentro de un solo proceso. **Límite:** las flechas expresan dependencias conceptuales; no prueban que el código impida accesos a detalles internos ni describen toda la ejecución.

La separación **lógica** establece responsabilidades, visibilidad y contratos. La separación **física** introduce unidades como bibliotecas, procesos o despliegues. Un monolito puede conservar buenas fronteras lógicas; varios servicios pueden depender continuamente de los detalles de sus vecinos y requerir cambios coordinados. Por eso no conviene equiparar modularidad con distribución.

Un *namespace* distingue nombres: `clientes.Estado` y `pedidos.Estado` pueden coexistir sin representar el mismo concepto. Esto resuelve identificación, pero no demuestra cohesión. Una carpeta `utilidades` puede contener funciones sin relación aunque todos sus nombres sean únicos.

El recorrido histórico del libro conecta programación estructurada, mecanismos de módulos y posterior conservación de paquetes y espacios de nombres en lenguajes orientados a objetos. Sirve para entender por qué conviven funciones, clases y paquetes. Aquí no se reproduce como cronología estricta de versiones de Java: el propósito didáctico es distinguir **organización de nombres, encapsulación y empaquetado físico**. Ninguna de esas propiedades sustituye automáticamente a las otras.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=1|PDF pp. 1–4; impresas pp. 37–40]].

## 2. Cohesión: razones para permanecer juntos

![Responsabilidades mezcladas frente a módulos cohesivos de pedidos, pagos y entregas](Recursos%20visuales/09-cohesion-responsabilidades.png)

**Cómo leer la imagen:** a la izquierda, cada contenedor mezcla pedidos, pagos y entregas, de modo que un cambio puede atravesar varias fronteras. A la derecha, cada responsabilidad tiene un lugar reconocible y se comunica mediante interfaces. Los puentes muestran que sigue habiendo acoplamiento. La frase «baja dependencia» expresa el objetivo de este ejemplo, no una garantía: hacen falta contratos y límites efectivos para conseguirlo. Los contenedores son módulos lógicos; no obligan a desplegar tres servicios.

La cohesión expresa cuánto sentido tiene que las partes pertenezcan al mismo módulo. Una intuición útil es preguntar si colaboran para una responsabilidad reconocible y cambian por razones relacionadas. Separar piezas muy cohesionadas puede obligarlas a compartir tantos detalles que el acoplamiento externo empeore.

### Las siete formas de cohesión

El libro las presenta desde funcional hasta accidental. Es una orientación cualitativa, **no una escala numérica ni un orden rígido aplicable sin contexto**. Además, aunque algunas descripciones del texto hablan de dos módulos, aquí examinamos la razón para agrupar operaciones dentro de la unidad evaluada.

1. **Funcional.** Todas las partes contribuyen a una función concreta. `CalcularTotalPedido` valida cantidades, aplica las reglas pertinentes y obtiene el total. La unidad se entiende por el resultado que produce. No significa que deba contener también envío de correos o persistencia de clientes: una finalidad excesivamente amplia, como «gestionar todo el negocio», no demuestra cohesión.

2. **Secuencial.** La salida de una operación alimenta a la siguiente. PedidoClaro transforma líneas de pedido en subtotales y después los subtotales en una base para descuentos. Existe una dependencia de datos que explica la agrupación. No basta con que las operaciones se ejecuten una después de otra: debe haber ese flujo de salida a entrada.

3. **Comunicacional.** Varias operaciones trabajan sobre los mismos datos o contribuyen a una salida común. Preparar el recibo y preparar el resumen de cocina pueden utilizar la misma instantánea confirmada del pedido. Eso ofrece una razón para agruparlas, aunque el hecho de compartir datos no garantiza que deban permanecer juntas si evolucionan con reglas distintas.

4. **Procedimental.** La agrupación se explica por un orden de pasos, sin exigir que cada salida sea la entrada siguiente. Un procedimiento de cierre puede cerrar la caja y después emitir el informe diario. La relación está en el procedimiento; las responsabilidades internas todavía pueden ser diferentes.

5. **Temporal.** Las operaciones se reúnen porque ocurren en un momento común. Al arrancar PedidoClaro se carga configuración, se preparan conexiones y se registran tareas. Coinciden en el inicio, pero sus causas de cambio son distintas. Un coordinador de arranque puede ser apropiado sin convertirse en propietario de todas esas implementaciones.

6. **Lógica.** Las operaciones pertenecen a una categoría amplia: convertir cadenas, leer formatos o validar entradas. `Conversores` puede incluir conversión de fechas, importes y direcciones. La semejanza nominal no crea una única función de negocio. Un argumento que selecciona entre muchas operaciones suele hacer visible esta agrupación, aunque no es obligatorio para clasificarla así.

7. **Accidental o coincidente.** Las partes solo comparten ubicación. Un archivo con redondeo monetario, limpieza de archivos temporales y generación de colores no tiene una responsabilidad común. Cambiarlo obliga a revisar consumidores ajenos y amplía innecesariamente el alcance de pruebas y permisos de modificación.

Una misma unidad puede mostrar varias relaciones. La clasificación ayuda a formular preguntas, no a condenar automáticamente módulos de inicialización o bibliotecas de funciones puras.

### El caso Customer/Order del libro

El libro compara un módulo de mantenimiento de clientes que añade, actualiza, consulta y notifica clientes, pero también consulta y cancela sus pedidos, con una separación entre `Customer Maintenance` y `Order Maintenance`.

La separación no se decide contando verbos. Si consultar y cancelar son las únicas operaciones de pedidos y requieren conocer profundamente al cliente, extraerlas puede producir una interfaz muy conversadora. Si los pedidos crecerán con estados, devoluciones y reservas, una responsabilidad independiente gana sentido.

**Aplicación propia:** en PedidoClaro, cancelar un pedido confirmado puede liberar inventario y solicitar un reembolso. Esa regla pertenece probablemente a Pedidos. Clientes puede solicitarla mediante el identificador del cliente y del pedido. Si Pedidos exige doce campos internos del cliente, hay que revisar el contrato: cambiar de carpeta no eliminó el conocimiento compartido. La evidencia decisiva son las invariantes, los cambios esperados y las dependencias resultantes.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=5|PDF pp. 5–7; impresas pp. 41–43]].

## 3. LCOM: medir estructura sin confundirla con intención

LCOM significa *Lack of Cohesion of Methods*: falta de cohesión entre métodos. Hay distintas variantes y no comparten necesariamente escala, fórmula o tratamiento de casos especiales. Antes de comparar resultados de herramientas hay que verificar qué calculan.

### LCOM1 con cuatro métodos

Usaremos la formulación que el capítulo denomina versión 1. Para cada método se obtiene el conjunto de campos de instancia que utiliza. Después se examinan **pares no ordenados de métodos distintos**:

- $P$: conjunto de pares cuyos conjuntos de campos son disjuntos.
- $Q$: conjunto de pares que comparten al menos un campo.

$$
\mathrm{LCOM1}=\max\left(|P|-|Q|,0\right)
$$

**Aclaración técnica:** se cuentan pares, no métodos aislados ni accesos individuales. $|Q|$ es un conteo no negativo; no se va «decrementando». Compartir tres campos sigue aportando un solo par a $Q$. La prosa de la página impresa 43 puede inducir a confusión en este punto.

Supongamos una clase de PedidoClaro con cuatro métodos:

| Método | Campos usados |
|---|---|
| `subtotal()` | `lineas` |
| `cantidadArticulos()` | `lineas` |
| `destinatario()` | `correo` |
| `cambiarDestinatario()` | `correo` |

Hay $4\times3/2=6$ pares. Dos comparten campos: los dos primeros métodos entre sí y los dos últimos entre sí. Los cuatro pares que cruzan grupos no comparten campos. Por tanto, $|P|=4$, $|Q|=2$ y **LCOM1 = 2**. Esto sugiere dos responsabilidades para investigar, no ordena una extracción automática.

![LCOM1 con cuatro métodos ](Recursos%20visuales/Diagramas/cap03-diagrama-02.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap03-diagrama-02.mmd)

**Interpretación:** aparecen dos grupos desconectados de métodos y campos. **Límite:** el dibujo no muestra llamadas entre métodos, reglas de negocio ni acceso indirecto al estado. Esas omisiones importan al elegir una variante de LCOM.

### LCOM1 no es LCOM4

**Ampliación técnica propia:** LCOM4 cuenta componentes conexas en un grafo de métodos, conectados por acceso a campos comunes o por llamadas entre ellos, según las reglas de la herramienta. Si no hay llamadas adicionales, el ejemplo anterior tiene dos componentes: LCOM4 = 2. La coincidencia numérica con LCOM1 es accidental.

Para comprobarlo, imaginemos tres métodos que comparten `lineas` y un cuarto que usa únicamente `correo`. Hay tres pares compartidos y tres disjuntos: LCOM1 = 0. Sin llamadas adicionales siguen existiendo **dos componentes conexas**. Por tanto, un cero en LCOM1 no demuestra que toda la clase esté conectada.

### La expresión LCOM96b de la página 43

La ecuación 3-2 se comprobó directamente en la imagen ampliada del escaneo. El libro imprime bajo el nombre **LCOM96b**:

$$
\mathrm{LCOM96b}=\frac{1}{a}\sum_{j=1}^{a}\frac{m-\mu(A_j)}{m}.
$$

Para interpretar esa expresión, tomamos $a$ como número de atributos, $m$ como número de métodos y $\mu(A_j)$ como número de métodos que utilizan el atributo $A_j$. Para cada atributo contamos qué proporción de métodos **no lo usa**; después promediamos esas proporciones. Es equivalente a $1-\sum_j\mu(A_j)/(am)$, cuando $a>0$ y $m>0$.

En nuestro ejemplo hay dos atributos y cuatro métodos; cada atributo es utilizado por dos métodos. El resultado es $\frac12[(4-2)/4+(4-2)/4]=0.5$. Si todos los métodos utilizan todos los atributos, da cero. Si ningún método utiliza ningún atributo, da uno. Esta fórmula tampoco cuenta componentes conexas ni demuestra cohesión semántica. Sin métodos o sin atributos queda indefinida bajo la expresión escrita; una herramienta puede establecer una convención propia.

**Precisión sobre variantes:** se está explicando la expresión impresa del escaneo. Existen otras normalizaciones que emplean $m-1$ en el denominador; no producen necesariamente el mismo resultado ni deben sustituirse silenciosamente al comparar herramientas. La explicación de los símbolos y el cálculo anterior son elaboración didáctica propia, porque el libro no desarrolla sus variables.

Una clase de funciones matemáticas puras puede no tener campos y aun así poseer una responsabilidad coherente. A la inversa, compartir un campo `contexto` entre todos los métodos puede producir un indicador favorable y ocultar muchas responsabilidades. La métrica descubre estructura; el dominio explica su conveniencia.

![lcom](Recursos%20visuales/05-lcom.png)

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=7|PDF pp. 7–8; impresas pp. 43–44]].

## 4. Acoplamiento: quién depende de quién

El acoplamiento aferente $C_a$ cuenta dependencias **entrantes**: otros elementos dependen del elemento analizado. El eferente $C_e$ cuenta dependencias **salientes**: el elemento analizado depende de otros.

![4. Acoplamiento: quién depende de quién ](Recursos%20visuales/Diagramas/cap03-diagrama-03.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap03-diagrama-03.mmd)

**Interpretación:** para Pedidos, en este grafo $C_a=3$ y $C_e=2$. La flecha va del dependiente hacia aquello que utiliza. **Límite:** son dependencias entre módulos distintos, no cantidad de llamadas, tráfico, latencia ni una traza temporal.

Hay que fijar la unidad: tipos, paquetes o componentes. También qué relación cuenta: importación, referencia de tipo o uso efectivo. En este ejemplo contamos módulos distintos y excluimos dependencias internas. Mezclar conteos de clases con conteos de paquetes produciría ratios engañosos.

Un $C_a$ elevado señala un alcance potencial de propagación de cambios: modificar un contrato puede afectar muchos consumidores. Un $C_e$ elevado señala muchos proveedores cuyos cambios podrían afectar al módulo. Ninguno demuestra por sí solo mala arquitectura; un contrato central estable puede tener numerosos consumidores deliberadamente.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=8|PDF pp. 8–9; impresas pp. 44–45]].

## 5. Abstracción, inestabilidad y secuencia principal

### Abstracción: contar tipos, no líneas

Para una unidad con $N_a$ tipos abstractos —interfaces o clases abstractas— y $N_c$ tipos concretos:

$$
A=\frac{N_a}{N_a+N_c}
$$

Si Pedidos tiene dos tipos abstractos y ocho concretos, $A=2/10=0.2$. **No intervienen las líneas de código.** El ejemplo narrativo de las 5.000 líneas en la página impresa 46 mezcla unidades y no debe utilizarse para calcular esta métrica. Si solo hubiera una clase concreta y ningún tipo abstracto, $A=0$, independientemente de su longitud. Sin tipos contables, el denominador es cero y el valor queda indefinido.

### Inestabilidad: una relación de dependencias

$$
I=\frac{C_e}{C_a+C_e}
$$

Con el grafo anterior, $I=2/(3+2)=0.4$. En esta terminología, una unidad con muchos dependientes tiene más restricciones para cambiar: se considera relativamente estable. Una unidad que depende de otras y tiene pocos consumidores dispone de mayor libertad estructural para cambiar y queda más expuesta a sus proveedores.

**$I$ no es una probabilidad de fallo**, ni mide cuántos defectos aparecen, ni la frecuencia real de cambios. Si $C_a=0$ y $C_e>0$, resulta $I=1$, incluso con un solo proveedor. Si $C_e=0$ y $C_a>0$, resulta $I=0$. Si ambos son cero, $I$ está **indefinida**; una herramienta puede adoptar una convención, que debe documentarse.

### Distancia y zonas

La secuencia principal es la recta $A+I=1$. Relaciona estabilidad estructural y abstracción: las unidades muy utilizadas pueden beneficiarse de contratos abstractos; las implementaciones concretas pueden ubicarse en unidades con mayor libertad de cambio.

$$
D=|A+I-1|
$$

Esta es la **distancia normalizada** del capítulo. La distancia geométrica perpendicular a la recta, usando ejes con la misma escala, es:

$$
d_{\perp}=\frac{|A+I-1|}{\sqrt{2}}
$$

En Pedidos, $A=0.2$ e $I=0.4$: $D=0.4$ y $d_{\perp}\approx0.283$. No son fórmulas contradictorias: la primera normaliza el máximo posible dentro del cuadrado unitario a 1.

| Región | Valores próximos | Qué invita a investigar |
|---|---|---|
| Zona de dolor | $A=0, I=0$ | Muchas dependencias hacia implementaciones concretas pueden encarecer cambios. |
| Secuencia principal | $A+I=1$ | Equilibrio estructural según este modelo; no certificación de calidad. |
| Zona de inutilidad | $A=1, I=1$ | Abstracciones con pocos consumidores y dependencias salientes pueden aportar poco valor. |

Los nombres de las zonas son provocadores. Una biblioteca concreta, pequeña y muy estable puede estar en la zona de dolor sin causar dolor real. Una abstracción nueva puede no tener consumidores todavía y seguir siendo necesaria. Además, $D$ pierde dirección: $(A=0.1,I=0.1)$ y $(A=0.9,I=0.9)$ producen $D=0.8$, pero plantean preguntas diferentes.

![secuencia principal](Recursos%20visuales/04-secuencia-principal.png)

**Uso responsable:** medir con criterios constantes, establecer una referencia, investigar cambios y contrastarlos con mantenimiento real. Añadir interfaces únicamente para acercarse a una recta puede aumentar complejidad sin resolver ninguna necesidad. Si $A$ o $I$ están indefinidas, tampoco corresponde presentar $D$ como una medida válida.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=9|PDF pp. 9–12; impresas pp. 45–48]].

## 6. Connascencia: precisar qué debe coincidir

Dos elementos presentan connascencia cuando cambiar uno exige adaptar el otro para conservar la corrección. El libro la presenta como **vocabulario de análisis**, no como una única puntuación comparable a $C_a$ o $C_e$.

### Cinco formas estáticas

Las formas estáticas pueden identificarse principalmente examinando código y contratos. Los siguientes ejemplos de PedidoClaro son propios.

| Forma | Acuerdo necesario | Ejemplo y consecuencia |
|---|---|---|
| Nombre | Identificador de una entidad | Renombrar `confirmarPedido` exige actualizar referencias. Un refactor automático ayuda dentro del código accesible; no actualiza por sí solo clientes externos. |
| Tipo | Tipo o estructura esperada | Cambiar `Importe` por una cadena exige adaptar operaciones y consumidores. En lenguajes dinámicos también existen expectativas de estructura. |
| Significado o convención | Interpretación de valores | Si `2` significa «confirmado», todos deben interpretarlo igual. Un nombre explícito reduce interpretaciones dispersas. |
| Posición | Orden de los valores | `entregar(origen, destino)` puede aceptar dos cadenas intercambiadas sin error de tipos y enviar el pedido a otro sitio. |
| Algoritmo | Procedimiento de cálculo | Caja y facturación deben aplicar la misma regla de redondeo si ambas calculan el importe exigible. |

Para el último caso, supongamos un importe decimal exacto de **2,345** y redondeo a dos decimales. Redondear los empates hacia arriba produce **2,35**; redondear al dígito par produce **2,34**. Ambos sistemas pueden parecer razonables y discrepar por un centavo. La solución requiere acordar la regla, su momento de aplicación y su versión; una función compartida o un único propietario del cálculo puede reducir duplicación. Este ejemplo presupone representación decimal exacta.

### Cuatro formas dinámicas

Las formas dinámicas dependen de cómo interactúan los elementos durante la ejecución.

| Forma | Acuerdo necesario | Ejemplo y consecuencia |
|---|---|---|
| Ejecución | Orden de operaciones | Confirmar antes de fijar las líneas deja un pedido incompleto. Un constructor validado puede impedir crear ese estado. |
| Timing o temporización | Momento, duración o concurrencia | Dos cajas leen que queda un pan y ambas lo reservan; el resultado depende de la intercalación de operaciones. |
| Valores | Relación entre varios valores | `total = subtotal - descuento` debe conservarse al modificar cantidades. Almacenar los tres sin control permite contradicciones. |
| Identidad | Referencia a la misma entidad | Cocina y caja deben actualizar el mismo pedido persistido; dos registros con atributos iguales no son necesariamente la misma entidad. |

La diferencia entre ejecución y timing importa: la primera exige un orden lógico; la segunda depende de la coordinación temporal. Introducir una espera fija no garantiza que el otro participante haya terminado. Para inventario, una operación atómica de reserva con comprobación del stock puede proteger la invariante en su frontera transaccional.

La connascencia de valores tampoco impone por sí sola una transacción distribuida. **Aclaración propia:** hay que determinar si la relación debe cumplirse inmediatamente o admite convergencia posterior, y diseñar el protocolo correspondiente. El requisito de negocio decide qué estados intermedios son aceptables.

### Fuerza, localidad y grado

La **fuerza** expresa cuánto cuesta reconocer y modificar el acuerdo: un nombre referenciado suele ser más fácil de cambiar que una carrera entre procesos. La **localidad** indica cuán próximos están los participantes; una regla dentro de un módulo es más fácil de coordinar que entre equipos y despliegues independientes. El **grado** considera cuántos participantes están involucrados: cambiar un acuerdo en dos lugares difiere de hacerlo en cuarenta.

![Fuerza, localidad y grado ](Recursos%20visuales/Diagramas/cap03-diagrama-04.png)

[Fuente editable del diagrama](Recursos%20visuales/Diagramas/cap03-diagrama-04.mmd)

**Interpretación:** los refactors hacen explícito el acuerdo o concentran su mantenimiento. **Límite:** no eliminan todas las dependencias. Una constante conserva semántica compartida; un objeto necesita contrato; una operación solo protege los datos bajo su control.

El libro recomienda debilitar acuerdos difíciles y mantener los más fuertes cerca. No conviene transformar su tipología en una clasificación universal: cambiar un nombre público usado por miles de clientes puede ser más costoso que ajustar un algoritmo privado en dos funciones vecinas.

La recomendación de concentrar connascencia dentro de fronteras debe leerse como **encapsular relaciones necesarias**, no crear dependencias gratuitas. También hay una ambigüedad terminológica: la «Rule of Degree» citada en la página impresa 53 habla de convertir formas fuertes en débiles, aunque la propiedad *grado* se había definido por cantidad de participantes. Mantener separadas ambas ideas evita confundir fuerza y alcance.

Fuente: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=13|PDF pp. 13–17; impresas pp. 49–53]].

## 7. Preguntas de comprobación

### 1. ¿Extraer Precios como servicio mejora necesariamente la modularidad?

> [!success]- Solución
> No. Hay que evaluar sus fronteras y acuerdos. La extracción física puede conservar dependencias internas mal definidas y añadir coordinación remota. Primero conviene identificar responsabilidad, contrato y motivo del despliegue independiente.

### 2. ¿Qué distingue cohesión secuencial de procedimental?

> [!success]- Solución
> En la secuencial, la salida de una operación alimenta a otra. En la procedimental, la relación exige un orden, sin requerir ese flujo de datos. «Ocurre después» no demuestra cohesión secuencial.

### 3. Cuatro métodos forman dos parejas que comparten campos. ¿Cuánto da LCOM1?

> [!success]- Solución
> Hay seis pares: cuatro disjuntos y dos compartidos. LCOM1 = max(4 − 2, 0) = 2. No se cuentan cuatro métodos como cuatro pares.

### 4. ¿LCOM1 = 0 demuestra una sola componente conexa?

> [!success]- Solución
> No. Tres métodos conectados por un campo y un cuarto aislado producen tres pares compartidos y tres disjuntos: LCOM1 = 0. Sin llamadas adicionales, LCOM4 sigue identificando dos componentes.

### 5. Con tres tipos abstractos, siete concretos, Ca = 6 y Ce = 2, ¿cuáles son A, I y D?

> [!success]- Solución
> A = 3/10 = 0,3; I = 2/8 = 0,25; D = |0,3 + 0,25 − 1| = 0,45. La distancia perpendicular es aproximadamente 0,318. Las líneas de código no intervienen.

### 6. Un módulo sin dependencias, ¿tiene I = 0?

> [!success]- Solución
> La fórmula da 0/0: está indefinida. Asignarle cero sería una convención de herramienta, no una consecuencia matemática ni una prueba de estabilidad.

### 7. ¿Una constante compartida elimina la connascencia de significado?

> [!success]- Solución
> Hace explícita parte del acuerdo mediante un nombre y facilita cambios coordinados. Los consumidores todavía deben interpretar ese estado correctamente; si lo persisten o intercambian externamente, también deben respetar su contrato y evolución.

## 8. Ejercicio aplicado: cancelar en PedidoClaro

**Supuestos propios:** `Clientes` contiene datos personales, consulta pedidos y ejecuta cancelaciones. Cada cancelación modifica el estado, libera existencias y recalcula importes. Web y Kiosco dependen de Clientes; Clientes depende de Inventario, Pagos y Correo. Tiene una interfaz y cuatro clases concretas.

Calcula $A$, $I$ y $D$. Propón una frontera para cancelaciones, identifica dos connascencias y explica cómo verificarías una mejora sin limitarte a bajar métricas.

> [!success]- Una solución razonada
> A = 1/5 = 0,2; Ca = 2; Ce = 3; I = 3/5 = 0,6; D = 0,2. Estos números no deciden la extracción.
>
> Una opción es trasladar el ciclo de vida y la cancelación a Pedidos, con una operación `cancelar(idPedido)` que aplique reglas según el estado. Clientes conserva datos personales. Antes de hacerlo, se comprueba qué datos de cliente necesita realmente la decisión.
>
> Hay connascencia de valores entre estado, existencias e importe; también de ejecución si el proceso exige validar la cancelación antes de ordenar un reembolso. Si intervienen servicios distintos, se deben especificar estados intermedios, reintentos y compensaciones según el negocio, sin suponer atomicidad global.
>
> La mejora se verifica con escenarios de cancelación repetida, fallo del proveedor de pagos y cambios en las reglas de devolución. Interesa que el cambio quede localizado, que los contratos sean comprensibles y que las invariantes se mantengan. Las métricas posteriores se recalculan sobre el grafo nuevo; no se promete que todas disminuyan.

## 9. Alcance y cautelas de la fuente

El cierre del capítulo conecta módulos con componentes como unidades de construcción arquitectónica, pero no desarrolla aquí un procedimiento completo para derivarlos del dominio: [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/02 Modularidad.pdf#page=18|PDF p. 18; impresa p. 54]].

Se revisaron las 18 páginas del escaneo, usando reconocimiento de texto y revisión visual; la ecuación LCOM96b se verificó en una ampliación de la página impresa 43. Se han señalado las ambigüedades relevantes: conteo de pares de LCOM, variantes de normalización, unidades del ejemplo de abstracción, interpretación de inestabilidad y nombres de las reglas de connascencia. Los diagramas y cálculos de esta nota son elaboraciones didácticas propias, no figuras reproducidas del libro.
