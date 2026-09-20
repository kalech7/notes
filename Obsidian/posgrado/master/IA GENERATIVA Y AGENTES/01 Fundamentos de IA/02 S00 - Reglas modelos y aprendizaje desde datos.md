---
title: "02 S00 - Reglas modelos y aprendizaje desde datos"
tags:
  - maestria/ia-generativa
  - estudio
---

# 02 S00 - Reglas modelos y aprendizaje desde datos

[[00 INICIO - Ruta de aprendizaje|Volver al índice]]

## 1. Qué es un modelo, con un ejemplo sencillo

Un mapa representa una ciudad, pero no contiene todo lo que hay en ella. Conserva lo necesario para orientarte. Un modelo hace algo parecido: representa ciertas relaciones de un problema para poder calcular o predecir algo.

Por ejemplo, un modelo de correos recibe información de un mensaje e intenta decidir si es spam. No reproduce todo lo que sabe una persona sobre comunicación; utiliza las características y relaciones que su diseño permite representar.

Por eso un modelo puede ser útil y equivocarse. Su representación es una simplificación.

## 2. Primera forma: una persona escribe las reglas

Supón que defines estas instrucciones:

```text
Si Ana entregó el proyecto y aprobó el examen,
entonces cumple los dos requisitos considerados.
```

El sistema revisa los hechos y aplica la regla. Esto es un ejemplo de enfoque **simbólico**: el conocimiento se expresa como hechos y reglas.

Puedes revisar cómo llegó a la conclusión. Pero si olvidaste incluir un tercer requisito, la conclusión puede ser insuficiente para la situación real. Razonar correctamente con una regla no garantiza que la regla describa todo el problema.

LISP y Prolog aparecen en la sesión por su importancia histórica. Para esta parte basta recordar que permitieron expresar programas y conocimiento de manera explícita; no necesitas aprender sus lenguajes ahora.

## 3. Segunda forma: ajustar a partir de ejemplos

En lugar de escribir todas las condiciones que hacen spam a un correo, entregas muchos correos clasificados. El modelo busca valores numéricos que le ayuden a predecir esas etiquetas.

Esos valores se llaman **parámetros**. Por ejemplo, un peso puede aumentar cuánto influye una característica en la decisión. **Entrenar** significa ajustar esos valores usando los datos.

El proceso tiene una secuencia:

1. El modelo recibe un ejemplo y hace una predicción.
2. Se compara con el resultado esperado.
3. Una función de pérdida mide cuánto se equivocó según el criterio elegido.
4. Un procedimiento de ajuste modifica los parámetros.
5. Se repite con más ejemplos y se comprueba el desempeño en datos nuevos.

Las personas siguen tomando decisiones: qué datos usar, qué modelo construir y qué error minimizar. Aprender de datos no elimina esas decisiones.

## 4. Entrenar no es lo mismo que usar el modelo

Durante el entrenamiento cambian los parámetros. Durante el uso ordinario del modelo, llamado **inferencia**, los parámetros permanecen fijos y cambia la entrada.

Piensa en estudiar y rendir un examen. Al estudiar ajustas lo que sabes; al responder utilizas lo aprendido. Es una analogía para distinguir etapas, no una afirmación de que una red aprende igual que una persona.

## 5. Por qué memorizar puede dar malos resultados

Bishop muestra una curva que pasa por todos los puntos de entrenamiento, pero hace oscilaciones extrañas entre ellos. Captura también pequeñas variaciones que no representan la tendencia general. A esto se le llama **sobreajuste**.

Imagina mediciones de temperatura con algo de ruido del sensor. Una curva demasiado rígida puede no seguir la tendencia; una demasiado flexible puede perseguir cada error de medición. Queremos que funcione en horas que no medimos, no solo que copie los datos conocidos.

Por eso se separan conjuntos de datos: entrenamiento para ajustar; validación para orientar decisiones de desarrollo; prueba para evaluar al final. Si usas la prueba repetidamente para cambiar el modelo, deja de ser una comprobación independiente.

**Capacidad** es lo que la familia del modelo puede representar. **Generalización** es cómo funciona lo que aprendió en datos nuevos. Tener más capacidad no garantiza generalizar mejor.

## 6. Qué añade el aprendizaje profundo

En muchos métodos tradicionales, una persona diseña características como longitud del correo o presencia de una palabra. Una red profunda puede aprender representaciones intermedias útiles a partir de los datos.

Para entender qué significa esto, comienza con una unidad sencilla: [[03 S00 - Perceptrón redes neuronales y XOR|el perceptrón]].

## Fuentes de esta explicación

Las explicaciones y ejemplos están desarrollados en esta nota. Los enlaces permiten consultar su base sin que necesites leer los libros completos.

- [[sesion-00.pdf#page=11|Sesión 00, páginas 11–13]]
- [[bishop-2006-prml.pdf#page=26|Bishop, §1.1, pp. impresas 6–8; PDF 26–28]]

## Preguntas para comprobar que entendiste

Intenta responder antes de desplegar cada respuesta.

> [!question]- ¿Qué diferencia hay entre un modelo y la realidad?
> El modelo es una representación con supuestos y simplificaciones. Puede ser útil y aun así fallar en situaciones que sus supuestos no cubren.

> [!question]- ¿Por qué una derivación lógica no garantiza una conclusión verdadera en el mundo?
> Porque depende de la corrección y suficiencia de los hechos y reglas. Una derivación válida a partir de premisas equivocadas puede producir una conclusión inaplicable.

> [!question]- ¿Qué cambia al entrenar y qué suele permanecer fijo al usar un modelo?
> Durante el entrenamiento se ajustan parámetros. Durante la inferencia ordinaria se usan esos parámetros fijos; cambian las entradas y las activaciones.

> [!question]- ¿Por qué no basta con medir aciertos en los ejemplos de entrenamiento?
> Porque puede haber memorización o sobreajuste. Se necesitan ejemplos nuevos para evaluar generalización.


> [!question]- ¿Por qué pasar por todos los puntos puede ser una mala señal?
> Porque esos puntos pueden contener ruido. Ajustarlo exactamente puede producir predicciones inestables entre observaciones.

> [!question]- ¿Capacidad y generalización son sinónimos?
> No. Capacidad describe qué puede representar la familia; generalización describe el desempeño aprendido en casos nuevos.
