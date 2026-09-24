---
title: "37 S08 - Estrategias de fragmentación y solapamiento"
sesion: "08"
tags:
  - maestria/ia-generativa
  - rag
  - estudio
fuente: "[[sesion-08.pdf]]"
---

# 37 S08 - Estrategias de fragmentación y solapamiento

[[00 INICIO - Ruta de aprendizaje|Inicio de la materia]] · [[34 S08 - Guía para entender fragmentación y recuperación|Guía de la sesión 08]]

## 1. El problema es conservar una unidad de sentido

Fragmentar consiste en decidir qué información debe viajar junta. Una regla, su sujeto y sus condiciones suelen necesitarse mutuamente. Si separas demasiado, recuperas piezas ambiguas. Si agrupas demasiado, mezclas temas y gastas contexto en información que no responde a la pregunta.

Este es el compromiso entre **precisión de la unidad buscada** y **suficiencia del contexto**. Un fragmento pequeño puede localizar un dato con precisión y dejar fuera su excepción. Uno grande puede incluir ambas cosas y diluirlas entre otros asuntos. No existe un tamaño universal que resuelva todos los documentos.

## 2. Cómo funciona cada estrategia y por qué existe

| Estrategia | Cómo decide los cortes | Qué intenta resolver | Qué puede costar |
| --- | --- | --- | --- |
| Fija | Divide cada cierto número de unidades | Simplicidad y tamaño controlado | Puede partir oraciones o relaciones |
| Ventana deslizante | Avanza menos que el tamaño de la ventana | Conserva parte de la frontera anterior | Duplica texto y candidatos |
| Estructural | Usa títulos, párrafos y secciones | Mantiene organización explícita | Depende de extraer bien la estructura |
| Semántica | Busca cambios de significado con algún criterio | Agrupa contenido relacionado | Añade cómputo y decisiones que hay que evaluar |
| Jerárquica | Busca unidades pequeñas y recupera contexto padre | Combina precisión de búsqueda con contexto amplio | Mantiene relaciones hijo-padre y ocupa más contexto |
| Contextual | Añade información de procedencia o contexto | Evita fragmentos aislados o ambiguos | Consume tokens; el contexto generado puede ser incorrecto |

El PDF agrupa «semántico o estructural» en una familia, pero conviene distinguirlos: respetar un salto de párrafo no equivale a medir cambios de significado. Asimismo, estas estrategias pueden combinarse: dividir por secciones, subdividir las largas con ventanas y conservar el título en cada fragmento.

Añadir el título original es una forma sencilla de contextualizar. Si se genera un resumen adicional con un modelo, debe mantenerse la distinción entre fuente original y texto derivado. No conviene convertir una inferencia añadida en supuesta evidencia documental.

### Fragmentar por estructura: seguir relaciones ya presentes

Un documento suele señalar su organización mediante títulos, subtítulos, párrafos, listas y tablas. Un divisor estructural utiliza esas señales para proponer límites. Puede empezar por secciones y subdividir las que exceden el presupuesto en párrafos; si todavía son demasiado largas, avanzar a oraciones o cortes menores. Esa aplicación sucesiva de criterios es lo que se suele llamar división recursiva.

El propósito no es confiar ciegamente en el formato. Un encabezado debe conservarse o asociarse a los fragmentos de su sección; una lista puede depender de la frase que la introduce; una fila de una tabla puede necesitar encabezados de columna y unidades. La estructura es útil porque expresa relaciones, y pierde valor si solo conservas saltos de línea sin saber qué significan.

### Fragmentar por semántica: decidir dónde cambia la unidad temática

Una posibilidad consiste en representar oraciones o grupos de oraciones y comparar regiones vecinas. Una caída de semejanza puede sugerir un cambio de tema y, por tanto, un lugar para cortar. Después hacen falta reglas de longitud mínima, máxima y manejo de casos ambiguos.

La palabra «semántica» no significa que el sistema conozca perfectamente los límites de cada idea. El resultado depende del modelo, la comparación y el umbral elegido. Una excepción puede diferir de la regla en su significado y, precisamente por eso, necesitar permanecer con ella. Un cambio temático es una pista, no una definición completa de unidad de respuesta.

### Fragmentación jerárquica: buscar pequeño y leer con contexto

Aquí se conservan dos escalas. Los fragmentos pequeños son unidades de búsqueda y tienen una referencia a una sección mayor, llamada **padre**. Si se recupera un fragmento hijo, el sistema puede entregar la sección padre o una región ampliada alrededor de él.

Esto intenta resolver una tensión: para encontrar una coincidencia precisa interesa una unidad pequeña; para interpretar la respuesta puede hacer falta una unidad mayor. La conexión padre-hijo permite usar ambas, en vez de exigir que un único tamaño satisfaga las dos necesidades.

Pero recuperar el padre vuelve a consumir más contexto. Si cinco hijos pertenecen al mismo padre, no conviene copiar cinco veces la sección completa. Se deben unir esas referencias y comprobar el presupuesto final. El método desplaza parte de la decisión desde la ingesta hacia la selección del contexto.

### Contextualizar: devolver al fragmento las referencias que perdió

Separar un pasaje puede quitarle el nombre de la entidad, el tema o la versión que estaban en el título. Incorporar esa información ayuda a interpretar el fragmento. Si se añade **antes de calcular el embedding**, puede afectar su recuperación; si solo se añade al prompt, puede ayudar a interpretarlo, pero no mejora retrospectivamente el vector ya calculado.

