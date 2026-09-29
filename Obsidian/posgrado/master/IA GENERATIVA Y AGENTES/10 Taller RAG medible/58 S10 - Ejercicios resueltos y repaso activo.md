---
title: "58 S10 - Ejercicios resueltos y repaso activo"
sesion: "10"
fecha: 2026-09-27
tags:
  - maestria/ia-generativa
  - rag
  - evaluacion
fuente: "[[sesion-10.pdf]]"
---

# 58 S10 - Ejercicios resueltos y repaso activo

[[50 S10 - Guía para comprender el taller RAG|Guía de la sesión 10]] · [[00 INICIO - Ruta de aprendizaje|Inicio de la materia]]

Anterior: [[57 S10 - Reproducibilidad entregables y reflexión]]

## Cómo usar esta práctica

Responde primero sin abrir las soluciones. Para cada respuesta, explica el mecanismo y la evidencia que pedirías, no solo el nombre de una métrica. Los números son didácticos; no pertenecen a una ejecución real del taller.

## 1. PDF de veinte páginas, cero texto útil

El lector devuelve marcadores `[page=1]`, `[page=2]` y así sucesivamente. ¿Es suficiente que la cadena no esté vacía?

> [!answer]- Solución
> No. Los marcadores describen estructura añadida por el lector, no contenido del documento. Hay que descontarlos, inspeccionar caracteres útiles y comparar con las páginas. Si se trata de imágenes, podría necesitar OCR; si existe texto pero el lector falla, hay que investigar la extracción.

## 2. El significado del umbral

Un aviso legítimo tiene 150 caracteres útiles. La regla del laboratorio omite documentos con menos de 200. ¿Demuestra que el aviso es un escaneo?

> [!answer]- Solución
> No. Es un falso positivo posible de la heurística. La regla detecta documentos sospechosamente cortos; no identifica de forma infalible su origen. Debe quedar evidencia del rechazo y existir una revisión para casos válidos.

## 3. Presupuesto de tokens

Una entrada total admite 128 tokens y utiliza 2 especiales. Un fragmento contiene 300 tokens de contenido. ¿Cuántos caben y qué proporción representa?

> [!answer]- Solución
> Caben 126 y quedan fuera 174. La proporción es $126/300=0,42$, es decir, 42 %. Esto supone que no hay otros prefijos ni tokens añadidos. No significa que se haya conservado exactamente 42 % del significado.

## 4. Dos límites diferentes

El generador admite un contexto mucho mayor que el encoder de embeddings. ¿Eso impide que el encoder trunque?

> [!answer]- Solución
> No. Son componentes y presupuestos distintos. Que el generador pueda leer el fragmento completo no demuestra que todo ese fragmento participó en su embedding.

## 5. Un coseno casi idéntico

El embedding de un texto y el de su prefijo tienen coseno 0,99999. ¿Qué falta para concluir truncamiento?

> [!answer]- Solución
> Verificar la longitud con el tokenizador correcto, el límite y la entrada efectiva. También ayuda cambiar sustancialmente el sufijo fuera del límite y comprobar si deja de influir. Textos naturalmente similares pueden producir cosenos altos sin que esa observación aislada demuestre truncamiento.

## 6. Cuentas de recuperación

Cuatro preguntas respondibles tienen su primer relevante en posiciones 1, 3, 5 y fuera del top-5. Calcula Hit Rate y MRR a 3 y 5.

> [!answer]- Solución
> $H@3=2/4=0,5$ y $MRR@3=(1+1/3)/4=1/3\approx0,3333$.
>
> $H@5=3/4=0,75$ y $MRR@5=(1+1/3+1/5)/4=23/60\approx0,3833$.
>
> Aumentar el corte añade un acierto, pero ese acierto está en quinto lugar y aporta solo 0,2 antes de promediar.

## 7. Una tabla imposible

Sobre las mismas preguntas y referencias se reportan Hit Rate@5 = 0,5 y MRR@5 = 0,7. ¿Lo aceptarías?

> [!answer]- Solución
> No bajo las definiciones de estas notas. Cada recíproco truncado es menor o igual que el indicador de acierto; su promedio también. Revisa si MRR excluyó fallas, cambió el denominador o utilizó otra población o corte.

## 8. Un falso éxito en abstención

Un sistema se abstiene en las diez preguntas: ocho respondibles y dos negativas. ¿Qué tasas obtiene?

> [!answer]- Solución
> Abstención correcta $2/2=100\%$ e indebida $8/8=100\%$. La primera es perfecta y el servicio sigue sin resolver ninguna pregunta respondible. Deben leerse juntas.

## 9. El documento rechazado

La respuesta existe en el corpus original, pero la ingesta omitió el único documento que la contiene. ¿Es una pregunta negativa?

