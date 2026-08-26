---
tags:
  - machine-learning
  - embeddings
  - representacion-vectorial
related: "[[00 Índice - Espacios vectoriales y embeddings]]"
---

# Embeddings y representación de objetos

Anterior: [[03 Independencia, bases, dimensión y subespacios]] · Siguiente: [[05 Comprobación con NumPy]]

## 1. De objetos a números

Un algoritmo necesita trabajar con números. Por eso definimos una función de representación

$$
\varphi:X\to\mathbb{R}^d,
$$

donde:

- $X$ es el dominio de objetos: documentos, palabras, imágenes o mediciones;
- $\varphi$ es la regla de representación;
- $\mathbb{R}^d$ es el codominio;
- $\varphi(x)$ es el vector concreto asignado al objeto $x$;
- $d$ es la cantidad de componentes de la representación.

Un **embedding** es precisamente este tipo de asignación vectorial cuando busca colocar objetos en un espacio donde su geometría resulte útil para una tarea.

### Qué es el dominio

El **dominio** es el conjunto de todos los objetos que la función puede recibir como entrada. En la expresión $\varphi:X\to\mathbb{R}^d$, el dominio es $X$.

Por ejemplo, si $\varphi$ representa palabras mediante vectores, $X$ puede ser el vocabulario del modelo. Si representa imágenes, $X$ puede ser el conjunto de imágenes con un formato determinado. Para cada objeto $x\in X$, la función produce un vector $\varphi(x)\in\mathbb{R}^d$.

> [!example] Entrada y salida
> Si $X$ es un conjunto de documentos y $d=3$, entonces $\varphi$ recibe un documento $x\in X$ y devuelve tres componentes numéricas: $\varphi(x)=(a_1,a_2,a_3)\in\mathbb{R}^3$.

![[assets/23-embedding.jpg|850]]

## 2. Objeto, vector y coordenadas

![[assets/11-objeto-vector-coordenadas.jpg|850]]

Supón que $d$ es un documento y elegimos dos características:

1. frecuencia de la palabra «modelo»;
2. frecuencia de la palabra «datos».

Podríamos definir

$$
\varphi(d)=v\in\mathbb{R}^2.
$$

Aquí hay tres entidades diferentes:

- **Objeto $d$:** el documento real, con toda su información.
- **Vector $v=\varphi(d)$:** un resumen matemático construido con las características seleccionadas.
- **Coordenadas $[v]_B$:** los números que describen $v$ en una base ordenada $B$.

### Qué es una base ordenada

Una **base** de un espacio vectorial es un conjunto de vectores linealmente independientes con los que se puede construir cualquier vector del espacio. Decimos que la base está **ordenada** porque importa la posición de cada vector base:

$$
B=(b_1,b_2,\ldots,b_d).
$$

Todo vector $v$ del espacio puede escribirse de manera única como

$$
v=c_1b_1+c_2b_2+\cdots+c_db_d.
$$

Sus coordenadas respecto de $B$ son la lista ordenada de coeficientes

$$
[v]_B=(c_1,c_2,\ldots,c_d).
$$

El orden es esencial: la primera coordenada multiplica a $b_1$, la segunda a $b_2$, y así sucesivamente. Por ejemplo, si $B=(b_1,b_2)$ y $v=2b_1+3b_2$, entonces $[v]_B=(2,3)$. Si invertimos el orden y usamos $B'=(b_2,b_1)$, el vector no cambia, pero sus coordenadas pasan a ser $[v]_{B'}=(3,2)$.

En $\mathbb{R}^d$ suele utilizarse la **base canónica** $E=(e_1,\ldots,e_d)$. Por eso, cuando un modelo devuelve el embedding $(a_1,\ldots,a_d)$, normalmente esos números se interpretan como sus coordenadas en dicha base.

> [!important] El vector no es el objeto
> La representación conserva cierta información y descarta otra. Dos documentos distintos incluso podrían recibir el mismo vector si las características elegidas no los distinguen.

