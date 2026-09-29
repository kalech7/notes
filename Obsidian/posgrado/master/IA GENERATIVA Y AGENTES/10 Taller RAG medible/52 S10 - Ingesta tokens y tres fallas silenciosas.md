---
title: "52 S10 - Ingesta tokens y tres fallas silenciosas"
sesion: "10"
fecha: 2026-09-27
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-10.pdf]]"
---

# 52 S10 - Ingesta tokens y tres fallas silenciosas

[[50 S10 - Guía para comprender el taller RAG|Guía de la sesión 10]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[51 S10 - Del documento a una respuesta con evidencia]]

Siguiente: [[53 S10 - Golden set y límites de lo respondible]]

## 1. Qué significa una falla silenciosa

Una excepción interrumpe o señala una operación fallida. Una falla silenciosa puede producir estructuras válidas, guardar registros y devolver respuestas, pero perder la información que necesitábamos. «No hubo error» solo comprueba una parte del contrato del programa.

La Parte 0 del PDF estudia tres casos: un documento sin texto útil, un fragmento truncado y un índice que devuelve vecinos incluso cuando no dispone de la respuesta.

## 2. Primera falla: el PDF visible pero vacío para el lector

Un PDF puede contener imágenes de páginas en lugar de caracteres codificados. Tú lees las letras de la imagen; el extractor de texto convencional no realiza necesariamente reconocimiento óptico de caracteres, u **OCR**.

La presentación explica que una versión anterior añadía marcadores de página al texto vacío. La cadena resultante ya no estaba vacía, pero tampoco contenía el contenido académico. Era posible generar e indexar un fragmento compuesto esencialmente por esos marcadores.

La revisión descrita cuenta letras y dígitos después de quitar los marcadores y aplica un umbral de **200 caracteres útiles por documento**. Si no se alcanza, avisa y omite el documento.

El umbral es una **heurística**: una regla práctica para detectar sospechas. No demuestra que todo documento rechazado sea un escaneo, ni que todo documento aceptado esté bien leído. Un aviso breve auténtico podría quedar por debajo de 200; un PDF largo con extracción defectuosa podría superarlo.

**Diagnóstico correcto:** registra qué se extrajo, cuánto y de qué páginas; compara una muestra con la página visible. Si haces OCR, revisa cifras, signos, tablas y orden de lectura. La existencia de texto no garantiza su fidelidad.

## 3. Segunda falla: texto guardado y texto representado no coinciden

![[36-s10-truncamiento.png]]

**Cómo leer la imagen:** el bloque completo sigue almacenado. Para crear el embedding solo entra el prefijo dentro del presupuesto. Si luego el sistema recupera ese registro, puede enviar al generador el bloque completo. El sufijo puede leerse en la respuesta aunque no haya contribuido a que el buscador encontrara ese fragmento.

Un **token** es una unidad del tokenizador: puede ser una palabra, una parte de ella, un signo u otra secuencia. La relación palabras/tokens depende del idioma, el texto y el tokenizador. Mide con el tokenizador del modelo utilizado; contar espacios no sustituye esa medición.

En el caso del PDF, el modelo del laboratorio tiene un límite configurado de 128 tokens y la versión anterior cortaba a 900 palabras. El límite de 128 es propio del caso descrito, no de todos los modelos de embeddings.

Para entenderlo sin mezclar unidades, usa este ejemplo separado: un fragmento tiene **900 tokens de contenido** y la secuencia admite 128 en total. Si la codificación necesita 2 tokens especiales, el presupuesto útil es:

$$B=128-2=126\text{ tokens de contenido}$$

La fracción del contenido que entra es:

$$\frac{126}{900}=0{,}14=14\%$$

Quedan 774 tokens fuera de esa entrada. La diapositiva usa $128/900\approx14{,}2\%$ como cota explicativa bajo su conversión palabras/tokens. No es un porcentaje medido del texto semánticamente comprendido. Ni siquiera el 14 % de tokens implica el 14 % del significado: las partes no contienen la misma cantidad de información.

> [!warning] El número 2 no es universal
> La reserva para tokens especiales depende del modelo y de cómo se construye su entrada. El PDF describe `max_seq_tokens - 2` para su laboratorio. Una implementación general debe comprobar tokens especiales, prefijos y cualquier otra envoltura del encoder.

La documentación de [Sentence Transformers](https://www.sbert.net/docs/package_reference/sentence_transformer/model.html?highlight=hub) describe el límite de secuencia y su configuración. Cambiar un número en la configuración no demuestra que el modelo pueda procesar correctamente cualquier longitud nueva.

## 4. Por qué comparar embeddings revela el truncamiento

Sean $x$ un texto largo y $x_B$ su prefijo efectivo. Si el procesamiento de ambos genera exactamente la misma secuencia de entrada y el encoder se ejecuta de forma determinista:

$$f(x)=f(x_B)\quad\Longrightarrow\quad\cos(f(x),f(x_B))=1$$

Esto requiere vectores no nulos. En la práctica puede observarse un valor cercano a 1 por tolerancias numéricas. Debes asegurar que el prefijo se construyó con la misma tokenización y los mismos tokens especiales.

**Ejemplo conceptual:** dos versiones comparten el principio y difieren solo en una cláusula posterior al corte. Si ambas producen el mismo vector, ese vector no está distinguiendo el cambio de cláusula.

Un coseno cercano a 1, por sí solo, no prueba truncamiento: dos textos realmente similares también pueden tener vectores parecidos. La evidencia convincente combina longitud, límite efectivo, entrada procesada y una modificación controlada del sufijo.

La precisión importante es esta: lo que quedó fuera **no está representado directamente en ese embedding**. El fragmento aún puede recuperarse gracias al prefijo; no es correcto afirmar que todo su sufijo será imposible de encontrar bajo cualquier consulta.

## 5. Tamaño y solapamiento: cómo se relacionan

Si cada fragmento tiene $C$ tokens y el solapamiento es $O$, el avance entre comienzos es $C-O$. Necesitamos $0\le O<C$ para que haya avance.

Con $L=500$, $C=126$ y $O=26$, el avance es 100. En un esquema que deja un último fragmento parcial:

$$n=1+\left\lceil\frac{L-C}{C-O}\right\rceil
=1+\left\lceil\frac{374}{100}\right\rceil=5$$

Los comienzos son 0, 100, 200, 300 y 400. Las longitudes son 126, 126, 126, 126 y 100: se procesan 604 tokens de contenido contando repeticiones, frente a 500 originales.

El solapamiento ayuda a conservar una frase cortada en un borde, pero repite información, añade vectores y puede llenar el top-k con fragmentos casi duplicados. No arregla un PDF vacío ni un límite que cada fragmento sigue excediendo.

## 6. Tercera falla: devolver vecinos no demuestra respuesta

Un ranking responde a «¿qué candidatos son más próximos dentro de los disponibles?». No responde automáticamente a «¿existe suficiente evidencia para contestar?». Si todos los documentos son inadecuados, alguno puede seguir ocupando el primer puesto.

El PDF compara una pregunta ausente del corpus con otra cuya respuesta está en un documento rechazado. Las dos pueden producir vecinos plausibles. El puntaje solo no permite reconstruir la causa. Para separarlas necesitas el inventario original, el registro de ingesta y una anotación explícita del corpus evaluado; continúa en [[53 S10 - Golden set y límites de lo respondible]].

**Fuente:** PDF, pp. 7–10. Las cuentas con 900 tokens y el ejemplo de solapamiento son propios; no se ejecutaron las reproducciones de la Parte 0.