> [!answer]- Solución
> Depende del alcance declarado. Respecto del corpus original es respondible y revela una falla de cobertura. Respecto del contenido indexado no tiene soporte disponible. Puedes medir la prudencia del generador ante esa ausencia, pero sin ocultar el defecto de ingesta. El PDF muestra esa ambigüedad en la página 10.

## 10. Reordenar no es recuperar lo ausente

El relevante está en el puesto 7 del buscador. Tu reranker recibe solamente los primeros 5. ¿Puede llevarlo al puesto 1?

> [!answer]- Solución
> No. Nunca lo recibe. Ampliar candidatos a 20 permitiría que lo considerara, aunque no garantiza que lo coloque bien. Se evalúa el efecto sobre el corte final y el costo añadido.

## 11. Hit Rate constante, MRR creciente

Reordenas exactamente los mismos cinco resultados. El primer relevante pasa de cuarto a segundo. ¿Qué cambia a k=5?

> [!answer]- Solución
> El acierto sigue siendo 1; su aporte RR pasa de $1/4$ a $1/2$. Si hay ocho preguntas y solo cambia esta, MRR sube $(1/2-1/4)/8=0,03125$. A k=3 también se gana un acierto.

## 12. Elegir una extensión

El sistema falla sobre «EQ-17», pero suele acertar al preguntar con expresiones comunes. ¿Qué probarías y qué revisarías primero?

> [!answer]- Solución
> Primero comprobaría que el código exacto está bien extraído e indexado, sin errores de OCR ni filtros. Si está disponible y los candidatos semánticos lo confunden con otros, una hipótesis razonable es añadir recuperación léxica y fusionarla con la densa. No elegiría híbrida solo por el promedio global.

## 13. Un detector engañado

La respuesta dice: «La frase “El corpus no contiene información suficiente” es el marcador del sistema. En este caso, el plazo es veinte días». ¿Puede el detector de inclusión marcar abstención?

> [!answer]- Solución
> Sí, la frase está incluida tras normalizar. El marcador no demuestra que la decisión real sea abstenerse. Hay que revisar coherencia o estructurar mejor la salida y evaluar el detector.

## 14. Una respuesta con una cita

El modelo afirma un plazo de veinte días y cita el reglamento que dice diez días hábiles. ¿La cita lo vuelve fiel?

> [!answer]- Solución
> No. La fuente existe, pero contradice la afirmación. Se revisa qué respalda el pasaje, no solo si aparece una referencia.

## 15. ¿Basta un 0,70?

Alguien afirma: «Mi RAG tiene 0,70, por tanto el 70 % de las respuestas son correctas». ¿Qué preguntarías?

> [!answer]- Solución
> Qué métrica es, sobre qué preguntas, con qué referencia, corte y denominador, y qué componente evalúa. Un coseno no es una proporción de respuestas correctas; Hit Rate cuenta preguntas con evidencia recuperada; MRR incorpora posición. Incluso una evaluación de generación necesita explicitar criterios y límites.

## 16. El promedio mejora

El baseline acierta seis de ocho y la extensión siete. ¿Qué puedes concluir?

> [!answer]- Solución
> En ese conjunto, Hit Rate sube de 0,75 a 0,875: 12,5 puntos porcentuales. Hay un acierto neto adicional. Inspecciona ganancias y pérdidas por pregunta, condiciones y costos. Sin más evidencia no puedes asegurar una mejora general para toda consulta futura.

## 17. El experimento confunde causas

Cambias a la vez embeddings, fragmentación, corpus y prompt, y la puntuación sube. ¿Demuestra que el nuevo embedding es mejor?

> [!answer]- Solución
> No. El resultado corresponde al conjunto de cambios. Para atribuir un efecto necesitas una comparación que controle las otras condiciones, o experimentos adicionales que separen intervenciones.

## 18. Una pregunta global

Recuperaste cinco párrafos sobre becas. El usuario pregunta por todos los requisitos comunes a diez reglamentos. ¿Puedes afirmar que no hay otros requisitos?

> [!answer]- Solución
> No solo a partir de esos cinco párrafos. La ausencia en una selección local no prueba ausencia en todos los documentos. Necesitas una estrategia que cubra las fuentes y verifique la síntesis.

## Recordatorio para explicar de memoria

1. **Ingesta:** compruebo qué texto existe realmente para el sistema.
2. **Fragmentación:** conservo evidencia dentro del presupuesto del encoder.
3. **Recuperación:** distingo cercanía de relevancia y suficiencia.
4. **Referencia:** declaro corpus, preguntas, anclas y etiquetas.
5. **Métricas:** calculo presencia y orden con denominadores claros.
6. **Abstención:** mido tanto la prudencia como el silencio indebido.
7. **Generación:** reviso afirmaciones, condiciones y citas.
8. **Extensión:** pruebo una hipótesis y conservo los resultados comparables.

**Fuente:** síntesis de [[sesion-10.pdf]] y de las notas 50–57. Los ejercicios y soluciones son elaboraciones propias.
