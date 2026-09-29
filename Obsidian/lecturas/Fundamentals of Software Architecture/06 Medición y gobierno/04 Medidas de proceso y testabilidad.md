---
title: "06 · Proceso: testabilidad, cobertura y desplegabilidad"
created: 2026-09-28
tags:
  - lecturas/software-architecture
  - arquitectura/medicion
---

# Proceso: testabilidad, cobertura y desplegabilidad

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|← Índice del capítulo]]

> [!info] Fuente y alcance
> *Fundamentals of Software Architecture*, capítulo 6. **PDF 6 y 12 · impresas 86 y 92** del [[Obsidian/lecturas/Fundamentals of Software Architecture/Materiales/04 Medición y gobierno.pdf|PDF conservado]]. «Libro» identifica sus planteamientos; las ampliaciones, plantillas y datos supuestos se señalan como elaboración didáctica.

La arquitectura también condiciona el trabajo diario. Probar un módulo aislado suele ser más sencillo que arrancar todo un sistema para verificar una regla pequeña. Desplegar una parte independiente puede ser más rápido que coordinar múltiples equipos. Por eso una preocupación de proceso puede conducir a decisiones estructurales.

## Agilidad como característica compuesta

El libro usa la agilidad como ejemplo de cualidad compuesta que incluye testabilidad y desplegabilidad. No existe un único contador que capture toda esa capacidad. La estrategia es descomponerla y observar dimensiones relevantes para las prioridades del equipo.

**Testabilidad** se refiere a la facilidad de preparar condiciones, ejecutar comportamiento y observar resultados. **Desplegabilidad** se relaciona con introducir cambios de forma eficaz. La modularidad y el aislamiento pueden favorecer ambas, pero requieren límites reales: si un módulo necesita acceder a los detalles internos de otros cinco, tener carpetas separadas no basta.

## Qué muestra la cobertura

Las herramientas de cobertura indican qué partes del código fueron ejecutadas por las pruebas, según la modalidad de medición: líneas, instrucciones o ramas. El capítulo utiliza la cobertura para ilustrar que puede medirse algo objetivo sin capturar toda la cualidad deseada.

![Diferencia entre ejecutar código, comprobar resultados y detectar defectos](../Recursos%20visuales/Cap%C3%ADtulos%206%20a%208/c06-09-cobertura.png)

**Procedencia:** diagrama propio a partir de los argumentos de las pp. 86 y 92.

La fila superior separa tres pasos: ejecutar código, comprobar un resultado y detectar un defecto. Las flechas señalan la progresión deseada, no una equivalencia lógica. Abajo se compara una llamada sin verificación con una prueba que contrasta el resultado esperado.

**Causalidad:** la llamada `calcularTotal(2,10)` puede ejecutar todas las líneas aun cuando devuelva 999. La aserción contra 20 convierte ese error en un fallo visible. Una **aserción** es una comprobación que hace fallar la prueba cuando no se cumple la condición esperada; por ejemplo, `assert calcularTotal(2, 10) == 20` en Python. Pero una aserción siempre verdadera, como `assert True`, tampoco representa la intención del caso.

**Conclusión:** cobertura alta identifica código ejercitado, no demuestra corrección. **Límites:** una aserción válida puede ser insuficiente para casos negativos, límites numéricos, concurrencia o integración. El dibujo usa una función simple y no caracteriza toda una estrategia de pruebas.

### Ejemplo calculado

Supongamos 100 líneas ejecutables y una suite que toca 92: cobertura de líneas = `92/100 × 100 = 92 %`. Si la suite no compara resultados, puede no detectar errores de cálculo. Una segunda suite cubre 88 líneas y verifica invariantes relevantes; no podemos decidir cuál aporta más confianza mirando exclusivamente 92 % frente a 88 %. Hay que estudiar qué partes se omiten y qué defectos detecta cada prueba.

Como ampliación didáctica, las pruebas de mutación introducen cambios controlados en el código para observar si la suite los detecta. Son otra evidencia posible, no un requisito del capítulo ni una certificación absoluta. Lo esencial aquí es mantener alineada la medición con la intención.

## Métricas de desplegabilidad que enumera el libro

| Dimensión | Pregunta que ayuda a responder | Riesgo de interpretación |
|---|---|---|
| Porcentaje de despliegues exitosos | ¿Con qué frecuencia termina bien un cambio? | Definir éxito solo como proceso terminado puede ocultar incidentes posteriores |
| Duración del despliegue | ¿Cuánto tarda introducir la versión? | El promedio mezcla despliegues pequeños y migraciones extraordinarias |
| Problemas o errores asociados | ¿Qué efectos adversos introduce el despliegue? | La atribución puede ser difícil si se despliegan varios cambios a la vez |

**Ejemplo supuesto:** de 20 despliegues mensuales, 18 no necesitan reversión ni corrección urgente: tasa de éxito definida así = 90 %. Si los 18 duran 5 minutos y los otros 2 duran 35, la duración media es `(18×5+2×35)/20 = 8` minutos. Decir solamente «desplegamos en ocho minutos» oculta los dos casos problemáticos.

No existe una cifra buena aislada del contexto. Un despliegue regulado con migración y validación extensa no se compara directamente con publicar una página estática. La ventana, el tamaño del cambio y los criterios de éxito deben acompañar al número.

## Del problema de proceso a una decisión arquitectónica

Si un cambio de pedidos obliga a desplegar inventario y pagos juntos, una hipótesis razonable es que existe acoplamiento en contratos, datos o dependencias. Investigar esos límites puede orientar una mejora de modularidad. La secuencia es: **dificultad observada → causa probable → cambio estructural → nueva medición**.

No se debe saltar de «el despliegue tarda» a «necesitamos microservicios». Quizá el cuello de botella es una aprobación manual, pruebas inestables o una migración lenta. Separar procesos podría aumentar la coordinación sin eliminar esa causa. Este razonamiento es una ampliación para aplicar con cuidado el vínculo entre proceso y estructura del libro.

## Ejercicio resuelto

**Enunciado:** se impone 100 % de cobertura y el equipo añade pruebas sin aserciones. La métrica mejora. ¿Mejoró la testabilidad?

**Respuesta:** la cifra muestra más ejecución, pero no evidencia más capacidad de detectar errores. El libro explica que el equipo puede optimizar el indicador y perder su propósito. Una regla que exige alguna aserción previene omisiones sencillas, pero también es insuficiente: una aserción vacía de significado cumple formalmente. Revisar intención, resultados esperados y riesgo de los comportamientos sigue siendo necesario.

---

[[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/03 Complejidad ciclomática|← Anterior]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/00 Índice|Índice]] · [[Obsidian/lecturas/Fundamentals of Software Architecture/06 Medición y gobierno/05 Gobierno y funciones de aptitud|Siguiente →]]