Este detalle conecta dos decisiones que suelen mezclarse: qué texto representas para buscar y qué texto muestras para responder. Pueden diferir, siempre que mantengas la procedencia y no presentes información generada como si fuera parte literal de la fuente.

## 3. Qué es el solapamiento

El **solapamiento** es la región que comparten dos fragmentos consecutivos. Con tamaño $C$ y solapamiento $V$, la siguiente ventana avanza $S=C-V$ unidades. Se requiere $0\leq V<C$ para avanzar.

Su razón de ser es dar una segunda oportunidad a la información situada cerca de un corte. Puede mantener juntas relaciones que una partición sin solapamiento separaría. No garantiza conservar cualquier idea: una dependencia muy larga o un solapamiento insuficiente todavía pueden dejar información necesaria fuera.

![Relación entre solapamiento y número de ventanas](<../Recursos visuales/22-s08-solapamiento.png>)

La curva muestra el multiplicador aproximado del número de ventanas para textos largos. Al acercar el solapamiento al tamaño del fragmento, se avanza muy poco y se repite mucho trabajo. Por eso «más solapamiento» no es una mejora gratuita.

## 4. Por qué aparece la fórmula del costo

Sin solapamiento, cada fragmento cubre aproximadamente $C$ unidades nuevas. Con solapamiento, solo aporta $C-V$ unidades nuevas. Para recorrer el mismo texto, la razón aproximada del número de fragmentos es:

$$F\approx\frac{C}{C-V}=\frac{1}{1-V/C}.$$

Si se repite el 20 % de cada ventana, se avanza el 80 %: $F\approx 1/0.8=1.25$. Se generan aproximadamente un 25 % más de fragmentos, no un 20 % más. La diferencia aparece porque el costo se compara con el avance restante.

| Configuración del PDF | Unidad | Multiplicador aproximado | Aumento aproximado |
| --- | --- | ---: | ---: |
| 512 / 102 | tokens del modelo del Lab | 1,249 | 24,9 % |
| 512 / 64 | tokens | 1,143 | 14,3 % |
| 500 / 100 | tokens aproximados en el material | 1,250 | 25,0 % |
| 300 / 80 | caracteres del notebook | 1,364 | 36,4 % |

Aquí se comparan proporciones de repetición; la tabla no convierte caracteres en tokens ni demuestra que las configuraciones produzcan fragmentos equivalentes.

## 5. La precisión que falta en «el costo es exacto»

Para un texto no vacío de longitud $L$, ventanas de tamaño máximo $C$, avance $C-V$ y una última ventana que puede ser parcial, una implementación que se detiene al cubrir el final produce:

$$N=\begin{cases}1,&L\leq C\\1+\left\lceil\frac{L-C}{C-V}\right\rceil,&L>C.\end{cases}$$

El símbolo $\lceil x\rceil$ significa redondear hacia arriba. La primera ventana cubre hasta $C$ unidades; de las $L-C$ restantes, cada nueva ventana cubre hasta $C-V$ unidades nuevas. Esa es la razón de dividir y redondear: una fracción pendiente también necesita una ventana.

La razón $C/(C-V)$ describe el régimen de textos largos y cortes regulares. En corpus finitos, los bordes, redondeos y documentos cortos cambian la razón exacta. Si todo el documento cabe en una sola ventana, no hay otra ventana con la que solapar.

Además, número de fragmentos no es idéntico a bytes totales del índice ni a latencia. Influyen metadatos, estructura del índice, procesamiento por lotes y longitud efectiva de las entradas. La fórmula ayuda a anticipar repetición; no sustituye medir el sistema.

### El costo que no aparece en la fórmula: diversidad de evidencia

El solapamiento puede producir fragmentos casi idénticos que obtienen puntajes parecidos. Si varios ocupan los primeros lugares, un top-k aparentemente amplio puede contener muy poca información distinta. Tener cinco resultados no implica tener cinco aportes complementarios.

Esto explica por qué hay que inspeccionar duplicación al construir el contexto. Quitar repeticiones puede liberar espacio para otro pasaje necesario. No significa eliminar toda semejanza: dos textos parecidos pueden diferir precisamente en una condición importante. La decisión depende de qué información adicional conserva cada candidato.

## 6. Cómo decidir con criterio

Primero conserva las unidades de sentido del documento y comprueba que caben en el codificador. Después establece un baseline sencillo y observa qué relaciones se pierden en las fronteras. Ajusta el solapamiento por ese problema concreto, no porque un porcentaje parezca habitual.

El PDF propone empezar por párrafos o grupos de oraciones. Es una orientación estructural útil, no una exención del límite de tokens: un párrafo largo también puede excederlo. Cuando cambian los cortes, hay que reconstruir las representaciones y los índices afectados.

> [!abstract] Para recordar
> **Cortar decide qué viaja junto; solapar repite para proteger fronteras.** El objetivo es conservar sentido con un costo justificable.

> [!question] Comprueba que lo entendiste
> ¿Por qué un fragmento más pequeño puede empeorar una respuesta aunque su embedding sea más específico?
>
> Porque la búsqueda puede localizar la regla y dejar fuera la condición que cambia su interpretación. Precisión temática y suficiencia de evidencia son cosas distintas.

**Fuente:** [[sesion-08.pdf#page=13|páginas 13–15]]. La fórmula finita y los matices de costo son derivaciones propias. Continúa con [[38 S08 - Búsqueda léxica densa y fusión RRF]].