## 3. Embeddings aprendidos

En modelos modernos, las componentes no suelen ser características diseñadas a mano como frecuencias. El sistema aprende $\varphi$ a partir de datos y un objetivo de entrenamiento. Aun así, la estructura conceptual no cambia:

```mermaid
flowchart LR
    X["Objeto x"] --> F["Función aprendida φ"]
    F --> V["Vector φ(x) en Rᵈ"]
    V --> M["Medida de comparación"]
    M --> T["Tarea: buscar, clasificar, agrupar"]
```

La utilidad del espacio depende de tres elementos:

1. **datos** usados para construir o entrenar la representación;
2. **método** que define cómo se produce el vector;
3. **medida** usada para comparar vectores.

## 4. Cercanía y medidas

Decir que dos embeddings están «cerca» no tiene significado hasta escoger una medida. Dos opciones comunes son:

### Distancia euclídea

$$
d(x,y)=\lVert x-y\rVert_2.
$$

Valores pequeños indican poca separación geométrica.

### Similitud coseno

$$
\operatorname{cos}(x,y)=\frac{x^Ty}{\lVert x\rVert_2\lVert y\rVert_2}.
$$

Mide alineación de direcciones. Cerca de $1$ indica orientación similar; cerca de $0$, ortogonalidad; cerca de $-1$, orientación opuesta.

Estas medidas no son intercambiables: una considera la diferencia absoluta y la otra normaliza la magnitud. La medida debe estar alineada con cómo se construyó el embedding y con la tarea.

## 5. Qué se puede y qué no se puede inferir

### Una coordenada aislada no tiene semántica garantizada

En un embedding aprendido, no debemos asumir que la componente 17 significa «formalidad» o que la 83 significa «animal». El significado puede estar distribuido entre muchas componentes y depender de la representación completa.

### Cercanía no implica causalidad

Si dos objetos quedan próximos, podemos afirmar que sus representaciones son similares según la medida elegida. No podemos concluir que uno causa al otro.

### La geometría depende de la construcción

Distancias, ángulos y agrupamientos son interpretables solo en relación con el método, los datos y la métrica. Cambiar cualquiera de ellos puede cambiar las relaciones observadas.

### La reducción a dos dimensiones puede distorsionar

Un gráfico 2D de embeddings de dimensión alta es otra transformación. Puede ayudar a explorar, pero no preserva necesariamente todas las distancias ni autoriza conclusiones absolutas.

## 6. Papel de la base en los embeddings

Un embedding es un vector; los números que vemos son sus coordenadas en la base usada por el modelo. Un cambio de base invertible puede alterar todas las componentes sin perder la información lineal del vector. Por eso atribuir significado directo a un eje individual suele ser frágil.

Lo que a menudo importa más es la estructura relacional preservada: cercanías, direcciones, agrupamientos o separabilidad para una tarea concreta.

## 7. Ejemplo conceptual

Supón tres palabras $w_1,w_2,w_3$ con

$$
f(w_1)=(0.8,-0.1,0.4),\quad
f(w_2)=(-0.3,0.9,0.2),\quad
f(w_3)=(0.1,0.5,-0.6).
$$

Sabemos que cada palabra se ha representado con tres números. Sin conocer cómo se construyó $f$ ni qué medida usa el sistema, no podemos declarar qué significa cada coordenada ni cuál palabra es «más parecida» a otra de manera justificada.

## Preguntas de repaso

1. En $\varphi:X\to\mathbb{R}^d$, ¿qué representa cada símbolo?
2. ¿Por qué $\varphi(x)$ no es el objeto $x$?
3. ¿Qué debes especificar antes de hablar de cercanía?
4. ¿Por qué cercanía geométrica no prueba causalidad?
5. ¿Qué riesgo existe al interpretar una sola componente de un embedding?
